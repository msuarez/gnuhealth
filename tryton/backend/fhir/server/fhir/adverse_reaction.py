from .base_classes import *
from .support_functions import *


class AdverseReaction(Resource):
    """Records an unexpected reaction suspected to be related to the
    exposure of the reaction subject to a substance.If the element
    is present, it must have either a @value, an @id, or extensions"""
    subclass = None
    superclass = Resource
    def __init__(self, id=None, extension=None, modifierExtension=None, language=None, text=None, contained=None, identifier=None, date=None, subject=None, didNotOccurFlag=None, recorder=None, symptom=None, exposure=None):
        self.original_tagname_ = None
        super(AdverseReaction, self).__init__(id, extension, modifierExtension, language, text, contained, )
        if identifier is None:
            self.identifier = []
        else:
            self.identifier = identifier
        self.date = date
        self.subject = subject
        self.didNotOccurFlag = didNotOccurFlag
        self.recorder = recorder
        if symptom is None:
            self.symptom = []
        else:
            self.symptom = symptom
        if exposure is None:
            self.exposure = []
        else:
            self.exposure = exposure
    def factory(*args_, **kwargs_):
        if AdverseReaction.subclass:
            return AdverseReaction.subclass(*args_, **kwargs_)
        else:
            return AdverseReaction(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_identifier(self): return self.identifier
    def set_identifier(self, identifier): self.identifier = identifier
    def add_identifier(self, value): self.identifier.append(value)
    def insert_identifier(self, index, value): self.identifier[index] = value
    def get_date(self): return self.date
    def set_date(self, date): self.date = date
    def get_subject(self): return self.subject
    def set_subject(self, subject): self.subject = subject
    def get_didNotOccurFlag(self): return self.didNotOccurFlag
    def set_didNotOccurFlag(self, didNotOccurFlag): self.didNotOccurFlag = didNotOccurFlag
    def get_recorder(self): return self.recorder
    def set_recorder(self, recorder): self.recorder = recorder
    def get_symptom(self): return self.symptom
    def set_symptom(self, symptom): self.symptom = symptom
    def add_symptom(self, value): self.symptom.append(value)
    def insert_symptom(self, index, value): self.symptom[index] = value
    def get_exposure(self): return self.exposure
    def set_exposure(self, exposure): self.exposure = exposure
    def add_exposure(self, value): self.exposure.append(value)
    def insert_exposure(self, index, value): self.exposure[index] = value
    def hasContent_(self):
        if (
            self.identifier or
            self.date is not None or
            self.subject is not None or
            self.didNotOccurFlag is not None or
            self.recorder is not None or
            self.symptom or
            self.exposure or
            super(AdverseReaction, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='AdverseReaction', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='AdverseReaction')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='AdverseReaction', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='AdverseReaction'):
        super(AdverseReaction, self).exportAttributes(outfile, level, already_processed, namespace_, name_='AdverseReaction')
    def exportChildren(self, outfile, level, namespace_='', name_='AdverseReaction', fromsubclass_=False, pretty_print=True):
        super(AdverseReaction, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for identifier_ in self.identifier:
            identifier_.export(outfile, level, namespace_, name_='identifier', pretty_print=pretty_print)
        if self.date is not None:
            self.date.export(outfile, level, namespace_, name_='date', pretty_print=pretty_print)
        if self.subject is not None:
            self.subject.export(outfile, level, namespace_, name_='subject', pretty_print=pretty_print)
        if self.didNotOccurFlag is not None:
            self.didNotOccurFlag.export(outfile, level, namespace_, name_='didNotOccurFlag', pretty_print=pretty_print)
        if self.recorder is not None:
            self.recorder.export(outfile, level, namespace_, name_='recorder', pretty_print=pretty_print)
        for symptom_ in self.symptom:
            symptom_.export(outfile, level, namespace_, name_='symptom', pretty_print=pretty_print)
        for exposure_ in self.exposure:
            exposure_.export(outfile, level, namespace_, name_='exposure', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='AdverseReaction', mapping_=None):
        element = super(AdverseReaction, self).to_etree(parent_element, name_, mapping_)
        for identifier_ in self.identifier:
            identifier_.to_etree(element, name_='identifier', mapping_=mapping_)
        if self.date is not None:
            date_ = self.date
            date_.to_etree(element, name_='date', mapping_=mapping_)
        if self.subject is not None:
            subject_ = self.subject
            subject_.to_etree(element, name_='subject', mapping_=mapping_)
        if self.didNotOccurFlag is not None:
            didNotOccurFlag_ = self.didNotOccurFlag
            didNotOccurFlag_.to_etree(element, name_='didNotOccurFlag', mapping_=mapping_)
        if self.recorder is not None:
            recorder_ = self.recorder
            recorder_.to_etree(element, name_='recorder', mapping_=mapping_)
        for symptom_ in self.symptom:
            symptom_.to_etree(element, name_='symptom', mapping_=mapping_)
        for exposure_ in self.exposure:
            exposure_.to_etree(element, name_='exposure', mapping_=mapping_)
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
        super(AdverseReaction, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'identifier':
            obj_ = Identifier.factory()
            obj_.build(child_)
            self.identifier.append(obj_)
            obj_.original_tagname_ = 'identifier'
        elif nodeName_ == 'date':
            obj_ = dateTime.factory()
            obj_.build(child_)
            self.date = obj_
            obj_.original_tagname_ = 'date'
        elif nodeName_ == 'subject':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.subject = obj_
            obj_.original_tagname_ = 'subject'
        elif nodeName_ == 'didNotOccurFlag':
            obj_ = boolean.factory()
            obj_.build(child_)
            self.didNotOccurFlag = obj_
            obj_.original_tagname_ = 'didNotOccurFlag'
        elif nodeName_ == 'recorder':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.recorder = obj_
            obj_.original_tagname_ = 'recorder'
        elif nodeName_ == 'symptom':
            obj_ = AdverseReaction_Symptom.factory()
            obj_.build(child_)
            self.symptom.append(obj_)
            obj_.original_tagname_ = 'symptom'
        elif nodeName_ == 'exposure':
            obj_ = AdverseReaction_Exposure.factory()
            obj_.build(child_)
            self.exposure.append(obj_)
            obj_.original_tagname_ = 'exposure'
        super(AdverseReaction, self).buildChildren(child_, node, nodeName_, True)
# end class AdverseReaction


class AdverseReaction_Symptom(BackboneElement):
    """Records an unexpected reaction suspected to be related to the
    exposure of the reaction subject to a substance."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, code=None, severity=None):
        self.original_tagname_ = None
        super(AdverseReaction_Symptom, self).__init__(id, extension, modifierExtension, )
        self.code = code
        self.severity = severity
    def factory(*args_, **kwargs_):
        if AdverseReaction_Symptom.subclass:
            return AdverseReaction_Symptom.subclass(*args_, **kwargs_)
        else:
            return AdverseReaction_Symptom(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_code(self): return self.code
    def set_code(self, code): self.code = code
    def get_severity(self): return self.severity
    def set_severity(self, severity): self.severity = severity
    def hasContent_(self):
        if (
            self.code is not None or
            self.severity is not None or
            super(AdverseReaction_Symptom, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='AdverseReaction.Symptom', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='AdverseReaction.Symptom')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='AdverseReaction.Symptom', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='AdverseReaction.Symptom'):
        super(AdverseReaction_Symptom, self).exportAttributes(outfile, level, already_processed, namespace_, name_='AdverseReaction.Symptom')
    def exportChildren(self, outfile, level, namespace_='', name_='AdverseReaction.Symptom', fromsubclass_=False, pretty_print=True):
        super(AdverseReaction_Symptom, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.code is not None:
            self.code.export(outfile, level, namespace_, name_='code', pretty_print=pretty_print)
        if self.severity is not None:
            self.severity.export(outfile, level, namespace_, name_='severity', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='AdverseReaction.Symptom', mapping_=None):
        element = super(AdverseReaction_Symptom, self).to_etree(parent_element, name_, mapping_)
        if self.code is not None:
            code_ = self.code
            code_.to_etree(element, name_='code', mapping_=mapping_)
        if self.severity is not None:
            severity_ = self.severity
            severity_.to_etree(element, name_='severity', mapping_=mapping_)
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
        super(AdverseReaction_Symptom, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'code':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.code = obj_
            obj_.original_tagname_ = 'code'
        elif nodeName_ == 'severity':
            obj_ = ReactionSeverity.factory()
            obj_.build(child_)
            self.severity = obj_
            obj_.original_tagname_ = 'severity'
        super(AdverseReaction_Symptom, self).buildChildren(child_, node, nodeName_, True)
# end class AdverseReaction_Symptom


class AdverseReaction_Exposure(BackboneElement):
    """Records an unexpected reaction suspected to be related to the
    exposure of the reaction subject to a substance."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, date=None, type_=None, causalityExpectation=None, substance=None):
        self.original_tagname_ = None
        super(AdverseReaction_Exposure, self).__init__(id, extension, modifierExtension, )
        self.date = date
        self.type_ = type_
        self.causalityExpectation = causalityExpectation
        self.substance = substance
    def factory(*args_, **kwargs_):
        if AdverseReaction_Exposure.subclass:
            return AdverseReaction_Exposure.subclass(*args_, **kwargs_)
        else:
            return AdverseReaction_Exposure(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_date(self): return self.date
    def set_date(self, date): self.date = date
    def get_type(self): return self.type_
    def set_type(self, type_): self.type_ = type_
    def get_causalityExpectation(self): return self.causalityExpectation
    def set_causalityExpectation(self, causalityExpectation): self.causalityExpectation = causalityExpectation
    def get_substance(self): return self.substance
    def set_substance(self, substance): self.substance = substance
    def hasContent_(self):
        if (
            self.date is not None or
            self.type_ is not None or
            self.causalityExpectation is not None or
            self.substance is not None or
            super(AdverseReaction_Exposure, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='AdverseReaction.Exposure', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='AdverseReaction.Exposure')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='AdverseReaction.Exposure', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='AdverseReaction.Exposure'):
        super(AdverseReaction_Exposure, self).exportAttributes(outfile, level, already_processed, namespace_, name_='AdverseReaction.Exposure')
    def exportChildren(self, outfile, level, namespace_='', name_='AdverseReaction.Exposure', fromsubclass_=False, pretty_print=True):
        super(AdverseReaction_Exposure, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.date is not None:
            self.date.export(outfile, level, namespace_, name_='date', pretty_print=pretty_print)
        if self.type_ is not None:
            self.type_.export(outfile, level, namespace_, name_='type', pretty_print=pretty_print)
        if self.causalityExpectation is not None:
            self.causalityExpectation.export(outfile, level, namespace_, name_='causalityExpectation', pretty_print=pretty_print)
        if self.substance is not None:
            self.substance.export(outfile, level, namespace_, name_='substance', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='AdverseReaction.Exposure', mapping_=None):
        element = super(AdverseReaction_Exposure, self).to_etree(parent_element, name_, mapping_)
        if self.date is not None:
            date_ = self.date
            date_.to_etree(element, name_='date', mapping_=mapping_)
        if self.type_ is not None:
            type__ = self.type_
            type__.to_etree(element, name_='type', mapping_=mapping_)
        if self.causalityExpectation is not None:
            causalityExpectation_ = self.causalityExpectation
            causalityExpectation_.to_etree(element, name_='causalityExpectation', mapping_=mapping_)
        if self.substance is not None:
            substance_ = self.substance
            substance_.to_etree(element, name_='substance', mapping_=mapping_)
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
        super(AdverseReaction_Exposure, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'date':
            obj_ = dateTime.factory()
            obj_.build(child_)
            self.date = obj_
            obj_.original_tagname_ = 'date'
        elif nodeName_ == 'type':
            obj_ = ExposureType.factory()
            obj_.build(child_)
            self.type_ = obj_
            obj_.original_tagname_ = 'type'
        elif nodeName_ == 'causalityExpectation':
            obj_ = CausalityExpectation.factory()
            obj_.build(child_)
            self.causalityExpectation = obj_
            obj_.original_tagname_ = 'causalityExpectation'
        elif nodeName_ == 'substance':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.substance = obj_
            obj_.original_tagname_ = 'substance'
        super(AdverseReaction_Exposure, self).buildChildren(child_, node, nodeName_, True)
# end class AdverseReaction_Exposure


class ReactionSeverity(Element):
    """The severity of an adverse reaction.If the element is present, it
    must have either a @value, an @id, or extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(ReactionSeverity, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if ReactionSeverity.subclass:
            return ReactionSeverity.subclass(*args_, **kwargs_)
        else:
            return ReactionSeverity(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(ReactionSeverity, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='ReactionSeverity', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ReactionSeverity')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='ReactionSeverity', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='ReactionSeverity'):
        super(ReactionSeverity, self).exportAttributes(outfile, level, already_processed, namespace_, name_='ReactionSeverity')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='ReactionSeverity', fromsubclass_=False, pretty_print=True):
        super(ReactionSeverity, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='ReactionSeverity', mapping_=None):
        element = super(ReactionSeverity, self).to_etree(parent_element, name_, mapping_)
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
        super(ReactionSeverity, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(ReactionSeverity, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class ReactionSeverity


class ExposureType(Element):
    """The type of exposure that resulted in an adverse reactionIf the
    element is present, it must have either a @value, an @id, or
    extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(ExposureType, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if ExposureType.subclass:
            return ExposureType.subclass(*args_, **kwargs_)
        else:
            return ExposureType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(ExposureType, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='ExposureType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ExposureType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='ExposureType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='ExposureType'):
        super(ExposureType, self).exportAttributes(outfile, level, already_processed, namespace_, name_='ExposureType')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='ExposureType', fromsubclass_=False, pretty_print=True):
        super(ExposureType, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='ExposureType', mapping_=None):
        element = super(ExposureType, self).to_etree(parent_element, name_, mapping_)
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
        super(ExposureType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(ExposureType, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class ExposureType


class CausalityExpectation(Element):
    """How likely is it that the given exposure caused a reactionIf the
    element is present, it must have either a @value, an @id, or
    extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(CausalityExpectation, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if CausalityExpectation.subclass:
            return CausalityExpectation.subclass(*args_, **kwargs_)
        else:
            return CausalityExpectation(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(CausalityExpectation, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='CausalityExpectation', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='CausalityExpectation')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='CausalityExpectation', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='CausalityExpectation'):
        super(CausalityExpectation, self).exportAttributes(outfile, level, already_processed, namespace_, name_='CausalityExpectation')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='CausalityExpectation', fromsubclass_=False, pretty_print=True):
        super(CausalityExpectation, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='CausalityExpectation', mapping_=None):
        element = super(CausalityExpectation, self).to_etree(parent_element, name_, mapping_)
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
        super(CausalityExpectation, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(CausalityExpectation, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class CausalityExpectation


class SensitivityStatus(Element):
    """The status of the adverse sensitivityIf the element is present, it
    must have either a @value, an @id, or extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(SensitivityStatus, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if SensitivityStatus.subclass:
            return SensitivityStatus.subclass(*args_, **kwargs_)
        else:
            return SensitivityStatus(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(SensitivityStatus, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='SensitivityStatus', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='SensitivityStatus')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='SensitivityStatus', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='SensitivityStatus'):
        super(SensitivityStatus, self).exportAttributes(outfile, level, already_processed, namespace_, name_='SensitivityStatus')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='SensitivityStatus', fromsubclass_=False, pretty_print=True):
        super(SensitivityStatus, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='SensitivityStatus', mapping_=None):
        element = super(SensitivityStatus, self).to_etree(parent_element, name_, mapping_)
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
        super(SensitivityStatus, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(SensitivityStatus, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class SensitivityStatus


class Criticality(Element):
    """The criticality of an adverse sensitivityIf the element is present,
    it must have either a @value, an @id, or extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(Criticality, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if Criticality.subclass:
            return Criticality.subclass(*args_, **kwargs_)
        else:
            return Criticality(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(Criticality, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Criticality', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Criticality')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Criticality', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Criticality'):
        super(Criticality, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Criticality')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='Criticality', fromsubclass_=False, pretty_print=True):
        super(Criticality, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Criticality', mapping_=None):
        element = super(Criticality, self).to_etree(parent_element, name_, mapping_)
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
        super(Criticality, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(Criticality, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class Criticality


class SensitivityType(Element):
    """The type of an adverse sensitivityIf the element is present, it must
    have either a @value, an @id, or extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(SensitivityType, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if SensitivityType.subclass:
            return SensitivityType.subclass(*args_, **kwargs_)
        else:
            return SensitivityType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(SensitivityType, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='SensitivityType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='SensitivityType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='SensitivityType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='SensitivityType'):
        super(SensitivityType, self).exportAttributes(outfile, level, already_processed, namespace_, name_='SensitivityType')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='SensitivityType', fromsubclass_=False, pretty_print=True):
        super(SensitivityType, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='SensitivityType', mapping_=None):
        element = super(SensitivityType, self).to_etree(parent_element, name_, mapping_)
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
        super(SensitivityType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(SensitivityType, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class SensitivityType


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
