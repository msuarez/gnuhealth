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
from orthanc_rest_client import Orthanc as RestClient
import pendulum
from requests.auth import HTTPBasicAuth as auth
from requests.exceptions import HTTPError, ConnectionError
from datetime import datetime
import logging

__all__=['OrthancServerConfig', 'OrthancPatient', 'OrthancStudy', 'Orthanc']

logger = logging.getLogger(__name__)

class OrthancServerConfig(ModelSQL, ModelView):
    '''Orthanc server details'''

    __name__ = 'gnuhealth.orthanc.config'
    _rec_name = 'label'

    label = fields.Char('Label', required=True, help="Label for server (eg., remote1)")
    domain = fields.Char('URL', required=True, help="The full URL of the Orthanc server")
    user = fields.Char('Username', required=True, help="Username for Orthanc REST server")
    password = fields.Char('Password', required=True, help="Password for Orthanc REST server")
    last = fields.BigInteger('Last Index', readonly=True, help="Index of last change")
    sync_time = fields.DateTime('Sync Time', readonly=True, help="Time of last server sync")
    confirmed = fields.Boolean('Confirmed', help="The server details have been successfully checked")
    since_sync = fields.Function(fields.TimeDelta('Since last sync', help="Time since last sync"), 'get_since_sync')
    since_sync_readable = fields.Function(fields.Char('Since last sync', help="Time since last sync"), 'get_since_sync_readable')
    patients = fields.One2Many('gnuhealth.orthanc.patient', 'server', 'Patients')
    studies = fields.One2Many('gnuhealth.orthanc.study', 'server', 'Studies')

    @classmethod
    def __setup__(cls):
       super(OrthancServerConfig, cls).__setup__()
       t = cls.__table__()
       cls._sql_constraints = [
               ('label_unique', Unique(t, t.label), 'The label must be unique.'),
               ]
       cls._buttons.update({
              'do_sync': {},
              'do_full_sync': {},
              })

    @classmethod
    @ModelView.button
    def do_sync(cls, servers):
        cls.sync(servers)

    @classmethod
    @ModelView.button
    def do_full_sync(cls, servers):
        cls.full_sync(servers)

    @classmethod
    def sync(cls, servers=None):
        """Sync from changes endpoint"""

        pool = Pool()
        patient = pool.get('gnuhealth.orthanc.patient')
        study = pool.get('gnuhealth.orthanc.study')

        if not servers:
            servers = cls.search(['domain', '!=', None])

        logger.info('Starting sync')
        for server in servers:
            logger.info('Getting new changes for <{}>'.format(server.label))
            orthanc = RestClient(server.domain, auth=auth(server.user, server.password))
            curr = server.last
            new_studies = []
            update_studies = []
            new_patients = []
            update_patients = []
            while True:
                changes = orthanc.get_changes(since=curr)
                for change in changes['Changes']:
                    if change['ChangeType'] == 'NewStudy':
                        new_studies.append(orthanc.get_study(change['ID']))
                    elif change['ChangeType'] == 'StableStudy':
                        update_studies.append(orthanc.get_study(change['ID']))
                    elif change['ChangeType'] == 'NewPatient':
                        new_patients.append(orthanc.get_patient(change['ID']))
                    elif change['ChangeType'] == 'StablePatient':
                        update_patients.append(orthanc.get_patient(change['ID']))
                    else:
                        pass
                curr = changes['Last']
                if changes['Done'] == True:
                    logger.info('<{}> at newest change'.format(server.label))
                    break
            patient.create_patients(new_patients, server)
            study.create_studies(new_studies, server)
            server.last = curr
            server.sync_time = datetime.now()
            logger.info('{} sync complete: {} new patients, {} new studies'.format(server.label, len(new_patients), len(new_studies)))
        cls.save(servers)

    @classmethod
    def full_sync(cls, servers=None):
        """Import and create all current patients and studies on remote DICOM server

                 Used as first sync on adding new server
        """

        pool = Pool()
        Patient = pool.get('gnuhealth.orthanc.patient')
        Study = pool.get('gnuhealth.orthanc.study')

        if not servers:
            servers = cls.search(['domain', '!=', None])

        for server in servers:
            logger.info('Full sync for <{}>'.format(server.label))
            orthanc = RestClient(server.domain, auth=auth(server.user, server.password))
            try:
                patients = [p for p in orthanc.get_patients(params={'expand': ''})]
                studies = [s for s in orthanc.get_studies(params={'expand': ''})]
            except HTTPError as err:
                if err.response.status_code == 401:
                    cls.raise_user_error("Invalid credentials for {}".format(server.label))
                else:
                    cls.raise_user_error("Invalid domain {}".format(server.domain))
            except:
                cls.raise_user_error("Invalid domain {}".format(server.domain))
            else:
                Patient.create_patients(patients, server)
                Study.create_studies(studies, server)
                server.last = orthanc.get_changes(last=True).get('Last')
                server.sync_time = datetime.now()
                server.confirmed = True
                logger.info('<{}> sync complete: {} new patients, {} new studies'.format(server.label, len(patients), len(studies)))
            finally:
                pass
        cls.save(servers)

    @staticmethod
    def quick_check(domain, user, password):
        """Confirm server details"""

        try:
            orthanc = RestClient(domain, auth=auth(user, password))
            orthanc.get_changes(last=True)
        except:
            return False
        else:
            return True

    @fields.depends('domain', 'user', 'password')
    def on_change_with_confirmed(self):
        return self.quick_check(self.domain, self.user, self.password)

    def get_since_sync(self, name):
        return datetime.now() - self.sync_time

    def get_since_sync_readable(self, name):
        try:
            d = pendulum.now() - pendulum.instance(self.sync_time)
            return d.in_words(Transaction().language)
        except:
            return ''

