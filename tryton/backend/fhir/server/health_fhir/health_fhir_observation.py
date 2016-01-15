from StringIO import StringIO
from .datastore import find_record
from operator import attrgetter
import server.fhir as supermod
from server.common import safe_attrgetter
from .health_mixin import ExportXMLMixin

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
            'performer': 'pathologist',
            'comments': 'remarks',
            'value': 'result',
            'excluded': 'excluded'},
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

    url_prefixes ={}
            #'gnuhealth.lab.test.critearea': 'lab',
            #'gnuhealth.patient.rounding': 'rounds',
            #'gnuhealth.patient.evaluation': 'eval',
            #'gnuhealth.patient.ambulatory_care': 'amb',
            #'gnuhealth.icu.apache2': 'icu'}

    resource_search_params = {
                    '_id': 'token',
                    '_language': None,
                    'date': 'date',
                    'name': 'token',
                    'performer': None,
                    'reliability': None,
                    'related': None,
                    'related-target': None,
                    'related-type': None,
                    'specimen': None,
                    'status': None,
                    'subject': 'reference',
                    'value-concept': None,
                    'value-date': None,
                    'value-quantity': 'quantity',
                    'value-string': None}

    # Must be attached to lab
    root_search=[[('gnuhealth_lab_id', '!=', None)]]
    #root_search=[['OR', [('result', '!=', None)],
                        #[('excluded', '=', True)],
                        #[('gnuhealth_lab_id', '!=', None)]]]

    # Maps reference parameters to correct resource
    chain_map={
                'subject': 'Patient'}

    search_mapping ={
                    '_id': ['id'],
                    'date': ['gnuhealth_lab_id.date_analysis'],
                    'name': ['name'],
                    'subject': ['gnuhealth_lab_id.patient'],
                    'value-quantity': ['result']}

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
class health_Observation(supermod.Observation, Observation_Map, ExportXMLMixin):
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

        self.map_ = self.model_mapping[self.model_type]

        # These models require fields
        if self.map_.get('fields') and self.field is None:
            raise FieldError('This model requires a field')

        # Not these
        if self.map_.get('value') and self.field is not None:
            raise ValueError('Ambiguous field; not required')

        #self.search_prefix = self.url_prefixes[self.model_type]

        if self.field:
            self.model_field = self.map_['fields'][self.field]
            self.description=self.gnu_obs.fields_get(self.model_field)[self.model_field]['string']
        else:
            self.model_field = self.map_['value']
            self.description = self.gnu_obs.name

        # Quietly import the info
        self.__import_from_gnu_observation()
        self.__set_feed_info()

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
        """Set the feed-relevant data"""
        if self.gnu_obs:
            if RUN_FLASK:
                uri = url_for('obs_record',
                                log_id=self.gnu_obs.id,
                                _external=True)
            else:
                uri = dumb_url_generate(['Observation',
                                self.gnu_obs.id])
            self.feed={'id': uri,
                    'published': self.gnu_obs.create_date,
                    'updated': self.gnu_obs.write_date or self.gnu_obs.create_date,
                    'title': self.identifier.label.value
                        }

    def __import_from_gnu_observation(self):
        """Set the data from the model"""
        if self.gnu_obs:
            self.set_identifier(
                    self.gnu_obs,
                    safe_attrgetter(self.gnu_obs, self.map_['patient']),
                    safe_attrgetter(self.gnu_obs, self.map_['date']))
            self.set_subject(
                    safe_attrgetter(self.gnu_obs,
                                            self.map_['patient']))
            self.set_comments(
                    safe_attrgetter(self.gnu_obs, self.map_['comments']))
            self.set_valueQuantity(
                    safe_attrgetter(self.gnu_obs, self.model_field),
                    safe_attrgetter(self.gnu_obs, 'units.name'))
            self.set_referenceRange(
                    safe_attrgetter(self.gnu_obs, 'units.name', default='unknown'),
                    safe_attrgetter(self.gnu_obs, 'lower_limit'),
                    safe_attrgetter(self.gnu_obs, 'upper_limit'))
            self.set_interpretation(
                    safe_attrgetter(self.gnu_obs, self.model_field),
                    safe_attrgetter(self.gnu_obs, 'lower_limit'),
                    safe_attrgetter(self.gnu_obs, 'upper_limit'))
            self.set_status(
                    safe_attrgetter(self.gnu_obs, self.map_['excluded']),
                    safe_attrgetter(self.gnu_obs, self.model_field))
            self.set_reliability('ok')
            self.set_issued(
                    self.gnu_obs.write_date or self.gnu_obs.create_date)
            self.set_performer(
                    safe_attrgetter(self.gnu_obs, self.map_['performer']))
            self.set_name(
                    self.description)

    def set_comments(self, comments):
        """Extends superclass for convenience

        Set comments

        Keyword arguments:
        comments -- the comments
        """

        if comments:
            m = supermod.string(value=str(comments))
            super(health_Observation, self).set_comments(m)

    def set_identifier(self, observation, patient, date):
        """Extends superclass for convenience

        Set the identifier from the data model

        Keyword arguments:
        observation -- the observation (Health model)
        patient -- patient (Health model)
        date -- date of observation (datetime object)
        """

        if observation and patient:
            if date is not None:
                label = '{0} value for {1} on {2}'.format(observation.name,
                                                    patient.name.rec_name,
                                                    date.strftime('%Y/%m/%d'))
            else:
                label = '{0} value for {1} on unknown'.format(observation.name,
                                                    patient.name.rec_name)

            if RUN_FLASK:
                value = url_for('obs_record', log_id=observation.id)
            else:
                value = dumb_url_generate(['Observation', observation.id])
            ident = supermod.Identifier(
                        label=supermod.string(value=label),
                        value=supermod.string(value=value))
            super(health_Observation, self).set_identifier(ident)

    def set_interpretation(self, value, lower_limit, upper_limit):
        """Extends superclass for convenience

        Set the interpretation

        Keyword arguments:
        value -- observation value
        lower_limit -- the lower normal
        upper_limit -- the upper normal
        """
        # TODO: Interpretation is complicated

        if value and lower_limit and upper_limit:
            interp = supermod.CodeableConcept()
            interp.coding = [supermod.Coding()]
            if value < lower_limit:
                v = 'L'
                d = 'Low'
            elif value > upper_limit:
                v = 'H'
                d = 'High'
            else:
                v = 'N'
                d = 'Normal'
            interp.coding[0].system = supermod.uri(value='http://hl7.org/fhir/v2/0078')
            interp.coding[0].code = supermod.code(value=v)
            interp.coding[0].display = supermod.string(value=d)
            super(health_Observation, self).set_interpretation(interp)

    def set_issued(self, issued):
        """Extends superclass for convenience

        Set newest update time

        Keyword arguments:
        issued -- time issued (datetime object)
        """

        if issued is not None:
            time=issued.strftime("%Y-%m-%dT%H:%M:%S")
            instant = supermod.instant(value=time)
            super(health_Observation, self).set_issued(instant)

    def set_name(self, name):
        """Extends superclass for convenience

        Set the observation type

        Keyword arguments:
        name -- the description of the observation
        """
        #TODO Better coding

        if name:
            n = supermod.CodeableConcept()
            n.coding = [supermod.Coding()]
            n.coding[0].display = supermod.string(value=name)
            super(health_Observation, self).set_name(n)

    def set_performer(self, performer):
        """Extends superclass for convenience

        Set who/what captured the observation

        Keyword arguments:
        performer -- who performed the observation (Health model)
        """

        if performer:
            try:
                if RUN_FLASK:
                    uri=url_for('hp_record', log_id=performer.id)
                else:
                    uri=dumb_url_generate('/Practitioner', str(performer.id))
                display = performer.name.rec_name
                ref=supermod.ResourceReference()
                ref.display = supermod.string(value=display)
                ref.reference = supermod.string(value=uri)
            except:
                # Not absolutely needed, so continue execution
                pass
            else:
                super(health_Observation, self).set_performer([ref])

    def set_referenceRange(self, units, lower_limit, upper_limit):
        """Extends superclass for convenience

        Set reference range from data model

        Keyword arguments:
        units -- units name
        lower_limit -- lower limit
        upper_limit -- upper limit
        """

        if units is not None \
                and lower_limit is not None \
                and upper_limit is not None:
            ref = supermod.Observation_ReferenceRange()
            #ref.age = supermod.Range() #Not relevant, usually
            ref.low = supermod.Quantity()
            ref.high = supermod.Quantity()
            ref.low.units = ref.high.units = supermod.string(value=units)
            ref.low.value = supermod.decimal(value=lower_limit)
            ref.high.value = supermod.decimal(value=upper_limit)
            ref.meaning = supermod.Coding()
            ref.meaning.system = supermod.uri(value='http://hl7.org/fhir/referencerange-meaning')
            ref.meaning.code = supermod.code(value='normal')
            ref.meaning.display = supermod.string(value='Normal range')
            super(health_Observation, self).set_referenceRange([ref])

    def set_reliability(self, reliability='ok'):
        """Extends superclass for convenience

        Set reliability; mandatory

        Keyword arguments:
        reliability -- how reliable the observation
        """

        rel = supermod.ObservationReliability()
        rel.value = reliability or 'ok'
        super(health_Observation, self).set_reliability(rel)

    def set_status(self, excluded=False, value=None):
        """Extends superclass for convenience

        Set status; mandatory

        Keyword arguments:
        excluded -- excluded or not
        value -- the test value (used to determine specific status)
        """

        s = supermod.ObservationStatus()
        if excluded:
            if value is not None:
                s.value = 'cancelled'
            else:
                s.value = 'entered in error'
        else:
            if value is not None:
                s.value = 'final'
            else:
                s.value = 'temporary'
        super(health_Observation, self).set_status(s)

    def set_valueQuantity(self, value, units=None, code=None, system=None):
        """Extends superclass for convenience

        Set actual value of observation

        Keyword arguments:
        value -- the actual value
        units -- units (e.g., g/dL)
        code -- the code (e.g., 'XHEHA1')
        system -- the code system (e.g., 'http://code.system')
        """

        if value:

            # This is to handle multi-field
            #if self.field == 'temp':
                #units = "degrees C"
                #code = "258710007"
                #system = "http://snomed.info/sct"
            #elif self.field == 'press_d':
                #units = "mm[Hg]"
            #elif self.field == 'press_s':
                #units = "mm[Hg]"
            #elif self.field == 'pulse':
                #units = "beats/min"
            #elif self.field == 'rate':
                #units= "breaths/min"


            q = supermod.Quantity()
            q.value = supermod.decimal(value=value)

            if units:
                q.units = supermod.string(value=str(units))
            if code:
                q.code = supermod.code(value=str(code))
            if system:
                q.system = supermod.uri(value=str(system))
            super(health_Observation, self).set_valueQuantity(q)

    def set_subject(self, subject):
        """Extends superclass for convenience

        Set subject (usually patient); mandatory

        Keyword arguments:
        subject -- the subject (Health model)
        """

        if subject:
            try:
                if RUN_FLASK:
                    uri=url_for('pat_record', log_id=subject.id)
                else:
                    uri=dumb_url_generate('/Patient', str(subject.id))
                display = subject.name.rec_name
                ref=supermod.ResourceReference()
                ref.display = supermod.string(value=display)
                ref.reference = supermod.string(value=uri)
            except:
                raise
            else:
                super(health_Observation, self).set_subject(ref)

    def set_applies_date_time(self):
        pass

    def set_applies_period(self):
        pass

    def set_specimen(self):
        pass

    def set_related(self):
        pass

    def set_method(self):
        pass

supermod.Observation.subclass=health_Observation
