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
from trytond.pool import Pool
import hashlib


__all__ = ['HealthCrypto','PrescriptionOrder']


class HealthCrypto:
    """ GNU Health Cryptographic functions
    """

    def serialize(self,fields_to_serialize):
        return str(fields_to_serialize)

    def gen_hash(self, serialized_doc):
        
        return hashlib.sha512(serialized_doc).hexdigest()



class PrescriptionOrder(ModelSQL, ModelView):
    """ Add the serialized and hash fields to the
    prescription order document"""
    
    __name__ = 'gnuhealth.prescription.order'
    
    serialized = fields.Function(
        fields.Text('Document'), 'serialize_doc')

    document_hash = fields.Function(
        fields.Char('Hash'), 'gen_doc_hash')

    def serialize_doc(self, name):
        fields_to_serialize = [ 
            self.patient.lastname, self.prescription_id,
            self.prescription_date, self.prescription_line ]
            
        s = HealthCrypto()
        return s.serialize(fields_to_serialize)
    
    def gen_doc_hash(self, name):
        h = HealthCrypto()
        
        return h.gen_hash(self.serialized)
