from StringIO import StringIO
from operator import attrgetter
from server.common import safe_attrgetter
import server.fhir as supermod
from .health_mixin import ExportXMLMixin

try:
    from flask import url_for
    RUN_FLASK=True
except:
    from .datastore import dumb_url_generate
    RUN_FLASK=False


class MedicationStatement_Map:
    """Holds essential mappings and information for
        the MedicationStatement class
    """

    root_search=[('name', '!=', None)]

    resource_search_params={
            '_id': 'token',
            'patient': 'reference',
            'when-given': 'date',
            'medication': 'reference',
            'identifier': None,
            'device': None,
            '_language': None}

    chain_map={'patient': 'Patient',
            'medication': 'Medication'}

    search_mapping={
            '_id': ['id'],
            'patient': ['name'],
            'when-given': ['start_treatment'],
            'medication': ['medicament']}


    url_prefixes={}
    model_mapping={'gnuhealth.patient.medication':
            {
                'patient': 'name',
                'when-given': {
                        'start': 'start_treatment',
                        'end': 'end_treatment'},
                'medication': 'medicament',
                'dose': {
                        'quantity': 'dose',
                        'units': 'dose_unit.name',
                        'route': 'route',
                        'asNeededBoolean': 'frequency_prn'}
            }}

class health_MedicationStatement(supermod.MedicationStatement, MedicationStatement_Map, ExportXMLMixin):
    def __init__(self, *args, **kwargs):
        rec = kwargs.pop('gnu_record', None)
        super(health_MedicationStatement, self).__init__(*args, **kwargs)
        if rec:
            self.set_gnu_medication_statement(rec)

    def set_gnu_medication_statement(self, medication_statement):
        """Set the GNU Health record
        ::::
            params:
                medication_statement ===> Health model
            returns:
                instance

        """
        self.medication_statement = medication_statement
        self.model_type = self.medication_statement.__name__

        # Only certain models
        if self.model_type not in self.model_mapping:
            raise ValueError('Not a valid model')

        self.map = self.model_mapping[self.model_type]

        self.__import_from_gnu_medication_statement()

    def __import_from_gnu_medication_statement(self):
        """Import the data from the model"""
        if self.medication_statement:
            self.__set_gnu_patient()
            self.__set_gnu_when_given()
            self.__set_gnu_medication()
            #self.__set_gnu_dosage()

            self.__set_feed_info()

    def __set_feed_info(self):
        """Sets the feed-relevant info"""
        if self.medication_statement:
            if RUN_FLASK:
                uri = url_for('ms_record',
                            log_id=self.medication_statement.id,
                            _external=True)
            else:
                uri = dumb_url_generate(['MedicationStatement', self.medication_statement.id])
            self.feed={'id': uri,
                    'published': self.medication_statement.create_date,
                    'updated': self.medication_statement.write_date or self.medication_statement.create_date,
                    'title': '{} for {}'.format(
                            self.medication_statement.medicament.name.name,
                            self.medication_statement.name.rec_name)
                        }

    def __set_gnu_patient(self):
        """Set the patient info"""
        if self.medication_statement:
            patient = attrgetter(self.map['patient'])(self.medication_statement)
            if RUN_FLASK:
                uri = url_for('pat_record', log_id=patient.id)
            else:
                uri = dumb_url_generate(['Patient', patient.id])
            display = patient.rec_name
            ref=supermod.ResourceReference()
            ref.display = supermod.string(value=display)
            ref.reference = supermod.string(value=uri)
            self.set_patient(ref)

    def __set_gnu_dosage(self):
        """Set dosage"""
        # TODO Add better dosage info
        # FIX On hold since many changes upcoming to the dosage
        if self.medication_statement:
            d = supermod.MedicationStatement_Dosage()


            d.quantity = supermod.Quantity()
            f = safe_attrgetter(self.medication_statement, self.map['dose']['quantity'])
            if f:
                d.quantity.value = supermod.decimal(value=f)
            u = safe_attrgetter(self.medication_statement, self.map['dose']['units'])
            if u:
                d.quantity.units = supermod.string(value=u)

            d.route = supermod.CodeableConcept()
            r = safe_attrgetter(self.medication_statement, self.map['dose']['route'])
            if r:
                d.route.coding = [supermod.Coding()]
                d.route.coding[0].code = supermod.code(value=r.code)
                d.route.coding[0].display = supermod.string(value=r.name)
                d.route.text = supermod.string(r.name)

            # PRN?
            an = safe_attrgetter(self.medication_statement,
                            self.map['dose']['asNeededBoolean'])
            if an:
                self.set_asNeededBoolean(supermod.boolean(value=True))

            d.timing = supermod.Schedule()

            if self.medication_statement.infusion:
                d.rate

    def __set_gnu_when_given(self):
        """Set datetime when given"""
        # TODO Maybe add hours, minutes, etc.
        if self.medication_statement:
            start = safe_attrgetter(self.medication_statement,
                                    self.map['when-given']['start'])
            end = safe_attrgetter(self.medication_statement,
                                    self.map['when-given']['end'])
            if start:
                p = supermod.Period()
                p.start = supermod.dateTime(value=start.strftime('%Y/%m/%d'))
                if end:
                    p.end = supermod.dateTime(value=end.strftime('%Y/%m/%d'))
                self.set_whenGiven(p)


    def __set_gnu_medication(self):
        if self.medication_statement:
            med = attrgetter(self.map['medication'])(self.medication_statement)
            if RUN_FLASK:
                uri = url_for('med_record', log_id=med.id)
            else:
                uri = dumb_url_generate(['Medication', med.id])
            display = med.active_component
            ref=supermod.ResourceReference()
            ref.display = supermod.string(value=display)
            ref.reference = supermod.string(value=uri)
            self.set_medication(ref)

supermod.MedicationStatement.subclass=health_MedicationStatement
