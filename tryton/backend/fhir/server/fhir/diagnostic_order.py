from .base_classes import *
from .support_functions import *


class DiagnosticOrder(Resource):
    """A request for a diagnostic investigation service to be performed.If
    the element is present, it must have either a @value, an @id, or
    extensions"""
    subclass = None
    superclass = Resource
    def __init__(self, id=None, extension=None, modifierExtension=None, language=None, text=None, contained=None, subject=None, orderer=None, identifier=None, encounter=None, clinicalNotes=None, specimen=None, status=None, priority=None, event=None, item=None):
        self.original_tagname_ = None
        super(DiagnosticOrder, self).__init__(id, extension, modifierExtension, language, text, contained, )
        self.subject = subject
        self.orderer = orderer
        if identifier is None:
            self.identifier = []
        else:
            self.identifier = identifier
        self.encounter = encounter
        self.clinicalNotes = clinicalNotes
        if specimen is None:
            self.specimen = []
        else:
            self.specimen = specimen
        self.status = status
        self.priority = priority
        if event is None:
            self.event = []
        else:
            self.event = event
        if item is None:
            self.item = []
        else:
            self.item = item
    def factory(*args_, **kwargs_):
        if DiagnosticOrder.subclass:
            return DiagnosticOrder.subclass(*args_, **kwargs_)
        else:
            return DiagnosticOrder(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_subject(self): return self.subject
    def set_subject(self, subject): self.subject = subject
    def get_orderer(self): return self.orderer
    def set_orderer(self, orderer): self.orderer = orderer
    def get_identifier(self): return self.identifier
    def set_identifier(self, identifier): self.identifier = identifier
    def add_identifier(self, value): self.identifier.append(value)
    def insert_identifier(self, index, value): self.identifier[index] = value
    def get_encounter(self): return self.encounter
    def set_encounter(self, encounter): self.encounter = encounter
    def get_clinicalNotes(self): return self.clinicalNotes
    def set_clinicalNotes(self, clinicalNotes): self.clinicalNotes = clinicalNotes
    def get_specimen(self): return self.specimen
    def set_specimen(self, specimen): self.specimen = specimen
    def add_specimen(self, value): self.specimen.append(value)
    def insert_specimen(self, index, value): self.specimen[index] = value
    def get_status(self): return self.status
    def set_status(self, status): self.status = status
    def get_priority(self): return self.priority
    def set_priority(self, priority): self.priority = priority
    def get_event(self): return self.event
    def set_event(self, event): self.event = event
    def add_event(self, value): self.event.append(value)
    def insert_event(self, index, value): self.event[index] = value
    def get_item(self): return self.item
    def set_item(self, item): self.item = item
    def add_item(self, value): self.item.append(value)
    def insert_item(self, index, value): self.item[index] = value
    def hasContent_(self):
        if (
            self.subject is not None or
            self.orderer is not None or
            self.identifier or
            self.encounter is not None or
            self.clinicalNotes is not None or
            self.specimen or
            self.status is not None or
            self.priority is not None or
            self.event or
            self.item or
            super(DiagnosticOrder, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='DiagnosticOrder', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='DiagnosticOrder')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='DiagnosticOrder', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='DiagnosticOrder'):
        super(DiagnosticOrder, self).exportAttributes(outfile, level, already_processed, namespace_, name_='DiagnosticOrder')
    def exportChildren(self, outfile, level, namespace_='', name_='DiagnosticOrder', fromsubclass_=False, pretty_print=True):
        super(DiagnosticOrder, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.subject is not None:
            self.subject.export(outfile, level, namespace_, name_='subject', pretty_print=pretty_print)
        if self.orderer is not None:
            self.orderer.export(outfile, level, namespace_, name_='orderer', pretty_print=pretty_print)
        for identifier_ in self.identifier:
            identifier_.export(outfile, level, namespace_, name_='identifier', pretty_print=pretty_print)
        if self.encounter is not None:
            self.encounter.export(outfile, level, namespace_, name_='encounter', pretty_print=pretty_print)
        if self.clinicalNotes is not None:
            self.clinicalNotes.export(outfile, level, namespace_, name_='clinicalNotes', pretty_print=pretty_print)
        for specimen_ in self.specimen:
            specimen_.export(outfile, level, namespace_, name_='specimen', pretty_print=pretty_print)
        if self.status is not None:
            self.status.export(outfile, level, namespace_, name_='status', pretty_print=pretty_print)
        if self.priority is not None:
            self.priority.export(outfile, level, namespace_, name_='priority', pretty_print=pretty_print)
        for event_ in self.event:
            event_.export(outfile, level, namespace_, name_='event', pretty_print=pretty_print)
        for item_ in self.item:
            item_.export(outfile, level, namespace_, name_='item', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='DiagnosticOrder', mapping_=None):
        element = super(DiagnosticOrder, self).to_etree(parent_element, name_, mapping_)
        if self.subject is not None:
            subject_ = self.subject
            subject_.to_etree(element, name_='subject', mapping_=mapping_)
        if self.orderer is not None:
            orderer_ = self.orderer
            orderer_.to_etree(element, name_='orderer', mapping_=mapping_)
        for identifier_ in self.identifier:
            identifier_.to_etree(element, name_='identifier', mapping_=mapping_)
        if self.encounter is not None:
            encounter_ = self.encounter
            encounter_.to_etree(element, name_='encounter', mapping_=mapping_)
        if self.clinicalNotes is not None:
            clinicalNotes_ = self.clinicalNotes
            clinicalNotes_.to_etree(element, name_='clinicalNotes', mapping_=mapping_)
        for specimen_ in self.specimen:
            specimen_.to_etree(element, name_='specimen', mapping_=mapping_)
        if self.status is not None:
            status_ = self.status
            status_.to_etree(element, name_='status', mapping_=mapping_)
        if self.priority is not None:
            priority_ = self.priority
            priority_.to_etree(element, name_='priority', mapping_=mapping_)
        for event_ in self.event:
            event_.to_etree(element, name_='event', mapping_=mapping_)
        for item_ in self.item:
            item_.to_etree(element, name_='item', mapping_=mapping_)
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
        super(DiagnosticOrder, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'subject':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.subject = obj_
            obj_.original_tagname_ = 'subject'
        elif nodeName_ == 'orderer':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.orderer = obj_
            obj_.original_tagname_ = 'orderer'
        elif nodeName_ == 'identifier':
            obj_ = Identifier.factory()
            obj_.build(child_)
            self.identifier.append(obj_)
            obj_.original_tagname_ = 'identifier'
        elif nodeName_ == 'encounter':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.encounter = obj_
            obj_.original_tagname_ = 'encounter'
        elif nodeName_ == 'clinicalNotes':
            obj_ = string.factory()
            obj_.build(child_)
            self.clinicalNotes = obj_
            obj_.original_tagname_ = 'clinicalNotes'
        elif nodeName_ == 'specimen':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.specimen.append(obj_)
            obj_.original_tagname_ = 'specimen'
        elif nodeName_ == 'status':
            obj_ = DiagnosticOrderStatus.factory()
            obj_.build(child_)
            self.status = obj_
            obj_.original_tagname_ = 'status'
        elif nodeName_ == 'priority':
            obj_ = DiagnosticOrderPriority.factory()
            obj_.build(child_)
            self.priority = obj_
            obj_.original_tagname_ = 'priority'
        elif nodeName_ == 'event':
            obj_ = DiagnosticOrder_Event.factory()
            obj_.build(child_)
            self.event.append(obj_)
            obj_.original_tagname_ = 'event'
        elif nodeName_ == 'item':
            obj_ = DiagnosticOrder_Item.factory()
            obj_.build(child_)
            self.item.append(obj_)
            obj_.original_tagname_ = 'item'
        super(DiagnosticOrder, self).buildChildren(child_, node, nodeName_, True)
# end class DiagnosticOrder


class DiagnosticOrder_Event(BackboneElement):
    """A request for a diagnostic investigation service to be performed."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, status=None, description=None, dateTime=None, actor=None):
        self.original_tagname_ = None
        super(DiagnosticOrder_Event, self).__init__(id, extension, modifierExtension, )
        self.status = status
        self.description = description
        self.dateTime = dateTime
        self.actor = actor
    def factory(*args_, **kwargs_):
        if DiagnosticOrder_Event.subclass:
            return DiagnosticOrder_Event.subclass(*args_, **kwargs_)
        else:
            return DiagnosticOrder_Event(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_status(self): return self.status
    def set_status(self, status): self.status = status
    def get_description(self): return self.description
    def set_description(self, description): self.description = description
    def get_dateTime(self): return self.dateTime
    def set_dateTime(self, dateTime): self.dateTime = dateTime
    def get_actor(self): return self.actor
    def set_actor(self, actor): self.actor = actor
    def hasContent_(self):
        if (
            self.status is not None or
            self.description is not None or
            self.dateTime is not None or
            self.actor is not None or
            super(DiagnosticOrder_Event, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='DiagnosticOrder.Event', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='DiagnosticOrder.Event')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='DiagnosticOrder.Event', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='DiagnosticOrder.Event'):
        super(DiagnosticOrder_Event, self).exportAttributes(outfile, level, already_processed, namespace_, name_='DiagnosticOrder.Event')
    def exportChildren(self, outfile, level, namespace_='', name_='DiagnosticOrder.Event', fromsubclass_=False, pretty_print=True):
        super(DiagnosticOrder_Event, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.status is not None:
            self.status.export(outfile, level, namespace_, name_='status', pretty_print=pretty_print)
        if self.description is not None:
            self.description.export(outfile, level, namespace_, name_='description', pretty_print=pretty_print)
        if self.dateTime is not None:
            self.dateTime.export(outfile, level, namespace_, name_='dateTime', pretty_print=pretty_print)
        if self.actor is not None:
            self.actor.export(outfile, level, namespace_, name_='actor', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='DiagnosticOrder.Event', mapping_=None):
        element = super(DiagnosticOrder_Event, self).to_etree(parent_element, name_, mapping_)
        if self.status is not None:
            status_ = self.status
            status_.to_etree(element, name_='status', mapping_=mapping_)
        if self.description is not None:
            description_ = self.description
            description_.to_etree(element, name_='description', mapping_=mapping_)
        if self.dateTime is not None:
            dateTime_ = self.dateTime
            dateTime_.to_etree(element, name_='dateTime', mapping_=mapping_)
        if self.actor is not None:
            actor_ = self.actor
            actor_.to_etree(element, name_='actor', mapping_=mapping_)
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
        super(DiagnosticOrder_Event, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'status':
            obj_ = DiagnosticOrderStatus.factory()
            obj_.build(child_)
            self.status = obj_
            obj_.original_tagname_ = 'status'
        elif nodeName_ == 'description':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.description = obj_
            obj_.original_tagname_ = 'description'
        elif nodeName_ == 'dateTime':
            obj_ = dateTime.factory()
            obj_.build(child_)
            self.dateTime = obj_
            obj_.original_tagname_ = 'dateTime'
        elif nodeName_ == 'actor':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.actor = obj_
            obj_.original_tagname_ = 'actor'
        super(DiagnosticOrder_Event, self).buildChildren(child_, node, nodeName_, True)
# end class DiagnosticOrder_Event


class DiagnosticOrder_Item(BackboneElement):
    """A request for a diagnostic investigation service to be performed."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, code=None, specimen=None, bodySite=None, status=None, event=None):
        self.original_tagname_ = None
        super(DiagnosticOrder_Item, self).__init__(id, extension, modifierExtension, )
        self.code = code
        if specimen is None:
            self.specimen = []
        else:
            self.specimen = specimen
        self.bodySite = bodySite
        self.status = status
        if event is None:
            self.event = []
        else:
            self.event = event
    def factory(*args_, **kwargs_):
        if DiagnosticOrder_Item.subclass:
            return DiagnosticOrder_Item.subclass(*args_, **kwargs_)
        else:
            return DiagnosticOrder_Item(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_code(self): return self.code
    def set_code(self, code): self.code = code
    def get_specimen(self): return self.specimen
    def set_specimen(self, specimen): self.specimen = specimen
    def add_specimen(self, value): self.specimen.append(value)
    def insert_specimen(self, index, value): self.specimen[index] = value
    def get_bodySite(self): return self.bodySite
    def set_bodySite(self, bodySite): self.bodySite = bodySite
    def get_status(self): return self.status
    def set_status(self, status): self.status = status
    def get_event(self): return self.event
    def set_event(self, event): self.event = event
    def add_event(self, value): self.event.append(value)
    def insert_event(self, index, value): self.event[index] = value
    def hasContent_(self):
        if (
            self.code is not None or
            self.specimen or
            self.bodySite is not None or
            self.status is not None or
            self.event or
            super(DiagnosticOrder_Item, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='DiagnosticOrder.Item', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='DiagnosticOrder.Item')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='DiagnosticOrder.Item', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='DiagnosticOrder.Item'):
        super(DiagnosticOrder_Item, self).exportAttributes(outfile, level, already_processed, namespace_, name_='DiagnosticOrder.Item')
    def exportChildren(self, outfile, level, namespace_='', name_='DiagnosticOrder.Item', fromsubclass_=False, pretty_print=True):
        super(DiagnosticOrder_Item, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.code is not None:
            self.code.export(outfile, level, namespace_, name_='code', pretty_print=pretty_print)
        for specimen_ in self.specimen:
            specimen_.export(outfile, level, namespace_, name_='specimen', pretty_print=pretty_print)
        if self.bodySite is not None:
            self.bodySite.export(outfile, level, namespace_, name_='bodySite', pretty_print=pretty_print)
        if self.status is not None:
            self.status.export(outfile, level, namespace_, name_='status', pretty_print=pretty_print)
        for event_ in self.event:
            event_.export(outfile, level, namespace_, name_='event', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='DiagnosticOrder.Item', mapping_=None):
        element = super(DiagnosticOrder_Item, self).to_etree(parent_element, name_, mapping_)
        if self.code is not None:
            code_ = self.code
            code_.to_etree(element, name_='code', mapping_=mapping_)
        for specimen_ in self.specimen:
            specimen_.to_etree(element, name_='specimen', mapping_=mapping_)
        if self.bodySite is not None:
            bodySite_ = self.bodySite
            bodySite_.to_etree(element, name_='bodySite', mapping_=mapping_)
        if self.status is not None:
            status_ = self.status
            status_.to_etree(element, name_='status', mapping_=mapping_)
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
        super(DiagnosticOrder_Item, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'code':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.code = obj_
            obj_.original_tagname_ = 'code'
        elif nodeName_ == 'specimen':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.specimen.append(obj_)
            obj_.original_tagname_ = 'specimen'
        elif nodeName_ == 'bodySite':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.bodySite = obj_
            obj_.original_tagname_ = 'bodySite'
        elif nodeName_ == 'status':
            obj_ = DiagnosticOrderStatus.factory()
            obj_.build(child_)
            self.status = obj_
            obj_.original_tagname_ = 'status'
        elif nodeName_ == 'event':
            obj_ = DiagnosticOrder_Event.factory()
            obj_.build(child_)
            self.event.append(obj_)
            obj_.original_tagname_ = 'event'
        super(DiagnosticOrder_Item, self).buildChildren(child_, node, nodeName_, True)
# end class DiagnosticOrder_Item


class DiagnosticOrderStatus(Element):
    """The status of a diagnostic orderIf the element is present, it must
    have either a @value, an @id, or extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(DiagnosticOrderStatus, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if DiagnosticOrderStatus.subclass:
            return DiagnosticOrderStatus.subclass(*args_, **kwargs_)
        else:
            return DiagnosticOrderStatus(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(DiagnosticOrderStatus, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='DiagnosticOrderStatus', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='DiagnosticOrderStatus')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='DiagnosticOrderStatus', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='DiagnosticOrderStatus'):
        super(DiagnosticOrderStatus, self).exportAttributes(outfile, level, already_processed, namespace_, name_='DiagnosticOrderStatus')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='DiagnosticOrderStatus', fromsubclass_=False, pretty_print=True):
        super(DiagnosticOrderStatus, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='DiagnosticOrderStatus', mapping_=None):
        element = super(DiagnosticOrderStatus, self).to_etree(parent_element, name_, mapping_)
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
        super(DiagnosticOrderStatus, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(DiagnosticOrderStatus, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class DiagnosticOrderStatus


class DiagnosticOrderPriority(Element):
    """The clinical priority of a diagnostic orderIf the element is
    present, it must have either a @value, an @id, or extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(DiagnosticOrderPriority, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if DiagnosticOrderPriority.subclass:
            return DiagnosticOrderPriority.subclass(*args_, **kwargs_)
        else:
            return DiagnosticOrderPriority(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(DiagnosticOrderPriority, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='DiagnosticOrderPriority', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='DiagnosticOrderPriority')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='DiagnosticOrderPriority', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='DiagnosticOrderPriority'):
        super(DiagnosticOrderPriority, self).exportAttributes(outfile, level, already_processed, namespace_, name_='DiagnosticOrderPriority')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='DiagnosticOrderPriority', fromsubclass_=False, pretty_print=True):
        super(DiagnosticOrderPriority, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='DiagnosticOrderPriority', mapping_=None):
        element = super(DiagnosticOrderPriority, self).to_etree(parent_element, name_, mapping_)
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
        super(DiagnosticOrderPriority, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(DiagnosticOrderPriority, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class DiagnosticOrderPriority
