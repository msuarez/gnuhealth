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


__all__ = ['DiseaseGene', 'PatientGeneticRisk', 'FamilyDiseases',
    'GnuHealthPatient']


class DiseaseGene(ModelSQL, ModelView):
    'Disease Genes'
    __name__ = 'gnuhealth.disease.gene'

    name = fields.Char('Official Symbol', required=True,select=True)
    long_name = fields.Char('Official Long Name', select=True)
    gene_id = fields.Char('Gene ID',
        help="default code from NCBI Entrez database.", select=True)
    chromosome = fields.Char('Affected Chromosome',
        help="Name of the affected chromosome", select=True)
    location = fields.Char('Location', help="Locus of the chromosome")
    dominance = fields.Selection([
        (None, ''),
        ('d', 'dominant'),
        ('r', 'recessive'),
        ], 'Dominance', select=True)
    info = fields.Text('Information', help="Extra Information")

    @classmethod
    def __setup__(cls):
        super(DiseaseGene, cls).__setup__()
        cls._sql_constraints = [
            ('name_uniq', 'UNIQUE(name)', 
            'The Official Symbol name must be unique !'),
        ]

    def get_rec_name(self, name):
        return self.name + ':' + self.long_name

    @classmethod
    def search_rec_name(cls, name, clause):
        """ Search for the official and long name"""
        field = None
        for field in ('name', 'long_name'):
            parties = cls.search([(field,) + tuple(clause[1:])], limit=1)
            if parties:
                break
        if parties:
            return [(field,) + tuple(clause[1:])]
        return [(cls._rec_name,) + tuple(clause[1:])]


class PatientGeneticRisk(ModelSQL, ModelView):
    'Patient Genetic Risks'
    __name__ = 'gnuhealth.patient.genetic.risk'

    patient = fields.Many2One('gnuhealth.patient', 'Patient', select=True)
    disease_gene = fields.Many2One('gnuhealth.disease.gene',
        'Disease Gene', required=True)
    notes = fields.Char("Notes")

class FamilyDiseases(ModelSQL, ModelView):
    'Family Diseases'
    __name__ = 'gnuhealth.patient.family.diseases'

    patient = fields.Many2One('gnuhealth.patient', 'Patient', select=True)
    name = fields.Many2One('gnuhealth.pathology', 'Disease', required=True)
    xory = fields.Selection([
        (None, ''),
        ('m', 'Maternal'),
        ('f', 'Paternal'),
        ('s', 'Sibling'),
        ], 'Maternal or Paternal', select=True)

    relative = fields.Selection([
        ('mother', 'Mother'),
        ('father', 'Father'),
        ('brother', 'Brother'),
        ('sister', 'Sister'),
        ('aunt', 'Aunt'),
        ('uncle', 'Uncle'),
        ('nephew', 'Nephew'),
        ('niece', 'Niece'),
        ('grandfather', 'Grandfather'),
        ('grandmother', 'Grandmother'),
        ('cousin', 'Cousin'),
        ], 'Relative',
        help="First degree = siblings, mother and father; second degree = "
        "Uncles, nephews and Nieces; third degree = Grandparents and cousins",
        required=True)


class GnuHealthPatient (ModelSQL, ModelView):
    'Add to the Medical patient_data class (gnuhealth.patient) the genetic ' \
    'and family risks'
    __name__ = 'gnuhealth.patient'

    genetic_risks = fields.One2Many('gnuhealth.patient.genetic.risk',
        'patient', 'Genetic Risks')
    family_history = fields.One2Many('gnuhealth.patient.family.diseases',
        'patient', 'Family History')
