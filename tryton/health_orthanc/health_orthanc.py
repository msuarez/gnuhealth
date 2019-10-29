# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from trytond.model import ModelView, ModelSQL, fields, Unique
from trytond.pool import Pool
from trytond.transaction import Transaction
from beren import Orthanc as RestClient
from requests.auth import HTTPBasicAuth as auth
from datetime import datetime
from urllib.parse import urljoin
import logging
import pendulum

__all__ = [
    "OrthancServerConfig",
    "OrthancPatient",
    "OrthancStudy",
    "Patient",
    "TestResult",
]

logger = logging.getLogger(__name__)


class OrthancServerConfig(ModelSQL, ModelView):
    """Orthanc server details"""

    __name__ = "gnuhealth.orthanc.config"
    _rec_name = "label"

    label = fields.Char("Label", required=True, help="Label for server (eg., remote1)")
    domain = fields.Char(
        "URL", required=True, help="The full URL of the Orthanc server"
    )
    user = fields.Char(
        "Username", required=True, help="Username for Orthanc REST server"
    )
    password = fields.Char(
        "Password", required=True, help="Password for Orthanc REST server"
    )
    last = fields.BigInteger("Last Index", readonly=True, help="Index of last change")
    sync_time = fields.DateTime(
        "Sync Time", readonly=True, help="Time of last server sync"
    )
    validated = fields.Boolean(
        "Validated", help="Whether the server details have been successfully checked"
    )
    since_sync = fields.Function(
        fields.TimeDelta("Since last sync", help="Time since last sync"),
        "get_since_sync",
    )
    since_sync_readable = fields.Function(
        fields.Char("Since last sync", help="Time since last sync"),
        "get_since_sync_readable",
    )
    patients = fields.One2Many("gnuhealth.orthanc.patient", "server", "Patients")
    studies = fields.One2Many("gnuhealth.orthanc.study", "server", "Studies")
    link = fields.Function(
        fields.Char("URL", help="Link to server in Orthanc Explorer"), "get_link"
    )

    def get_link(self, name):
        pre = "".join([self.domain.rstrip("/"), "/"])
        add = "app/explorer.html"
        return urljoin(pre, add)

    @classmethod
    def __setup__(cls):
        super().__setup__()
        t = cls.__table__()
        cls._sql_constraints = [
            ("label_unique", Unique(t, t.label), "The label must be unique.")
        ]
        cls._buttons.update({"do_sync": {}})

    @classmethod
    @ModelView.button
    def do_sync(cls, servers):
        cls.sync(servers)

    @classmethod
    def sync(cls, servers=None):
        """Sync from changes endpoint"""

        pool = Pool()
        patient = pool.get("gnuhealth.orthanc.patient")
        study = pool.get("gnuhealth.orthanc.study")

        if not servers:
            servers = cls.search([("domain", "!=", None), ("validated", "=", True)])

        logger.info("Starting sync")
        for server in servers:
            if not server.validated:
                continue
            logger.info("Getting new changes for <{}>".format(server.label))
            orthanc = RestClient(server.domain, auth=auth(server.user, server.password))
            curr = server.last
            new_patients = set()
            update_patients = set()
            new_studies = set()
            update_studies = set()

            while True:
                try:
                    changes = orthanc.get_changes(since=curr)
                except:
                    server.validated = False
                    logger.exception("Invalid details for <{}>".format(server.label))
                    break
                for change in changes["Changes"]:
                    type_ = change["ChangeType"]
                    if type_ == "NewStudy":
                        new_studies.add(change["ID"])
                    elif type_ == "StableStudy":
                        update_studies.add(change["ID"])
                    elif type_ == "NewPatient":
                        new_patients.add(change["ID"])
                    elif type_ == "StablePatient":
                        update_patients.add(change["ID"])
                    else:
                        pass
                curr = changes["Last"]
                if changes["Done"] == True:
                    logger.info("<{}> at newest change".format(server.label))
                    break

            update_patients -= new_patients
            update_studies -= new_studies
            if new_patients:
                patient.create_patients(
                    [orthanc.get_patient(p) for p in new_patients], server
                )
            if update_patients:
                patient.update_patients(
                    [orthanc.get_patient(p) for p in update_patients], server
                )
            if new_studies:
                study.create_studies(
                    [orthanc.get_study(s) for s in new_studies], server
                )
            if update_studies:
                study.update_studies(
                    [orthanc.get_study(s) for s in update_studies], server
                )
            server.last = curr
            server.sync_time = datetime.now()
            logger.info(
                "<{}> sync complete: {} new patients, {} update patients, {} new studies, {} updated studies".format(
                    server.label,
                    len(new_patients),
                    len(update_patients),
                    len(new_studies),
                    len(update_studies),
                )
            )
        cls.save(servers)

    @staticmethod
    def quick_check(domain, user, password):
        """Validate the server details"""

        try:
            orthanc = RestClient(domain, auth=auth(user, password))
            orthanc.get_changes(last=True)
        except:
            return False
        else:
            return True

    @fields.depends("domain", "user", "password")
    def on_change_with_validated(self):
        return self.quick_check(self.domain, self.user, self.password)

    def get_since_sync(self, name):
        return datetime.now() - self.sync_time

    def get_since_sync_readable(self, name):
        try:
            d = pendulum.now() - pendulum.instance(self.sync_time)
            return d.in_words(Transaction().language)
        except:
            return ""


