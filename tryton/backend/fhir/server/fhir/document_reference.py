from .base_classes import *
from .support_functions import *


class DocumentReference(Resource):
    """A reference to a document.If the element is present, it must have
    either a @value, an @id, or extensions"""
    subclass = None
    superclass = Resource
    def __init__(self, id=None, extension=None, modifierExtension=None, language=None, text=None, contained=None, masterIdentifier=None, identifier=None, subject=None, type_=None, class_=None, author=None, custodian=None, policyManager=None, authenticator=None, created=None, indexed=None, status=None, docStatus=None, relatesTo=None, description=None, confidentiality=None, primaryLanguage=None, mimeType=None, format=None, size=None, hash=None, location=None, service=None, context=None):
        self.original_tagname_ = None
        super(DocumentReference, self).__init__(id, extension, modifierExtension, language, text, contained, )
        self.masterIdentifier = masterIdentifier
        if identifier is None:
            self.identifier = []
        else:
            self.identifier = identifier
        self.subject = subject
        self.type_ = type_
        self.class_ = class_
        if author is None:
            self.author = []
        else:
            self.author = author
        self.custodian = custodian
        self.policyManager = policyManager
        self.authenticator = authenticator
        self.created = created
        self.indexed = indexed
        self.status = status
        self.docStatus = docStatus
        if relatesTo is None:
            self.relatesTo = []
        else:
            self.relatesTo = relatesTo
        self.description = description
        if confidentiality is None:
            self.confidentiality = []
        else:
            self.confidentiality = confidentiality
        self.primaryLanguage = primaryLanguage
        self.mimeType = mimeType
        if format is None:
            self.format = []
        else:
            self.format = format
        self.size = size
        self.hash = hash
        self.location = location
        self.service = service
        self.context = context
    def factory(*args_, **kwargs_):
        if DocumentReference.subclass:
            return DocumentReference.subclass(*args_, **kwargs_)
        else:
            return DocumentReference(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_masterIdentifier(self): return self.masterIdentifier
    def set_masterIdentifier(self, masterIdentifier): self.masterIdentifier = masterIdentifier
    def get_identifier(self): return self.identifier
    def set_identifier(self, identifier): self.identifier = identifier
    def add_identifier(self, value): self.identifier.append(value)
    def insert_identifier(self, index, value): self.identifier[index] = value
    def get_subject(self): return self.subject
    def set_subject(self, subject): self.subject = subject
    def get_type(self): return self.type_
    def set_type(self, type_): self.type_ = type_
    def get_class(self): return self.class_
    def set_class(self, class_): self.class_ = class_
    def get_author(self): return self.author
    def set_author(self, author): self.author = author
    def add_author(self, value): self.author.append(value)
    def insert_author(self, index, value): self.author[index] = value
    def get_custodian(self): return self.custodian
    def set_custodian(self, custodian): self.custodian = custodian
    def get_policyManager(self): return self.policyManager
    def set_policyManager(self, policyManager): self.policyManager = policyManager
    def get_authenticator(self): return self.authenticator
    def set_authenticator(self, authenticator): self.authenticator = authenticator
    def get_created(self): return self.created
    def set_created(self, created): self.created = created
    def get_indexed(self): return self.indexed
    def set_indexed(self, indexed): self.indexed = indexed
    def get_status(self): return self.status
    def set_status(self, status): self.status = status
    def get_docStatus(self): return self.docStatus
    def set_docStatus(self, docStatus): self.docStatus = docStatus
    def get_relatesTo(self): return self.relatesTo
    def set_relatesTo(self, relatesTo): self.relatesTo = relatesTo
    def add_relatesTo(self, value): self.relatesTo.append(value)
    def insert_relatesTo(self, index, value): self.relatesTo[index] = value
    def get_description(self): return self.description
    def set_description(self, description): self.description = description
    def get_confidentiality(self): return self.confidentiality
    def set_confidentiality(self, confidentiality): self.confidentiality = confidentiality
    def add_confidentiality(self, value): self.confidentiality.append(value)
    def insert_confidentiality(self, index, value): self.confidentiality[index] = value
    def get_primaryLanguage(self): return self.primaryLanguage
    def set_primaryLanguage(self, primaryLanguage): self.primaryLanguage = primaryLanguage
    def get_mimeType(self): return self.mimeType
    def set_mimeType(self, mimeType): self.mimeType = mimeType
    def get_format(self): return self.format
    def set_format(self, format): self.format = format
    def add_format(self, value): self.format.append(value)
    def insert_format(self, index, value): self.format[index] = value
    def get_size(self): return self.size
    def set_size(self, size): self.size = size
    def get_hash(self): return self.hash
    def set_hash(self, hash): self.hash = hash
    def get_location(self): return self.location
    def set_location(self, location): self.location = location
    def get_service(self): return self.service
    def set_service(self, service): self.service = service
    def get_context(self): return self.context
    def set_context(self, context): self.context = context
    def hasContent_(self):
        if (
            self.masterIdentifier is not None or
            self.identifier or
            self.subject is not None or
            self.type_ is not None or
            self.class_ is not None or
            self.author or
            self.custodian is not None or
            self.policyManager is not None or
            self.authenticator is not None or
            self.created is not None or
            self.indexed is not None or
            self.status is not None or
            self.docStatus is not None or
            self.relatesTo or
            self.description is not None or
            self.confidentiality or
            self.primaryLanguage is not None or
            self.mimeType is not None or
            self.format or
            self.size is not None or
            self.hash is not None or
            self.location is not None or
            self.service is not None or
            self.context is not None or
            super(DocumentReference, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='DocumentReference', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='DocumentReference')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='DocumentReference', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='DocumentReference'):
        super(DocumentReference, self).exportAttributes(outfile, level, already_processed, namespace_, name_='DocumentReference')
    def exportChildren(self, outfile, level, namespace_='', name_='DocumentReference', fromsubclass_=False, pretty_print=True):
        super(DocumentReference, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.masterIdentifier is not None:
            self.masterIdentifier.export(outfile, level, namespace_, name_='masterIdentifier', pretty_print=pretty_print)
        for identifier_ in self.identifier:
            identifier_.export(outfile, level, namespace_, name_='identifier', pretty_print=pretty_print)
        if self.subject is not None:
            self.subject.export(outfile, level, namespace_, name_='subject', pretty_print=pretty_print)
        if self.type_ is not None:
            self.type_.export(outfile, level, namespace_, name_='type', pretty_print=pretty_print)
        if self.class_ is not None:
            self.class_.export(outfile, level, namespace_, name_='class', pretty_print=pretty_print)
        for author_ in self.author:
            author_.export(outfile, level, namespace_, name_='author', pretty_print=pretty_print)
        if self.custodian is not None:
            self.custodian.export(outfile, level, namespace_, name_='custodian', pretty_print=pretty_print)
        if self.policyManager is not None:
            self.policyManager.export(outfile, level, namespace_, name_='policyManager', pretty_print=pretty_print)
        if self.authenticator is not None:
            self.authenticator.export(outfile, level, namespace_, name_='authenticator', pretty_print=pretty_print)
        if self.created is not None:
            self.created.export(outfile, level, namespace_, name_='created', pretty_print=pretty_print)
        if self.indexed is not None:
            self.indexed.export(outfile, level, namespace_, name_='indexed', pretty_print=pretty_print)
        if self.status is not None:
            self.status.export(outfile, level, namespace_, name_='status', pretty_print=pretty_print)
        if self.docStatus is not None:
            self.docStatus.export(outfile, level, namespace_, name_='docStatus', pretty_print=pretty_print)
        for relatesTo_ in self.relatesTo:
            relatesTo_.export(outfile, level, namespace_, name_='relatesTo', pretty_print=pretty_print)
        if self.description is not None:
            self.description.export(outfile, level, namespace_, name_='description', pretty_print=pretty_print)
        for confidentiality_ in self.confidentiality:
            confidentiality_.export(outfile, level, namespace_, name_='confidentiality', pretty_print=pretty_print)
        if self.primaryLanguage is not None:
            self.primaryLanguage.export(outfile, level, namespace_, name_='primaryLanguage', pretty_print=pretty_print)
        if self.mimeType is not None:
            self.mimeType.export(outfile, level, namespace_, name_='mimeType', pretty_print=pretty_print)
        for format_ in self.format:
            format_.export(outfile, level, namespace_, name_='format', pretty_print=pretty_print)
        if self.size is not None:
            self.size.export(outfile, level, namespace_, name_='size', pretty_print=pretty_print)
        if self.hash is not None:
            self.hash.export(outfile, level, namespace_, name_='hash', pretty_print=pretty_print)
        if self.location is not None:
            self.location.export(outfile, level, namespace_, name_='location', pretty_print=pretty_print)
        if self.service is not None:
            self.service.export(outfile, level, namespace_, name_='service', pretty_print=pretty_print)
        if self.context is not None:
            self.context.export(outfile, level, namespace_, name_='context', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='DocumentReference', mapping_=None):
        element = super(DocumentReference, self).to_etree(parent_element, name_, mapping_)
        if self.masterIdentifier is not None:
            masterIdentifier_ = self.masterIdentifier
            masterIdentifier_.to_etree(element, name_='masterIdentifier', mapping_=mapping_)
        for identifier_ in self.identifier:
            identifier_.to_etree(element, name_='identifier', mapping_=mapping_)
        if self.subject is not None:
            subject_ = self.subject
            subject_.to_etree(element, name_='subject', mapping_=mapping_)
        if self.type_ is not None:
            type__ = self.type_
            type__.to_etree(element, name_='type', mapping_=mapping_)
        if self.class_ is not None:
            class__ = self.class_
            class__.to_etree(element, name_='class', mapping_=mapping_)
        for author_ in self.author:
            author_.to_etree(element, name_='author', mapping_=mapping_)
        if self.custodian is not None:
            custodian_ = self.custodian
            custodian_.to_etree(element, name_='custodian', mapping_=mapping_)
        if self.policyManager is not None:
            policyManager_ = self.policyManager
            policyManager_.to_etree(element, name_='policyManager', mapping_=mapping_)
        if self.authenticator is not None:
            authenticator_ = self.authenticator
            authenticator_.to_etree(element, name_='authenticator', mapping_=mapping_)
        if self.created is not None:
            created_ = self.created
            created_.to_etree(element, name_='created', mapping_=mapping_)
        if self.indexed is not None:
            indexed_ = self.indexed
            indexed_.to_etree(element, name_='indexed', mapping_=mapping_)
        if self.status is not None:
            status_ = self.status
            status_.to_etree(element, name_='status', mapping_=mapping_)
        if self.docStatus is not None:
            docStatus_ = self.docStatus
            docStatus_.to_etree(element, name_='docStatus', mapping_=mapping_)
        for relatesTo_ in self.relatesTo:
            relatesTo_.to_etree(element, name_='relatesTo', mapping_=mapping_)
        if self.description is not None:
            description_ = self.description
            description_.to_etree(element, name_='description', mapping_=mapping_)
        for confidentiality_ in self.confidentiality:
            confidentiality_.to_etree(element, name_='confidentiality', mapping_=mapping_)
        if self.primaryLanguage is not None:
            primaryLanguage_ = self.primaryLanguage
            primaryLanguage_.to_etree(element, name_='primaryLanguage', mapping_=mapping_)
        if self.mimeType is not None:
            mimeType_ = self.mimeType
            mimeType_.to_etree(element, name_='mimeType', mapping_=mapping_)
        for format_ in self.format:
            format_.to_etree(element, name_='format', mapping_=mapping_)
        if self.size is not None:
            size_ = self.size
            size_.to_etree(element, name_='size', mapping_=mapping_)
        if self.hash is not None:
            hash_ = self.hash
            hash_.to_etree(element, name_='hash', mapping_=mapping_)
        if self.location is not None:
            location_ = self.location
            location_.to_etree(element, name_='location', mapping_=mapping_)
        if self.service is not None:
            service_ = self.service
            service_.to_etree(element, name_='service', mapping_=mapping_)
        if self.context is not None:
            context_ = self.context
            context_.to_etree(element, name_='context', mapping_=mapping_)
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
        super(DocumentReference, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'masterIdentifier':
            obj_ = Identifier.factory()
            obj_.build(child_)
            self.masterIdentifier = obj_
            obj_.original_tagname_ = 'masterIdentifier'
        elif nodeName_ == 'identifier':
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
        elif nodeName_ == 'class':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.class_ = obj_
            obj_.original_tagname_ = 'class'
        elif nodeName_ == 'author':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.author.append(obj_)
            obj_.original_tagname_ = 'author'
        elif nodeName_ == 'custodian':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.custodian = obj_
            obj_.original_tagname_ = 'custodian'
        elif nodeName_ == 'policyManager':
            obj_ = uri.factory()
            obj_.build(child_)
            self.policyManager = obj_
            obj_.original_tagname_ = 'policyManager'
        elif nodeName_ == 'authenticator':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.authenticator = obj_
            obj_.original_tagname_ = 'authenticator'
        elif nodeName_ == 'created':
            obj_ = dateTime.factory()
            obj_.build(child_)
            self.created = obj_
            obj_.original_tagname_ = 'created'
        elif nodeName_ == 'indexed':
            obj_ = instant.factory()
            obj_.build(child_)
            self.indexed = obj_
            obj_.original_tagname_ = 'indexed'
        elif nodeName_ == 'status':
            obj_ = DocumentReferenceStatus.factory()
            obj_.build(child_)
            self.status = obj_
            obj_.original_tagname_ = 'status'
        elif nodeName_ == 'docStatus':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.docStatus = obj_
            obj_.original_tagname_ = 'docStatus'
        elif nodeName_ == 'relatesTo':
            obj_ = DocumentReference_RelatesTo.factory()
            obj_.build(child_)
            self.relatesTo.append(obj_)
            obj_.original_tagname_ = 'relatesTo'
        elif nodeName_ == 'description':
            obj_ = string.factory()
            obj_.build(child_)
            self.description = obj_
            obj_.original_tagname_ = 'description'
        elif nodeName_ == 'confidentiality':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.confidentiality.append(obj_)
            obj_.original_tagname_ = 'confidentiality'
        elif nodeName_ == 'primaryLanguage':
            obj_ = code.factory()
            obj_.build(child_)
            self.primaryLanguage = obj_
            obj_.original_tagname_ = 'primaryLanguage'
        elif nodeName_ == 'mimeType':
            obj_ = code.factory()
            obj_.build(child_)
            self.mimeType = obj_
            obj_.original_tagname_ = 'mimeType'
        elif nodeName_ == 'format':
            obj_ = uri.factory()
            obj_.build(child_)
            self.format.append(obj_)
            obj_.original_tagname_ = 'format'
        elif nodeName_ == 'size':
            obj_ = integer.factory()
            obj_.build(child_)
            self.size = obj_
            obj_.original_tagname_ = 'size'
        elif nodeName_ == 'hash':
            obj_ = string.factory()
            obj_.build(child_)
            self.hash = obj_
            obj_.original_tagname_ = 'hash'
        elif nodeName_ == 'location':
            obj_ = uri.factory()
            obj_.build(child_)
            self.location = obj_
            obj_.original_tagname_ = 'location'
        elif nodeName_ == 'service':
            obj_ = DocumentReference_Service.factory()
            obj_.build(child_)
            self.service = obj_
            obj_.original_tagname_ = 'service'
        elif nodeName_ == 'context':
            obj_ = DocumentReference_Context.factory()
            obj_.build(child_)
            self.context = obj_
            obj_.original_tagname_ = 'context'
        super(DocumentReference, self).buildChildren(child_, node, nodeName_, True)
# end class DocumentReference


class DocumentReference_RelatesTo(BackboneElement):
    """A reference to a document."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, code=None, target=None):
        self.original_tagname_ = None
        super(DocumentReference_RelatesTo, self).__init__(id, extension, modifierExtension, )
        self.code = code
        self.target = target
    def factory(*args_, **kwargs_):
        if DocumentReference_RelatesTo.subclass:
            return DocumentReference_RelatesTo.subclass(*args_, **kwargs_)
        else:
            return DocumentReference_RelatesTo(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_code(self): return self.code
    def set_code(self, code): self.code = code
    def get_target(self): return self.target
    def set_target(self, target): self.target = target
    def hasContent_(self):
        if (
            self.code is not None or
            self.target is not None or
            super(DocumentReference_RelatesTo, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='DocumentReference.RelatesTo', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='DocumentReference.RelatesTo')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='DocumentReference.RelatesTo', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='DocumentReference.RelatesTo'):
        super(DocumentReference_RelatesTo, self).exportAttributes(outfile, level, already_processed, namespace_, name_='DocumentReference.RelatesTo')
    def exportChildren(self, outfile, level, namespace_='', name_='DocumentReference.RelatesTo', fromsubclass_=False, pretty_print=True):
        super(DocumentReference_RelatesTo, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.code is not None:
            self.code.export(outfile, level, namespace_, name_='code', pretty_print=pretty_print)
        if self.target is not None:
            self.target.export(outfile, level, namespace_, name_='target', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='DocumentReference.RelatesTo', mapping_=None):
        element = super(DocumentReference_RelatesTo, self).to_etree(parent_element, name_, mapping_)
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
        super(DocumentReference_RelatesTo, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'code':
            obj_ = DocumentRelationshipType.factory()
            obj_.build(child_)
            self.code = obj_
            obj_.original_tagname_ = 'code'
        elif nodeName_ == 'target':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.target = obj_
            obj_.original_tagname_ = 'target'
        super(DocumentReference_RelatesTo, self).buildChildren(child_, node, nodeName_, True)
# end class DocumentReference_RelatesTo


class DocumentReference_Service(BackboneElement):
    """A reference to a document."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, type_=None, address=None, parameter=None):
        self.original_tagname_ = None
        super(DocumentReference_Service, self).__init__(id, extension, modifierExtension, )
        self.type_ = type_
        self.address = address
        if parameter is None:
            self.parameter = []
        else:
            self.parameter = parameter
    def factory(*args_, **kwargs_):
        if DocumentReference_Service.subclass:
            return DocumentReference_Service.subclass(*args_, **kwargs_)
        else:
            return DocumentReference_Service(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_type(self): return self.type_
    def set_type(self, type_): self.type_ = type_
    def get_address(self): return self.address
    def set_address(self, address): self.address = address
    def get_parameter(self): return self.parameter
    def set_parameter(self, parameter): self.parameter = parameter
    def add_parameter(self, value): self.parameter.append(value)
    def insert_parameter(self, index, value): self.parameter[index] = value
    def hasContent_(self):
        if (
            self.type_ is not None or
            self.address is not None or
            self.parameter or
            super(DocumentReference_Service, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='DocumentReference.Service', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='DocumentReference.Service')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='DocumentReference.Service', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='DocumentReference.Service'):
        super(DocumentReference_Service, self).exportAttributes(outfile, level, already_processed, namespace_, name_='DocumentReference.Service')
    def exportChildren(self, outfile, level, namespace_='', name_='DocumentReference.Service', fromsubclass_=False, pretty_print=True):
        super(DocumentReference_Service, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.type_ is not None:
            self.type_.export(outfile, level, namespace_, name_='type', pretty_print=pretty_print)
        if self.address is not None:
            self.address.export(outfile, level, namespace_, name_='address', pretty_print=pretty_print)
        for parameter_ in self.parameter:
            parameter_.export(outfile, level, namespace_, name_='parameter', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='DocumentReference.Service', mapping_=None):
        element = super(DocumentReference_Service, self).to_etree(parent_element, name_, mapping_)
        if self.type_ is not None:
            type__ = self.type_
            type__.to_etree(element, name_='type', mapping_=mapping_)
        if self.address is not None:
            address_ = self.address
            address_.to_etree(element, name_='address', mapping_=mapping_)
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
        super(DocumentReference_Service, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'type':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.type_ = obj_
            obj_.original_tagname_ = 'type'
        elif nodeName_ == 'address':
            obj_ = string.factory()
            obj_.build(child_)
            self.address = obj_
            obj_.original_tagname_ = 'address'
        elif nodeName_ == 'parameter':
            obj_ = DocumentReference_Parameter.factory()
            obj_.build(child_)
            self.parameter.append(obj_)
            obj_.original_tagname_ = 'parameter'
        super(DocumentReference_Service, self).buildChildren(child_, node, nodeName_, True)
# end class DocumentReference_Service


class DocumentReference_Parameter(BackboneElement):
    """A reference to a document."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, name=None, value=None):
        self.original_tagname_ = None
        super(DocumentReference_Parameter, self).__init__(id, extension, modifierExtension, )
        self.name = name
        self.value = value
    def factory(*args_, **kwargs_):
        if DocumentReference_Parameter.subclass:
            return DocumentReference_Parameter.subclass(*args_, **kwargs_)
        else:
            return DocumentReference_Parameter(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_name(self): return self.name
    def set_name(self, name): self.name = name
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            self.name is not None or
            self.value is not None or
            super(DocumentReference_Parameter, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='DocumentReference.Parameter', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='DocumentReference.Parameter')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='DocumentReference.Parameter', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='DocumentReference.Parameter'):
        super(DocumentReference_Parameter, self).exportAttributes(outfile, level, already_processed, namespace_, name_='DocumentReference.Parameter')
    def exportChildren(self, outfile, level, namespace_='', name_='DocumentReference.Parameter', fromsubclass_=False, pretty_print=True):
        super(DocumentReference_Parameter, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.name is not None:
            self.name.export(outfile, level, namespace_, name_='name', pretty_print=pretty_print)
        if self.value is not None:
            self.value.export(outfile, level, namespace_, name_='value', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='DocumentReference.Parameter', mapping_=None):
        element = super(DocumentReference_Parameter, self).to_etree(parent_element, name_, mapping_)
        if self.name is not None:
            name_ = self.name
            name_.to_etree(element, name_='name', mapping_=mapping_)
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
        super(DocumentReference_Parameter, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'name':
            obj_ = string.factory()
            obj_.build(child_)
            self.name = obj_
            obj_.original_tagname_ = 'name'
        elif nodeName_ == 'value':
            obj_ = string.factory()
            obj_.build(child_)
            self.value = obj_
            obj_.original_tagname_ = 'value'
        super(DocumentReference_Parameter, self).buildChildren(child_, node, nodeName_, True)
# end class DocumentReference_Parameter


class DocumentReference_Context(BackboneElement):
    """A reference to a document."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, event=None, period=None, facilityType=None):
        self.original_tagname_ = None
        super(DocumentReference_Context, self).__init__(id, extension, modifierExtension, )
        if event is None:
            self.event = []
        else:
            self.event = event
        self.period = period
        self.facilityType = facilityType
    def factory(*args_, **kwargs_):
        if DocumentReference_Context.subclass:
            return DocumentReference_Context.subclass(*args_, **kwargs_)
        else:
            return DocumentReference_Context(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_event(self): return self.event
    def set_event(self, event): self.event = event
    def add_event(self, value): self.event.append(value)
    def insert_event(self, index, value): self.event[index] = value
    def get_period(self): return self.period
    def set_period(self, period): self.period = period
    def get_facilityType(self): return self.facilityType
    def set_facilityType(self, facilityType): self.facilityType = facilityType
    def hasContent_(self):
        if (
            self.event or
            self.period is not None or
            self.facilityType is not None or
            super(DocumentReference_Context, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='DocumentReference.Context', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='DocumentReference.Context')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='DocumentReference.Context', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='DocumentReference.Context'):
        super(DocumentReference_Context, self).exportAttributes(outfile, level, already_processed, namespace_, name_='DocumentReference.Context')
    def exportChildren(self, outfile, level, namespace_='', name_='DocumentReference.Context', fromsubclass_=False, pretty_print=True):
        super(DocumentReference_Context, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for event_ in self.event:
            event_.export(outfile, level, namespace_, name_='event', pretty_print=pretty_print)
        if self.period is not None:
            self.period.export(outfile, level, namespace_, name_='period', pretty_print=pretty_print)
        if self.facilityType is not None:
            self.facilityType.export(outfile, level, namespace_, name_='facilityType', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='DocumentReference.Context', mapping_=None):
        element = super(DocumentReference_Context, self).to_etree(parent_element, name_, mapping_)
        for event_ in self.event:
            event_.to_etree(element, name_='event', mapping_=mapping_)
        if self.period is not None:
            period_ = self.period
            period_.to_etree(element, name_='period', mapping_=mapping_)
        if self.facilityType is not None:
            facilityType_ = self.facilityType
            facilityType_.to_etree(element, name_='facilityType', mapping_=mapping_)
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
        super(DocumentReference_Context, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'event':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.event.append(obj_)
            obj_.original_tagname_ = 'event'
        elif nodeName_ == 'period':
            obj_ = Period.factory()
            obj_.build(child_)
            self.period = obj_
            obj_.original_tagname_ = 'period'
        elif nodeName_ == 'facilityType':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.facilityType = obj_
            obj_.original_tagname_ = 'facilityType'
        super(DocumentReference_Context, self).buildChildren(child_, node, nodeName_, True)
# end class DocumentReference_Context


class DocumentReferenceStatus(Element):
    """If the element is present, it must have either a @value, an @id, or
    extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(DocumentReferenceStatus, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if DocumentReferenceStatus.subclass:
            return DocumentReferenceStatus.subclass(*args_, **kwargs_)
        else:
            return DocumentReferenceStatus(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(DocumentReferenceStatus, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='DocumentReferenceStatus', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='DocumentReferenceStatus')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='DocumentReferenceStatus', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='DocumentReferenceStatus'):
        super(DocumentReferenceStatus, self).exportAttributes(outfile, level, already_processed, namespace_, name_='DocumentReferenceStatus')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='DocumentReferenceStatus', fromsubclass_=False, pretty_print=True):
        super(DocumentReferenceStatus, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='DocumentReferenceStatus', mapping_=None):
        element = super(DocumentReferenceStatus, self).to_etree(parent_element, name_, mapping_)
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
        super(DocumentReferenceStatus, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(DocumentReferenceStatus, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class DocumentReferenceStatus
