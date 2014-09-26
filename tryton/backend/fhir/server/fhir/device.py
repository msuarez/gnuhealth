from .base_classes import *
from .support_functions import *


class Device(Resource):
    """This resource identifies an instance of a manufactured thing that is
    used in the provision of healthcare without being substantially
    changed through that activity. The device may be a machine, an
    insert, a computer, an application, etc. This includes durable
    (reusable) medical equipment as well as disposable equipment
    used for diagnostic, treatment, and research for healthcare and
    public health.If the element is present, it must have either a
    @value, an @id, or extensions"""
    subclass = None
    superclass = Resource
    def __init__(self, id=None, extension=None, modifierExtension=None, language=None, text=None, contained=None, identifier=None, type_=None, manufacturer=None, model=None, version=None, expiry=None, udi=None, lotNumber=None, owner=None, location=None, patient=None, contact=None, url=None):
        self.original_tagname_ = None
        super(Device, self).__init__(id, extension, modifierExtension, language, text, contained, )
        if identifier is None:
            self.identifier = []
        else:
            self.identifier = identifier
        self.type_ = type_
        self.manufacturer = manufacturer
        self.model = model
        self.version = version
        self.expiry = expiry
        self.udi = udi
        self.lotNumber = lotNumber
        self.owner = owner
        self.location = location
        self.patient = patient
        if contact is None:
            self.contact = []
        else:
            self.contact = contact
        self.url = url
    def factory(*args_, **kwargs_):
        if Device.subclass:
            return Device.subclass(*args_, **kwargs_)
        else:
            return Device(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_identifier(self): return self.identifier
    def set_identifier(self, identifier): self.identifier = identifier
    def add_identifier(self, value): self.identifier.append(value)
    def insert_identifier(self, index, value): self.identifier[index] = value
    def get_type(self): return self.type_
    def set_type(self, type_): self.type_ = type_
    def get_manufacturer(self): return self.manufacturer
    def set_manufacturer(self, manufacturer): self.manufacturer = manufacturer
    def get_model(self): return self.model
    def set_model(self, model): self.model = model
    def get_version(self): return self.version
    def set_version(self, version): self.version = version
    def get_expiry(self): return self.expiry
    def set_expiry(self, expiry): self.expiry = expiry
    def get_udi(self): return self.udi
    def set_udi(self, udi): self.udi = udi
    def get_lotNumber(self): return self.lotNumber
    def set_lotNumber(self, lotNumber): self.lotNumber = lotNumber
    def get_owner(self): return self.owner
    def set_owner(self, owner): self.owner = owner
    def get_location(self): return self.location
    def set_location(self, location): self.location = location
    def get_patient(self): return self.patient
    def set_patient(self, patient): self.patient = patient
    def get_contact(self): return self.contact
    def set_contact(self, contact): self.contact = contact
    def add_contact(self, value): self.contact.append(value)
    def insert_contact(self, index, value): self.contact[index] = value
    def get_url(self): return self.url
    def set_url(self, url): self.url = url
    def hasContent_(self):
        if (
            self.identifier or
            self.type_ is not None or
            self.manufacturer is not None or
            self.model is not None or
            self.version is not None or
            self.expiry is not None or
            self.udi is not None or
            self.lotNumber is not None or
            self.owner is not None or
            self.location is not None or
            self.patient is not None or
            self.contact or
            self.url is not None or
            super(Device, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Device', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Device')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Device', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Device'):
        super(Device, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Device')
    def exportChildren(self, outfile, level, namespace_='', name_='Device', fromsubclass_=False, pretty_print=True):
        super(Device, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for identifier_ in self.identifier:
            identifier_.export(outfile, level, namespace_, name_='identifier', pretty_print=pretty_print)
        if self.type_ is not None:
            self.type_.export(outfile, level, namespace_, name_='type', pretty_print=pretty_print)
        if self.manufacturer is not None:
            self.manufacturer.export(outfile, level, namespace_, name_='manufacturer', pretty_print=pretty_print)
        if self.model is not None:
            self.model.export(outfile, level, namespace_, name_='model', pretty_print=pretty_print)
        if self.version is not None:
            self.version.export(outfile, level, namespace_, name_='version', pretty_print=pretty_print)
        if self.expiry is not None:
            self.expiry.export(outfile, level, namespace_, name_='expiry', pretty_print=pretty_print)
        if self.udi is not None:
            self.udi.export(outfile, level, namespace_, name_='udi', pretty_print=pretty_print)
        if self.lotNumber is not None:
            self.lotNumber.export(outfile, level, namespace_, name_='lotNumber', pretty_print=pretty_print)
        if self.owner is not None:
            self.owner.export(outfile, level, namespace_, name_='owner', pretty_print=pretty_print)
        if self.location is not None:
            self.location.export(outfile, level, namespace_, name_='location', pretty_print=pretty_print)
        if self.patient is not None:
            self.patient.export(outfile, level, namespace_, name_='patient', pretty_print=pretty_print)
        for contact_ in self.contact:
            contact_.export(outfile, level, namespace_, name_='contact', pretty_print=pretty_print)
        if self.url is not None:
            self.url.export(outfile, level, namespace_, name_='url', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Device', mapping_=None):
        element = super(Device, self).to_etree(parent_element, name_, mapping_)
        for identifier_ in self.identifier:
            identifier_.to_etree(element, name_='identifier', mapping_=mapping_)
        if self.type_ is not None:
            type__ = self.type_
            type__.to_etree(element, name_='type', mapping_=mapping_)
        if self.manufacturer is not None:
            manufacturer_ = self.manufacturer
            manufacturer_.to_etree(element, name_='manufacturer', mapping_=mapping_)
        if self.model is not None:
            model_ = self.model
            model_.to_etree(element, name_='model', mapping_=mapping_)
        if self.version is not None:
            version_ = self.version
            version_.to_etree(element, name_='version', mapping_=mapping_)
        if self.expiry is not None:
            expiry_ = self.expiry
            expiry_.to_etree(element, name_='expiry', mapping_=mapping_)
        if self.udi is not None:
            udi_ = self.udi
            udi_.to_etree(element, name_='udi', mapping_=mapping_)
        if self.lotNumber is not None:
            lotNumber_ = self.lotNumber
            lotNumber_.to_etree(element, name_='lotNumber', mapping_=mapping_)
        if self.owner is not None:
            owner_ = self.owner
            owner_.to_etree(element, name_='owner', mapping_=mapping_)
        if self.location is not None:
            location_ = self.location
            location_.to_etree(element, name_='location', mapping_=mapping_)
        if self.patient is not None:
            patient_ = self.patient
            patient_.to_etree(element, name_='patient', mapping_=mapping_)
        for contact_ in self.contact:
            contact_.to_etree(element, name_='contact', mapping_=mapping_)
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
        super(Device, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'identifier':
            obj_ = Identifier.factory()
            obj_.build(child_)
            self.identifier.append(obj_)
            obj_.original_tagname_ = 'identifier'
        elif nodeName_ == 'type':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.type_ = obj_
            obj_.original_tagname_ = 'type'
        elif nodeName_ == 'manufacturer':
            obj_ = string.factory()
            obj_.build(child_)
            self.manufacturer = obj_
            obj_.original_tagname_ = 'manufacturer'
        elif nodeName_ == 'model':
            obj_ = string.factory()
            obj_.build(child_)
            self.model = obj_
            obj_.original_tagname_ = 'model'
        elif nodeName_ == 'version':
            obj_ = string.factory()
            obj_.build(child_)
            self.version = obj_
            obj_.original_tagname_ = 'version'
        elif nodeName_ == 'expiry':
            obj_ = date.factory()
            obj_.build(child_)
            self.expiry = obj_
            obj_.original_tagname_ = 'expiry'
        elif nodeName_ == 'udi':
            obj_ = string.factory()
            obj_.build(child_)
            self.udi = obj_
            obj_.original_tagname_ = 'udi'
        elif nodeName_ == 'lotNumber':
            obj_ = string.factory()
            obj_.build(child_)
            self.lotNumber = obj_
            obj_.original_tagname_ = 'lotNumber'
        elif nodeName_ == 'owner':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.owner = obj_
            obj_.original_tagname_ = 'owner'
        elif nodeName_ == 'location':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.location = obj_
            obj_.original_tagname_ = 'location'
        elif nodeName_ == 'patient':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.patient = obj_
            obj_.original_tagname_ = 'patient'
        elif nodeName_ == 'contact':
            obj_ = Contact.factory()
            obj_.build(child_)
            self.contact.append(obj_)
            obj_.original_tagname_ = 'contact'
        elif nodeName_ == 'url':
            obj_ = uri.factory()
            obj_.build(child_)
            self.url = obj_
            obj_.original_tagname_ = 'url'
        super(Device, self).buildChildren(child_, node, nodeName_, True)
# end class Device
