from .base_classes import *
from .support_functions import *

class Query(Resource):
    """A description of a query with a set of parameters.If the element is
    present, it must have either a @value, an @id, or extensions"""
    subclass = None
    superclass = Resource
    def __init__(self, id=None, extension=None, modifierExtension=None, language=None, text=None, contained=None, identifier=None, parameter=None, response=None):
        self.original_tagname_ = None
        super(Query, self).__init__(id, extension, modifierExtension, language, text, contained, )
        self.identifier = identifier
        if parameter is None:
            self.parameter = []
        else:
            self.parameter = parameter
        self.response = response
    def factory(*args_, **kwargs_):
        if Query.subclass:
            return Query.subclass(*args_, **kwargs_)
        else:
            return Query(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_identifier(self): return self.identifier
    def set_identifier(self, identifier): self.identifier = identifier
    def get_parameter(self): return self.parameter
    def set_parameter(self, parameter): self.parameter = parameter
    def add_parameter(self, value): self.parameter.append(value)
    def insert_parameter(self, index, value): self.parameter[index] = value
    def get_response(self): return self.response
    def set_response(self, response): self.response = response
    def hasContent_(self):
        if (
            self.identifier is not None or
            self.parameter or
            self.response is not None or
            super(Query, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Query', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Query')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Query', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Query'):
        super(Query, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Query')
    def exportChildren(self, outfile, level, namespace_='', name_='Query', fromsubclass_=False, pretty_print=True):
        super(Query, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.identifier is not None:
            self.identifier.export(outfile, level, namespace_, name_='identifier', pretty_print=pretty_print)
        for parameter_ in self.parameter:
            parameter_.export(outfile, level, namespace_, name_='parameter', pretty_print=pretty_print)
        if self.response is not None:
            self.response.export(outfile, level, namespace_, name_='response', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Query', mapping_=None):
        element = super(Query, self).to_etree(parent_element, name_, mapping_)
        if self.identifier is not None:
            identifier_ = self.identifier
            identifier_.to_etree(element, name_='identifier', mapping_=mapping_)
        for parameter_ in self.parameter:
            parameter_.to_etree(element, name_='parameter', mapping_=mapping_)
        if self.response is not None:
            response_ = self.response
            response_.to_etree(element, name_='response', mapping_=mapping_)
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
        super(Query, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'identifier':
            obj_ = uri.factory()
            obj_.build(child_)
            self.identifier = obj_
            obj_.original_tagname_ = 'identifier'
        elif nodeName_ == 'parameter':
            obj_ = Extension.factory()
            obj_.build(child_)
            self.parameter.append(obj_)
            obj_.original_tagname_ = 'parameter'
        elif nodeName_ == 'response':
            obj_ = Query_Response.factory()
            obj_.build(child_)
            self.response = obj_
            obj_.original_tagname_ = 'response'
        super(Query, self).buildChildren(child_, node, nodeName_, True)
# end class Query


class Query_Response(BackboneElement):
    """A description of a query with a set of parameters."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, identifier=None, outcome=None, total=None, parameter=None, first=None, previous=None, next_=None, last=None, reference=None):
        self.original_tagname_ = None
        super(Query_Response, self).__init__(id, extension, modifierExtension, )
        self.identifier = identifier
        self.outcome = outcome
        self.total = total
        if parameter is None:
            self.parameter = []
        else:
            self.parameter = parameter
        if first is None:
            self.first = []
        else:
            self.first = first
        if previous is None:
            self.previous = []
        else:
            self.previous = previous
        if next_ is None:
            self.next_ = []
        else:
            self.next_ = next_
        if last is None:
            self.last = []
        else:
            self.last = last
        if reference is None:
            self.reference = []
        else:
            self.reference = reference
    def factory(*args_, **kwargs_):
        if Query_Response.subclass:
            return Query_Response.subclass(*args_, **kwargs_)
        else:
            return Query_Response(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_identifier(self): return self.identifier
    def set_identifier(self, identifier): self.identifier = identifier
    def get_outcome(self): return self.outcome
    def set_outcome(self, outcome): self.outcome = outcome
    def get_total(self): return self.total
    def set_total(self, total): self.total = total
    def get_parameter(self): return self.parameter
    def set_parameter(self, parameter): self.parameter = parameter
    def add_parameter(self, value): self.parameter.append(value)
    def insert_parameter(self, index, value): self.parameter[index] = value
    def get_first(self): return self.first
    def set_first(self, first): self.first = first
    def add_first(self, value): self.first.append(value)
    def insert_first(self, index, value): self.first[index] = value
    def get_previous(self): return self.previous
    def set_previous(self, previous): self.previous = previous
    def add_previous(self, value): self.previous.append(value)
    def insert_previous(self, index, value): self.previous[index] = value
    def get_next(self): return self.next_
    def set_next(self, next_): self.next_ = next_
    def add_next(self, value): self.next_.append(value)
    def insert_next(self, index, value): self.next_[index] = value
    def get_last(self): return self.last
    def set_last(self, last): self.last = last
    def add_last(self, value): self.last.append(value)
    def insert_last(self, index, value): self.last[index] = value
    def get_reference(self): return self.reference
    def set_reference(self, reference): self.reference = reference
    def add_reference(self, value): self.reference.append(value)
    def insert_reference(self, index, value): self.reference[index] = value
    def hasContent_(self):
        if (
            self.identifier is not None or
            self.outcome is not None or
            self.total is not None or
            self.parameter or
            self.first or
            self.previous or
            self.next_ or
            self.last or
            self.reference or
            super(Query_Response, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Query.Response', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Query.Response')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Query.Response', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Query.Response'):
        super(Query_Response, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Query.Response')
    def exportChildren(self, outfile, level, namespace_='', name_='Query.Response', fromsubclass_=False, pretty_print=True):
        super(Query_Response, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.identifier is not None:
            self.identifier.export(outfile, level, namespace_, name_='identifier', pretty_print=pretty_print)
        if self.outcome is not None:
            self.outcome.export(outfile, level, namespace_, name_='outcome', pretty_print=pretty_print)
        if self.total is not None:
            self.total.export(outfile, level, namespace_, name_='total', pretty_print=pretty_print)
        for parameter_ in self.parameter:
            parameter_.export(outfile, level, namespace_, name_='parameter', pretty_print=pretty_print)
        for first_ in self.first:
            first_.export(outfile, level, namespace_, name_='first', pretty_print=pretty_print)
        for previous_ in self.previous:
            previous_.export(outfile, level, namespace_, name_='previous', pretty_print=pretty_print)
        for next_ in self.next_:
            next_.export(outfile, level, namespace_, name_='next', pretty_print=pretty_print)
        for last_ in self.last:
            last_.export(outfile, level, namespace_, name_='last', pretty_print=pretty_print)
        for reference_ in self.reference:
            reference_.export(outfile, level, namespace_, name_='reference', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Query.Response', mapping_=None):
        element = super(Query_Response, self).to_etree(parent_element, name_, mapping_)
        if self.identifier is not None:
            identifier_ = self.identifier
            identifier_.to_etree(element, name_='identifier', mapping_=mapping_)
        if self.outcome is not None:
            outcome_ = self.outcome
            outcome_.to_etree(element, name_='outcome', mapping_=mapping_)
        if self.total is not None:
            total_ = self.total
            total_.to_etree(element, name_='total', mapping_=mapping_)
        for parameter_ in self.parameter:
            parameter_.to_etree(element, name_='parameter', mapping_=mapping_)
        for first_ in self.first:
            first_.to_etree(element, name_='first', mapping_=mapping_)
        for previous_ in self.previous:
            previous_.to_etree(element, name_='previous', mapping_=mapping_)
        for next_ in self.next_:
            next_.to_etree(element, name_='next', mapping_=mapping_)
        for last_ in self.last:
            last_.to_etree(element, name_='last', mapping_=mapping_)
        for reference_ in self.reference:
            reference_.to_etree(element, name_='reference', mapping_=mapping_)
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
        super(Query_Response, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'identifier':
            obj_ = uri.factory()
            obj_.build(child_)
            self.identifier = obj_
            obj_.original_tagname_ = 'identifier'
        elif nodeName_ == 'outcome':
            obj_ = QueryOutcome.factory()
            obj_.build(child_)
            self.outcome = obj_
            obj_.original_tagname_ = 'outcome'
        elif nodeName_ == 'total':
            obj_ = integer.factory()
            obj_.build(child_)
            self.total = obj_
            obj_.original_tagname_ = 'total'
        elif nodeName_ == 'parameter':
            obj_ = Extension.factory()
            obj_.build(child_)
            self.parameter.append(obj_)
            obj_.original_tagname_ = 'parameter'
        elif nodeName_ == 'first':
            obj_ = Extension.factory()
            obj_.build(child_)
            self.first.append(obj_)
            obj_.original_tagname_ = 'first'
        elif nodeName_ == 'previous':
            obj_ = Extension.factory()
            obj_.build(child_)
            self.previous.append(obj_)
            obj_.original_tagname_ = 'previous'
        elif nodeName_ == 'next':
            obj_ = Extension.factory()
            obj_.build(child_)
            self.next_.append(obj_)
            obj_.original_tagname_ = 'next'
        elif nodeName_ == 'last':
            obj_ = Extension.factory()
            obj_.build(child_)
            self.last.append(obj_)
            obj_.original_tagname_ = 'last'
        elif nodeName_ == 'reference':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.reference.append(obj_)
            obj_.original_tagname_ = 'reference'
        super(Query_Response, self).buildChildren(child_, node, nodeName_, True)
# end class Query_Response


class QueryOutcome(Element):
    """The outcome of processing a query requestIf the element is present,
    it must have either a @value, an @id, or extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(QueryOutcome, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if QueryOutcome.subclass:
            return QueryOutcome.subclass(*args_, **kwargs_)
        else:
            return QueryOutcome(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(QueryOutcome, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='QueryOutcome', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='QueryOutcome')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='QueryOutcome', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='QueryOutcome'):
        super(QueryOutcome, self).exportAttributes(outfile, level, already_processed, namespace_, name_='QueryOutcome')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='QueryOutcome', fromsubclass_=False, pretty_print=True):
        super(QueryOutcome, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='QueryOutcome', mapping_=None):
        element = super(QueryOutcome, self).to_etree(parent_element, name_, mapping_)
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
        super(QueryOutcome, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(QueryOutcome, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class QueryOutcome
