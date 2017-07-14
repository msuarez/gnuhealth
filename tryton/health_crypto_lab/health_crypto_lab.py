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
from datetime import datetime
from trytond.model import ModelView, ModelSQL, fields
from trytond.transaction import Transaction
from trytond.rpc import RPC
from trytond.pool import Pool
from trytond.wizard import Wizard, StateAction, StateView, Button
from trytond.pyson import Eval, Not, Bool, PYSONEncoder, Equal, And, Or
import hashlib
import json

__all__ = ['LabTest']


class LabTest(ModelSQL, ModelView):
    'Lab Test'
    __name__ = 'gnuhealth.lab'

    STATES = {'readonly': Eval('state') == 'validated'}

    serializer = fields.Text('Doc String', readonly=True)

    document_digest = fields.Char('Digest', readonly=True,
        help="Original Document Digest")

    state = fields.Selection([
        ('draft', 'Draft'),
        ('done', 'Done'),        
        ('validated', 'Validated'),        
        ], 'State', readonly=True, sort=False)


    digest_status = fields.Function(fields.Boolean('Altered',
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

    done_by = fields.Many2One(
        'gnuhealth.healthprofessional', 
        'Done by', readonly=True, help='Professional who processes this'
        ' lab test',
        states = STATES )

    done_date = fields.DateTime('Finished on', readonly=True,
        states = STATES )

    validated_by = fields.Many2One(
        'gnuhealth.healthprofessional', 
        'Validated by', readonly=True, help='Professional who validates this'
        ' lab test',
        states = STATES )

    validation_date = fields.DateTime('Validated on', readonly=True,
        states = STATES )
        
    @staticmethod
    def default_state():
        return 'draft'

    @classmethod
    def __setup__(cls):
        super(LabTest, cls).__setup__()
        cls._buttons.update({
            'generate_document': {
                'invisible': Not(Equal(Eval('state'), 'draft')),
                },
            'set_to_draft': {
                'invisible': Not(Equal(Eval('state'), 'done')),
                },
            'sign_document': {
                'invisible': Not(Equal(Eval('state'), 'done')),
                },
            })
        ''' Allow calling the set_signature method via RPC '''
        cls.__rpc__.update({
                'set_signature': RPC(readonly=False),
                })

    @classmethod
    @ModelView.button
    def generate_document(cls, documents):
        pool = Pool()
        HealthProfessional = pool.get('gnuhealth.healthprofessional')

        document = documents[0]


        # Set the document to "Done"
        # and write the name of the signing health professional

        hp = HealthProfessional.get_health_professional()
        if not hp:
            cls.raise_user_error(
                "No health professional associated to this user !")

        serial_doc=cls.get_serial(document)

        cls.write(documents, {
            'done_by': hp,
            'done_date': datetime.now(),
            'state': 'done',})

    @classmethod
    @ModelView.button
    def set_to_draft(cls, documents):
        document = documents[0]

        cls.write(documents, {
            'state': 'draft',})

    @classmethod
    @ModelView.button
    def sign_document(cls, documents):
        pool = Pool()
        HealthProfessional = pool.get('gnuhealth.healthprofessional')

        document = documents[0]

        # Validate / generate digest for the document
        # and write the name of the signing health professional

        hp = HealthProfessional.get_health_professional()
        if not hp:
            cls.raise_user_error(
                "No health professional associated to this user !")

        serial_doc=cls.get_serial(document)
        
        cls.write(documents, {
            'serializer': serial_doc,
            'document_digest': HealthCrypto().gen_hash(serial_doc),
            'validated_by': hp,
            'validation_date': datetime.now(),
            'state': 'validated',})


    @classmethod
    def get_serial(cls,document):

        analyte_line=[]
        
        for line in document.critearea:
            line_elements=[line.name or '',
                line.result or '', 
                line.result_text or '',
                line.remarks or '']
                
            analyte_line.append(line_elements)

        data_to_serialize = { 
            'Lab_test': str(document.name) or '',
            'Test': str(document.test.rec_name) or '',
            'HP': str(document.requestor.rec_name),
            'Patient': str(document.patient.rec_name),
            'Patient_ID': str(document.patient.name.ref) or '',
            'Analyte_line': str(analyte_line),
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
        return [('//group[@id="document_digest"]', 'states', {
                'invisible': Not(Eval('state') == 'validated'),
                })]
       



class HealthCrypto:
    """ GNU Health Cryptographic functions
    """

    def serialize(self,data_to_serialize):
        """ Format to JSON """

        json_output = \
            json.dumps(data_to_serialize,ensure_ascii=False)
        return json_output

    def gen_hash(self, serialized_doc):
        return hashlib.sha512(serialized_doc.encode('utf-8')).hexdigest()


