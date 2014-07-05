from .base_classes import *
from .support_functions import *


class Order(Resource):
    """A request to perform an action.If the element is present, it must
    have either a @value, an @id, or extensionsText - why the order
    was made."""
    subclass = None
    superclass = Resource
    def __init__(self, id=None, extension=None, modifierExtension=None, language=None, text=None, contained=None, identifier=None, date=None, subject=None, source=None, target=None, reasonCodeableConcept=None, reasonResource=None, authority=None, when=None, detail=None):
        self.original_tagname_ = None
        super(Order, self).__init__(id, extension, modifierExtension, language, text, contained, )
        if identifier is None:
            self.identifier = []
        else:
            self.identifier = identifier
        self.date = date
        self.subject = subject
        self.source = source
        self.target = target
        self.reasonCodeableConcept = reasonCodeableConcept
        self.reasonResource = reasonResource
        self.authority = authority
        self.when = when
        if detail is None:
            self.detail = []
        else:
            self.detail = detail
    def factory(*args_, **kwargs_):
        if Order.subclass:
            return Order.subclass(*args_, **kwargs_)
        else:
            return Order(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_identifier(self): return self.identifier
    def set_identifier(self, identifier): self.identifier = identifier
    def add_identifier(self, value): self.identifier.append(value)
    def insert_identifier(self, index, value): self.identifier[index] = value
    def get_date(self): return self.date
    def set_date(self, date): self.date = date
    def get_subject(self): return self.subject
    def set_subject(self, subject): self.subject = subject
    def get_source(self): return self.source
    def set_source(self, source): self.source = source
    def get_target(self): return self.target
    def set_target(self, target): self.target = target
    def get_reasonCodeableConcept(self): return self.reasonCodeableConcept
    def set_reasonCodeableConcept(self, reasonCodeableConcept): self.reasonCodeableConcept = reasonCodeableConcept
    def get_reasonResource(self): return self.reasonResource
    def set_reasonResource(self, reasonResource): self.reasonResource = reasonResource
    def get_authority(self): return self.authority
    def set_authority(self, authority): self.authority = authority
    def get_when(self): return self.when
    def set_when(self, when): self.when = when
    def get_detail(self): return self.detail
    def set_detail(self, detail): self.detail = detail
    def add_detail(self, value): self.detail.append(value)
    def insert_detail(self, index, value): self.detail[index] = value
    def hasContent_(self):
        if (
            self.identifier or
            self.date is not None or
            self.subject is not None or
            self.source is not None or
            self.target is not None or
            self.reasonCodeableConcept is not None or
            self.reasonResource is not None or
            self.authority is not None or
            self.when is not None or
            self.detail or
            super(Order, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Order', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Order')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Order', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Order'):
        super(Order, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Order')
    def exportChildren(self, outfile, level, namespace_='', name_='Order', fromsubclass_=False, pretty_print=True):
        super(Order, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
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
        if self.source is not None:
            self.source.export(outfile, level, namespace_, name_='source', pretty_print=pretty_print)
        if self.target is not None:
            self.target.export(outfile, level, namespace_, name_='target', pretty_print=pretty_print)
        if self.reasonCodeableConcept is not None:
            self.reasonCodeableConcept.export(outfile, level, namespace_, name_='reasonCodeableConcept', pretty_print=pretty_print)
        if self.reasonResource is not None:
            self.reasonResource.export(outfile, level, namespace_, name_='reasonResource', pretty_print=pretty_print)
        if self.authority is not None:
            self.authority.export(outfile, level, namespace_, name_='authority', pretty_print=pretty_print)
        if self.when is not None:
            self.when.export(outfile, level, namespace_, name_='when', pretty_print=pretty_print)
        for detail_ in self.detail:
            detail_.export(outfile, level, namespace_, name_='detail', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Order', mapping_=None):
        element = super(Order, self).to_etree(parent_element, name_, mapping_)
        for identifier_ in self.identifier:
            identifier_.to_etree(element, name_='identifier', mapping_=mapping_)
        if self.date is not None:
            date_ = self.date
            date_.to_etree(element, name_='date', mapping_=mapping_)
        if self.subject is not None:
            subject_ = self.subject
            subject_.to_etree(element, name_='subject', mapping_=mapping_)
        if self.source is not None:
            source_ = self.source
            source_.to_etree(element, name_='source', mapping_=mapping_)
        if self.target is not None:
            target_ = self.target
            target_.to_etree(element, name_='target', mapping_=mapping_)
        if self.reasonCodeableConcept is not None:
            reasonCodeableConcept_ = self.reasonCodeableConcept
            reasonCodeableConcept_.to_etree(element, name_='reasonCodeableConcept', mapping_=mapping_)
        if self.reasonResource is not None:
            reasonResource_ = self.reasonResource
            reasonResource_.to_etree(element, name_='reasonResource', mapping_=mapping_)
        if self.authority is not None:
            authority_ = self.authority
            authority_.to_etree(element, name_='authority', mapping_=mapping_)
        if self.when is not None:
            when_ = self.when
            when_.to_etree(element, name_='when', mapping_=mapping_)
        for detail_ in self.detail:
            detail_.to_etree(element, name_='detail', mapping_=mapping_)
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
        super(Order, self).buildAttributes(node, attrs, already_processed)
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
        elif nodeName_ == 'reasonCodeableConcept':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.reasonCodeableConcept = obj_
            obj_.original_tagname_ = 'reasonCodeableConcept'
        elif nodeName_ == 'reasonResource':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.reasonResource = obj_
            obj_.original_tagname_ = 'reasonResource'
        elif nodeName_ == 'authority':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.authority = obj_
            obj_.original_tagname_ = 'authority'
        elif nodeName_ == 'when':
            obj_ = Order_When.factory()
            obj_.build(child_)
            self.when = obj_
            obj_.original_tagname_ = 'when'
        elif nodeName_ == 'detail':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.detail.append(obj_)
            obj_.original_tagname_ = 'detail'
        super(Order, self).buildChildren(child_, node, nodeName_, True)
# end class Order


class Order_When(BackboneElement):
    """A request to perform an action."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, code=None, schedule=None):
        self.original_tagname_ = None
        super(Order_When, self).__init__(id, extension, modifierExtension, )
        self.code = code
        self.schedule = schedule
    def factory(*args_, **kwargs_):
        if Order_When.subclass:
            return Order_When.subclass(*args_, **kwargs_)
        else:
            return Order_When(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_code(self): return self.code
    def set_code(self, code): self.code = code
    def get_schedule(self): return self.schedule
    def set_schedule(self, schedule): self.schedule = schedule
    def hasContent_(self):
        if (
            self.code is not None or
            self.schedule is not None or
            super(Order_When, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Order.When', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Order.When')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Order.When', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Order.When'):
        super(Order_When, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Order.When')
    def exportChildren(self, outfile, level, namespace_='', name_='Order.When', fromsubclass_=False, pretty_print=True):
        super(Order_When, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.code is not None:
            self.code.export(outfile, level, namespace_, name_='code', pretty_print=pretty_print)
        if self.schedule is not None:
            self.schedule.export(outfile, level, namespace_, name_='schedule', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Order.When', mapping_=None):
        element = super(Order_When, self).to_etree(parent_element, name_, mapping_)
        if self.code is not None:
            code_ = self.code
            code_.to_etree(element, name_='code', mapping_=mapping_)
        if self.schedule is not None:
            schedule_ = self.schedule
            schedule_.to_etree(element, name_='schedule', mapping_=mapping_)
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
        super(Order_When, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'code':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.code = obj_
            obj_.original_tagname_ = 'code'
        elif nodeName_ == 'schedule':
            obj_ = Schedule.factory()
            obj_.build(child_)
            self.schedule = obj_
            obj_.original_tagname_ = 'schedule'
        super(Order_When, self).buildChildren(child_, node, nodeName_, True)
# end class Order_When
