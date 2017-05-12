# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    Copyright (C) 2008-2017 Luis Falcon <lfalcon@gnusolidario.org>
#    Copyright (C) 2011-2017 GNU Solidario <health@gnusolidario.org>
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
from trytond.model import ModelView, ModelSQL, fields
from trytond.transaction import Transaction
from trytond.rpc import RPC
from trytond.pool import Pool
from trytond.wizard import Wizard, StateAction, StateView, Button
from trytond.pyson import Eval, Not, Bool, PYSONEncoder, Equal, And, Or
import hashlib
import json

__all__ = ['HealthCrypto','PatientPrescriptionOrder',
    'BirthCertificate','DeathCertificate','PatientEvaluation']


class HealthCrypto:
    """ GNU Health Cryptographic functions
    """

    def serialize(self,data_to_serialize):
        """ Format to JSON """
        json_output = \
            json.dumps(data_to_serialize, ensure_ascii=False)
        return json_output

    def gen_hash(self, serialized_doc):
        return str(hashlib.sha512(serialized_doc.encode('utf-8')).hexdigest())


class PatientPrescriptionOrder(ModelSQL, ModelView):
    """ Add the serialized and hash fields to the
    prescription order document"""
    
    __name__ = 'gnuhealth.prescription.order'
    
    serializer = fields.Text('Doc String', readonly=True)

    document_digest = fields.Char('Digest', readonly=True,
        help="Original Document Digest")

    digest_status = fields.Function(fields.Boolean('Altered',
        states={
        'invisible': Not(Equal(Eval('state'),'done')),
        },
        help="This field will be set whenever parts of" \
        " the main original document has been changed." \
        " Please note that the verification is done only on selected" \
        " fields." ),
        'check_digest')

    serializer_current = fields.Function(fields.Text('Current Doc',
            states={
            'invisible': Not(Bool(Eval('digest_status'))),
            }),
        'check_digest')

        
    digest_current = fields.Function(fields.Char('Current Hash',
            states={
            'invisible': Not(Bool(Eval('digest_status'))),
            }),
        'check_digest')

    digital_signature = fields.Text('Digital Signature', readonly=True)


    @staticmethod
    def default_state():
        return 'draft'

    @classmethod
    def __setup__(cls):
        super(PatientPrescriptionOrder, cls).__setup__()
        cls._buttons.update({
            'generate_prescription': {
                'invisible': Equal(Eval('state'), 'validated'),
            },
            'create_prescription': {
                'invisible': Or(Equal(Eval('state'), 'done'),
                    Equal(Eval('state'), 'validated'))
            },

            })
        ''' Allow calling the set_signature method via RPC '''
        cls.__rpc__.update({
                'set_signature': RPC(readonly=False),
                })

    @classmethod
    @ModelView.button
    def generate_prescription(cls, prescriptions):
        prescription = prescriptions[0]

        # Change the state of the prescription to "Validated"

        serial_doc=cls.get_serial(prescription)
        
        cls.write(prescriptions, {
            'serializer': serial_doc,
            'document_digest': HealthCrypto().gen_hash(serial_doc),
            'state': 'validated',})


    @classmethod
    def get_serial(cls,prescription):

        presc_line=[]
        
        for line in prescription.prescription_line:
            line_elements=[line.medicament and line.medicament.name.name or '',
                line.dose or '', 
                line.route and line.route.name or '',
                line.form and line.form.name or '',
                line.indication and line.indication.name or '',
                line.short_comment or '']
                
            presc_line.append(line_elements)

        data_to_serialize = { 
            'Prescription': str(prescription.prescription_id) or '',
            'Date': str(prescription.prescription_date) or '',
            'HP': str(prescription.healthprof.rec_name),
            'Patient': str(prescription.patient.rec_name),
            'Patient_ID': str(prescription.patient.name.ref) or '',
            'Prescription_line': str(presc_line),
            'Notes': str(prescription.notes),
             }

        serialized_doc = str(HealthCrypto().serialize(data_to_serialize))
        
        return serialized_doc
    
    @classmethod
    def set_signature(cls, data, signature):
        """
        Set the clearsigned signature
        """
        
            
        doc_id = data['id']
        
        cls.write([cls(doc_id)], {
            'digital_signature': signature,
            })



    def check_digest (self,name):
        result=''
        serial_doc=self.get_serial(self)
        if (name == 'digest_status' and self.document_digest):
            if (HealthCrypto().gen_hash(serial_doc) == self.document_digest):
                result = False
            else:
                ''' Return true if the document has been altered'''
                result = True
        if (name=='digest_current'):
            result = HealthCrypto().gen_hash(serial_doc)

        if (name=='serializer_current'):
            result = serial_doc
            
        return result
 
    # Hide the group holding validation information when state is 
    # not validated
    
    @classmethod
    def view_attributes(cls):
        return [('//group[@id="prescription_digest"]', 'states', {
                'invisible': Not(Eval('state') == 'validated'),
                })]
       

