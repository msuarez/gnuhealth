# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    Copyright (C) 2008-2013  Luis Falcon <falcon@gnu.org>
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
import qrcode
import StringIO
from trytond.model import ModelView, ModelSQL, fields


__all__ = ['Patient', 'Newborn']


# Add the QR field and QR image in the patient model

class Patient(ModelSQL, ModelView):
    'Patient'
    __name__ = 'gnuhealth.patient'

    def make_qrcode(self, name):
# Create the QR code

        patient_ssn = self.ssn or ''

        patient_blood_type = self.blood_type or ''

        patient_rh = self.rh or ''

        patient_sex = self.sex or ''

        patient_dob = self.dob or ''

        patient_id = self.identification_code or ''

        if self.lastname:
            patient_lastname = self.lastname + ', '
        else:
            patient_lastname = ''

        qr_string = 'ID: ' + patient_id \
            + '\nName: ' + patient_lastname + ',' \
                + self.name.name \
            + '\nSSN: ' + patient_ssn \
            + '\nSex: ' + patient_sex \
            + '\nDoB: ' + str(patient_dob) \
            + '\nBlood Type: ' + patient_blood_type \
                + ' ' + patient_rh

        qr_image = qrcode.make(qr_string)

# Make a PNG image from PIL without the need to create a temp file
        holder = StringIO.StringIO()
        qr_image.save(holder)
        qr_png = holder.getvalue()
        holder.close()

        return  buffer(qr_png)

# Add the QR Code to the Patient
    qr = fields.Function(fields.Binary('QR Code'), 'make_qrcode')


# Add the QR code field and image to the Newborn

class Newborn(ModelSQL, ModelView):
    'NewBorn'
    __name__ = 'gnuhealth.newborn'

    def make_qrcode(self, name):
# Create the QR code

        if self.mother:
            if self.mother.name.lastname:
                newborn_mother_lastname = self.mother.name.lastname + ', '
            else:
                newborn_mother_lastname = ''

            newborn_mother_name = self.mother.name.name or ''

            newborn_mother_id = self.mother.identification_code or ''

        else:
            newborn_mother_lastname = ''
            newborn_mother_name = ''
            newborn_mother_id = ''

        newborn_name = self.name or ''

        newborn_sex = self.sex or ''

        newborn_birth_date = self.birth_date or ''

        qr_string = 'ID: ' + newborn_name \
            + '\nMother: ' + newborn_mother_lastname \
                    + newborn_mother_name \
            + '\nMother\'s ID: ' + newborn_mother_id \
            + '\nSex: ' + newborn_sex \
            + '\nDoB: ' + str(newborn_birth_date)

        qr_image = qrcode.make(qr_string)

# Make a PNG image from PIL without the need to create a temp file
        holder = StringIO.StringIO()
        qr_image.save(holder)
        qr_png = holder.getvalue()
        holder.close()

        return buffer(qr_png)

# Add the QR Code to the Newborn
    qr = fields.Function(fields.Binary('QR Code'), 'make_qrcode')

