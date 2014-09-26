from .base_classes import *
from .support_functions import *


class ConceptMap(Resource):
    """A statement of relationships from one set of concepts to one or more
    other concept systems.If the element is present, it must have
    either a @value, an @id, or extensions"""
    subclass = None
    superclass = Resource
    def __init__(self, id=None, extension=None, modifierExtension=None, language=None, text=None, contained=None, identifier=None, version=None, name=None, publisher=None, telecom=None, description=None, copyright=None, status=None, experimental=None, date=None, source=None, target=None, concept=None):
        self.original_tagname_ = None
        super(ConceptMap, self).__init__(id, extension, modifierExtension, language, text, contained, )
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
        self.date = date
        self.source = source
        self.target = target
        if concept is None:
            self.concept = []
        else:
            self.concept = concept
    def factory(*args_, **kwargs_):
        if ConceptMap.subclass:
            return ConceptMap.subclass(*args_, **kwargs_)
        else:
            return ConceptMap(*args_, **kwargs_)
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
    def get_date(self): return self.date
    def set_date(self, date): self.date = date
    def get_source(self): return self.source
    def set_source(self, source): self.source = source
    def get_target(self): return self.target
    def set_target(self, target): self.target = target
    def get_concept(self): return self.concept
    def set_concept(self, concept): self.concept = concept
    def add_concept(self, value): self.concept.append(value)
    def insert_concept(self, index, value): self.concept[index] = value
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
            self.date is not None or
            self.source is not None or
            self.target is not None or
            self.concept or
            super(ConceptMap, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='ConceptMap', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ConceptMap')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='ConceptMap', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='ConceptMap'):
        super(ConceptMap, self).exportAttributes(outfile, level, already_processed, namespace_, name_='ConceptMap')
    def exportChildren(self, outfile, level, namespace_='', name_='ConceptMap', fromsubclass_=False, pretty_print=True):
        super(ConceptMap, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
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
        if self.date is not None:
            self.date.export(outfile, level, namespace_, name_='date', pretty_print=pretty_print)
        if self.source is not None:
            self.source.export(outfile, level, namespace_, name_='source', pretty_print=pretty_print)
        if self.target is not None:
            self.target.export(outfile, level, namespace_, name_='target', pretty_print=pretty_print)
        for concept_ in self.concept:
            concept_.export(outfile, level, namespace_, name_='concept', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='ConceptMap', mapping_=None):
        element = super(ConceptMap, self).to_etree(parent_element, name_, mapping_)
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
        if self.date is not None:
            date_ = self.date
            date_.to_etree(element, name_='date', mapping_=mapping_)
        if self.source is not None:
            source_ = self.source
            source_.to_etree(element, name_='source', mapping_=mapping_)
        if self.target is not None:
            target_ = self.target
            target_.to_etree(element, name_='target', mapping_=mapping_)
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
        super(ConceptMap, self).buildAttributes(node, attrs, already_processed)
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
        elif nodeName_ == 'date':
            obj_ = dateTime.factory()
            obj_.build(child_)
            self.date = obj_
            obj_.original_tagname_ = 'date'
        elif nodeName_ == 'source':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.source = obj_
            obj_.original_tagname_ = 'source'
        elif nodeName_ == 'target':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.target = obj_
            obj_.original_tagname_ = 'target'
        elif nodeName_ == 'concept':
            obj_ = ConceptMap_Concept.factory()
            obj_.build(child_)
            self.concept.append(obj_)
            obj_.original_tagname_ = 'concept'
        super(ConceptMap, self).buildChildren(child_, node, nodeName_, True)
# end class ConceptMap


class ConceptMap_Concept(BackboneElement):
    """A statement of relationships from one set of concepts to one or more
    other concept systems."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, system=None, code=None, dependsOn=None, map=None):
        self.original_tagname_ = None
        super(ConceptMap_Concept, self).__init__(id, extension, modifierExtension, )
        self.system = system
        self.code = code
        if dependsOn is None:
            self.dependsOn = []
        else:
            self.dependsOn = dependsOn
        if map is None:
            self.map = []
        else:
            self.map = map
    def factory(*args_, **kwargs_):
        if ConceptMap_Concept.subclass:
            return ConceptMap_Concept.subclass(*args_, **kwargs_)
        else:
            return ConceptMap_Concept(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_system(self): return self.system
    def set_system(self, system): self.system = system
    def get_code(self): return self.code
    def set_code(self, code): self.code = code
    def get_dependsOn(self): return self.dependsOn
    def set_dependsOn(self, dependsOn): self.dependsOn = dependsOn
    def add_dependsOn(self, value): self.dependsOn.append(value)
    def insert_dependsOn(self, index, value): self.dependsOn[index] = value
    def get_map(self): return self.map
    def set_map(self, map): self.map = map
    def add_map(self, value): self.map.append(value)
    def insert_map(self, index, value): self.map[index] = value
    def hasContent_(self):
        if (
            self.system is not None or
            self.code is not None or
            self.dependsOn or
            self.map or
            super(ConceptMap_Concept, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='ConceptMap.Concept', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ConceptMap.Concept')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='ConceptMap.Concept', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='ConceptMap.Concept'):
        super(ConceptMap_Concept, self).exportAttributes(outfile, level, already_processed, namespace_, name_='ConceptMap.Concept')
    def exportChildren(self, outfile, level, namespace_='', name_='ConceptMap.Concept', fromsubclass_=False, pretty_print=True):
        super(ConceptMap_Concept, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.system is not None:
            self.system.export(outfile, level, namespace_, name_='system', pretty_print=pretty_print)
        if self.code is not None:
            self.code.export(outfile, level, namespace_, name_='code', pretty_print=pretty_print)
        for dependsOn_ in self.dependsOn:
            dependsOn_.export(outfile, level, namespace_, name_='dependsOn', pretty_print=pretty_print)
        for map_ in self.map:
            map_.export(outfile, level, namespace_, name_='map', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='ConceptMap.Concept', mapping_=None):
        element = super(ConceptMap_Concept, self).to_etree(parent_element, name_, mapping_)
        if self.system is not None:
            system_ = self.system
            system_.to_etree(element, name_='system', mapping_=mapping_)
        if self.code is not None:
            code_ = self.code
            code_.to_etree(element, name_='code', mapping_=mapping_)
        for dependsOn_ in self.dependsOn:
            dependsOn_.to_etree(element, name_='dependsOn', mapping_=mapping_)
        for map_ in self.map:
            map_.to_etree(element, name_='map', mapping_=mapping_)
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
        super(ConceptMap_Concept, self).buildAttributes(node, attrs, already_processed)
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
        elif nodeName_ == 'dependsOn':
            obj_ = ConceptMap_DependsOn.factory()
            obj_.build(child_)
            self.dependsOn.append(obj_)
            obj_.original_tagname_ = 'dependsOn'
        elif nodeName_ == 'map':
            obj_ = ConceptMap_Map.factory()
            obj_.build(child_)
            self.map.append(obj_)
            obj_.original_tagname_ = 'map'
        super(ConceptMap_Concept, self).buildChildren(child_, node, nodeName_, True)
# end class ConceptMap_Concept


class ConceptMap_DependsOn(BackboneElement):
    """A statement of relationships from one set of concepts to one or more
    other concept systems."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, concept=None, system=None, code=None):
        self.original_tagname_ = None
        super(ConceptMap_DependsOn, self).__init__(id, extension, modifierExtension, )
        self.concept = concept
        self.system = system
        self.code = code
    def factory(*args_, **kwargs_):
        if ConceptMap_DependsOn.subclass:
            return ConceptMap_DependsOn.subclass(*args_, **kwargs_)
        else:
            return ConceptMap_DependsOn(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_concept(self): return self.concept
    def set_concept(self, concept): self.concept = concept
    def get_system(self): return self.system
    def set_system(self, system): self.system = system
    def get_code(self): return self.code
    def set_code(self, code): self.code = code
    def hasContent_(self):
        if (
            self.concept is not None or
            self.system is not None or
            self.code is not None or
            super(ConceptMap_DependsOn, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='ConceptMap.DependsOn', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ConceptMap.DependsOn')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='ConceptMap.DependsOn', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='ConceptMap.DependsOn'):
        super(ConceptMap_DependsOn, self).exportAttributes(outfile, level, already_processed, namespace_, name_='ConceptMap.DependsOn')
    def exportChildren(self, outfile, level, namespace_='', name_='ConceptMap.DependsOn', fromsubclass_=False, pretty_print=True):
        super(ConceptMap_DependsOn, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.concept is not None:
            self.concept.export(outfile, level, namespace_, name_='concept', pretty_print=pretty_print)
        if self.system is not None:
            self.system.export(outfile, level, namespace_, name_='system', pretty_print=pretty_print)
        if self.code is not None:
            self.code.export(outfile, level, namespace_, name_='code', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='ConceptMap.DependsOn', mapping_=None):
        element = super(ConceptMap_DependsOn, self).to_etree(parent_element, name_, mapping_)
        if self.concept is not None:
            concept_ = self.concept
            concept_.to_etree(element, name_='concept', mapping_=mapping_)
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
        super(ConceptMap_DependsOn, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'concept':
            obj_ = uri.factory()
            obj_.build(child_)
            self.concept = obj_
            obj_.original_tagname_ = 'concept'
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
        super(ConceptMap_DependsOn, self).buildChildren(child_, node, nodeName_, True)
# end class ConceptMap_DependsOn


class ConceptMap_Map(BackboneElement):
    """A statement of relationships from one set of concepts to one or more
    other concept systems."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, system=None, code=None, equivalence=None, comments=None, product=None):
        self.original_tagname_ = None
        super(ConceptMap_Map, self).__init__(id, extension, modifierExtension, )
        self.system = system
        self.code = code
        self.equivalence = equivalence
        self.comments = comments
        if product is None:
            self.product = []
        else:
            self.product = product
    def factory(*args_, **kwargs_):
        if ConceptMap_Map.subclass:
            return ConceptMap_Map.subclass(*args_, **kwargs_)
        else:
            return ConceptMap_Map(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_system(self): return self.system
    def set_system(self, system): self.system = system
    def get_code(self): return self.code
    def set_code(self, code): self.code = code
    def get_equivalence(self): return self.equivalence
    def set_equivalence(self, equivalence): self.equivalence = equivalence
    def get_comments(self): return self.comments
    def set_comments(self, comments): self.comments = comments
    def get_product(self): return self.product
    def set_product(self, product): self.product = product
    def add_product(self, value): self.product.append(value)
    def insert_product(self, index, value): self.product[index] = value
    def hasContent_(self):
        if (
            self.system is not None or
            self.code is not None or
            self.equivalence is not None or
            self.comments is not None or
            self.product or
            super(ConceptMap_Map, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='ConceptMap.Map', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ConceptMap.Map')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='ConceptMap.Map', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='ConceptMap.Map'):
        super(ConceptMap_Map, self).exportAttributes(outfile, level, already_processed, namespace_, name_='ConceptMap.Map')
    def exportChildren(self, outfile, level, namespace_='', name_='ConceptMap.Map', fromsubclass_=False, pretty_print=True):
        super(ConceptMap_Map, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.system is not None:
            self.system.export(outfile, level, namespace_, name_='system', pretty_print=pretty_print)
        if self.code is not None:
            self.code.export(outfile, level, namespace_, name_='code', pretty_print=pretty_print)
        if self.equivalence is not None:
            self.equivalence.export(outfile, level, namespace_, name_='equivalence', pretty_print=pretty_print)
        if self.comments is not None:
            self.comments.export(outfile, level, namespace_, name_='comments', pretty_print=pretty_print)
        for product_ in self.product:
            product_.export(outfile, level, namespace_, name_='product', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='ConceptMap.Map', mapping_=None):
        element = super(ConceptMap_Map, self).to_etree(parent_element, name_, mapping_)
        if self.system is not None:
            system_ = self.system
            system_.to_etree(element, name_='system', mapping_=mapping_)
        if self.code is not None:
            code_ = self.code
            code_.to_etree(element, name_='code', mapping_=mapping_)
        if self.equivalence is not None:
            equivalence_ = self.equivalence
            equivalence_.to_etree(element, name_='equivalence', mapping_=mapping_)
        if self.comments is not None:
            comments_ = self.comments
            comments_.to_etree(element, name_='comments', mapping_=mapping_)
        for product_ in self.product:
            product_.to_etree(element, name_='product', mapping_=mapping_)
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
        super(ConceptMap_Map, self).buildAttributes(node, attrs, already_processed)
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
        elif nodeName_ == 'equivalence':
            obj_ = ConceptMapEquivalence.factory()
            obj_.build(child_)
            self.equivalence = obj_
            obj_.original_tagname_ = 'equivalence'
        elif nodeName_ == 'comments':
            obj_ = string.factory()
            obj_.build(child_)
            self.comments = obj_
            obj_.original_tagname_ = 'comments'
        elif nodeName_ == 'product':
            obj_ = ConceptMap_DependsOn.factory()
            obj_.build(child_)
            self.product.append(obj_)
            obj_.original_tagname_ = 'product'
        super(ConceptMap_Map, self).buildChildren(child_, node, nodeName_, True)
# end class ConceptMap_Map


class ConceptMapEquivalence(Element):
    """The degree of equivalence between conceptsIf the element is present,
    it must have either a @value, an @id, or extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(ConceptMapEquivalence, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if ConceptMapEquivalence.subclass:
            return ConceptMapEquivalence.subclass(*args_, **kwargs_)
        else:
            return ConceptMapEquivalence(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(ConceptMapEquivalence, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='ConceptMapEquivalence', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ConceptMapEquivalence')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='ConceptMapEquivalence', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='ConceptMapEquivalence'):
        super(ConceptMapEquivalence, self).exportAttributes(outfile, level, already_processed, namespace_, name_='ConceptMapEquivalence')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='ConceptMapEquivalence', fromsubclass_=False, pretty_print=True):
        super(ConceptMapEquivalence, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='ConceptMapEquivalence', mapping_=None):
        element = super(ConceptMapEquivalence, self).to_etree(parent_element, name_, mapping_)
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
        super(ConceptMapEquivalence, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(ConceptMapEquivalence, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class ConceptMapEquivalence


class ValueSetStatus(Element):
    """If the element is present, it must have either a @value, an @id, or
    extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(ValueSetStatus, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if ValueSetStatus.subclass:
            return ValueSetStatus.subclass(*args_, **kwargs_)
        else:
            return ValueSetStatus(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(ValueSetStatus, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='ValueSetStatus', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ValueSetStatus')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='ValueSetStatus', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='ValueSetStatus'):
        super(ValueSetStatus, self).exportAttributes(outfile, level, already_processed, namespace_, name_='ValueSetStatus')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='ValueSetStatus', fromsubclass_=False, pretty_print=True):
        super(ValueSetStatus, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='ValueSetStatus', mapping_=None):
        element = super(ValueSetStatus, self).to_etree(parent_element, name_, mapping_)
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
        super(ValueSetStatus, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(ValueSetStatus, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class ValueSetStatus