class BirthCertificate(ModelSQL, ModelView):
    
    __name__ = 'gnuhealth.birth_certificate'
    
    serializer = fields.Text('Doc String', readonly=True)

    document_digest = fields.Char('Digest', readonly=True,
        help="Original Document Digest")
    
    digest_status = fields.Function(fields.Boolean('Altered',
        states={
        'invisible': Not(Equal(Eval('state'),'done')),
        },
        help="This field will be set whenever parts of" \
        " the main original document has been changed." \
        " Please note that the verification is done only on selected" \
        " fields." ),
        'check_digest')

    serializer_current = fields.Function(fields.Text('Current Doc',
            states={
            'invisible': Not(Bool(Eval('digest_status'))),
            }),
        'check_digest')

        
    digest_current = fields.Function(fields.Char('Current Hash',
            states={
            'invisible': Not(Bool(Eval('digest_status'))),
            }),
        'check_digest')

    digital_signature = fields.Text('Digital Signature', readonly=True)

    @classmethod

    def __setup__(cls):
        super(BirthCertificate, cls).__setup__()
        cls._buttons.update({
            'generate_birth_certificate': {
                'invisible': Not(Equal(Eval('state'), 'signed'))},
            })
        ''' Allow calling the set_signature method via RPC '''
        cls.__rpc__.update({
                'set_signature': RPC(readonly=False),
                })

    @classmethod
    @ModelView.button
    def generate_birth_certificate(cls, certificates):
        certificate = certificates[0]
        HealthProf = Pool().get('gnuhealth.healthprofessional')

        # Change the state of the certificate to "Done"

        serial_doc=cls.get_serial(certificate)
        
        signing_hp = HealthProf.get_health_professional()
        if not signing_hp:
            cls.raise_user_error(
                "No health professional associated to this user !")

        cls.write(certificates, {
            'serializer': serial_doc,
            'document_digest': HealthCrypto().gen_hash(serial_doc),
            'state': 'done',})


    @classmethod
    def get_serial(cls,certificate):

        data_to_serialize = { 
            'certificate': str(certificate.code) or '',
            'Date': str(certificate.dob) or '',
            'HP': certificate.signed_by \
                and str(certificate.signed_by.rec_name) or '',
            'Person':str(certificate.name.rec_name),
            'Person_dob':str(certificate.name.dob) or '',
            'Person_ID': str(certificate.name.ref) or '',
            'Country': str(certificate.country.rec_name) or '',
            'Country_subdivision': certificate.country_subdivision \
                and str(certificate.country_subdivision.rec_name) or '',
            'Mother': certificate.mother \
                and str(certificate.mother.rec_name) or '',
            'Father': certificate.father \
                and str(certificate.father.rec_name) or '',
            'Observations': str(certificate.observations),
             }

        serialized_doc = str(HealthCrypto().serialize(data_to_serialize))
        
        return serialized_doc
    
    @classmethod
    def set_signature(cls, data, signature):
        """
        Set the clearsigned signature
        """
        doc_id = data['id']
        
        cls.write([cls(doc_id)], {
            'digital_signature': signature,
            })

    def check_digest (self,name):
        result=''
        serial_doc=self.get_serial(self)
        if (name == 'digest_status' and self.document_digest):
            if (HealthCrypto().gen_hash(serial_doc) == self.document_digest):
                result = False
            else:
                ''' Return true if the document has been altered'''
                result = True
        if (name=='digest_current'):
            result = HealthCrypto().gen_hash(serial_doc)

        if (name=='serializer_current'):
            result = serial_doc
            
        return result

    # Hide the group holding all the digital signature until signed
        
    @classmethod
    def view_attributes(cls):
        return [('//group[@id="group_current_string"]', 'states', {
                'invisible': ~Eval('digest_status'),
                })]

