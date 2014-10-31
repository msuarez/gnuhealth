from flask import current_app
from StringIO import StringIO
from datetime import datetime
from .datastore import find_record
from operator import attrgetter
import fhir as supermod
from utils import get_address
import sys

#TODO Put restrictions on code values (interp, status, reliability, etc)

class health_Observation(supermod.Observation):
    def __init__(self, *args, **kwargs):
        super(health_Observation, self).__init__(*args, **kwargs)
        self.model_mapping = {
                'lab': {'patient': 'gnuhealth_lab_id.patient',
                    'date': 'gnuhealth_lab_id.date_analysis',
                    'comments': 'remarks',
                    'value': 'result'},
                'icu':{ 'patient': 'name.patient',
                    'date': 'score_date',
                    'fields': {
                        'rate': 'respiratory_rate',
                        'pulse': 'heart_rate',
                        'temp': 'temperature'}},
                'amb': { 'patient': 'patient',
                    'comments': 'session_notes',
                    'date': 'session_start',
                    'fields': {
                        'rate': 'respiratory_rate',
                        'pulse': 'bpm',
                        'temp': 'temperature',
                        'press_d': 'diastolic',
                        'press_s': 'systolic'}},
                'eval': {'patient': 'patient',
                    'comments': 'notes',
                    'date': 'evaluation_start',
                    'fields': {
                        'rate': 'respiratory_rate',
                        'pulse': 'bpm',
                        'temp': 'temperature',
                        'press_d': 'diastolic',
                        'press_s': 'systolic'}},
                'rounds': {'patient': 'name.patient',
                    'comments': 'round_summary',
                    'date': 'evaluation_start',
                    'fields': {
                        'rate': 'respiratory_rate',
                        'pulse': 'bpm',
                        'temp': 'temperature',
                        'press_d': 'diastolic',
                        'press_s': 'systolic'}}}

    def set_gnu_observation(self, obs, model='lab', field=None):
        """Set gnu observation"""
        self.gnu_obs = obs
        self.field = field
        self.model_type = model

        # Only certain models
        if self.model_type not in self.model_mapping:
            raise ValueError('Not a valid model')

        # These models require fields
        if self.model_type in ('eval', 'rounds', 'amb', 'icu'):
            if self.field is None: raise ValueError('Require a field')

        # Not these
        if self.model_type in ('lab'):
            if self.field is not None:
                raise ValueError('Bad field addendum')

        self.map = self.model_mapping[self.model_type]
        if self.field:
            self.model_field = self.map['fields'][self.field]
            self.description=self.gnu_obs.fields_get(self.model_field)[self.model_field]['string']
        else:
            self.model_field = self.map['value']
            self.description = self.gnu_obs.name

    def create_observation(self, lab_test, units, lab_result, patient):
        """Create observation.

        ***Must be connected to a patient***

        NOTE: Must create singleton Lab Test at the moment(?)
        """
        patient_id = find_record(patient, [('id', '=', self.models['patient']['id'])])
        if not patient_id:
            raise ValueError
        units_id = find_record(units, [['OR', [('name', '=', self.models['units']['name'])],
                                            [('code', '=', self.models['units']['code'])]]])
        if not units_id:
            raise ValueError

        pass

    def __set_gnu_models(self):
        pass

    def import_from_gnu_observation(self):
        """Imports Health values into
            Observation structure"""
        if self.gnu_obs:
            self.__set_gnu_identifier()
            self.__set_gnu_subject()
            self.__set_gnu_comments()
            self.__set_gnu_value()
            self.__set_gnu_referenceRange()
            self.__set_gnu_interpretation()
            self.__set_gnu_status()
            self.__set_gnu_reliability()
            self.__set_gnu_issued()

    def set_applies_date_time(self):
        pass

    def set_applies_period(self):
        pass

    def __set_gnu_comments(self):
        if self.gnu_obs:
            comments = attrgetter(self.map['comments'])(self.gnu_obs)
            self.set_comments(comments)

    def set_comments(self, comments):
        """Set comments"""
        if comments:
            m = supermod.string(value=str(comments))
            super(health_Observation, self).set_comments(m)

    def __set_gnu_identifier(self):
        if self.gnu_obs:
            id = self.gnu_obs.id
            obj = self.description
            patient, time = attrgetter(self.map['patient'], self.map['date'])(self.gnu_obs)

            if id and obj and patient and time:
                label = '{0} value for {1} on {2}'.format(obj, patient.name.rec_name, time.strftime('%Y/%m/%d'))
                value = '-'.join([self.model_type, str(id)])
                if self.field:
                    value='-'.join((value, self.field))
                ident = supermod.Identifier(
                            label=supermod.string(value=label),
                            system=supermod.uri(value='gnuhealth::0'), #TODO
                            value=supermod.string(value=value))
                self.set_identifier(ident)


    def set_identifier(self, identifier):
        """Set identifier"""
        if identifier:
            super(health_Observation, self).set_identifier(identifier)

    def __set_gnu_interpretation(self):
        # TODO: Interpretation is complicated
        if self.gnu_obs:
            if self.model_type == 'lab':
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

    def __set_gnu_issued(self):
        if self.gnu_obs:
            time=self.gnu_obs.write_date.strftime("%Y-%m-%dT%H:%M:%S")
            if time:
                instant = supermod.instant(value=time)
                self.set_issued(instant)


    def set_issued(self, issued):
        """Set newest update time"""
        if issued:
            super(health_Observation, self).set_issued(issued)

    def set_method(self):
        pass

    def set_name(self):
        pass

    def set_performer(self):
        pass

    def __set_gnu_referenceRange(self):
        if self.gnu_obs:
            if self.model_type == 'lab':
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

    def __set_gnu_value(self):
        if self.gnu_obs:
            code = None
            system = None
            units = None
            value = attrgetter(self.model_field)(self.gnu_obs)
            if self.field == 'temp':
                units = "degrees C"
                code = "258710007"
                system = "http://snomed.info/sct"
            elif self.field == 'press_d':
                units = "mm[Hg]"
            elif self.field == 'press_s':
                units = "mm[Hg]"
            elif self.field == 'pulse':
                units = "beats/min"
            elif self.field == 'rate':
                units= "breaths/min"
            else:
                units = self.gnu_obs.units.name

            if value and units:
                q = supermod.Quantity()
                q.value = supermod.decimal(value=value)
                q.units = supermod.string(value=units)
                if code and system:
                    q.code = supermod.code(value=code)
                    q.system = supermod.uri(value=system)
                self.set_valueQuantity(q)
            else:
                raise ValueError('No value.')

    def set_valueQuantity(self, quantity):
        """Set actual value of observation"""
        if quantity:
            super(health_Observation, self).set_valueQuantity(quantity)

    def __set_gnu_subject(self):
        if self.gnu_obs:
            try:
                patient = attrgetter(self.map['patient'])(self.gnu_obs)
                if not patient:
                    raise ValueError('No patient field')

                uri = ''.join(['/Patient/', str(patient.id)])
                display = patient.name.rec_name
                ref=supermod.ResourceReference()
                ref.display = supermod.string(value=display)
                ref.reference = supermod.string(value=uri)
            except:
                raise ValueError('Unknown error')
            else:
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
