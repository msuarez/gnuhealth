from .base_classes import *
from .support_functions import *


class Procedure(Resource):
    """An action that is performed on a patient. This can be a physical
    'thing' like an operation, or less invasive like counseling or
    hypnotherapy.If the element is present, it must have either a
    @value, an @id, or extensions"""
    subclass = None
    superclass = Resource
    def __init__(self, id=None, extension=None, modifierExtension=None, language=None, text=None, contained=None, identifier=None, subject=None, type_=None, bodySite=None, indication=None, performer=None, date=None, encounter=None, outcome=None, report=None, complication=None, followUp=None, relatedItem=None, notes=None):
        self.original_tagname_ = None
        super(Procedure, self).__init__(id, extension, modifierExtension, language, text, contained, )
        if identifier is None:
            self.identifier = []
        else:
            self.identifier = identifier
        self.subject = subject
        self.type_ = type_
        if bodySite is None:
            self.bodySite = []
        else:
            self.bodySite = bodySite
        if indication is None:
            self.indication = []
        else:
            self.indication = indication
        if performer is None:
            self.performer = []
        else:
            self.performer = performer
        self.date = date
        self.encounter = encounter
        self.outcome = outcome
        if report is None:
            self.report = []
        else:
            self.report = report
        if complication is None:
            self.complication = []
        else:
            self.complication = complication
        self.followUp = followUp
        if relatedItem is None:
            self.relatedItem = []
        else:
            self.relatedItem = relatedItem
        self.notes = notes
    def factory(*args_, **kwargs_):
        if Procedure.subclass:
            return Procedure.subclass(*args_, **kwargs_)
        else:
            return Procedure(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_identifier(self): return self.identifier
    def set_identifier(self, identifier): self.identifier = identifier
    def add_identifier(self, value): self.identifier.append(value)
    def insert_identifier(self, index, value): self.identifier[index] = value
    def get_subject(self): return self.subject
    def set_subject(self, subject): self.subject = subject
    def get_type(self): return self.type_
    def set_type(self, type_): self.type_ = type_
    def get_bodySite(self): return self.bodySite
    def set_bodySite(self, bodySite): self.bodySite = bodySite
    def add_bodySite(self, value): self.bodySite.append(value)
    def insert_bodySite(self, index, value): self.bodySite[index] = value
    def get_indication(self): return self.indication
    def set_indication(self, indication): self.indication = indication
    def add_indication(self, value): self.indication.append(value)
    def insert_indication(self, index, value): self.indication[index] = value
    def get_performer(self): return self.performer
    def set_performer(self, performer): self.performer = performer
    def add_performer(self, value): self.performer.append(value)
    def insert_performer(self, index, value): self.performer[index] = value
    def get_date(self): return self.date
    def set_date(self, date): self.date = date
    def get_encounter(self): return self.encounter
    def set_encounter(self, encounter): self.encounter = encounter
    def get_outcome(self): return self.outcome
    def set_outcome(self, outcome): self.outcome = outcome
    def get_report(self): return self.report
    def set_report(self, report): self.report = report
    def add_report(self, value): self.report.append(value)
    def insert_report(self, index, value): self.report[index] = value
    def get_complication(self): return self.complication
    def set_complication(self, complication): self.complication = complication
    def add_complication(self, value): self.complication.append(value)
    def insert_complication(self, index, value): self.complication[index] = value
    def get_followUp(self): return self.followUp
    def set_followUp(self, followUp): self.followUp = followUp
    def get_relatedItem(self): return self.relatedItem
    def set_relatedItem(self, relatedItem): self.relatedItem = relatedItem
    def add_relatedItem(self, value): self.relatedItem.append(value)
    def insert_relatedItem(self, index, value): self.relatedItem[index] = value
    def get_notes(self): return self.notes
    def set_notes(self, notes): self.notes = notes
    def hasContent_(self):
        if (
            self.identifier or
            self.subject is not None or
            self.type_ is not None or
            self.bodySite or
            self.indication or
            self.performer or
            self.date is not None or
            self.encounter is not None or
            self.outcome is not None or
            self.report or
            self.complication or
            self.followUp is not None or
            self.relatedItem or
            self.notes is not None or
            super(Procedure, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Procedure', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Procedure')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Procedure', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Procedure'):
        super(Procedure, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Procedure')
    def exportChildren(self, outfile, level, namespace_='', name_='Procedure', fromsubclass_=False, pretty_print=True):
        super(Procedure, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for identifier_ in self.identifier:
            identifier_.export(outfile, level, namespace_, name_='identifier', pretty_print=pretty_print)
        if self.subject is not None:
            self.subject.export(outfile, level, namespace_, name_='subject', pretty_print=pretty_print)
        if self.type_ is not None:
            self.type_.export(outfile, level, namespace_, name_='type', pretty_print=pretty_print)
        for bodySite_ in self.bodySite:
            bodySite_.export(outfile, level, namespace_, name_='bodySite', pretty_print=pretty_print)
        for indication_ in self.indication:
            indication_.export(outfile, level, namespace_, name_='indication', pretty_print=pretty_print)
        for performer_ in self.performer:
            performer_.export(outfile, level, namespace_, name_='performer', pretty_print=pretty_print)
        if self.date is not None:
            self.date.export(outfile, level, namespace_, name_='date', pretty_print=pretty_print)
        if self.encounter is not None:
            self.encounter.export(outfile, level, namespace_, name_='encounter', pretty_print=pretty_print)
        if self.outcome is not None:
            self.outcome.export(outfile, level, namespace_, name_='outcome', pretty_print=pretty_print)
        for report_ in self.report:
            report_.export(outfile, level, namespace_, name_='report', pretty_print=pretty_print)
        for complication_ in self.complication:
            complication_.export(outfile, level, namespace_, name_='complication', pretty_print=pretty_print)
        if self.followUp is not None:
            self.followUp.export(outfile, level, namespace_, name_='followUp', pretty_print=pretty_print)
        for relatedItem_ in self.relatedItem:
            relatedItem_.export(outfile, level, namespace_, name_='relatedItem', pretty_print=pretty_print)
        if self.notes is not None:
            self.notes.export(outfile, level, namespace_, name_='notes', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Procedure', mapping_=None):
        element = super(Procedure, self).to_etree(parent_element, name_, mapping_)
        for identifier_ in self.identifier:
            identifier_.to_etree(element, name_='identifier', mapping_=mapping_)
        if self.subject is not None:
            subject_ = self.subject
            subject_.to_etree(element, name_='subject', mapping_=mapping_)
        if self.type_ is not None:
            type__ = self.type_
            type__.to_etree(element, name_='type', mapping_=mapping_)
        for bodySite_ in self.bodySite:
            bodySite_.to_etree(element, name_='bodySite', mapping_=mapping_)
        for indication_ in self.indication:
            indication_.to_etree(element, name_='indication', mapping_=mapping_)
        for performer_ in self.performer:
            performer_.to_etree(element, name_='performer', mapping_=mapping_)
        if self.date is not None:
            date_ = self.date
            date_.to_etree(element, name_='date', mapping_=mapping_)
        if self.encounter is not None:
            encounter_ = self.encounter
            encounter_.to_etree(element, name_='encounter', mapping_=mapping_)
        if self.outcome is not None:
            outcome_ = self.outcome
            outcome_.to_etree(element, name_='outcome', mapping_=mapping_)
        for report_ in self.report:
            report_.to_etree(element, name_='report', mapping_=mapping_)
        for complication_ in self.complication:
            complication_.to_etree(element, name_='complication', mapping_=mapping_)
        if self.followUp is not None:
            followUp_ = self.followUp
            followUp_.to_etree(element, name_='followUp', mapping_=mapping_)
        for relatedItem_ in self.relatedItem:
            relatedItem_.to_etree(element, name_='relatedItem', mapping_=mapping_)
        if self.notes is not None:
            notes_ = self.notes
            notes_.to_etree(element, name_='notes', mapping_=mapping_)
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
        super(Procedure, self).buildAttributes(node, attrs, already_processed)
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
        elif nodeName_ == 'type':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.type_ = obj_
            obj_.original_tagname_ = 'type'
        elif nodeName_ == 'bodySite':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.bodySite.append(obj_)
            obj_.original_tagname_ = 'bodySite'
        elif nodeName_ == 'indication':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.indication.append(obj_)
            obj_.original_tagname_ = 'indication'
        elif nodeName_ == 'performer':
            obj_ = Procedure_Performer.factory()
            obj_.build(child_)
            self.performer.append(obj_)
            obj_.original_tagname_ = 'performer'
        elif nodeName_ == 'date':
            obj_ = Period.factory()
            obj_.build(child_)
            self.date = obj_
            obj_.original_tagname_ = 'date'
        elif nodeName_ == 'encounter':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.encounter = obj_
            obj_.original_tagname_ = 'encounter'
        elif nodeName_ == 'outcome':
            obj_ = string.factory()
            obj_.build(child_)
            self.outcome = obj_
            obj_.original_tagname_ = 'outcome'
        elif nodeName_ == 'report':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.report.append(obj_)
            obj_.original_tagname_ = 'report'
        elif nodeName_ == 'complication':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.complication.append(obj_)
            obj_.original_tagname_ = 'complication'
        elif nodeName_ == 'followUp':
            obj_ = string.factory()
            obj_.build(child_)
            self.followUp = obj_
            obj_.original_tagname_ = 'followUp'
        elif nodeName_ == 'relatedItem':
            obj_ = Procedure_RelatedItem.factory()
            obj_.build(child_)
            self.relatedItem.append(obj_)
            obj_.original_tagname_ = 'relatedItem'
        elif nodeName_ == 'notes':
            obj_ = string.factory()
            obj_.build(child_)
            self.notes = obj_
            obj_.original_tagname_ = 'notes'
        super(Procedure, self).buildChildren(child_, node, nodeName_, True)
# end class Procedure


class Procedure_Performer(BackboneElement):
    """An action that is performed on a patient. This can be a physical
    'thing' like an operation, or less invasive like counseling or
    hypnotherapy."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, person=None, role=None):
        self.original_tagname_ = None
        super(Procedure_Performer, self).__init__(id, extension, modifierExtension, )
        self.person = person
        self.role = role
    def factory(*args_, **kwargs_):
        if Procedure_Performer.subclass:
            return Procedure_Performer.subclass(*args_, **kwargs_)
        else:
            return Procedure_Performer(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_person(self): return self.person
    def set_person(self, person): self.person = person
    def get_role(self): return self.role
    def set_role(self, role): self.role = role
    def hasContent_(self):
        if (
            self.person is not None or
            self.role is not None or
            super(Procedure_Performer, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Procedure.Performer', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Procedure.Performer')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Procedure.Performer', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Procedure.Performer'):
        super(Procedure_Performer, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Procedure.Performer')
    def exportChildren(self, outfile, level, namespace_='', name_='Procedure.Performer', fromsubclass_=False, pretty_print=True):
        super(Procedure_Performer, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.person is not None:
            self.person.export(outfile, level, namespace_, name_='person', pretty_print=pretty_print)
        if self.role is not None:
            self.role.export(outfile, level, namespace_, name_='role', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Procedure.Performer', mapping_=None):
        element = super(Procedure_Performer, self).to_etree(parent_element, name_, mapping_)
        if self.person is not None:
            person_ = self.person
            person_.to_etree(element, name_='person', mapping_=mapping_)
        if self.role is not None:
            role_ = self.role
            role_.to_etree(element, name_='role', mapping_=mapping_)
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
        super(Procedure_Performer, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'person':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.person = obj_
            obj_.original_tagname_ = 'person'
        elif nodeName_ == 'role':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.role = obj_
            obj_.original_tagname_ = 'role'
        super(Procedure_Performer, self).buildChildren(child_, node, nodeName_, True)
# end class Procedure_Performer


class Procedure_RelatedItem(BackboneElement):
    """An action that is performed on a patient. This can be a physical
    'thing' like an operation, or less invasive like counseling or
    hypnotherapy."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, type_=None, target=None):
        self.original_tagname_ = None
        super(Procedure_RelatedItem, self).__init__(id, extension, modifierExtension, )
        self.type_ = type_
        self.target = target
    def factory(*args_, **kwargs_):
        if Procedure_RelatedItem.subclass:
            return Procedure_RelatedItem.subclass(*args_, **kwargs_)
        else:
            return Procedure_RelatedItem(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_type(self): return self.type_
    def set_type(self, type_): self.type_ = type_
    def get_target(self): return self.target
    def set_target(self, target): self.target = target
    def hasContent_(self):
        if (
            self.type_ is not None or
            self.target is not None or
            super(Procedure_RelatedItem, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Procedure.RelatedItem', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Procedure.RelatedItem')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Procedure.RelatedItem', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Procedure.RelatedItem'):
        super(Procedure_RelatedItem, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Procedure.RelatedItem')
    def exportChildren(self, outfile, level, namespace_='', name_='Procedure.RelatedItem', fromsubclass_=False, pretty_print=True):
        super(Procedure_RelatedItem, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.type_ is not None:
            self.type_.export(outfile, level, namespace_, name_='type', pretty_print=pretty_print)
        if self.target is not None:
            self.target.export(outfile, level, namespace_, name_='target', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Procedure.RelatedItem', mapping_=None):
        element = super(Procedure_RelatedItem, self).to_etree(parent_element, name_, mapping_)
        if self.type_ is not None:
            type__ = self.type_
            type__.to_etree(element, name_='type', mapping_=mapping_)
        if self.target is not None:
            target_ = self.target
            target_.to_etree(element, name_='target', mapping_=mapping_)
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
        super(Procedure_RelatedItem, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'type':
            obj_ = ProcedureRelationshipType.factory()
            obj_.build(child_)
            self.type_ = obj_
            obj_.original_tagname_ = 'type'
        elif nodeName_ == 'target':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.target = obj_
            obj_.original_tagname_ = 'target'
        super(Procedure_RelatedItem, self).buildChildren(child_, node, nodeName_, True)
# end class Procedure_RelatedItem


class ProcedureRelationshipType(Element):
    """The nature of the relationship with this procedureIf the element is
    present, it must have either a @value, an @id, or extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(ProcedureRelationshipType, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if ProcedureRelationshipType.subclass:
            return ProcedureRelationshipType.subclass(*args_, **kwargs_)
        else:
            return ProcedureRelationshipType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(ProcedureRelationshipType, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='ProcedureRelationshipType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ProcedureRelationshipType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='ProcedureRelationshipType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='ProcedureRelationshipType'):
        super(ProcedureRelationshipType, self).exportAttributes(outfile, level, already_processed, namespace_, name_='ProcedureRelationshipType')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='ProcedureRelationshipType', fromsubclass_=False, pretty_print=True):
        super(ProcedureRelationshipType, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='ProcedureRelationshipType', mapping_=None):
        element = super(ProcedureRelationshipType, self).to_etree(parent_element, name_, mapping_)
        if self.value is not None:
            element.set('value', self.value)
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
        value = find_attr_value_('value', node)
        if value is not None and 'value' not in already_processed:
            already_processed.add('value')
            self.value = value
        super(ProcedureRelationshipType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(ProcedureRelationshipType, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class ProcedureRelationshipType
