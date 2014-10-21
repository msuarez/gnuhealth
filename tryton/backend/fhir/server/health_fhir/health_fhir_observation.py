from flask import current_app
from StringIO import StringIO
from datetime import datetime
from .datastore import find_record
import fhir as supermod
from utils import get_address
import sys

class health_Observation(supermod.Observation):
    def set_gnu_observation(self, obs):
        self.gnu_obs = obs

    def import_from_gnu_observation(self):
        if self.gnu_obs:
            self.set_identifier()
            self.set_comments()

    def set_applies_date_time():
        pass

    def set_applies_period():
        pass

    def set_comments(self):
        if getattr(self, 'gnu_obs'):
            comments = self.gnu_obs.remarks
            if comments:
                m = supermod.string(value=str(comments))
                super(health_Observation, self).set_comments(m)

    def set_identifier(self):
        if getattr(self, 'gnu_obs'):
            id = self.gnu_obs.id
            analyte = self.gnu_obs.name
            patient = self.gnu_obs.gnuhealth_lab_id.patient.name
            time = self.gnu_obs.gnuhealth_lab_id.date_analysis.strftime('%Y/%m/%d')
            if id and analyte and patient and time:
                ident = supermod.Identifier(
                            label=supermod.string(value='{0} value for {1} on {2}'.format(analyte, patient, time)),
                            system=supermod.uri(value='gnuhealth::0'), #TODO
                            value=supermod.string(value=str(id)))
                super(health_Observation, self).set_identifier(ident)

    def set_interpretation():
        pass

    def set_issued():
        pass

    def set_method():
        pass

    def set_name():
        pass

    def set_performer():
        pass

    def set_reference_range():
        pass

    def set_related():
        pass

    def set_reliability():
        pass

    def set_specimen():
        pass

    def set_status():
        pass

    def set_subject():
        pass

class health_Observation_ReferenceRange(supermod.Observation_ReferenceRange):
    pass

class health_Observation_Related(supermod.Observation_Related):
    pass

class health_ObservationReliability(supermod.ObservationReliability):
    pass

class health_ObservationStatus(supermod.ObservationStatus):
    pass

class health_ObservationRelationshipType(supermod.ObservationRelationshipType):
    pass
