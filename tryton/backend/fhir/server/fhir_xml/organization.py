from .base_classes import *
from .support_functions import *


class Organization(Resource):
    """A formally or informally recognized grouping of people or
    organizations formed for the purpose of achieving some form of
    collective action. Includes companies, institutions,
    corporations, departments, community groups, healthcare practice
    groups, etc.If the element is present, it must have either a
    @value, an @id, or extensions"""
    subclass = None
    superclass = Resource
    def __init__(self, id=None, extension=None, modifierExtension=None, language=None, text=None, contained=None, identifier=None, name=None, type_=None, telecom=None, address=None, partOf=None, contact=None, location=None, active=None):
        self.original_tagname_ = None
        super(Organization, self).__init__(id, extension, modifierExtension, language, text, contained, )
        if identifier is None:
            self.identifier = []
        else:
            self.identifier = identifier
        self.name = name
        self.type_ = type_
        if telecom is None:
            self.telecom = []
        else:
            self.telecom = telecom
        if address is None:
            self.address = []
        else:
            self.address = address
        self.partOf = partOf
        if contact is None:
            self.contact = []
        else:
            self.contact = contact
        if location is None:
            self.location = []
        else:
            self.location = location
        self.active = active
    def factory(*args_, **kwargs_):
        if Organization.subclass:
            return Organization.subclass(*args_, **kwargs_)
        else:
            return Organization(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_identifier(self): return self.identifier
    def set_identifier(self, identifier): self.identifier = identifier
    def add_identifier(self, value): self.identifier.append(value)
    def insert_identifier(self, index, value): self.identifier[index] = value
    def get_name(self): return self.name
    def set_name(self, name): self.name = name
    def get_type(self): return self.type_
    def set_type(self, type_): self.type_ = type_
    def get_telecom(self): return self.telecom
    def set_telecom(self, telecom): self.telecom = telecom
    def add_telecom(self, value): self.telecom.append(value)
    def insert_telecom(self, index, value): self.telecom[index] = value
    def get_address(self): return self.address
    def set_address(self, address): self.address = address
    def add_address(self, value): self.address.append(value)
    def insert_address(self, index, value): self.address[index] = value
    def get_partOf(self): return self.partOf
    def set_partOf(self, partOf): self.partOf = partOf
    def get_contact(self): return self.contact
    def set_contact(self, contact): self.contact = contact
    def add_contact(self, value): self.contact.append(value)
    def insert_contact(self, index, value): self.contact[index] = value
    def get_location(self): return self.location
    def set_location(self, location): self.location = location
    def add_location(self, value): self.location.append(value)
    def insert_location(self, index, value): self.location[index] = value
    def get_active(self): return self.active
    def set_active(self, active): self.active = active
    def hasContent_(self):
        if (
            self.identifier or
            self.name is not None or
            self.type_ is not None or
            self.telecom or
            self.address or
            self.partOf is not None or
            self.contact or
            self.location or
            self.active is not None or
            super(Organization, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Organization', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Organization')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Organization', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Organization'):
        super(Organization, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Organization')
    def exportChildren(self, outfile, level, namespace_='', name_='Organization', fromsubclass_=False, pretty_print=True):
        super(Organization, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for identifier_ in self.identifier:
            identifier_.export(outfile, level, namespace_, name_='identifier', pretty_print=pretty_print)
        if self.name is not None:
            self.name.export(outfile, level, namespace_, name_='name', pretty_print=pretty_print)
        if self.type_ is not None:
            self.type_.export(outfile, level, namespace_, name_='type', pretty_print=pretty_print)
        for telecom_ in self.telecom:
            telecom_.export(outfile, level, namespace_, name_='telecom', pretty_print=pretty_print)
        for address_ in self.address:
            address_.export(outfile, level, namespace_, name_='address', pretty_print=pretty_print)
        if self.partOf is not None:
            self.partOf.export(outfile, level, namespace_, name_='partOf', pretty_print=pretty_print)
        for contact_ in self.contact:
            contact_.export(outfile, level, namespace_, name_='contact', pretty_print=pretty_print)
        for location_ in self.location:
            location_.export(outfile, level, namespace_, name_='location', pretty_print=pretty_print)
        if self.active is not None:
            self.active.export(outfile, level, namespace_, name_='active', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Organization', mapping_=None):
        element = super(Organization, self).to_etree(parent_element, name_, mapping_)
        for identifier_ in self.identifier:
            identifier_.to_etree(element, name_='identifier', mapping_=mapping_)
        if self.name is not None:
            name_ = self.name
            name_.to_etree(element, name_='name', mapping_=mapping_)
        if self.type_ is not None:
            type__ = self.type_
            type__.to_etree(element, name_='type', mapping_=mapping_)
        for telecom_ in self.telecom:
            telecom_.to_etree(element, name_='telecom', mapping_=mapping_)
        for address_ in self.address:
            address_.to_etree(element, name_='address', mapping_=mapping_)
        if self.partOf is not None:
            partOf_ = self.partOf
            partOf_.to_etree(element, name_='partOf', mapping_=mapping_)
        for contact_ in self.contact:
            contact_.to_etree(element, name_='contact', mapping_=mapping_)
        for location_ in self.location:
            location_.to_etree(element, name_='location', mapping_=mapping_)
        if self.active is not None:
            active_ = self.active
            active_.to_etree(element, name_='active', mapping_=mapping_)
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
        super(Organization, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'identifier':
            obj_ = Identifier.factory()
            obj_.build(child_)
            self.identifier.append(obj_)
            obj_.original_tagname_ = 'identifier'
        elif nodeName_ == 'name':
            obj_ = string.factory()
            obj_.build(child_)
            self.name = obj_
            obj_.original_tagname_ = 'name'
        elif nodeName_ == 'type':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.type_ = obj_
            obj_.original_tagname_ = 'type'
        elif nodeName_ == 'telecom':
            obj_ = Contact.factory()
            obj_.build(child_)
            self.telecom.append(obj_)
            obj_.original_tagname_ = 'telecom'
        elif nodeName_ == 'address':
            obj_ = Address.factory()
            obj_.build(child_)
            self.address.append(obj_)
            obj_.original_tagname_ = 'address'
        elif nodeName_ == 'partOf':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.partOf = obj_
            obj_.original_tagname_ = 'partOf'
        elif nodeName_ == 'contact':
            obj_ = Organization_Contact.factory()
            obj_.build(child_)
            self.contact.append(obj_)
            obj_.original_tagname_ = 'contact'
        elif nodeName_ == 'location':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.location.append(obj_)
            obj_.original_tagname_ = 'location'
        elif nodeName_ == 'active':
            obj_ = boolean.factory()
            obj_.build(child_)
            self.active = obj_
            obj_.original_tagname_ = 'active'
        super(Organization, self).buildChildren(child_, node, nodeName_, True)
# end class Organization


class Organization_Contact(BackboneElement):
    """A formally or informally recognized grouping of people or
    organizations formed for the purpose of achieving some form of
    collective action. Includes companies, institutions,
    corporations, departments, community groups, healthcare practice
    groups, etc."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, purpose=None, name=None, telecom=None, address=None, gender=None):
        self.original_tagname_ = None
        super(Organization_Contact, self).__init__(id, extension, modifierExtension, )
        self.purpose = purpose
        self.name = name
        if telecom is None:
            self.telecom = []
        else:
            self.telecom = telecom
        self.address = address
        self.gender = gender
    def factory(*args_, **kwargs_):
        if Organization_Contact.subclass:
            return Organization_Contact.subclass(*args_, **kwargs_)
        else:
            return Organization_Contact(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_purpose(self): return self.purpose
    def set_purpose(self, purpose): self.purpose = purpose
    def get_name(self): return self.name
    def set_name(self, name): self.name = name
    def get_telecom(self): return self.telecom
    def set_telecom(self, telecom): self.telecom = telecom
    def add_telecom(self, value): self.telecom.append(value)
    def insert_telecom(self, index, value): self.telecom[index] = value
    def get_address(self): return self.address
    def set_address(self, address): self.address = address
    def get_gender(self): return self.gender
    def set_gender(self, gender): self.gender = gender
    def hasContent_(self):
        if (
            self.purpose is not None or
            self.name is not None or
            self.telecom or
            self.address is not None or
            self.gender is not None or
            super(Organization_Contact, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Organization.Contact', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Organization.Contact')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Organization.Contact', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Organization.Contact'):
        super(Organization_Contact, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Organization.Contact')
    def exportChildren(self, outfile, level, namespace_='', name_='Organization.Contact', fromsubclass_=False, pretty_print=True):
        super(Organization_Contact, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.purpose is not None:
            self.purpose.export(outfile, level, namespace_, name_='purpose', pretty_print=pretty_print)
        if self.name is not None:
            self.name.export(outfile, level, namespace_, name_='name', pretty_print=pretty_print)
        for telecom_ in self.telecom:
            telecom_.export(outfile, level, namespace_, name_='telecom', pretty_print=pretty_print)
        if self.address is not None:
            self.address.export(outfile, level, namespace_, name_='address', pretty_print=pretty_print)
        if self.gender is not None:
            self.gender.export(outfile, level, namespace_, name_='gender', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Organization.Contact', mapping_=None):
        element = super(Organization_Contact, self).to_etree(parent_element, name_, mapping_)
        if self.purpose is not None:
            purpose_ = self.purpose
            purpose_.to_etree(element, name_='purpose', mapping_=mapping_)
        if self.name is not None:
            name_ = self.name
            name_.to_etree(element, name_='name', mapping_=mapping_)
        for telecom_ in self.telecom:
            telecom_.to_etree(element, name_='telecom', mapping_=mapping_)
        if self.address is not None:
            address_ = self.address
            address_.to_etree(element, name_='address', mapping_=mapping_)
        if self.gender is not None:
            gender_ = self.gender
            gender_.to_etree(element, name_='gender', mapping_=mapping_)
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
        super(Organization_Contact, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'purpose':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.purpose = obj_
            obj_.original_tagname_ = 'purpose'
        elif nodeName_ == 'name':
            obj_ = HumanName.factory()
            obj_.build(child_)
            self.name = obj_
            obj_.original_tagname_ = 'name'
        elif nodeName_ == 'telecom':
            obj_ = Contact.factory()
            obj_.build(child_)
            self.telecom.append(obj_)
            obj_.original_tagname_ = 'telecom'
        elif nodeName_ == 'address':
            obj_ = Address.factory()
            obj_.build(child_)
            self.address = obj_
            obj_.original_tagname_ = 'address'
        elif nodeName_ == 'gender':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.gender = obj_
            obj_.original_tagname_ = 'gender'
        super(Organization_Contact, self).buildChildren(child_, node, nodeName_, True)
# end class Organization_Contact
