from .base_classes import *
from .support_functions import *


class ValueSet(Resource):
    """A value set specifies a set of codes drawn from one or more code
    systems.If the element is present, it must have either a @value,
    an @id, or extensions"""
    subclass = None
    superclass = Resource
    def __init__(self, id=None, extension=None, modifierExtension=None, language=None, text=None, contained=None, identifier=None, version=None, name=None, publisher=None, telecom=None, description=None, copyright=None, status=None, experimental=None, extensible=None, date=None, define=None, compose=None, expansion=None):
        self.original_tagname_ = None
        super(ValueSet, self).__init__(id, extension, modifierExtension, language, text, contained, )
        self.identifier = identifier
        self.version = version
        self.name = name
        self.publisher = publisher
        if telecom is None:
            self.telecom = []
        else:
            self.telecom = telecom
        self.description = description
        self.copyright = copyright
        self.status = status
        self.experimental = experimental
        self.extensible = extensible
        self.date = date
        self.define = define
        self.compose = compose
        self.expansion = expansion
    def factory(*args_, **kwargs_):
        if ValueSet.subclass:
            return ValueSet.subclass(*args_, **kwargs_)
        else:
            return ValueSet(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_identifier(self): return self.identifier
    def set_identifier(self, identifier): self.identifier = identifier
    def get_version(self): return self.version
    def set_version(self, version): self.version = version
    def get_name(self): return self.name
    def set_name(self, name): self.name = name
    def get_publisher(self): return self.publisher
    def set_publisher(self, publisher): self.publisher = publisher
    def get_telecom(self): return self.telecom
    def set_telecom(self, telecom): self.telecom = telecom
    def add_telecom(self, value): self.telecom.append(value)
    def insert_telecom(self, index, value): self.telecom[index] = value
    def get_description(self): return self.description
    def set_description(self, description): self.description = description
    def get_copyright(self): return self.copyright
    def set_copyright(self, copyright): self.copyright = copyright
    def get_status(self): return self.status
    def set_status(self, status): self.status = status
    def get_experimental(self): return self.experimental
    def set_experimental(self, experimental): self.experimental = experimental
    def get_extensible(self): return self.extensible
    def set_extensible(self, extensible): self.extensible = extensible
    def get_date(self): return self.date
    def set_date(self, date): self.date = date
    def get_define(self): return self.define
    def set_define(self, define): self.define = define
    def get_compose(self): return self.compose
    def set_compose(self, compose): self.compose = compose
    def get_expansion(self): return self.expansion
    def set_expansion(self, expansion): self.expansion = expansion
    def hasContent_(self):
        if (
            self.identifier is not None or
            self.version is not None or
            self.name is not None or
            self.publisher is not None or
            self.telecom or
            self.description is not None or
            self.copyright is not None or
            self.status is not None or
            self.experimental is not None or
            self.extensible is not None or
            self.date is not None or
            self.define is not None or
            self.compose is not None or
            self.expansion is not None or
            super(ValueSet, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='ValueSet', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ValueSet')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='ValueSet', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='ValueSet'):
        super(ValueSet, self).exportAttributes(outfile, level, already_processed, namespace_, name_='ValueSet')
    def exportChildren(self, outfile, level, namespace_='', name_='ValueSet', fromsubclass_=False, pretty_print=True):
        super(ValueSet, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.identifier is not None:
            self.identifier.export(outfile, level, namespace_, name_='identifier', pretty_print=pretty_print)
        if self.version is not None:
            self.version.export(outfile, level, namespace_, name_='version', pretty_print=pretty_print)
        if self.name is not None:
            self.name.export(outfile, level, namespace_, name_='name', pretty_print=pretty_print)
        if self.publisher is not None:
            self.publisher.export(outfile, level, namespace_, name_='publisher', pretty_print=pretty_print)
        for telecom_ in self.telecom:
            telecom_.export(outfile, level, namespace_, name_='telecom', pretty_print=pretty_print)
        if self.description is not None:
            self.description.export(outfile, level, namespace_, name_='description', pretty_print=pretty_print)
        if self.copyright is not None:
            self.copyright.export(outfile, level, namespace_, name_='copyright', pretty_print=pretty_print)
        if self.status is not None:
            self.status.export(outfile, level, namespace_, name_='status', pretty_print=pretty_print)
        if self.experimental is not None:
            self.experimental.export(outfile, level, namespace_, name_='experimental', pretty_print=pretty_print)
        if self.extensible is not None:
            self.extensible.export(outfile, level, namespace_, name_='extensible', pretty_print=pretty_print)
        if self.date is not None:
            self.date.export(outfile, level, namespace_, name_='date', pretty_print=pretty_print)
        if self.define is not None:
            self.define.export(outfile, level, namespace_, name_='define', pretty_print=pretty_print)
        if self.compose is not None:
            self.compose.export(outfile, level, namespace_, name_='compose', pretty_print=pretty_print)
        if self.expansion is not None:
            self.expansion.export(outfile, level, namespace_, name_='expansion', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='ValueSet', mapping_=None):
        element = super(ValueSet, self).to_etree(parent_element, name_, mapping_)
        if self.identifier is not None:
            identifier_ = self.identifier
            identifier_.to_etree(element, name_='identifier', mapping_=mapping_)
        if self.version is not None:
            version_ = self.version
            version_.to_etree(element, name_='version', mapping_=mapping_)
        if self.name is not None:
            name_ = self.name
            name_.to_etree(element, name_='name', mapping_=mapping_)
        if self.publisher is not None:
            publisher_ = self.publisher
            publisher_.to_etree(element, name_='publisher', mapping_=mapping_)
        for telecom_ in self.telecom:
            telecom_.to_etree(element, name_='telecom', mapping_=mapping_)
        if self.description is not None:
            description_ = self.description
            description_.to_etree(element, name_='description', mapping_=mapping_)
        if self.copyright is not None:
            copyright_ = self.copyright
            copyright_.to_etree(element, name_='copyright', mapping_=mapping_)
        if self.status is not None:
            status_ = self.status
            status_.to_etree(element, name_='status', mapping_=mapping_)
        if self.experimental is not None:
            experimental_ = self.experimental
            experimental_.to_etree(element, name_='experimental', mapping_=mapping_)
        if self.extensible is not None:
            extensible_ = self.extensible
            extensible_.to_etree(element, name_='extensible', mapping_=mapping_)
        if self.date is not None:
            date_ = self.date
            date_.to_etree(element, name_='date', mapping_=mapping_)
        if self.define is not None:
            define_ = self.define
            define_.to_etree(element, name_='define', mapping_=mapping_)
        if self.compose is not None:
            compose_ = self.compose
            compose_.to_etree(element, name_='compose', mapping_=mapping_)
        if self.expansion is not None:
            expansion_ = self.expansion
            expansion_.to_etree(element, name_='expansion', mapping_=mapping_)
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
        super(ValueSet, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'identifier':
            obj_ = string.factory()
            obj_.build(child_)
            self.identifier = obj_
            obj_.original_tagname_ = 'identifier'
        elif nodeName_ == 'version':
            obj_ = string.factory()
            obj_.build(child_)
            self.version = obj_
            obj_.original_tagname_ = 'version'
        elif nodeName_ == 'name':
            obj_ = string.factory()
            obj_.build(child_)
            self.name = obj_
            obj_.original_tagname_ = 'name'
        elif nodeName_ == 'publisher':
            obj_ = string.factory()
            obj_.build(child_)
            self.publisher = obj_
            obj_.original_tagname_ = 'publisher'
        elif nodeName_ == 'telecom':
            obj_ = Contact.factory()
            obj_.build(child_)
            self.telecom.append(obj_)
            obj_.original_tagname_ = 'telecom'
        elif nodeName_ == 'description':
            obj_ = string.factory()
            obj_.build(child_)
            self.description = obj_
            obj_.original_tagname_ = 'description'
        elif nodeName_ == 'copyright':
            obj_ = string.factory()
            obj_.build(child_)
            self.copyright = obj_
            obj_.original_tagname_ = 'copyright'
        elif nodeName_ == 'status':
            obj_ = ValueSetStatus.factory()
            obj_.build(child_)
            self.status = obj_
            obj_.original_tagname_ = 'status'
        elif nodeName_ == 'experimental':
            obj_ = boolean.factory()
            obj_.build(child_)
            self.experimental = obj_
            obj_.original_tagname_ = 'experimental'
        elif nodeName_ == 'extensible':
            obj_ = boolean.factory()
            obj_.build(child_)
            self.extensible = obj_
            obj_.original_tagname_ = 'extensible'
        elif nodeName_ == 'date':
            obj_ = dateTime.factory()
            obj_.build(child_)
            self.date = obj_
            obj_.original_tagname_ = 'date'
        elif nodeName_ == 'define':
            obj_ = ValueSet_Define.factory()
            obj_.build(child_)
            self.define = obj_
            obj_.original_tagname_ = 'define'
        elif nodeName_ == 'compose':
            obj_ = ValueSet_Compose.factory()
            obj_.build(child_)
            self.compose = obj_
            obj_.original_tagname_ = 'compose'
        elif nodeName_ == 'expansion':
            obj_ = ValueSet_Expansion.factory()
            obj_.build(child_)
            self.expansion = obj_
            obj_.original_tagname_ = 'expansion'
        super(ValueSet, self).buildChildren(child_, node, nodeName_, True)
# end class ValueSet


class ValueSet_Define(BackboneElement):
    """A value set specifies a set of codes drawn from one or more code
    systems."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, system=None, version=None, caseSensitive=None, concept=None):
        self.original_tagname_ = None
        super(ValueSet_Define, self).__init__(id, extension, modifierExtension, )
        self.system = system
        self.version = version
        self.caseSensitive = caseSensitive
        if concept is None:
            self.concept = []
        else:
            self.concept = concept
    def factory(*args_, **kwargs_):
        if ValueSet_Define.subclass:
            return ValueSet_Define.subclass(*args_, **kwargs_)
        else:
            return ValueSet_Define(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_system(self): return self.system
    def set_system(self, system): self.system = system
    def get_version(self): return self.version
    def set_version(self, version): self.version = version
    def get_caseSensitive(self): return self.caseSensitive
    def set_caseSensitive(self, caseSensitive): self.caseSensitive = caseSensitive
    def get_concept(self): return self.concept
    def set_concept(self, concept): self.concept = concept
    def add_concept(self, value): self.concept.append(value)
    def insert_concept(self, index, value): self.concept[index] = value
    def hasContent_(self):
        if (
            self.system is not None or
            self.version is not None or
            self.caseSensitive is not None or
            self.concept or
            super(ValueSet_Define, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='ValueSet.Define', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ValueSet.Define')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='ValueSet.Define', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='ValueSet.Define'):
        super(ValueSet_Define, self).exportAttributes(outfile, level, already_processed, namespace_, name_='ValueSet.Define')
    def exportChildren(self, outfile, level, namespace_='', name_='ValueSet.Define', fromsubclass_=False, pretty_print=True):
        super(ValueSet_Define, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.system is not None:
            self.system.export(outfile, level, namespace_, name_='system', pretty_print=pretty_print)
        if self.version is not None:
            self.version.export(outfile, level, namespace_, name_='version', pretty_print=pretty_print)
        if self.caseSensitive is not None:
            self.caseSensitive.export(outfile, level, namespace_, name_='caseSensitive', pretty_print=pretty_print)
        for concept_ in self.concept:
            concept_.export(outfile, level, namespace_, name_='concept', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='ValueSet.Define', mapping_=None):
        element = super(ValueSet_Define, self).to_etree(parent_element, name_, mapping_)
        if self.system is not None:
            system_ = self.system
            system_.to_etree(element, name_='system', mapping_=mapping_)
        if self.version is not None:
            version_ = self.version
            version_.to_etree(element, name_='version', mapping_=mapping_)
        if self.caseSensitive is not None:
            caseSensitive_ = self.caseSensitive
            caseSensitive_.to_etree(element, name_='caseSensitive', mapping_=mapping_)
        for concept_ in self.concept:
            concept_.to_etree(element, name_='concept', mapping_=mapping_)
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
        super(ValueSet_Define, self).buildAttributes(node, attrs, already_processed)
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
        elif nodeName_ == 'caseSensitive':
            obj_ = boolean.factory()
            obj_.build(child_)
            self.caseSensitive = obj_
            obj_.original_tagname_ = 'caseSensitive'
        elif nodeName_ == 'concept':
            obj_ = ValueSet_Concept.factory()
            obj_.build(child_)
            self.concept.append(obj_)
            obj_.original_tagname_ = 'concept'
        super(ValueSet_Define, self).buildChildren(child_, node, nodeName_, True)
# end class ValueSet_Define


class ValueSet_Concept(BackboneElement):
    """A value set specifies a set of codes drawn from one or more code
    systems."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, code=None, abstract=None, display=None, definition=None, concept=None):
        self.original_tagname_ = None
        super(ValueSet_Concept, self).__init__(id, extension, modifierExtension, )
        self.code = code
        self.abstract = abstract
        self.display = display
        self.definition = definition
        if concept is None:
            self.concept = []
        else:
            self.concept = concept
    def factory(*args_, **kwargs_):
        if ValueSet_Concept.subclass:
            return ValueSet_Concept.subclass(*args_, **kwargs_)
        else:
            return ValueSet_Concept(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_code(self): return self.code
    def set_code(self, code): self.code = code
    def get_abstract(self): return self.abstract
    def set_abstract(self, abstract): self.abstract = abstract
    def get_display(self): return self.display
    def set_display(self, display): self.display = display
    def get_definition(self): return self.definition
    def set_definition(self, definition): self.definition = definition
    def get_concept(self): return self.concept
    def set_concept(self, concept): self.concept = concept
    def add_concept(self, value): self.concept.append(value)
    def insert_concept(self, index, value): self.concept[index] = value
    def hasContent_(self):
        if (
            self.code is not None or
            self.abstract is not None or
            self.display is not None or
            self.definition is not None or
            self.concept or
            super(ValueSet_Concept, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='ValueSet.Concept', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ValueSet.Concept')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='ValueSet.Concept', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='ValueSet.Concept'):
        super(ValueSet_Concept, self).exportAttributes(outfile, level, already_processed, namespace_, name_='ValueSet.Concept')
    def exportChildren(self, outfile, level, namespace_='', name_='ValueSet.Concept', fromsubclass_=False, pretty_print=True):
        super(ValueSet_Concept, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.code is not None:
            self.code.export(outfile, level, namespace_, name_='code', pretty_print=pretty_print)
        if self.abstract is not None:
            self.abstract.export(outfile, level, namespace_, name_='abstract', pretty_print=pretty_print)
        if self.display is not None:
            self.display.export(outfile, level, namespace_, name_='display', pretty_print=pretty_print)
        if self.definition is not None:
            self.definition.export(outfile, level, namespace_, name_='definition', pretty_print=pretty_print)
        for concept_ in self.concept:
            concept_.export(outfile, level, namespace_, name_='concept', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='ValueSet.Concept', mapping_=None):
        element = super(ValueSet_Concept, self).to_etree(parent_element, name_, mapping_)
        if self.code is not None:
            code_ = self.code
            code_.to_etree(element, name_='code', mapping_=mapping_)
        if self.abstract is not None:
            abstract_ = self.abstract
            abstract_.to_etree(element, name_='abstract', mapping_=mapping_)
        if self.display is not None:
            display_ = self.display
            display_.to_etree(element, name_='display', mapping_=mapping_)
        if self.definition is not None:
            definition_ = self.definition
            definition_.to_etree(element, name_='definition', mapping_=mapping_)
        for concept_ in self.concept:
            concept_.to_etree(element, name_='concept', mapping_=mapping_)
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
        super(ValueSet_Concept, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'code':
            obj_ = code.factory()
            obj_.build(child_)
            self.code = obj_
            obj_.original_tagname_ = 'code'
        elif nodeName_ == 'abstract':
            obj_ = boolean.factory()
            obj_.build(child_)
            self.abstract = obj_
            obj_.original_tagname_ = 'abstract'
        elif nodeName_ == 'display':
            obj_ = string.factory()
            obj_.build(child_)
            self.display = obj_
            obj_.original_tagname_ = 'display'
        elif nodeName_ == 'definition':
            obj_ = string.factory()
            obj_.build(child_)
            self.definition = obj_
            obj_.original_tagname_ = 'definition'
        elif nodeName_ == 'concept':
            obj_ = ValueSet_Concept.factory()
            obj_.build(child_)
            self.concept.append(obj_)
            obj_.original_tagname_ = 'concept'
        super(ValueSet_Concept, self).buildChildren(child_, node, nodeName_, True)
# end class ValueSet_Concept


class ValueSet_Compose(BackboneElement):
    """A value set specifies a set of codes drawn from one or more code
    systems."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, import_=None, include=None, exclude=None):
        self.original_tagname_ = None
        super(ValueSet_Compose, self).__init__(id, extension, modifierExtension, )
        if import_ is None:
            self.import_ = []
        else:
            self.import_ = import_
        if include is None:
            self.include = []
        else:
            self.include = include
        if exclude is None:
            self.exclude = []
        else:
            self.exclude = exclude
    def factory(*args_, **kwargs_):
        if ValueSet_Compose.subclass:
            return ValueSet_Compose.subclass(*args_, **kwargs_)
        else:
            return ValueSet_Compose(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_import(self): return self.import_
    def set_import(self, import_): self.import_ = import_
    def add_import(self, value): self.import_.append(value)
    def insert_import(self, index, value): self.import_[index] = value
    def get_include(self): return self.include
    def set_include(self, include): self.include = include
    def add_include(self, value): self.include.append(value)
    def insert_include(self, index, value): self.include[index] = value
    def get_exclude(self): return self.exclude
    def set_exclude(self, exclude): self.exclude = exclude
    def add_exclude(self, value): self.exclude.append(value)
    def insert_exclude(self, index, value): self.exclude[index] = value
    def hasContent_(self):
        if (
            self.import_ or
            self.include or
            self.exclude or
            super(ValueSet_Compose, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='ValueSet.Compose', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ValueSet.Compose')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='ValueSet.Compose', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='ValueSet.Compose'):
        super(ValueSet_Compose, self).exportAttributes(outfile, level, already_processed, namespace_, name_='ValueSet.Compose')
    def exportChildren(self, outfile, level, namespace_='', name_='ValueSet.Compose', fromsubclass_=False, pretty_print=True):
        super(ValueSet_Compose, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for import_ in self.import_:
            import_.export(outfile, level, namespace_, name_='import', pretty_print=pretty_print)
        for include_ in self.include:
            include_.export(outfile, level, namespace_, name_='include', pretty_print=pretty_print)
        for exclude_ in self.exclude:
            exclude_.export(outfile, level, namespace_, name_='exclude', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='ValueSet.Compose', mapping_=None):
        element = super(ValueSet_Compose, self).to_etree(parent_element, name_, mapping_)
        for import__ in self.import_:
            import__.to_etree(element, name_='import', mapping_=mapping_)
        for include_ in self.include:
            include_.to_etree(element, name_='include', mapping_=mapping_)
        for exclude_ in self.exclude:
            exclude_.to_etree(element, name_='exclude', mapping_=mapping_)
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
        super(ValueSet_Compose, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'import':
            obj_ = uri.factory()
            obj_.build(child_)
            self.import_.append(obj_)
            obj_.original_tagname_ = 'import'
        elif nodeName_ == 'include':
            obj_ = ValueSet_Include.factory()
            obj_.build(child_)
            self.include.append(obj_)
            obj_.original_tagname_ = 'include'
        elif nodeName_ == 'exclude':
            obj_ = ValueSet_Include.factory()
            obj_.build(child_)
            self.exclude.append(obj_)
            obj_.original_tagname_ = 'exclude'
        super(ValueSet_Compose, self).buildChildren(child_, node, nodeName_, True)
# end class ValueSet_Compose


class ValueSet_Include(BackboneElement):
    """A value set specifies a set of codes drawn from one or more code
    systems."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, system=None, version=None, code=None, filter=None):
        self.original_tagname_ = None
        super(ValueSet_Include, self).__init__(id, extension, modifierExtension, )
        self.system = system
        self.version = version
        if code is None:
            self.code = []
        else:
            self.code = code
        if filter is None:
            self.filter = []
        else:
            self.filter = filter
    def factory(*args_, **kwargs_):
        if ValueSet_Include.subclass:
            return ValueSet_Include.subclass(*args_, **kwargs_)
        else:
            return ValueSet_Include(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_system(self): return self.system
    def set_system(self, system): self.system = system
    def get_version(self): return self.version
    def set_version(self, version): self.version = version
    def get_code(self): return self.code
    def set_code(self, code): self.code = code
    def add_code(self, value): self.code.append(value)
    def insert_code(self, index, value): self.code[index] = value
    def get_filter(self): return self.filter
    def set_filter(self, filter): self.filter = filter
    def add_filter(self, value): self.filter.append(value)
    def insert_filter(self, index, value): self.filter[index] = value
    def hasContent_(self):
        if (
            self.system is not None or
            self.version is not None or
            self.code or
            self.filter or
            super(ValueSet_Include, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='ValueSet.Include', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ValueSet.Include')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='ValueSet.Include', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='ValueSet.Include'):
        super(ValueSet_Include, self).exportAttributes(outfile, level, already_processed, namespace_, name_='ValueSet.Include')
    def exportChildren(self, outfile, level, namespace_='', name_='ValueSet.Include', fromsubclass_=False, pretty_print=True):
        super(ValueSet_Include, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.system is not None:
            self.system.export(outfile, level, namespace_, name_='system', pretty_print=pretty_print)
        if self.version is not None:
            self.version.export(outfile, level, namespace_, name_='version', pretty_print=pretty_print)
        for code_ in self.code:
            code_.export(outfile, level, namespace_, name_='code', pretty_print=pretty_print)
        for filter_ in self.filter:
            filter_.export(outfile, level, namespace_, name_='filter', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='ValueSet.Include', mapping_=None):
        element = super(ValueSet_Include, self).to_etree(parent_element, name_, mapping_)
        if self.system is not None:
            system_ = self.system
            system_.to_etree(element, name_='system', mapping_=mapping_)
        if self.version is not None:
            version_ = self.version
            version_.to_etree(element, name_='version', mapping_=mapping_)
        for code_ in self.code:
            code_.to_etree(element, name_='code', mapping_=mapping_)
        for filter_ in self.filter:
            filter_.to_etree(element, name_='filter', mapping_=mapping_)
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
        super(ValueSet_Include, self).buildAttributes(node, attrs, already_processed)
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
            self.code.append(obj_)
            obj_.original_tagname_ = 'code'
        elif nodeName_ == 'filter':
            obj_ = ValueSet_Filter.factory()
            obj_.build(child_)
            self.filter.append(obj_)
            obj_.original_tagname_ = 'filter'
        super(ValueSet_Include, self).buildChildren(child_, node, nodeName_, True)
# end class ValueSet_Include


class ValueSet_Filter(BackboneElement):
    """A value set specifies a set of codes drawn from one or more code
    systems."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, property=None, op=None, value=None):
        self.original_tagname_ = None
        super(ValueSet_Filter, self).__init__(id, extension, modifierExtension, )
        self.property = property
        self.op = op
        self.value = value
    def factory(*args_, **kwargs_):
        if ValueSet_Filter.subclass:
            return ValueSet_Filter.subclass(*args_, **kwargs_)
        else:
            return ValueSet_Filter(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_property(self): return self.property
    def set_property(self, property): self.property = property
    def get_op(self): return self.op
    def set_op(self, op): self.op = op
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            self.property is not None or
            self.op is not None or
            self.value is not None or
            super(ValueSet_Filter, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='ValueSet.Filter', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ValueSet.Filter')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='ValueSet.Filter', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='ValueSet.Filter'):
        super(ValueSet_Filter, self).exportAttributes(outfile, level, already_processed, namespace_, name_='ValueSet.Filter')
    def exportChildren(self, outfile, level, namespace_='', name_='ValueSet.Filter', fromsubclass_=False, pretty_print=True):
        super(ValueSet_Filter, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.property is not None:
            self.property.export(outfile, level, namespace_, name_='property', pretty_print=pretty_print)
        if self.op is not None:
            self.op.export(outfile, level, namespace_, name_='op', pretty_print=pretty_print)
        if self.value is not None:
            self.value.export(outfile, level, namespace_, name_='value', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='ValueSet.Filter', mapping_=None):
        element = super(ValueSet_Filter, self).to_etree(parent_element, name_, mapping_)
        if self.property is not None:
            property_ = self.property
            property_.to_etree(element, name_='property', mapping_=mapping_)
        if self.op is not None:
            op_ = self.op
            op_.to_etree(element, name_='op', mapping_=mapping_)
        if self.value is not None:
            value_ = self.value
            value_.to_etree(element, name_='value', mapping_=mapping_)
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
        super(ValueSet_Filter, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'property':
            obj_ = code.factory()
            obj_.build(child_)
            self.property = obj_
            obj_.original_tagname_ = 'property'
        elif nodeName_ == 'op':
            obj_ = FilterOperator.factory()
            obj_.build(child_)
            self.op = obj_
            obj_.original_tagname_ = 'op'
        elif nodeName_ == 'value':
            obj_ = code.factory()
            obj_.build(child_)
            self.value = obj_
            obj_.original_tagname_ = 'value'
        super(ValueSet_Filter, self).buildChildren(child_, node, nodeName_, True)
# end class ValueSet_Filter


class ValueSet_Expansion(BackboneElement):
    """A value set specifies a set of codes drawn from one or more code
    systems."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, identifier=None, timestamp=None, contains=None):
        self.original_tagname_ = None
        super(ValueSet_Expansion, self).__init__(id, extension, modifierExtension, )
        self.identifier = identifier
        self.timestamp = timestamp
        if contains is None:
            self.contains = []
        else:
            self.contains = contains
    def factory(*args_, **kwargs_):
        if ValueSet_Expansion.subclass:
            return ValueSet_Expansion.subclass(*args_, **kwargs_)
        else:
            return ValueSet_Expansion(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_identifier(self): return self.identifier
    def set_identifier(self, identifier): self.identifier = identifier
    def get_timestamp(self): return self.timestamp
    def set_timestamp(self, timestamp): self.timestamp = timestamp
    def get_contains(self): return self.contains
    def set_contains(self, contains): self.contains = contains
    def add_contains(self, value): self.contains.append(value)
    def insert_contains(self, index, value): self.contains[index] = value
    def hasContent_(self):
        if (
            self.identifier is not None or
            self.timestamp is not None or
            self.contains or
            super(ValueSet_Expansion, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='ValueSet.Expansion', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ValueSet.Expansion')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='ValueSet.Expansion', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='ValueSet.Expansion'):
        super(ValueSet_Expansion, self).exportAttributes(outfile, level, already_processed, namespace_, name_='ValueSet.Expansion')
    def exportChildren(self, outfile, level, namespace_='', name_='ValueSet.Expansion', fromsubclass_=False, pretty_print=True):
        super(ValueSet_Expansion, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.identifier is not None:
            self.identifier.export(outfile, level, namespace_, name_='identifier', pretty_print=pretty_print)
        if self.timestamp is not None:
            self.timestamp.export(outfile, level, namespace_, name_='timestamp', pretty_print=pretty_print)
        for contains_ in self.contains:
            contains_.export(outfile, level, namespace_, name_='contains', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='ValueSet.Expansion', mapping_=None):
        element = super(ValueSet_Expansion, self).to_etree(parent_element, name_, mapping_)
        if self.identifier is not None:
            identifier_ = self.identifier
            identifier_.to_etree(element, name_='identifier', mapping_=mapping_)
        if self.timestamp is not None:
            timestamp_ = self.timestamp
            timestamp_.to_etree(element, name_='timestamp', mapping_=mapping_)
        for contains_ in self.contains:
            contains_.to_etree(element, name_='contains', mapping_=mapping_)
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
        super(ValueSet_Expansion, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'identifier':
            obj_ = Identifier.factory()
            obj_.build(child_)
            self.identifier = obj_
            obj_.original_tagname_ = 'identifier'
        elif nodeName_ == 'timestamp':
            obj_ = instant.factory()
            obj_.build(child_)
            self.timestamp = obj_
            obj_.original_tagname_ = 'timestamp'
        elif nodeName_ == 'contains':
            obj_ = ValueSet_Contains.factory()
            obj_.build(child_)
            self.contains.append(obj_)
            obj_.original_tagname_ = 'contains'
        super(ValueSet_Expansion, self).buildChildren(child_, node, nodeName_, True)
# end class ValueSet_Expansion


class ValueSet_Contains(BackboneElement):
    """A value set specifies a set of codes drawn from one or more code
    systems."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, system=None, code=None, display=None, contains=None):
        self.original_tagname_ = None
        super(ValueSet_Contains, self).__init__(id, extension, modifierExtension, )
        self.system = system
        self.code = code
        self.display = display
        if contains is None:
            self.contains = []
        else:
            self.contains = contains
    def factory(*args_, **kwargs_):
        if ValueSet_Contains.subclass:
            return ValueSet_Contains.subclass(*args_, **kwargs_)
        else:
            return ValueSet_Contains(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_system(self): return self.system
    def set_system(self, system): self.system = system
    def get_code(self): return self.code
    def set_code(self, code): self.code = code
    def get_display(self): return self.display
    def set_display(self, display): self.display = display
    def get_contains(self): return self.contains
    def set_contains(self, contains): self.contains = contains
    def add_contains(self, value): self.contains.append(value)
    def insert_contains(self, index, value): self.contains[index] = value
    def hasContent_(self):
        if (
            self.system is not None or
            self.code is not None or
            self.display is not None or
            self.contains or
            super(ValueSet_Contains, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='ValueSet.Contains', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ValueSet.Contains')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='ValueSet.Contains', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='ValueSet.Contains'):
        super(ValueSet_Contains, self).exportAttributes(outfile, level, already_processed, namespace_, name_='ValueSet.Contains')
    def exportChildren(self, outfile, level, namespace_='', name_='ValueSet.Contains', fromsubclass_=False, pretty_print=True):
        super(ValueSet_Contains, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.system is not None:
            self.system.export(outfile, level, namespace_, name_='system', pretty_print=pretty_print)
        if self.code is not None:
            self.code.export(outfile, level, namespace_, name_='code', pretty_print=pretty_print)
        if self.display is not None:
            self.display.export(outfile, level, namespace_, name_='display', pretty_print=pretty_print)
        for contains_ in self.contains:
            contains_.export(outfile, level, namespace_, name_='contains', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='ValueSet.Contains', mapping_=None):
        element = super(ValueSet_Contains, self).to_etree(parent_element, name_, mapping_)
        if self.system is not None:
            system_ = self.system
            system_.to_etree(element, name_='system', mapping_=mapping_)
        if self.code is not None:
            code_ = self.code
            code_.to_etree(element, name_='code', mapping_=mapping_)
        if self.display is not None:
            display_ = self.display
            display_.to_etree(element, name_='display', mapping_=mapping_)
        for contains_ in self.contains:
            contains_.to_etree(element, name_='contains', mapping_=mapping_)
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
        super(ValueSet_Contains, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'system':
            obj_ = uri.factory()
            obj_.build(child_)
            self.system = obj_
            obj_.original_tagname_ = 'system'
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
        elif nodeName_ == 'contains':
            obj_ = ValueSet_Contains.factory()
            obj_.build(child_)
            self.contains.append(obj_)
            obj_.original_tagname_ = 'contains'
        super(ValueSet_Contains, self).buildChildren(child_, node, nodeName_, True)
# end class ValueSet_Contains
