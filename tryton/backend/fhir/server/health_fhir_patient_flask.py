from flask import Blueprint, request, current_app
from flask.ext.restful import Resource, abort, reqparse
from health_fhir_flask import (tryton, api, patient, party,
                                safe_fromstring, safe_parse)
from io import StringIO
import fhir_xml

def etree_to_dict(tree):
    '''Converts an etree into a dictionary.'''
    #TODO Peculiarities of FHIR standard need to
    #    be addresssed
    children=tree.getchildren()
    if children:
        return {tree.tag: [etree_to_dict(c) for c in children]}
    else:
        return {tree.tag: dict(tree.attrib)}

# 'Patient' blueprint on '/Patient'
patient_endpoint = Blueprint('patient_endpoint', __name__,
                                template_folder='templates',
                                url_prefix="/Patient")

# Initialize api restful
api.init_app(patient_endpoint)

class meta_patient(object):
    '''Mediate between XML/JSON schema bindings and
        the GNU Health models'''

    def __init__(record=None, patient=None):
        self.record = record
        self.patient = patient or fhir_xml.Patient()
        if self.record and getattr(self.record, 'name', None):
            self.set_gender()
            self.set_deceased_status()
            self.set_deceased_datetime()
            self.set_birthdate()
            self.set_telecom()
            self.set_name()
            self.set_identifier()
            self.set_address()
            self.set_active()
            self.set_photo()
            self.set_communication()
            self.set_contact()
            self.set_care_provider()
            self.set_marital_status()

    def set_identifier(self):
        if getattr(self.record, 'puid', None):
            ident = fhir_xml.Identifier(
                        use=fhir_xml.IdentifierUse(value='usual'),
                        label=fhir_xml.string(value='PUID'),
                        system=fhir_xml.system(
                            fhir_xml.uri(
                                value=current_app.config.get(
                                    'INSTITUTION_ODI', None))),
                        value=fhir_xml.string(value=self.record.puid))

        elif getattr(self.record, 'alternative_identification', None):
            ident = fhir_xml.Identifier(
                        use=fhir_xml.IdentifierUse(value='usual'),
                        label=fhir_xml.string(value='ALTERNATE_ID'),
                        system=fhir_xml.system(
                            fhir_xml.uri(
                                value=current_app.config.get(
                                    'INSTITUTION_ODI',None))),
                        value=fhir_xml.string(
                            value=self.record.alternative_identification))
        else:
            return
        self.patient.add_identifier(value=ident)

    def set_name(self):
        name = []
        name.append(fhir_xml.HumanName(
                    use=fhir_xml.NameUse(value='official'),
                    family=[fhir_xml.string(value=x) for x in self.record.lastname.split()],
                    given=[fhir_xml.string(value=x) for x in self.record.name.name.split()]))

        if getattr(self.record.name, 'alias', None):
            name.append(fhir_xmlHumanName(
                        use=fhir_xml.NameUse(value='usual'),
                        given=[fhir_xml.string(value=self.record.name.alias)]))
        for x in name:
            self.patient.add_name(x)

    def set_telecom(self):
        telecom = []
        if getattr(self.record.name, 'phone', None):
            telecom.append(fhir_xml.Contact(
                    system=fhir_xml.ContactSystem(value='phone'),
                    value=fhir_xml.string(value=self.record.name.phone),
                    use=fhir_xml.ContactUse(value='home')))
        if getattr(self.record.name, 'mobile', None):
            telecom.append(fhir_xml.Contact(
                    system=fhir_xml.ContactSystem(value='phone'),
                    value=fhir_xml.string(value=self.record.name.mobile),
                    use=fhir_xml.ContactUse(value='mobile')))
        if getattr(self.record.name, 'email', None):
            telecom.append(fhir_xml.Contact(
                    system=fhir_xml.ContactSystem(value='email'),
                    value=fhir_xml.string(value=self.record.name.email),
                    use=fhir_xml.ContactUse(value='email')))
        for x in telecom:
            self.patient.add_telecom(x)

    def set_gender(self):
        if getattr(self.record, 'sex', None):
            coding = fhir_xml.Coding(
                        system=fhir_xml.uri(value='http://hl7.org/fhir/v3/AdministrativeGender'),
                        code=fhir_xml.code(value=self.record.sex.upper()),
                        display=fhir_xml.string(value='Male' if record.sex == 'm' else 'Female')
                        )
            gender=fhir_xml.CodeableConcept(coding=[coding])
            self.patient.set_gender(gender)

    def set_birthdate(self):
        if getattr(self.record, 'dob', None):
            self.patient.set_birthdate(fhir_xml.dateTime(value=self.record.dob))

    def set_deceased_status(self):
        if getattr(self.record, 'deceased', None):
            status=fhir_xml.boolean(value='true')
        else:
            status=fhir_xml.boolean(value='false')
        self.patient.set_deceaseadBoolean(status)

    def set_deceased_datetime(self):
        if getattr(self.record, 'deceased', None):
            self.patient.set_deceasedDateTime(fhir_xml.dateTime(value=str(self.record.dod)))

    def set_address(self):
        if getattr(self.record.name, 'du', None):
            address=fhir_xml.Address()
            address.set_use(fhir_xml.string(value='home'))
            address.add_line(fhir_xml.string(value=' '.join([
                                        str(self.record.name.du.address_street_number),
                                        self.record.name.du.address_street])))
            address.set_city(fhir_xml.string(value=self.record.name.du.address_city))
            address.set_state(fhir_xml.string(value=self.record.name.du.address_subdivision))
            address.set_zip(fhir_xml.string(value=self.record.name.du.address_zip))
            address.set_country(fhir_xml.string(value=self.record.name.du.address_country))

            self.patient.add_address(address)

    def set_active(self):
        self.patient.set_active(fhir_xml.boolean(value='true'))

    def set_contact(self):
        pass

    def set_care_provider(self):
        pass

    def set_communication(self):
        pass

    def set_photo(self):
        import base64
        if getattr(self.record, 'photo', None):
            im = fhir_xml.Attachment(data=base64.encodestring(self.record.photo))
            self.patient.add_photo(im)

    def set_marital_status(self):
        pass

    def export(self):
        return self.patient

