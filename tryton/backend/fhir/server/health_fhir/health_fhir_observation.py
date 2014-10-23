from flask import current_app
from StringIO import StringIO
from datetime import datetime
from .datastore import find_record
import fhir as supermod
from utils import get_address
import sys

#TODO Put restrictions on code values (interp, status, reliability, etc)

class health_Observation(supermod.Observation):
    def set_gnu_observation(self, obs):
        """Set gnu observation"""
        self.gnu_obs = obs

    def import_from_gnu_observation(self):
        """Imports Health values into
            Observation structure"""
        if self.gnu_obs:
            self.__set_gnu_identifier()
            self.__set_gnu_subject()
            self.__set_gnu_comments()
            self.__set_gnu_valueQuantity()
            self.__set_gnu_referenceRange()
            self.__set_gnu_interpretation()
            self.__set_gnu_status()
            self.__set_gnu_reliability()

    def set_applies_date_time(self):
        pass

    def set_applies_period(self):
        pass

    def __set_gnu_comments(self):
        if getattr(self, 'gnu_obs'):
            comments = self.gnu_obs.remarks
            if comments:
                self.set_comments(comments)

    def set_comments(self, comments):
        """Set comments"""
        if comments:
            m = supermod.string(value=str(comments))
            super(health_Observation, self).set_comments(m)

    def __set_gnu_identifier(self):
        if getattr(self, 'gnu_obs'):
            id = self.gnu_obs.id
            analyte = self.gnu_obs.name
            patient = self.gnu_obs.gnuhealth_lab_id.patient.name.rec_name
            time = self.gnu_obs.gnuhealth_lab_id.date_analysis.strftime('%Y/%m/%d')
            if id and analyte and patient and time:
                ident = supermod.Identifier(
                            label=supermod.string(value='{0} value for {1} on {2}'.format(analyte, patient, time)),
                            system=supermod.uri(value='gnuhealth::0'), #TODO
                            value=supermod.string(value=str(id)))
                self.set_identifier(ident)


    def set_identifier(self, identifier):
        """Set identifier"""
        if identifier:
            super(health_Observation, self).set_identifier(identifier)

    def __set_gnu_interpretation(self):
        # TODO: Interpretation is complicated
        if self.gnu_obs:
            interp = supermod.CodeableConcept()
            interp.coding = [supermod.Coding()]
            if self.gnu_obs.result < self.gnu_obs.lower_limit:
                value = 'L'
                display = 'Low'
            elif self.gnu_obs.result > self.gnu_obs.lower_limit:
                value = 'H'
                display = 'High'
            else:
                value = 'N'
                display = 'Normal'
            interp.coding[0].system = supermod.uri(value='http://hl7.org/fhir/v2/0078')
            interp.coding[0].code = supermod.code(value=value)
            interp.coding[0].display = supermod.string(value=display)
            self.set_interpretation(interp)

    def set_interpretation(self, interpretation):
        """Set interpretation"""
        if interpretation:
            super(health_Observation, self).set_interpretation(interpretation)

    def set_issued(self):
        if self.gnu_obs:
            pass


    def set_method(self):
        pass

    def set_name(self):
        pass

    def set_performer(self):
        pass

    def __set_gnu_referenceRange(self):
        if self.gnu_obs:
            ref = health_Observation_ReferenceRange()
            #ref.age = supermod.Range() #Not relevant, usually
            ref.low = supermod.Quantity()
            ref.low.units = supermod.string(value=self.gnu_obs.units.name)
            ref.low.value = supermod.decimal(value=self.gnu_obs.lower_limit)
            ref.high = supermod.Quantity()
            ref.high.units = supermod.string(value=self.gnu_obs.units.name)
            ref.high.value = supermod.decimal(value=self.gnu_obs.upper_limit)
            ref.meaning = supermod.Coding()
            ref.meaning.system = supermod.uri(value='http://hl7.org/fhir/referencerange-meaning')
            ref.meaning.code = supermod.code(value='normal')
            ref.meaning.display = supermod.string(value='Normal range')
            self.set_referenceRange([ref])

    def set_referenceRange(self, ranges):
        """Set reference range"""
        if ranges:
            super(health_Observation, self).set_referenceRange(ranges)

    def set_related(self):
        pass

    def __set_gnu_reliability(self):
        if self.gnu_obs:
            rel = health_ObservationReliability()
            rel.value = 'ok'
            self.set_reliability(rel)

    def set_reliability(self, rel):
        '''Set reliability; mandatory'''
        if rel:
            super(health_Observation, self).set_reliability(rel)

    def set_specimen(self):
        pass

    def __set_gnu_status(self):
        if self.gnu_obs:
            s = health_ObservationStatus()
            s.value = 'final'
            self.set_status(s)

    def set_status(self, status):
        '''Set status; mandatory'''
        if status:
            super(health_Observation, self).set_status(status)

    def __set_gnu_valueQuantity(self):
        if self.gnu_obs:
            q = supermod.Quantity()
            q.value = supermod.decimal(value=self.gnu_obs.result)
            q.units = supermod.string(value=self.gnu_obs.units.name)
            self.set_valueQuantity(q)

    def set_valueQuantity(self, quantity):
        """Set actual value of observation"""
        if quantity:
            super(health_Observation, self).set_valueQuantity(quantity)

    def __set_gnu_subject(self):
        if self.gnu_obs:
            patient = self.gnu_obs.gnuhealth_lab_id.patient
            uri = ''.join(['/Patient/', str(patient.id)])
            display = patient.rec_name
            ref=supermod.ResourceReference()
            ref.display = supermod.string(value=display)
            ref.reference = supermod.string(value=uri)
            self.set_subject(ref)

    def set_subject(self, subject):
        """Set subject (usually patient)"""
        if subject:
            super(health_Observation, self).set_subject(subject)

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
