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
from trytond.model import ModelView, ModelSQL, fields, Unique
from trytond.transaction import Transaction
from trytond.pyson import Eval, Not, Bool, PYSONEncoder, Equal, And, Or, If
from trytond import backend


__all__ = ['DiseaseGene', 'ProteinDisease', 'GeneVariant','GeneVariantPhenotype',
            'PatientGeneticRisk', 'FamilyDiseases', 'GnuHealthPatient']


class DiseaseGene(ModelSQL, ModelView):
    'Disease Genes'
    __name__ = 'gnuhealth.disease.gene'

    name = fields.Char('Gene Name', required=True,select=True)
    protein_name = fields.Char('Protein Code', 
        help="Encoding Protein Code, such as UniProt protein name", 
        select=True)
    long_name = fields.Char('Official Long Name', translate=True)
    gene_id = fields.Char('Gene ID',
        help="default code from NCBI Entrez database.", select=True)
    chromosome = fields.Char('Chromosome',
        help="Name of the affected chromosome", select=True)
    location = fields.Char('Location', help="Locus of the chromosome")

    info = fields.Text('Information', help="Extra Information")
    variants = fields.One2Many('gnuhealth.gene.variant', 'name',
     'Variants')
        
    protein_uri = fields.Function(fields.Char("Protein URI"),
     'get_protein_uri')
    
    def get_protein_uri(self, name):
        ret_url=''
        if (self.protein_name):
            ret_url = 'http://www.uniprot.org/uniprot/' + \
                str(self.protein_name)
        return ret_url

    @classmethod
    def __setup__(cls):
        super(DiseaseGene, cls).__setup__()

        t = cls.__table__()
        cls._sql_constraints = [
            ('name_unique', Unique(t,t.name),
                'The Official Symbol name must be unique'),
            ]

    def get_rec_name(self, name):
        return self.name + ':' + self.long_name

    @classmethod
    def search_rec_name(cls, name, clause):
        # Search for the official and long name
        field = None
        for field in ('name', 'long_name'):
            parties = cls.search([(field,) + tuple(clause[1:])], limit=1)
            if parties:
                break
        if parties:
            return [(field,) + tuple(clause[1:])]
        return [(cls._rec_name,) + tuple(clause[1:])]

    @classmethod
    # Update to version 3.2
    def __register__(cls, module_name):
        super(DiseaseGene, cls).__register__(module_name)

        cursor = Transaction().connection.cursor()
        TableHandler = backend.get('TableHandler')
        table = TableHandler(cls, module_name)
        # Insert the current "specialty" associated to the HP in the
        # table that keeps the specialties associated to different health
        # professionals, gnuhealth.hp_specialty

        if table.column_exist('dominance'):
            # Drop old specialty column
            # which is now part of the gene variant phenotype
            table.drop_column('dominance')


class ProteinDisease(ModelSQL, ModelView):
    'Protein related disorders'
    __name__ = 'gnuhealth.protein.disease'

    name = fields.Char('Disease', required=True,select=True,
        help="Uniprot Disease Code")
        
    disease_name = fields.Char('Disease name', translate=True)
    acronym = fields.Char('Acronym', required=True,select=True,
        help="Disease acronym / mnemonics")

    disease_uri = fields.Function(fields.Char("Disease URI"),
     'get_disease_uri')

    mim_reference = fields.Char('MIM', help="MIM -Mendelian Inheritance in Man- DB reference)")

    gene_variant = fields.One2Many('gnuhealth.gene.variant.phenotype', 'phenotype',
        'Gene Variants', help="Gene variants involved in this condition")
        
    dominance = fields.Selection([
        (None, ''),
        ('d', 'dominant'),
        ('r', 'recessive'),
        ('c', 'codominance'),
        ], 'Dominance', select=True)


    description = fields.Text('Description')        
    

    def get_disease_uri(self, name):
        ret_url=''
        if (self.name):
            ret_url = 'http://www.uniprot.org/diseases/' + \
                str(self.name)
        return ret_url

    @classmethod
    def __setup__(cls):
        super(ProteinDisease, cls).__setup__()

        t = cls.__table__()
        cls._sql_constraints = [
            ('name_unique', Unique(t,t.name),
                'The Disease Code  name must be unique'),
            ]

    def get_rec_name(self, name):
        return self.name + ':' + self.disease_name

    @classmethod
    def search_rec_name(cls, name, clause):
        # Search for the disease code or disease name
        field = None
        for field in ('name', 'disease_name'):
            parties = cls.search([(field,) + tuple(clause[1:])], limit=1)
            if parties:
                break
        if parties:
            return [(field,) + tuple(clause[1:])]
        return [(cls._rec_name,) + tuple(clause[1:])]