class Create(Resource):
    @tryton.transaction()
    def post():
        #Create interaction
        json = request.get_json(force=True, silent=True)
        if json:
            #json
            pass
        else:
            #try xml?
            xml=safe_xml_fromstring(request.data)
            if xml:
                pass
            else:
                abort(400, message="Bad data")
        abort(405, message='Not implemented.')

api.add_resource(Create, '/')

class Search(Resource):
    @tryton.transaction()
    def get():
        #Search interaction
        #TODO Search implementation is important, but
        # also very robust, so keep it simple for now
        allowed=['_id', 'active', 'address', 'animal-breed', 'animal-species',
            'birthdate', 'family', 'gender', 'given', 'identifier', 'language',
            'link', 'name', 'phonetic', 'provider', 'telecom']
        _id = request.args.get('_id', None)
        identifier = request.args.get('identifier', None)
        if _id:
            rec = patient.search(['id', '=', _id], limit=1)
        if identifier:
            rec = patient.search(['OR', ['ssn', '=', identifier],
                                ['identification_code', '=', identifier]], limit=1)
        if rec:
            return get_patient_record(rec)
        else:
            #TODO OperationOutcome; for now an error
            abort(403, message="No matching record(s)")

api.add_resource(Search, '/', '/_search')

class Record(Resource):
    @tryton.transaction()
    def get(self, log_id):
        #Read interaction
        record = patient.search(['id', '=', log_id], limit=1)
        if record:
            return meta_patient(record=record)
        else:
            abort(404, message="Record not found")
            #if track deleted records
            #abort(410, message="Record deleted")

    @tryton.transaction()
    def put(self, log_id):
        #Update interaction
        abort(405, message='Not implemented.')

    @tryton.transaction()
    def delete(self, log_id):
        #Delete interaction
        abort(405, message='Not implemented.')

api.add_resource(Record, '/<string:log_id>')

class Validate(Resource):
    @tryton.transaction()
    def post(self, log_id):
        #Validate interaction
        abort(405, message='Not implemented.')

api.add_resource(Validate, '/validate',
                        '/validate/<string:log_id>',
                defaults={'log_id': None})

class Version(Resource):
    @tryton.transaction()
    def get(self, log_id, v_id):
        #Vread interaction
        abort(405, message='Not implemented.')

api.add_resource(Version, '/<string:log_id>/_history',
                    '/<string:log_id>/_history/<string:v_id>',
                defaults={'v_id': None})

@api.representation('xml')
@api.representation('text/xml')
@api.representation('application/xml')
@api.representation('application/xml+fhir')
def output_xml(data, code, headers=None):
    with StringIO() as t:
        data.export(outfile=t, pretty_print=False)
        resp = make_response(t.getvalue(), code)
    resp.headers.extend(headers or {})
    resp.headers['Content-type']='application/xml+fhir' #Return proper type
    return resp

@api.representation('json')
@api.representation('application/json')
@api.representation('application/json+fhir')
def output_json(data, code, headers=None):
    resp = make_response(
                json.dumps(etree_to_dict(data.to_etree())),
                code)
    resp.headers.extend(headers or {})
    resp.headers['Content-type']='application/json+fhir' #Return proper type
    return resp


@api.representation('atom')
@api.representation('application/atom')
@api.representation('application/atom+fhir')
def output_atom(data, code, headers=None):
    resp = make_response(data, code)
    resp.headers.extend(headers or {})
    resp.headers['Content-type']='application/atom+fhir' #Return proper type
    return resp
