from .base_classes import *
from .support_functions import *


class OrderResponse(Resource):
    """A response to an order.If the element is present, it must have
    either a @value, an @id, or extensionsA reference to an
    authority policy that is the reason for the response. Usually
    this is used when the order is rejected, to provide a reason for
    rejection."""
    subclass = None
    superclass = Resource
    def __init__(self, id=None, extension=None, modifierExtension=None, language=None, text=None, contained=None, identifier=None, request=None, date=None, who=None, authorityCodeableConcept=None, authorityResource=None, code=None, description=None, fulfillment=None):
        self.original_tagname_ = None
        super(OrderResponse, self).__init__(id, extension, modifierExtension, language, text, contained, )
        if identifier is None:
            self.identifier = []
        else:
            self.identifier = identifier
        self.request = request
        self.date = date
        self.who = who
        self.authorityCodeableConcept = authorityCodeableConcept
        self.authorityResource = authorityResource
        self.code = code
        self.description = description
        if fulfillment is None:
            self.fulfillment = []
        else:
            self.fulfillment = fulfillment
    def factory(*args_, **kwargs_):
        if OrderResponse.subclass:
            return OrderResponse.subclass(*args_, **kwargs_)
        else:
            return OrderResponse(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_identifier(self): return self.identifier
    def set_identifier(self, identifier): self.identifier = identifier
    def add_identifier(self, value): self.identifier.append(value)
    def insert_identifier(self, index, value): self.identifier[index] = value
    def get_request(self): return self.request
    def set_request(self, request): self.request = request
    def get_date(self): return self.date
    def set_date(self, date): self.date = date
    def get_who(self): return self.who
    def set_who(self, who): self.who = who
    def get_authorityCodeableConcept(self): return self.authorityCodeableConcept
    def set_authorityCodeableConcept(self, authorityCodeableConcept): self.authorityCodeableConcept = authorityCodeableConcept
    def get_authorityResource(self): return self.authorityResource
    def set_authorityResource(self, authorityResource): self.authorityResource = authorityResource
    def get_code(self): return self.code
    def set_code(self, code): self.code = code
    def get_description(self): return self.description
    def set_description(self, description): self.description = description
    def get_fulfillment(self): return self.fulfillment
    def set_fulfillment(self, fulfillment): self.fulfillment = fulfillment
    def add_fulfillment(self, value): self.fulfillment.append(value)
    def insert_fulfillment(self, index, value): self.fulfillment[index] = value
    def hasContent_(self):
        if (
            self.identifier or
            self.request is not None or
            self.date is not None or
            self.who is not None or
            self.authorityCodeableConcept is not None or
            self.authorityResource is not None or
            self.code is not None or
            self.description is not None or
            self.fulfillment or
            super(OrderResponse, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='OrderResponse', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='OrderResponse')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='OrderResponse', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='OrderResponse'):
        super(OrderResponse, self).exportAttributes(outfile, level, already_processed, namespace_, name_='OrderResponse')
    def exportChildren(self, outfile, level, namespace_='', name_='OrderResponse', fromsubclass_=False, pretty_print=True):
        super(OrderResponse, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for identifier_ in self.identifier:
            identifier_.export(outfile, level, namespace_, name_='identifier', pretty_print=pretty_print)
        if self.request is not None:
            self.request.export(outfile, level, namespace_, name_='request', pretty_print=pretty_print)
        if self.date is not None:
            self.date.export(outfile, level, namespace_, name_='date', pretty_print=pretty_print)
        if self.who is not None:
            self.who.export(outfile, level, namespace_, name_='who', pretty_print=pretty_print)
        if self.authorityCodeableConcept is not None:
            self.authorityCodeableConcept.export(outfile, level, namespace_, name_='authorityCodeableConcept', pretty_print=pretty_print)
        if self.authorityResource is not None:
            self.authorityResource.export(outfile, level, namespace_, name_='authorityResource', pretty_print=pretty_print)
        if self.code is not None:
            self.code.export(outfile, level, namespace_, name_='code', pretty_print=pretty_print)
        if self.description is not None:
            self.description.export(outfile, level, namespace_, name_='description', pretty_print=pretty_print)
        for fulfillment_ in self.fulfillment:
            fulfillment_.export(outfile, level, namespace_, name_='fulfillment', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='OrderResponse', mapping_=None):
        element = super(OrderResponse, self).to_etree(parent_element, name_, mapping_)
        for identifier_ in self.identifier:
            identifier_.to_etree(element, name_='identifier', mapping_=mapping_)
        if self.request is not None:
            request_ = self.request
            request_.to_etree(element, name_='request', mapping_=mapping_)
        if self.date is not None:
            date_ = self.date
            date_.to_etree(element, name_='date', mapping_=mapping_)
        if self.who is not None:
            who_ = self.who
            who_.to_etree(element, name_='who', mapping_=mapping_)
        if self.authorityCodeableConcept is not None:
            authorityCodeableConcept_ = self.authorityCodeableConcept
            authorityCodeableConcept_.to_etree(element, name_='authorityCodeableConcept', mapping_=mapping_)
        if self.authorityResource is not None:
            authorityResource_ = self.authorityResource
            authorityResource_.to_etree(element, name_='authorityResource', mapping_=mapping_)
        if self.code is not None:
            code_ = self.code
            code_.to_etree(element, name_='code', mapping_=mapping_)
        if self.description is not None:
            description_ = self.description
            description_.to_etree(element, name_='description', mapping_=mapping_)
        for fulfillment_ in self.fulfillment:
            fulfillment_.to_etree(element, name_='fulfillment', mapping_=mapping_)
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
        super(OrderResponse, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'identifier':
            obj_ = Identifier.factory()
            obj_.build(child_)
            self.identifier.append(obj_)
            obj_.original_tagname_ = 'identifier'
        elif nodeName_ == 'request':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.request = obj_
            obj_.original_tagname_ = 'request'
        elif nodeName_ == 'date':
            obj_ = dateTime.factory()
            obj_.build(child_)
            self.date = obj_
            obj_.original_tagname_ = 'date'
        elif nodeName_ == 'who':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.who = obj_
            obj_.original_tagname_ = 'who'
        elif nodeName_ == 'authorityCodeableConcept':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.authorityCodeableConcept = obj_
            obj_.original_tagname_ = 'authorityCodeableConcept'
        elif nodeName_ == 'authorityResource':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.authorityResource = obj_
            obj_.original_tagname_ = 'authorityResource'
        elif nodeName_ == 'code':
            obj_ = OrderOutcomeStatus.factory()
            obj_.build(child_)
            self.code = obj_
            obj_.original_tagname_ = 'code'
        elif nodeName_ == 'description':
            obj_ = string.factory()
            obj_.build(child_)
            self.description = obj_
            obj_.original_tagname_ = 'description'
        elif nodeName_ == 'fulfillment':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.fulfillment.append(obj_)
            obj_.original_tagname_ = 'fulfillment'
        super(OrderResponse, self).buildChildren(child_, node, nodeName_, True)
# end class OrderResponse


class OrderOutcomeStatus(Element):
    """The status of the response to an orderIf the element is present, it
    must have either a @value, an @id, or extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(OrderOutcomeStatus, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if OrderOutcomeStatus.subclass:
            return OrderOutcomeStatus.subclass(*args_, **kwargs_)
        else:
            return OrderOutcomeStatus(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(OrderOutcomeStatus, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='OrderOutcomeStatus', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='OrderOutcomeStatus')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='OrderOutcomeStatus', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='OrderOutcomeStatus'):
        super(OrderOutcomeStatus, self).exportAttributes(outfile, level, already_processed, namespace_, name_='OrderOutcomeStatus')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='OrderOutcomeStatus', fromsubclass_=False, pretty_print=True):
        super(OrderOutcomeStatus, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='OrderOutcomeStatus', mapping_=None):
        element = super(OrderOutcomeStatus, self).to_etree(parent_element, name_, mapping_)
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
        super(OrderOutcomeStatus, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(OrderOutcomeStatus, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class OrderOutcomeStatus
