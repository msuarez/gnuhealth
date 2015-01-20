from StringIO import StringIO
from .datastore import find_record
from operator import attrgetter
import server.fhir as supermod

try:
    from flask import url_for
    RUN_FLASK=True
except:
    from .datastore import dumb_url_generate
    RUN_FLASK=False

class FieldError(Exception): pass

class Observation_Map:
    """This class holds the mapping between GNU Health and FHIR
        for the Observation resource
    """
    model_mapping = {
        'gnuhealth.lab.test.critearea':
            {'patient': 'gnuhealth_lab_id.patient',
            'date': 'gnuhealth_lab_id.date_analysis',
            'comments': 'remarks',
            'value': 'result'},
        'gnuhealth.icu.apache2':
            { 'patient': 'name.patient',
            'date': 'score_date',
            'fields': {
                'rate': 'respiratory_rate',
                'pulse': 'heart_rate',
                'temp': 'temperature'}},
        'gnuhealth.patient.ambulatory_care':
            { 'patient': 'patient',
            'comments': 'session_notes',
            'date': 'session_start',
            'performer': 'health_professional',
            'fields': {
                'rate': 'respiratory_rate',
                'pulse': 'bpm',
                'temp': 'temperature',
                'press_d': 'diastolic',
                'press_s': 'systolic'}},
        'gnuhealth.patient.evaluation':
            {'patient': 'patient',
            'comments': 'notes',
            'date': 'evaluation_start',
            'performer': 'healthprof',
            'fields': {
                'rate': 'respiratory_rate',
                'pulse': 'bpm',
                'temp': 'temperature',
                'press_d': 'diastolic',
                'press_s': 'systolic'}},
        'gnuhealth.patient.rounding':
            {'patient': 'name.patient',
            'comments': 'round_summary',
            'date': 'evaluation_start',
            'performer': 'health_professional',
            'fields': {
                'rate': 'respiratory_rate',
                'pulse': 'bpm',
                'temp': 'temperature',
                'press_d': 'diastolic',
                'press_s': 'systolic'}}}
    url_prefixes ={
            'gnuhealth.lab.test.critearea': 'lab',
            'gnuhealth.patient.rounding': 'rounds',
            'gnuhealth.patient.evaluation': 'eval',
            'gnuhealth.patient.ambulatory_care': 'amb',
            'gnuhealth.icu.apache2': 'icu'}

    search_mapping ={
            'gnuhealth.lab.test.critearea':
                    {'_id': (['id'], 'token'), #Needs to be parsed MODEL-ID-FIELD
                    '_language': None,
                    'date': (['gnuhealth_lab_id.date_analysis'], 'date'),
                    'name': (['name'], 'token'),
                    'performer': None,
                    'reliability': None,
                    'related': None,
                    'related-target': None,
                    'related-type': None,
                    'specimen': None,
                    'status': None,
                    'subject': (['gnuhealth_lab_id.patient'], 'reference'), 
                    'value-concept': None,
                    'value-date': None,
                    'value-quantity': (['result'], 'quantity'),
                    'value-string': None}}
    todo_search_mapping={
           'gnuhealth.patient.evaluation': {'_id': (['id'], 'token'), #Needs to be parsed MODEL-ID-FIELD
                    '_language': None,
                    'date': None,
                    # These values point to keys on the 'fields' dict
                    'name': ({'Respiratory rate': 'rate',
                                'Heart rate': 'pulse', 'Systolic pressure': 'press_s',
                                'Diastolic pressure': 'press_d',
                                'Temperature': 'temp'}, 'user-defined'),
                    'performer': (['healthprof'], 'reference'),
                    'reliability': None,
                    'related': None,
                    'related-target': None,
                    'related-type': None,
                    'specimen': None,
                    'status': None,
                    'subject': ({'Resource': 'Patient',
                                'Path': 'patient'}, 'reference'), 
                    'value-concept': None,
                    'value-date': None,
                    'value-quantity': (['respiratory_rate', 'bpm','diastolic','systolic', 'temperature'], 'quantity'),
                    'value-string': None},
            'gnuhealth.icu.apache2': {'_id': (['id'], 'token'), #Needs to be parsed MODEL-ID-FIELD
                    '_language': None,
                    'date': None,
                    # These values point to keys on the 'fields' dict
                    'name': ({'Respiratory rate': 'rate',
                                'Heart rate': 'pulse',
                                'Temperature': 'temp'}, 'user-defined'),
                    'performer': None,
                    'reliability': None,
                    'related': None,
                    'related-target': None,
                    'related-type': None,
                    'specimen': None,
                    'status': None,
                    'subject': (['name.patient'], 'reference'), 
                    'value-concept': None,
                    'value-date': None,
                    'value-quantity': (['respiratory_rate', 'heart_rate', 'temperature'], 'quantity'),
                    'value-string': None},
            'gnuhealth.patient.rounding': {'_id': (['id'], 'token'), #Needs to be parsed MODEL-ID-FIELD
                    '_language': None,
                    'date': None,
                    # These values point to keys on the 'fields' dict
                    'name': ({'Respiratory rate': 'rate',
                                'Heart rate': 'pulse', 'Systolic pressure': 'press_s',
                                'Diastolic pressure': 'press_d',
                                'Temperature': 'temp'}, 'user-defined'),
                    'performer': (['health_professional'], 'reference'),
                    'reliability': None,
                    'related': None,
                    'related-target': None,
                    'related-type': None,
                    'specimen': None,
                    'status': None,
                    'subject': (['name.patient'], 'reference'), 
                    'value-concept': None,
                    'value-date': None,
                    'value-quantity': (['respiratory_rate', 'bpm','diastolic','systolic', 'temperature'], 'quantity'),
                    'value-string': None},
            'gnuhealth.patient.ambulatory_care': {'_id': (['id'], 'token'), #Needs to be parsed MODEL-ID-FIELD
                    '_language': None,
                    'date': None,
                    # These values point to keys on the 'fields' dict
                    'name': ({'Respiratory rate': 'rate',
                                'Heart rate': 'pulse', 'Systolic pressure': 'press_s',
                                'Diastolic pressure': 'press_d',
                                'Temperature': 'temp'}, 'user-defined'),
                    'performer': (['health_professional'], 'reference'),
                    'reliability': None,
                    'related': None,
                    'related-target': None,
                    'related-type': None,
                    'specimen': None,
                    'status': None,
                    'subject': (['patient'], 'reference'),
                    'value-concept': None,
                    'value-date': None,
                    'value-quantity': (['respiratory_rate', 'bpm','diastolic','systolic', 'temperature'], 'quantity'),
                    'value-string': None}}

