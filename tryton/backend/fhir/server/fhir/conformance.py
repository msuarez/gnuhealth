from .base_classes import *
from .support_functions import *


class Conformance(Resource):
    """A conformance statement is a set of requirements for a desired
    implementation or a description of how a target application
    fulfills those requirements in a particular implementation.If
    the element is present, it must have either a @value, an @id, or
    extensions"""
    subclass = None
    superclass = Resource
    def __init__(self, id=None, extension=None, modifierExtension=None, language=None, text=None, contained=None, identifier=None, version=None, name=None, publisher=None, telecom=None, description=None, status=None, experimental=None, date=None, software=None, implementation=None, fhirVersion=None, acceptUnknown=None, format=None, profile=None, rest=None, messaging=None, document=None):
        self.original_tagname_ = None
        super(Conformance, self).__init__(id, extension, modifierExtension, language, text, contained, )
        self.identifier = identifier
        self.version = version
        self.name = name
        self.publisher = publisher
        if telecom is None:
            self.telecom = []
        else:
            self.telecom = telecom
        self.description = description
        self.status = status
        self.experimental = experimental
        self.date = date
        self.software = software
        self.implementation = implementation
        self.fhirVersion = fhirVersion
        self.acceptUnknown = acceptUnknown
        if format is None:
            self.format = []
        else:
            self.format = format
        if profile is None:
            self.profile = []
        else:
            self.profile = profile
        if rest is None:
            self.rest = []
        else:
            self.rest = rest
        if messaging is None:
            self.messaging = []
        else:
            self.messaging = messaging
        if document is None:
            self.document = []
        else:
            self.document = document
    def factory(*args_, **kwargs_):
        if Conformance.subclass:
            return Conformance.subclass(*args_, **kwargs_)
        else:
            return Conformance(*args_, **kwargs_)
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
    def get_status(self): return self.status
    def set_status(self, status): self.status = status
    def get_experimental(self): return self.experimental
    def set_experimental(self, experimental): self.experimental = experimental
    def get_date(self): return self.date
    def set_date(self, date): self.date = date
    def get_software(self): return self.software
    def set_software(self, software): self.software = software
    def get_implementation(self): return self.implementation
    def set_implementation(self, implementation): self.implementation = implementation
    def get_fhirVersion(self): return self.fhirVersion
    def set_fhirVersion(self, fhirVersion): self.fhirVersion = fhirVersion
    def get_acceptUnknown(self): return self.acceptUnknown
    def set_acceptUnknown(self, acceptUnknown): self.acceptUnknown = acceptUnknown
    def get_format(self): return self.format
    def set_format(self, format): self.format = format
    def add_format(self, value): self.format.append(value)
    def insert_format(self, index, value): self.format[index] = value
    def get_profile(self): return self.profile
    def set_profile(self, profile): self.profile = profile
    def add_profile(self, value): self.profile.append(value)
    def insert_profile(self, index, value): self.profile[index] = value
    def get_rest(self): return self.rest
    def set_rest(self, rest): self.rest = rest
    def add_rest(self, value): self.rest.append(value)
    def insert_rest(self, index, value): self.rest[index] = value
    def get_messaging(self): return self.messaging
    def set_messaging(self, messaging): self.messaging = messaging
    def add_messaging(self, value): self.messaging.append(value)
    def insert_messaging(self, index, value): self.messaging[index] = value
    def get_document(self): return self.document
    def set_document(self, document): self.document = document
    def add_document(self, value): self.document.append(value)
    def insert_document(self, index, value): self.document[index] = value
    def hasContent_(self):
        if (
            self.identifier is not None or
            self.version is not None or
            self.name is not None or
            self.publisher is not None or
            self.telecom or
            self.description is not None or
            self.status is not None or
            self.experimental is not None or
            self.date is not None or
            self.software is not None or
            self.implementation is not None or
            self.fhirVersion is not None or
            self.acceptUnknown is not None or
            self.format or
            self.profile or
            self.rest or
            self.messaging or
            self.document or
            super(Conformance, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Conformance', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Conformance')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Conformance', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Conformance'):
        super(Conformance, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Conformance')
    def exportChildren(self, outfile, level, namespace_='', name_='Conformance', fromsubclass_=False, pretty_print=True):
        super(Conformance, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
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
        if self.status is not None:
            self.status.export(outfile, level, namespace_, name_='status', pretty_print=pretty_print)
        if self.experimental is not None:
            self.experimental.export(outfile, level, namespace_, name_='experimental', pretty_print=pretty_print)
        if self.date is not None:
            self.date.export(outfile, level, namespace_, name_='date', pretty_print=pretty_print)
        if self.software is not None:
            self.software.export(outfile, level, namespace_, name_='software', pretty_print=pretty_print)
        if self.implementation is not None:
            self.implementation.export(outfile, level, namespace_, name_='implementation', pretty_print=pretty_print)
        if self.fhirVersion is not None:
            self.fhirVersion.export(outfile, level, namespace_, name_='fhirVersion', pretty_print=pretty_print)
        if self.acceptUnknown is not None:
            self.acceptUnknown.export(outfile, level, namespace_, name_='acceptUnknown', pretty_print=pretty_print)
        for format_ in self.format:
            format_.export(outfile, level, namespace_, name_='format', pretty_print=pretty_print)
        for profile_ in self.profile:
            profile_.export(outfile, level, namespace_, name_='profile', pretty_print=pretty_print)
        for rest_ in self.rest:
            rest_.export(outfile, level, namespace_, name_='rest', pretty_print=pretty_print)
        for messaging_ in self.messaging:
            messaging_.export(outfile, level, namespace_, name_='messaging', pretty_print=pretty_print)
        for document_ in self.document:
            document_.export(outfile, level, namespace_, name_='document', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Conformance', mapping_=None):
        element = super(Conformance, self).to_etree(parent_element, name_, mapping_)
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
        if self.status is not None:
            status_ = self.status
            status_.to_etree(element, name_='status', mapping_=mapping_)
        if self.experimental is not None:
            experimental_ = self.experimental
            experimental_.to_etree(element, name_='experimental', mapping_=mapping_)
        if self.date is not None:
            date_ = self.date
            date_.to_etree(element, name_='date', mapping_=mapping_)
        if self.software is not None:
            software_ = self.software
            software_.to_etree(element, name_='software', mapping_=mapping_)
        if self.implementation is not None:
            implementation_ = self.implementation
            implementation_.to_etree(element, name_='implementation', mapping_=mapping_)
        if self.fhirVersion is not None:
            fhirVersion_ = self.fhirVersion
            fhirVersion_.to_etree(element, name_='fhirVersion', mapping_=mapping_)
        if self.acceptUnknown is not None:
            acceptUnknown_ = self.acceptUnknown
            acceptUnknown_.to_etree(element, name_='acceptUnknown', mapping_=mapping_)
        for format_ in self.format:
            format_.to_etree(element, name_='format', mapping_=mapping_)
        for profile_ in self.profile:
            profile_.to_etree(element, name_='profile', mapping_=mapping_)
        for rest_ in self.rest:
            rest_.to_etree(element, name_='rest', mapping_=mapping_)
        for messaging_ in self.messaging:
            messaging_.to_etree(element, name_='messaging', mapping_=mapping_)
        for document_ in self.document:
            document_.to_etree(element, name_='document', mapping_=mapping_)
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
        super(Conformance, self).buildAttributes(node, attrs, already_processed)
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
        elif nodeName_ == 'status':
            obj_ = ConformanceStatementStatus.factory()
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
        elif nodeName_ == 'software':
            obj_ = Conformance_Software.factory()
            obj_.build(child_)
            self.software = obj_
            obj_.original_tagname_ = 'software'
        elif nodeName_ == 'implementation':
            obj_ = Conformance_Implementation.factory()
            obj_.build(child_)
            self.implementation = obj_
            obj_.original_tagname_ = 'implementation'
        elif nodeName_ == 'fhirVersion':
            obj_ = id.factory()
            obj_.build(child_)
            self.fhirVersion = obj_
            obj_.original_tagname_ = 'fhirVersion'
        elif nodeName_ == 'acceptUnknown':
            obj_ = boolean.factory()
            obj_.build(child_)
            self.acceptUnknown = obj_
            obj_.original_tagname_ = 'acceptUnknown'
        elif nodeName_ == 'format':
            obj_ = code.factory()
            obj_.build(child_)
            self.format.append(obj_)
            obj_.original_tagname_ = 'format'
        elif nodeName_ == 'profile':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.profile.append(obj_)
            obj_.original_tagname_ = 'profile'
        elif nodeName_ == 'rest':
            obj_ = Conformance_Rest.factory()
            obj_.build(child_)
            self.rest.append(obj_)
            obj_.original_tagname_ = 'rest'
        elif nodeName_ == 'messaging':
            obj_ = Conformance_Messaging.factory()
            obj_.build(child_)
            self.messaging.append(obj_)
            obj_.original_tagname_ = 'messaging'
        elif nodeName_ == 'document':
            obj_ = Conformance_Document.factory()
            obj_.build(child_)
            self.document.append(obj_)
            obj_.original_tagname_ = 'document'
        super(Conformance, self).buildChildren(child_, node, nodeName_, True)
# end class Conformance


class Conformance_Software(BackboneElement):
    """A conformance statement is a set of requirements for a desired
    implementation or a description of how a target application
    fulfills those requirements in a particular implementation."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, name=None, version=None, releaseDate=None):
        self.original_tagname_ = None
        super(Conformance_Software, self).__init__(id, extension, modifierExtension, )
        self.name = name
        self.version = version
        self.releaseDate = releaseDate
    def factory(*args_, **kwargs_):
        if Conformance_Software.subclass:
            return Conformance_Software.subclass(*args_, **kwargs_)
        else:
            return Conformance_Software(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_name(self): return self.name
    def set_name(self, name): self.name = name
    def get_version(self): return self.version
    def set_version(self, version): self.version = version
    def get_releaseDate(self): return self.releaseDate
    def set_releaseDate(self, releaseDate): self.releaseDate = releaseDate
    def hasContent_(self):
        if (
            self.name is not None or
            self.version is not None or
            self.releaseDate is not None or
            super(Conformance_Software, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Conformance.Software', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Conformance.Software')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Conformance.Software', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Conformance.Software'):
        super(Conformance_Software, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Conformance.Software')
    def exportChildren(self, outfile, level, namespace_='', name_='Conformance.Software', fromsubclass_=False, pretty_print=True):
        super(Conformance_Software, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.name is not None:
            self.name.export(outfile, level, namespace_, name_='name', pretty_print=pretty_print)
        if self.version is not None:
            self.version.export(outfile, level, namespace_, name_='version', pretty_print=pretty_print)
        if self.releaseDate is not None:
            self.releaseDate.export(outfile, level, namespace_, name_='releaseDate', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Conformance.Software', mapping_=None):
        element = super(Conformance_Software, self).to_etree(parent_element, name_, mapping_)
        if self.name is not None:
            name_ = self.name
            name_.to_etree(element, name_='name', mapping_=mapping_)
        if self.version is not None:
            version_ = self.version
            version_.to_etree(element, name_='version', mapping_=mapping_)
        if self.releaseDate is not None:
            releaseDate_ = self.releaseDate
            releaseDate_.to_etree(element, name_='releaseDate', mapping_=mapping_)
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
        super(Conformance_Software, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'name':
            obj_ = string.factory()
            obj_.build(child_)
            self.name = obj_
            obj_.original_tagname_ = 'name'
        elif nodeName_ == 'version':
            obj_ = string.factory()
            obj_.build(child_)
            self.version = obj_
            obj_.original_tagname_ = 'version'
        elif nodeName_ == 'releaseDate':
            obj_ = dateTime.factory()
            obj_.build(child_)
            self.releaseDate = obj_
            obj_.original_tagname_ = 'releaseDate'
        super(Conformance_Software, self).buildChildren(child_, node, nodeName_, True)
# end class Conformance_Software


class Conformance_Implementation(BackboneElement):
    """A conformance statement is a set of requirements for a desired
    implementation or a description of how a target application
    fulfills those requirements in a particular implementation."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, description=None, url=None):
        self.original_tagname_ = None
        super(Conformance_Implementation, self).__init__(id, extension, modifierExtension, )
        self.description = description
        self.url = url
    def factory(*args_, **kwargs_):
        if Conformance_Implementation.subclass:
            return Conformance_Implementation.subclass(*args_, **kwargs_)
        else:
            return Conformance_Implementation(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_description(self): return self.description
    def set_description(self, description): self.description = description
    def get_url(self): return self.url
    def set_url(self, url): self.url = url
    def hasContent_(self):
        if (
            self.description is not None or
            self.url is not None or
            super(Conformance_Implementation, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Conformance.Implementation', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Conformance.Implementation')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Conformance.Implementation', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Conformance.Implementation'):
        super(Conformance_Implementation, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Conformance.Implementation')
    def exportChildren(self, outfile, level, namespace_='', name_='Conformance.Implementation', fromsubclass_=False, pretty_print=True):
        super(Conformance_Implementation, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.description is not None:
            self.description.export(outfile, level, namespace_, name_='description', pretty_print=pretty_print)
        if self.url is not None:
            self.url.export(outfile, level, namespace_, name_='url', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Conformance.Implementation', mapping_=None):
        element = super(Conformance_Implementation, self).to_etree(parent_element, name_, mapping_)
        if self.description is not None:
            description_ = self.description
            description_.to_etree(element, name_='description', mapping_=mapping_)
        if self.url is not None:
            url_ = self.url
            url_.to_etree(element, name_='url', mapping_=mapping_)
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
        super(Conformance_Implementation, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'description':
            obj_ = string.factory()
            obj_.build(child_)
            self.description = obj_
            obj_.original_tagname_ = 'description'
        elif nodeName_ == 'url':
            obj_ = uri.factory()
            obj_.build(child_)
            self.url = obj_
            obj_.original_tagname_ = 'url'
        super(Conformance_Implementation, self).buildChildren(child_, node, nodeName_, True)
# end class Conformance_Implementation


class Conformance_Rest(BackboneElement):
    """A conformance statement is a set of requirements for a desired
    implementation or a description of how a target application
    fulfills those requirements in a particular implementation."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, mode=None, documentation=None, security=None, resource=None, operation=None, query=None, documentMailbox=None):
        self.original_tagname_ = None
        super(Conformance_Rest, self).__init__(id, extension, modifierExtension, )
        self.mode = mode
        self.documentation = documentation
        self.security = security
        if resource is None:
            self.resource = []
        else:
            self.resource = resource
        if operation is None:
            self.operation = []
        else:
            self.operation = operation
        if query is None:
            self.query = []
        else:
            self.query = query
        if documentMailbox is None:
            self.documentMailbox = []
        else:
            self.documentMailbox = documentMailbox
    def factory(*args_, **kwargs_):
        if Conformance_Rest.subclass:
            return Conformance_Rest.subclass(*args_, **kwargs_)
        else:
            return Conformance_Rest(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_mode(self): return self.mode
    def set_mode(self, mode): self.mode = mode
    def get_documentation(self): return self.documentation
    def set_documentation(self, documentation): self.documentation = documentation
    def get_security(self): return self.security
    def set_security(self, security): self.security = security
    def get_resource(self): return self.resource
    def set_resource(self, resource): self.resource = resource
    def add_resource(self, value): self.resource.append(value)
    def insert_resource(self, index, value): self.resource[index] = value
    def get_operation(self): return self.operation
    def set_operation(self, operation): self.operation = operation
    def add_operation(self, value): self.operation.append(value)
    def insert_operation(self, index, value): self.operation[index] = value
    def get_query(self): return self.query
    def set_query(self, query): self.query = query
    def add_query(self, value): self.query.append(value)
    def insert_query(self, index, value): self.query[index] = value
    def get_documentMailbox(self): return self.documentMailbox
    def set_documentMailbox(self, documentMailbox): self.documentMailbox = documentMailbox
    def add_documentMailbox(self, value): self.documentMailbox.append(value)
    def insert_documentMailbox(self, index, value): self.documentMailbox[index] = value
    def hasContent_(self):
        if (
            self.mode is not None or
            self.documentation is not None or
            self.security is not None or
            self.resource or
            self.operation or
            self.query or
            self.documentMailbox or
            super(Conformance_Rest, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Conformance.Rest', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Conformance.Rest')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Conformance.Rest', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Conformance.Rest'):
        super(Conformance_Rest, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Conformance.Rest')
    def exportChildren(self, outfile, level, namespace_='', name_='Conformance.Rest', fromsubclass_=False, pretty_print=True):
        super(Conformance_Rest, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.mode is not None:
            self.mode.export(outfile, level, namespace_, name_='mode', pretty_print=pretty_print)
        if self.documentation is not None:
            self.documentation.export(outfile, level, namespace_, name_='documentation', pretty_print=pretty_print)
        if self.security is not None:
            self.security.export(outfile, level, namespace_, name_='security', pretty_print=pretty_print)
        for resource_ in self.resource:
            resource_.export(outfile, level, namespace_, name_='resource', pretty_print=pretty_print)
        for operation_ in self.operation:
            operation_.export(outfile, level, namespace_, name_='operation', pretty_print=pretty_print)
        for query_ in self.query:
            query_.export(outfile, level, namespace_, name_='query', pretty_print=pretty_print)
        for documentMailbox_ in self.documentMailbox:
            documentMailbox_.export(outfile, level, namespace_, name_='documentMailbox', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Conformance.Rest', mapping_=None):
        element = super(Conformance_Rest, self).to_etree(parent_element, name_, mapping_)
        if self.mode is not None:
            mode_ = self.mode
            mode_.to_etree(element, name_='mode', mapping_=mapping_)
        if self.documentation is not None:
            documentation_ = self.documentation
            documentation_.to_etree(element, name_='documentation', mapping_=mapping_)
        if self.security is not None:
            security_ = self.security
            security_.to_etree(element, name_='security', mapping_=mapping_)
        for resource_ in self.resource:
            resource_.to_etree(element, name_='resource', mapping_=mapping_)
        for operation_ in self.operation:
            operation_.to_etree(element, name_='operation', mapping_=mapping_)
        for query_ in self.query:
            query_.to_etree(element, name_='query', mapping_=mapping_)
        for documentMailbox_ in self.documentMailbox:
            documentMailbox_.to_etree(element, name_='documentMailbox', mapping_=mapping_)
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
        super(Conformance_Rest, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'mode':
            obj_ = RestfulConformanceMode.factory()
            obj_.build(child_)
            self.mode = obj_
            obj_.original_tagname_ = 'mode'
        elif nodeName_ == 'documentation':
            obj_ = string.factory()
            obj_.build(child_)
            self.documentation = obj_
            obj_.original_tagname_ = 'documentation'
        elif nodeName_ == 'security':
            obj_ = Conformance_Security.factory()
            obj_.build(child_)
            self.security = obj_
            obj_.original_tagname_ = 'security'
        elif nodeName_ == 'resource':
            obj_ = Conformance_Resource.factory()
            obj_.build(child_)
            self.resource.append(obj_)
            obj_.original_tagname_ = 'resource'
        elif nodeName_ == 'operation':
            obj_ = Conformance_Operation1.factory()
            obj_.build(child_)
            self.operation.append(obj_)
            obj_.original_tagname_ = 'operation'
        elif nodeName_ == 'query':
            obj_ = Conformance_Query.factory()
            obj_.build(child_)
            self.query.append(obj_)
            obj_.original_tagname_ = 'query'
        elif nodeName_ == 'documentMailbox':
            obj_ = uri.factory()
            obj_.build(child_)
            self.documentMailbox.append(obj_)
            obj_.original_tagname_ = 'documentMailbox'
        super(Conformance_Rest, self).buildChildren(child_, node, nodeName_, True)
# end class Conformance_Rest


class Conformance_Security(BackboneElement):
    """A conformance statement is a set of requirements for a desired
    implementation or a description of how a target application
    fulfills those requirements in a particular implementation."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, cors=None, service=None, description=None, certificate=None):
        self.original_tagname_ = None
        super(Conformance_Security, self).__init__(id, extension, modifierExtension, )
        self.cors = cors
        if service is None:
            self.service = []
        else:
            self.service = service
        self.description = description
        if certificate is None:
            self.certificate = []
        else:
            self.certificate = certificate
    def factory(*args_, **kwargs_):
        if Conformance_Security.subclass:
            return Conformance_Security.subclass(*args_, **kwargs_)
        else:
            return Conformance_Security(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_cors(self): return self.cors
    def set_cors(self, cors): self.cors = cors
    def get_service(self): return self.service
    def set_service(self, service): self.service = service
    def add_service(self, value): self.service.append(value)
    def insert_service(self, index, value): self.service[index] = value
    def get_description(self): return self.description
    def set_description(self, description): self.description = description
    def get_certificate(self): return self.certificate
    def set_certificate(self, certificate): self.certificate = certificate
    def add_certificate(self, value): self.certificate.append(value)
    def insert_certificate(self, index, value): self.certificate[index] = value
    def hasContent_(self):
        if (
            self.cors is not None or
            self.service or
            self.description is not None or
            self.certificate or
            super(Conformance_Security, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Conformance.Security', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Conformance.Security')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Conformance.Security', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Conformance.Security'):
        super(Conformance_Security, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Conformance.Security')
    def exportChildren(self, outfile, level, namespace_='', name_='Conformance.Security', fromsubclass_=False, pretty_print=True):
        super(Conformance_Security, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.cors is not None:
            self.cors.export(outfile, level, namespace_, name_='cors', pretty_print=pretty_print)
        for service_ in self.service:
            service_.export(outfile, level, namespace_, name_='service', pretty_print=pretty_print)
        if self.description is not None:
            self.description.export(outfile, level, namespace_, name_='description', pretty_print=pretty_print)
        for certificate_ in self.certificate:
            certificate_.export(outfile, level, namespace_, name_='certificate', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Conformance.Security', mapping_=None):
        element = super(Conformance_Security, self).to_etree(parent_element, name_, mapping_)
        if self.cors is not None:
            cors_ = self.cors
            cors_.to_etree(element, name_='cors', mapping_=mapping_)
        for service_ in self.service:
            service_.to_etree(element, name_='service', mapping_=mapping_)
        if self.description is not None:
            description_ = self.description
            description_.to_etree(element, name_='description', mapping_=mapping_)
        for certificate_ in self.certificate:
            certificate_.to_etree(element, name_='certificate', mapping_=mapping_)
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
        super(Conformance_Security, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'cors':
            obj_ = boolean.factory()
            obj_.build(child_)
            self.cors = obj_
            obj_.original_tagname_ = 'cors'
        elif nodeName_ == 'service':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.service.append(obj_)
            obj_.original_tagname_ = 'service'
        elif nodeName_ == 'description':
            obj_ = string.factory()
            obj_.build(child_)
            self.description = obj_
            obj_.original_tagname_ = 'description'
        elif nodeName_ == 'certificate':
            obj_ = Conformance_Certificate.factory()
            obj_.build(child_)
            self.certificate.append(obj_)
            obj_.original_tagname_ = 'certificate'
        super(Conformance_Security, self).buildChildren(child_, node, nodeName_, True)
# end class Conformance_Security


class Conformance_Certificate(BackboneElement):
    """A conformance statement is a set of requirements for a desired
    implementation or a description of how a target application
    fulfills those requirements in a particular implementation."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, type_=None, blob=None):
        self.original_tagname_ = None
        super(Conformance_Certificate, self).__init__(id, extension, modifierExtension, )
        self.type_ = type_
        self.blob = blob
    def factory(*args_, **kwargs_):
        if Conformance_Certificate.subclass:
            return Conformance_Certificate.subclass(*args_, **kwargs_)
        else:
            return Conformance_Certificate(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_type(self): return self.type_
    def set_type(self, type_): self.type_ = type_
    def get_blob(self): return self.blob
    def set_blob(self, blob): self.blob = blob
    def hasContent_(self):
        if (
            self.type_ is not None or
            self.blob is not None or
            super(Conformance_Certificate, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Conformance.Certificate', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Conformance.Certificate')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Conformance.Certificate', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Conformance.Certificate'):
        super(Conformance_Certificate, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Conformance.Certificate')
    def exportChildren(self, outfile, level, namespace_='', name_='Conformance.Certificate', fromsubclass_=False, pretty_print=True):
        super(Conformance_Certificate, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.type_ is not None:
            self.type_.export(outfile, level, namespace_, name_='type', pretty_print=pretty_print)
        if self.blob is not None:
            self.blob.export(outfile, level, namespace_, name_='blob', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Conformance.Certificate', mapping_=None):
        element = super(Conformance_Certificate, self).to_etree(parent_element, name_, mapping_)
        if self.type_ is not None:
            type__ = self.type_
            type__.to_etree(element, name_='type', mapping_=mapping_)
        if self.blob is not None:
            blob_ = self.blob
            blob_.to_etree(element, name_='blob', mapping_=mapping_)
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
        super(Conformance_Certificate, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'type':
            obj_ = code.factory()
            obj_.build(child_)
            self.type_ = obj_
            obj_.original_tagname_ = 'type'
        elif nodeName_ == 'blob':
            obj_ = base64Binary.factory()
            obj_.build(child_)
            self.blob = obj_
            obj_.original_tagname_ = 'blob'
        super(Conformance_Certificate, self).buildChildren(child_, node, nodeName_, True)
# end class Conformance_Certificate


class Conformance_Resource(BackboneElement):
    """A conformance statement is a set of requirements for a desired
    implementation or a description of how a target application
    fulfills those requirements in a particular implementation."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, type_=None, profile=None, operation=None, readHistory=None, updateCreate=None, searchInclude=None, searchParam=None):
        self.original_tagname_ = None
        super(Conformance_Resource, self).__init__(id, extension, modifierExtension, )
        self.type_ = type_
        self.profile = profile
        if operation is None:
            self.operation = []
        else:
            self.operation = operation
        self.readHistory = readHistory
        self.updateCreate = updateCreate
        if searchInclude is None:
            self.searchInclude = []
        else:
            self.searchInclude = searchInclude
        if searchParam is None:
            self.searchParam = []
        else:
            self.searchParam = searchParam
    def factory(*args_, **kwargs_):
        if Conformance_Resource.subclass:
            return Conformance_Resource.subclass(*args_, **kwargs_)
        else:
            return Conformance_Resource(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_type(self): return self.type_
    def set_type(self, type_): self.type_ = type_
    def get_profile(self): return self.profile
    def set_profile(self, profile): self.profile = profile
    def get_operation(self): return self.operation
    def set_operation(self, operation): self.operation = operation
    def add_operation(self, value): self.operation.append(value)
    def insert_operation(self, index, value): self.operation[index] = value
    def get_readHistory(self): return self.readHistory
    def set_readHistory(self, readHistory): self.readHistory = readHistory
    def get_updateCreate(self): return self.updateCreate
    def set_updateCreate(self, updateCreate): self.updateCreate = updateCreate
    def get_searchInclude(self): return self.searchInclude
    def set_searchInclude(self, searchInclude): self.searchInclude = searchInclude
    def add_searchInclude(self, value): self.searchInclude.append(value)
    def insert_searchInclude(self, index, value): self.searchInclude[index] = value
    def get_searchParam(self): return self.searchParam
    def set_searchParam(self, searchParam): self.searchParam = searchParam
    def add_searchParam(self, value): self.searchParam.append(value)
    def insert_searchParam(self, index, value): self.searchParam[index] = value
    def hasContent_(self):
        if (
            self.type_ is not None or
            self.profile is not None or
            self.operation or
            self.readHistory is not None or
            self.updateCreate is not None or
            self.searchInclude or
            self.searchParam or
            super(Conformance_Resource, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Conformance.Resource', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Conformance.Resource')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Conformance.Resource', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Conformance.Resource'):
        super(Conformance_Resource, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Conformance.Resource')
    def exportChildren(self, outfile, level, namespace_='', name_='Conformance.Resource', fromsubclass_=False, pretty_print=True):
        super(Conformance_Resource, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.type_ is not None:
            self.type_.export(outfile, level, namespace_, name_='type', pretty_print=pretty_print)
        if self.profile is not None:
            self.profile.export(outfile, level, namespace_, name_='profile', pretty_print=pretty_print)
        for operation_ in self.operation:
            operation_.export(outfile, level, namespace_, name_='operation', pretty_print=pretty_print)
        if self.readHistory is not None:
            self.readHistory.export(outfile, level, namespace_, name_='readHistory', pretty_print=pretty_print)
        if self.updateCreate is not None:
            self.updateCreate.export(outfile, level, namespace_, name_='updateCreate', pretty_print=pretty_print)
        for searchInclude_ in self.searchInclude:
            searchInclude_.export(outfile, level, namespace_, name_='searchInclude', pretty_print=pretty_print)
        for searchParam_ in self.searchParam:
            searchParam_.export(outfile, level, namespace_, name_='searchParam', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Conformance.Resource', mapping_=None):
        element = super(Conformance_Resource, self).to_etree(parent_element, name_, mapping_)
        if self.type_ is not None:
            type__ = self.type_
            type__.to_etree(element, name_='type', mapping_=mapping_)
        if self.profile is not None:
            profile_ = self.profile
            profile_.to_etree(element, name_='profile', mapping_=mapping_)
        for operation_ in self.operation:
            operation_.to_etree(element, name_='operation', mapping_=mapping_)
        if self.readHistory is not None:
            readHistory_ = self.readHistory
            readHistory_.to_etree(element, name_='readHistory', mapping_=mapping_)
        if self.updateCreate is not None:
            updateCreate_ = self.updateCreate
            updateCreate_.to_etree(element, name_='updateCreate', mapping_=mapping_)
        for searchInclude_ in self.searchInclude:
            searchInclude_.to_etree(element, name_='searchInclude', mapping_=mapping_)
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
        super(Conformance_Resource, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'type':
            obj_ = code.factory()
            obj_.build(child_)
            self.type_ = obj_
            obj_.original_tagname_ = 'type'
        elif nodeName_ == 'profile':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.profile = obj_
            obj_.original_tagname_ = 'profile'
        elif nodeName_ == 'operation':
            obj_ = Conformance_Operation.factory()
            obj_.build(child_)
            self.operation.append(obj_)
            obj_.original_tagname_ = 'operation'
        elif nodeName_ == 'readHistory':
            obj_ = boolean.factory()
            obj_.build(child_)
            self.readHistory = obj_
            obj_.original_tagname_ = 'readHistory'
        elif nodeName_ == 'updateCreate':
            obj_ = boolean.factory()
            obj_.build(child_)
            self.updateCreate = obj_
            obj_.original_tagname_ = 'updateCreate'
        elif nodeName_ == 'searchInclude':
            obj_ = string.factory()
            obj_.build(child_)
            self.searchInclude.append(obj_)
            obj_.original_tagname_ = 'searchInclude'
        elif nodeName_ == 'searchParam':
            obj_ = Conformance_SearchParam.factory()
            obj_.build(child_)
            self.searchParam.append(obj_)
            obj_.original_tagname_ = 'searchParam'
        super(Conformance_Resource, self).buildChildren(child_, node, nodeName_, True)
# end class Conformance_Resource


class Conformance_Operation(BackboneElement):
    """A conformance statement is a set of requirements for a desired
    implementation or a description of how a target application
    fulfills those requirements in a particular implementation."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, code=None, documentation=None):
        self.original_tagname_ = None
        super(Conformance_Operation, self).__init__(id, extension, modifierExtension, )
        self.code = code
        self.documentation = documentation
    def factory(*args_, **kwargs_):
        if Conformance_Operation.subclass:
            return Conformance_Operation.subclass(*args_, **kwargs_)
        else:
            return Conformance_Operation(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_code(self): return self.code
    def set_code(self, code): self.code = code
    def get_documentation(self): return self.documentation
    def set_documentation(self, documentation): self.documentation = documentation
    def hasContent_(self):
        if (
            self.code is not None or
            self.documentation is not None or
            super(Conformance_Operation, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Conformance.Operation', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Conformance.Operation')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Conformance.Operation', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Conformance.Operation'):
        super(Conformance_Operation, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Conformance.Operation')
    def exportChildren(self, outfile, level, namespace_='', name_='Conformance.Operation', fromsubclass_=False, pretty_print=True):
        super(Conformance_Operation, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.code is not None:
            self.code.export(outfile, level, namespace_, name_='code', pretty_print=pretty_print)
        if self.documentation is not None:
            self.documentation.export(outfile, level, namespace_, name_='documentation', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Conformance.Operation', mapping_=None):
        element = super(Conformance_Operation, self).to_etree(parent_element, name_, mapping_)
        if self.code is not None:
            code_ = self.code
            code_.to_etree(element, name_='code', mapping_=mapping_)
        if self.documentation is not None:
            documentation_ = self.documentation
            documentation_.to_etree(element, name_='documentation', mapping_=mapping_)
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
        super(Conformance_Operation, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'code':
            obj_ = RestfulOperationType.factory()
            obj_.build(child_)
            self.code = obj_
            obj_.original_tagname_ = 'code'
        elif nodeName_ == 'documentation':
            obj_ = string.factory()
            obj_.build(child_)
            self.documentation = obj_
            obj_.original_tagname_ = 'documentation'
        super(Conformance_Operation, self).buildChildren(child_, node, nodeName_, True)
# end class Conformance_Operation


class Conformance_SearchParam(BackboneElement):
    """A conformance statement is a set of requirements for a desired
    implementation or a description of how a target application
    fulfills those requirements in a particular implementation."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, name=None, definition=None, type_=None, documentation=None, target=None, chain=None):
        self.original_tagname_ = None
        super(Conformance_SearchParam, self).__init__(id, extension, modifierExtension, )
        self.name = name
        self.definition = definition
        self.type_ = type_
        self.documentation = documentation
        if target is None:
            self.target = []
        else:
            self.target = target
        if chain is None:
            self.chain = []
        else:
            self.chain = chain
    def factory(*args_, **kwargs_):
        if Conformance_SearchParam.subclass:
            return Conformance_SearchParam.subclass(*args_, **kwargs_)
        else:
            return Conformance_SearchParam(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_name(self): return self.name
    def set_name(self, name): self.name = name
    def get_definition(self): return self.definition
    def set_definition(self, definition): self.definition = definition
    def get_type(self): return self.type_
    def set_type(self, type_): self.type_ = type_
    def get_documentation(self): return self.documentation
    def set_documentation(self, documentation): self.documentation = documentation
    def get_target(self): return self.target
    def set_target(self, target): self.target = target
    def add_target(self, value): self.target.append(value)
    def insert_target(self, index, value): self.target[index] = value
    def get_chain(self): return self.chain
    def set_chain(self, chain): self.chain = chain
    def add_chain(self, value): self.chain.append(value)
    def insert_chain(self, index, value): self.chain[index] = value
    def hasContent_(self):
        if (
            self.name is not None or
            self.definition is not None or
            self.type_ is not None or
            self.documentation is not None or
            self.target or
            self.chain or
            super(Conformance_SearchParam, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Conformance.SearchParam', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Conformance.SearchParam')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Conformance.SearchParam', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Conformance.SearchParam'):
        super(Conformance_SearchParam, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Conformance.SearchParam')
    def exportChildren(self, outfile, level, namespace_='', name_='Conformance.SearchParam', fromsubclass_=False, pretty_print=True):
        super(Conformance_SearchParam, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.name is not None:
            self.name.export(outfile, level, namespace_, name_='name', pretty_print=pretty_print)
        if self.definition is not None:
            self.definition.export(outfile, level, namespace_, name_='definition', pretty_print=pretty_print)
        if self.type_ is not None:
            self.type_.export(outfile, level, namespace_, name_='type', pretty_print=pretty_print)
        if self.documentation is not None:
            self.documentation.export(outfile, level, namespace_, name_='documentation', pretty_print=pretty_print)
        for target_ in self.target:
            target_.export(outfile, level, namespace_, name_='target', pretty_print=pretty_print)
        for chain_ in self.chain:
            chain_.export(outfile, level, namespace_, name_='chain', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Conformance.SearchParam', mapping_=None):
        element = super(Conformance_SearchParam, self).to_etree(parent_element, name_, mapping_)
        if self.name is not None:
            name_ = self.name
            name_.to_etree(element, name_='name', mapping_=mapping_)
        if self.definition is not None:
            definition_ = self.definition
            definition_.to_etree(element, name_='definition', mapping_=mapping_)
        if self.type_ is not None:
            type__ = self.type_
            type__.to_etree(element, name_='type', mapping_=mapping_)
        if self.documentation is not None:
            documentation_ = self.documentation
            documentation_.to_etree(element, name_='documentation', mapping_=mapping_)
        for target_ in self.target:
            target_.to_etree(element, name_='target', mapping_=mapping_)
        for chain_ in self.chain:
            chain_.to_etree(element, name_='chain', mapping_=mapping_)
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
        super(Conformance_SearchParam, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'name':
            obj_ = string.factory()
            obj_.build(child_)
            self.name = obj_
            obj_.original_tagname_ = 'name'
        elif nodeName_ == 'definition':
            obj_ = uri.factory()
            obj_.build(child_)
            self.definition = obj_
            obj_.original_tagname_ = 'definition'
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
        elif nodeName_ == 'target':
            obj_ = code.factory()
            obj_.build(child_)
            self.target.append(obj_)
            obj_.original_tagname_ = 'target'
        elif nodeName_ == 'chain':
            obj_ = string.factory()
            obj_.build(child_)
            self.chain.append(obj_)
            obj_.original_tagname_ = 'chain'
        super(Conformance_SearchParam, self).buildChildren(child_, node, nodeName_, True)
# end class Conformance_SearchParam


class Conformance_Operation1(BackboneElement):
    """A conformance statement is a set of requirements for a desired
    implementation or a description of how a target application
    fulfills those requirements in a particular implementation."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, code=None, documentation=None):
        self.original_tagname_ = None
        super(Conformance_Operation1, self).__init__(id, extension, modifierExtension, )
        self.code = code
        self.documentation = documentation
    def factory(*args_, **kwargs_):
        if Conformance_Operation1.subclass:
            return Conformance_Operation1.subclass(*args_, **kwargs_)
        else:
            return Conformance_Operation1(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_code(self): return self.code
    def set_code(self, code): self.code = code
    def get_documentation(self): return self.documentation
    def set_documentation(self, documentation): self.documentation = documentation
    def hasContent_(self):
        if (
            self.code is not None or
            self.documentation is not None or
            super(Conformance_Operation1, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Conformance.Operation1', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Conformance.Operation1')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Conformance.Operation1', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Conformance.Operation1'):
        super(Conformance_Operation1, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Conformance.Operation1')
    def exportChildren(self, outfile, level, namespace_='', name_='Conformance.Operation1', fromsubclass_=False, pretty_print=True):
        super(Conformance_Operation1, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.code is not None:
            self.code.export(outfile, level, namespace_, name_='code', pretty_print=pretty_print)
        if self.documentation is not None:
            self.documentation.export(outfile, level, namespace_, name_='documentation', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Conformance.Operation1', mapping_=None):
        element = super(Conformance_Operation1, self).to_etree(parent_element, name_, mapping_)
        if self.code is not None:
            code_ = self.code
            code_.to_etree(element, name_='code', mapping_=mapping_)
        if self.documentation is not None:
            documentation_ = self.documentation
            documentation_.to_etree(element, name_='documentation', mapping_=mapping_)
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
        super(Conformance_Operation1, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'code':
            obj_ = RestfulOperationSystem.factory()
            obj_.build(child_)
            self.code = obj_
            obj_.original_tagname_ = 'code'
        elif nodeName_ == 'documentation':
            obj_ = string.factory()
            obj_.build(child_)
            self.documentation = obj_
            obj_.original_tagname_ = 'documentation'
        super(Conformance_Operation1, self).buildChildren(child_, node, nodeName_, True)
# end class Conformance_Operation1


class Conformance_Query(BackboneElement):
    """A conformance statement is a set of requirements for a desired
    implementation or a description of how a target application
    fulfills those requirements in a particular implementation."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, name=None, definition=None, documentation=None, parameter=None):
        self.original_tagname_ = None
        super(Conformance_Query, self).__init__(id, extension, modifierExtension, )
        self.name = name
        self.definition = definition
        self.documentation = documentation
        if parameter is None:
            self.parameter = []
        else:
            self.parameter = parameter
    def factory(*args_, **kwargs_):
        if Conformance_Query.subclass:
            return Conformance_Query.subclass(*args_, **kwargs_)
        else:
            return Conformance_Query(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_name(self): return self.name
    def set_name(self, name): self.name = name
    def get_definition(self): return self.definition
    def set_definition(self, definition): self.definition = definition
    def get_documentation(self): return self.documentation
    def set_documentation(self, documentation): self.documentation = documentation
    def get_parameter(self): return self.parameter
    def set_parameter(self, parameter): self.parameter = parameter
    def add_parameter(self, value): self.parameter.append(value)
    def insert_parameter(self, index, value): self.parameter[index] = value
    def hasContent_(self):
        if (
            self.name is not None or
            self.definition is not None or
            self.documentation is not None or
            self.parameter or
            super(Conformance_Query, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Conformance.Query', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Conformance.Query')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Conformance.Query', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Conformance.Query'):
        super(Conformance_Query, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Conformance.Query')
    def exportChildren(self, outfile, level, namespace_='', name_='Conformance.Query', fromsubclass_=False, pretty_print=True):
        super(Conformance_Query, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.name is not None:
            self.name.export(outfile, level, namespace_, name_='name', pretty_print=pretty_print)
        if self.definition is not None:
            self.definition.export(outfile, level, namespace_, name_='definition', pretty_print=pretty_print)
        if self.documentation is not None:
            self.documentation.export(outfile, level, namespace_, name_='documentation', pretty_print=pretty_print)
        for parameter_ in self.parameter:
            parameter_.export(outfile, level, namespace_, name_='parameter', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Conformance.Query', mapping_=None):
        element = super(Conformance_Query, self).to_etree(parent_element, name_, mapping_)
        if self.name is not None:
            name_ = self.name
            name_.to_etree(element, name_='name', mapping_=mapping_)
        if self.definition is not None:
            definition_ = self.definition
            definition_.to_etree(element, name_='definition', mapping_=mapping_)
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
        super(Conformance_Query, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'name':
            obj_ = string.factory()
            obj_.build(child_)
            self.name = obj_
            obj_.original_tagname_ = 'name'
        elif nodeName_ == 'definition':
            obj_ = uri.factory()
            obj_.build(child_)
            self.definition = obj_
            obj_.original_tagname_ = 'definition'
        elif nodeName_ == 'documentation':
            obj_ = string.factory()
            obj_.build(child_)
            self.documentation = obj_
            obj_.original_tagname_ = 'documentation'
        elif nodeName_ == 'parameter':
            obj_ = Conformance_SearchParam.factory()
            obj_.build(child_)
            self.parameter.append(obj_)
            obj_.original_tagname_ = 'parameter'
        super(Conformance_Query, self).buildChildren(child_, node, nodeName_, True)
# end class Conformance_Query


class Conformance_Messaging(BackboneElement):
    """A conformance statement is a set of requirements for a desired
    implementation or a description of how a target application
    fulfills those requirements in a particular implementation."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, endpoint=None, reliableCache=None, documentation=None, event=None):
        self.original_tagname_ = None
        super(Conformance_Messaging, self).__init__(id, extension, modifierExtension, )
        self.endpoint = endpoint
        self.reliableCache = reliableCache
        self.documentation = documentation
        if event is None:
            self.event = []
        else:
            self.event = event
    def factory(*args_, **kwargs_):
        if Conformance_Messaging.subclass:
            return Conformance_Messaging.subclass(*args_, **kwargs_)
        else:
            return Conformance_Messaging(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_endpoint(self): return self.endpoint
    def set_endpoint(self, endpoint): self.endpoint = endpoint
    def get_reliableCache(self): return self.reliableCache
    def set_reliableCache(self, reliableCache): self.reliableCache = reliableCache
    def get_documentation(self): return self.documentation
    def set_documentation(self, documentation): self.documentation = documentation
    def get_event(self): return self.event
    def set_event(self, event): self.event = event
    def add_event(self, value): self.event.append(value)
    def insert_event(self, index, value): self.event[index] = value
    def hasContent_(self):
        if (
            self.endpoint is not None or
            self.reliableCache is not None or
            self.documentation is not None or
            self.event or
            super(Conformance_Messaging, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Conformance.Messaging', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Conformance.Messaging')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Conformance.Messaging', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Conformance.Messaging'):
        super(Conformance_Messaging, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Conformance.Messaging')
    def exportChildren(self, outfile, level, namespace_='', name_='Conformance.Messaging', fromsubclass_=False, pretty_print=True):
        super(Conformance_Messaging, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.endpoint is not None:
            self.endpoint.export(outfile, level, namespace_, name_='endpoint', pretty_print=pretty_print)
        if self.reliableCache is not None:
            self.reliableCache.export(outfile, level, namespace_, name_='reliableCache', pretty_print=pretty_print)
        if self.documentation is not None:
            self.documentation.export(outfile, level, namespace_, name_='documentation', pretty_print=pretty_print)
        for event_ in self.event:
            event_.export(outfile, level, namespace_, name_='event', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Conformance.Messaging', mapping_=None):
        element = super(Conformance_Messaging, self).to_etree(parent_element, name_, mapping_)
        if self.endpoint is not None:
            endpoint_ = self.endpoint
            endpoint_.to_etree(element, name_='endpoint', mapping_=mapping_)
        if self.reliableCache is not None:
            reliableCache_ = self.reliableCache
            reliableCache_.to_etree(element, name_='reliableCache', mapping_=mapping_)
        if self.documentation is not None:
            documentation_ = self.documentation
            documentation_.to_etree(element, name_='documentation', mapping_=mapping_)
        for event_ in self.event:
            event_.to_etree(element, name_='event', mapping_=mapping_)
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
        super(Conformance_Messaging, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'endpoint':
            obj_ = uri.factory()
            obj_.build(child_)
            self.endpoint = obj_
            obj_.original_tagname_ = 'endpoint'
        elif nodeName_ == 'reliableCache':
            obj_ = integer.factory()
            obj_.build(child_)
            self.reliableCache = obj_
            obj_.original_tagname_ = 'reliableCache'
        elif nodeName_ == 'documentation':
            obj_ = string.factory()
            obj_.build(child_)
            self.documentation = obj_
            obj_.original_tagname_ = 'documentation'
        elif nodeName_ == 'event':
            obj_ = Conformance_Event.factory()
            obj_.build(child_)
            self.event.append(obj_)
            obj_.original_tagname_ = 'event'
        super(Conformance_Messaging, self).buildChildren(child_, node, nodeName_, True)
# end class Conformance_Messaging


class Conformance_Event(BackboneElement):
    """A conformance statement is a set of requirements for a desired
    implementation or a description of how a target application
    fulfills those requirements in a particular implementation."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, code=None, category=None, mode=None, protocol=None, focus=None, request=None, response=None, documentation=None):
        self.original_tagname_ = None
        super(Conformance_Event, self).__init__(id, extension, modifierExtension, )
        self.code = code
        self.category = category
        self.mode = mode
        if protocol is None:
            self.protocol = []
        else:
            self.protocol = protocol
        self.focus = focus
        self.request = request
        self.response = response
        self.documentation = documentation
    def factory(*args_, **kwargs_):
        if Conformance_Event.subclass:
            return Conformance_Event.subclass(*args_, **kwargs_)
        else:
            return Conformance_Event(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_code(self): return self.code
    def set_code(self, code): self.code = code
    def get_category(self): return self.category
    def set_category(self, category): self.category = category
    def get_mode(self): return self.mode
    def set_mode(self, mode): self.mode = mode
    def get_protocol(self): return self.protocol
    def set_protocol(self, protocol): self.protocol = protocol
    def add_protocol(self, value): self.protocol.append(value)
    def insert_protocol(self, index, value): self.protocol[index] = value
    def get_focus(self): return self.focus
    def set_focus(self, focus): self.focus = focus
    def get_request(self): return self.request
    def set_request(self, request): self.request = request
    def get_response(self): return self.response
    def set_response(self, response): self.response = response
    def get_documentation(self): return self.documentation
    def set_documentation(self, documentation): self.documentation = documentation
    def hasContent_(self):
        if (
            self.code is not None or
            self.category is not None or
            self.mode is not None or
            self.protocol or
            self.focus is not None or
            self.request is not None or
            self.response is not None or
            self.documentation is not None or
            super(Conformance_Event, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Conformance.Event', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Conformance.Event')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Conformance.Event', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Conformance.Event'):
        super(Conformance_Event, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Conformance.Event')
    def exportChildren(self, outfile, level, namespace_='', name_='Conformance.Event', fromsubclass_=False, pretty_print=True):
        super(Conformance_Event, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.code is not None:
            self.code.export(outfile, level, namespace_, name_='code', pretty_print=pretty_print)
        if self.category is not None:
            self.category.export(outfile, level, namespace_, name_='category', pretty_print=pretty_print)
        if self.mode is not None:
            self.mode.export(outfile, level, namespace_, name_='mode', pretty_print=pretty_print)
        for protocol_ in self.protocol:
            protocol_.export(outfile, level, namespace_, name_='protocol', pretty_print=pretty_print)
        if self.focus is not None:
            self.focus.export(outfile, level, namespace_, name_='focus', pretty_print=pretty_print)
        if self.request is not None:
            self.request.export(outfile, level, namespace_, name_='request', pretty_print=pretty_print)
        if self.response is not None:
            self.response.export(outfile, level, namespace_, name_='response', pretty_print=pretty_print)
        if self.documentation is not None:
            self.documentation.export(outfile, level, namespace_, name_='documentation', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Conformance.Event', mapping_=None):
        element = super(Conformance_Event, self).to_etree(parent_element, name_, mapping_)
        if self.code is not None:
            code_ = self.code
            code_.to_etree(element, name_='code', mapping_=mapping_)
        if self.category is not None:
            category_ = self.category
            category_.to_etree(element, name_='category', mapping_=mapping_)
        if self.mode is not None:
            mode_ = self.mode
            mode_.to_etree(element, name_='mode', mapping_=mapping_)
        for protocol_ in self.protocol:
            protocol_.to_etree(element, name_='protocol', mapping_=mapping_)
        if self.focus is not None:
            focus_ = self.focus
            focus_.to_etree(element, name_='focus', mapping_=mapping_)
        if self.request is not None:
            request_ = self.request
            request_.to_etree(element, name_='request', mapping_=mapping_)
        if self.response is not None:
            response_ = self.response
            response_.to_etree(element, name_='response', mapping_=mapping_)
        if self.documentation is not None:
            documentation_ = self.documentation
            documentation_.to_etree(element, name_='documentation', mapping_=mapping_)
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
        super(Conformance_Event, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'code':
            obj_ = Coding.factory()
            obj_.build(child_)
            self.code = obj_
            obj_.original_tagname_ = 'code'
        elif nodeName_ == 'category':
            obj_ = MessageSignificanceCategory.factory()
            obj_.build(child_)
            self.category = obj_
            obj_.original_tagname_ = 'category'
        elif nodeName_ == 'mode':
            obj_ = ConformanceEventMode.factory()
            obj_.build(child_)
            self.mode = obj_
            obj_.original_tagname_ = 'mode'
        elif nodeName_ == 'protocol':
            obj_ = Coding.factory()
            obj_.build(child_)
            self.protocol.append(obj_)
            obj_.original_tagname_ = 'protocol'
        elif nodeName_ == 'focus':
            obj_ = code.factory()
            obj_.build(child_)
            self.focus = obj_
            obj_.original_tagname_ = 'focus'
        elif nodeName_ == 'request':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.request = obj_
            obj_.original_tagname_ = 'request'
        elif nodeName_ == 'response':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.response = obj_
            obj_.original_tagname_ = 'response'
        elif nodeName_ == 'documentation':
            obj_ = string.factory()
            obj_.build(child_)
            self.documentation = obj_
            obj_.original_tagname_ = 'documentation'
        super(Conformance_Event, self).buildChildren(child_, node, nodeName_, True)
# end class Conformance_Event


class Conformance_Document(BackboneElement):
    """A conformance statement is a set of requirements for a desired
    implementation or a description of how a target application
    fulfills those requirements in a particular implementation."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, mode=None, documentation=None, profile=None):
        self.original_tagname_ = None
        super(Conformance_Document, self).__init__(id, extension, modifierExtension, )
        self.mode = mode
        self.documentation = documentation
        self.profile = profile
    def factory(*args_, **kwargs_):
        if Conformance_Document.subclass:
            return Conformance_Document.subclass(*args_, **kwargs_)
        else:
            return Conformance_Document(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_mode(self): return self.mode
    def set_mode(self, mode): self.mode = mode
    def get_documentation(self): return self.documentation
    def set_documentation(self, documentation): self.documentation = documentation
    def get_profile(self): return self.profile
    def set_profile(self, profile): self.profile = profile
    def hasContent_(self):
        if (
            self.mode is not None or
            self.documentation is not None or
            self.profile is not None or
            super(Conformance_Document, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Conformance.Document', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Conformance.Document')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Conformance.Document', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Conformance.Document'):
        super(Conformance_Document, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Conformance.Document')
    def exportChildren(self, outfile, level, namespace_='', name_='Conformance.Document', fromsubclass_=False, pretty_print=True):
        super(Conformance_Document, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.mode is not None:
            self.mode.export(outfile, level, namespace_, name_='mode', pretty_print=pretty_print)
        if self.documentation is not None:
            self.documentation.export(outfile, level, namespace_, name_='documentation', pretty_print=pretty_print)
        if self.profile is not None:
            self.profile.export(outfile, level, namespace_, name_='profile', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Conformance.Document', mapping_=None):
        element = super(Conformance_Document, self).to_etree(parent_element, name_, mapping_)
        if self.mode is not None:
            mode_ = self.mode
            mode_.to_etree(element, name_='mode', mapping_=mapping_)
        if self.documentation is not None:
            documentation_ = self.documentation
            documentation_.to_etree(element, name_='documentation', mapping_=mapping_)
        if self.profile is not None:
            profile_ = self.profile
            profile_.to_etree(element, name_='profile', mapping_=mapping_)
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
        super(Conformance_Document, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'mode':
            obj_ = DocumentMode.factory()
            obj_.build(child_)
            self.mode = obj_
            obj_.original_tagname_ = 'mode'
        elif nodeName_ == 'documentation':
            obj_ = string.factory()
            obj_.build(child_)
            self.documentation = obj_
            obj_.original_tagname_ = 'documentation'
        elif nodeName_ == 'profile':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.profile = obj_
            obj_.original_tagname_ = 'profile'
        super(Conformance_Document, self).buildChildren(child_, node, nodeName_, True)
# end class Conformance_Document


class ConformanceStatementStatus(Element):
    """The status of this conformance statementIf the element is present,
    it must have either a @value, an @id, or extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(ConformanceStatementStatus, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if ConformanceStatementStatus.subclass:
            return ConformanceStatementStatus.subclass(*args_, **kwargs_)
        else:
            return ConformanceStatementStatus(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(ConformanceStatementStatus, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='ConformanceStatementStatus', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ConformanceStatementStatus')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='ConformanceStatementStatus', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='ConformanceStatementStatus'):
        super(ConformanceStatementStatus, self).exportAttributes(outfile, level, already_processed, namespace_, name_='ConformanceStatementStatus')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='ConformanceStatementStatus', fromsubclass_=False, pretty_print=True):
        super(ConformanceStatementStatus, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='ConformanceStatementStatus', mapping_=None):
        element = super(ConformanceStatementStatus, self).to_etree(parent_element, name_, mapping_)
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
        super(ConformanceStatementStatus, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(ConformanceStatementStatus, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class ConformanceStatementStatus


class ConformanceEventMode(Element):
    """The mode of a message conformance statementIf the element is
    present, it must have either a @value, an @id, or extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(ConformanceEventMode, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if ConformanceEventMode.subclass:
            return ConformanceEventMode.subclass(*args_, **kwargs_)
        else:
            return ConformanceEventMode(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(ConformanceEventMode, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='ConformanceEventMode', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ConformanceEventMode')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='ConformanceEventMode', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='ConformanceEventMode'):
        super(ConformanceEventMode, self).exportAttributes(outfile, level, already_processed, namespace_, name_='ConformanceEventMode')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='ConformanceEventMode', fromsubclass_=False, pretty_print=True):
        super(ConformanceEventMode, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='ConformanceEventMode', mapping_=None):
        element = super(ConformanceEventMode, self).to_etree(parent_element, name_, mapping_)
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
        super(ConformanceEventMode, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(ConformanceEventMode, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class ConformanceEventMode


class RestfulConformanceMode(Element):
    """The mode of a RESTful conformance statementIf the element is
    present, it must have either a @value, an @id, or extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(RestfulConformanceMode, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if RestfulConformanceMode.subclass:
            return RestfulConformanceMode.subclass(*args_, **kwargs_)
        else:
            return RestfulConformanceMode(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(RestfulConformanceMode, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='RestfulConformanceMode', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='RestfulConformanceMode')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='RestfulConformanceMode', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='RestfulConformanceMode'):
        super(RestfulConformanceMode, self).exportAttributes(outfile, level, already_processed, namespace_, name_='RestfulConformanceMode')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='RestfulConformanceMode', fromsubclass_=False, pretty_print=True):
        super(RestfulConformanceMode, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='RestfulConformanceMode', mapping_=None):
        element = super(RestfulConformanceMode, self).to_etree(parent_element, name_, mapping_)
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
        super(RestfulConformanceMode, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(RestfulConformanceMode, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class RestfulConformanceMode


class RestfulOperationSystem(Element):
    """Operations supported by REST at the system levelIf the element is
    present, it must have either a @value, an @id, or extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(RestfulOperationSystem, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if RestfulOperationSystem.subclass:
            return RestfulOperationSystem.subclass(*args_, **kwargs_)
        else:
            return RestfulOperationSystem(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(RestfulOperationSystem, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='RestfulOperationSystem', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='RestfulOperationSystem')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='RestfulOperationSystem', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='RestfulOperationSystem'):
        super(RestfulOperationSystem, self).exportAttributes(outfile, level, already_processed, namespace_, name_='RestfulOperationSystem')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='RestfulOperationSystem', fromsubclass_=False, pretty_print=True):
        super(RestfulOperationSystem, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='RestfulOperationSystem', mapping_=None):
        element = super(RestfulOperationSystem, self).to_etree(parent_element, name_, mapping_)
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
        super(RestfulOperationSystem, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(RestfulOperationSystem, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class RestfulOperationSystem


class RestfulOperationType(Element):
    """Operations supported by REST at the type or instance levelIf the
    element is present, it must have either a @value, an @id, or
    extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(RestfulOperationType, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if RestfulOperationType.subclass:
            return RestfulOperationType.subclass(*args_, **kwargs_)
        else:
            return RestfulOperationType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(RestfulOperationType, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='RestfulOperationType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='RestfulOperationType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='RestfulOperationType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='RestfulOperationType'):
        super(RestfulOperationType, self).exportAttributes(outfile, level, already_processed, namespace_, name_='RestfulOperationType')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='RestfulOperationType', fromsubclass_=False, pretty_print=True):
        super(RestfulOperationType, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='RestfulOperationType', mapping_=None):
        element = super(RestfulOperationType, self).to_etree(parent_element, name_, mapping_)
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
        super(RestfulOperationType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(RestfulOperationType, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class RestfulOperationType


class SearchParamType(Element):
    """If the element is present, it must have either a @value, an @id, or
    extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(SearchParamType, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if SearchParamType.subclass:
            return SearchParamType.subclass(*args_, **kwargs_)
        else:
            return SearchParamType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(SearchParamType, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='SearchParamType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='SearchParamType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='SearchParamType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='SearchParamType'):
        super(SearchParamType, self).exportAttributes(outfile, level, already_processed, namespace_, name_='SearchParamType')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='SearchParamType', fromsubclass_=False, pretty_print=True):
        super(SearchParamType, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='SearchParamType', mapping_=None):
        element = super(SearchParamType, self).to_etree(parent_element, name_, mapping_)
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
        super(SearchParamType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(SearchParamType, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class SearchParamType


class DocumentMode(Element):
    """Whether the application produces or consumes documentsIf the element
    is present, it must have either a @value, an @id, or extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(DocumentMode, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if DocumentMode.subclass:
            return DocumentMode.subclass(*args_, **kwargs_)
        else:
            return DocumentMode(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(DocumentMode, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='DocumentMode', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='DocumentMode')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='DocumentMode', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='DocumentMode'):
        super(DocumentMode, self).exportAttributes(outfile, level, already_processed, namespace_, name_='DocumentMode')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='DocumentMode', fromsubclass_=False, pretty_print=True):
        super(DocumentMode, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='DocumentMode', mapping_=None):
        element = super(DocumentMode, self).to_etree(parent_element, name_, mapping_)
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
        super(DocumentMode, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(DocumentMode, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class DocumentMode
