from .base_classes import *
from .support_functions import *


class MessageHeader(Resource):
    """The header for a message exchange that is either requesting or
    responding to an action. The resource(s) that are the subject of
    the action as well as other Information related to the action
    are typically transmitted in a bundle in which the MessageHeader
    resource instance is the first resource in the bundle.If the
    element is present, it must have either a @value, an @id, or
    extensions"""
    subclass = None
    superclass = Resource
    def __init__(self, id=None, extension=None, modifierExtension=None, language=None, text=None, contained=None, identifier=None, timestamp=None, event=None, response=None, source=None, destination=None, enterer=None, author=None, receiver=None, responsible=None, reason=None, data=None):
        self.original_tagname_ = None
        super(MessageHeader, self).__init__(id, extension, modifierExtension, language, text, contained, )
        self.identifier = identifier
        self.timestamp = timestamp
        self.event = event
        self.response = response
        self.source = source
        if destination is None:
            self.destination = []
        else:
            self.destination = destination
        self.enterer = enterer
        self.author = author
        self.receiver = receiver
        self.responsible = responsible
        self.reason = reason
        if data is None:
            self.data = []
        else:
            self.data = data
    def factory(*args_, **kwargs_):
        if MessageHeader.subclass:
            return MessageHeader.subclass(*args_, **kwargs_)
        else:
            return MessageHeader(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_identifier(self): return self.identifier
    def set_identifier(self, identifier): self.identifier = identifier
    def get_timestamp(self): return self.timestamp
    def set_timestamp(self, timestamp): self.timestamp = timestamp
    def get_event(self): return self.event
    def set_event(self, event): self.event = event
    def get_response(self): return self.response
    def set_response(self, response): self.response = response
    def get_source(self): return self.source
    def set_source(self, source): self.source = source
    def get_destination(self): return self.destination
    def set_destination(self, destination): self.destination = destination
    def add_destination(self, value): self.destination.append(value)
    def insert_destination(self, index, value): self.destination[index] = value
    def get_enterer(self): return self.enterer
    def set_enterer(self, enterer): self.enterer = enterer
    def get_author(self): return self.author
    def set_author(self, author): self.author = author
    def get_receiver(self): return self.receiver
    def set_receiver(self, receiver): self.receiver = receiver
    def get_responsible(self): return self.responsible
    def set_responsible(self, responsible): self.responsible = responsible
    def get_reason(self): return self.reason
    def set_reason(self, reason): self.reason = reason
    def get_data(self): return self.data
    def set_data(self, data): self.data = data
    def add_data(self, value): self.data.append(value)
    def insert_data(self, index, value): self.data[index] = value
    def hasContent_(self):
        if (
            self.identifier is not None or
            self.timestamp is not None or
            self.event is not None or
            self.response is not None or
            self.source is not None or
            self.destination or
            self.enterer is not None or
            self.author is not None or
            self.receiver is not None or
            self.responsible is not None or
            self.reason is not None or
            self.data or
            super(MessageHeader, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='MessageHeader', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='MessageHeader')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='MessageHeader', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='MessageHeader'):
        super(MessageHeader, self).exportAttributes(outfile, level, already_processed, namespace_, name_='MessageHeader')
    def exportChildren(self, outfile, level, namespace_='', name_='MessageHeader', fromsubclass_=False, pretty_print=True):
        super(MessageHeader, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.identifier is not None:
            self.identifier.export(outfile, level, namespace_, name_='identifier', pretty_print=pretty_print)
        if self.timestamp is not None:
            self.timestamp.export(outfile, level, namespace_, name_='timestamp', pretty_print=pretty_print)
        if self.event is not None:
            self.event.export(outfile, level, namespace_, name_='event', pretty_print=pretty_print)
        if self.response is not None:
            self.response.export(outfile, level, namespace_, name_='response', pretty_print=pretty_print)
        if self.source is not None:
            self.source.export(outfile, level, namespace_, name_='source', pretty_print=pretty_print)
        for destination_ in self.destination:
            destination_.export(outfile, level, namespace_, name_='destination', pretty_print=pretty_print)
        if self.enterer is not None:
            self.enterer.export(outfile, level, namespace_, name_='enterer', pretty_print=pretty_print)
        if self.author is not None:
            self.author.export(outfile, level, namespace_, name_='author', pretty_print=pretty_print)
        if self.receiver is not None:
            self.receiver.export(outfile, level, namespace_, name_='receiver', pretty_print=pretty_print)
        if self.responsible is not None:
            self.responsible.export(outfile, level, namespace_, name_='responsible', pretty_print=pretty_print)
        if self.reason is not None:
            self.reason.export(outfile, level, namespace_, name_='reason', pretty_print=pretty_print)
        for data_ in self.data:
            data_.export(outfile, level, namespace_, name_='data', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='MessageHeader', mapping_=None):
        element = super(MessageHeader, self).to_etree(parent_element, name_, mapping_)
        if self.identifier is not None:
            identifier_ = self.identifier
            identifier_.to_etree(element, name_='identifier', mapping_=mapping_)
        if self.timestamp is not None:
            timestamp_ = self.timestamp
            timestamp_.to_etree(element, name_='timestamp', mapping_=mapping_)
        if self.event is not None:
            event_ = self.event
            event_.to_etree(element, name_='event', mapping_=mapping_)
        if self.response is not None:
            response_ = self.response
            response_.to_etree(element, name_='response', mapping_=mapping_)
        if self.source is not None:
            source_ = self.source
            source_.to_etree(element, name_='source', mapping_=mapping_)
        for destination_ in self.destination:
            destination_.to_etree(element, name_='destination', mapping_=mapping_)
        if self.enterer is not None:
            enterer_ = self.enterer
            enterer_.to_etree(element, name_='enterer', mapping_=mapping_)
        if self.author is not None:
            author_ = self.author
            author_.to_etree(element, name_='author', mapping_=mapping_)
        if self.receiver is not None:
            receiver_ = self.receiver
            receiver_.to_etree(element, name_='receiver', mapping_=mapping_)
        if self.responsible is not None:
            responsible_ = self.responsible
            responsible_.to_etree(element, name_='responsible', mapping_=mapping_)
        if self.reason is not None:
            reason_ = self.reason
            reason_.to_etree(element, name_='reason', mapping_=mapping_)
        for data_ in self.data:
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
        super(MessageHeader, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'identifier':
            obj_ = id.factory()
            obj_.build(child_)
            self.identifier = obj_
            obj_.original_tagname_ = 'identifier'
        elif nodeName_ == 'timestamp':
            obj_ = instant.factory()
            obj_.build(child_)
            self.timestamp = obj_
            obj_.original_tagname_ = 'timestamp'
        elif nodeName_ == 'event':
            obj_ = Coding.factory()
            obj_.build(child_)
            self.event = obj_
            obj_.original_tagname_ = 'event'
        elif nodeName_ == 'response':
            obj_ = MessageHeader_Response.factory()
            obj_.build(child_)
            self.response = obj_
            obj_.original_tagname_ = 'response'
        elif nodeName_ == 'source':
            obj_ = MessageHeader_Source.factory()
            obj_.build(child_)
            self.source = obj_
            obj_.original_tagname_ = 'source'
        elif nodeName_ == 'destination':
            obj_ = MessageHeader_Destination.factory()
            obj_.build(child_)
            self.destination.append(obj_)
            obj_.original_tagname_ = 'destination'
        elif nodeName_ == 'enterer':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.enterer = obj_
            obj_.original_tagname_ = 'enterer'
        elif nodeName_ == 'author':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.author = obj_
            obj_.original_tagname_ = 'author'
        elif nodeName_ == 'receiver':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.receiver = obj_
            obj_.original_tagname_ = 'receiver'
        elif nodeName_ == 'responsible':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.responsible = obj_
            obj_.original_tagname_ = 'responsible'
        elif nodeName_ == 'reason':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.reason = obj_
            obj_.original_tagname_ = 'reason'
        elif nodeName_ == 'data':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.data.append(obj_)
            obj_.original_tagname_ = 'data'
        super(MessageHeader, self).buildChildren(child_, node, nodeName_, True)
# end class MessageHeader


class MessageHeader_Response(BackboneElement):
    """The header for a message exchange that is either requesting or
    responding to an action. The resource(s) that are the subject of
    the action as well as other Information related to the action
    are typically transmitted in a bundle in which the MessageHeader
    resource instance is the first resource in the bundle."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, identifier=None, code=None, details=None):
        self.original_tagname_ = None
        super(MessageHeader_Response, self).__init__(id, extension, modifierExtension, )
        self.identifier = identifier
        self.code = code
        self.details = details
    def factory(*args_, **kwargs_):
        if MessageHeader_Response.subclass:
            return MessageHeader_Response.subclass(*args_, **kwargs_)
        else:
            return MessageHeader_Response(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_identifier(self): return self.identifier
    def set_identifier(self, identifier): self.identifier = identifier
    def get_code(self): return self.code
    def set_code(self, code): self.code = code
    def get_details(self): return self.details
    def set_details(self, details): self.details = details
    def hasContent_(self):
        if (
            self.identifier is not None or
            self.code is not None or
            self.details is not None or
            super(MessageHeader_Response, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='MessageHeader.Response', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='MessageHeader.Response')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='MessageHeader.Response', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='MessageHeader.Response'):
        super(MessageHeader_Response, self).exportAttributes(outfile, level, already_processed, namespace_, name_='MessageHeader.Response')
    def exportChildren(self, outfile, level, namespace_='', name_='MessageHeader.Response', fromsubclass_=False, pretty_print=True):
        super(MessageHeader_Response, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.identifier is not None:
            self.identifier.export(outfile, level, namespace_, name_='identifier', pretty_print=pretty_print)
        if self.code is not None:
            self.code.export(outfile, level, namespace_, name_='code', pretty_print=pretty_print)
        if self.details is not None:
            self.details.export(outfile, level, namespace_, name_='details', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='MessageHeader.Response', mapping_=None):
        element = super(MessageHeader_Response, self).to_etree(parent_element, name_, mapping_)
        if self.identifier is not None:
            identifier_ = self.identifier
            identifier_.to_etree(element, name_='identifier', mapping_=mapping_)
        if self.code is not None:
            code_ = self.code
            code_.to_etree(element, name_='code', mapping_=mapping_)
        if self.details is not None:
            details_ = self.details
            details_.to_etree(element, name_='details', mapping_=mapping_)
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
        super(MessageHeader_Response, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'identifier':
            obj_ = id.factory()
            obj_.build(child_)
            self.identifier = obj_
            obj_.original_tagname_ = 'identifier'
        elif nodeName_ == 'code':
            obj_ = ResponseType.factory()
            obj_.build(child_)
            self.code = obj_
            obj_.original_tagname_ = 'code'
        elif nodeName_ == 'details':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.details = obj_
            obj_.original_tagname_ = 'details'
        super(MessageHeader_Response, self).buildChildren(child_, node, nodeName_, True)
# end class MessageHeader_Response


class MessageHeader_Source(BackboneElement):
    """The header for a message exchange that is either requesting or
    responding to an action. The resource(s) that are the subject of
    the action as well as other Information related to the action
    are typically transmitted in a bundle in which the MessageHeader
    resource instance is the first resource in the bundle."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, name=None, software=None, version=None, contact=None, endpoint=None):
        self.original_tagname_ = None
        super(MessageHeader_Source, self).__init__(id, extension, modifierExtension, )
        self.name = name
        self.software = software
        self.version = version
        self.contact = contact
        self.endpoint = endpoint
    def factory(*args_, **kwargs_):
        if MessageHeader_Source.subclass:
            return MessageHeader_Source.subclass(*args_, **kwargs_)
        else:
            return MessageHeader_Source(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_name(self): return self.name
    def set_name(self, name): self.name = name
    def get_software(self): return self.software
    def set_software(self, software): self.software = software
    def get_version(self): return self.version
    def set_version(self, version): self.version = version
    def get_contact(self): return self.contact
    def set_contact(self, contact): self.contact = contact
    def get_endpoint(self): return self.endpoint
    def set_endpoint(self, endpoint): self.endpoint = endpoint
    def hasContent_(self):
        if (
            self.name is not None or
            self.software is not None or
            self.version is not None or
            self.contact is not None or
            self.endpoint is not None or
            super(MessageHeader_Source, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='MessageHeader.Source', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='MessageHeader.Source')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='MessageHeader.Source', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='MessageHeader.Source'):
        super(MessageHeader_Source, self).exportAttributes(outfile, level, already_processed, namespace_, name_='MessageHeader.Source')
    def exportChildren(self, outfile, level, namespace_='', name_='MessageHeader.Source', fromsubclass_=False, pretty_print=True):
        super(MessageHeader_Source, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.name is not None:
            self.name.export(outfile, level, namespace_, name_='name', pretty_print=pretty_print)
        if self.software is not None:
            self.software.export(outfile, level, namespace_, name_='software', pretty_print=pretty_print)
        if self.version is not None:
            self.version.export(outfile, level, namespace_, name_='version', pretty_print=pretty_print)
        if self.contact is not None:
            self.contact.export(outfile, level, namespace_, name_='contact', pretty_print=pretty_print)
        if self.endpoint is not None:
            self.endpoint.export(outfile, level, namespace_, name_='endpoint', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='MessageHeader.Source', mapping_=None):
        element = super(MessageHeader_Source, self).to_etree(parent_element, name_, mapping_)
        if self.name is not None:
            name_ = self.name
            name_.to_etree(element, name_='name', mapping_=mapping_)
        if self.software is not None:
            software_ = self.software
            software_.to_etree(element, name_='software', mapping_=mapping_)
        if self.version is not None:
            version_ = self.version
            version_.to_etree(element, name_='version', mapping_=mapping_)
        if self.contact is not None:
            contact_ = self.contact
            contact_.to_etree(element, name_='contact', mapping_=mapping_)
        if self.endpoint is not None:
            endpoint_ = self.endpoint
            endpoint_.to_etree(element, name_='endpoint', mapping_=mapping_)
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
        super(MessageHeader_Source, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'name':
            obj_ = string.factory()
            obj_.build(child_)
            self.name = obj_
            obj_.original_tagname_ = 'name'
        elif nodeName_ == 'software':
            obj_ = string.factory()
            obj_.build(child_)
            self.software = obj_
            obj_.original_tagname_ = 'software'
        elif nodeName_ == 'version':
            obj_ = string.factory()
            obj_.build(child_)
            self.version = obj_
            obj_.original_tagname_ = 'version'
        elif nodeName_ == 'contact':
            obj_ = Contact.factory()
            obj_.build(child_)
            self.contact = obj_
            obj_.original_tagname_ = 'contact'
        elif nodeName_ == 'endpoint':
            obj_ = uri.factory()
            obj_.build(child_)
            self.endpoint = obj_
            obj_.original_tagname_ = 'endpoint'
        super(MessageHeader_Source, self).buildChildren(child_, node, nodeName_, True)
# end class MessageHeader_Source


class MessageHeader_Destination(BackboneElement):
    """The header for a message exchange that is either requesting or
    responding to an action. The resource(s) that are the subject of
    the action as well as other Information related to the action
    are typically transmitted in a bundle in which the MessageHeader
    resource instance is the first resource in the bundle."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, name=None, target=None, endpoint=None):
        self.original_tagname_ = None
        super(MessageHeader_Destination, self).__init__(id, extension, modifierExtension, )
        self.name = name
        self.target = target
        self.endpoint = endpoint
    def factory(*args_, **kwargs_):
        if MessageHeader_Destination.subclass:
            return MessageHeader_Destination.subclass(*args_, **kwargs_)
        else:
            return MessageHeader_Destination(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_name(self): return self.name
    def set_name(self, name): self.name = name
    def get_target(self): return self.target
    def set_target(self, target): self.target = target
    def get_endpoint(self): return self.endpoint
    def set_endpoint(self, endpoint): self.endpoint = endpoint
    def hasContent_(self):
        if (
            self.name is not None or
            self.target is not None or
            self.endpoint is not None or
            super(MessageHeader_Destination, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='MessageHeader.Destination', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='MessageHeader.Destination')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='MessageHeader.Destination', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='MessageHeader.Destination'):
        super(MessageHeader_Destination, self).exportAttributes(outfile, level, already_processed, namespace_, name_='MessageHeader.Destination')
    def exportChildren(self, outfile, level, namespace_='', name_='MessageHeader.Destination', fromsubclass_=False, pretty_print=True):
        super(MessageHeader_Destination, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.name is not None:
            self.name.export(outfile, level, namespace_, name_='name', pretty_print=pretty_print)
        if self.target is not None:
            self.target.export(outfile, level, namespace_, name_='target', pretty_print=pretty_print)
        if self.endpoint is not None:
            self.endpoint.export(outfile, level, namespace_, name_='endpoint', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='MessageHeader.Destination', mapping_=None):
        element = super(MessageHeader_Destination, self).to_etree(parent_element, name_, mapping_)
        if self.name is not None:
            name_ = self.name
            name_.to_etree(element, name_='name', mapping_=mapping_)
        if self.target is not None:
            target_ = self.target
            target_.to_etree(element, name_='target', mapping_=mapping_)
        if self.endpoint is not None:
            endpoint_ = self.endpoint
            endpoint_.to_etree(element, name_='endpoint', mapping_=mapping_)
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
        super(MessageHeader_Destination, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'name':
            obj_ = string.factory()
            obj_.build(child_)
            self.name = obj_
            obj_.original_tagname_ = 'name'
        elif nodeName_ == 'target':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.target = obj_
            obj_.original_tagname_ = 'target'
        elif nodeName_ == 'endpoint':
            obj_ = uri.factory()
            obj_.build(child_)
            self.endpoint = obj_
            obj_.original_tagname_ = 'endpoint'
        super(MessageHeader_Destination, self).buildChildren(child_, node, nodeName_, True)
# end class MessageHeader_Destination


class ResponseType(Element):
    """The kind of response to a messageIf the element is present, it must
    have either a @value, an @id, or extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(ResponseType, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if ResponseType.subclass:
            return ResponseType.subclass(*args_, **kwargs_)
        else:
            return ResponseType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(ResponseType, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='ResponseType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ResponseType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='ResponseType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='ResponseType'):
        super(ResponseType, self).exportAttributes(outfile, level, already_processed, namespace_, name_='ResponseType')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='ResponseType', fromsubclass_=False, pretty_print=True):
        super(ResponseType, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='ResponseType', mapping_=None):
        element = super(ResponseType, self).to_etree(parent_element, name_, mapping_)
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
        super(ResponseType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(ResponseType, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class ResponseType
