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
from trytond.model import ModelView, ModelSQL, fields
from trytond.transaction import Transaction
from trytond.backend import TableHandler

__all__ = ['Party','GnuHealthPatient']


class Party (ModelSQL, ModelView):
    __name__ = 'party.party'

    occupation = fields.Many2One('gnuhealth.occupation', 'Occupation')

    education = fields.Selection([
        (None, ''),
        ('0', 'None'),
        ('1', 'Incomplete Primary School'),
        ('2', 'Primary School'),
        ('3', 'Incomplete Secondary School'),
        ('4', 'Secondary School'),
        ('5', 'University'),
        ], 'Education Level', help="Education Level", sort=False)


class GnuHealthPatient(ModelSQL, ModelView):
    __name__ = 'gnuhealth.patient'

    def get_patient_occupation(self, name):
        if (self.name.occupation):
            return self.name.occupation.id

    def get_patient_education(self, name):
        return self.name.education

    def get_patient_housing(self, name):
        if (self.name.du):
            return self.name.du.housing

    ses = fields.Selection([
        (None, ''),
        ('0', 'Lower'),
        ('1', 'Lower-middle'),
        ('2', 'Middle'),
        ('3', 'Middle-upper'),
        ('4', 'Higher'),
        ], 'Socioeconomics', help="SES - Socioeconomic Status", sort=False)

    hostile_area = fields.Boolean('Hostile Area',
        help="Check if patient lives in a zone of high hostility (eg, war)")

    single_parent = fields.Boolean('Single parent family')
    domestic_violence = fields.Boolean('Domestic violence')
    working_children = fields.Boolean('Working children')
    teenage_pregnancy = fields.Boolean('Teenage pregnancy')
    sexual_abuse = fields.Boolean('Sexual abuse')
    drug_addiction = fields.Boolean('Drug addiction')
    school_withdrawal = fields.Boolean('School withdrawal')
    prison_past = fields.Boolean('Has been in prison')
    prison_current = fields.Boolean('Is currently in prison')
    relative_in_prison = fields.Boolean('Relative in prison',
        help="Check if someone from the nuclear family - parents / " \
        "sibblings  is or has been in prison")

    ses_notes = fields.Text('Extra info')

    fam_apgar_help = fields.Selection([
        (None, ''),
        ('0', 'None'),
        ('1', 'Moderately'),
        ('2', 'Very much'),
        ], 'Help from family',
        help="Is the patient satisfied with the level of help coming from " \
        "the family when there is a problem ?", sort=False)

    fam_apgar_discussion = fields.Selection([
        (None, ''),
        ('0', 'None'),
        ('1', 'Moderately'),
        ('2', 'Very much'),
        ], 'Problems discussion',
        help="Is the patient satisfied with the level talking over the " \
        "problems as family ?", sort=False)

    fam_apgar_decisions = fields.Selection([
        (None, ''),
        ('0', 'None'),
        ('1', 'Moderately'),
        ('2', 'Very much'),
        ], 'Decision making',
        help="Is the patient satisfied with the level of making important " \
        "decisions as a group ?", sort=False)

    fam_apgar_timesharing = fields.Selection([
        (None, ''),
        ('0', 'None'),
        ('1', 'Moderately'),
        ('2', 'Very much'),
        ], 'Time sharing',
        help="Is the patient satisfied with the level of time that they " \
        "spend together ?", sort=False)

    fam_apgar_affection = fields.Selection([
        (None, ''),
        ('0', 'None'),
        ('1', 'Moderately'),
        ('2', 'Very much'),
        ], 'Family affection',
        help="Is the patient satisfied with the level of affection coming " \
        "from the family ?", sort=False)

    fam_apgar_score = fields.Integer('Score',
        help="Total Family APGAR \n" \
        "7 - 10 : Functional Family \n" \
        "4 - 6  : Some level of disfunction \n" \
        "0 - 3  : Severe disfunctional family \n",
        on_change_with=['fam_apgar_help', 'fam_apgar_timesharing',
        'fam_apgar_discussion', 'fam_apgar_decisions', 'fam_apgar_affection'])

    income = fields.Selection([
        (None, ''),
        ('h', 'High'),
        ('m', 'Medium / Average'),
        ('l', 'Low'),
        ], 'Income', sort=False)


    # GnuHealth 2.0 . Occupation and Education are now functional fields.
    # Retrives the information from the party model.
    occupation = fields.Function(fields.Many2One('gnuhealth.occupation','Occupation'), 'get_patient_occupation')

    education = fields.Function(fields.Selection([
        (None, ''),
        ('0', 'None'),
        ('1', 'Incomplete Primary School'),
        ('2', 'Primary School'),
        ('3', 'Incomplete Secondary School'),
        ('4', 'Secondary School'),
        ('5', 'University'),
        ], 'Education Level', help="Education Level", sort=False), 'get_patient_education')


    housing = fields.Function(fields.Selection([
        (None, ''),
        ('0', 'Shanty, deficient sanitary conditions'),
        ('1', 'Small, crowded but with good sanitary conditions'),
        ('2', 'Comfortable and good sanitary conditions'),
        ('3', 'Roomy and excellent sanitary conditions'),
        ('4', 'Luxury and excellent sanitary conditions'),
        ], 'Housing conditions', help="Housing and sanitary living conditions", sort=False), 'get_patient_housing')

    works_at_home = fields.Boolean('Works at home',
        help="Check if the patient works at his / her house")
    hours_outside = fields.Integer('Hours outside home',
        help="Number of hours a day the patient spend outside the house")

    @staticmethod
    def default_sewers():
        return True

    @staticmethod
    def default_water():
        return True

    @staticmethod
    def default_trash():
        return True

    @staticmethod
    def default_electricity():
        return True

    @staticmethod
    def default_gas():
        return True

    @staticmethod
    def default_telephone():
        return True

    @staticmethod
    def default_television():
        return True

    def on_change_with_fam_apgar_score(self):
        fam_apgar_help = int(self.fam_apgar_help)
        fam_apgar_timesharing = int(self.fam_apgar_timesharing or '0')
        fam_apgar_discussion = int(self.fam_apgar_discussion or '0')
        fam_apgar_decisions = int(self.fam_apgar_decisions or '0')
        fam_apgar_affection = int(self.fam_apgar_affection or '0')
        total = (fam_apgar_help + fam_apgar_timesharing +
            fam_apgar_discussion + fam_apgar_decisions +
            fam_apgar_affection)

        return total

    @classmethod
    # Update to version 2.0
    def __register__(cls, module_name):
        super(GnuHealthPatient, cls).__register__(module_name)

        cursor = Transaction().cursor
        table = TableHandler(cursor, cls, module_name)
        # Move occupation from patient to party

        if table.column_exist('occupation'):
            cursor.execute ('UPDATE PARTY_PARTY '
                'SET OCCUPATION = GNUHEALTH_PATIENT.OCCUPATION '
                'FROM GNUHEALTH_PATIENT '
                'WHERE GNUHEALTH_PATIENT.NAME = PARTY_PARTY.ID')

            table.drop_column('occupation')

        # Move education from patient to party

        if table.column_exist('education'):
            cursor.execute ('UPDATE PARTY_PARTY '
                'SET EDUCATION = GNUHEALTH_PATIENT.EDUCATION '
                'FROM GNUHEALTH_PATIENT '
                'WHERE GNUHEALTH_PATIENT.NAME = PARTY_PARTY.ID')

            table.drop_column('education')

        # The following indicators are now part of the Domiciliary Unit

        if table.column_exist('sewers'):
            table.drop_column ('sewers')

        if table.column_exist('water'):
            table.drop_column ('water')

        if table.column_exist('trash'):
            table.drop_column ('trash')

        if table.column_exist('electricity'):
            table.drop_column ('electricity')

        if table.column_exist('gas'):
            table.drop_column ('gas')

        if table.column_exist('telephone'):
            table.drop_column ('telephone')

        if table.column_exist('internet'):
            table.drop_column ('internet')

        if table.column_exist('housing'):
            table.drop_column ('housing')
