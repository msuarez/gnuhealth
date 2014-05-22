# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    Copyright (C) 2008-2014 Luis Falcon <lfalcon@gnusolidario.org>
#    Copyright (C) 2011-2014 GNU Solidario <health@gnusolidario.org>
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
from trytond.pyson import Eval, Not, Bool, PYSONEncoder, Equal, And
import hashlib
import json

__all__ = ['HealthCrypto','PatientPrescriptionOrder']


class HealthCrypto:
    """ GNU Health Cryptographic functions
    """

    def serialize(self,data_to_serialize):
        """ Format to JSON """
        json_output = json.dumps(data_to_serialize)
        return json_output

    def gen_hash(self, serialized_doc):
        return hashlib.sha512(serialized_doc).hexdigest()


class PatientPrescriptionOrder(ModelSQL, ModelView):
    """ Add the serialized and hash fields to the
    prescription order document"""
    
    __name__ = 'gnuhealth.prescription.order'
    
    serializer = fields.Text('Doc String', readonly=True)

    document_digest = fields.Char('Digest', readonly=True,
        help="Original Document Digest")
    
    state = fields.Selection([
        ('draft', 'Draft'),
        ('done', 'Done'),
        ], 'State', readonly=True, sort=False)


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
        cls._buttons.update({
            'generate_prescription': {
                'invisible': Equal(Eval('state'), 'done'),
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

        # Change the state of the evaluation to "Done"
        # and write the name of the signing health professional

        serial_doc=cls.get_serial(prescription)
        

        cls.write(prescriptions, {
            'serializer': serial_doc,
            'document_digest': HealthCrypto().gen_hash(serial_doc),
            'state': 'done',})


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
            'Prescription': prescription.prescription_id or '',
            'Date': str(prescription.prescription_date) or '',
            'HP': ','.join([prescription.healthprof.name.lastname,
                prescription.healthprof.name.name]),
            'Patient':','.join([prescription.patient.lastname, prescription.patient.name.name]),
            'Patient_ID': prescription.patient.name.ref or '',
            'Prescription_line': str(presc_line),
            'Notes': str(prescription.notes),
             }

        serialized_doc = HealthCrypto().serialize(data_to_serialize)
        
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
        
