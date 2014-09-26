from .base_classes import *
from .support_functions import *


class Supply(Resource):
    """A supply - a request for something, and provision of what is
    supplied.If the element is present, it must have either a
    @value, an @id, or extensions"""
    subclass = None
    superclass = Resource
    def __init__(self, id=None, extension=None, modifierExtension=None, language=None, text=None, contained=None, kind=None, identifier=None, status=None, orderedItem=None, patient=None, dispense=None):
        self.original_tagname_ = None
        super(Supply, self).__init__(id, extension, modifierExtension, language, text, contained, )
        self.kind = kind
        self.identifier = identifier
        self.status = status
        self.orderedItem = orderedItem
        self.patient = patient
        if dispense is None:
            self.dispense = []
        else:
            self.dispense = dispense
    def factory(*args_, **kwargs_):
        if Supply.subclass:
            return Supply.subclass(*args_, **kwargs_)
        else:
            return Supply(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_kind(self): return self.kind
    def set_kind(self, kind): self.kind = kind
    def get_identifier(self): return self.identifier
    def set_identifier(self, identifier): self.identifier = identifier
    def get_status(self): return self.status
    def set_status(self, status): self.status = status
    def get_orderedItem(self): return self.orderedItem
    def set_orderedItem(self, orderedItem): self.orderedItem = orderedItem
    def get_patient(self): return self.patient
    def set_patient(self, patient): self.patient = patient
    def get_dispense(self): return self.dispense
    def set_dispense(self, dispense): self.dispense = dispense
    def add_dispense(self, value): self.dispense.append(value)
    def insert_dispense(self, index, value): self.dispense[index] = value
    def hasContent_(self):
        if (
            self.kind is not None or
            self.identifier is not None or
            self.status is not None or
            self.orderedItem is not None or
            self.patient is not None or
            self.dispense or
            super(Supply, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Supply', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Supply')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Supply', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Supply'):
        super(Supply, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Supply')
    def exportChildren(self, outfile, level, namespace_='', name_='Supply', fromsubclass_=False, pretty_print=True):
        super(Supply, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.kind is not None:
            self.kind.export(outfile, level, namespace_, name_='kind', pretty_print=pretty_print)
        if self.identifier is not None:
            self.identifier.export(outfile, level, namespace_, name_='identifier', pretty_print=pretty_print)
        if self.status is not None:
            self.status.export(outfile, level, namespace_, name_='status', pretty_print=pretty_print)
        if self.orderedItem is not None:
            self.orderedItem.export(outfile, level, namespace_, name_='orderedItem', pretty_print=pretty_print)
        if self.patient is not None:
            self.patient.export(outfile, level, namespace_, name_='patient', pretty_print=pretty_print)
        for dispense_ in self.dispense:
            dispense_.export(outfile, level, namespace_, name_='dispense', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Supply', mapping_=None):
        element = super(Supply, self).to_etree(parent_element, name_, mapping_)
        if self.kind is not None:
            kind_ = self.kind
            kind_.to_etree(element, name_='kind', mapping_=mapping_)
        if self.identifier is not None:
            identifier_ = self.identifier
            identifier_.to_etree(element, name_='identifier', mapping_=mapping_)
        if self.status is not None:
            status_ = self.status
            status_.to_etree(element, name_='status', mapping_=mapping_)
        if self.orderedItem is not None:
            orderedItem_ = self.orderedItem
            orderedItem_.to_etree(element, name_='orderedItem', mapping_=mapping_)
        if self.patient is not None:
            patient_ = self.patient
            patient_.to_etree(element, name_='patient', mapping_=mapping_)
        for dispense_ in self.dispense:
            dispense_.to_etree(element, name_='dispense', mapping_=mapping_)
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
        super(Supply, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'kind':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.kind = obj_
            obj_.original_tagname_ = 'kind'
        elif nodeName_ == 'identifier':
            obj_ = Identifier.factory()
            obj_.build(child_)
            self.identifier = obj_
            obj_.original_tagname_ = 'identifier'
        elif nodeName_ == 'status':
            obj_ = SupplyStatus.factory()
            obj_.build(child_)
            self.status = obj_
            obj_.original_tagname_ = 'status'
        elif nodeName_ == 'orderedItem':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.orderedItem = obj_
            obj_.original_tagname_ = 'orderedItem'
        elif nodeName_ == 'patient':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.patient = obj_
            obj_.original_tagname_ = 'patient'
        elif nodeName_ == 'dispense':
            obj_ = Supply_Dispense.factory()
            obj_.build(child_)
            self.dispense.append(obj_)
            obj_.original_tagname_ = 'dispense'
        super(Supply, self).buildChildren(child_, node, nodeName_, True)
# end class Supply


class Supply_Dispense(BackboneElement):
    """A supply - a request for something, and provision of what is
    supplied."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, identifier=None, status=None, type_=None, quantity=None, suppliedItem=None, supplier=None, whenPrepared=None, whenHandedOver=None, destination=None, receiver=None):
        self.original_tagname_ = None
        super(Supply_Dispense, self).__init__(id, extension, modifierExtension, )
        self.identifier = identifier
        self.status = status
        self.type_ = type_
        self.quantity = quantity
        self.suppliedItem = suppliedItem
        self.supplier = supplier
        self.whenPrepared = whenPrepared
        self.whenHandedOver = whenHandedOver
        self.destination = destination
        if receiver is None:
            self.receiver = []
        else:
            self.receiver = receiver
    def factory(*args_, **kwargs_):
        if Supply_Dispense.subclass:
            return Supply_Dispense.subclass(*args_, **kwargs_)
        else:
            return Supply_Dispense(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_identifier(self): return self.identifier
    def set_identifier(self, identifier): self.identifier = identifier
    def get_status(self): return self.status
    def set_status(self, status): self.status = status
    def get_type(self): return self.type_
    def set_type(self, type_): self.type_ = type_
    def get_quantity(self): return self.quantity
    def set_quantity(self, quantity): self.quantity = quantity
    def get_suppliedItem(self): return self.suppliedItem
    def set_suppliedItem(self, suppliedItem): self.suppliedItem = suppliedItem
    def get_supplier(self): return self.supplier
    def set_supplier(self, supplier): self.supplier = supplier
    def get_whenPrepared(self): return self.whenPrepared
    def set_whenPrepared(self, whenPrepared): self.whenPrepared = whenPrepared
    def get_whenHandedOver(self): return self.whenHandedOver
    def set_whenHandedOver(self, whenHandedOver): self.whenHandedOver = whenHandedOver
    def get_destination(self): return self.destination
    def set_destination(self, destination): self.destination = destination
    def get_receiver(self): return self.receiver
    def set_receiver(self, receiver): self.receiver = receiver
    def add_receiver(self, value): self.receiver.append(value)
    def insert_receiver(self, index, value): self.receiver[index] = value
    def hasContent_(self):
        if (
            self.identifier is not None or
            self.status is not None or
            self.type_ is not None or
            self.quantity is not None or
            self.suppliedItem is not None or
            self.supplier is not None or
            self.whenPrepared is not None or
            self.whenHandedOver is not None or
            self.destination is not None or
            self.receiver or
            super(Supply_Dispense, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Supply.Dispense', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Supply.Dispense')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Supply.Dispense', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Supply.Dispense'):
        super(Supply_Dispense, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Supply.Dispense')
    def exportChildren(self, outfile, level, namespace_='', name_='Supply.Dispense', fromsubclass_=False, pretty_print=True):
        super(Supply_Dispense, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.identifier is not None:
            self.identifier.export(outfile, level, namespace_, name_='identifier', pretty_print=pretty_print)
        if self.status is not None:
            self.status.export(outfile, level, namespace_, name_='status', pretty_print=pretty_print)
        if self.type_ is not None:
            self.type_.export(outfile, level, namespace_, name_='type', pretty_print=pretty_print)
        if self.quantity is not None:
            self.quantity.export(outfile, level, namespace_, name_='quantity', pretty_print=pretty_print)
        if self.suppliedItem is not None:
            self.suppliedItem.export(outfile, level, namespace_, name_='suppliedItem', pretty_print=pretty_print)
        if self.supplier is not None:
            self.supplier.export(outfile, level, namespace_, name_='supplier', pretty_print=pretty_print)
        if self.whenPrepared is not None:
            self.whenPrepared.export(outfile, level, namespace_, name_='whenPrepared', pretty_print=pretty_print)
        if self.whenHandedOver is not None:
            self.whenHandedOver.export(outfile, level, namespace_, name_='whenHandedOver', pretty_print=pretty_print)
        if self.destination is not None:
            self.destination.export(outfile, level, namespace_, name_='destination', pretty_print=pretty_print)
        for receiver_ in self.receiver:
            receiver_.export(outfile, level, namespace_, name_='receiver', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Supply.Dispense', mapping_=None):
        element = super(Supply_Dispense, self).to_etree(parent_element, name_, mapping_)
        if self.identifier is not None:
            identifier_ = self.identifier
            identifier_.to_etree(element, name_='identifier', mapping_=mapping_)
        if self.status is not None:
            status_ = self.status
            status_.to_etree(element, name_='status', mapping_=mapping_)
        if self.type_ is not None:
            type__ = self.type_
            type__.to_etree(element, name_='type', mapping_=mapping_)
        if self.quantity is not None:
            quantity_ = self.quantity
            quantity_.to_etree(element, name_='quantity', mapping_=mapping_)
        if self.suppliedItem is not None:
            suppliedItem_ = self.suppliedItem
            suppliedItem_.to_etree(element, name_='suppliedItem', mapping_=mapping_)
        if self.supplier is not None:
            supplier_ = self.supplier
            supplier_.to_etree(element, name_='supplier', mapping_=mapping_)
        if self.whenPrepared is not None:
            whenPrepared_ = self.whenPrepared
            whenPrepared_.to_etree(element, name_='whenPrepared', mapping_=mapping_)
        if self.whenHandedOver is not None:
            whenHandedOver_ = self.whenHandedOver
            whenHandedOver_.to_etree(element, name_='whenHandedOver', mapping_=mapping_)
        if self.destination is not None:
            destination_ = self.destination
            destination_.to_etree(element, name_='destination', mapping_=mapping_)
        for receiver_ in self.receiver:
            receiver_.to_etree(element, name_='receiver', mapping_=mapping_)
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
        super(Supply_Dispense, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'identifier':
            obj_ = Identifier.factory()
            obj_.build(child_)
            self.identifier = obj_
            obj_.original_tagname_ = 'identifier'
        elif nodeName_ == 'status':
            obj_ = SupplyDispenseStatus.factory()
            obj_.build(child_)
            self.status = obj_
            obj_.original_tagname_ = 'status'
        elif nodeName_ == 'type':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.type_ = obj_
            obj_.original_tagname_ = 'type'
        elif nodeName_ == 'quantity':
            obj_ = Quantity.factory()
            obj_.build(child_)
            self.quantity = obj_
            obj_.original_tagname_ = 'quantity'
        elif nodeName_ == 'suppliedItem':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.suppliedItem = obj_
            obj_.original_tagname_ = 'suppliedItem'
        elif nodeName_ == 'supplier':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.supplier = obj_
            obj_.original_tagname_ = 'supplier'
        elif nodeName_ == 'whenPrepared':
            obj_ = Period.factory()
            obj_.build(child_)
            self.whenPrepared = obj_
            obj_.original_tagname_ = 'whenPrepared'
        elif nodeName_ == 'whenHandedOver':
            obj_ = Period.factory()
            obj_.build(child_)
            self.whenHandedOver = obj_
            obj_.original_tagname_ = 'whenHandedOver'
        elif nodeName_ == 'destination':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.destination = obj_
            obj_.original_tagname_ = 'destination'
        elif nodeName_ == 'receiver':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.receiver.append(obj_)
            obj_.original_tagname_ = 'receiver'
        super(Supply_Dispense, self).buildChildren(child_, node, nodeName_, True)
# end class Supply_Dispense


class SupplyDispenseStatus(Element):
    """Status of the dispenseIf the element is present, it must have either
    a @value, an @id, or extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(SupplyDispenseStatus, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if SupplyDispenseStatus.subclass:
            return SupplyDispenseStatus.subclass(*args_, **kwargs_)
        else:
            return SupplyDispenseStatus(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(SupplyDispenseStatus, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='SupplyDispenseStatus', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='SupplyDispenseStatus')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='SupplyDispenseStatus', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='SupplyDispenseStatus'):
        super(SupplyDispenseStatus, self).exportAttributes(outfile, level, already_processed, namespace_, name_='SupplyDispenseStatus')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='SupplyDispenseStatus', fromsubclass_=False, pretty_print=True):
        super(SupplyDispenseStatus, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='SupplyDispenseStatus', mapping_=None):
        element = super(SupplyDispenseStatus, self).to_etree(parent_element, name_, mapping_)
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
        super(SupplyDispenseStatus, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(SupplyDispenseStatus, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class SupplyDispenseStatus


class SupplyStatus(Element):
    """Status of the supplyIf the element is present, it must have either a
    @value, an @id, or extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(SupplyStatus, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if SupplyStatus.subclass:
            return SupplyStatus.subclass(*args_, **kwargs_)
        else:
            return SupplyStatus(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(SupplyStatus, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='SupplyStatus', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='SupplyStatus')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='SupplyStatus', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='SupplyStatus'):
        super(SupplyStatus, self).exportAttributes(outfile, level, already_processed, namespace_, name_='SupplyStatus')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='SupplyStatus', fromsubclass_=False, pretty_print=True):
        super(SupplyStatus, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='SupplyStatus', mapping_=None):
        element = super(SupplyStatus, self).to_etree(parent_element, name_, mapping_)
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
        super(SupplyStatus, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(SupplyStatus, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class SupplyStatus