class OrthancPatient(ModelSQL, ModelView):
    """Orthanc patient information"""

    __name__ = "gnuhealth.orthanc.patient"

    patient = fields.Many2One(
        "gnuhealth.patient", "Patient", help="Local linked patient"
    )
    name = fields.Char("PatientName", readonly=True)
    bd = fields.Date("Birthdate", readonly=True)
    ident = fields.Char("PatientID", readonly=True)
    uuid = fields.Char("PatientUUID", readonly=True, required=True)
    studies = fields.One2Many(
        "gnuhealth.orthanc.study", "patient", "Studies", readonly=True
    )
    server = fields.Many2One("gnuhealth.orthanc.config", "Server", readonly=True)
    link = fields.Function(
        fields.Char("URL", help="Link to patient in Orthanc Explorer"), "get_link"
    )

    def get_link(self, name):
        pre = "".join([self.server.domain.rstrip("/"), "/"])
        add = "app/explorer.html#patient?uuid={}".format(self.uuid)
        return urljoin(pre, add)

    @classmethod
    def __setup__(cls):
        super().__setup__()
        t = cls.__table__()
        cls._sql_constraints = [
            (
                "uuid_unique",
                Unique(t, t.server, t.uuid),
                "UUID must be unique for a given server",
            )
        ]

    @staticmethod
    def get_info_from_dicom(patients):
        """Extract information for writing to database"""

        data = []
        for patient in patients:
            try:
                bd = datetime.strptime(
                    patient["MainDicomTags"]["PatientBirthDate"], "%Y%m%d"
                ).date()
            except:
                bd = None
            data.append(
                {
                    "name": patient.get("MainDicomTags").get("PatientName"),
                    "bd": bd,
                    "ident": patient.get("MainDicomTags").get("PatientID"),
                    "uuid": patient.get("ID"),
                }
            )
        return data

    @classmethod
    def update_patients(cls, patients, server):
        """Update patients"""

        Patient = pool.get("gnuhealth.patient")

        entries = cls.get_info_from_dicom(patients)
        updates = []
        for entry in entries:
            try:
                patient = cls.search(
                    [("uuid", "=", entry["uuid"]), ("server", "=", server)], limit=1
                )[0]
                patient.name = entry["name"]
                patient.bd = entry["bd"]
                patient.ident = entry["ident"]
                if not patient.patient:  # don't update unless no patient attached
                    try:
                        g_patient = Patient.search(
                            [("puid", "=", entry["ident"])], limit=1
                        )[0]
                        patient.patient = g_patient
                        logger.info(
                            "New Matching PUID found for {}".format(entry["ident"])
                        )
                    except:
                        pass
                updates.append(patient)
                logger.info("Updating patient {}".format(entry["uuid"]))
            except:
                continue
                logger.warning("Unable to update patient {}".format(entry["uuid"]))
        cls.save(updates)

    @classmethod
    def create_patients(cls, patients, server):
        """Create patients"""

        pool = Pool()
        Patient = pool.get("gnuhealth.patient")

        entries = cls.get_info_from_dicom(patients)
        for entry in entries:
            try:
                g_patient = Patient.search([("puid", "=", entry["ident"])], limit=1)[0]
                logger.info("Matching PUID found for {}".format(entry["uuid"]))
            except:
                g_patient = None
            entry["server"] = server
            entry["patient"] = g_patient
        cls.create(entries)


