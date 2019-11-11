# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#
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
from datetime import datetime
from trytond.model import ModelView, fields
from trytond.wizard import Wizard, StateTransition, StateView, Button
from trytond.transaction import Transaction
from trytond.pool import Pool
from requests.auth import HTTPBasicAuth as auth
from requests.exceptions import HTTPError
from beren import Orthanc as RestClient
import logging

logger = logging.getLogger(__name__)

__all__ = ["AddOrthancInit", "FullSyncOrthanc", "AddOrthancResult"]


class AddOrthancInit(ModelView):
    """Init Full Orthanc Sync"""

    __name__ = "gnuhealth.orthanc.add.init"

    label = fields.Char(
        "Label", required=True, help="The label of the Orthanc server. Must be unique"
    )
    domain = fields.Char(
        "URL", required=True, help="The full URL of the Orthanc server"
    )
    user = fields.Char(
        "Username", required=True, help="Username for Orthanc REST server"
    )
    password = fields.Char(
        "Password", required=True, help="Password for Orthanc REST server"
    )


class AddOrthancResult(ModelView):
    """Display Result"""

    __name__ = "gnuhealth.orthanc.add.result"

    result = fields.Text("Result", help="Information")


class FullSyncOrthanc(Wizard):
    "Full sync new orthanc server"
    __name__ = "gnuhealth.orthanc.wizard.full_sync"

    start = StateView(
        "gnuhealth.orthanc.add.init",
        "health_orthanc.view_orthanc_add_init",
        [
            Button("Cancel", "end", "tryton-cancel"),
            Button("Begin", "first_sync", "tryton-ok", default=True),
        ],
    )

    first_sync = StateTransition()
    result = StateView(
        "gnuhealth.orthanc.add.result",
        "health_orthanc.view_orthanc_add_result",
        [Button("Close", "end", "tryton-close")],
    )

    def transition_first_sync(self):
        """Import and create all current patients and studies on remote DICOM server
        """

        pool = Pool()
        Patient = pool.get("gnuhealth.orthanc.patient")
        Study = pool.get("gnuhealth.orthanc.study")
        Config = pool.get("gnuhealth.orthanc.config")

        orthanc = RestClient(
            self.start.domain, auth=auth(self.start.user, self.start.password)
        )
        try:
            patients = orthanc.get_patients(expand=True)
            studies = orthanc.get_studies(expand=True)
        except HTTPError as err:
            if err.response.status_code == 401:
                self.result.result = "Invalid credentials provided"
                logger.exception("Invalid credentials provided")
            else:
                self.result.result = "Invalid domain provided"
                logger.exception("Request returned error status code")
        except:
            self.result.result = "Invalid domain provided"
            logger.exception("Other error occurred")
        else:
            new_server = {
                "label": self.start.label,
                "domain": self.start.domain,
                "user": self.start.user,
                "password": self.start.password,
            }
            server, = Config.create([new_server])
            Patient.create_patients(patients, server)
            Study.create_studies(studies, server)
            server.last = orthanc.get_changes(last=True).get("Last")
            server.sync_time = datetime.now()
            server.validated = True
            Config.save([server])
            self.result.result = "Successfully added and synced <{}>".format(
                server.label
            )
            logger.info(
                "<{}> sync complete: {} new patients, {} new studies".format(
                    server.label, len(patients), len(studies)
                )
            )
        finally:
            return "result"

    def default_result(self, fields):
        return {"result": self.result.result}
