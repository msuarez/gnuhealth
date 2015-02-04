from .base_classes import *
from .support_functions import *


class AllergyIntolerance(Resource):
    """Indicates the patient has a susceptibility to an adverse reaction
    upon exposure to a specified substance.If the element is
    present, it must have either a @value, an @id, or extensions"""
    subclass = None
    superclass = Resource
    def __init__(self, id=None, extension=None, modifierExtension=None, language=None, text=None, contained=None, identifier=None, criticality=None, sensitivityType=None, recordedDate=None, status=None, subject=None, recorder=None, substance=None, reaction=None, sensitivityTest=None):
        self.original_tagname_ = None
        super(AllergyIntolerance, self).__init__(id, extension, modifierExtension, language, text, contained, )
        if identifier is None:
            self.identifier = []
        else:
            self.identifier = identifier
        self.criticality = criticality
        self.sensitivityType = sensitivityType
        self.recordedDate = recordedDate
        self.status = status
        self.subject = subject
        self.recorder = recorder
        self.substance = substance
        if reaction is None:
            self.reaction = []
        else:
            self.reaction = reaction
        if sensitivityTest is None:
            self.sensitivityTest = []
        else:
            self.sensitivityTest = sensitivityTest
    def factory(*args_, **kwargs_):
        if AllergyIntolerance.subclass:
            return AllergyIntolerance.subclass(*args_, **kwargs_)
        else:
            return AllergyIntolerance(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_identifier(self): return self.identifier
    def set_identifier(self, identifier): self.identifier = identifier
    def add_identifier(self, value): self.identifier.append(value)
    def insert_identifier(self, index, value): self.identifier[index] = value
    def get_criticality(self): return self.criticality
    def set_criticality(self, criticality): self.criticality = criticality
    def get_sensitivityType(self): return self.sensitivityType
    def set_sensitivityType(self, sensitivityType): self.sensitivityType = sensitivityType
    def get_recordedDate(self): return self.recordedDate
    def set_recordedDate(self, recordedDate): self.recordedDate = recordedDate
    def get_status(self): return self.status
    def set_status(self, status): self.status = status
    def get_subject(self): return self.subject
    def set_subject(self, subject): self.subject = subject
    def get_recorder(self): return self.recorder
    def set_recorder(self, recorder): self.recorder = recorder
    def get_substance(self): return self.substance
    def set_substance(self, substance): self.substance = substance
    def get_reaction(self): return self.reaction
    def set_reaction(self, reaction): self.reaction = reaction
    def add_reaction(self, value): self.reaction.append(value)
    def insert_reaction(self, index, value): self.reaction[index] = value
    def get_sensitivityTest(self): return self.sensitivityTest
    def set_sensitivityTest(self, sensitivityTest): self.sensitivityTest = sensitivityTest
    def add_sensitivityTest(self, value): self.sensitivityTest.append(value)
    def insert_sensitivityTest(self, index, value): self.sensitivityTest[index] = value
    def hasContent_(self):
        if (
            self.identifier or
            self.criticality is not None or
            self.sensitivityType is not None or
            self.recordedDate is not None or
            self.status is not None or
            self.subject is not None or
            self.recorder is not None or
            self.substance is not None or
            self.reaction or
            self.sensitivityTest or
            super(AllergyIntolerance, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='AllergyIntolerance', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='AllergyIntolerance')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='AllergyIntolerance', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='AllergyIntolerance'):
        super(AllergyIntolerance, self).exportAttributes(outfile, level, already_processed, namespace_, name_='AllergyIntolerance')
    def exportChildren(self, outfile, level, namespace_='', name_='AllergyIntolerance', fromsubclass_=False, pretty_print=True):
        super(AllergyIntolerance, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for identifier_ in self.identifier:
            identifier_.export(outfile, level, namespace_, name_='identifier', pretty_print=pretty_print)
        if self.criticality is not None:
            self.criticality.export(outfile, level, namespace_, name_='criticality', pretty_print=pretty_print)
        if self.sensitivityType is not None:
            self.sensitivityType.export(outfile, level, namespace_, name_='sensitivityType', pretty_print=pretty_print)
        if self.recordedDate is not None:
            self.recordedDate.export(outfile, level, namespace_, name_='recordedDate', pretty_print=pretty_print)
        if self.status is not None:
            self.status.export(outfile, level, namespace_, name_='status', pretty_print=pretty_print)
        if self.subject is not None:
            self.subject.export(outfile, level, namespace_, name_='subject', pretty_print=pretty_print)
        if self.recorder is not None:
            self.recorder.export(outfile, level, namespace_, name_='recorder', pretty_print=pretty_print)
        if self.substance is not None:
            self.substance.export(outfile, level, namespace_, name_='substance', pretty_print=pretty_print)
        for reaction_ in self.reaction:
            reaction_.export(outfile, level, namespace_, name_='reaction', pretty_print=pretty_print)
        for sensitivityTest_ in self.sensitivityTest:
            sensitivityTest_.export(outfile, level, namespace_, name_='sensitivityTest', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='AllergyIntolerance', mapping_=None):
        element = super(AllergyIntolerance, self).to_etree(parent_element, name_, mapping_)
        for identifier_ in self.identifier:
            identifier_.to_etree(element, name_='identifier', mapping_=mapping_)
        if self.criticality is not None:
            criticality_ = self.criticality
            criticality_.to_etree(element, name_='criticality', mapping_=mapping_)
        if self.sensitivityType is not None:
            sensitivityType_ = self.sensitivityType
            sensitivityType_.to_etree(element, name_='sensitivityType', mapping_=mapping_)
        if self.recordedDate is not None:
            recordedDate_ = self.recordedDate
            recordedDate_.to_etree(element, name_='recordedDate', mapping_=mapping_)
        if self.status is not None:
            status_ = self.status
            status_.to_etree(element, name_='status', mapping_=mapping_)
        if self.subject is not None:
            subject_ = self.subject
            subject_.to_etree(element, name_='subject', mapping_=mapping_)
        if self.recorder is not None:
            recorder_ = self.recorder
            recorder_.to_etree(element, name_='recorder', mapping_=mapping_)
        if self.substance is not None:
            substance_ = self.substance
            substance_.to_etree(element, name_='substance', mapping_=mapping_)
        for reaction_ in self.reaction:
            reaction_.to_etree(element, name_='reaction', mapping_=mapping_)
        for sensitivityTest_ in self.sensitivityTest:
            sensitivityTest_.to_etree(element, name_='sensitivityTest', mapping_=mapping_)
        if mapping_ is not None:
            mapping_[self] = element
        return element
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        super(AllergyIntolerance, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'identifier':
            obj_ = Identifier.factory()
            obj_.build(child_)
            self.identifier.append(obj_)
            obj_.original_tagname_ = 'identifier'
        elif nodeName_ == 'criticality':
            obj_ = Criticality.factory()
            obj_.build(child_)
            self.criticality = obj_
            obj_.original_tagname_ = 'criticality'
        elif nodeName_ == 'sensitivityType':
            obj_ = SensitivityType.factory()
            obj_.build(child_)
            self.sensitivityType = obj_
            obj_.original_tagname_ = 'sensitivityType'
        elif nodeName_ == 'recordedDate':
            obj_ = dateTime.factory()
            obj_.build(child_)
            self.recordedDate = obj_
            obj_.original_tagname_ = 'recordedDate'
        elif nodeName_ == 'status':
            obj_ = SensitivityStatus.factory()
            obj_.build(child_)
            self.status = obj_
            obj_.original_tagname_ = 'status'
        elif nodeName_ == 'subject':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.subject = obj_
            obj_.original_tagname_ = 'subject'
        elif nodeName_ == 'recorder':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.recorder = obj_
            obj_.original_tagname_ = 'recorder'
        elif nodeName_ == 'substance':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.substance = obj_
            obj_.original_tagname_ = 'substance'
        elif nodeName_ == 'reaction':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.reaction.append(obj_)
            obj_.original_tagname_ = 'reaction'
        elif nodeName_ == 'sensitivityTest':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.sensitivityTest.append(obj_)
            obj_.original_tagname_ = 'sensitivityTest'
        super(AllergyIntolerance, self).buildChildren(child_, node, nodeName_, True)
# end class AllergyIntolerance
