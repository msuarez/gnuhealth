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
import qrcode
import barcode
import io
from trytond.model import ModelView, ModelSQL, fields


__all__ = ['Patient', 'Appointment', 'Newborn','LabTest']


# Add the QR field and QR image in the patient model

class Patient(ModelSQL, ModelView):
    'Patient'
    __name__ = 'gnuhealth.patient'

    # Add the QR Code to the Patient
    qr = fields.Function(fields.Binary('QR Code'), 'make_qrcode')

    def make_qrcode(self, name):
    # Create the QR code

        patient_puid = self.puid or ''

        patient_blood_type = self.blood_type or ''

        patient_rh = self.rh or ''

        patient_gender = self.gender or ''

        patient_dob = self.dob or ''

        patient_id = self.puid or ''

        if self.lastname:
            patient_lastname = self.lastname + ', '
        else:
            patient_lastname = ''

        qr_string = 'ID: ' + patient_id \
            + '\nName: ' + patient_lastname + ',' \
                + self.name.name \
            + '\nPUID: ' + patient_puid \
            + '\nGender: ' + patient_gender \
            + '\nDoB: ' + str(patient_dob) \
            + '\nBlood Type: ' + patient_blood_type \
                + ' ' + patient_rh

        
        qr_image = qrcode.make(qr_string)
         
        # Make a PNG image from PIL without the need to create a temp file

        holder = io.BytesIO()
        qr_image.save(holder)
        qr_png = holder.getvalue()
        holder.close()

        return bytearray(qr_png)
        

# Add the QR field and QR image in the appointment model

class Appointment(ModelSQL, ModelView):
    __name__ = 'gnuhealth.appointment'

    # Add the QR Code to the Appointment
    qr = fields.Function(fields.Binary('QR Code'), 'make_qrcode')

    def make_qrcode(self, name):
    # Create the QR code

        appointment_healthprof = ''
        appointment_patient = ''
        patient_puid = ''
        appointment_specialty = ''
        appointment_date = ''
        appointment = ''
        
        if (self.name):
            appointment = self.name

        if (self.healthprof):
            appointment_healthprof = str(self.healthprof.rec_name) or ''

        if (self.patient):
            appointment_patient = self.patient.rec_name or ''
            patient_puid = self.patient.puid
            
        if (self.appointment_date):
            appointment_date = str(self.appointment_date)

        if (self.speciality):
            appointment_specialty = str(self.speciality.rec_name) or ''

        qr_string = 'ID: ' + appointment \
            + '\nName: ' + appointment_patient \
            + '\nPUID: ' + patient_puid \
            + '\nSpecialty: ' + appointment_specialty \
            + '\nhealth Prof: ' + appointment_healthprof or ''\
            + '\nDate: ' + appointment_date or ''
        
        qr_image = qrcode.make(qr_string)
         
        # Make a PNG image from PIL without the need to create a temp file

        holder = io.BytesIO()
        qr_image.save(holder)
        qr_png = holder.getvalue()
        holder.close()

        return bytearray(qr_png)



class Newborn(ModelSQL, ModelView):
    'NewBorn'
    __name__ = 'gnuhealth.newborn'

    # Add the QR Code to the Newborn
    qr = fields.Function(fields.Binary('QR Code'), 'make_qrcode')

    def make_qrcode(self, name):
    # Create the QR code

        if self.mother:
            if self.mother.name.lastname:
                newborn_mother_lastname = self.mother.name.lastname + ', '
            else:
                newborn_mother_lastname = ''

            newborn_mother_name = self.mother.name.name or ''

            newborn_mother_id = self.mother.puid or ''

        else:
            newborn_mother_lastname = ''
            newborn_mother_name = ''
            newborn_mother_id = ''

        newborn_name = self.name or ''

        newborn_sex = self.sex or ''

        newborn_birth_date = self.birth_date or ''

        qr_string = 'PUID: ' + newborn_name \
            + '\nMother: ' + newborn_mother_lastname \
                    + newborn_mother_name \
            + '\nMother\'s PUID: ' + newborn_mother_id \
            + '\nSex: ' + newborn_sex \
            + '\nDoB: ' + str(newborn_birth_date)


        qr_image = qrcode.make(qr_string)
         
        # Make a PNG image from PIL without the need to create a temp file

        holder = io.BytesIO()
        qr_image.save(holder)
        qr_png = holder.getvalue()
        holder.close()

        return bytearray(qr_png)

        
class LabTest(ModelSQL, ModelView):
    __name__ = 'gnuhealth.lab'

    # Add the QR Code to the Lab Test
    qr = fields.Function(fields.Binary('QR Code'), 'make_qrcode')
    bar = fields.Function(fields.Binary('Bar Code39'), 'make_barcode')
    
    def make_qrcode(self, name):
    # Create the QR code

        labtest_id = self.name or ''
        labtest_type = self.test or ''

        patient_puid = self.patient.puid or ''
        patient_name = self.patient.rec_name or ''

        requestor_name = self.requestor.rec_name or ''

        qr_string = 'Test ID' + labtest_id \
            + 'Test: ' + labtest_type.rec_name \
            + 'Patient ID: ' + patient_puid \
            + '\nPatient: ' + patient_name \
            + '\nRequestor: ' + requestor_name 
        
        qr_image = qrcode.make(qr_string)
         
        # Make a PNG image from PIL without the need to create a temp file

        holder = io.BytesIO()
        qr_image.save(holder)
        qr_png = holder.getvalue()
        holder.close()

        return bytearray(qr_png)


    def make_barcode(self, name):
    # Create the Code39 bar code to encode the TEST ID 
    
        labtest_id = self.name or ''
        
        CODE39 = barcode.get_barcode_class('code39')
        
        code39 = CODE39(labtest_id, add_checksum=False)
        
        # Make a PNG image from PIL without the need to create a temp file

        holder = io.BytesIO()
        code39.write(holder)
        code39_png = holder.getvalue()
        holder.close()

        return bytearray(code39_png)
