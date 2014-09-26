from .base_classes import Element, ResourceReference
from .config import *
from .primitive_types import *
from .support_functions import *


class CodeableConcept(Element):
    """A concept that may be defined by a formal reference to a terminology
    or ontology or may be provided by text.If the element is
    present, it must have a value for at least one of the defined
    elements, an @id referenced from the Narrative, or extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, coding=None, text=None):
        self.original_tagname_ = None
        super(CodeableConcept, self).__init__(id, extension, )
        if coding is None:
            self.coding = []
        else:
            self.coding = coding
        self.text = text
    def factory(*args_, **kwargs_):
        if CodeableConcept.subclass:
            return CodeableConcept.subclass(*args_, **kwargs_)
        else:
            return CodeableConcept(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_coding(self): return self.coding
    def set_coding(self, coding): self.coding = coding
    def add_coding(self, value): self.coding.append(value)
    def insert_coding(self, index, value): self.coding[index] = value
    def get_text(self): return self.text
    def set_text(self, text): self.text = text
    def hasContent_(self):
        if (
            self.coding or
            self.text is not None or
            super(CodeableConcept, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='CodeableConcept', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='CodeableConcept')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='CodeableConcept', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='CodeableConcept'):
        super(CodeableConcept, self).exportAttributes(outfile, level, already_processed, namespace_, name_='CodeableConcept')
    def exportChildren(self, outfile, level, namespace_='', name_='CodeableConcept', fromsubclass_=False, pretty_print=True):
        super(CodeableConcept, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for coding_ in self.coding:
            coding_.export(outfile, level, namespace_, name_='coding', pretty_print=pretty_print)
        if self.text is not None:
            self.text.export(outfile, level, namespace_, name_='text', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='CodeableConcept', mapping_=None):
        element = super(CodeableConcept, self).to_etree(parent_element, name_, mapping_)
        for coding_ in self.coding:
            coding_.to_etree(element, name_='coding', mapping_=mapping_)
        if self.text is not None:
            text_ = self.text
            text_.to_etree(element, name_='text', mapping_=mapping_)
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
        super(CodeableConcept, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'coding':
            obj_ = Coding.factory()
            obj_.build(child_)
            self.coding.append(obj_)
            obj_.original_tagname_ = 'coding'
        elif nodeName_ == 'text':
            obj_ = string.factory()
            obj_.build(child_)
            self.text = obj_
            obj_.original_tagname_ = 'text'
        super(CodeableConcept, self).buildChildren(child_, node, nodeName_, True)
# end class CodeableConcept


class HumanName(Element):
    """A human's name with the ability to identify parts and usage.If the
    element is present, it must have a value for at least one of the
    defined elements, an @id referenced from the Narrative, or
    extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, use=None, text=None, family=None, given=None, prefix=None, suffix=None, period=None):
        self.original_tagname_ = None
        super(HumanName, self).__init__(id, extension, )
        self.use = use
        self.text = text
        if family is None:
            self.family = []
        else:
            self.family = family
        if given is None:
            self.given = []
        else:
            self.given = given
        if prefix is None:
            self.prefix = []
        else:
            self.prefix = prefix
        if suffix is None:
            self.suffix = []
        else:
            self.suffix = suffix
        self.period = period
    def factory(*args_, **kwargs_):
        if HumanName.subclass:
            return HumanName.subclass(*args_, **kwargs_)
        else:
            return HumanName(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_use(self): return self.use
    def set_use(self, use): self.use = use
    def get_text(self): return self.text
    def set_text(self, text): self.text = text
    def get_family(self): return self.family
    def set_family(self, family): self.family = family
    def add_family(self, value): self.family.append(value)
    def insert_family(self, index, value): self.family[index] = value
    def get_given(self): return self.given
    def set_given(self, given): self.given = given
    def add_given(self, value): self.given.append(value)
    def insert_given(self, index, value): self.given[index] = value
    def get_prefix(self): return self.prefix
    def set_prefix(self, prefix): self.prefix = prefix
    def add_prefix(self, value): self.prefix.append(value)
    def insert_prefix(self, index, value): self.prefix[index] = value
    def get_suffix(self): return self.suffix
    def set_suffix(self, suffix): self.suffix = suffix
    def add_suffix(self, value): self.suffix.append(value)
    def insert_suffix(self, index, value): self.suffix[index] = value
    def get_period(self): return self.period
    def set_period(self, period): self.period = period
    def hasContent_(self):
        if (
            self.use is not None or
            self.text is not None or
            self.family or
            self.given or
            self.prefix or
            self.suffix or
            self.period is not None or
            super(HumanName, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='HumanName', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='HumanName')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='HumanName', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='HumanName'):
        super(HumanName, self).exportAttributes(outfile, level, already_processed, namespace_, name_='HumanName')
    def exportChildren(self, outfile, level, namespace_='', name_='HumanName', fromsubclass_=False, pretty_print=True):
        super(HumanName, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.use is not None:
            self.use.export(outfile, level, namespace_, name_='use', pretty_print=pretty_print)
        if self.text is not None:
            self.text.export(outfile, level, namespace_, name_='text', pretty_print=pretty_print)
        for family_ in self.family:
            family_.export(outfile, level, namespace_, name_='family', pretty_print=pretty_print)
        for given_ in self.given:
            given_.export(outfile, level, namespace_, name_='given', pretty_print=pretty_print)
        for prefix_ in self.prefix:
            prefix_.export(outfile, level, namespace_, name_='prefix', pretty_print=pretty_print)
        for suffix_ in self.suffix:
            suffix_.export(outfile, level, namespace_, name_='suffix', pretty_print=pretty_print)
        if self.period is not None:
            self.period.export(outfile, level, namespace_, name_='period', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='HumanName', mapping_=None):
        element = super(HumanName, self).to_etree(parent_element, name_, mapping_)
        if self.use is not None:
            use_ = self.use
            use_.to_etree(element, name_='use', mapping_=mapping_)
        if self.text is not None:
            text_ = self.text
            text_.to_etree(element, name_='text', mapping_=mapping_)
        for family_ in self.family:
            family_.to_etree(element, name_='family', mapping_=mapping_)
        for given_ in self.given:
            given_.to_etree(element, name_='given', mapping_=mapping_)
        for prefix_ in self.prefix:
            prefix_.to_etree(element, name_='prefix', mapping_=mapping_)
        for suffix_ in self.suffix:
            suffix_.to_etree(element, name_='suffix', mapping_=mapping_)
        if self.period is not None:
            period_ = self.period
            period_.to_etree(element, name_='period', mapping_=mapping_)
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
        super(HumanName, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'use':
            obj_ = NameUse.factory()
            obj_.build(child_)
            self.use = obj_
            obj_.original_tagname_ = 'use'
        elif nodeName_ == 'text':
            obj_ = string.factory()
            obj_.build(child_)
            self.text = obj_
            obj_.original_tagname_ = 'text'
        elif nodeName_ == 'family':
            obj_ = string.factory()
            obj_.build(child_)
            self.family.append(obj_)
            obj_.original_tagname_ = 'family'
        elif nodeName_ == 'given':
            obj_ = string.factory()
            obj_.build(child_)
            self.given.append(obj_)
            obj_.original_tagname_ = 'given'
        elif nodeName_ == 'prefix':
            obj_ = string.factory()
            obj_.build(child_)
            self.prefix.append(obj_)
            obj_.original_tagname_ = 'prefix'
        elif nodeName_ == 'suffix':
            obj_ = string.factory()
            obj_.build(child_)
            self.suffix.append(obj_)
            obj_.original_tagname_ = 'suffix'
        elif nodeName_ == 'period':
            obj_ = Period.factory()
            obj_.build(child_)
            self.period = obj_
            obj_.original_tagname_ = 'period'
        super(HumanName, self).buildChildren(child_, node, nodeName_, True)
# end class HumanName


class NameUse(Element):
    """The use of a human nameIf the element is present, it must have
    either a @value, an @id, or extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(NameUse, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if NameUse.subclass:
            return NameUse.subclass(*args_, **kwargs_)
        else:
            return NameUse(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(NameUse, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='NameUse', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='NameUse')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='NameUse', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='NameUse'):
        super(NameUse, self).exportAttributes(outfile, level, already_processed, namespace_, name_='NameUse')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='NameUse', fromsubclass_=False, pretty_print=True):
        super(NameUse, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='NameUse', mapping_=None):
        element = super(NameUse, self).to_etree(parent_element, name_, mapping_)
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
        super(NameUse, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(NameUse, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class NameUse


class Identifier(Element):
    """A technical identifier - identifies some entity uniquely and
    unambiguously.If the element is present, it must have a value
    for at least one of the defined elements, an @id referenced from
    the Narrative, or extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, use=None, label=None, system=None, value=None, period=None, assigner=None):
        self.original_tagname_ = None
        super(Identifier, self).__init__(id, extension, )
        self.use = use
        self.label = label
        self.system = system
        self.value = value
        self.period = period
        self.assigner = assigner
    def factory(*args_, **kwargs_):
        if Identifier.subclass:
            return Identifier.subclass(*args_, **kwargs_)
        else:
            return Identifier(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_use(self): return self.use
    def set_use(self, use): self.use = use
    def get_label(self): return self.label
    def set_label(self, label): self.label = label
    def get_system(self): return self.system
    def set_system(self, system): self.system = system
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def get_period(self): return self.period
    def set_period(self, period): self.period = period
    def get_assigner(self): return self.assigner
    def set_assigner(self, assigner): self.assigner = assigner
    def hasContent_(self):
        if (
            self.use is not None or
            self.label is not None or
            self.system is not None or
            self.value is not None or
            self.period is not None or
            self.assigner is not None or
            super(Identifier, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Identifier', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Identifier')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Identifier', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Identifier'):
        super(Identifier, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Identifier')
    def exportChildren(self, outfile, level, namespace_='', name_='Identifier', fromsubclass_=False, pretty_print=True):
        super(Identifier, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.use is not None:
            self.use.export(outfile, level, namespace_, name_='use', pretty_print=pretty_print)
        if self.label is not None:
            self.label.export(outfile, level, namespace_, name_='label', pretty_print=pretty_print)
        if self.system is not None:
            self.system.export(outfile, level, namespace_, name_='system', pretty_print=pretty_print)
        if self.value is not None:
            self.value.export(outfile, level, namespace_, name_='value', pretty_print=pretty_print)
        if self.period is not None:
            self.period.export(outfile, level, namespace_, name_='period', pretty_print=pretty_print)
        if self.assigner is not None:
            self.assigner.export(outfile, level, namespace_, name_='assigner', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Identifier', mapping_=None):
        element = super(Identifier, self).to_etree(parent_element, name_, mapping_)
        if self.use is not None:
            use_ = self.use
            use_.to_etree(element, name_='use', mapping_=mapping_)
        if self.label is not None:
            label_ = self.label
            label_.to_etree(element, name_='label', mapping_=mapping_)
        if self.system is not None:
            system_ = self.system
            system_.to_etree(element, name_='system', mapping_=mapping_)
        if self.value is not None:
            value_ = self.value
            value_.to_etree(element, name_='value', mapping_=mapping_)
        if self.period is not None:
            period_ = self.period
            period_.to_etree(element, name_='period', mapping_=mapping_)
        if self.assigner is not None:
            assigner_ = self.assigner
            assigner_.to_etree(element, name_='assigner', mapping_=mapping_)
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
        super(Identifier, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'use':
            obj_ = IdentifierUse.factory()
            obj_.build(child_)
            self.use = obj_
            obj_.original_tagname_ = 'use'
        elif nodeName_ == 'label':
            obj_ = string.factory()
            obj_.build(child_)
            self.label = obj_
            obj_.original_tagname_ = 'label'
        elif nodeName_ == 'system':
            obj_ = uri.factory()
            obj_.build(child_)
            self.system = obj_
            obj_.original_tagname_ = 'system'
        elif nodeName_ == 'value':
            obj_ = string.factory()
            obj_.build(child_)
            self.value = obj_
            obj_.original_tagname_ = 'value'
        elif nodeName_ == 'period':
            obj_ = Period.factory()
            obj_.build(child_)
            self.period = obj_
            obj_.original_tagname_ = 'period'
        elif nodeName_ == 'assigner':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.assigner = obj_
            obj_.original_tagname_ = 'assigner'
        super(Identifier, self).buildChildren(child_, node, nodeName_, True)
# end class Identifier


class IdentifierUse(Element):
    """Identifies the purpose for this identifier, if knownIf the element
    is present, it must have either a @value, an @id, or extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(IdentifierUse, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if IdentifierUse.subclass:
            return IdentifierUse.subclass(*args_, **kwargs_)
        else:
            return IdentifierUse(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(IdentifierUse, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='IdentifierUse', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='IdentifierUse')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='IdentifierUse', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='IdentifierUse'):
        super(IdentifierUse, self).exportAttributes(outfile, level, already_processed, namespace_, name_='IdentifierUse')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='IdentifierUse', fromsubclass_=False, pretty_print=True):
        super(IdentifierUse, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='IdentifierUse', mapping_=None):
        element = super(IdentifierUse, self).to_etree(parent_element, name_, mapping_)
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
        super(IdentifierUse, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(IdentifierUse, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class IdentifierUse


class Contact(Element):
    """All kinds of technology mediated contact details for a person or
    organization, including telephone, email, etc.If the element is
    present, it must have a value for at least one of the defined
    elements, an @id referenced from the Narrative, or extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, system=None, value=None, use=None, period=None):
        self.original_tagname_ = None
        super(Contact, self).__init__(id, extension, )
        self.system = system
        self.value = value
        self.use = use
        self.period = period
    def factory(*args_, **kwargs_):
        if Contact.subclass:
            return Contact.subclass(*args_, **kwargs_)
        else:
            return Contact(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_system(self): return self.system
    def set_system(self, system): self.system = system
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def get_use(self): return self.use
    def set_use(self, use): self.use = use
    def get_period(self): return self.period
    def set_period(self, period): self.period = period
    def hasContent_(self):
        if (
            self.system is not None or
            self.value is not None or
            self.use is not None or
            self.period is not None or
            super(Contact, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Contact', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Contact')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Contact', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Contact'):
        super(Contact, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Contact')
    def exportChildren(self, outfile, level, namespace_='', name_='Contact', fromsubclass_=False, pretty_print=True):
        super(Contact, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.system is not None:
            self.system.export(outfile, level, namespace_, name_='system', pretty_print=pretty_print)
        if self.value is not None:
            self.value.export(outfile, level, namespace_, name_='value', pretty_print=pretty_print)
        if self.use is not None:
            self.use.export(outfile, level, namespace_, name_='use', pretty_print=pretty_print)
        if self.period is not None:
            self.period.export(outfile, level, namespace_, name_='period', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Contact', mapping_=None):
        element = super(Contact, self).to_etree(parent_element, name_, mapping_)
        if self.system is not None:
            system_ = self.system
            system_.to_etree(element, name_='system', mapping_=mapping_)
        if self.value is not None:
            value_ = self.value
            value_.to_etree(element, name_='value', mapping_=mapping_)
        if self.use is not None:
            use_ = self.use
            use_.to_etree(element, name_='use', mapping_=mapping_)
        if self.period is not None:
            period_ = self.period
            period_.to_etree(element, name_='period', mapping_=mapping_)
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
        super(Contact, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'system':
            obj_ = ContactSystem.factory()
            obj_.build(child_)
            self.system = obj_
            obj_.original_tagname_ = 'system'
        elif nodeName_ == 'value':
            obj_ = string.factory()
            obj_.build(child_)
            self.value = obj_
            obj_.original_tagname_ = 'value'
        elif nodeName_ == 'use':
            obj_ = ContactUse.factory()
            obj_.build(child_)
            self.use = obj_
            obj_.original_tagname_ = 'use'
        elif nodeName_ == 'period':
            obj_ = Period.factory()
            obj_.build(child_)
            self.period = obj_
            obj_.original_tagname_ = 'period'
        super(Contact, self).buildChildren(child_, node, nodeName_, True)
# end class Contact


class ContactSystem(Element):
    """Telecommunications form for contactIf the element is present, it
    must have either a @value, an @id, or extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(ContactSystem, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if ContactSystem.subclass:
            return ContactSystem.subclass(*args_, **kwargs_)
        else:
            return ContactSystem(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(ContactSystem, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='ContactSystem', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ContactSystem')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='ContactSystem', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='ContactSystem'):
        super(ContactSystem, self).exportAttributes(outfile, level, already_processed, namespace_, name_='ContactSystem')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='ContactSystem', fromsubclass_=False, pretty_print=True):
        super(ContactSystem, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='ContactSystem', mapping_=None):
        element = super(ContactSystem, self).to_etree(parent_element, name_, mapping_)
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
        super(ContactSystem, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(ContactSystem, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class ContactSystem


class ContactUse(Element):
    """Location, type or status of telecommunications address indicating
    useIf the element is present, it must have either a @value, an
    @id, or extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(ContactUse, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if ContactUse.subclass:
            return ContactUse.subclass(*args_, **kwargs_)
        else:
            return ContactUse(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(ContactUse, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='ContactUse', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ContactUse')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='ContactUse', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='ContactUse'):
        super(ContactUse, self).exportAttributes(outfile, level, already_processed, namespace_, name_='ContactUse')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='ContactUse', fromsubclass_=False, pretty_print=True):
        super(ContactUse, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='ContactUse', mapping_=None):
        element = super(ContactUse, self).to_etree(parent_element, name_, mapping_)
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
        super(ContactUse, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(ContactUse, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class ContactUse


class Address(Element):
    """There is a variety of postal address formats defined around the
    world. This format defines a superset that is the basis for all
    addresses around the world.If the element is present, it must
    have a value for at least one of the defined elements, an @id
    referenced from the Narrative, or extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, use=None, text=None, line=None, city=None, state=None, zip=None, country=None, period=None):
        self.original_tagname_ = None
        super(Address, self).__init__(id, extension, )
        self.use = use
        self.text = text
        if line is None:
            self.line = []
        else:
            self.line = line
        self.city = city
        self.state = state
        self.zip = zip
        self.country = country
        self.period = period
    def factory(*args_, **kwargs_):
        if Address.subclass:
            return Address.subclass(*args_, **kwargs_)
        else:
            return Address(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_use(self): return self.use
    def set_use(self, use): self.use = use
    def get_text(self): return self.text
    def set_text(self, text): self.text = text
    def get_line(self): return self.line
    def set_line(self, line): self.line = line
    def add_line(self, value): self.line.append(value)
    def insert_line(self, index, value): self.line[index] = value
    def get_city(self): return self.city
    def set_city(self, city): self.city = city
    def get_state(self): return self.state
    def set_state(self, state): self.state = state
    def get_zip(self): return self.zip
    def set_zip(self, zip): self.zip = zip
    def get_country(self): return self.country
    def set_country(self, country): self.country = country
    def get_period(self): return self.period
    def set_period(self, period): self.period = period
    def hasContent_(self):
        if (
            self.use is not None or
            self.text is not None or
            self.line or
            self.city is not None or
            self.state is not None or
            self.zip is not None or
            self.country is not None or
            self.period is not None or
            super(Address, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Address', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Address')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Address', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Address'):
        super(Address, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Address')
    def exportChildren(self, outfile, level, namespace_='', name_='Address', fromsubclass_=False, pretty_print=True):
        super(Address, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.use is not None:
            self.use.export(outfile, level, namespace_, name_='use', pretty_print=pretty_print)
        if self.text is not None:
            self.text.export(outfile, level, namespace_, name_='text', pretty_print=pretty_print)
        for line_ in self.line:
            line_.export(outfile, level, namespace_, name_='line', pretty_print=pretty_print)
        if self.city is not None:
            self.city.export(outfile, level, namespace_, name_='city', pretty_print=pretty_print)
        if self.state is not None:
            self.state.export(outfile, level, namespace_, name_='state', pretty_print=pretty_print)
        if self.zip is not None:
            self.zip.export(outfile, level, namespace_, name_='zip', pretty_print=pretty_print)
        if self.country is not None:
            self.country.export(outfile, level, namespace_, name_='country', pretty_print=pretty_print)
        if self.period is not None:
            self.period.export(outfile, level, namespace_, name_='period', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Address', mapping_=None):
        element = super(Address, self).to_etree(parent_element, name_, mapping_)
        if self.use is not None:
            use_ = self.use
            use_.to_etree(element, name_='use', mapping_=mapping_)
        if self.text is not None:
            text_ = self.text
            text_.to_etree(element, name_='text', mapping_=mapping_)
        for line_ in self.line:
            line_.to_etree(element, name_='line', mapping_=mapping_)
        if self.city is not None:
            city_ = self.city
            city_.to_etree(element, name_='city', mapping_=mapping_)
        if self.state is not None:
            state_ = self.state
            state_.to_etree(element, name_='state', mapping_=mapping_)
        if self.zip is not None:
            zip_ = self.zip
            zip_.to_etree(element, name_='zip', mapping_=mapping_)
        if self.country is not None:
            country_ = self.country
            country_.to_etree(element, name_='country', mapping_=mapping_)
        if self.period is not None:
            period_ = self.period
            period_.to_etree(element, name_='period', mapping_=mapping_)
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
        super(Address, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'use':
            obj_ = AddressUse.factory()
            obj_.build(child_)
            self.use = obj_
            obj_.original_tagname_ = 'use'
        elif nodeName_ == 'text':
            obj_ = string.factory()
            obj_.build(child_)
            self.text = obj_
            obj_.original_tagname_ = 'text'
        elif nodeName_ == 'line':
            obj_ = string.factory()
            obj_.build(child_)
            self.line.append(obj_)
            obj_.original_tagname_ = 'line'
        elif nodeName_ == 'city':
            obj_ = string.factory()
            obj_.build(child_)
            self.city = obj_
            obj_.original_tagname_ = 'city'
        elif nodeName_ == 'state':
            obj_ = string.factory()
            obj_.build(child_)
            self.state = obj_
            obj_.original_tagname_ = 'state'
        elif nodeName_ == 'zip':
            obj_ = string.factory()
            obj_.build(child_)
            self.zip = obj_
            obj_.original_tagname_ = 'zip'
        elif nodeName_ == 'country':
            obj_ = string.factory()
            obj_.build(child_)
            self.country = obj_
            obj_.original_tagname_ = 'country'
        elif nodeName_ == 'period':
            obj_ = Period.factory()
            obj_.build(child_)
            self.period = obj_
            obj_.original_tagname_ = 'period'
        super(Address, self).buildChildren(child_, node, nodeName_, True)
# end class Address


class AddressUse(Element):
    """The use of an addressIf the element is present, it must have either
    a @value, an @id, or extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(AddressUse, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if AddressUse.subclass:
            return AddressUse.subclass(*args_, **kwargs_)
        else:
            return AddressUse(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(AddressUse, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='AddressUse', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='AddressUse')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='AddressUse', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='AddressUse'):
        super(AddressUse, self).exportAttributes(outfile, level, already_processed, namespace_, name_='AddressUse')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='AddressUse', fromsubclass_=False, pretty_print=True):
        super(AddressUse, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='AddressUse', mapping_=None):
        element = super(AddressUse, self).to_etree(parent_element, name_, mapping_)
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
        super(AddressUse, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(AddressUse, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class AddressUse


class Schedule(Element):
    """Specifies an event that may occur multiple times. Schedules are used
    for to reord when things are expected or requested to occur.If
    the element is present, it must have a value for at least one of
    the defined elements, an @id referenced from the Narrative, or
    extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, event=None, repeat=None):
        self.original_tagname_ = None
        super(Schedule, self).__init__(id, extension, )
        if event is None:
            self.event = []
        else:
            self.event = event
        self.repeat = repeat
    def factory(*args_, **kwargs_):
        if Schedule.subclass:
            return Schedule.subclass(*args_, **kwargs_)
        else:
            return Schedule(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_event(self): return self.event
    def set_event(self, event): self.event = event
    def add_event(self, value): self.event.append(value)
    def insert_event(self, index, value): self.event[index] = value
    def get_repeat(self): return self.repeat
    def set_repeat(self, repeat): self.repeat = repeat
    def hasContent_(self):
        if (
            self.event or
            self.repeat is not None or
            super(Schedule, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Schedule', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Schedule')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Schedule', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Schedule'):
        super(Schedule, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Schedule')
    def exportChildren(self, outfile, level, namespace_='', name_='Schedule', fromsubclass_=False, pretty_print=True):
        super(Schedule, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for event_ in self.event:
            event_.export(outfile, level, namespace_, name_='event', pretty_print=pretty_print)
        if self.repeat is not None:
            self.repeat.export(outfile, level, namespace_, name_='repeat', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Schedule', mapping_=None):
        element = super(Schedule, self).to_etree(parent_element, name_, mapping_)
        for event_ in self.event:
            event_.to_etree(element, name_='event', mapping_=mapping_)
        if self.repeat is not None:
            repeat_ = self.repeat
            repeat_.to_etree(element, name_='repeat', mapping_=mapping_)
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
        super(Schedule, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'event':
            obj_ = Period.factory()
            obj_.build(child_)
            self.event.append(obj_)
            obj_.original_tagname_ = 'event'
        elif nodeName_ == 'repeat':
            obj_ = Schedule_Repeat.factory()
            obj_.build(child_)
            self.repeat = obj_
            obj_.original_tagname_ = 'repeat'
        super(Schedule, self).buildChildren(child_, node, nodeName_, True)
# end class Schedule


class Schedule_Repeat(Element):
    """Specifies an event that may occur multiple times. Schedules are used
    for to reord when things are expected or requested to occur.If
    the element is present, it must have a value for at least one of
    the defined elements, an @id referenced from the Narrative, or
    extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, frequency=None, when=None, duration=None, units=None, count=None, end=None):
        self.original_tagname_ = None
        super(Schedule_Repeat, self).__init__(id, extension, )
        self.frequency = frequency
        self.when = when
        self.duration = duration
        self.units = units
        self.count = count
        self.end = end
    def factory(*args_, **kwargs_):
        if Schedule_Repeat.subclass:
            return Schedule_Repeat.subclass(*args_, **kwargs_)
        else:
            return Schedule_Repeat(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_frequency(self): return self.frequency
    def set_frequency(self, frequency): self.frequency = frequency
    def get_when(self): return self.when
    def set_when(self, when): self.when = when
    def get_duration(self): return self.duration
    def set_duration(self, duration): self.duration = duration
    def get_units(self): return self.units
    def set_units(self, units): self.units = units
    def get_count(self): return self.count
    def set_count(self, count): self.count = count
    def get_end(self): return self.end
    def set_end(self, end): self.end = end
    def hasContent_(self):
        if (
            self.frequency is not None or
            self.when is not None or
            self.duration is not None or
            self.units is not None or
            self.count is not None or
            self.end is not None or
            super(Schedule_Repeat, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Schedule.Repeat', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Schedule.Repeat')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Schedule.Repeat', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Schedule.Repeat'):
        super(Schedule_Repeat, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Schedule.Repeat')
    def exportChildren(self, outfile, level, namespace_='', name_='Schedule.Repeat', fromsubclass_=False, pretty_print=True):
        super(Schedule_Repeat, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.frequency is not None:
            self.frequency.export(outfile, level, namespace_, name_='frequency', pretty_print=pretty_print)
        if self.when is not None:
            self.when.export(outfile, level, namespace_, name_='when', pretty_print=pretty_print)
        if self.duration is not None:
            self.duration.export(outfile, level, namespace_, name_='duration', pretty_print=pretty_print)
        if self.units is not None:
            self.units.export(outfile, level, namespace_, name_='units', pretty_print=pretty_print)
        if self.count is not None:
            self.count.export(outfile, level, namespace_, name_='count', pretty_print=pretty_print)
        if self.end is not None:
            self.end.export(outfile, level, namespace_, name_='end', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Schedule.Repeat', mapping_=None):
        element = super(Schedule_Repeat, self).to_etree(parent_element, name_, mapping_)
        if self.frequency is not None:
            frequency_ = self.frequency
            frequency_.to_etree(element, name_='frequency', mapping_=mapping_)
        if self.when is not None:
            when_ = self.when
            when_.to_etree(element, name_='when', mapping_=mapping_)
        if self.duration is not None:
            duration_ = self.duration
            duration_.to_etree(element, name_='duration', mapping_=mapping_)
        if self.units is not None:
            units_ = self.units
            units_.to_etree(element, name_='units', mapping_=mapping_)
        if self.count is not None:
            count_ = self.count
            count_.to_etree(element, name_='count', mapping_=mapping_)
        if self.end is not None:
            end_ = self.end
            end_.to_etree(element, name_='end', mapping_=mapping_)
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
        super(Schedule_Repeat, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'frequency':
            obj_ = integer.factory()
            obj_.build(child_)
            self.frequency = obj_
            obj_.original_tagname_ = 'frequency'
        elif nodeName_ == 'when':
            obj_ = EventTiming.factory()
            obj_.build(child_)
            self.when = obj_
            obj_.original_tagname_ = 'when'
        elif nodeName_ == 'duration':
            obj_ = decimal.factory()
            obj_.build(child_)
            self.duration = obj_
            obj_.original_tagname_ = 'duration'
        elif nodeName_ == 'units':
            obj_ = UnitsOfTime.factory()
            obj_.build(child_)
            self.units = obj_
            obj_.original_tagname_ = 'units'
        elif nodeName_ == 'count':
            obj_ = integer.factory()
            obj_.build(child_)
            self.count = obj_
            obj_.original_tagname_ = 'count'
        elif nodeName_ == 'end':
            obj_ = dateTime.factory()
            obj_.build(child_)
            self.end = obj_
            obj_.original_tagname_ = 'end'
        super(Schedule_Repeat, self).buildChildren(child_, node, nodeName_, True)
# end class Schedule_Repeat


class EventTiming(Element):
    """Real world event that the schedule relates toIf the element is
    present, it must have either a @value, an @id, or extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(EventTiming, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if EventTiming.subclass:
            return EventTiming.subclass(*args_, **kwargs_)
        else:
            return EventTiming(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(EventTiming, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='EventTiming', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='EventTiming')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='EventTiming', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='EventTiming'):
        super(EventTiming, self).exportAttributes(outfile, level, already_processed, namespace_, name_='EventTiming')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='EventTiming', fromsubclass_=False, pretty_print=True):
        super(EventTiming, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='EventTiming', mapping_=None):
        element = super(EventTiming, self).to_etree(parent_element, name_, mapping_)
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
        super(EventTiming, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(EventTiming, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class EventTiming


class UnitsOfTime(Element):
    """A unit of time (units from UCUM)If the element is present, it must
    have either a @value, an @id, or extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(UnitsOfTime, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if UnitsOfTime.subclass:
            return UnitsOfTime.subclass(*args_, **kwargs_)
        else:
            return UnitsOfTime(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(UnitsOfTime, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='UnitsOfTime', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='UnitsOfTime')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='UnitsOfTime', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='UnitsOfTime'):
        super(UnitsOfTime, self).exportAttributes(outfile, level, already_processed, namespace_, name_='UnitsOfTime')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='UnitsOfTime', fromsubclass_=False, pretty_print=True):
        super(UnitsOfTime, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='UnitsOfTime', mapping_=None):
        element = super(UnitsOfTime, self).to_etree(parent_element, name_, mapping_)
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
        super(UnitsOfTime, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(UnitsOfTime, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class UnitsOfTime


class Period(Element):
    """A time period defined by a start and end date and optionally time.If
    the element is present, it must have a value for at least one of
    the defined elements, an @id referenced from the Narrative, or
    extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, start=None, end=None):
        self.original_tagname_ = None
        super(Period, self).__init__(id, extension, )
        self.start = start
        self.end = end
    def factory(*args_, **kwargs_):
        if Period.subclass:
            return Period.subclass(*args_, **kwargs_)
        else:
            return Period(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_start(self): return self.start
    def set_start(self, start): self.start = start
    def get_end(self): return self.end
    def set_end(self, end): self.end = end
    def hasContent_(self):
        if (
            self.start is not None or
            self.end is not None or
            super(Period, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Period', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Period')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Period', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Period'):
        super(Period, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Period')
    def exportChildren(self, outfile, level, namespace_='', name_='Period', fromsubclass_=False, pretty_print=True):
        super(Period, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.start is not None:
            self.start.export(outfile, level, namespace_, name_='start', pretty_print=pretty_print)
        if self.end is not None:
            self.end.export(outfile, level, namespace_, name_='end', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Period', mapping_=None):
        element = super(Period, self).to_etree(parent_element, name_, mapping_)
        if self.start is not None:
            start_ = self.start
            start_.to_etree(element, name_='start', mapping_=mapping_)
        if self.end is not None:
            end_ = self.end
            end_.to_etree(element, name_='end', mapping_=mapping_)
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
        super(Period, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'start':
            obj_ = dateTime.factory()
            obj_.build(child_)
            self.start = obj_
            obj_.original_tagname_ = 'start'
        elif nodeName_ == 'end':
            obj_ = dateTime.factory()
            obj_.build(child_)
            self.end = obj_
            obj_.original_tagname_ = 'end'
        super(Period, self).buildChildren(child_, node, nodeName_, True)
# end class Period


class Coding(Element):
    """A reference to a code defined by a terminology system.If the element
    is present, it must have a value for at least one of the defined
    elements, an @id referenced from the Narrative, or extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, system=None, version=None, code=None, display=None, primary=None, valueSet=None):
        self.original_tagname_ = None
        super(Coding, self).__init__(id, extension, )
        self.system = system
        self.version = version
        self.code = code
        self.display = display
        self.primary = primary
        self.valueSet = valueSet
    def factory(*args_, **kwargs_):
        if Coding.subclass:
            return Coding.subclass(*args_, **kwargs_)
        else:
            return Coding(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_system(self): return self.system
    def set_system(self, system): self.system = system
    def get_version(self): return self.version
    def set_version(self, version): self.version = version
    def get_code(self): return self.code
    def set_code(self, code): self.code = code
    def get_display(self): return self.display
    def set_display(self, display): self.display = display
    def get_primary(self): return self.primary
    def set_primary(self, primary): self.primary = primary
    def get_valueSet(self): return self.valueSet
    def set_valueSet(self, valueSet): self.valueSet = valueSet
    def hasContent_(self):
        if (
            self.system is not None or
            self.version is not None or
            self.code is not None or
            self.display is not None or
            self.primary is not None or
            self.valueSet is not None or
            super(Coding, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Coding', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Coding')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Coding', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Coding'):
        super(Coding, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Coding')
    def exportChildren(self, outfile, level, namespace_='', name_='Coding', fromsubclass_=False, pretty_print=True):
        super(Coding, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.system is not None:
            self.system.export(outfile, level, namespace_, name_='system', pretty_print=pretty_print)
        if self.version is not None:
            self.version.export(outfile, level, namespace_, name_='version', pretty_print=pretty_print)
        if self.code is not None:
            self.code.export(outfile, level, namespace_, name_='code', pretty_print=pretty_print)
        if self.display is not None:
            self.display.export(outfile, level, namespace_, name_='display', pretty_print=pretty_print)
        if self.primary is not None:
            self.primary.export(outfile, level, namespace_, name_='primary', pretty_print=pretty_print)
        if self.valueSet is not None:
            self.valueSet.export(outfile, level, namespace_, name_='valueSet', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Coding', mapping_=None):
        element = super(Coding, self).to_etree(parent_element, name_, mapping_)
        if self.system is not None:
            system_ = self.system
            system_.to_etree(element, name_='system', mapping_=mapping_)
        if self.version is not None:
            version_ = self.version
            version_.to_etree(element, name_='version', mapping_=mapping_)
        if self.code is not None:
            code_ = self.code
            code_.to_etree(element, name_='code', mapping_=mapping_)
        if self.display is not None:
            display_ = self.display
            display_.to_etree(element, name_='display', mapping_=mapping_)
        if self.primary is not None:
            primary_ = self.primary
            primary_.to_etree(element, name_='primary', mapping_=mapping_)
        if self.valueSet is not None:
            valueSet_ = self.valueSet
            valueSet_.to_etree(element, name_='valueSet', mapping_=mapping_)
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
        super(Coding, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'system':
            obj_ = uri.factory()
            obj_.build(child_)
            self.system = obj_
            obj_.original_tagname_ = 'system'
        elif nodeName_ == 'version':
            obj_ = string.factory()
            obj_.build(child_)
            self.version = obj_
            obj_.original_tagname_ = 'version'
        elif nodeName_ == 'code':
            obj_ = code.factory()
            obj_.build(child_)
            self.code = obj_
            obj_.original_tagname_ = 'code'
        elif nodeName_ == 'display':
            obj_ = string.factory()
            obj_.build(child_)
            self.display = obj_
            obj_.original_tagname_ = 'display'
        elif nodeName_ == 'primary':
            obj_ = boolean.factory()
            obj_.build(child_)
            self.primary = obj_
            obj_.original_tagname_ = 'primary'
        elif nodeName_ == 'valueSet':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.valueSet = obj_
            obj_.original_tagname_ = 'valueSet'
        super(Coding, self).buildChildren(child_, node, nodeName_, True)
# end class Coding


class Range(Element):
    """A set of ordered Quantities defined by a low and high limit.If the
    element is present, it must have a value for at least one of the
    defined elements, an @id referenced from the Narrative, or
    extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, low=None, high=None):
        self.original_tagname_ = None
        super(Range, self).__init__(id, extension, )
        self.low = low
        self.high = high
    def factory(*args_, **kwargs_):
        if Range.subclass:
            return Range.subclass(*args_, **kwargs_)
        else:
            return Range(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_low(self): return self.low
    def set_low(self, low): self.low = low
    def get_high(self): return self.high
    def set_high(self, high): self.high = high
    def hasContent_(self):
        if (
            self.low is not None or
            self.high is not None or
            super(Range, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Range', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Range')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Range', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Range'):
        super(Range, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Range')
    def exportChildren(self, outfile, level, namespace_='', name_='Range', fromsubclass_=False, pretty_print=True):
        super(Range, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.low is not None:
            self.low.export(outfile, level, namespace_, name_='low', pretty_print=pretty_print)
        if self.high is not None:
            self.high.export(outfile, level, namespace_, name_='high', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Range', mapping_=None):
        element = super(Range, self).to_etree(parent_element, name_, mapping_)
        if self.low is not None:
            low_ = self.low
            low_.to_etree(element, name_='low', mapping_=mapping_)
        if self.high is not None:
            high_ = self.high
            high_.to_etree(element, name_='high', mapping_=mapping_)
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
        super(Range, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'low':
            obj_ = Quantity.factory()
            obj_.build(child_)
            self.low = obj_
            obj_.original_tagname_ = 'low'
        elif nodeName_ == 'high':
            obj_ = Quantity.factory()
            obj_.build(child_)
            self.high = obj_
            obj_.original_tagname_ = 'high'
        super(Range, self).buildChildren(child_, node, nodeName_, True)
# end class Range


class Quantity(Element):
    """A measured amount (or an amount that can potentially be measured).
    Note that measured amounts include amounts that are not
    precisely quantified, including amounts involving arbitrary
    units and floating currencies.If the element is present, it must
    have a value for at least one of the defined elements, an @id
    referenced from the Narrative, or extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None, comparator=None, units=None, system=None, code=None):
        self.original_tagname_ = None
        super(Quantity, self).__init__(id, extension, )
        self.value = value
        self.comparator = comparator
        self.units = units
        self.system = system
        self.code = code
    def factory(*args_, **kwargs_):
        if Quantity.subclass:
            return Quantity.subclass(*args_, **kwargs_)
        else:
            return Quantity(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def get_comparator(self): return self.comparator
    def set_comparator(self, comparator): self.comparator = comparator
    def get_units(self): return self.units
    def set_units(self, units): self.units = units
    def get_system(self): return self.system
    def set_system(self, system): self.system = system
    def get_code(self): return self.code
    def set_code(self, code): self.code = code
    def hasContent_(self):
        if (
            self.value is not None or
            self.comparator is not None or
            self.units is not None or
            self.system is not None or
            self.code is not None or
            super(Quantity, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Quantity', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Quantity')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Quantity', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Quantity'):
        super(Quantity, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Quantity')
    def exportChildren(self, outfile, level, namespace_='', name_='Quantity', fromsubclass_=False, pretty_print=True):
        super(Quantity, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.value is not None:
            self.value.export(outfile, level, namespace_, name_='value', pretty_print=pretty_print)
        if self.comparator is not None:
            self.comparator.export(outfile, level, namespace_, name_='comparator', pretty_print=pretty_print)
        if self.units is not None:
            self.units.export(outfile, level, namespace_, name_='units', pretty_print=pretty_print)
        if self.system is not None:
            self.system.export(outfile, level, namespace_, name_='system', pretty_print=pretty_print)
        if self.code is not None:
            self.code.export(outfile, level, namespace_, name_='code', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Quantity', mapping_=None):
        element = super(Quantity, self).to_etree(parent_element, name_, mapping_)
        if self.value is not None:
            value_ = self.value
            value_.to_etree(element, name_='value', mapping_=mapping_)
        if self.comparator is not None:
            comparator_ = self.comparator
            comparator_.to_etree(element, name_='comparator', mapping_=mapping_)
        if self.units is not None:
            units_ = self.units
            units_.to_etree(element, name_='units', mapping_=mapping_)
        if self.system is not None:
            system_ = self.system
            system_.to_etree(element, name_='system', mapping_=mapping_)
        if self.code is not None:
            code_ = self.code
            code_.to_etree(element, name_='code', mapping_=mapping_)
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
        super(Quantity, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'value':
            obj_ = decimal.factory()
            obj_.build(child_)
            self.value = obj_
            obj_.original_tagname_ = 'value'
        elif nodeName_ == 'comparator':
            obj_ = QuantityCompararator.factory()
            obj_.build(child_)
            self.comparator = obj_
            obj_.original_tagname_ = 'comparator'
        elif nodeName_ == 'units':
            obj_ = string.factory()
            obj_.build(child_)
            self.units = obj_
            obj_.original_tagname_ = 'units'
        elif nodeName_ == 'system':
            obj_ = uri.factory()
            obj_.build(child_)
            self.system = obj_
            obj_.original_tagname_ = 'system'
        elif nodeName_ == 'code':
            obj_ = code.factory()
            obj_.build(child_)
            self.code = obj_
            obj_.original_tagname_ = 'code'
        super(Quantity, self).buildChildren(child_, node, nodeName_, True)
# end class Quantity


class QuantityCompararator(Element):
    """How the Quantity should be understood and representedIf the element
    is present, it must have either a @value, an @id, or extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(QuantityCompararator, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if QuantityCompararator.subclass:
            return QuantityCompararator.subclass(*args_, **kwargs_)
        else:
            return QuantityCompararator(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(QuantityCompararator, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='QuantityCompararator', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='QuantityCompararator')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='QuantityCompararator', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='QuantityCompararator'):
        super(QuantityCompararator, self).exportAttributes(outfile, level, already_processed, namespace_, name_='QuantityCompararator')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='QuantityCompararator', fromsubclass_=False, pretty_print=True):
        super(QuantityCompararator, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='QuantityCompararator', mapping_=None):
        element = super(QuantityCompararator, self).to_etree(parent_element, name_, mapping_)
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
        super(QuantityCompararator, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(QuantityCompararator, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class QuantityCompararator


class Age(Quantity):
    subclass = None
    superclass = Quantity
    def __init__(self, id=None, extension=None, value=None, comparator=None, units=None, system=None, code=None):
        self.original_tagname_ = None
        super(Age, self).__init__(id, extension, value, comparator, units, system, code, )
        self.id = _cast(None, id)
        self.value = value
        self.comparator = comparator
        self.units = units
        self.system = system
        self.code = code
    def factory(*args_, **kwargs_):
        if Age.subclass:
            return Age.subclass(*args_, **kwargs_)
        else:
            return Age(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def get_comparator(self): return self.comparator
    def set_comparator(self, comparator): self.comparator = comparator
    def get_units(self): return self.units
    def set_units(self, units): self.units = units
    def get_system(self): return self.system
    def set_system(self, system): self.system = system
    def get_code(self): return self.code
    def set_code(self, code): self.code = code
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def hasContent_(self):
        if (
            self.value is not None or
            self.comparator is not None or
            self.units is not None or
            self.system is not None or
            self.code is not None or
            super(Age, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Age', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Age')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Age', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Age'):
        super(Age, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Age')
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (quote_attrib(self.id), ))
    def exportChildren(self, outfile, level, namespace_='', name_='Age', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.value is not None:
            self.value.export(outfile, level, namespace_, name_='value', pretty_print=pretty_print)
        if self.comparator is not None:
            self.comparator.export(outfile, level, namespace_, name_='comparator', pretty_print=pretty_print)
        if self.units is not None:
            self.units.export(outfile, level, namespace_, name_='units', pretty_print=pretty_print)
        if self.system is not None:
            self.system.export(outfile, level, namespace_, name_='system', pretty_print=pretty_print)
        if self.code is not None:
            self.code.export(outfile, level, namespace_, name_='code', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Age', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://hl7.org/fhir}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://hl7.org/fhir}' + name_)
        if self.id is not None:
            element.set('id', self.id)
        if self.value is not None:
            value_ = self.value
            value_.to_etree(element, name_='value', mapping_=mapping_)
        if self.comparator is not None:
            comparator_ = self.comparator
            comparator_.to_etree(element, name_='comparator', mapping_=mapping_)
        if self.units is not None:
            units_ = self.units
            units_.to_etree(element, name_='units', mapping_=mapping_)
        if self.system is not None:
            system_ = self.system
            system_.to_etree(element, name_='system', mapping_=mapping_)
        if self.code is not None:
            code_ = self.code
            code_.to_etree(element, name_='code', mapping_=mapping_)
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
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        super(Age, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'value':
            obj_ = decimal.factory()
            obj_.build(child_)
            self.value = obj_
            obj_.original_tagname_ = 'value'
        elif nodeName_ == 'comparator':
            obj_ = QuantityCompararator.factory()
            obj_.build(child_)
            self.comparator = obj_
            obj_.original_tagname_ = 'comparator'
        elif nodeName_ == 'units':
            obj_ = string.factory()
            obj_.build(child_)
            self.units = obj_
            obj_.original_tagname_ = 'units'
        elif nodeName_ == 'system':
            obj_ = uri.factory()
            obj_.build(child_)
            self.system = obj_
            obj_.original_tagname_ = 'system'
        elif nodeName_ == 'code':
            obj_ = code.factory()
            obj_.build(child_)
            self.code = obj_
            obj_.original_tagname_ = 'code'
# end class Age


class Count(Quantity):
    subclass = None
    superclass = Quantity
    def __init__(self, id=None, extension=None, value=None, comparator=None, units=None, system=None, code=None):
        self.original_tagname_ = None
        super(Count, self).__init__(id, extension, value, comparator, units, system, code, )
        self.id = _cast(None, id)
        self.value = value
        self.comparator = comparator
        self.units = units
        self.system = system
        self.code = code
    def factory(*args_, **kwargs_):
        if Count.subclass:
            return Count.subclass(*args_, **kwargs_)
        else:
            return Count(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def get_comparator(self): return self.comparator
    def set_comparator(self, comparator): self.comparator = comparator
    def get_units(self): return self.units
    def set_units(self, units): self.units = units
    def get_system(self): return self.system
    def set_system(self, system): self.system = system
    def get_code(self): return self.code
    def set_code(self, code): self.code = code
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def hasContent_(self):
        if (
            self.value is not None or
            self.comparator is not None or
            self.units is not None or
            self.system is not None or
            self.code is not None or
            super(Count, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Count', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Count')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Count', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Count'):
        super(Count, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Count')
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (quote_attrib(self.id), ))
    def exportChildren(self, outfile, level, namespace_='', name_='Count', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.value is not None:
            self.value.export(outfile, level, namespace_, name_='value', pretty_print=pretty_print)
        if self.comparator is not None:
            self.comparator.export(outfile, level, namespace_, name_='comparator', pretty_print=pretty_print)
        if self.units is not None:
            self.units.export(outfile, level, namespace_, name_='units', pretty_print=pretty_print)
        if self.system is not None:
            self.system.export(outfile, level, namespace_, name_='system', pretty_print=pretty_print)
        if self.code is not None:
            self.code.export(outfile, level, namespace_, name_='code', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Count', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://hl7.org/fhir}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://hl7.org/fhir}' + name_)
        if self.id is not None:
            element.set('id', self.id)
        if self.value is not None:
            value_ = self.value
            value_.to_etree(element, name_='value', mapping_=mapping_)
        if self.comparator is not None:
            comparator_ = self.comparator
            comparator_.to_etree(element, name_='comparator', mapping_=mapping_)
        if self.units is not None:
            units_ = self.units
            units_.to_etree(element, name_='units', mapping_=mapping_)
        if self.system is not None:
            system_ = self.system
            system_.to_etree(element, name_='system', mapping_=mapping_)
        if self.code is not None:
            code_ = self.code
            code_.to_etree(element, name_='code', mapping_=mapping_)
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
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        super(Count, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'value':
            obj_ = decimal.factory()
            obj_.build(child_)
            self.value = obj_
            obj_.original_tagname_ = 'value'
        elif nodeName_ == 'comparator':
            obj_ = QuantityCompararator.factory()
            obj_.build(child_)
            self.comparator = obj_
            obj_.original_tagname_ = 'comparator'
        elif nodeName_ == 'units':
            obj_ = string.factory()
            obj_.build(child_)
            self.units = obj_
            obj_.original_tagname_ = 'units'
        elif nodeName_ == 'system':
            obj_ = uri.factory()
            obj_.build(child_)
            self.system = obj_
            obj_.original_tagname_ = 'system'
        elif nodeName_ == 'code':
            obj_ = code.factory()
            obj_.build(child_)
            self.code = obj_
            obj_.original_tagname_ = 'code'
# end class Count


class Money(Quantity):
    subclass = None
    superclass = Quantity
    def __init__(self, id=None, extension=None, value=None, comparator=None, units=None, system=None, code=None):
        self.original_tagname_ = None
        super(Money, self).__init__(id, extension, value, comparator, units, system, code, )
        self.id = _cast(None, id)
        self.value = value
        self.comparator = comparator
        self.units = units
        self.system = system
        self.code = code
    def factory(*args_, **kwargs_):
        if Money.subclass:
            return Money.subclass(*args_, **kwargs_)
        else:
            return Money(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def get_comparator(self): return self.comparator
    def set_comparator(self, comparator): self.comparator = comparator
    def get_units(self): return self.units
    def set_units(self, units): self.units = units
    def get_system(self): return self.system
    def set_system(self, system): self.system = system
    def get_code(self): return self.code
    def set_code(self, code): self.code = code
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def hasContent_(self):
        if (
            self.value is not None or
            self.comparator is not None or
            self.units is not None or
            self.system is not None or
            self.code is not None or
            super(Money, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Money', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Money')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Money', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Money'):
        super(Money, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Money')
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (quote_attrib(self.id), ))
    def exportChildren(self, outfile, level, namespace_='', name_='Money', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.value is not None:
            self.value.export(outfile, level, namespace_, name_='value', pretty_print=pretty_print)
        if self.comparator is not None:
            self.comparator.export(outfile, level, namespace_, name_='comparator', pretty_print=pretty_print)
        if self.units is not None:
            self.units.export(outfile, level, namespace_, name_='units', pretty_print=pretty_print)
        if self.system is not None:
            self.system.export(outfile, level, namespace_, name_='system', pretty_print=pretty_print)
        if self.code is not None:
            self.code.export(outfile, level, namespace_, name_='code', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Money', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://hl7.org/fhir}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://hl7.org/fhir}' + name_)
        if self.id is not None:
            element.set('id', self.id)
        if self.value is not None:
            value_ = self.value
            value_.to_etree(element, name_='value', mapping_=mapping_)
        if self.comparator is not None:
            comparator_ = self.comparator
            comparator_.to_etree(element, name_='comparator', mapping_=mapping_)
        if self.units is not None:
            units_ = self.units
            units_.to_etree(element, name_='units', mapping_=mapping_)
        if self.system is not None:
            system_ = self.system
            system_.to_etree(element, name_='system', mapping_=mapping_)
        if self.code is not None:
            code_ = self.code
            code_.to_etree(element, name_='code', mapping_=mapping_)
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
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        super(Money, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'value':
            obj_ = decimal.factory()
            obj_.build(child_)
            self.value = obj_
            obj_.original_tagname_ = 'value'
        elif nodeName_ == 'comparator':
            obj_ = QuantityCompararator.factory()
            obj_.build(child_)
            self.comparator = obj_
            obj_.original_tagname_ = 'comparator'
        elif nodeName_ == 'units':
            obj_ = string.factory()
            obj_.build(child_)
            self.units = obj_
            obj_.original_tagname_ = 'units'
        elif nodeName_ == 'system':
            obj_ = uri.factory()
            obj_.build(child_)
            self.system = obj_
            obj_.original_tagname_ = 'system'
        elif nodeName_ == 'code':
            obj_ = code.factory()
            obj_.build(child_)
            self.code = obj_
            obj_.original_tagname_ = 'code'
# end class Money


class Distance(Quantity):
    subclass = None
    superclass = Quantity
    def __init__(self, id=None, extension=None, value=None, comparator=None, units=None, system=None, code=None):
        self.original_tagname_ = None
        super(Distance, self).__init__(id, extension, value, comparator, units, system, code, )
        self.id = _cast(None, id)
        self.value = value
        self.comparator = comparator
        self.units = units
        self.system = system
        self.code = code
    def factory(*args_, **kwargs_):
        if Distance.subclass:
            return Distance.subclass(*args_, **kwargs_)
        else:
            return Distance(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def get_comparator(self): return self.comparator
    def set_comparator(self, comparator): self.comparator = comparator
    def get_units(self): return self.units
    def set_units(self, units): self.units = units
    def get_system(self): return self.system
    def set_system(self, system): self.system = system
    def get_code(self): return self.code
    def set_code(self, code): self.code = code
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def hasContent_(self):
        if (
            self.value is not None or
            self.comparator is not None or
            self.units is not None or
            self.system is not None or
            self.code is not None or
            super(Distance, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Distance', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Distance')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Distance', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Distance'):
        super(Distance, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Distance')
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (quote_attrib(self.id), ))
    def exportChildren(self, outfile, level, namespace_='', name_='Distance', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.value is not None:
            self.value.export(outfile, level, namespace_, name_='value', pretty_print=pretty_print)
        if self.comparator is not None:
            self.comparator.export(outfile, level, namespace_, name_='comparator', pretty_print=pretty_print)
        if self.units is not None:
            self.units.export(outfile, level, namespace_, name_='units', pretty_print=pretty_print)
        if self.system is not None:
            self.system.export(outfile, level, namespace_, name_='system', pretty_print=pretty_print)
        if self.code is not None:
            self.code.export(outfile, level, namespace_, name_='code', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Distance', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://hl7.org/fhir}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://hl7.org/fhir}' + name_)
        if self.id is not None:
            element.set('id', self.id)
        if self.value is not None:
            value_ = self.value
            value_.to_etree(element, name_='value', mapping_=mapping_)
        if self.comparator is not None:
            comparator_ = self.comparator
            comparator_.to_etree(element, name_='comparator', mapping_=mapping_)
        if self.units is not None:
            units_ = self.units
            units_.to_etree(element, name_='units', mapping_=mapping_)
        if self.system is not None:
            system_ = self.system
            system_.to_etree(element, name_='system', mapping_=mapping_)
        if self.code is not None:
            code_ = self.code
            code_.to_etree(element, name_='code', mapping_=mapping_)
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
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        super(Distance, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'value':
            obj_ = decimal.factory()
            obj_.build(child_)
            self.value = obj_
            obj_.original_tagname_ = 'value'
        elif nodeName_ == 'comparator':
            obj_ = QuantityCompararator.factory()
            obj_.build(child_)
            self.comparator = obj_
            obj_.original_tagname_ = 'comparator'
        elif nodeName_ == 'units':
            obj_ = string.factory()
            obj_.build(child_)
            self.units = obj_
            obj_.original_tagname_ = 'units'
        elif nodeName_ == 'system':
            obj_ = uri.factory()
            obj_.build(child_)
            self.system = obj_
            obj_.original_tagname_ = 'system'
        elif nodeName_ == 'code':
            obj_ = code.factory()
            obj_.build(child_)
            self.code = obj_
            obj_.original_tagname_ = 'code'
# end class Distance


class Duration(Quantity):
    subclass = None
    superclass = Quantity
    def __init__(self, id=None, extension=None, value=None, comparator=None, units=None, system=None, code=None):
        self.original_tagname_ = None
        super(Duration, self).__init__(id, extension, value, comparator, units, system, code, )
        self.id = _cast(None, id)
        self.value = value
        self.comparator = comparator
        self.units = units
        self.system = system
        self.code = code
    def factory(*args_, **kwargs_):
        if Duration.subclass:
            return Duration.subclass(*args_, **kwargs_)
        else:
            return Duration(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def get_comparator(self): return self.comparator
    def set_comparator(self, comparator): self.comparator = comparator
    def get_units(self): return self.units
    def set_units(self, units): self.units = units
    def get_system(self): return self.system
    def set_system(self, system): self.system = system
    def get_code(self): return self.code
    def set_code(self, code): self.code = code
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def hasContent_(self):
        if (
            self.value is not None or
            self.comparator is not None or
            self.units is not None or
            self.system is not None or
            self.code is not None or
            super(Duration, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Duration', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Duration')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Duration', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Duration'):
        super(Duration, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Duration')
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (quote_attrib(self.id), ))
    def exportChildren(self, outfile, level, namespace_='', name_='Duration', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.value is not None:
            self.value.export(outfile, level, namespace_, name_='value', pretty_print=pretty_print)
        if self.comparator is not None:
            self.comparator.export(outfile, level, namespace_, name_='comparator', pretty_print=pretty_print)
        if self.units is not None:
            self.units.export(outfile, level, namespace_, name_='units', pretty_print=pretty_print)
        if self.system is not None:
            self.system.export(outfile, level, namespace_, name_='system', pretty_print=pretty_print)
        if self.code is not None:
            self.code.export(outfile, level, namespace_, name_='code', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Duration', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://hl7.org/fhir}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://hl7.org/fhir}' + name_)
        if self.id is not None:
            element.set('id', self.id)
        if self.value is not None:
            value_ = self.value
            value_.to_etree(element, name_='value', mapping_=mapping_)
        if self.comparator is not None:
            comparator_ = self.comparator
            comparator_.to_etree(element, name_='comparator', mapping_=mapping_)
        if self.units is not None:
            units_ = self.units
            units_.to_etree(element, name_='units', mapping_=mapping_)
        if self.system is not None:
            system_ = self.system
            system_.to_etree(element, name_='system', mapping_=mapping_)
        if self.code is not None:
            code_ = self.code
            code_.to_etree(element, name_='code', mapping_=mapping_)
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
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        super(Duration, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'value':
            obj_ = decimal.factory()
            obj_.build(child_)
            self.value = obj_
            obj_.original_tagname_ = 'value'
        elif nodeName_ == 'comparator':
            obj_ = QuantityCompararator.factory()
            obj_.build(child_)
            self.comparator = obj_
            obj_.original_tagname_ = 'comparator'
        elif nodeName_ == 'units':
            obj_ = string.factory()
            obj_.build(child_)
            self.units = obj_
            obj_.original_tagname_ = 'units'
        elif nodeName_ == 'system':
            obj_ = uri.factory()
            obj_.build(child_)
            self.system = obj_
            obj_.original_tagname_ = 'system'
        elif nodeName_ == 'code':
            obj_ = code.factory()
            obj_.build(child_)
            self.code = obj_
            obj_.original_tagname_ = 'code'
# end class Duration


class Attachment(Element):
    """For referring to data content defined in other formats.If the
    element is present, it must have a value for at least one of the
    defined elements, an @id referenced from the Narrative, or
    extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, contentType=None, language=None, data=None, url=None, size=None, hash=None, title=None):
        self.original_tagname_ = None
        super(Attachment, self).__init__(id, extension, )
        self.contentType = contentType
        self.language = language
        self.data = data
        self.url = url
        self.size = size
        self.hash = hash
        self.title = title
    def factory(*args_, **kwargs_):
        if Attachment.subclass:
            return Attachment.subclass(*args_, **kwargs_)
        else:
            return Attachment(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_contentType(self): return self.contentType
    def set_contentType(self, contentType): self.contentType = contentType
    def get_language(self): return self.language
    def set_language(self, language): self.language = language
    def get_data(self): return self.data
    def set_data(self, data): self.data = data
    def get_url(self): return self.url
    def set_url(self, url): self.url = url
    def get_size(self): return self.size
    def set_size(self, size): self.size = size
    def get_hash(self): return self.hash
    def set_hash(self, hash): self.hash = hash
    def get_title(self): return self.title
    def set_title(self, title): self.title = title
    def hasContent_(self):
        if (
            self.contentType is not None or
            self.language is not None or
            self.data is not None or
            self.url is not None or
            self.size is not None or
            self.hash is not None or
            self.title is not None or
            super(Attachment, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Attachment', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Attachment')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Attachment', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Attachment'):
        super(Attachment, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Attachment')
    def exportChildren(self, outfile, level, namespace_='', name_='Attachment', fromsubclass_=False, pretty_print=True):
        super(Attachment, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.contentType is not None:
            self.contentType.export(outfile, level, namespace_, name_='contentType', pretty_print=pretty_print)
        if self.language is not None:
            self.language.export(outfile, level, namespace_, name_='language', pretty_print=pretty_print)
        if self.data is not None:
            self.data.export(outfile, level, namespace_, name_='data', pretty_print=pretty_print)
        if self.url is not None:
            self.url.export(outfile, level, namespace_, name_='url', pretty_print=pretty_print)
        if self.size is not None:
            self.size.export(outfile, level, namespace_, name_='size', pretty_print=pretty_print)
        if self.hash is not None:
            self.hash.export(outfile, level, namespace_, name_='hash', pretty_print=pretty_print)
        if self.title is not None:
            self.title.export(outfile, level, namespace_, name_='title', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Attachment', mapping_=None):
        element = super(Attachment, self).to_etree(parent_element, name_, mapping_)
        if self.contentType is not None:
            contentType_ = self.contentType
            contentType_.to_etree(element, name_='contentType', mapping_=mapping_)
        if self.language is not None:
            language_ = self.language
            language_.to_etree(element, name_='language', mapping_=mapping_)
        if self.data is not None:
            data_ = self.data
            data_.to_etree(element, name_='data', mapping_=mapping_)
        if self.url is not None:
            url_ = self.url
            url_.to_etree(element, name_='url', mapping_=mapping_)
        if self.size is not None:
            size_ = self.size
            size_.to_etree(element, name_='size', mapping_=mapping_)
        if self.hash is not None:
            hash_ = self.hash
            hash_.to_etree(element, name_='hash', mapping_=mapping_)
        if self.title is not None:
            title_ = self.title
            title_.to_etree(element, name_='title', mapping_=mapping_)
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
        super(Attachment, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'contentType':
            obj_ = code.factory()
            obj_.build(child_)
            self.contentType = obj_
            obj_.original_tagname_ = 'contentType'
        elif nodeName_ == 'language':
            obj_ = code.factory()
            obj_.build(child_)
            self.language = obj_
            obj_.original_tagname_ = 'language'
        elif nodeName_ == 'data':
            obj_ = base64Binary.factory()
            obj_.build(child_)
            self.data = obj_
            obj_.original_tagname_ = 'data'
        elif nodeName_ == 'url':
            obj_ = uri.factory()
            obj_.build(child_)
            self.url = obj_
            obj_.original_tagname_ = 'url'
        elif nodeName_ == 'size':
            obj_ = integer.factory()
            obj_.build(child_)
            self.size = obj_
            obj_.original_tagname_ = 'size'
        elif nodeName_ == 'hash':
            obj_ = base64Binary.factory()
            obj_.build(child_)
            self.hash = obj_
            obj_.original_tagname_ = 'hash'
        elif nodeName_ == 'title':
            obj_ = string.factory()
            obj_.build(child_)
            self.title = obj_
            obj_.original_tagname_ = 'title'
        super(Attachment, self).buildChildren(child_, node, nodeName_, True)
# end class Attachment


class Ratio(Element):
    """A relationship of two Quantity values - expressed as a numerator and
    a denominator.If the element is present, it must have a value
    for at least one of the defined elements, an @id referenced from
    the Narrative, or extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, numerator=None, denominator=None):
        self.original_tagname_ = None
        super(Ratio, self).__init__(id, extension, )
        self.numerator = numerator
        self.denominator = denominator
    def factory(*args_, **kwargs_):
        if Ratio.subclass:
            return Ratio.subclass(*args_, **kwargs_)
        else:
            return Ratio(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_numerator(self): return self.numerator
    def set_numerator(self, numerator): self.numerator = numerator
    def get_denominator(self): return self.denominator
    def set_denominator(self, denominator): self.denominator = denominator
    def hasContent_(self):
        if (
            self.numerator is not None or
            self.denominator is not None or
            super(Ratio, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Ratio', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Ratio')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Ratio', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Ratio'):
        super(Ratio, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Ratio')
    def exportChildren(self, outfile, level, namespace_='', name_='Ratio', fromsubclass_=False, pretty_print=True):
        super(Ratio, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.numerator is not None:
            self.numerator.export(outfile, level, namespace_, name_='numerator', pretty_print=pretty_print)
        if self.denominator is not None:
            self.denominator.export(outfile, level, namespace_, name_='denominator', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Ratio', mapping_=None):
        element = super(Ratio, self).to_etree(parent_element, name_, mapping_)
        if self.numerator is not None:
            numerator_ = self.numerator
            numerator_.to_etree(element, name_='numerator', mapping_=mapping_)
        if self.denominator is not None:
            denominator_ = self.denominator
            denominator_.to_etree(element, name_='denominator', mapping_=mapping_)
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
        super(Ratio, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'numerator':
            obj_ = Quantity.factory()
            obj_.build(child_)
            self.numerator = obj_
            obj_.original_tagname_ = 'numerator'
        elif nodeName_ == 'denominator':
            obj_ = Quantity.factory()
            obj_.build(child_)
            self.denominator = obj_
            obj_.original_tagname_ = 'denominator'
        super(Ratio, self).buildChildren(child_, node, nodeName_, True)
# end class Ratio


class SampledData(Element):
    """A series of measurements taken by a device, with upper and lower
    limits. There may be more than one dimension in the data.If the
    element is present, it must have a value for at least one of the
    defined elements, an @id referenced from the Narrative, or
    extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, origin=None, period=None, factor=None, lowerLimit=None, upperLimit=None, dimensions=None, data=None):
        self.original_tagname_ = None
        super(SampledData, self).__init__(id, extension, )
        self.origin = origin
        self.period = period
        self.factor = factor
        self.lowerLimit = lowerLimit
        self.upperLimit = upperLimit
        self.dimensions = dimensions
        self.data = data
    def factory(*args_, **kwargs_):
        if SampledData.subclass:
            return SampledData.subclass(*args_, **kwargs_)
        else:
            return SampledData(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_origin(self): return self.origin
    def set_origin(self, origin): self.origin = origin
    def get_period(self): return self.period
    def set_period(self, period): self.period = period
    def get_factor(self): return self.factor
    def set_factor(self, factor): self.factor = factor
    def get_lowerLimit(self): return self.lowerLimit
    def set_lowerLimit(self, lowerLimit): self.lowerLimit = lowerLimit
    def get_upperLimit(self): return self.upperLimit
    def set_upperLimit(self, upperLimit): self.upperLimit = upperLimit
    def get_dimensions(self): return self.dimensions
    def set_dimensions(self, dimensions): self.dimensions = dimensions
    def get_data(self): return self.data
    def set_data(self, data): self.data = data
    def hasContent_(self):
        if (
            self.origin is not None or
            self.period is not None or
            self.factor is not None or
            self.lowerLimit is not None or
            self.upperLimit is not None or
            self.dimensions is not None or
            self.data is not None or
            super(SampledData, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='SampledData', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='SampledData')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='SampledData', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='SampledData'):
        super(SampledData, self).exportAttributes(outfile, level, already_processed, namespace_, name_='SampledData')
    def exportChildren(self, outfile, level, namespace_='', name_='SampledData', fromsubclass_=False, pretty_print=True):
        super(SampledData, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.origin is not None:
            self.origin.export(outfile, level, namespace_, name_='origin', pretty_print=pretty_print)
        if self.period is not None:
            self.period.export(outfile, level, namespace_, name_='period', pretty_print=pretty_print)
        if self.factor is not None:
            self.factor.export(outfile, level, namespace_, name_='factor', pretty_print=pretty_print)
        if self.lowerLimit is not None:
            self.lowerLimit.export(outfile, level, namespace_, name_='lowerLimit', pretty_print=pretty_print)
        if self.upperLimit is not None:
            self.upperLimit.export(outfile, level, namespace_, name_='upperLimit', pretty_print=pretty_print)
        if self.dimensions is not None:
            self.dimensions.export(outfile, level, namespace_, name_='dimensions', pretty_print=pretty_print)
        if self.data is not None:
            self.data.export(outfile, level, namespace_, name_='data', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='SampledData', mapping_=None):
        element = super(SampledData, self).to_etree(parent_element, name_, mapping_)
        if self.origin is not None:
            origin_ = self.origin
            origin_.to_etree(element, name_='origin', mapping_=mapping_)
        if self.period is not None:
            period_ = self.period
            period_.to_etree(element, name_='period', mapping_=mapping_)
        if self.factor is not None:
            factor_ = self.factor
            factor_.to_etree(element, name_='factor', mapping_=mapping_)
        if self.lowerLimit is not None:
            lowerLimit_ = self.lowerLimit
            lowerLimit_.to_etree(element, name_='lowerLimit', mapping_=mapping_)
        if self.upperLimit is not None:
            upperLimit_ = self.upperLimit
            upperLimit_.to_etree(element, name_='upperLimit', mapping_=mapping_)
        if self.dimensions is not None:
            dimensions_ = self.dimensions
            dimensions_.to_etree(element, name_='dimensions', mapping_=mapping_)
        if self.data is not None:
            data_ = self.data
            data_.to_etree(element, name_='data', mapping_=mapping_)
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
        super(SampledData, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'origin':
            obj_ = Quantity.factory()
            obj_.build(child_)
            self.origin = obj_
            obj_.original_tagname_ = 'origin'
        elif nodeName_ == 'period':
            obj_ = decimal.factory()
            obj_.build(child_)
            self.period = obj_
            obj_.original_tagname_ = 'period'
        elif nodeName_ == 'factor':
            obj_ = decimal.factory()
            obj_.build(child_)
            self.factor = obj_
            obj_.original_tagname_ = 'factor'
        elif nodeName_ == 'lowerLimit':
            obj_ = decimal.factory()
            obj_.build(child_)
            self.lowerLimit = obj_
            obj_.original_tagname_ = 'lowerLimit'
        elif nodeName_ == 'upperLimit':
            obj_ = decimal.factory()
            obj_.build(child_)
            self.upperLimit = obj_
            obj_.original_tagname_ = 'upperLimit'
        elif nodeName_ == 'dimensions':
            obj_ = integer.factory()
            obj_.build(child_)
            self.dimensions = obj_
            obj_.original_tagname_ = 'dimensions'
        elif nodeName_ == 'data':
            obj_ = SampledDataDataType.factory()
            obj_.build(child_)
            self.data = obj_
            obj_.original_tagname_ = 'data'
        super(SampledData, self).buildChildren(child_, node, nodeName_, True)
# end class SampledData


class SampledDataDataType(Element):
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(SampledDataDataType, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if SampledDataDataType.subclass:
            return SampledDataDataType.subclass(*args_, **kwargs_)
        else:
            return SampledDataDataType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(SampledDataDataType, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='SampledDataDataType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='SampledDataDataType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='SampledDataDataType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='SampledDataDataType'):
        super(SampledDataDataType, self).exportAttributes(outfile, level, already_processed, namespace_, name_='SampledDataDataType')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='SampledDataDataType', fromsubclass_=False, pretty_print=True):
        super(SampledDataDataType, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='SampledDataDataType', mapping_=None):
        element = super(SampledDataDataType, self).to_etree(parent_element, name_, mapping_)
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
        super(SampledDataDataType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(SampledDataDataType, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class SampledDataDataType
