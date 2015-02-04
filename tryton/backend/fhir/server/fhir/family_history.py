from .base_classes import *
from .support_functions import *


class FamilyHistory(Resource):
    """Significant health events and conditions for people related to the
    subject relevant in the context of care for the subject.If the
    element is present, it must have either a @value, an @id, or
    extensions"""
    subclass = None
    superclass = Resource
    def __init__(self, id=None, extension=None, modifierExtension=None, language=None, text=None, contained=None, identifier=None, subject=None, note=None, relation=None):
        self.original_tagname_ = None
        super(FamilyHistory, self).__init__(id, extension, modifierExtension, language, text, contained, )
        if identifier is None:
            self.identifier = []
        else:
            self.identifier = identifier
        self.subject = subject
        self.note = note
        if relation is None:
            self.relation = []
        else:
            self.relation = relation
    def factory(*args_, **kwargs_):
        if FamilyHistory.subclass:
            return FamilyHistory.subclass(*args_, **kwargs_)
        else:
            return FamilyHistory(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_identifier(self): return self.identifier
    def set_identifier(self, identifier): self.identifier = identifier
    def add_identifier(self, value): self.identifier.append(value)
    def insert_identifier(self, index, value): self.identifier[index] = value
    def get_subject(self): return self.subject
    def set_subject(self, subject): self.subject = subject
    def get_note(self): return self.note
    def set_note(self, note): self.note = note
    def get_relation(self): return self.relation
    def set_relation(self, relation): self.relation = relation
    def add_relation(self, value): self.relation.append(value)
    def insert_relation(self, index, value): self.relation[index] = value
    def hasContent_(self):
        if (
            self.identifier or
            self.subject is not None or
            self.note is not None or
            self.relation or
            super(FamilyHistory, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='FamilyHistory', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='FamilyHistory')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='FamilyHistory', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='FamilyHistory'):
        super(FamilyHistory, self).exportAttributes(outfile, level, already_processed, namespace_, name_='FamilyHistory')
    def exportChildren(self, outfile, level, namespace_='', name_='FamilyHistory', fromsubclass_=False, pretty_print=True):
        super(FamilyHistory, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for identifier_ in self.identifier:
            identifier_.export(outfile, level, namespace_, name_='identifier', pretty_print=pretty_print)
        if self.subject is not None:
            self.subject.export(outfile, level, namespace_, name_='subject', pretty_print=pretty_print)
        if self.note is not None:
            self.note.export(outfile, level, namespace_, name_='note', pretty_print=pretty_print)
        for relation_ in self.relation:
            relation_.export(outfile, level, namespace_, name_='relation', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='FamilyHistory', mapping_=None):
        element = super(FamilyHistory, self).to_etree(parent_element, name_, mapping_)
        for identifier_ in self.identifier:
            identifier_.to_etree(element, name_='identifier', mapping_=mapping_)
        if self.subject is not None:
            subject_ = self.subject
            subject_.to_etree(element, name_='subject', mapping_=mapping_)
        if self.note is not None:
            note_ = self.note
            note_.to_etree(element, name_='note', mapping_=mapping_)
        for relation_ in self.relation:
            relation_.to_etree(element, name_='relation', mapping_=mapping_)
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
        super(FamilyHistory, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'identifier':
            obj_ = Identifier.factory()
            obj_.build(child_)
            self.identifier.append(obj_)
            obj_.original_tagname_ = 'identifier'
        elif nodeName_ == 'subject':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.subject = obj_
            obj_.original_tagname_ = 'subject'
        elif nodeName_ == 'note':
            obj_ = string.factory()
            obj_.build(child_)
            self.note = obj_
            obj_.original_tagname_ = 'note'
        elif nodeName_ == 'relation':
            obj_ = FamilyHistory_Relation.factory()
            obj_.build(child_)
            self.relation.append(obj_)
            obj_.original_tagname_ = 'relation'
        super(FamilyHistory, self).buildChildren(child_, node, nodeName_, True)
# end class FamilyHistory


class FamilyHistory_Relation(BackboneElement):
    """Significant health events and conditions for people related to the
    subject relevant in the context of care for the subject.The
    actual or approximate date of birth of the relative.If this
    resource is indicating that the related person is deceased, then
    an indicator of whether the person is deceased (yes) or not (no)
    or the age or age range or description of age at death - can be
    indicated here. If the reason for death is known, then it can be
    indicated in the outcome code of the condition - in this case
    the deceased property should still be set."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, name=None, relationship=None, bornPeriod=None, bornDate=None, bornString=None, deceasedBoolean=None, deceasedAge=None, deceasedRange=None, deceasedDate=None, deceasedString=None, note=None, condition=None):
        self.original_tagname_ = None
        super(FamilyHistory_Relation, self).__init__(id, extension, modifierExtension, )
        self.name = name
        self.relationship = relationship
        self.bornPeriod = bornPeriod
        self.bornDate = bornDate
        self.bornString = bornString
        self.deceasedBoolean = deceasedBoolean
        self.deceasedAge = deceasedAge
        self.deceasedRange = deceasedRange
        self.deceasedDate = deceasedDate
        self.deceasedString = deceasedString
        self.note = note
        if condition is None:
            self.condition = []
        else:
            self.condition = condition
    def factory(*args_, **kwargs_):
        if FamilyHistory_Relation.subclass:
            return FamilyHistory_Relation.subclass(*args_, **kwargs_)
        else:
            return FamilyHistory_Relation(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_name(self): return self.name
    def set_name(self, name): self.name = name
    def get_relationship(self): return self.relationship
    def set_relationship(self, relationship): self.relationship = relationship
    def get_bornPeriod(self): return self.bornPeriod
    def set_bornPeriod(self, bornPeriod): self.bornPeriod = bornPeriod
    def get_bornDate(self): return self.bornDate
    def set_bornDate(self, bornDate): self.bornDate = bornDate
    def get_bornString(self): return self.bornString
    def set_bornString(self, bornString): self.bornString = bornString
    def get_deceasedBoolean(self): return self.deceasedBoolean
    def set_deceasedBoolean(self, deceasedBoolean): self.deceasedBoolean = deceasedBoolean
    def get_deceasedAge(self): return self.deceasedAge
    def set_deceasedAge(self, deceasedAge): self.deceasedAge = deceasedAge
    def get_deceasedRange(self): return self.deceasedRange
    def set_deceasedRange(self, deceasedRange): self.deceasedRange = deceasedRange
    def get_deceasedDate(self): return self.deceasedDate
    def set_deceasedDate(self, deceasedDate): self.deceasedDate = deceasedDate
    def get_deceasedString(self): return self.deceasedString
    def set_deceasedString(self, deceasedString): self.deceasedString = deceasedString
    def get_note(self): return self.note
    def set_note(self, note): self.note = note
    def get_condition(self): return self.condition
    def set_condition(self, condition): self.condition = condition
    def add_condition(self, value): self.condition.append(value)
    def insert_condition(self, index, value): self.condition[index] = value
    def hasContent_(self):
        if (
            self.name is not None or
            self.relationship is not None or
            self.bornPeriod is not None or
            self.bornDate is not None or
            self.bornString is not None or
            self.deceasedBoolean is not None or
            self.deceasedAge is not None or
            self.deceasedRange is not None or
            self.deceasedDate is not None or
            self.deceasedString is not None or
            self.note is not None or
            self.condition or
            super(FamilyHistory_Relation, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='FamilyHistory.Relation', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='FamilyHistory.Relation')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='FamilyHistory.Relation', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='FamilyHistory.Relation'):
        super(FamilyHistory_Relation, self).exportAttributes(outfile, level, already_processed, namespace_, name_='FamilyHistory.Relation')
    def exportChildren(self, outfile, level, namespace_='', name_='FamilyHistory.Relation', fromsubclass_=False, pretty_print=True):
        super(FamilyHistory_Relation, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.name is not None:
            self.name.export(outfile, level, namespace_, name_='name', pretty_print=pretty_print)
        if self.relationship is not None:
            self.relationship.export(outfile, level, namespace_, name_='relationship', pretty_print=pretty_print)
        if self.bornPeriod is not None:
            self.bornPeriod.export(outfile, level, namespace_, name_='bornPeriod', pretty_print=pretty_print)
        if self.bornDate is not None:
            self.bornDate.export(outfile, level, namespace_, name_='bornDate', pretty_print=pretty_print)
        if self.bornString is not None:
            self.bornString.export(outfile, level, namespace_, name_='bornString', pretty_print=pretty_print)
        if self.deceasedBoolean is not None:
            self.deceasedBoolean.export(outfile, level, namespace_, name_='deceasedBoolean', pretty_print=pretty_print)
        if self.deceasedAge is not None:
            self.deceasedAge.export(outfile, level, namespace_, name_='deceasedAge', pretty_print=pretty_print)
        if self.deceasedRange is not None:
            self.deceasedRange.export(outfile, level, namespace_, name_='deceasedRange', pretty_print=pretty_print)
        if self.deceasedDate is not None:
            self.deceasedDate.export(outfile, level, namespace_, name_='deceasedDate', pretty_print=pretty_print)
        if self.deceasedString is not None:
            self.deceasedString.export(outfile, level, namespace_, name_='deceasedString', pretty_print=pretty_print)
        if self.note is not None:
            self.note.export(outfile, level, namespace_, name_='note', pretty_print=pretty_print)
        for condition_ in self.condition:
            condition_.export(outfile, level, namespace_, name_='condition', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='FamilyHistory.Relation', mapping_=None):
        element = super(FamilyHistory_Relation, self).to_etree(parent_element, name_, mapping_)
        if self.name is not None:
            name_ = self.name
            name_.to_etree(element, name_='name', mapping_=mapping_)
        if self.relationship is not None:
            relationship_ = self.relationship
            relationship_.to_etree(element, name_='relationship', mapping_=mapping_)
        if self.bornPeriod is not None:
            bornPeriod_ = self.bornPeriod
            bornPeriod_.to_etree(element, name_='bornPeriod', mapping_=mapping_)
        if self.bornDate is not None:
            bornDate_ = self.bornDate
            bornDate_.to_etree(element, name_='bornDate', mapping_=mapping_)
        if self.bornString is not None:
            bornString_ = self.bornString
            bornString_.to_etree(element, name_='bornString', mapping_=mapping_)
        if self.deceasedBoolean is not None:
            deceasedBoolean_ = self.deceasedBoolean
            deceasedBoolean_.to_etree(element, name_='deceasedBoolean', mapping_=mapping_)
        if self.deceasedAge is not None:
            deceasedAge_ = self.deceasedAge
            deceasedAge_.to_etree(element, name_='deceasedAge', mapping_=mapping_)
        if self.deceasedRange is not None:
            deceasedRange_ = self.deceasedRange
            deceasedRange_.to_etree(element, name_='deceasedRange', mapping_=mapping_)
        if self.deceasedDate is not None:
            deceasedDate_ = self.deceasedDate
            deceasedDate_.to_etree(element, name_='deceasedDate', mapping_=mapping_)
        if self.deceasedString is not None:
            deceasedString_ = self.deceasedString
            deceasedString_.to_etree(element, name_='deceasedString', mapping_=mapping_)
        if self.note is not None:
            note_ = self.note
            note_.to_etree(element, name_='note', mapping_=mapping_)
        for condition_ in self.condition:
            condition_.to_etree(element, name_='condition', mapping_=mapping_)
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
        super(FamilyHistory_Relation, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'name':
            obj_ = string.factory()
            obj_.build(child_)
            self.name = obj_
            obj_.original_tagname_ = 'name'
        elif nodeName_ == 'relationship':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.relationship = obj_
            obj_.original_tagname_ = 'relationship'
        elif nodeName_ == 'bornPeriod':
            obj_ = Period.factory()
            obj_.build(child_)
            self.bornPeriod = obj_
            obj_.original_tagname_ = 'bornPeriod'
        elif nodeName_ == 'bornDate':
            obj_ = date.factory()
            obj_.build(child_)
            self.bornDate = obj_
            obj_.original_tagname_ = 'bornDate'
        elif nodeName_ == 'bornString':
            obj_ = string.factory()
            obj_.build(child_)
            self.bornString = obj_
            obj_.original_tagname_ = 'bornString'
        elif nodeName_ == 'deceasedBoolean':
            obj_ = boolean.factory()
            obj_.build(child_)
            self.deceasedBoolean = obj_
            obj_.original_tagname_ = 'deceasedBoolean'
        elif nodeName_ == 'deceasedAge':
            obj_ = Age.factory()
            obj_.build(child_)
            self.deceasedAge = obj_
            obj_.original_tagname_ = 'deceasedAge'
        elif nodeName_ == 'deceasedRange':
            obj_ = Range.factory()
            obj_.build(child_)
            self.deceasedRange = obj_
            obj_.original_tagname_ = 'deceasedRange'
        elif nodeName_ == 'deceasedDate':
            obj_ = date.factory()
            obj_.build(child_)
            self.deceasedDate = obj_
            obj_.original_tagname_ = 'deceasedDate'
        elif nodeName_ == 'deceasedString':
            obj_ = string.factory()
            obj_.build(child_)
            self.deceasedString = obj_
            obj_.original_tagname_ = 'deceasedString'
        elif nodeName_ == 'note':
            obj_ = string.factory()
            obj_.build(child_)
            self.note = obj_
            obj_.original_tagname_ = 'note'
        elif nodeName_ == 'condition':
            obj_ = FamilyHistory_Condition.factory()
            obj_.build(child_)
            self.condition.append(obj_)
            obj_.original_tagname_ = 'condition'
        super(FamilyHistory_Relation, self).buildChildren(child_, node, nodeName_, True)
# end class FamilyHistory_Relation


class FamilyHistory_Condition(BackboneElement):
    """Significant health events and conditions for people related to the
    subject relevant in the context of care for the subject.Either
    the age of onset, range of approximate age or descriptive string
    can be recorded. For conditions with multiple occurrences, this
    describes the first known occurrence."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, type_=None, outcome=None, onsetAge=None, onsetRange=None, onsetString=None, note=None):
        self.original_tagname_ = None
        super(FamilyHistory_Condition, self).__init__(id, extension, modifierExtension, )
        self.type_ = type_
        self.outcome = outcome
        self.onsetAge = onsetAge
        self.onsetRange = onsetRange
        self.onsetString = onsetString
        self.note = note
    def factory(*args_, **kwargs_):
        if FamilyHistory_Condition.subclass:
            return FamilyHistory_Condition.subclass(*args_, **kwargs_)
        else:
            return FamilyHistory_Condition(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_type(self): return self.type_
    def set_type(self, type_): self.type_ = type_
    def get_outcome(self): return self.outcome
    def set_outcome(self, outcome): self.outcome = outcome
    def get_onsetAge(self): return self.onsetAge
    def set_onsetAge(self, onsetAge): self.onsetAge = onsetAge
    def get_onsetRange(self): return self.onsetRange
    def set_onsetRange(self, onsetRange): self.onsetRange = onsetRange
    def get_onsetString(self): return self.onsetString
    def set_onsetString(self, onsetString): self.onsetString = onsetString
    def get_note(self): return self.note
    def set_note(self, note): self.note = note
    def hasContent_(self):
        if (
            self.type_ is not None or
            self.outcome is not None or
            self.onsetAge is not None or
            self.onsetRange is not None or
            self.onsetString is not None or
            self.note is not None or
            super(FamilyHistory_Condition, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='FamilyHistory.Condition', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='FamilyHistory.Condition')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='FamilyHistory.Condition', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='FamilyHistory.Condition'):
        super(FamilyHistory_Condition, self).exportAttributes(outfile, level, already_processed, namespace_, name_='FamilyHistory.Condition')
    def exportChildren(self, outfile, level, namespace_='', name_='FamilyHistory.Condition', fromsubclass_=False, pretty_print=True):
        super(FamilyHistory_Condition, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.type_ is not None:
            self.type_.export(outfile, level, namespace_, name_='type', pretty_print=pretty_print)
        if self.outcome is not None:
            self.outcome.export(outfile, level, namespace_, name_='outcome', pretty_print=pretty_print)
        if self.onsetAge is not None:
            self.onsetAge.export(outfile, level, namespace_, name_='onsetAge', pretty_print=pretty_print)
        if self.onsetRange is not None:
            self.onsetRange.export(outfile, level, namespace_, name_='onsetRange', pretty_print=pretty_print)
        if self.onsetString is not None:
            self.onsetString.export(outfile, level, namespace_, name_='onsetString', pretty_print=pretty_print)
        if self.note is not None:
            self.note.export(outfile, level, namespace_, name_='note', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='FamilyHistory.Condition', mapping_=None):
        element = super(FamilyHistory_Condition, self).to_etree(parent_element, name_, mapping_)
        if self.type_ is not None:
            type__ = self.type_
            type__.to_etree(element, name_='type', mapping_=mapping_)
        if self.outcome is not None:
            outcome_ = self.outcome
            outcome_.to_etree(element, name_='outcome', mapping_=mapping_)
        if self.onsetAge is not None:
            onsetAge_ = self.onsetAge
            onsetAge_.to_etree(element, name_='onsetAge', mapping_=mapping_)
        if self.onsetRange is not None:
            onsetRange_ = self.onsetRange
            onsetRange_.to_etree(element, name_='onsetRange', mapping_=mapping_)
        if self.onsetString is not None:
            onsetString_ = self.onsetString
            onsetString_.to_etree(element, name_='onsetString', mapping_=mapping_)
        if self.note is not None:
            note_ = self.note
            note_.to_etree(element, name_='note', mapping_=mapping_)
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
        super(FamilyHistory_Condition, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'type':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.type_ = obj_
            obj_.original_tagname_ = 'type'
        elif nodeName_ == 'outcome':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.outcome = obj_
            obj_.original_tagname_ = 'outcome'
        elif nodeName_ == 'onsetAge':
            obj_ = Age.factory()
            obj_.build(child_)
            self.onsetAge = obj_
            obj_.original_tagname_ = 'onsetAge'
        elif nodeName_ == 'onsetRange':
            obj_ = Range.factory()
            obj_.build(child_)
            self.onsetRange = obj_
            obj_.original_tagname_ = 'onsetRange'
        elif nodeName_ == 'onsetString':
            obj_ = string.factory()
            obj_.build(child_)
            self.onsetString = obj_
            obj_.original_tagname_ = 'onsetString'
        elif nodeName_ == 'note':
            obj_ = string.factory()
            obj_.build(child_)
            self.note = obj_
            obj_.original_tagname_ = 'note'
        super(FamilyHistory_Condition, self).buildChildren(child_, node, nodeName_, True)
# end class FamilyHistory_Condition
