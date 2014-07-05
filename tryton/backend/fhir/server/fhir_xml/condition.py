from .base_classes import *
from .support_functions import *


class Condition(Resource):
    """Use to record detailed information about conditions, problems or
    diagnoses recognized by a clinician. There are many uses
    including: recording a Diagnosis during an Encounter; populating
    a problem List or a Summary Statement, such as a Discharge
    Summary.If the element is present, it must have either a @value,
    an @id, or extensionsEstimated or actual date the condition
    began, in the opinion of the clinician.The date or estimated
    date that the condition resolved or went into remission. This is
    called "abatement" because of the many overloaded connotations
    associated with "remission" or "resolution" - Conditions are
    never really resolved, but they can abate."""
    subclass = None
    superclass = Resource
    def __init__(self, id=None, extension=None, modifierExtension=None, language=None, text=None, contained=None, identifier=None, subject=None, encounter=None, asserter=None, dateAsserted=None, code=None, category=None, status=None, certainty=None, severity=None, onsetDate=None, onsetAge=None, abatementDate=None, abatementAge=None, abatementBoolean=None, stage=None, evidence=None, location=None, relatedItem=None, notes=None):
        self.original_tagname_ = None
        super(Condition, self).__init__(id, extension, modifierExtension, language, text, contained, )
        if identifier is None:
            self.identifier = []
        else:
            self.identifier = identifier
        self.subject = subject
        self.encounter = encounter
        self.asserter = asserter
        self.dateAsserted = dateAsserted
        self.code = code
        self.category = category
        self.status = status
        self.certainty = certainty
        self.severity = severity
        self.onsetDate = onsetDate
        self.onsetAge = onsetAge
        self.abatementDate = abatementDate
        self.abatementAge = abatementAge
        self.abatementBoolean = abatementBoolean
        self.stage = stage
        if evidence is None:
            self.evidence = []
        else:
            self.evidence = evidence
        if location is None:
            self.location = []
        else:
            self.location = location
        if relatedItem is None:
            self.relatedItem = []
        else:
            self.relatedItem = relatedItem
        self.notes = notes
    def factory(*args_, **kwargs_):
        if Condition.subclass:
            return Condition.subclass(*args_, **kwargs_)
        else:
            return Condition(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_identifier(self): return self.identifier
    def set_identifier(self, identifier): self.identifier = identifier
    def add_identifier(self, value): self.identifier.append(value)
    def insert_identifier(self, index, value): self.identifier[index] = value
    def get_subject(self): return self.subject
    def set_subject(self, subject): self.subject = subject
    def get_encounter(self): return self.encounter
    def set_encounter(self, encounter): self.encounter = encounter
    def get_asserter(self): return self.asserter
    def set_asserter(self, asserter): self.asserter = asserter
    def get_dateAsserted(self): return self.dateAsserted
    def set_dateAsserted(self, dateAsserted): self.dateAsserted = dateAsserted
    def get_code(self): return self.code
    def set_code(self, code): self.code = code
    def get_category(self): return self.category
    def set_category(self, category): self.category = category
    def get_status(self): return self.status
    def set_status(self, status): self.status = status
    def get_certainty(self): return self.certainty
    def set_certainty(self, certainty): self.certainty = certainty
    def get_severity(self): return self.severity
    def set_severity(self, severity): self.severity = severity
    def get_onsetDate(self): return self.onsetDate
    def set_onsetDate(self, onsetDate): self.onsetDate = onsetDate
    def get_onsetAge(self): return self.onsetAge
    def set_onsetAge(self, onsetAge): self.onsetAge = onsetAge
    def get_abatementDate(self): return self.abatementDate
    def set_abatementDate(self, abatementDate): self.abatementDate = abatementDate
    def get_abatementAge(self): return self.abatementAge
    def set_abatementAge(self, abatementAge): self.abatementAge = abatementAge
    def get_abatementBoolean(self): return self.abatementBoolean
    def set_abatementBoolean(self, abatementBoolean): self.abatementBoolean = abatementBoolean
    def get_stage(self): return self.stage
    def set_stage(self, stage): self.stage = stage
    def get_evidence(self): return self.evidence
    def set_evidence(self, evidence): self.evidence = evidence
    def add_evidence(self, value): self.evidence.append(value)
    def insert_evidence(self, index, value): self.evidence[index] = value
    def get_location(self): return self.location
    def set_location(self, location): self.location = location
    def add_location(self, value): self.location.append(value)
    def insert_location(self, index, value): self.location[index] = value
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
            self.encounter is not None or
            self.asserter is not None or
            self.dateAsserted is not None or
            self.code is not None or
            self.category is not None or
            self.status is not None or
            self.certainty is not None or
            self.severity is not None or
            self.onsetDate is not None or
            self.onsetAge is not None or
            self.abatementDate is not None or
            self.abatementAge is not None or
            self.abatementBoolean is not None or
            self.stage is not None or
            self.evidence or
            self.location or
            self.relatedItem or
            self.notes is not None or
            super(Condition, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Condition', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Condition')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Condition', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Condition'):
        super(Condition, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Condition')
    def exportChildren(self, outfile, level, namespace_='', name_='Condition', fromsubclass_=False, pretty_print=True):
        super(Condition, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for identifier_ in self.identifier:
            identifier_.export(outfile, level, namespace_, name_='identifier', pretty_print=pretty_print)
        if self.subject is not None:
            self.subject.export(outfile, level, namespace_, name_='subject', pretty_print=pretty_print)
        if self.encounter is not None:
            self.encounter.export(outfile, level, namespace_, name_='encounter', pretty_print=pretty_print)
        if self.asserter is not None:
            self.asserter.export(outfile, level, namespace_, name_='asserter', pretty_print=pretty_print)
        if self.dateAsserted is not None:
            self.dateAsserted.export(outfile, level, namespace_, name_='dateAsserted', pretty_print=pretty_print)
        if self.code is not None:
            self.code.export(outfile, level, namespace_, name_='code', pretty_print=pretty_print)
        if self.category is not None:
            self.category.export(outfile, level, namespace_, name_='category', pretty_print=pretty_print)
        if self.status is not None:
            self.status.export(outfile, level, namespace_, name_='status', pretty_print=pretty_print)
        if self.certainty is not None:
            self.certainty.export(outfile, level, namespace_, name_='certainty', pretty_print=pretty_print)
        if self.severity is not None:
            self.severity.export(outfile, level, namespace_, name_='severity', pretty_print=pretty_print)
        if self.onsetDate is not None:
            self.onsetDate.export(outfile, level, namespace_, name_='onsetDate', pretty_print=pretty_print)
        if self.onsetAge is not None:
            self.onsetAge.export(outfile, level, namespace_, name_='onsetAge', pretty_print=pretty_print)
        if self.abatementDate is not None:
            self.abatementDate.export(outfile, level, namespace_, name_='abatementDate', pretty_print=pretty_print)
        if self.abatementAge is not None:
            self.abatementAge.export(outfile, level, namespace_, name_='abatementAge', pretty_print=pretty_print)
        if self.abatementBoolean is not None:
            self.abatementBoolean.export(outfile, level, namespace_, name_='abatementBoolean', pretty_print=pretty_print)
        if self.stage is not None:
            self.stage.export(outfile, level, namespace_, name_='stage', pretty_print=pretty_print)
        for evidence_ in self.evidence:
            evidence_.export(outfile, level, namespace_, name_='evidence', pretty_print=pretty_print)
        for location_ in self.location:
            location_.export(outfile, level, namespace_, name_='location', pretty_print=pretty_print)
        for relatedItem_ in self.relatedItem:
            relatedItem_.export(outfile, level, namespace_, name_='relatedItem', pretty_print=pretty_print)
        if self.notes is not None:
            self.notes.export(outfile, level, namespace_, name_='notes', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Condition', mapping_=None):
        element = super(Condition, self).to_etree(parent_element, name_, mapping_)
        for identifier_ in self.identifier:
            identifier_.to_etree(element, name_='identifier', mapping_=mapping_)
        if self.subject is not None:
            subject_ = self.subject
            subject_.to_etree(element, name_='subject', mapping_=mapping_)
        if self.encounter is not None:
            encounter_ = self.encounter
            encounter_.to_etree(element, name_='encounter', mapping_=mapping_)
        if self.asserter is not None:
            asserter_ = self.asserter
            asserter_.to_etree(element, name_='asserter', mapping_=mapping_)
        if self.dateAsserted is not None:
            dateAsserted_ = self.dateAsserted
            dateAsserted_.to_etree(element, name_='dateAsserted', mapping_=mapping_)
        if self.code is not None:
            code_ = self.code
            code_.to_etree(element, name_='code', mapping_=mapping_)
        if self.category is not None:
            category_ = self.category
            category_.to_etree(element, name_='category', mapping_=mapping_)
        if self.status is not None:
            status_ = self.status
            status_.to_etree(element, name_='status', mapping_=mapping_)
        if self.certainty is not None:
            certainty_ = self.certainty
            certainty_.to_etree(element, name_='certainty', mapping_=mapping_)
        if self.severity is not None:
            severity_ = self.severity
            severity_.to_etree(element, name_='severity', mapping_=mapping_)
        if self.onsetDate is not None:
            onsetDate_ = self.onsetDate
            onsetDate_.to_etree(element, name_='onsetDate', mapping_=mapping_)
        if self.onsetAge is not None:
            onsetAge_ = self.onsetAge
            onsetAge_.to_etree(element, name_='onsetAge', mapping_=mapping_)
        if self.abatementDate is not None:
            abatementDate_ = self.abatementDate
            abatementDate_.to_etree(element, name_='abatementDate', mapping_=mapping_)
        if self.abatementAge is not None:
            abatementAge_ = self.abatementAge
            abatementAge_.to_etree(element, name_='abatementAge', mapping_=mapping_)
        if self.abatementBoolean is not None:
            abatementBoolean_ = self.abatementBoolean
            abatementBoolean_.to_etree(element, name_='abatementBoolean', mapping_=mapping_)
        if self.stage is not None:
            stage_ = self.stage
            stage_.to_etree(element, name_='stage', mapping_=mapping_)
        for evidence_ in self.evidence:
            evidence_.to_etree(element, name_='evidence', mapping_=mapping_)
        for location_ in self.location:
            location_.to_etree(element, name_='location', mapping_=mapping_)
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
        super(Condition, self).buildAttributes(node, attrs, already_processed)
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
        elif nodeName_ == 'encounter':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.encounter = obj_
            obj_.original_tagname_ = 'encounter'
        elif nodeName_ == 'asserter':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.asserter = obj_
            obj_.original_tagname_ = 'asserter'
        elif nodeName_ == 'dateAsserted':
            obj_ = date.factory()
            obj_.build(child_)
            self.dateAsserted = obj_
            obj_.original_tagname_ = 'dateAsserted'
        elif nodeName_ == 'code':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.code = obj_
            obj_.original_tagname_ = 'code'
        elif nodeName_ == 'category':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.category = obj_
            obj_.original_tagname_ = 'category'
        elif nodeName_ == 'status':
            obj_ = ConditionStatus.factory()
            obj_.build(child_)
            self.status = obj_
            obj_.original_tagname_ = 'status'
        elif nodeName_ == 'certainty':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.certainty = obj_
            obj_.original_tagname_ = 'certainty'
        elif nodeName_ == 'severity':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.severity = obj_
            obj_.original_tagname_ = 'severity'
        elif nodeName_ == 'onsetDate':
            obj_ = date.factory()
            obj_.build(child_)
            self.onsetDate = obj_
            obj_.original_tagname_ = 'onsetDate'
        elif nodeName_ == 'onsetAge':
            obj_ = Age.factory()
            obj_.build(child_)
            self.onsetAge = obj_
            obj_.original_tagname_ = 'onsetAge'
        elif nodeName_ == 'abatementDate':
            obj_ = date.factory()
            obj_.build(child_)
            self.abatementDate = obj_
            obj_.original_tagname_ = 'abatementDate'
        elif nodeName_ == 'abatementAge':
            obj_ = Age.factory()
            obj_.build(child_)
            self.abatementAge = obj_
            obj_.original_tagname_ = 'abatementAge'
        elif nodeName_ == 'abatementBoolean':
            obj_ = boolean.factory()
            obj_.build(child_)
            self.abatementBoolean = obj_
            obj_.original_tagname_ = 'abatementBoolean'
        elif nodeName_ == 'stage':
            obj_ = Condition_Stage.factory()
            obj_.build(child_)
            self.stage = obj_
            obj_.original_tagname_ = 'stage'
        elif nodeName_ == 'evidence':
            obj_ = Condition_Evidence.factory()
            obj_.build(child_)
            self.evidence.append(obj_)
            obj_.original_tagname_ = 'evidence'
        elif nodeName_ == 'location':
            obj_ = Condition_Location.factory()
            obj_.build(child_)
            self.location.append(obj_)
            obj_.original_tagname_ = 'location'
        elif nodeName_ == 'relatedItem':
            obj_ = Condition_RelatedItem.factory()
            obj_.build(child_)
            self.relatedItem.append(obj_)
            obj_.original_tagname_ = 'relatedItem'
        elif nodeName_ == 'notes':
            obj_ = string.factory()
            obj_.build(child_)
            self.notes = obj_
            obj_.original_tagname_ = 'notes'
        super(Condition, self).buildChildren(child_, node, nodeName_, True)
# end class Condition


class Condition_Stage(BackboneElement):
    """Use to record detailed information about conditions, problems or
    diagnoses recognized by a clinician. There are many uses
    including: recording a Diagnosis during an Encounter; populating
    a problem List or a Summary Statement, such as a Discharge
    Summary."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, summary=None, assessment=None):
        self.original_tagname_ = None
        super(Condition_Stage, self).__init__(id, extension, modifierExtension, )
        self.summary = summary
        if assessment is None:
            self.assessment = []
        else:
            self.assessment = assessment
    def factory(*args_, **kwargs_):
        if Condition_Stage.subclass:
            return Condition_Stage.subclass(*args_, **kwargs_)
        else:
            return Condition_Stage(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_summary(self): return self.summary
    def set_summary(self, summary): self.summary = summary
    def get_assessment(self): return self.assessment
    def set_assessment(self, assessment): self.assessment = assessment
    def add_assessment(self, value): self.assessment.append(value)
    def insert_assessment(self, index, value): self.assessment[index] = value
    def hasContent_(self):
        if (
            self.summary is not None or
            self.assessment or
            super(Condition_Stage, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Condition.Stage', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Condition.Stage')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Condition.Stage', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Condition.Stage'):
        super(Condition_Stage, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Condition.Stage')
    def exportChildren(self, outfile, level, namespace_='', name_='Condition.Stage', fromsubclass_=False, pretty_print=True):
        super(Condition_Stage, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.summary is not None:
            self.summary.export(outfile, level, namespace_, name_='summary', pretty_print=pretty_print)
        for assessment_ in self.assessment:
            assessment_.export(outfile, level, namespace_, name_='assessment', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Condition.Stage', mapping_=None):
        element = super(Condition_Stage, self).to_etree(parent_element, name_, mapping_)
        if self.summary is not None:
            summary_ = self.summary
            summary_.to_etree(element, name_='summary', mapping_=mapping_)
        for assessment_ in self.assessment:
            assessment_.to_etree(element, name_='assessment', mapping_=mapping_)
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
        super(Condition_Stage, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'summary':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.summary = obj_
            obj_.original_tagname_ = 'summary'
        elif nodeName_ == 'assessment':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.assessment.append(obj_)
            obj_.original_tagname_ = 'assessment'
        super(Condition_Stage, self).buildChildren(child_, node, nodeName_, True)
# end class Condition_Stage


class Condition_Evidence(BackboneElement):
    """Use to record detailed information about conditions, problems or
    diagnoses recognized by a clinician. There are many uses
    including: recording a Diagnosis during an Encounter; populating
    a problem List or a Summary Statement, such as a Discharge
    Summary."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, code=None, detail=None):
        self.original_tagname_ = None
        super(Condition_Evidence, self).__init__(id, extension, modifierExtension, )
        self.code = code
        if detail is None:
            self.detail = []
        else:
            self.detail = detail
    def factory(*args_, **kwargs_):
        if Condition_Evidence.subclass:
            return Condition_Evidence.subclass(*args_, **kwargs_)
        else:
            return Condition_Evidence(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_code(self): return self.code
    def set_code(self, code): self.code = code
    def get_detail(self): return self.detail
    def set_detail(self, detail): self.detail = detail
    def add_detail(self, value): self.detail.append(value)
    def insert_detail(self, index, value): self.detail[index] = value
    def hasContent_(self):
        if (
            self.code is not None or
            self.detail or
            super(Condition_Evidence, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Condition.Evidence', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Condition.Evidence')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Condition.Evidence', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Condition.Evidence'):
        super(Condition_Evidence, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Condition.Evidence')
    def exportChildren(self, outfile, level, namespace_='', name_='Condition.Evidence', fromsubclass_=False, pretty_print=True):
        super(Condition_Evidence, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.code is not None:
            self.code.export(outfile, level, namespace_, name_='code', pretty_print=pretty_print)
        for detail_ in self.detail:
            detail_.export(outfile, level, namespace_, name_='detail', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Condition.Evidence', mapping_=None):
        element = super(Condition_Evidence, self).to_etree(parent_element, name_, mapping_)
        if self.code is not None:
            code_ = self.code
            code_.to_etree(element, name_='code', mapping_=mapping_)
        for detail_ in self.detail:
            detail_.to_etree(element, name_='detail', mapping_=mapping_)
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
        super(Condition_Evidence, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'code':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.code = obj_
            obj_.original_tagname_ = 'code'
        elif nodeName_ == 'detail':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.detail.append(obj_)
            obj_.original_tagname_ = 'detail'
        super(Condition_Evidence, self).buildChildren(child_, node, nodeName_, True)
# end class Condition_Evidence


class Condition_Location(BackboneElement):
    """Use to record detailed information about conditions, problems or
    diagnoses recognized by a clinician. There are many uses
    including: recording a Diagnosis during an Encounter; populating
    a problem List or a Summary Statement, such as a Discharge
    Summary."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, code=None, detail=None):
        self.original_tagname_ = None
        super(Condition_Location, self).__init__(id, extension, modifierExtension, )
        self.code = code
        self.detail = detail
    def factory(*args_, **kwargs_):
        if Condition_Location.subclass:
            return Condition_Location.subclass(*args_, **kwargs_)
        else:
            return Condition_Location(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_code(self): return self.code
    def set_code(self, code): self.code = code
    def get_detail(self): return self.detail
    def set_detail(self, detail): self.detail = detail
    def hasContent_(self):
        if (
            self.code is not None or
            self.detail is not None or
            super(Condition_Location, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Condition.Location', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Condition.Location')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Condition.Location', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Condition.Location'):
        super(Condition_Location, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Condition.Location')
    def exportChildren(self, outfile, level, namespace_='', name_='Condition.Location', fromsubclass_=False, pretty_print=True):
        super(Condition_Location, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.code is not None:
            self.code.export(outfile, level, namespace_, name_='code', pretty_print=pretty_print)
        if self.detail is not None:
            self.detail.export(outfile, level, namespace_, name_='detail', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Condition.Location', mapping_=None):
        element = super(Condition_Location, self).to_etree(parent_element, name_, mapping_)
        if self.code is not None:
            code_ = self.code
            code_.to_etree(element, name_='code', mapping_=mapping_)
        if self.detail is not None:
            detail_ = self.detail
            detail_.to_etree(element, name_='detail', mapping_=mapping_)
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
        super(Condition_Location, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'code':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.code = obj_
            obj_.original_tagname_ = 'code'
        elif nodeName_ == 'detail':
            obj_ = string.factory()
            obj_.build(child_)
            self.detail = obj_
            obj_.original_tagname_ = 'detail'
        super(Condition_Location, self).buildChildren(child_, node, nodeName_, True)
# end class Condition_Location


class Condition_RelatedItem(BackboneElement):
    """Use to record detailed information about conditions, problems or
    diagnoses recognized by a clinician. There are many uses
    including: recording a Diagnosis during an Encounter; populating
    a problem List or a Summary Statement, such as a Discharge
    Summary."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, type_=None, code=None, target=None):
        self.original_tagname_ = None
        super(Condition_RelatedItem, self).__init__(id, extension, modifierExtension, )
        self.type_ = type_
        self.code = code
        self.target = target
    def factory(*args_, **kwargs_):
        if Condition_RelatedItem.subclass:
            return Condition_RelatedItem.subclass(*args_, **kwargs_)
        else:
            return Condition_RelatedItem(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_type(self): return self.type_
    def set_type(self, type_): self.type_ = type_
    def get_code(self): return self.code
    def set_code(self, code): self.code = code
    def get_target(self): return self.target
    def set_target(self, target): self.target = target
    def hasContent_(self):
        if (
            self.type_ is not None or
            self.code is not None or
            self.target is not None or
            super(Condition_RelatedItem, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Condition.RelatedItem', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Condition.RelatedItem')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Condition.RelatedItem', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Condition.RelatedItem'):
        super(Condition_RelatedItem, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Condition.RelatedItem')
    def exportChildren(self, outfile, level, namespace_='', name_='Condition.RelatedItem', fromsubclass_=False, pretty_print=True):
        super(Condition_RelatedItem, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.type_ is not None:
            self.type_.export(outfile, level, namespace_, name_='type', pretty_print=pretty_print)
        if self.code is not None:
            self.code.export(outfile, level, namespace_, name_='code', pretty_print=pretty_print)
        if self.target is not None:
            self.target.export(outfile, level, namespace_, name_='target', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Condition.RelatedItem', mapping_=None):
        element = super(Condition_RelatedItem, self).to_etree(parent_element, name_, mapping_)
        if self.type_ is not None:
            type__ = self.type_
            type__.to_etree(element, name_='type', mapping_=mapping_)
        if self.code is not None:
            code_ = self.code
            code_.to_etree(element, name_='code', mapping_=mapping_)
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
        super(Condition_RelatedItem, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'type':
            obj_ = ConditionRelationshipType.factory()
            obj_.build(child_)
            self.type_ = obj_
            obj_.original_tagname_ = 'type'
        elif nodeName_ == 'code':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.code = obj_
            obj_.original_tagname_ = 'code'
        elif nodeName_ == 'target':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.target = obj_
            obj_.original_tagname_ = 'target'
        super(Condition_RelatedItem, self).buildChildren(child_, node, nodeName_, True)
# end class Condition_RelatedItem


class ConditionStatus(Element):
    """The clinical status of the Condition or diagnosisIf the element is
    present, it must have either a @value, an @id, or extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(ConditionStatus, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if ConditionStatus.subclass:
            return ConditionStatus.subclass(*args_, **kwargs_)
        else:
            return ConditionStatus(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(ConditionStatus, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='ConditionStatus', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ConditionStatus')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='ConditionStatus', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='ConditionStatus'):
        super(ConditionStatus, self).exportAttributes(outfile, level, already_processed, namespace_, name_='ConditionStatus')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='ConditionStatus', fromsubclass_=False, pretty_print=True):
        super(ConditionStatus, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='ConditionStatus', mapping_=None):
        element = super(ConditionStatus, self).to_etree(parent_element, name_, mapping_)
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
        super(ConditionStatus, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(ConditionStatus, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class ConditionStatus


class ConditionRelationshipType(Element):
    """The type of relationship between a condition and its related itemIf
    the element is present, it must have either a @value, an @id, or
    extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(ConditionRelationshipType, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if ConditionRelationshipType.subclass:
            return ConditionRelationshipType.subclass(*args_, **kwargs_)
        else:
            return ConditionRelationshipType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(ConditionRelationshipType, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='ConditionRelationshipType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ConditionRelationshipType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='ConditionRelationshipType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='ConditionRelationshipType'):
        super(ConditionRelationshipType, self).exportAttributes(outfile, level, already_processed, namespace_, name_='ConditionRelationshipType')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='ConditionRelationshipType', fromsubclass_=False, pretty_print=True):
        super(ConditionRelationshipType, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='ConditionRelationshipType', mapping_=None):
        element = super(ConditionRelationshipType, self).to_etree(parent_element, name_, mapping_)
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
        super(ConditionRelationshipType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(ConditionRelationshipType, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class ConditionRelationshipType