class DeathCertificate(ModelSQL, ModelView):
    
    __name__ = 'gnuhealth.death_certificate'
    
    serializer = fields.Text('Doc String', readonly=True)

    document_digest = fields.Char('Digest', readonly=True,
        help="Original Document Digest")
    
    digest_status = fields.Function(fields.Boolean('Altered',
        states={
        'invisible': Not(Equal(Eval('state'),'done')),
        },
        help="This field will be set whenever parts of" \
        " the main original document has been changed." \
        " Please note that the verification is done only on selected" \
        " fields." ),
        'check_digest')

    serializer_current = fields.Function(fields.Text('Current Doc',
            states={
            'invisible': Not(Bool(Eval('digest_status'))),
            }),
        'check_digest')

        
    digest_current = fields.Function(fields.Char('Current Hash',
            states={
            'invisible': Not(Bool(Eval('digest_status'))),
            }),
        'check_digest')

    digital_signature = fields.Text('Digital Signature', readonly=True)

    @classmethod
    def __setup__(cls):
        super(DeathCertificate, cls).__setup__()
        cls._buttons.update({
            'generate_death_certificate': {
                'invisible': Not(Equal(Eval('state'), 'signed')),
                },
            })
        ''' Allow calling the set_signature method via RPC '''
        cls.__rpc__.update({
                'set_signature': RPC(readonly=False),
                })

    @classmethod
    @ModelView.button
    def generate_death_certificate(cls, certificates):
        certificate = certificates[0]
        HealthProf = Pool().get('gnuhealth.healthprofessional')

        # Change the state of the certificate to "Done"

        serial_doc=cls.get_serial(certificate)
        
        signing_hp = HealthProf.get_health_professional()
        if not signing_hp:
            cls.raise_user_error(
                "No health professional associated to this user !")

        cls.write(certificates, {
            'serializer': serial_doc,
            'document_digest': HealthCrypto().gen_hash(serial_doc),
            'state': 'done',})


    @classmethod
    def get_serial(cls,certificate):

        underlying_conds =[]
        
        for condition in certificate.underlying_conditions:
            cond = []
            cond = [str(condition.condition.rec_name),
                condition.interval,
                condition.unit_of_time]
                
            underlying_conds.append(cond)

        data_to_serialize = { 
            'certificate': str(certificate.code) or '',
            'Date': str(certificate.dod) or '',
            'HP': certificate.signed_by \
                and str(certificate.signed_by.rec_name) or '',
            'Person': str(certificate.name.rec_name),
            'Person_dob':str(certificate.name.dob) or '',
            'Person_ID': str(certificate.name.ref) or '',
            'Cod': str(certificate.cod.rec_name),
            'Underlying_conditions': underlying_conds or '',    
            'Autopsy': certificate.autopsy,
            'Type_of_death': str(certificate.type_of_death),
            'Place_of_death': str(certificate.place_of_death),
            'Country': str(certificate.country.rec_name) or '',
            'Country_subdivision': certificate.country_subdivision \
                and str(certificate.country_subdivision.rec_name) or '',
            'Observations': str(certificate.observations),
             }

        serialized_doc = str(HealthCrypto().serialize(data_to_serialize))
        
        return serialized_doc
    
    @classmethod
    def set_signature(cls, data, signature):
        """
        Set the clearsigned signature
        """
        doc_id = data['id']
        
        cls.write([cls(doc_id)], {
            'digital_signature': signature,
            })

    def check_digest (self,name):
        result=''
        serial_doc=self.get_serial(self)
        if (name == 'digest_status' and self.document_digest):
            if (HealthCrypto().gen_hash(serial_doc) == self.document_digest):
                result = False
            else:
                ''' Return true if the document has been altered'''
                result = True
        if (name=='digest_current'):
            result = HealthCrypto().gen_hash(serial_doc.encode('uft-8'))

        if (name=='serializer_current'):
            result = serial_doc
            
        return result

    # Hide the group holding all the digital signature until signed
        
    @classmethod
    def view_attributes(cls):
        return [('//group[@id="group_current_string"]', 'states', {
                'invisible': ~Eval('digest_status'),
                })]