class OrthancPatient(ModelSQL, ModelView):
    '''Orthanc patient information'''

    __name__ = 'gnuhealth.orthanc.patient'

    patient = fields.Many2One('gnuhealth.patient', 'Patient', help="Local linked patient")
    name = fields.Char('PatientName', readonly=True)
    bd = fields.Date('Birthdate', readonly=True)
    ident = fields.Char('PatientID', readonly=True)
    uuid = fields.Char('PatientUUID', readonly=True, required=True)
    studies = fields.One2Many('gnuhealth.orthanc.study', 'patient', 'Studies', readonly=True)
    server = fields.Many2One('gnuhealth.orthanc.config', 'Server', readonly=True)

    @staticmethod
    def get_info_from_dicom(patients):
        """Extract information for writing to database"""

        data = []
        for patient in patients:
            try:
                bd = datetime.strptime(patient['MainDicomTags']['PatientBirthDate'], '%Y%m%d').date()
            except:
                bd = None
            data.append({
                    'name': patient.get('MainDicomTags').get('PatientName'),
                    'bd': bd,
                    'ident': patient.get('MainDicomTags').get('PatientID'),
                    'uuid': patient.get('ID'),
                    })
        return data

    @classmethod
    def update_patients(cls, patients, server):
        pass

    @classmethod
    def create_patients(cls, patients, server):
        """Create patients"""

        pool = Pool()
        Patient = pool.get('gnuhealth.patient')

        entries = cls.get_info_from_dicom(patients)
        for entry in entries:
            try:
                g_patient = Patient.search([('puid', '=', entry['ident'])], limit=1)[0]
                logger.info('Matching PUID found for {}'.format(entry['uuid']))
            except:
                g_patient = None
            entry['server'] = server
            entry['patient'] = g_patient
        cls.create(entries)

class OrthancStudy(ModelSQL, ModelView):
    '''Orthanc study'''

    __name__ = 'gnuhealth.orthanc.study'

    patient = fields.Many2One('gnuhealth.orthanc.patient', 'Patient', readonly=True)
    uuid = fields.Char('UUID', readonly=True, required=True)
    description = fields.Char('Description', readonly=True)
    date = fields.Date('Date', readonly=True)
    ident = fields.Char('ID', readonly=True)
    institution = fields.Char('Institution', readonly=True, help="Imaging center where study was undertaken")
    ref_phys = fields.Char('Referring Physician', readonly=True)
    req_phys = fields.Char('Requesting Physician', readonly=True)
    server = fields.Many2One('gnuhealth.orthanc.config', 'Server', readonly=True)

    def get_rec_name(self, name):
        return ': '.join((self.ident or self.uuid, self.description or ''))

    @staticmethod
    def get_info_from_dicom(studies):
        """Extract information for writing to database"""

        data = []

        for study in studies:
            try:
                date = datetime.strptime(study['MainDicomTags']['StudyDate'], '%Y%m%d').date()
            except:
                date = None
            try:
                description = study['MainDicomTags']['RequestedProcedureDescription']
            except:
                description = None
            data.append({
                'parent_patient': study['ParentPatient'],
                'uuid': study['ID'],
                'description': description,
                'date': date,
                'ident': study.get('MainDicomTags').get('StudyID'),
                'institution': study.get('MainDicomTags').get('InstitutionName'),
                'ref_phys': study.get('MainDicomTags').get('ReferringPhysicianName'),
                'req_phys': study.get('MainDicomTags').get('RequestingPhysician'),
                })
        return data

    @classmethod
    def update_studies(cls, studies, server):
        pass

    @classmethod
    def create_studies(cls, studies, server):
        """Create studies"""

        pool = Pool()
        Patient = pool.get('gnuhealth.orthanc.patient')

        entries = cls.get_info_from_dicom(studies)
        for entry in entries:
            try:
                patient = Patient.search([('uuid', '=', entry['parent_patient']),
                                            ('server', '=', server)], limit=1)[0]
            except:
                patient = None
                logger.warning('No parent patient found for study {}'.format(entry['ID']))
            entry.pop('parent_patient')
            entry['server'] = server
            entry['patient'] = patient
        cls.create(entries)

class Orthanc(ModelSQL, ModelView):
    '''Add Orthanc patient(s) to the main patient data'''

    __name__ = 'gnuhealth.patient'

    orthanc_patients = fields.One2Many('gnuhealth.orthanc.patient', 'patient', 'Orthanc patients')