class OrthancStudy(ModelSQL, ModelView):
    """Orthanc study"""

    __name__ = "gnuhealth.orthanc.study"

    patient = fields.Many2One("gnuhealth.orthanc.patient", "Patient", readonly=True)
    uuid = fields.Char("UUID", readonly=True, required=True)
    description = fields.Char("Description", readonly=True)
    date = fields.Date("Date", readonly=True)
    ident = fields.Char("ID", readonly=True)
    institution = fields.Char(
        "Institution", readonly=True, help="Imaging center where study was undertaken"
    )
    ref_phys = fields.Char("Referring Physician", readonly=True)
    req_phys = fields.Char("Requesting Physician", readonly=True)
    server = fields.Many2One("gnuhealth.orthanc.config", "Server", readonly=True)
    link = fields.Function(
        fields.Char("URL", help="Link to study in Orthanc Explorer"), "get_link"
    )
    imaging_test = fields.Many2One("gnuhealth.imaging.test.result", "Test")

    def get_link(self, name):
        pre = "".join([self.server.domain.rstrip("/"), "/"])
        add = "app/explorer.html#study?uuid={}".format(self.uuid)
        return urljoin(pre, add)

    @classmethod
    def __setup__(cls):
        super().__setup__()
        t = cls.__table__()
        cls._sql_constraints = [
            (
                "uuid_unique",
                Unique(t, t.server, t.uuid),
                "UUID must be unique for a given server",
            )
        ]

    def get_rec_name(self, name):
        return ": ".join((self.ident or self.uuid, self.description or ""))

    @staticmethod
    def get_info_from_dicom(studies):
        """Extract information for writing to database"""

        data = []

        for study in studies:
            try:
                date = datetime.strptime(
                    study["MainDicomTags"]["StudyDate"], "%Y%m%d"
                ).date()
            except:
                date = None
            try:
                description = study["MainDicomTags"]["RequestedProcedureDescription"]
            except:
                description = None
            data.append(
                {
                    "parent_patient": study["ParentPatient"],
                    "uuid": study["ID"],
                    "description": description,
                    "date": date,
                    "ident": study.get("MainDicomTags").get("StudyID"),
                    "institution": study.get("MainDicomTags").get("InstitutionName"),
                    "ref_phys": study.get("MainDicomTags").get(
                        "ReferringPhysicianName"
                    ),
                    "req_phys": study.get("MainDicomTags").get("RequestingPhysician"),
                }
            )
        return data

    @classmethod
    def update_studies(cls, studies, server):
        """Update studies"""

        entries = cls.get_info_from_dicom(studies)
        updates = []
        for entry in entries:
            try:
                study = cls.search(
                    [("uuid", "=", entry["uuid"]), ("server", "=", server)], limit=1
                )[0]
                study.description = entry["description"]
                study.date = entry["date"]
                study.ident = entry["ident"]
                study.institution = entry["institution"]
                study.ref_phys = entry["ref_phys"]
                study.req_phys = entry["req_phys"]
                updates.append(study)
                logger.info("Updating study {}".format(entry["uuid"]))
            except:
                continue
                logger.warning("Unable to update study {}".format(entry["uuid"]))
        cls.save(updates)

    @classmethod
    def create_studies(cls, studies, server):
        """Create studies"""

        pool = Pool()
        Patient = pool.get("gnuhealth.orthanc.patient")

        entries = cls.get_info_from_dicom(studies)
        for entry in entries:
            try:
                patient = Patient.search(
                    [("uuid", "=", entry["parent_patient"]), ("server", "=", server)],
                    limit=1,
                )[0]
            except:
                patient = None
                logger.warning(
                    "No parent patient found for study {}".format(entry["ID"])
                )
            entry.pop("parent_patient")  # remove non-model entry
            entry["server"] = server
            entry["patient"] = patient
        cls.create(entries)


class TestResult(ModelSQL, ModelView):
    """Add Orthanc imaging studies to imaging test result"""

    __name__ = "gnuhealth.imaging.test.result"

    studies = fields.One2Many(
        "gnuhealth.orthanc.study", "imaging_test", "Studies", readonly=True
    )


class Patient(ModelSQL, ModelView):
    """Add Orthanc patient(s) to the main patient data"""

    __name__ = "gnuhealth.patient"

    orthanc_patients = fields.One2Many(
        "gnuhealth.orthanc.patient", "patient", "Orthanc patients"
    )