#TODO Put restrictions on code values (interp, status, reliability, etc)
class health_Observation(supermod.Observation, Observation_Map):
    def __init__(self, *args, **kwargs):
        gnu=kwargs.pop('gnu_record', None)
        field=kwargs.pop('field', None)
        super(health_Observation, self).__init__(*args, **kwargs)
        if gnu:
            self.set_gnu_observation(gnu, field=field)

    def set_gnu_observation(self, obs, field=None):
        """Set gnu observation"""
        self.gnu_obs = obs
        self.field = field
        self.model_type = self.gnu_obs.__name__

        # Only certain models
        if self.model_type not in self.model_mapping:
            raise ValueError('Not a valid model')

        self.map = self.model_mapping[self.model_type]

        # These models require fields
        if self.map.get('fields') and self.field is None:
            raise FieldError('This model requires a field')

        # Not these
        if self.map.get('value') and self.field is not None:
            raise ValueError('Ambiguous field; not required')

        self.search_prefix = self.url_prefixes[self.model_type]

        if self.field:
            self.model_field = self.map['fields'][self.field]
            self.description=self.gnu_obs.fields_get(self.model_field)[self.model_field]['string']
        else:
            self.model_field = self.map['value']
            self.description = self.gnu_obs.name

        # Quietly import the info
        self.__import_from_gnu_observation()

    def create_observation(self, lab_test, units, lab_result, patient):
        """Create observation.

        ***Must be connected to a patient***

        NOTE: Must create singleton Lab Test at the moment(?)
        NOTE: Where to put vital signs? Evals?
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

    def __set_feed_info(self):
        if self.gnu_obs:
            self.feed={'id': self.gnu_obs.id,
                    'published': self.gnu_obs.create_date,
                    'updated': self.gnu_obs.write_date or self.gnu_obs.create_date,
                    'title': self.identifier.label.value
                        }


    def __import_from_gnu_observation(self):
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
            self.__set_gnu_performer()
            self.__set_gnu_name()

            self.__set_feed_info()

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
            obj = self.description
            patient, time = attrgetter(self.map['patient'], self.map['date'])(self.gnu_obs)

            if id and obj and patient and time:
                label = '{0} value for {1} on {2}'.format(obj, patient.name.rec_name, time.strftime('%Y/%m/%d'))
                if RUN_FLASK:
                    value = url_for('obs_record', log_id=(self.search_prefix, self.gnu_obs.id, self.field))
                else:
                    value = dumb_url_generate(['Observation', self.search_prefix,
                                                                self.gnu_obs.id,
                                                                self.field])
                ident = supermod.Identifier(
                            label=supermod.string(value=label),
                            #system=supermod.uri(value='gnuhealth::0'), #TODO
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

    def __set_gnu_name(self):
        #TODO Support better coding
        if self.gnu_obs:
            name = supermod.CodeableConcept()
            name.coding = [supermod.Coding()]
            name.coding[0].display = supermod.string(value=self.description)
            self.set_name(name)

    def set_name(self, name):
        '''Set the observation type'''
        if name:
            super(health_Observation, self).set_name(name)

    def __set_gnu_performer(self):
        if self.gnu_obs:
            try:
                p = attrgetter(self.map['performer'])(self.gnu_obs)
                uri = ''.join(['/Practioner/', str(p.id)])
                display = p.name.rec_name
                ref=supermod.ResourceReference()
                ref.display = supermod.string(value=display)
                ref.reference = supermod.string(value=uri)
            except:
                # Not absolutely needed, so continue execution
                pass
            else:
                self.set_performer([ref])

    def set_performer(self, performer):
        '''Set who/what captured the observation'''
        if performer:
            super(health_Observation, self).set_performer(performer)


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
                # If there is no value, the observation is useless
                #    Therefore, exit early (handle this in the blueprint)
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
                    # If there is no connected patient, the observation is useless
                    #    Therefore, exit early (handle this in the blueprint)
                    raise ValueError('No patient field')

                uri = ''.join(['/Patient/', str(patient.id)])
                display = patient.name.rec_name
                ref=supermod.ResourceReference()
                ref.display = supermod.string(value=display)
                ref.reference = supermod.string(value=uri)
            except:
                # Errors in this section must stop execution
                raise
            else:
                self.set_subject(ref)

    def set_subject(self, subject):
        """Set subject (usually patient)"""
        if subject:
            super(health_Observation, self).set_subject(subject)

    def export_to_xml_string(self):
        output = StringIO()
        self.export(outfile=output, namespacedef_='xmlns="http://hl7.org/fhir"', pretty_print=False, level=4)
        content = output.getvalue()
        output.close()
        return content
supermod.Observation.subclass=health_Observation

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

