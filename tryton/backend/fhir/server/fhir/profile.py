from .base_classes import *
from .support_functions import *


class Profile(Resource):
    """A Resource Profile - a statement of use of one or more FHIR
    Resources. It may include constraints on Resources and Data
    Types, Terminology Binding Statements and Extension
    Definitions.If the element is present, it must have either a
    @value, an @id, or extensions"""
    subclass = None
    superclass = Resource
    def __init__(self, id=None, extension=None, modifierExtension=None, language=None, text=None, contained=None, identifier=None, version=None, name=None, publisher=None, telecom=None, description=None, code=None, status=None, experimental=None, date=None, requirements=None, fhirVersion=None, mapping=None, structure=None, extensionDefn=None, query=None):
        self.original_tagname_ = None
        super(Profile, self).__init__(id, extension, modifierExtension, language, text, contained, )
        self.identifier = identifier
        self.version = version
        self.name = name
        self.publisher = publisher
        if telecom is None:
            self.telecom = []
        else:
            self.telecom = telecom
        self.description = description
        if code is None:
            self.code = []
        else:
            self.code = code
        self.status = status
        self.experimental = experimental
        self.date = date
        self.requirements = requirements
        self.fhirVersion = fhirVersion
        if mapping is None:
            self.mapping = []
        else:
            self.mapping = mapping
        if structure is None:
            self.structure = []
        else:
            self.structure = structure
        if extensionDefn is None:
            self.extensionDefn = []
        else:
            self.extensionDefn = extensionDefn
        if query is None:
            self.query = []
        else:
            self.query = query
    def factory(*args_, **kwargs_):
        if Profile.subclass:
            return Profile.subclass(*args_, **kwargs_)
        else:
            return Profile(*args_, **kwargs_)
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
    def get_code(self): return self.code
    def set_code(self, code): self.code = code
    def add_code(self, value): self.code.append(value)
    def insert_code(self, index, value): self.code[index] = value
    def get_status(self): return self.status
    def set_status(self, status): self.status = status
    def get_experimental(self): return self.experimental
    def set_experimental(self, experimental): self.experimental = experimental
    def get_date(self): return self.date
    def set_date(self, date): self.date = date
    def get_requirements(self): return self.requirements
    def set_requirements(self, requirements): self.requirements = requirements
    def get_fhirVersion(self): return self.fhirVersion
    def set_fhirVersion(self, fhirVersion): self.fhirVersion = fhirVersion
    def get_mapping(self): return self.mapping
    def set_mapping(self, mapping): self.mapping = mapping
    def add_mapping(self, value): self.mapping.append(value)
    def insert_mapping(self, index, value): self.mapping[index] = value
    def get_structure(self): return self.structure
    def set_structure(self, structure): self.structure = structure
    def add_structure(self, value): self.structure.append(value)
    def insert_structure(self, index, value): self.structure[index] = value
    def get_extensionDefn(self): return self.extensionDefn
    def set_extensionDefn(self, extensionDefn): self.extensionDefn = extensionDefn
    def add_extensionDefn(self, value): self.extensionDefn.append(value)
    def insert_extensionDefn(self, index, value): self.extensionDefn[index] = value
    def get_query(self): return self.query
    def set_query(self, query): self.query = query
    def add_query(self, value): self.query.append(value)
    def insert_query(self, index, value): self.query[index] = value
    def hasContent_(self):
        if (
            self.identifier is not None or
            self.version is not None or
            self.name is not None or
            self.publisher is not None or
            self.telecom or
            self.description is not None or
            self.code or
            self.status is not None or
            self.experimental is not None or
            self.date is not None or
            self.requirements is not None or
            self.fhirVersion is not None or
            self.mapping or
            self.structure or
            self.extensionDefn or
            self.query or
            super(Profile, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Profile', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Profile')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Profile', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Profile'):
        super(Profile, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Profile')
    def exportChildren(self, outfile, level, namespace_='', name_='Profile', fromsubclass_=False, pretty_print=True):
        super(Profile, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
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
        for code_ in self.code:
            code_.export(outfile, level, namespace_, name_='code', pretty_print=pretty_print)
        if self.status is not None:
            self.status.export(outfile, level, namespace_, name_='status', pretty_print=pretty_print)
        if self.experimental is not None:
            self.experimental.export(outfile, level, namespace_, name_='experimental', pretty_print=pretty_print)
        if self.date is not None:
            self.date.export(outfile, level, namespace_, name_='date', pretty_print=pretty_print)
        if self.requirements is not None:
            self.requirements.export(outfile, level, namespace_, name_='requirements', pretty_print=pretty_print)
        if self.fhirVersion is not None:
            self.fhirVersion.export(outfile, level, namespace_, name_='fhirVersion', pretty_print=pretty_print)
        for mapping_ in self.mapping:
            mapping_.export(outfile, level, namespace_, name_='mapping', pretty_print=pretty_print)
        for structure_ in self.structure:
            structure_.export(outfile, level, namespace_, name_='structure', pretty_print=pretty_print)
        for extensionDefn_ in self.extensionDefn:
            extensionDefn_.export(outfile, level, namespace_, name_='extensionDefn', pretty_print=pretty_print)
        for query_ in self.query:
            query_.export(outfile, level, namespace_, name_='query', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Profile', mapping_=None):
        element = super(Profile, self).to_etree(parent_element, name_, mapping_)
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
        for code_ in self.code:
            code_.to_etree(element, name_='code', mapping_=mapping_)
        if self.status is not None:
            status_ = self.status
            status_.to_etree(element, name_='status', mapping_=mapping_)
        if self.experimental is not None:
            experimental_ = self.experimental
            experimental_.to_etree(element, name_='experimental', mapping_=mapping_)
        if self.date is not None:
            date_ = self.date
            date_.to_etree(element, name_='date', mapping_=mapping_)
        if self.requirements is not None:
            requirements_ = self.requirements
            requirements_.to_etree(element, name_='requirements', mapping_=mapping_)
        if self.fhirVersion is not None:
            fhirVersion_ = self.fhirVersion
            fhirVersion_.to_etree(element, name_='fhirVersion', mapping_=mapping_)
        for mapping_ in self.mapping:
            mapping_.to_etree(element, name_='mapping', mapping_=mapping_)
        for structure_ in self.structure:
            structure_.to_etree(element, name_='structure', mapping_=mapping_)
        for extensionDefn_ in self.extensionDefn:
            extensionDefn_.to_etree(element, name_='extensionDefn', mapping_=mapping_)
        for query_ in self.query:
            query_.to_etree(element, name_='query', mapping_=mapping_)
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
        super(Profile, self).buildAttributes(node, attrs, already_processed)
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
        elif nodeName_ == 'code':
            obj_ = Coding.factory()
            obj_.build(child_)
            self.code.append(obj_)
            obj_.original_tagname_ = 'code'
        elif nodeName_ == 'status':
            obj_ = ResourceProfileStatus.factory()
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
        elif nodeName_ == 'requirements':
            obj_ = string.factory()
            obj_.build(child_)
            self.requirements = obj_
            obj_.original_tagname_ = 'requirements'
        elif nodeName_ == 'fhirVersion':
            obj_ = id.factory()
            obj_.build(child_)
            self.fhirVersion = obj_
            obj_.original_tagname_ = 'fhirVersion'
        elif nodeName_ == 'mapping':
            obj_ = Profile_Mapping.factory()
            obj_.build(child_)
            self.mapping.append(obj_)
            obj_.original_tagname_ = 'mapping'
        elif nodeName_ == 'structure':
            obj_ = Profile_Structure.factory()
            obj_.build(child_)
            self.structure.append(obj_)
            obj_.original_tagname_ = 'structure'
        elif nodeName_ == 'extensionDefn':
            obj_ = Profile_ExtensionDefn.factory()
            obj_.build(child_)
            self.extensionDefn.append(obj_)
            obj_.original_tagname_ = 'extensionDefn'
        elif nodeName_ == 'query':
            obj_ = Profile_Query.factory()
            obj_.build(child_)
            self.query.append(obj_)
            obj_.original_tagname_ = 'query'
        super(Profile, self).buildChildren(child_, node, nodeName_, True)
# end class Profile


class Profile_Mapping(BackboneElement):
    """A Resource Profile - a statement of use of one or more FHIR
    Resources. It may include constraints on Resources and Data
    Types, Terminology Binding Statements and Extension Definitions."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, identity=None, uri=None, name=None, comments=None):
        self.original_tagname_ = None
        super(Profile_Mapping, self).__init__(id, extension, modifierExtension, )
        self.identity = identity
        self.uri = uri
        self.name = name
        self.comments = comments
    def factory(*args_, **kwargs_):
        if Profile_Mapping.subclass:
            return Profile_Mapping.subclass(*args_, **kwargs_)
        else:
            return Profile_Mapping(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_identity(self): return self.identity
    def set_identity(self, identity): self.identity = identity
    def get_uri(self): return self.uri
    def set_uri(self, uri): self.uri = uri
    def get_name(self): return self.name
    def set_name(self, name): self.name = name
    def get_comments(self): return self.comments
    def set_comments(self, comments): self.comments = comments
    def hasContent_(self):
        if (
            self.identity is not None or
            self.uri is not None or
            self.name is not None or
            self.comments is not None or
            super(Profile_Mapping, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Profile.Mapping', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Profile.Mapping')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Profile.Mapping', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Profile.Mapping'):
        super(Profile_Mapping, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Profile.Mapping')
    def exportChildren(self, outfile, level, namespace_='', name_='Profile.Mapping', fromsubclass_=False, pretty_print=True):
        super(Profile_Mapping, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.identity is not None:
            self.identity.export(outfile, level, namespace_, name_='identity', pretty_print=pretty_print)
        if self.uri is not None:
            self.uri.export(outfile, level, namespace_, name_='uri', pretty_print=pretty_print)
        if self.name is not None:
            self.name.export(outfile, level, namespace_, name_='name', pretty_print=pretty_print)
        if self.comments is not None:
            self.comments.export(outfile, level, namespace_, name_='comments', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Profile.Mapping', mapping_=None):
        element = super(Profile_Mapping, self).to_etree(parent_element, name_, mapping_)
        if self.identity is not None:
            identity_ = self.identity
            identity_.to_etree(element, name_='identity', mapping_=mapping_)
        if self.uri is not None:
            uri_ = self.uri
            uri_.to_etree(element, name_='uri', mapping_=mapping_)
        if self.name is not None:
            name_ = self.name
            name_.to_etree(element, name_='name', mapping_=mapping_)
        if self.comments is not None:
            comments_ = self.comments
            comments_.to_etree(element, name_='comments', mapping_=mapping_)
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
        super(Profile_Mapping, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'identity':
            obj_ = id.factory()
            obj_.build(child_)
            self.identity = obj_
            obj_.original_tagname_ = 'identity'
        elif nodeName_ == 'uri':
            obj_ = uri.factory()
            obj_.build(child_)
            self.uri = obj_
            obj_.original_tagname_ = 'uri'
        elif nodeName_ == 'name':
            obj_ = string.factory()
            obj_.build(child_)
            self.name = obj_
            obj_.original_tagname_ = 'name'
        elif nodeName_ == 'comments':
            obj_ = string.factory()
            obj_.build(child_)
            self.comments = obj_
            obj_.original_tagname_ = 'comments'
        super(Profile_Mapping, self).buildChildren(child_, node, nodeName_, True)
# end class Profile_Mapping


class Profile_Structure(BackboneElement):
    """A Resource Profile - a statement of use of one or more FHIR
    Resources. It may include constraints on Resources and Data
    Types, Terminology Binding Statements and Extension Definitions."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, type_=None, name=None, publish=None, purpose=None, element=None, searchParam=None):
        self.original_tagname_ = None
        super(Profile_Structure, self).__init__(id, extension, modifierExtension, )
        self.type_ = type_
        self.name = name
        self.publish = publish
        self.purpose = purpose
        if element is None:
            self.element = []
        else:
            self.element = element
        if searchParam is None:
            self.searchParam = []
        else:
            self.searchParam = searchParam
    def factory(*args_, **kwargs_):
        if Profile_Structure.subclass:
            return Profile_Structure.subclass(*args_, **kwargs_)
        else:
            return Profile_Structure(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_type(self): return self.type_
    def set_type(self, type_): self.type_ = type_
    def get_name(self): return self.name
    def set_name(self, name): self.name = name
    def get_publish(self): return self.publish
    def set_publish(self, publish): self.publish = publish
    def get_purpose(self): return self.purpose
    def set_purpose(self, purpose): self.purpose = purpose
    def get_element(self): return self.element
    def set_element(self, element): self.element = element
    def add_element(self, value): self.element.append(value)
    def insert_element(self, index, value): self.element[index] = value
    def get_searchParam(self): return self.searchParam
    def set_searchParam(self, searchParam): self.searchParam = searchParam
    def add_searchParam(self, value): self.searchParam.append(value)
    def insert_searchParam(self, index, value): self.searchParam[index] = value
    def hasContent_(self):
        if (
            self.type_ is not None or
            self.name is not None or
            self.publish is not None or
            self.purpose is not None or
            self.element or
            self.searchParam or
            super(Profile_Structure, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Profile.Structure', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Profile.Structure')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Profile.Structure', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Profile.Structure'):
        super(Profile_Structure, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Profile.Structure')
    def exportChildren(self, outfile, level, namespace_='', name_='Profile.Structure', fromsubclass_=False, pretty_print=True):
        super(Profile_Structure, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.type_ is not None:
            self.type_.export(outfile, level, namespace_, name_='type', pretty_print=pretty_print)
        if self.name is not None:
            self.name.export(outfile, level, namespace_, name_='name', pretty_print=pretty_print)
        if self.publish is not None:
            self.publish.export(outfile, level, namespace_, name_='publish', pretty_print=pretty_print)
        if self.purpose is not None:
            self.purpose.export(outfile, level, namespace_, name_='purpose', pretty_print=pretty_print)
        for element_ in self.element:
            element_.export(outfile, level, namespace_, name_='element', pretty_print=pretty_print)
        for searchParam_ in self.searchParam:
            searchParam_.export(outfile, level, namespace_, name_='searchParam', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Profile.Structure', mapping_=None):
        element = super(Profile_Structure, self).to_etree(parent_element, name_, mapping_)
        if self.type_ is not None:
            type__ = self.type_
            type__.to_etree(element, name_='type', mapping_=mapping_)
        if self.name is not None:
            name_ = self.name
            name_.to_etree(element, name_='name', mapping_=mapping_)
        if self.publish is not None:
            publish_ = self.publish
            publish_.to_etree(element, name_='publish', mapping_=mapping_)
        if self.purpose is not None:
            purpose_ = self.purpose
            purpose_.to_etree(element, name_='purpose', mapping_=mapping_)
        for element_ in self.element:
            element_.to_etree(element, name_='element', mapping_=mapping_)
        for searchParam_ in self.searchParam:
            searchParam_.to_etree(element, name_='searchParam', mapping_=mapping_)
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
        super(Profile_Structure, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'type':
            obj_ = code.factory()
            obj_.build(child_)
            self.type_ = obj_
            obj_.original_tagname_ = 'type'
        elif nodeName_ == 'name':
            obj_ = string.factory()
            obj_.build(child_)
            self.name = obj_
            obj_.original_tagname_ = 'name'
        elif nodeName_ == 'publish':
            obj_ = boolean.factory()
            obj_.build(child_)
            self.publish = obj_
            obj_.original_tagname_ = 'publish'
        elif nodeName_ == 'purpose':
            obj_ = string.factory()
            obj_.build(child_)
            self.purpose = obj_
            obj_.original_tagname_ = 'purpose'
        elif nodeName_ == 'element':
            obj_ = Profile_Element.factory()
            obj_.build(child_)
            self.element.append(obj_)
            obj_.original_tagname_ = 'element'
        elif nodeName_ == 'searchParam':
            obj_ = Profile_SearchParam.factory()
            obj_.build(child_)
            self.searchParam.append(obj_)
            obj_.original_tagname_ = 'searchParam'
        super(Profile_Structure, self).buildChildren(child_, node, nodeName_, True)
# end class Profile_Structure


class Profile_Element(BackboneElement):
    """A Resource Profile - a statement of use of one or more FHIR
    Resources. It may include constraints on Resources and Data
    Types, Terminology Binding Statements and Extension Definitions."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, path=None, representation=None, name=None, slicing=None, definition=None):
        self.original_tagname_ = None
        super(Profile_Element, self).__init__(id, extension, modifierExtension, )
        self.path = path
        if representation is None:
            self.representation = []
        else:
            self.representation = representation
        self.name = name
        self.slicing = slicing
        self.definition = definition
    def factory(*args_, **kwargs_):
        if Profile_Element.subclass:
            return Profile_Element.subclass(*args_, **kwargs_)
        else:
            return Profile_Element(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_path(self): return self.path
    def set_path(self, path): self.path = path
    def get_representation(self): return self.representation
    def set_representation(self, representation): self.representation = representation
    def add_representation(self, value): self.representation.append(value)
    def insert_representation(self, index, value): self.representation[index] = value
    def get_name(self): return self.name
    def set_name(self, name): self.name = name
    def get_slicing(self): return self.slicing
    def set_slicing(self, slicing): self.slicing = slicing
    def get_definition(self): return self.definition
    def set_definition(self, definition): self.definition = definition
    def hasContent_(self):
        if (
            self.path is not None or
            self.representation or
            self.name is not None or
            self.slicing is not None or
            self.definition is not None or
            super(Profile_Element, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Profile.Element', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Profile.Element')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Profile.Element', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Profile.Element'):
        super(Profile_Element, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Profile.Element')
    def exportChildren(self, outfile, level, namespace_='', name_='Profile.Element', fromsubclass_=False, pretty_print=True):
        super(Profile_Element, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.path is not None:
            self.path.export(outfile, level, namespace_, name_='path', pretty_print=pretty_print)
        for representation_ in self.representation:
            representation_.export(outfile, level, namespace_, name_='representation', pretty_print=pretty_print)
        if self.name is not None:
            self.name.export(outfile, level, namespace_, name_='name', pretty_print=pretty_print)
        if self.slicing is not None:
            self.slicing.export(outfile, level, namespace_, name_='slicing', pretty_print=pretty_print)
        if self.definition is not None:
            self.definition.export(outfile, level, namespace_, name_='definition', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Profile.Element', mapping_=None):
        element = super(Profile_Element, self).to_etree(parent_element, name_, mapping_)
        if self.path is not None:
            path_ = self.path
            path_.to_etree(element, name_='path', mapping_=mapping_)
        for representation_ in self.representation:
            representation_.to_etree(element, name_='representation', mapping_=mapping_)
        if self.name is not None:
            name_ = self.name
            name_.to_etree(element, name_='name', mapping_=mapping_)
        if self.slicing is not None:
            slicing_ = self.slicing
            slicing_.to_etree(element, name_='slicing', mapping_=mapping_)
        if self.definition is not None:
            definition_ = self.definition
            definition_.to_etree(element, name_='definition', mapping_=mapping_)
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
        super(Profile_Element, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'path':
            obj_ = string.factory()
            obj_.build(child_)
            self.path = obj_
            obj_.original_tagname_ = 'path'
        elif nodeName_ == 'representation':
            obj_ = PropertyRepresentation.factory()
            obj_.build(child_)
            self.representation.append(obj_)
            obj_.original_tagname_ = 'representation'
        elif nodeName_ == 'name':
            obj_ = string.factory()
            obj_.build(child_)
            self.name = obj_
            obj_.original_tagname_ = 'name'
        elif nodeName_ == 'slicing':
            obj_ = Profile_Slicing.factory()
            obj_.build(child_)
            self.slicing = obj_
            obj_.original_tagname_ = 'slicing'
        elif nodeName_ == 'definition':
            obj_ = Profile_Definition.factory()
            obj_.build(child_)
            self.definition = obj_
            obj_.original_tagname_ = 'definition'
        super(Profile_Element, self).buildChildren(child_, node, nodeName_, True)
# end class Profile_Element


class Profile_Slicing(BackboneElement):
    """A Resource Profile - a statement of use of one or more FHIR
    Resources. It may include constraints on Resources and Data
    Types, Terminology Binding Statements and Extension Definitions."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, discriminator=None, ordered=None, rules=None):
        self.original_tagname_ = None
        super(Profile_Slicing, self).__init__(id, extension, modifierExtension, )
        self.discriminator = discriminator
        self.ordered = ordered
        self.rules = rules
    def factory(*args_, **kwargs_):
        if Profile_Slicing.subclass:
            return Profile_Slicing.subclass(*args_, **kwargs_)
        else:
            return Profile_Slicing(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_discriminator(self): return self.discriminator
    def set_discriminator(self, discriminator): self.discriminator = discriminator
    def get_ordered(self): return self.ordered
    def set_ordered(self, ordered): self.ordered = ordered
    def get_rules(self): return self.rules
    def set_rules(self, rules): self.rules = rules
    def hasContent_(self):
        if (
            self.discriminator is not None or
            self.ordered is not None or
            self.rules is not None or
            super(Profile_Slicing, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Profile.Slicing', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Profile.Slicing')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Profile.Slicing', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Profile.Slicing'):
        super(Profile_Slicing, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Profile.Slicing')
    def exportChildren(self, outfile, level, namespace_='', name_='Profile.Slicing', fromsubclass_=False, pretty_print=True):
        super(Profile_Slicing, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.discriminator is not None:
            self.discriminator.export(outfile, level, namespace_, name_='discriminator', pretty_print=pretty_print)
        if self.ordered is not None:
            self.ordered.export(outfile, level, namespace_, name_='ordered', pretty_print=pretty_print)
        if self.rules is not None:
            self.rules.export(outfile, level, namespace_, name_='rules', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Profile.Slicing', mapping_=None):
        element = super(Profile_Slicing, self).to_etree(parent_element, name_, mapping_)
        if self.discriminator is not None:
            discriminator_ = self.discriminator
            discriminator_.to_etree(element, name_='discriminator', mapping_=mapping_)
        if self.ordered is not None:
            ordered_ = self.ordered
            ordered_.to_etree(element, name_='ordered', mapping_=mapping_)
        if self.rules is not None:
            rules_ = self.rules
            rules_.to_etree(element, name_='rules', mapping_=mapping_)
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
        super(Profile_Slicing, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'discriminator':
            obj_ = id.factory()
            obj_.build(child_)
            self.discriminator = obj_
            obj_.original_tagname_ = 'discriminator'
        elif nodeName_ == 'ordered':
            obj_ = boolean.factory()
            obj_.build(child_)
            self.ordered = obj_
            obj_.original_tagname_ = 'ordered'
        elif nodeName_ == 'rules':
            obj_ = SlicingRules.factory()
            obj_.build(child_)
            self.rules = obj_
            obj_.original_tagname_ = 'rules'
        super(Profile_Slicing, self).buildChildren(child_, node, nodeName_, True)
# end class Profile_Slicing


class Profile_Definition(BackboneElement):
    """A Resource Profile - a statement of use of one or more FHIR
    Resources. It may include constraints on Resources and Data
    Types, Terminology Binding Statements and Extension
    Definitions.Specifies a primitive value that SHALL hold for this
    element in the instance.An example value for this element."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, short=None, formal=None, comments=None, requirements=None, synonym=None, min=None, max=None, type_=None, nameReference=None, valueBoolean=None, valueInteger=None, valueDecimal=None, valueBase64Binary=None, valueInstant=None, valueString=None, valueUri=None, valueDate=None, valueDateTime=None, valueCode=None, valueOid=None, valueUuid=None, valueId=None, valueAttachment=None, valueIdentifier=None, valueCodeableConcept=None, valueCoding=None, valueQuantity=None, valueRange=None, valuePeriod=None, valueRatio=None, valueResource=None, valueSampledData=None, valueHumanName=None, valueAddress=None, valueContact=None, valueSchedule=None, exampleBoolean=None, exampleInteger=None, exampleDecimal=None, exampleBase64Binary=None, exampleInstant=None, exampleString=None, exampleUri=None, exampleDate=None, exampleDateTime=None, exampleCode=None, exampleOid=None, exampleUuid=None, exampleId=None, exampleAttachment=None, exampleIdentifier=None, exampleCodeableConcept=None, exampleCoding=None, exampleQuantity=None, exampleRange=None, examplePeriod=None, exampleRatio=None, exampleResource=None, exampleSampledData=None, exampleHumanName=None, exampleAddress=None, exampleContact=None, exampleSchedule=None, maxLength=None, condition=None, constraint=None, mustSupport=None, isModifier=None, binding=None, mapping=None):
        self.original_tagname_ = None
        super(Profile_Definition, self).__init__(id, extension, modifierExtension, )
        self.short = short
        self.formal = formal
        self.comments = comments
        self.requirements = requirements
        if synonym is None:
            self.synonym = []
        else:
            self.synonym = synonym
        self.min = min
        self.max = max
        if type_ is None:
            self.type_ = []
        else:
            self.type_ = type_
        self.nameReference = nameReference
        self.valueBoolean = valueBoolean
        self.valueInteger = valueInteger
        self.valueDecimal = valueDecimal
        self.valueBase64Binary = valueBase64Binary
        self.valueInstant = valueInstant
        self.valueString = valueString
        self.valueUri = valueUri
        self.valueDate = valueDate
        self.valueDateTime = valueDateTime
        self.valueCode = valueCode
        self.valueOid = valueOid
        self.valueUuid = valueUuid
        self.valueId = valueId
        self.valueAttachment = valueAttachment
        self.valueIdentifier = valueIdentifier
        self.valueCodeableConcept = valueCodeableConcept
        self.valueCoding = valueCoding
        self.valueQuantity = valueQuantity
        self.valueRange = valueRange
        self.valuePeriod = valuePeriod
        self.valueRatio = valueRatio
        self.valueResource = valueResource
        self.valueSampledData = valueSampledData
        self.valueHumanName = valueHumanName
        self.valueAddress = valueAddress
        self.valueContact = valueContact
        self.valueSchedule = valueSchedule
        self.exampleBoolean = exampleBoolean
        self.exampleInteger = exampleInteger
        self.exampleDecimal = exampleDecimal
        self.exampleBase64Binary = exampleBase64Binary
        self.exampleInstant = exampleInstant
        self.exampleString = exampleString
        self.exampleUri = exampleUri
        self.exampleDate = exampleDate
        self.exampleDateTime = exampleDateTime
        self.exampleCode = exampleCode
        self.exampleOid = exampleOid
        self.exampleUuid = exampleUuid
        self.exampleId = exampleId
        self.exampleAttachment = exampleAttachment
        self.exampleIdentifier = exampleIdentifier
        self.exampleCodeableConcept = exampleCodeableConcept
        self.exampleCoding = exampleCoding
        self.exampleQuantity = exampleQuantity
        self.exampleRange = exampleRange
        self.examplePeriod = examplePeriod
        self.exampleRatio = exampleRatio
        self.exampleResource = exampleResource
        self.exampleSampledData = exampleSampledData
        self.exampleHumanName = exampleHumanName
        self.exampleAddress = exampleAddress
        self.exampleContact = exampleContact
        self.exampleSchedule = exampleSchedule
        self.maxLength = maxLength
        if condition is None:
            self.condition = []
        else:
            self.condition = condition
        if constraint is None:
            self.constraint = []
        else:
            self.constraint = constraint
        self.mustSupport = mustSupport
        self.isModifier = isModifier
        self.binding = binding
        if mapping is None:
            self.mapping = []
        else:
            self.mapping = mapping
    def factory(*args_, **kwargs_):
        if Profile_Definition.subclass:
            return Profile_Definition.subclass(*args_, **kwargs_)
        else:
            return Profile_Definition(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_short(self): return self.short
    def set_short(self, short): self.short = short
    def get_formal(self): return self.formal
    def set_formal(self, formal): self.formal = formal
    def get_comments(self): return self.comments
    def set_comments(self, comments): self.comments = comments
    def get_requirements(self): return self.requirements
    def set_requirements(self, requirements): self.requirements = requirements
    def get_synonym(self): return self.synonym
    def set_synonym(self, synonym): self.synonym = synonym
    def add_synonym(self, value): self.synonym.append(value)
    def insert_synonym(self, index, value): self.synonym[index] = value
    def get_min(self): return self.min
    def set_min(self, min): self.min = min
    def get_max(self): return self.max
    def set_max(self, max): self.max = max
    def get_type(self): return self.type_
    def set_type(self, type_): self.type_ = type_
    def add_type(self, value): self.type_.append(value)
    def insert_type(self, index, value): self.type_[index] = value
    def get_nameReference(self): return self.nameReference
    def set_nameReference(self, nameReference): self.nameReference = nameReference
    def get_valueBoolean(self): return self.valueBoolean
    def set_valueBoolean(self, valueBoolean): self.valueBoolean = valueBoolean
    def get_valueInteger(self): return self.valueInteger
    def set_valueInteger(self, valueInteger): self.valueInteger = valueInteger
    def get_valueDecimal(self): return self.valueDecimal
    def set_valueDecimal(self, valueDecimal): self.valueDecimal = valueDecimal
    def get_valueBase64Binary(self): return self.valueBase64Binary
    def set_valueBase64Binary(self, valueBase64Binary): self.valueBase64Binary = valueBase64Binary
    def get_valueInstant(self): return self.valueInstant
    def set_valueInstant(self, valueInstant): self.valueInstant = valueInstant
    def get_valueString(self): return self.valueString
    def set_valueString(self, valueString): self.valueString = valueString
    def get_valueUri(self): return self.valueUri
    def set_valueUri(self, valueUri): self.valueUri = valueUri
    def get_valueDate(self): return self.valueDate
    def set_valueDate(self, valueDate): self.valueDate = valueDate
    def get_valueDateTime(self): return self.valueDateTime
    def set_valueDateTime(self, valueDateTime): self.valueDateTime = valueDateTime
    def get_valueCode(self): return self.valueCode
    def set_valueCode(self, valueCode): self.valueCode = valueCode
    def get_valueOid(self): return self.valueOid
    def set_valueOid(self, valueOid): self.valueOid = valueOid
    def get_valueUuid(self): return self.valueUuid
    def set_valueUuid(self, valueUuid): self.valueUuid = valueUuid
    def get_valueId(self): return self.valueId
    def set_valueId(self, valueId): self.valueId = valueId
    def get_valueAttachment(self): return self.valueAttachment
    def set_valueAttachment(self, valueAttachment): self.valueAttachment = valueAttachment
    def get_valueIdentifier(self): return self.valueIdentifier
    def set_valueIdentifier(self, valueIdentifier): self.valueIdentifier = valueIdentifier
    def get_valueCodeableConcept(self): return self.valueCodeableConcept
    def set_valueCodeableConcept(self, valueCodeableConcept): self.valueCodeableConcept = valueCodeableConcept
    def get_valueCoding(self): return self.valueCoding
    def set_valueCoding(self, valueCoding): self.valueCoding = valueCoding
    def get_valueQuantity(self): return self.valueQuantity
    def set_valueQuantity(self, valueQuantity): self.valueQuantity = valueQuantity
    def get_valueRange(self): return self.valueRange
    def set_valueRange(self, valueRange): self.valueRange = valueRange
    def get_valuePeriod(self): return self.valuePeriod
    def set_valuePeriod(self, valuePeriod): self.valuePeriod = valuePeriod
    def get_valueRatio(self): return self.valueRatio
    def set_valueRatio(self, valueRatio): self.valueRatio = valueRatio
    def get_valueResource(self): return self.valueResource
    def set_valueResource(self, valueResource): self.valueResource = valueResource
    def get_valueSampledData(self): return self.valueSampledData
    def set_valueSampledData(self, valueSampledData): self.valueSampledData = valueSampledData
    def get_valueHumanName(self): return self.valueHumanName
    def set_valueHumanName(self, valueHumanName): self.valueHumanName = valueHumanName
    def get_valueAddress(self): return self.valueAddress
    def set_valueAddress(self, valueAddress): self.valueAddress = valueAddress
    def get_valueContact(self): return self.valueContact
    def set_valueContact(self, valueContact): self.valueContact = valueContact
    def get_valueSchedule(self): return self.valueSchedule
    def set_valueSchedule(self, valueSchedule): self.valueSchedule = valueSchedule
    def get_exampleBoolean(self): return self.exampleBoolean
    def set_exampleBoolean(self, exampleBoolean): self.exampleBoolean = exampleBoolean
    def get_exampleInteger(self): return self.exampleInteger
    def set_exampleInteger(self, exampleInteger): self.exampleInteger = exampleInteger
    def get_exampleDecimal(self): return self.exampleDecimal
    def set_exampleDecimal(self, exampleDecimal): self.exampleDecimal = exampleDecimal
    def get_exampleBase64Binary(self): return self.exampleBase64Binary
    def set_exampleBase64Binary(self, exampleBase64Binary): self.exampleBase64Binary = exampleBase64Binary
    def get_exampleInstant(self): return self.exampleInstant
    def set_exampleInstant(self, exampleInstant): self.exampleInstant = exampleInstant
    def get_exampleString(self): return self.exampleString
    def set_exampleString(self, exampleString): self.exampleString = exampleString
    def get_exampleUri(self): return self.exampleUri
    def set_exampleUri(self, exampleUri): self.exampleUri = exampleUri
    def get_exampleDate(self): return self.exampleDate
    def set_exampleDate(self, exampleDate): self.exampleDate = exampleDate
    def get_exampleDateTime(self): return self.exampleDateTime
    def set_exampleDateTime(self, exampleDateTime): self.exampleDateTime = exampleDateTime
    def get_exampleCode(self): return self.exampleCode
    def set_exampleCode(self, exampleCode): self.exampleCode = exampleCode
    def get_exampleOid(self): return self.exampleOid
    def set_exampleOid(self, exampleOid): self.exampleOid = exampleOid
    def get_exampleUuid(self): return self.exampleUuid
    def set_exampleUuid(self, exampleUuid): self.exampleUuid = exampleUuid
    def get_exampleId(self): return self.exampleId
    def set_exampleId(self, exampleId): self.exampleId = exampleId
    def get_exampleAttachment(self): return self.exampleAttachment
    def set_exampleAttachment(self, exampleAttachment): self.exampleAttachment = exampleAttachment
    def get_exampleIdentifier(self): return self.exampleIdentifier
    def set_exampleIdentifier(self, exampleIdentifier): self.exampleIdentifier = exampleIdentifier
    def get_exampleCodeableConcept(self): return self.exampleCodeableConcept
    def set_exampleCodeableConcept(self, exampleCodeableConcept): self.exampleCodeableConcept = exampleCodeableConcept
    def get_exampleCoding(self): return self.exampleCoding
    def set_exampleCoding(self, exampleCoding): self.exampleCoding = exampleCoding
    def get_exampleQuantity(self): return self.exampleQuantity
    def set_exampleQuantity(self, exampleQuantity): self.exampleQuantity = exampleQuantity
    def get_exampleRange(self): return self.exampleRange
    def set_exampleRange(self, exampleRange): self.exampleRange = exampleRange
    def get_examplePeriod(self): return self.examplePeriod
    def set_examplePeriod(self, examplePeriod): self.examplePeriod = examplePeriod
    def get_exampleRatio(self): return self.exampleRatio
    def set_exampleRatio(self, exampleRatio): self.exampleRatio = exampleRatio
    def get_exampleResource(self): return self.exampleResource
    def set_exampleResource(self, exampleResource): self.exampleResource = exampleResource
    def get_exampleSampledData(self): return self.exampleSampledData
    def set_exampleSampledData(self, exampleSampledData): self.exampleSampledData = exampleSampledData
    def get_exampleHumanName(self): return self.exampleHumanName
    def set_exampleHumanName(self, exampleHumanName): self.exampleHumanName = exampleHumanName
    def get_exampleAddress(self): return self.exampleAddress
    def set_exampleAddress(self, exampleAddress): self.exampleAddress = exampleAddress
    def get_exampleContact(self): return self.exampleContact
    def set_exampleContact(self, exampleContact): self.exampleContact = exampleContact
    def get_exampleSchedule(self): return self.exampleSchedule
    def set_exampleSchedule(self, exampleSchedule): self.exampleSchedule = exampleSchedule
    def get_maxLength(self): return self.maxLength
    def set_maxLength(self, maxLength): self.maxLength = maxLength
    def get_condition(self): return self.condition
    def set_condition(self, condition): self.condition = condition
    def add_condition(self, value): self.condition.append(value)
    def insert_condition(self, index, value): self.condition[index] = value
    def get_constraint(self): return self.constraint
    def set_constraint(self, constraint): self.constraint = constraint
    def add_constraint(self, value): self.constraint.append(value)
    def insert_constraint(self, index, value): self.constraint[index] = value
    def get_mustSupport(self): return self.mustSupport
    def set_mustSupport(self, mustSupport): self.mustSupport = mustSupport
    def get_isModifier(self): return self.isModifier
    def set_isModifier(self, isModifier): self.isModifier = isModifier
    def get_binding(self): return self.binding
    def set_binding(self, binding): self.binding = binding
    def get_mapping(self): return self.mapping
    def set_mapping(self, mapping): self.mapping = mapping
    def add_mapping(self, value): self.mapping.append(value)
    def insert_mapping(self, index, value): self.mapping[index] = value
    def hasContent_(self):
        if (
            self.short is not None or
            self.formal is not None or
            self.comments is not None or
            self.requirements is not None or
            self.synonym or
            self.min is not None or
            self.max is not None or
            self.type_ or
            self.nameReference is not None or
            self.valueBoolean is not None or
            self.valueInteger is not None or
            self.valueDecimal is not None or
            self.valueBase64Binary is not None or
            self.valueInstant is not None or
            self.valueString is not None or
            self.valueUri is not None or
            self.valueDate is not None or
            self.valueDateTime is not None or
            self.valueCode is not None or
            self.valueOid is not None or
            self.valueUuid is not None or
            self.valueId is not None or
            self.valueAttachment is not None or
            self.valueIdentifier is not None or
            self.valueCodeableConcept is not None or
            self.valueCoding is not None or
            self.valueQuantity is not None or
            self.valueRange is not None or
            self.valuePeriod is not None or
            self.valueRatio is not None or
            self.valueResource is not None or
            self.valueSampledData is not None or
            self.valueHumanName is not None or
            self.valueAddress is not None or
            self.valueContact is not None or
            self.valueSchedule is not None or
            self.exampleBoolean is not None or
            self.exampleInteger is not None or
            self.exampleDecimal is not None or
            self.exampleBase64Binary is not None or
            self.exampleInstant is not None or
            self.exampleString is not None or
            self.exampleUri is not None or
            self.exampleDate is not None or
            self.exampleDateTime is not None or
            self.exampleCode is not None or
            self.exampleOid is not None or
            self.exampleUuid is not None or
            self.exampleId is not None or
            self.exampleAttachment is not None or
            self.exampleIdentifier is not None or
            self.exampleCodeableConcept is not None or
            self.exampleCoding is not None or
            self.exampleQuantity is not None or
            self.exampleRange is not None or
            self.examplePeriod is not None or
            self.exampleRatio is not None or
            self.exampleResource is not None or
            self.exampleSampledData is not None or
            self.exampleHumanName is not None or
            self.exampleAddress is not None or
            self.exampleContact is not None or
            self.exampleSchedule is not None or
            self.maxLength is not None or
            self.condition or
            self.constraint or
            self.mustSupport is not None or
            self.isModifier is not None or
            self.binding is not None or
            self.mapping or
            super(Profile_Definition, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Profile.Definition', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Profile.Definition')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Profile.Definition', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Profile.Definition'):
        super(Profile_Definition, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Profile.Definition')
    def exportChildren(self, outfile, level, namespace_='', name_='Profile.Definition', fromsubclass_=False, pretty_print=True):
        super(Profile_Definition, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.short is not None:
            self.short.export(outfile, level, namespace_, name_='short', pretty_print=pretty_print)
        if self.formal is not None:
            self.formal.export(outfile, level, namespace_, name_='formal', pretty_print=pretty_print)
        if self.comments is not None:
            self.comments.export(outfile, level, namespace_, name_='comments', pretty_print=pretty_print)
        if self.requirements is not None:
            self.requirements.export(outfile, level, namespace_, name_='requirements', pretty_print=pretty_print)
        for synonym_ in self.synonym:
            synonym_.export(outfile, level, namespace_, name_='synonym', pretty_print=pretty_print)
        if self.min is not None:
            self.min.export(outfile, level, namespace_, name_='min', pretty_print=pretty_print)
        if self.max is not None:
            self.max.export(outfile, level, namespace_, name_='max', pretty_print=pretty_print)
        for type_ in self.type_:
            type_.export(outfile, level, namespace_, name_='type', pretty_print=pretty_print)
        if self.nameReference is not None:
            self.nameReference.export(outfile, level, namespace_, name_='nameReference', pretty_print=pretty_print)
        if self.valueBoolean is not None:
            self.valueBoolean.export(outfile, level, namespace_, name_='valueBoolean', pretty_print=pretty_print)
        if self.valueInteger is not None:
            self.valueInteger.export(outfile, level, namespace_, name_='valueInteger', pretty_print=pretty_print)
        if self.valueDecimal is not None:
            self.valueDecimal.export(outfile, level, namespace_, name_='valueDecimal', pretty_print=pretty_print)
        if self.valueBase64Binary is not None:
            self.valueBase64Binary.export(outfile, level, namespace_, name_='valueBase64Binary', pretty_print=pretty_print)
        if self.valueInstant is not None:
            self.valueInstant.export(outfile, level, namespace_, name_='valueInstant', pretty_print=pretty_print)
        if self.valueString is not None:
            self.valueString.export(outfile, level, namespace_, name_='valueString', pretty_print=pretty_print)
        if self.valueUri is not None:
            self.valueUri.export(outfile, level, namespace_, name_='valueUri', pretty_print=pretty_print)
        if self.valueDate is not None:
            self.valueDate.export(outfile, level, namespace_, name_='valueDate', pretty_print=pretty_print)
        if self.valueDateTime is not None:
            self.valueDateTime.export(outfile, level, namespace_, name_='valueDateTime', pretty_print=pretty_print)
        if self.valueCode is not None:
            self.valueCode.export(outfile, level, namespace_, name_='valueCode', pretty_print=pretty_print)
        if self.valueOid is not None:
            self.valueOid.export(outfile, level, namespace_, name_='valueOid', pretty_print=pretty_print)
        if self.valueUuid is not None:
            self.valueUuid.export(outfile, level, namespace_, name_='valueUuid', pretty_print=pretty_print)
        if self.valueId is not None:
            self.valueId.export(outfile, level, namespace_, name_='valueId', pretty_print=pretty_print)
        if self.valueAttachment is not None:
            self.valueAttachment.export(outfile, level, namespace_, name_='valueAttachment', pretty_print=pretty_print)
        if self.valueIdentifier is not None:
            self.valueIdentifier.export(outfile, level, namespace_, name_='valueIdentifier', pretty_print=pretty_print)
        if self.valueCodeableConcept is not None:
            self.valueCodeableConcept.export(outfile, level, namespace_, name_='valueCodeableConcept', pretty_print=pretty_print)
        if self.valueCoding is not None:
            self.valueCoding.export(outfile, level, namespace_, name_='valueCoding', pretty_print=pretty_print)
        if self.valueQuantity is not None:
            self.valueQuantity.export(outfile, level, namespace_, name_='valueQuantity', pretty_print=pretty_print)
        if self.valueRange is not None:
            self.valueRange.export(outfile, level, namespace_, name_='valueRange', pretty_print=pretty_print)
        if self.valuePeriod is not None:
            self.valuePeriod.export(outfile, level, namespace_, name_='valuePeriod', pretty_print=pretty_print)
        if self.valueRatio is not None:
            self.valueRatio.export(outfile, level, namespace_, name_='valueRatio', pretty_print=pretty_print)
        if self.valueResource is not None:
            self.valueResource.export(outfile, level, namespace_, name_='valueResource', pretty_print=pretty_print)
        if self.valueSampledData is not None:
            self.valueSampledData.export(outfile, level, namespace_, name_='valueSampledData', pretty_print=pretty_print)
        if self.valueHumanName is not None:
            self.valueHumanName.export(outfile, level, namespace_, name_='valueHumanName', pretty_print=pretty_print)
        if self.valueAddress is not None:
            self.valueAddress.export(outfile, level, namespace_, name_='valueAddress', pretty_print=pretty_print)
        if self.valueContact is not None:
            self.valueContact.export(outfile, level, namespace_, name_='valueContact', pretty_print=pretty_print)
        if self.valueSchedule is not None:
            self.valueSchedule.export(outfile, level, namespace_, name_='valueSchedule', pretty_print=pretty_print)
        if self.exampleBoolean is not None:
            self.exampleBoolean.export(outfile, level, namespace_, name_='exampleBoolean', pretty_print=pretty_print)
        if self.exampleInteger is not None:
            self.exampleInteger.export(outfile, level, namespace_, name_='exampleInteger', pretty_print=pretty_print)
        if self.exampleDecimal is not None:
            self.exampleDecimal.export(outfile, level, namespace_, name_='exampleDecimal', pretty_print=pretty_print)
        if self.exampleBase64Binary is not None:
            self.exampleBase64Binary.export(outfile, level, namespace_, name_='exampleBase64Binary', pretty_print=pretty_print)
        if self.exampleInstant is not None:
            self.exampleInstant.export(outfile, level, namespace_, name_='exampleInstant', pretty_print=pretty_print)
        if self.exampleString is not None:
            self.exampleString.export(outfile, level, namespace_, name_='exampleString', pretty_print=pretty_print)
        if self.exampleUri is not None:
            self.exampleUri.export(outfile, level, namespace_, name_='exampleUri', pretty_print=pretty_print)
        if self.exampleDate is not None:
            self.exampleDate.export(outfile, level, namespace_, name_='exampleDate', pretty_print=pretty_print)
        if self.exampleDateTime is not None:
            self.exampleDateTime.export(outfile, level, namespace_, name_='exampleDateTime', pretty_print=pretty_print)
        if self.exampleCode is not None:
            self.exampleCode.export(outfile, level, namespace_, name_='exampleCode', pretty_print=pretty_print)
        if self.exampleOid is not None:
            self.exampleOid.export(outfile, level, namespace_, name_='exampleOid', pretty_print=pretty_print)
        if self.exampleUuid is not None:
            self.exampleUuid.export(outfile, level, namespace_, name_='exampleUuid', pretty_print=pretty_print)
        if self.exampleId is not None:
            self.exampleId.export(outfile, level, namespace_, name_='exampleId', pretty_print=pretty_print)
        if self.exampleAttachment is not None:
            self.exampleAttachment.export(outfile, level, namespace_, name_='exampleAttachment', pretty_print=pretty_print)
        if self.exampleIdentifier is not None:
            self.exampleIdentifier.export(outfile, level, namespace_, name_='exampleIdentifier', pretty_print=pretty_print)
        if self.exampleCodeableConcept is not None:
            self.exampleCodeableConcept.export(outfile, level, namespace_, name_='exampleCodeableConcept', pretty_print=pretty_print)
        if self.exampleCoding is not None:
            self.exampleCoding.export(outfile, level, namespace_, name_='exampleCoding', pretty_print=pretty_print)
        if self.exampleQuantity is not None:
            self.exampleQuantity.export(outfile, level, namespace_, name_='exampleQuantity', pretty_print=pretty_print)
        if self.exampleRange is not None:
            self.exampleRange.export(outfile, level, namespace_, name_='exampleRange', pretty_print=pretty_print)
        if self.examplePeriod is not None:
            self.examplePeriod.export(outfile, level, namespace_, name_='examplePeriod', pretty_print=pretty_print)
        if self.exampleRatio is not None:
            self.exampleRatio.export(outfile, level, namespace_, name_='exampleRatio', pretty_print=pretty_print)
        if self.exampleResource is not None:
            self.exampleResource.export(outfile, level, namespace_, name_='exampleResource', pretty_print=pretty_print)
        if self.exampleSampledData is not None:
            self.exampleSampledData.export(outfile, level, namespace_, name_='exampleSampledData', pretty_print=pretty_print)
        if self.exampleHumanName is not None:
            self.exampleHumanName.export(outfile, level, namespace_, name_='exampleHumanName', pretty_print=pretty_print)
        if self.exampleAddress is not None:
            self.exampleAddress.export(outfile, level, namespace_, name_='exampleAddress', pretty_print=pretty_print)
        if self.exampleContact is not None:
            self.exampleContact.export(outfile, level, namespace_, name_='exampleContact', pretty_print=pretty_print)
        if self.exampleSchedule is not None:
            self.exampleSchedule.export(outfile, level, namespace_, name_='exampleSchedule', pretty_print=pretty_print)
        if self.maxLength is not None:
            self.maxLength.export(outfile, level, namespace_, name_='maxLength', pretty_print=pretty_print)
        for condition_ in self.condition:
            condition_.export(outfile, level, namespace_, name_='condition', pretty_print=pretty_print)
        for constraint_ in self.constraint:
            constraint_.export(outfile, level, namespace_, name_='constraint', pretty_print=pretty_print)
        if self.mustSupport is not None:
            self.mustSupport.export(outfile, level, namespace_, name_='mustSupport', pretty_print=pretty_print)
        if self.isModifier is not None:
            self.isModifier.export(outfile, level, namespace_, name_='isModifier', pretty_print=pretty_print)
        if self.binding is not None:
            self.binding.export(outfile, level, namespace_, name_='binding', pretty_print=pretty_print)
        for mapping_ in self.mapping:
            mapping_.export(outfile, level, namespace_, name_='mapping', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Profile.Definition', mapping_=None):
        element = super(Profile_Definition, self).to_etree(parent_element, name_, mapping_)
        if self.short is not None:
            short_ = self.short
            short_.to_etree(element, name_='short', mapping_=mapping_)
        if self.formal is not None:
            formal_ = self.formal
            formal_.to_etree(element, name_='formal', mapping_=mapping_)
        if self.comments is not None:
            comments_ = self.comments
            comments_.to_etree(element, name_='comments', mapping_=mapping_)
        if self.requirements is not None:
            requirements_ = self.requirements
            requirements_.to_etree(element, name_='requirements', mapping_=mapping_)
        for synonym_ in self.synonym:
            synonym_.to_etree(element, name_='synonym', mapping_=mapping_)
        if self.min is not None:
            min_ = self.min
            min_.to_etree(element, name_='min', mapping_=mapping_)
        if self.max is not None:
            max_ = self.max
            max_.to_etree(element, name_='max', mapping_=mapping_)
        for type__ in self.type_:
            type__.to_etree(element, name_='type', mapping_=mapping_)
        if self.nameReference is not None:
            nameReference_ = self.nameReference
            nameReference_.to_etree(element, name_='nameReference', mapping_=mapping_)
        if self.valueBoolean is not None:
            valueBoolean_ = self.valueBoolean
            valueBoolean_.to_etree(element, name_='valueBoolean', mapping_=mapping_)
        if self.valueInteger is not None:
            valueInteger_ = self.valueInteger
            valueInteger_.to_etree(element, name_='valueInteger', mapping_=mapping_)
        if self.valueDecimal is not None:
            valueDecimal_ = self.valueDecimal
            valueDecimal_.to_etree(element, name_='valueDecimal', mapping_=mapping_)
        if self.valueBase64Binary is not None:
            valueBase64Binary_ = self.valueBase64Binary
            valueBase64Binary_.to_etree(element, name_='valueBase64Binary', mapping_=mapping_)
        if self.valueInstant is not None:
            valueInstant_ = self.valueInstant
            valueInstant_.to_etree(element, name_='valueInstant', mapping_=mapping_)
        if self.valueString is not None:
            valueString_ = self.valueString
            valueString_.to_etree(element, name_='valueString', mapping_=mapping_)
        if self.valueUri is not None:
            valueUri_ = self.valueUri
            valueUri_.to_etree(element, name_='valueUri', mapping_=mapping_)
        if self.valueDate is not None:
            valueDate_ = self.valueDate
            valueDate_.to_etree(element, name_='valueDate', mapping_=mapping_)
        if self.valueDateTime is not None:
            valueDateTime_ = self.valueDateTime
            valueDateTime_.to_etree(element, name_='valueDateTime', mapping_=mapping_)
        if self.valueCode is not None:
            valueCode_ = self.valueCode
            valueCode_.to_etree(element, name_='valueCode', mapping_=mapping_)
        if self.valueOid is not None:
            valueOid_ = self.valueOid
            valueOid_.to_etree(element, name_='valueOid', mapping_=mapping_)
        if self.valueUuid is not None:
            valueUuid_ = self.valueUuid
            valueUuid_.to_etree(element, name_='valueUuid', mapping_=mapping_)
        if self.valueId is not None:
            valueId_ = self.valueId
            valueId_.to_etree(element, name_='valueId', mapping_=mapping_)
        if self.valueAttachment is not None:
            valueAttachment_ = self.valueAttachment
            valueAttachment_.to_etree(element, name_='valueAttachment', mapping_=mapping_)
        if self.valueIdentifier is not None:
            valueIdentifier_ = self.valueIdentifier
            valueIdentifier_.to_etree(element, name_='valueIdentifier', mapping_=mapping_)
        if self.valueCodeableConcept is not None:
            valueCodeableConcept_ = self.valueCodeableConcept
            valueCodeableConcept_.to_etree(element, name_='valueCodeableConcept', mapping_=mapping_)
        if self.valueCoding is not None:
            valueCoding_ = self.valueCoding
            valueCoding_.to_etree(element, name_='valueCoding', mapping_=mapping_)
        if self.valueQuantity is not None:
            valueQuantity_ = self.valueQuantity
            valueQuantity_.to_etree(element, name_='valueQuantity', mapping_=mapping_)
        if self.valueRange is not None:
            valueRange_ = self.valueRange
            valueRange_.to_etree(element, name_='valueRange', mapping_=mapping_)
        if self.valuePeriod is not None:
            valuePeriod_ = self.valuePeriod
            valuePeriod_.to_etree(element, name_='valuePeriod', mapping_=mapping_)
        if self.valueRatio is not None:
            valueRatio_ = self.valueRatio
            valueRatio_.to_etree(element, name_='valueRatio', mapping_=mapping_)
        if self.valueResource is not None:
            valueResource_ = self.valueResource
            valueResource_.to_etree(element, name_='valueResource', mapping_=mapping_)
        if self.valueSampledData is not None:
            valueSampledData_ = self.valueSampledData
            valueSampledData_.to_etree(element, name_='valueSampledData', mapping_=mapping_)
        if self.valueHumanName is not None:
            valueHumanName_ = self.valueHumanName
            valueHumanName_.to_etree(element, name_='valueHumanName', mapping_=mapping_)
        if self.valueAddress is not None:
            valueAddress_ = self.valueAddress
            valueAddress_.to_etree(element, name_='valueAddress', mapping_=mapping_)
        if self.valueContact is not None:
            valueContact_ = self.valueContact
            valueContact_.to_etree(element, name_='valueContact', mapping_=mapping_)
        if self.valueSchedule is not None:
            valueSchedule_ = self.valueSchedule
            valueSchedule_.to_etree(element, name_='valueSchedule', mapping_=mapping_)
        if self.exampleBoolean is not None:
            exampleBoolean_ = self.exampleBoolean
            exampleBoolean_.to_etree(element, name_='exampleBoolean', mapping_=mapping_)
        if self.exampleInteger is not None:
            exampleInteger_ = self.exampleInteger
            exampleInteger_.to_etree(element, name_='exampleInteger', mapping_=mapping_)
        if self.exampleDecimal is not None:
            exampleDecimal_ = self.exampleDecimal
            exampleDecimal_.to_etree(element, name_='exampleDecimal', mapping_=mapping_)
        if self.exampleBase64Binary is not None:
            exampleBase64Binary_ = self.exampleBase64Binary
            exampleBase64Binary_.to_etree(element, name_='exampleBase64Binary', mapping_=mapping_)
        if self.exampleInstant is not None:
            exampleInstant_ = self.exampleInstant
            exampleInstant_.to_etree(element, name_='exampleInstant', mapping_=mapping_)
        if self.exampleString is not None:
            exampleString_ = self.exampleString
            exampleString_.to_etree(element, name_='exampleString', mapping_=mapping_)
        if self.exampleUri is not None:
            exampleUri_ = self.exampleUri
            exampleUri_.to_etree(element, name_='exampleUri', mapping_=mapping_)
        if self.exampleDate is not None:
            exampleDate_ = self.exampleDate
            exampleDate_.to_etree(element, name_='exampleDate', mapping_=mapping_)
        if self.exampleDateTime is not None:
            exampleDateTime_ = self.exampleDateTime
            exampleDateTime_.to_etree(element, name_='exampleDateTime', mapping_=mapping_)
        if self.exampleCode is not None:
            exampleCode_ = self.exampleCode
            exampleCode_.to_etree(element, name_='exampleCode', mapping_=mapping_)
        if self.exampleOid is not None:
            exampleOid_ = self.exampleOid
            exampleOid_.to_etree(element, name_='exampleOid', mapping_=mapping_)
        if self.exampleUuid is not None:
            exampleUuid_ = self.exampleUuid
            exampleUuid_.to_etree(element, name_='exampleUuid', mapping_=mapping_)
        if self.exampleId is not None:
            exampleId_ = self.exampleId
            exampleId_.to_etree(element, name_='exampleId', mapping_=mapping_)
        if self.exampleAttachment is not None:
            exampleAttachment_ = self.exampleAttachment
            exampleAttachment_.to_etree(element, name_='exampleAttachment', mapping_=mapping_)
        if self.exampleIdentifier is not None:
            exampleIdentifier_ = self.exampleIdentifier
            exampleIdentifier_.to_etree(element, name_='exampleIdentifier', mapping_=mapping_)
        if self.exampleCodeableConcept is not None:
            exampleCodeableConcept_ = self.exampleCodeableConcept
            exampleCodeableConcept_.to_etree(element, name_='exampleCodeableConcept', mapping_=mapping_)
        if self.exampleCoding is not None:
            exampleCoding_ = self.exampleCoding
            exampleCoding_.to_etree(element, name_='exampleCoding', mapping_=mapping_)
        if self.exampleQuantity is not None:
            exampleQuantity_ = self.exampleQuantity
            exampleQuantity_.to_etree(element, name_='exampleQuantity', mapping_=mapping_)
        if self.exampleRange is not None:
            exampleRange_ = self.exampleRange
            exampleRange_.to_etree(element, name_='exampleRange', mapping_=mapping_)
        if self.examplePeriod is not None:
            examplePeriod_ = self.examplePeriod
            examplePeriod_.to_etree(element, name_='examplePeriod', mapping_=mapping_)
        if self.exampleRatio is not None:
            exampleRatio_ = self.exampleRatio
            exampleRatio_.to_etree(element, name_='exampleRatio', mapping_=mapping_)
        if self.exampleResource is not None:
            exampleResource_ = self.exampleResource
            exampleResource_.to_etree(element, name_='exampleResource', mapping_=mapping_)
        if self.exampleSampledData is not None:
            exampleSampledData_ = self.exampleSampledData
            exampleSampledData_.to_etree(element, name_='exampleSampledData', mapping_=mapping_)
        if self.exampleHumanName is not None:
            exampleHumanName_ = self.exampleHumanName
            exampleHumanName_.to_etree(element, name_='exampleHumanName', mapping_=mapping_)
        if self.exampleAddress is not None:
            exampleAddress_ = self.exampleAddress
            exampleAddress_.to_etree(element, name_='exampleAddress', mapping_=mapping_)
        if self.exampleContact is not None:
            exampleContact_ = self.exampleContact
            exampleContact_.to_etree(element, name_='exampleContact', mapping_=mapping_)
        if self.exampleSchedule is not None:
            exampleSchedule_ = self.exampleSchedule
            exampleSchedule_.to_etree(element, name_='exampleSchedule', mapping_=mapping_)
        if self.maxLength is not None:
            maxLength_ = self.maxLength
            maxLength_.to_etree(element, name_='maxLength', mapping_=mapping_)
        for condition_ in self.condition:
            condition_.to_etree(element, name_='condition', mapping_=mapping_)
        for constraint_ in self.constraint:
            constraint_.to_etree(element, name_='constraint', mapping_=mapping_)
        if self.mustSupport is not None:
            mustSupport_ = self.mustSupport
            mustSupport_.to_etree(element, name_='mustSupport', mapping_=mapping_)
        if self.isModifier is not None:
            isModifier_ = self.isModifier
            isModifier_.to_etree(element, name_='isModifier', mapping_=mapping_)
        if self.binding is not None:
            binding_ = self.binding
            binding_.to_etree(element, name_='binding', mapping_=mapping_)
        for mapping_ in self.mapping:
            mapping_.to_etree(element, name_='mapping', mapping_=mapping_)
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
        super(Profile_Definition, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'short':
            obj_ = string.factory()
            obj_.build(child_)
            self.short = obj_
            obj_.original_tagname_ = 'short'
        elif nodeName_ == 'formal':
            obj_ = string.factory()
            obj_.build(child_)
            self.formal = obj_
            obj_.original_tagname_ = 'formal'
        elif nodeName_ == 'comments':
            obj_ = string.factory()
            obj_.build(child_)
            self.comments = obj_
            obj_.original_tagname_ = 'comments'
        elif nodeName_ == 'requirements':
            obj_ = string.factory()
            obj_.build(child_)
            self.requirements = obj_
            obj_.original_tagname_ = 'requirements'
        elif nodeName_ == 'synonym':
            obj_ = string.factory()
            obj_.build(child_)
            self.synonym.append(obj_)
            obj_.original_tagname_ = 'synonym'
        elif nodeName_ == 'min':
            obj_ = integer.factory()
            obj_.build(child_)
            self.min = obj_
            obj_.original_tagname_ = 'min'
        elif nodeName_ == 'max':
            obj_ = string.factory()
            obj_.build(child_)
            self.max = obj_
            obj_.original_tagname_ = 'max'
        elif nodeName_ == 'type':
            obj_ = Profile_Type.factory()
            obj_.build(child_)
            self.type_.append(obj_)
            obj_.original_tagname_ = 'type'
        elif nodeName_ == 'nameReference':
            obj_ = string.factory()
            obj_.build(child_)
            self.nameReference = obj_
            obj_.original_tagname_ = 'nameReference'
        elif nodeName_ == 'valueBoolean':
            obj_ = boolean.factory()
            obj_.build(child_)
            self.valueBoolean = obj_
            obj_.original_tagname_ = 'valueBoolean'
        elif nodeName_ == 'valueInteger':
            obj_ = integer.factory()
            obj_.build(child_)
            self.valueInteger = obj_
            obj_.original_tagname_ = 'valueInteger'
        elif nodeName_ == 'valueDecimal':
            obj_ = decimal.factory()
            obj_.build(child_)
            self.valueDecimal = obj_
            obj_.original_tagname_ = 'valueDecimal'
        elif nodeName_ == 'valueBase64Binary':
            obj_ = base64Binary.factory()
            obj_.build(child_)
            self.valueBase64Binary = obj_
            obj_.original_tagname_ = 'valueBase64Binary'
        elif nodeName_ == 'valueInstant':
            obj_ = instant.factory()
            obj_.build(child_)
            self.valueInstant = obj_
            obj_.original_tagname_ = 'valueInstant'
        elif nodeName_ == 'valueString':
            obj_ = string.factory()
            obj_.build(child_)
            self.valueString = obj_
            obj_.original_tagname_ = 'valueString'
        elif nodeName_ == 'valueUri':
            obj_ = uri.factory()
            obj_.build(child_)
            self.valueUri = obj_
            obj_.original_tagname_ = 'valueUri'
        elif nodeName_ == 'valueDate':
            obj_ = date.factory()
            obj_.build(child_)
            self.valueDate = obj_
            obj_.original_tagname_ = 'valueDate'
        elif nodeName_ == 'valueDateTime':
            obj_ = dateTime.factory()
            obj_.build(child_)
            self.valueDateTime = obj_
            obj_.original_tagname_ = 'valueDateTime'
        elif nodeName_ == 'valueCode':
            obj_ = code.factory()
            obj_.build(child_)
            self.valueCode = obj_
            obj_.original_tagname_ = 'valueCode'
        elif nodeName_ == 'valueOid':
            obj_ = oid.factory()
            obj_.build(child_)
            self.valueOid = obj_
            obj_.original_tagname_ = 'valueOid'
        elif nodeName_ == 'valueUuid':
            obj_ = uuid.factory()
            obj_.build(child_)
            self.valueUuid = obj_
            obj_.original_tagname_ = 'valueUuid'
        elif nodeName_ == 'valueId':
            obj_ = id.factory()
            obj_.build(child_)
            self.valueId = obj_
            obj_.original_tagname_ = 'valueId'
        elif nodeName_ == 'valueAttachment':
            obj_ = Attachment.factory()
            obj_.build(child_)
            self.valueAttachment = obj_
            obj_.original_tagname_ = 'valueAttachment'
        elif nodeName_ == 'valueIdentifier':
            obj_ = Identifier.factory()
            obj_.build(child_)
            self.valueIdentifier = obj_
            obj_.original_tagname_ = 'valueIdentifier'
        elif nodeName_ == 'valueCodeableConcept':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.valueCodeableConcept = obj_
            obj_.original_tagname_ = 'valueCodeableConcept'
        elif nodeName_ == 'valueCoding':
            obj_ = Coding.factory()
            obj_.build(child_)
            self.valueCoding = obj_
            obj_.original_tagname_ = 'valueCoding'
        elif nodeName_ == 'valueQuantity':
            obj_ = Quantity.factory()
            obj_.build(child_)
            self.valueQuantity = obj_
            obj_.original_tagname_ = 'valueQuantity'
        elif nodeName_ == 'valueRange':
            obj_ = Range.factory()
            obj_.build(child_)
            self.valueRange = obj_
            obj_.original_tagname_ = 'valueRange'
        elif nodeName_ == 'valuePeriod':
            obj_ = Period.factory()
            obj_.build(child_)
            self.valuePeriod = obj_
            obj_.original_tagname_ = 'valuePeriod'
        elif nodeName_ == 'valueRatio':
            obj_ = Ratio.factory()
            obj_.build(child_)
            self.valueRatio = obj_
            obj_.original_tagname_ = 'valueRatio'
        elif nodeName_ == 'valueResource':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.valueResource = obj_
            obj_.original_tagname_ = 'valueResource'
        elif nodeName_ == 'valueSampledData':
            obj_ = SampledData.factory()
            obj_.build(child_)
            self.valueSampledData = obj_
            obj_.original_tagname_ = 'valueSampledData'
        elif nodeName_ == 'valueHumanName':
            obj_ = HumanName.factory()
            obj_.build(child_)
            self.valueHumanName = obj_
            obj_.original_tagname_ = 'valueHumanName'
        elif nodeName_ == 'valueAddress':
            obj_ = Address.factory()
            obj_.build(child_)
            self.valueAddress = obj_
            obj_.original_tagname_ = 'valueAddress'
        elif nodeName_ == 'valueContact':
            obj_ = Contact.factory()
            obj_.build(child_)
            self.valueContact = obj_
            obj_.original_tagname_ = 'valueContact'
        elif nodeName_ == 'valueSchedule':
            obj_ = Schedule.factory()
            obj_.build(child_)
            self.valueSchedule = obj_
            obj_.original_tagname_ = 'valueSchedule'
        elif nodeName_ == 'exampleBoolean':
            obj_ = boolean.factory()
            obj_.build(child_)
            self.exampleBoolean = obj_
            obj_.original_tagname_ = 'exampleBoolean'
        elif nodeName_ == 'exampleInteger':
            obj_ = integer.factory()
            obj_.build(child_)
            self.exampleInteger = obj_
            obj_.original_tagname_ = 'exampleInteger'
        elif nodeName_ == 'exampleDecimal':
            obj_ = decimal.factory()
            obj_.build(child_)
            self.exampleDecimal = obj_
            obj_.original_tagname_ = 'exampleDecimal'
        elif nodeName_ == 'exampleBase64Binary':
            obj_ = base64Binary.factory()
            obj_.build(child_)
            self.exampleBase64Binary = obj_
            obj_.original_tagname_ = 'exampleBase64Binary'
        elif nodeName_ == 'exampleInstant':
            obj_ = instant.factory()
            obj_.build(child_)
            self.exampleInstant = obj_
            obj_.original_tagname_ = 'exampleInstant'
        elif nodeName_ == 'exampleString':
            obj_ = string.factory()
            obj_.build(child_)
            self.exampleString = obj_
            obj_.original_tagname_ = 'exampleString'
        elif nodeName_ == 'exampleUri':
            obj_ = uri.factory()
            obj_.build(child_)
            self.exampleUri = obj_
            obj_.original_tagname_ = 'exampleUri'
        elif nodeName_ == 'exampleDate':
            obj_ = date.factory()
            obj_.build(child_)
            self.exampleDate = obj_
            obj_.original_tagname_ = 'exampleDate'
        elif nodeName_ == 'exampleDateTime':
            obj_ = dateTime.factory()
            obj_.build(child_)
            self.exampleDateTime = obj_
            obj_.original_tagname_ = 'exampleDateTime'
        elif nodeName_ == 'exampleCode':
            obj_ = code.factory()
            obj_.build(child_)
            self.exampleCode = obj_
            obj_.original_tagname_ = 'exampleCode'
        elif nodeName_ == 'exampleOid':
            obj_ = oid.factory()
            obj_.build(child_)
            self.exampleOid = obj_
            obj_.original_tagname_ = 'exampleOid'
        elif nodeName_ == 'exampleUuid':
            obj_ = uuid.factory()
            obj_.build(child_)
            self.exampleUuid = obj_
            obj_.original_tagname_ = 'exampleUuid'
        elif nodeName_ == 'exampleId':
            obj_ = id.factory()
            obj_.build(child_)
            self.exampleId = obj_
            obj_.original_tagname_ = 'exampleId'
        elif nodeName_ == 'exampleAttachment':
            obj_ = Attachment.factory()
            obj_.build(child_)
            self.exampleAttachment = obj_
            obj_.original_tagname_ = 'exampleAttachment'
        elif nodeName_ == 'exampleIdentifier':
            obj_ = Identifier.factory()
            obj_.build(child_)
            self.exampleIdentifier = obj_
            obj_.original_tagname_ = 'exampleIdentifier'
        elif nodeName_ == 'exampleCodeableConcept':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.exampleCodeableConcept = obj_
            obj_.original_tagname_ = 'exampleCodeableConcept'
        elif nodeName_ == 'exampleCoding':
            obj_ = Coding.factory()
            obj_.build(child_)
            self.exampleCoding = obj_
            obj_.original_tagname_ = 'exampleCoding'
        elif nodeName_ == 'exampleQuantity':
            obj_ = Quantity.factory()
            obj_.build(child_)
            self.exampleQuantity = obj_
            obj_.original_tagname_ = 'exampleQuantity'
        elif nodeName_ == 'exampleRange':
            obj_ = Range.factory()
            obj_.build(child_)
            self.exampleRange = obj_
            obj_.original_tagname_ = 'exampleRange'
        elif nodeName_ == 'examplePeriod':
            obj_ = Period.factory()
            obj_.build(child_)
            self.examplePeriod = obj_
            obj_.original_tagname_ = 'examplePeriod'
        elif nodeName_ == 'exampleRatio':
            obj_ = Ratio.factory()
            obj_.build(child_)
            self.exampleRatio = obj_
            obj_.original_tagname_ = 'exampleRatio'
        elif nodeName_ == 'exampleResource':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.exampleResource = obj_
            obj_.original_tagname_ = 'exampleResource'
        elif nodeName_ == 'exampleSampledData':
            obj_ = SampledData.factory()
            obj_.build(child_)
            self.exampleSampledData = obj_
            obj_.original_tagname_ = 'exampleSampledData'
        elif nodeName_ == 'exampleHumanName':
            obj_ = HumanName.factory()
            obj_.build(child_)
            self.exampleHumanName = obj_
            obj_.original_tagname_ = 'exampleHumanName'
        elif nodeName_ == 'exampleAddress':
            obj_ = Address.factory()
            obj_.build(child_)
            self.exampleAddress = obj_
            obj_.original_tagname_ = 'exampleAddress'
        elif nodeName_ == 'exampleContact':
            obj_ = Contact.factory()
            obj_.build(child_)
            self.exampleContact = obj_
            obj_.original_tagname_ = 'exampleContact'
        elif nodeName_ == 'exampleSchedule':
            obj_ = Schedule.factory()
            obj_.build(child_)
            self.exampleSchedule = obj_
            obj_.original_tagname_ = 'exampleSchedule'
        elif nodeName_ == 'maxLength':
            obj_ = integer.factory()
            obj_.build(child_)
            self.maxLength = obj_
            obj_.original_tagname_ = 'maxLength'
        elif nodeName_ == 'condition':
            obj_ = id.factory()
            obj_.build(child_)
            self.condition.append(obj_)
            obj_.original_tagname_ = 'condition'
        elif nodeName_ == 'constraint':
            obj_ = Profile_Constraint.factory()
            obj_.build(child_)
            self.constraint.append(obj_)
            obj_.original_tagname_ = 'constraint'
        elif nodeName_ == 'mustSupport':
            obj_ = boolean.factory()
            obj_.build(child_)
            self.mustSupport = obj_
            obj_.original_tagname_ = 'mustSupport'
        elif nodeName_ == 'isModifier':
            obj_ = boolean.factory()
            obj_.build(child_)
            self.isModifier = obj_
            obj_.original_tagname_ = 'isModifier'
        elif nodeName_ == 'binding':
            obj_ = Profile_Binding.factory()
            obj_.build(child_)
            self.binding = obj_
            obj_.original_tagname_ = 'binding'
        elif nodeName_ == 'mapping':
            obj_ = Profile_Mapping1.factory()
            obj_.build(child_)
            self.mapping.append(obj_)
            obj_.original_tagname_ = 'mapping'
        super(Profile_Definition, self).buildChildren(child_, node, nodeName_, True)
# end class Profile_Definition


class Profile_Type(BackboneElement):
    """A Resource Profile - a statement of use of one or more FHIR
    Resources. It may include constraints on Resources and Data
    Types, Terminology Binding Statements and Extension Definitions."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, code=None, profile=None, aggregation=None):
        self.original_tagname_ = None
        super(Profile_Type, self).__init__(id, extension, modifierExtension, )
        self.code = code
        self.profile = profile
        if aggregation is None:
            self.aggregation = []
        else:
            self.aggregation = aggregation
    def factory(*args_, **kwargs_):
        if Profile_Type.subclass:
            return Profile_Type.subclass(*args_, **kwargs_)
        else:
            return Profile_Type(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_code(self): return self.code
    def set_code(self, code): self.code = code
    def get_profile(self): return self.profile
    def set_profile(self, profile): self.profile = profile
    def get_aggregation(self): return self.aggregation
    def set_aggregation(self, aggregation): self.aggregation = aggregation
    def add_aggregation(self, value): self.aggregation.append(value)
    def insert_aggregation(self, index, value): self.aggregation[index] = value
    def hasContent_(self):
        if (
            self.code is not None or
            self.profile is not None or
            self.aggregation or
            super(Profile_Type, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Profile.Type', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Profile.Type')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Profile.Type', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Profile.Type'):
        super(Profile_Type, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Profile.Type')
    def exportChildren(self, outfile, level, namespace_='', name_='Profile.Type', fromsubclass_=False, pretty_print=True):
        super(Profile_Type, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.code is not None:
            self.code.export(outfile, level, namespace_, name_='code', pretty_print=pretty_print)
        if self.profile is not None:
            self.profile.export(outfile, level, namespace_, name_='profile', pretty_print=pretty_print)
        for aggregation_ in self.aggregation:
            aggregation_.export(outfile, level, namespace_, name_='aggregation', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Profile.Type', mapping_=None):
        element = super(Profile_Type, self).to_etree(parent_element, name_, mapping_)
        if self.code is not None:
            code_ = self.code
            code_.to_etree(element, name_='code', mapping_=mapping_)
        if self.profile is not None:
            profile_ = self.profile
            profile_.to_etree(element, name_='profile', mapping_=mapping_)
        for aggregation_ in self.aggregation:
            aggregation_.to_etree(element, name_='aggregation', mapping_=mapping_)
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
        super(Profile_Type, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'code':
            obj_ = code.factory()
            obj_.build(child_)
            self.code = obj_
            obj_.original_tagname_ = 'code'
        elif nodeName_ == 'profile':
            obj_ = uri.factory()
            obj_.build(child_)
            self.profile = obj_
            obj_.original_tagname_ = 'profile'
        elif nodeName_ == 'aggregation':
            obj_ = AggregationMode.factory()
            obj_.build(child_)
            self.aggregation.append(obj_)
            obj_.original_tagname_ = 'aggregation'
        super(Profile_Type, self).buildChildren(child_, node, nodeName_, True)
# end class Profile_Type


class Profile_Constraint(BackboneElement):
    """A Resource Profile - a statement of use of one or more FHIR
    Resources. It may include constraints on Resources and Data
    Types, Terminology Binding Statements and Extension Definitions."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, key=None, name=None, severity=None, human=None, xpath=None):
        self.original_tagname_ = None
        super(Profile_Constraint, self).__init__(id, extension, modifierExtension, )
        self.key = key
        self.name = name
        self.severity = severity
        self.human = human
        self.xpath = xpath
    def factory(*args_, **kwargs_):
        if Profile_Constraint.subclass:
            return Profile_Constraint.subclass(*args_, **kwargs_)
        else:
            return Profile_Constraint(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_key(self): return self.key
    def set_key(self, key): self.key = key
    def get_name(self): return self.name
    def set_name(self, name): self.name = name
    def get_severity(self): return self.severity
    def set_severity(self, severity): self.severity = severity
    def get_human(self): return self.human
    def set_human(self, human): self.human = human
    def get_xpath(self): return self.xpath
    def set_xpath(self, xpath): self.xpath = xpath
    def hasContent_(self):
        if (
            self.key is not None or
            self.name is not None or
            self.severity is not None or
            self.human is not None or
            self.xpath is not None or
            super(Profile_Constraint, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Profile.Constraint', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Profile.Constraint')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Profile.Constraint', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Profile.Constraint'):
        super(Profile_Constraint, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Profile.Constraint')
    def exportChildren(self, outfile, level, namespace_='', name_='Profile.Constraint', fromsubclass_=False, pretty_print=True):
        super(Profile_Constraint, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.key is not None:
            self.key.export(outfile, level, namespace_, name_='key', pretty_print=pretty_print)
        if self.name is not None:
            self.name.export(outfile, level, namespace_, name_='name', pretty_print=pretty_print)
        if self.severity is not None:
            self.severity.export(outfile, level, namespace_, name_='severity', pretty_print=pretty_print)
        if self.human is not None:
            self.human.export(outfile, level, namespace_, name_='human', pretty_print=pretty_print)
        if self.xpath is not None:
            self.xpath.export(outfile, level, namespace_, name_='xpath', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Profile.Constraint', mapping_=None):
        element = super(Profile_Constraint, self).to_etree(parent_element, name_, mapping_)
        if self.key is not None:
            key_ = self.key
            key_.to_etree(element, name_='key', mapping_=mapping_)
        if self.name is not None:
            name_ = self.name
            name_.to_etree(element, name_='name', mapping_=mapping_)
        if self.severity is not None:
            severity_ = self.severity
            severity_.to_etree(element, name_='severity', mapping_=mapping_)
        if self.human is not None:
            human_ = self.human
            human_.to_etree(element, name_='human', mapping_=mapping_)
        if self.xpath is not None:
            xpath_ = self.xpath
            xpath_.to_etree(element, name_='xpath', mapping_=mapping_)
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
        super(Profile_Constraint, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'key':
            obj_ = id.factory()
            obj_.build(child_)
            self.key = obj_
            obj_.original_tagname_ = 'key'
        elif nodeName_ == 'name':
            obj_ = string.factory()
            obj_.build(child_)
            self.name = obj_
            obj_.original_tagname_ = 'name'
        elif nodeName_ == 'severity':
            obj_ = ConstraintSeverity.factory()
            obj_.build(child_)
            self.severity = obj_
            obj_.original_tagname_ = 'severity'
        elif nodeName_ == 'human':
            obj_ = string.factory()
            obj_.build(child_)
            self.human = obj_
            obj_.original_tagname_ = 'human'
        elif nodeName_ == 'xpath':
            obj_ = string.factory()
            obj_.build(child_)
            self.xpath = obj_
            obj_.original_tagname_ = 'xpath'
        super(Profile_Constraint, self).buildChildren(child_, node, nodeName_, True)
# end class Profile_Constraint


class Profile_Binding(BackboneElement):
    """A Resource Profile - a statement of use of one or more FHIR
    Resources. It may include constraints on Resources and Data
    Types, Terminology Binding Statements and Extension
    Definitions.Points to the value set or external definition that
    identifies the set of codes to be used."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, name=None, isExtensible=None, conformance=None, description=None, referenceUri=None, referenceResource=None):
        self.original_tagname_ = None
        super(Profile_Binding, self).__init__(id, extension, modifierExtension, )
        self.name = name
        self.isExtensible = isExtensible
        self.conformance = conformance
        self.description = description
        self.referenceUri = referenceUri
        self.referenceResource = referenceResource
    def factory(*args_, **kwargs_):
        if Profile_Binding.subclass:
            return Profile_Binding.subclass(*args_, **kwargs_)
        else:
            return Profile_Binding(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_name(self): return self.name
    def set_name(self, name): self.name = name
    def get_isExtensible(self): return self.isExtensible
    def set_isExtensible(self, isExtensible): self.isExtensible = isExtensible
    def get_conformance(self): return self.conformance
    def set_conformance(self, conformance): self.conformance = conformance
    def get_description(self): return self.description
    def set_description(self, description): self.description = description
    def get_referenceUri(self): return self.referenceUri
    def set_referenceUri(self, referenceUri): self.referenceUri = referenceUri
    def get_referenceResource(self): return self.referenceResource
    def set_referenceResource(self, referenceResource): self.referenceResource = referenceResource
    def hasContent_(self):
        if (
            self.name is not None or
            self.isExtensible is not None or
            self.conformance is not None or
            self.description is not None or
            self.referenceUri is not None or
            self.referenceResource is not None or
            super(Profile_Binding, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Profile.Binding', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Profile.Binding')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Profile.Binding', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Profile.Binding'):
        super(Profile_Binding, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Profile.Binding')
    def exportChildren(self, outfile, level, namespace_='', name_='Profile.Binding', fromsubclass_=False, pretty_print=True):
        super(Profile_Binding, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.name is not None:
            self.name.export(outfile, level, namespace_, name_='name', pretty_print=pretty_print)
        if self.isExtensible is not None:
            self.isExtensible.export(outfile, level, namespace_, name_='isExtensible', pretty_print=pretty_print)
        if self.conformance is not None:
            self.conformance.export(outfile, level, namespace_, name_='conformance', pretty_print=pretty_print)
        if self.description is not None:
            self.description.export(outfile, level, namespace_, name_='description', pretty_print=pretty_print)
        if self.referenceUri is not None:
            self.referenceUri.export(outfile, level, namespace_, name_='referenceUri', pretty_print=pretty_print)
        if self.referenceResource is not None:
            self.referenceResource.export(outfile, level, namespace_, name_='referenceResource', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Profile.Binding', mapping_=None):
        element = super(Profile_Binding, self).to_etree(parent_element, name_, mapping_)
        if self.name is not None:
            name_ = self.name
            name_.to_etree(element, name_='name', mapping_=mapping_)
        if self.isExtensible is not None:
            isExtensible_ = self.isExtensible
            isExtensible_.to_etree(element, name_='isExtensible', mapping_=mapping_)
        if self.conformance is not None:
            conformance_ = self.conformance
            conformance_.to_etree(element, name_='conformance', mapping_=mapping_)
        if self.description is not None:
            description_ = self.description
            description_.to_etree(element, name_='description', mapping_=mapping_)
        if self.referenceUri is not None:
            referenceUri_ = self.referenceUri
            referenceUri_.to_etree(element, name_='referenceUri', mapping_=mapping_)
        if self.referenceResource is not None:
            referenceResource_ = self.referenceResource
            referenceResource_.to_etree(element, name_='referenceResource', mapping_=mapping_)
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
        super(Profile_Binding, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'name':
            obj_ = string.factory()
            obj_.build(child_)
            self.name = obj_
            obj_.original_tagname_ = 'name'
        elif nodeName_ == 'isExtensible':
            obj_ = boolean.factory()
            obj_.build(child_)
            self.isExtensible = obj_
            obj_.original_tagname_ = 'isExtensible'
        elif nodeName_ == 'conformance':
            obj_ = BindingConformance.factory()
            obj_.build(child_)
            self.conformance = obj_
            obj_.original_tagname_ = 'conformance'
        elif nodeName_ == 'description':
            obj_ = string.factory()
            obj_.build(child_)
            self.description = obj_
            obj_.original_tagname_ = 'description'
        elif nodeName_ == 'referenceUri':
            obj_ = uri.factory()
            obj_.build(child_)
            self.referenceUri = obj_
            obj_.original_tagname_ = 'referenceUri'
        elif nodeName_ == 'referenceResource':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.referenceResource = obj_
            obj_.original_tagname_ = 'referenceResource'
        super(Profile_Binding, self).buildChildren(child_, node, nodeName_, True)
# end class Profile_Binding


class Profile_Mapping1(BackboneElement):
    """A Resource Profile - a statement of use of one or more FHIR
    Resources. It may include constraints on Resources and Data
    Types, Terminology Binding Statements and Extension Definitions."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, identity=None, map=None):
        self.original_tagname_ = None
        super(Profile_Mapping1, self).__init__(id, extension, modifierExtension, )
        self.identity = identity
        self.map = map
    def factory(*args_, **kwargs_):
        if Profile_Mapping1.subclass:
            return Profile_Mapping1.subclass(*args_, **kwargs_)
        else:
            return Profile_Mapping1(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_identity(self): return self.identity
    def set_identity(self, identity): self.identity = identity
    def get_map(self): return self.map
    def set_map(self, map): self.map = map
    def hasContent_(self):
        if (
            self.identity is not None or
            self.map is not None or
            super(Profile_Mapping1, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Profile.Mapping1', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Profile.Mapping1')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Profile.Mapping1', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Profile.Mapping1'):
        super(Profile_Mapping1, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Profile.Mapping1')
    def exportChildren(self, outfile, level, namespace_='', name_='Profile.Mapping1', fromsubclass_=False, pretty_print=True):
        super(Profile_Mapping1, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.identity is not None:
            self.identity.export(outfile, level, namespace_, name_='identity', pretty_print=pretty_print)
        if self.map is not None:
            self.map.export(outfile, level, namespace_, name_='map', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Profile.Mapping1', mapping_=None):
        element = super(Profile_Mapping1, self).to_etree(parent_element, name_, mapping_)
        if self.identity is not None:
            identity_ = self.identity
            identity_.to_etree(element, name_='identity', mapping_=mapping_)
        if self.map is not None:
            map_ = self.map
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
        super(Profile_Mapping1, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'identity':
            obj_ = id.factory()
            obj_.build(child_)
            self.identity = obj_
            obj_.original_tagname_ = 'identity'
        elif nodeName_ == 'map':
            obj_ = string.factory()
            obj_.build(child_)
            self.map = obj_
            obj_.original_tagname_ = 'map'
        super(Profile_Mapping1, self).buildChildren(child_, node, nodeName_, True)
# end class Profile_Mapping1


class Profile_SearchParam(BackboneElement):
    """A Resource Profile - a statement of use of one or more FHIR
    Resources. It may include constraints on Resources and Data
    Types, Terminology Binding Statements and Extension Definitions."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, name=None, type_=None, documentation=None, xpath=None, target=None):
        self.original_tagname_ = None
        super(Profile_SearchParam, self).__init__(id, extension, modifierExtension, )
        self.name = name
        self.type_ = type_
        self.documentation = documentation
        self.xpath = xpath
        if target is None:
            self.target = []
        else:
            self.target = target
    def factory(*args_, **kwargs_):
        if Profile_SearchParam.subclass:
            return Profile_SearchParam.subclass(*args_, **kwargs_)
        else:
            return Profile_SearchParam(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_name(self): return self.name
    def set_name(self, name): self.name = name
    def get_type(self): return self.type_
    def set_type(self, type_): self.type_ = type_
    def get_documentation(self): return self.documentation
    def set_documentation(self, documentation): self.documentation = documentation
    def get_xpath(self): return self.xpath
    def set_xpath(self, xpath): self.xpath = xpath
    def get_target(self): return self.target
    def set_target(self, target): self.target = target
    def add_target(self, value): self.target.append(value)
    def insert_target(self, index, value): self.target[index] = value
    def hasContent_(self):
        if (
            self.name is not None or
            self.type_ is not None or
            self.documentation is not None or
            self.xpath is not None or
            self.target or
            super(Profile_SearchParam, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Profile.SearchParam', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Profile.SearchParam')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Profile.SearchParam', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Profile.SearchParam'):
        super(Profile_SearchParam, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Profile.SearchParam')
    def exportChildren(self, outfile, level, namespace_='', name_='Profile.SearchParam', fromsubclass_=False, pretty_print=True):
        super(Profile_SearchParam, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.name is not None:
            self.name.export(outfile, level, namespace_, name_='name', pretty_print=pretty_print)
        if self.type_ is not None:
            self.type_.export(outfile, level, namespace_, name_='type', pretty_print=pretty_print)
        if self.documentation is not None:
            self.documentation.export(outfile, level, namespace_, name_='documentation', pretty_print=pretty_print)
        if self.xpath is not None:
            self.xpath.export(outfile, level, namespace_, name_='xpath', pretty_print=pretty_print)
        for target_ in self.target:
            target_.export(outfile, level, namespace_, name_='target', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Profile.SearchParam', mapping_=None):
        element = super(Profile_SearchParam, self).to_etree(parent_element, name_, mapping_)
        if self.name is not None:
            name_ = self.name
            name_.to_etree(element, name_='name', mapping_=mapping_)
        if self.type_ is not None:
            type__ = self.type_
            type__.to_etree(element, name_='type', mapping_=mapping_)
        if self.documentation is not None:
            documentation_ = self.documentation
            documentation_.to_etree(element, name_='documentation', mapping_=mapping_)
        if self.xpath is not None:
            xpath_ = self.xpath
            xpath_.to_etree(element, name_='xpath', mapping_=mapping_)
        for target_ in self.target:
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
        super(Profile_SearchParam, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'name':
            obj_ = string.factory()
            obj_.build(child_)
            self.name = obj_
            obj_.original_tagname_ = 'name'
        elif nodeName_ == 'type':
            obj_ = SearchParamType.factory()
            obj_.build(child_)
            self.type_ = obj_
            obj_.original_tagname_ = 'type'
        elif nodeName_ == 'documentation':
            obj_ = string.factory()
            obj_.build(child_)
            self.documentation = obj_
            obj_.original_tagname_ = 'documentation'
        elif nodeName_ == 'xpath':
            obj_ = string.factory()
            obj_.build(child_)
            self.xpath = obj_
            obj_.original_tagname_ = 'xpath'
        elif nodeName_ == 'target':
            obj_ = code.factory()
            obj_.build(child_)
            self.target.append(obj_)
            obj_.original_tagname_ = 'target'
        super(Profile_SearchParam, self).buildChildren(child_, node, nodeName_, True)
# end class Profile_SearchParam


class Profile_ExtensionDefn(BackboneElement):
    """A Resource Profile - a statement of use of one or more FHIR
    Resources. It may include constraints on Resources and Data
    Types, Terminology Binding Statements and Extension Definitions."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, code=None, display=None, contextType=None, context=None, definition=None):
        self.original_tagname_ = None
        super(Profile_ExtensionDefn, self).__init__(id, extension, modifierExtension, )
        self.code = code
        self.display = display
        self.contextType = contextType
        if context is None:
            self.context = []
        else:
            self.context = context
        self.definition = definition
    def factory(*args_, **kwargs_):
        if Profile_ExtensionDefn.subclass:
            return Profile_ExtensionDefn.subclass(*args_, **kwargs_)
        else:
            return Profile_ExtensionDefn(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_code(self): return self.code
    def set_code(self, code): self.code = code
    def get_display(self): return self.display
    def set_display(self, display): self.display = display
    def get_contextType(self): return self.contextType
    def set_contextType(self, contextType): self.contextType = contextType
    def get_context(self): return self.context
    def set_context(self, context): self.context = context
    def add_context(self, value): self.context.append(value)
    def insert_context(self, index, value): self.context[index] = value
    def get_definition(self): return self.definition
    def set_definition(self, definition): self.definition = definition
    def hasContent_(self):
        if (
            self.code is not None or
            self.display is not None or
            self.contextType is not None or
            self.context or
            self.definition is not None or
            super(Profile_ExtensionDefn, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Profile.ExtensionDefn', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Profile.ExtensionDefn')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Profile.ExtensionDefn', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Profile.ExtensionDefn'):
        super(Profile_ExtensionDefn, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Profile.ExtensionDefn')
    def exportChildren(self, outfile, level, namespace_='', name_='Profile.ExtensionDefn', fromsubclass_=False, pretty_print=True):
        super(Profile_ExtensionDefn, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.code is not None:
            self.code.export(outfile, level, namespace_, name_='code', pretty_print=pretty_print)
        if self.display is not None:
            self.display.export(outfile, level, namespace_, name_='display', pretty_print=pretty_print)
        if self.contextType is not None:
            self.contextType.export(outfile, level, namespace_, name_='contextType', pretty_print=pretty_print)
        for context_ in self.context:
            context_.export(outfile, level, namespace_, name_='context', pretty_print=pretty_print)
        if self.definition is not None:
            self.definition.export(outfile, level, namespace_, name_='definition', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Profile.ExtensionDefn', mapping_=None):
        element = super(Profile_ExtensionDefn, self).to_etree(parent_element, name_, mapping_)
        if self.code is not None:
            code_ = self.code
            code_.to_etree(element, name_='code', mapping_=mapping_)
        if self.display is not None:
            display_ = self.display
            display_.to_etree(element, name_='display', mapping_=mapping_)
        if self.contextType is not None:
            contextType_ = self.contextType
            contextType_.to_etree(element, name_='contextType', mapping_=mapping_)
        for context_ in self.context:
            context_.to_etree(element, name_='context', mapping_=mapping_)
        if self.definition is not None:
            definition_ = self.definition
            definition_.to_etree(element, name_='definition', mapping_=mapping_)
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
        super(Profile_ExtensionDefn, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'code':
            obj_ = code.factory()
            obj_.build(child_)
            self.code = obj_
            obj_.original_tagname_ = 'code'
        elif nodeName_ == 'display':
            obj_ = string.factory()
            obj_.build(child_)
            self.display = obj_
            obj_.original_tagname_ = 'display'
        elif nodeName_ == 'contextType':
            obj_ = ExtensionContext.factory()
            obj_.build(child_)
            self.contextType = obj_
            obj_.original_tagname_ = 'contextType'
        elif nodeName_ == 'context':
            obj_ = string.factory()
            obj_.build(child_)
            self.context.append(obj_)
            obj_.original_tagname_ = 'context'
        elif nodeName_ == 'definition':
            obj_ = Profile_Definition.factory()
            obj_.build(child_)
            self.definition = obj_
            obj_.original_tagname_ = 'definition'
        super(Profile_ExtensionDefn, self).buildChildren(child_, node, nodeName_, True)
# end class Profile_ExtensionDefn


class Profile_Query(BackboneElement):
    """A Resource Profile - a statement of use of one or more FHIR
    Resources. It may include constraints on Resources and Data
    Types, Terminology Binding Statements and Extension Definitions."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, name=None, documentation=None, parameter=None):
        self.original_tagname_ = None
        super(Profile_Query, self).__init__(id, extension, modifierExtension, )
        self.name = name
        self.documentation = documentation
        if parameter is None:
            self.parameter = []
        else:
            self.parameter = parameter
    def factory(*args_, **kwargs_):
        if Profile_Query.subclass:
            return Profile_Query.subclass(*args_, **kwargs_)
        else:
            return Profile_Query(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_name(self): return self.name
    def set_name(self, name): self.name = name
    def get_documentation(self): return self.documentation
    def set_documentation(self, documentation): self.documentation = documentation
    def get_parameter(self): return self.parameter
    def set_parameter(self, parameter): self.parameter = parameter
    def add_parameter(self, value): self.parameter.append(value)
    def insert_parameter(self, index, value): self.parameter[index] = value
    def hasContent_(self):
        if (
            self.name is not None or
            self.documentation is not None or
            self.parameter or
            super(Profile_Query, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Profile.Query', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Profile.Query')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Profile.Query', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Profile.Query'):
        super(Profile_Query, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Profile.Query')
    def exportChildren(self, outfile, level, namespace_='', name_='Profile.Query', fromsubclass_=False, pretty_print=True):
        super(Profile_Query, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.name is not None:
            self.name.export(outfile, level, namespace_, name_='name', pretty_print=pretty_print)
        if self.documentation is not None:
            self.documentation.export(outfile, level, namespace_, name_='documentation', pretty_print=pretty_print)
        for parameter_ in self.parameter:
            parameter_.export(outfile, level, namespace_, name_='parameter', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Profile.Query', mapping_=None):
        element = super(Profile_Query, self).to_etree(parent_element, name_, mapping_)
        if self.name is not None:
            name_ = self.name
            name_.to_etree(element, name_='name', mapping_=mapping_)
        if self.documentation is not None:
            documentation_ = self.documentation
            documentation_.to_etree(element, name_='documentation', mapping_=mapping_)
        for parameter_ in self.parameter:
            parameter_.to_etree(element, name_='parameter', mapping_=mapping_)
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
        super(Profile_Query, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'name':
            obj_ = string.factory()
            obj_.build(child_)
            self.name = obj_
            obj_.original_tagname_ = 'name'
        elif nodeName_ == 'documentation':
            obj_ = string.factory()
            obj_.build(child_)
            self.documentation = obj_
            obj_.original_tagname_ = 'documentation'
        elif nodeName_ == 'parameter':
            obj_ = Profile_SearchParam.factory()
            obj_.build(child_)
            self.parameter.append(obj_)
            obj_.original_tagname_ = 'parameter'
        super(Profile_Query, self).buildChildren(child_, node, nodeName_, True)
# end class Profile_Query


class ResourceProfileStatus(Element):
    """The lifecycle status of a Resource ProfileIf the element is present,
    it must have either a @value, an @id, or extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(ResourceProfileStatus, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if ResourceProfileStatus.subclass:
            return ResourceProfileStatus.subclass(*args_, **kwargs_)
        else:
            return ResourceProfileStatus(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(ResourceProfileStatus, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='ResourceProfileStatus', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ResourceProfileStatus')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='ResourceProfileStatus', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='ResourceProfileStatus'):
        super(ResourceProfileStatus, self).exportAttributes(outfile, level, already_processed, namespace_, name_='ResourceProfileStatus')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='ResourceProfileStatus', fromsubclass_=False, pretty_print=True):
        super(ResourceProfileStatus, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='ResourceProfileStatus', mapping_=None):
        element = super(ResourceProfileStatus, self).to_etree(parent_element, name_, mapping_)
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
        super(ResourceProfileStatus, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(ResourceProfileStatus, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class ResourceProfileStatus
