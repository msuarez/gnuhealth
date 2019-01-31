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
from orthanc_rest_client import Orthanc as RestClient
import pendulum
from requests.auth import HTTPBasicAuth as auth
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
              })

    @classmethod
    @ModelView.button
    def do_sync(cls, servers):
        cls.sync(servers)

    @classmethod
    def sync(cls, servers=None):
        pool = Pool()
        patient = pool.get('gnuhealth.orthanc.patient')
        study = pool.get('gnuhealth.orthanc.study')

        if not servers:
            servers = cls.search(['domain', '!=', None],)

        for server in servers:
            orthanc = RestClient(server.domain)
            a = auth(server.user, server.password)
            curr = server.last
            new_studies = []
            new_patients = []
            while True:
                logger.info('Getting new changes')
                changes = orthanc.get_changes(params={'since': curr}, auth=a)
                for change in changes['Changes']:
                    if change['ChangeType'] == 'NewStudy':
                        new_studies.append(orthanc.get_study(change['ID'], auth=a))
                        logger.info('New Study {}'.format(change['ID']))
                    elif change['ChangeType'] == 'NewPatient':
                        new_patients.append(orthanc.get_patient(change['ID'], auth=a))
                        logger.info('New Patient {}'.format(change['ID']))
                    else:
                        pass
                curr = changes['Last']
                if changes['Done'] == True:
                    logger.info('Up-to-date on changelog')
                    break
            logger.info('Creating patients and studies')
            patient.create_patients(new_patients, server)
            study.create_studies(new_studies, server)
            server.last = curr
            server.sync_time = datetime.now()
        cls.save(servers)
        logger.info('Sync complete: {} new patients, {} new studies'.format(len(new_patients), len(new_studies)))

    def get_since_sync(self, name):
        return datetime.now() - self.sync_time

    def get_since_sync_readable(self, name):
        try:
            d = pendulum.now() - pendulum.instance(self.sync_time)
            return d.in_words()
        except:
            return ''

class OrthancPatient(ModelSQL, ModelView):
    '''Orthanc patient information'''

    __name__ = 'gnuhealth.orthanc.patient'

    patient = fields.Many2One('gnuhealth.patient', 'Patient')
    name = fields.Char('PatientName', readonly=True)
    bd = fields.Date('Birthdate', readonly=True)
    ident = fields.Char('PatientID', readonly=True)
    uuid = fields.Char('PatientUUID', readonly=True, required=True)
    studies = fields.One2Many('gnuhealth.orthanc.study', 'patient', 'Studies', readonly=True)
    server = fields.Many2One('gnuhealth.orthanc.config', 'Server', readonly=True)

    @classmethod
    def create_patients(cls, patients, server=None):
        '''Add patients'''
        pool = Pool()
        Patient = pool.get('gnuhealth.patient')

        create = []
        for patient in patients:
            try:
                bd = datetime.strptime(patient['MainDicomTags']['PatientBirthDate'], '%Y%m%d').date()
            except:
                bd = None
            try:
                g_patient = Patient.search([('puid', '=', patient['MainDicomTags']['PatientID'])], limit=1)[0]
            except:
                g_patient = None
                logger.warning('No matching PUID found for {}'.format(patient['ID']))
            create.append({
                    'name': patient.get('MainDicomTags').get('PatientName'),
                    'bd': bd,
                    'ident': patient.get('MainDicomTags').get('PatientID'),
                    'uuid': patient.get('ID'),
                    'patient': g_patient,
                    'server': server,
                    })
        cls.create(create)

class OrthancStudy(ModelSQL, ModelView):
    '''Orthanc study'''

    __name__ = 'gnuhealth.orthanc.study'

    patient = fields.Many2One('gnuhealth.orthanc.patient', 'Patient', readonly=True)
    uuid = fields.Char('UUID', readonly=True, required=True)
    description = fields.Char('Description', readonly=True)
    date = fields.Date('Date', readonly=True)
    ident = fields.Char('ID', readonly=True)
    institution = fields.Char('Institution', readonly=True)
    ref_phys = fields.Char('Referring Physician', readonly=True)
    req_phys = fields.Char('Requesting Physician', readonly=True)
    server = fields.Many2One('gnuhealth.orthanc.config', 'Server', readonly=True)

    def get_rec_name(self, name):
        return ': '.join((self.ident or self.uuid, self.description or ''))

    @classmethod
    def create_studies(cls, studies, server=None):
        '''Add studies'''
        create = []
        pool = Pool()
        Patient = pool.get('gnuhealth.orthanc.patient')

        for study in studies:
            try:
                patient = Patient.search([('uuid', '=', study['ParentPatient'])], limit=1)[0]
            except:
                patient = None
                logger.warning('No parent patient found for study {}'.format(study['ID']))
            try:
                date = datetime.strptime(study['MainDicomTags']['StudyDate'], '%Y%m%d').date()
            except:
                date = None
            try:
                description = study['MainDicomTags']['RequestedProcedureDescription']
            except:
                description = None
            create.append({
                'patient': patient,
                'uuid': study['ID'],
                'description': description,
                'date': date,
                'ident': study.get('MainDicomTags').get('StudyID'),
                'institution': study.get('MainDicomTags').get('InstitutionName'),
                'ref_phys': study.get('MainDicomTags').get('ReferringPhysicianName'),
                'req_phys': study.get('MainDicomTags').get('RequestingPhysician'),
                'server': server,
                })
        cls.create(create)

class Orthanc(ModelSQL, ModelView):
    '''Add Orthanc patient(s) to the main patient data'''

    __name__ = 'gnuhealth.patient'

    orthanc_patients = fields.One2Many('gnuhealth.orthanc.patient', 'patient', 'Orthanc patients')