class PatientEvaluation(ModelSQL, ModelView):
    __name__ = 'gnuhealth.patient.evaluation'
    
    serializer = fields.Text('Doc String', readonly=True)

    document_digest = fields.Char('Digest', readonly=True,
        help="Original Document Digest")
    
    digest_status = fields.Function(fields.Boolean('Altered',
        states={
        'invisible': Not(Equal(Eval('state'),'signed')),
        },
        help="This field will be set whenever parts of" \
        " the main original document has been changed." \
        " Please note that the verification is done only on selected" \
        " fields." ),
        'check_digest')

    serializer_current = fields.Function(fields.Text('Current Doc',
            states={
            'invisible': Not(Bool(Eval('digest_status'))),
            }),
        'check_digest')

        
    digest_current = fields.Function(fields.Char('Current Hash',
            states={
            'invisible': Not(Bool(Eval('digest_status'))),
            }),
        'check_digest')

    digital_signature = fields.Text('Digital Signature', readonly=True)

    @classmethod
    def __setup__(cls):
        super(PatientEvaluation, cls).__setup__()
        cls._buttons.update({
            'sign_evaluation': {
                'invisible': Not(Equal(Eval('state'), 'done')),
                },
            })
        ''' Allow calling the set_signature method via RPC '''
        cls.__rpc__.update({
                'set_signature': RPC(readonly=False),
                })


    @classmethod
    @ModelView.button
    def sign_evaluation(cls, evaluations):
        evaluation = evaluations[0]

        HealthProf= Pool().get('gnuhealth.healthprofessional')
        
        # Change the state of the evaluation to "Signed"
        # Include signing health professional 
        
        serial_doc=cls.get_serial(evaluation)


        signing_hp = HealthProf.get_health_professional()
        if not signing_hp:
            cls.raise_user_error(
                "No health professional associated to this user !")



        cls.write(evaluations, {
            'serializer': serial_doc,
            'document_digest': HealthCrypto().gen_hash(serial_doc),
            'state': 'signed',})


    @classmethod
    def get_serial(cls,evaluation):

        signs_symptoms =[]
        secondary_conditions =[]
        diagnostic_hypotheses =[]
        procedures =[]
        
        for sign_symptom in evaluation.signs_and_symptoms:
            finding = []
            finding = [sign_symptom.clinical.rec_name,
                sign_symptom.sign_or_symptom,
                ]
                
            signs_symptoms.append(finding)

        for secondary_condition in evaluation.secondary_conditions:
            sc = []
            sc = [secondary_condition.pathology.rec_name]
                
            secondary_conditions.append(sc)

        for ddx in evaluation.diagnostic_hypothesis:
            dx = []
            dx = [ddx.pathology.rec_name]
                
            diagnostic_hypotheses.append(dx)

        for procedure in evaluation.actions:
            proc = []
            proc = [procedure.procedure.rec_name]
                
            procedures.append(proc)

        data_to_serialize = { 
            'Patient': str(evaluation.patient.rec_name) or '',
            'Start': str(evaluation.evaluation_start) or '',
            'End': str(evaluation.evaluation_endtime) or '',
            'Initiated_by': str(evaluation.healthprof.rec_name),
            'Signed_by': evaluation.signed_by and
                str(evaluation.signed_by.rec_name) or '',
            'Specialty': evaluation.specialty and
                str(evaluation.specialty.rec_name) or '',
            'Visit_type': str(evaluation.visit_type) or '',
            'Urgency': str(evaluation.urgency) or '',
            'Information_source': str(evaluation.information_source) or '',
            'Reliable_info': evaluation.reliable_info,
            'Chief_complaint': str(evaluation.chief_complaint) or '',
            'Present_illness': str(evaluation.present_illness) or '',
            'Evaluation_summary': str(evaluation.evaluation_summary),
            'Signs_and_Symptoms': signs_symptoms or '',
            'Glycemia': evaluation.glycemia or '',
            'Hba1c': evaluation.hba1c or '',
            'Total_Cholesterol': evaluation.cholesterol_total or '',
            'HDL': evaluation.hdl or '',
            'LDL': evaluation.ldl or '',
            'TAG': evaluation.ldl or '',
            'Systolic': evaluation.systolic or '',
            'Diastolic': evaluation.diastolic or '',
            'BPM': evaluation.bpm or '',
            'Respiratory_rate': evaluation.respiratory_rate or '',
            'Osat': evaluation.osat or '',
            'BPM': evaluation.bpm or '',
            'Malnutrition': evaluation.malnutrition,
            'Dehydration': evaluation.dehydration,
            'Temperature': evaluation.temperature,
            'Weight': evaluation.weight or '',
            'Height': evaluation.height or '',
            'BMI': evaluation.bmi or '',
            'Head_circ': evaluation.head_circumference or '',
            'Abdominal_cir': evaluation.abdominal_circ or '',
            'Hip': evaluation.hip or '',
            'WHR': evaluation.whr or '',
            'Abdominal_cir': evaluation.abdominal_circ or '',
            'Loc': evaluation.loc or '',
            'Loc_eyes': evaluation.loc_eyes or '',
            'Loc_verbal': evaluation.loc_verbal or '',
            'Loc_motor': evaluation.loc_motor or '',
            'Tremor': evaluation.tremor,
            'Violent': evaluation.violent,
            'Mood': str(evaluation.mood) or '',
            'Orientation':evaluation.orientation,
            'Orientation':evaluation.orientation,
            'Memory':evaluation.memory,
            'Knowledge_current_events':evaluation.knowledge_current_events,
            'Judgment':evaluation.judgment,
            'Abstraction':evaluation.abstraction,
            'Vocabulary':evaluation.vocabulary,
            'Calculation':evaluation.calculation_ability,
            'Object_recognition':evaluation.object_recognition,
            'Praxis':evaluation.praxis,
            'Diagnosis':evaluation.diagnosis and
                str(evaluation.diagnosis.rec_name) or '',
            'Secondary_conditions': secondary_conditions or '',
            'DDX': diagnostic_hypotheses or '',
            'Info_Diagnosis':str(evaluation.info_diagnosis) or '',
            'Treatment_plan':str(evaluation.directions) or '',
            'Procedures': procedures or '',
            'Institution': evaluation.institution and
                str(evaluation.institution.rec_name) or '',
            'Derived_from': evaluation.derived_from and
                str(evaluation.derived_from.rec_name) or '',
            'Derived_to':evaluation.derived_to and
                str(evaluation.derived_to.rec_name) or '',
             }

        serialized_doc = str(HealthCrypto().serialize(data_to_serialize))
        
        return serialized_doc
    
    @classmethod
    def set_signature(cls, data, signature):
        """
        Set the clearsigned signature
        """
        doc_id = data['id']
        
        cls.write([cls(doc_id)], {
            'digital_signature': signature,
            })

    def check_digest (self,name):
        result=''
        serial_doc=str(self.get_serial(self))
        if (name == 'digest_status' and self.document_digest):
            if (HealthCrypto().gen_hash(serial_doc) == self.document_digest):
                result = False
            else:
                ''' Return true if the document has been altered'''
                result = True
        if (name=='digest_current'):
            result = HealthCrypto().gen_hash(serial_doc)

        if (name=='serializer_current'):
            result = serial_doc
            
        return result
    # Hide the group holding all the digital signature until signed
        
    @classmethod
    def view_attributes(cls):
        return [('//group[@id="group_digital_signature"]', 'states', {
                'invisible': ~Eval('digital_signature')}),
                ('//group[@id="group_current_string"]', 'states', {
                'invisible': ~Eval('digest_status'),
                })]