class GeneVariant(ModelSQL, ModelView):
    'Gene Sequence Variant'
    __name__ = 'gnuhealth.gene.variant'

    name = fields.Many2One('gnuhealth.disease.gene', 'Gene',
        required=True)
    variant = fields.Char("Variant", required=True, select=True)
    aa_change = fields.Char('Change', help="Resulting amino acid change")
    phenotypes = fields.One2Many('gnuhealth.gene.variant.phenotype', 'variant',
     'Phenotypes')
        
    @classmethod
    def __setup__(cls):
        super(GeneVariant, cls).__setup__()

        t = cls.__table__()
        cls._sql_constraints = [
            ('variant_unique', Unique(t,t.variant),
                'The variant ID must be unique'),
            ('aa_unique', Unique(t,t.variant,t.aa_change),
                'The resulting AA change for this gene already exists'),
            ]

    def get_rec_name(self, name):
        return self.name.rec_name + " : " + self.variant + " : " + self.aa_change


class GeneVariantPhenotype(ModelSQL, ModelView):
    'Gene Sequence Variant Phenotypes'
    __name__ = 'gnuhealth.gene.variant.phenotype'

    name = fields.Char('Code', required=True)
    variant = fields.Many2One('gnuhealth.gene.variant', 'Variant',
        required=True)
 
    gene = fields.Function(fields.Many2One(
        'gnuhealth.disease.gene', 'Gene',
        depends=['variant']),'get_gene',
        searcher='search_gene')

    phenotype = fields.Many2One('gnuhealth.protein.disease', 'Phenotype',
        required=True)


    def get_gene(self, name):
        if (self.variant):
            return self.variant.name.id


    def get_rec_name(self, name):
        if self.phenotype:
            return self.phenotype.rec_name

    @classmethod
    def search_rec_name(cls, name, clause):
        return [('phenotype',) + tuple(clause[1:])]

    @classmethod
    def search_gene(cls, name, clause):
        res = []
        value = clause[2]
        res.append(('variant.name', clause[1], value))
        return res

    @classmethod
    def __setup__(cls):
        super(GeneVariantPhenotype, cls).__setup__()

        t = cls.__table__()
        cls._sql_constraints = [
            ('code', Unique(t,t.name),
                'This code already exists'),
            ]


class PatientGeneticRisk(ModelSQL, ModelView):
    'Patient Genetic Information'
    __name__ = 'gnuhealth.patient.genetic.risk'

    patient = fields.Many2One('gnuhealth.patient', 'Patient', select=True)
    disease_gene = fields.Many2One('gnuhealth.disease.gene',
        'Disease Gene', required=True)
    natural_variant = fields.Many2One('gnuhealth.gene.variant', 'Variant',
        domain=[('name', '=', Eval('disease_gene'))],
        depends=['disease_gene'])
    variant_phenotype = fields.Many2One('gnuhealth.gene.variant.phenotype',\
        'Phenotype',
        domain=[('variant', '=', Eval('natural_variant'))],
        depends=['natural_variant'])
    onset = fields.Integer('Onset', help="Age in years")
    
    notes = fields.Char("Notes")

class FamilyDiseases(ModelSQL, ModelView):
    'Family Diseases'
    __name__ = 'gnuhealth.patient.family.diseases'

    patient = fields.Many2One('gnuhealth.patient', 'Patient', select=True)
    name = fields.Many2One('gnuhealth.pathology', 'Condition', required=True)
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
        help='First degree = siblings, mother and father\n'
            'Second degree = Uncles, nephews and Nieces\n'
            'Third degree = Grandparents and cousins',
        required=True)


class GnuHealthPatient (ModelSQL, ModelView):
    'Add to the Medical patient_data class (gnuhealth.patient) the genetic ' \
    'and family risks'
    __name__ = 'gnuhealth.patient'

    genetic_risks = fields.One2Many('gnuhealth.patient.genetic.risk',
        'patient', 'Genetic Information')
    family_history = fields.One2Many('gnuhealth.patient.family.diseases',
        'patient', 'Family History')
