from .base_classes import *
from .support_functions import *


class Patient(Resource):
    """Demographics and other administrative information about a person or
    animal receiving care or other health-related services.If the
    element is present, it must have either a @value, an @id, or
    extensionsIndicates if the individual is deceased or
    not.Indicates whether the patient is part of a multiple or
    indicates the actual birth order."""
    subclass = None
    superclass = Resource
    def __init__(self, id=None, extension=None, modifierExtension=None, language=None, text=None, contained=None, identifier=None, name=None, telecom=None, gender=None, birthDate=None, deceasedBoolean=None, deceasedDateTime=None, address=None, maritalStatus=None, multipleBirthBoolean=None, multipleBirthInteger=None, photo=None, contact=None, animal=None, communication=None, careProvider=None, managingOrganization=None, link=None, active=None):
        self.original_tagname_ = None
        super(Patient, self).__init__(id, extension, modifierExtension, language, text, contained, )
        if identifier is None:
            self.identifier = []
        else:
            self.identifier = identifier
        if name is None:
            self.name = []
        else:
            self.name = name
        if telecom is None:
            self.telecom = []
        else:
            self.telecom = telecom
        self.gender = gender
        self.birthDate = birthDate
        self.deceasedBoolean = deceasedBoolean
        self.deceasedDateTime = deceasedDateTime
        if address is None:
            self.address = []
        else:
            self.address = address
        self.maritalStatus = maritalStatus
        self.multipleBirthBoolean = multipleBirthBoolean
        self.multipleBirthInteger = multipleBirthInteger
        if photo is None:
            self.photo = []
        else:
            self.photo = photo
        if contact is None:
            self.contact = []
        else:
            self.contact = contact
        self.animal = animal
        if communication is None:
            self.communication = []
        else:
            self.communication = communication
        if careProvider is None:
            self.careProvider = []
        else:
            self.careProvider = careProvider
        self.managingOrganization = managingOrganization
        if link is None:
            self.link = []
        else:
            self.link = link
        self.active = active
    def factory(*args_, **kwargs_):
        if Patient.subclass:
            return Patient.subclass(*args_, **kwargs_)
        else:
            return Patient(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_identifier(self): return self.identifier
    def set_identifier(self, identifier): self.identifier = identifier
    def add_identifier(self, value): self.identifier.append(value)
    def insert_identifier(self, index, value): self.identifier[index] = value
    def get_name(self): return self.name
    def set_name(self, name): self.name = name
    def add_name(self, value): self.name.append(value)
    def insert_name(self, index, value): self.name[index] = value
    def get_telecom(self): return self.telecom
    def set_telecom(self, telecom): self.telecom = telecom
    def add_telecom(self, value): self.telecom.append(value)
    def insert_telecom(self, index, value): self.telecom[index] = value
    def get_gender(self): return self.gender
    def set_gender(self, gender): self.gender = gender
    def get_birthDate(self): return self.birthDate
    def set_birthDate(self, birthDate): self.birthDate = birthDate
    def get_deceasedBoolean(self): return self.deceasedBoolean
    def set_deceasedBoolean(self, deceasedBoolean): self.deceasedBoolean = deceasedBoolean
    def get_deceasedDateTime(self): return self.deceasedDateTime
    def set_deceasedDateTime(self, deceasedDateTime): self.deceasedDateTime = deceasedDateTime
    def get_address(self): return self.address
    def set_address(self, address): self.address = address
    def add_address(self, value): self.address.append(value)
    def insert_address(self, index, value): self.address[index] = value
    def get_maritalStatus(self): return self.maritalStatus
    def set_maritalStatus(self, maritalStatus): self.maritalStatus = maritalStatus
    def get_multipleBirthBoolean(self): return self.multipleBirthBoolean
    def set_multipleBirthBoolean(self, multipleBirthBoolean): self.multipleBirthBoolean = multipleBirthBoolean
    def get_multipleBirthInteger(self): return self.multipleBirthInteger
    def set_multipleBirthInteger(self, multipleBirthInteger): self.multipleBirthInteger = multipleBirthInteger
    def get_photo(self): return self.photo
    def set_photo(self, photo): self.photo = photo
    def add_photo(self, value): self.photo.append(value)
    def insert_photo(self, index, value): self.photo[index] = value
    def get_contact(self): return self.contact
    def set_contact(self, contact): self.contact = contact
    def add_contact(self, value): self.contact.append(value)
    def insert_contact(self, index, value): self.contact[index] = value
    def get_animal(self): return self.animal
    def set_animal(self, animal): self.animal = animal
    def get_communication(self): return self.communication
    def set_communication(self, communication): self.communication = communication
    def add_communication(self, value): self.communication.append(value)
    def insert_communication(self, index, value): self.communication[index] = value
    def get_careProvider(self): return self.careProvider
    def set_careProvider(self, careProvider): self.careProvider = careProvider
    def add_careProvider(self, value): self.careProvider.append(value)
    def insert_careProvider(self, index, value): self.careProvider[index] = value
    def get_managingOrganization(self): return self.managingOrganization
    def set_managingOrganization(self, managingOrganization): self.managingOrganization = managingOrganization
    def get_link(self): return self.link
    def set_link(self, link): self.link = link
    def add_link(self, value): self.link.append(value)
    def insert_link(self, index, value): self.link[index] = value
    def get_active(self): return self.active
    def set_active(self, active): self.active = active
    def hasContent_(self):
        if (
            self.identifier or
            self.name or
            self.telecom or
            self.gender is not None or
            self.birthDate is not None or
            self.deceasedBoolean is not None or
            self.deceasedDateTime is not None or
            self.address or
            self.maritalStatus is not None or
            self.multipleBirthBoolean is not None or
            self.multipleBirthInteger is not None or
            self.photo or
            self.contact or
            self.animal is not None or
            self.communication or
            self.careProvider or
            self.managingOrganization is not None or
            self.link or
            self.active is not None or
            super(Patient, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Patient', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Patient')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Patient', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Patient'):
        super(Patient, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Patient')
    def exportChildren(self, outfile, level, namespace_='', name_='Patient', fromsubclass_=False, pretty_print=True):
        super(Patient, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for identifier_ in self.identifier:
            identifier_.export(outfile, level, namespace_, name_='identifier', pretty_print=pretty_print)
        for name_ in self.name:
            name_.export(outfile, level, namespace_, name_='name', pretty_print=pretty_print)
        for telecom_ in self.telecom:
            telecom_.export(outfile, level, namespace_, name_='telecom', pretty_print=pretty_print)
        if self.gender is not None:
            self.gender.export(outfile, level, namespace_, name_='gender', pretty_print=pretty_print)
        if self.birthDate is not None:
            self.birthDate.export(outfile, level, namespace_, name_='birthDate', pretty_print=pretty_print)
        if self.deceasedBoolean is not None:
            self.deceasedBoolean.export(outfile, level, namespace_, name_='deceasedBoolean', pretty_print=pretty_print)
        if self.deceasedDateTime is not None:
            self.deceasedDateTime.export(outfile, level, namespace_, name_='deceasedDateTime', pretty_print=pretty_print)
        for address_ in self.address:
            address_.export(outfile, level, namespace_, name_='address', pretty_print=pretty_print)
        if self.maritalStatus is not None:
            self.maritalStatus.export(outfile, level, namespace_, name_='maritalStatus', pretty_print=pretty_print)
        if self.multipleBirthBoolean is not None:
            self.multipleBirthBoolean.export(outfile, level, namespace_, name_='multipleBirthBoolean', pretty_print=pretty_print)
        if self.multipleBirthInteger is not None:
            self.multipleBirthInteger.export(outfile, level, namespace_, name_='multipleBirthInteger', pretty_print=pretty_print)
        for photo_ in self.photo:
            photo_.export(outfile, level, namespace_, name_='photo', pretty_print=pretty_print)
        for contact_ in self.contact:
            contact_.export(outfile, level, namespace_, name_='contact', pretty_print=pretty_print)
        if self.animal is not None:
            self.animal.export(outfile, level, namespace_, name_='animal', pretty_print=pretty_print)
        for communication_ in self.communication:
            communication_.export(outfile, level, namespace_, name_='communication', pretty_print=pretty_print)
        for careProvider_ in self.careProvider:
            careProvider_.export(outfile, level, namespace_, name_='careProvider', pretty_print=pretty_print)
        if self.managingOrganization is not None:
            self.managingOrganization.export(outfile, level, namespace_, name_='managingOrganization', pretty_print=pretty_print)
        for link_ in self.link:
            link_.export(outfile, level, namespace_, name_='link', pretty_print=pretty_print)
        if self.active is not None:
            self.active.export(outfile, level, namespace_, name_='active', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Patient', mapping_=None):
        element = super(Patient, self).to_etree(parent_element, name_, mapping_)
        for identifier_ in self.identifier:
            identifier_.to_etree(element, name_='identifier', mapping_=mapping_)
        for name_ in self.name:
            name_.to_etree(element, name_='name', mapping_=mapping_)
        for telecom_ in self.telecom:
            telecom_.to_etree(element, name_='telecom', mapping_=mapping_)
        if self.gender is not None:
            gender_ = self.gender
            gender_.to_etree(element, name_='gender', mapping_=mapping_)
        if self.birthDate is not None:
            birthDate_ = self.birthDate
            birthDate_.to_etree(element, name_='birthDate', mapping_=mapping_)
        if self.deceasedBoolean is not None:
            deceasedBoolean_ = self.deceasedBoolean
            deceasedBoolean_.to_etree(element, name_='deceasedBoolean', mapping_=mapping_)
        if self.deceasedDateTime is not None:
            deceasedDateTime_ = self.deceasedDateTime
            deceasedDateTime_.to_etree(element, name_='deceasedDateTime', mapping_=mapping_)
        for address_ in self.address:
            address_.to_etree(element, name_='address', mapping_=mapping_)
        if self.maritalStatus is not None:
            maritalStatus_ = self.maritalStatus
            maritalStatus_.to_etree(element, name_='maritalStatus', mapping_=mapping_)
        if self.multipleBirthBoolean is not None:
            multipleBirthBoolean_ = self.multipleBirthBoolean
            multipleBirthBoolean_.to_etree(element, name_='multipleBirthBoolean', mapping_=mapping_)
        if self.multipleBirthInteger is not None:
            multipleBirthInteger_ = self.multipleBirthInteger
            multipleBirthInteger_.to_etree(element, name_='multipleBirthInteger', mapping_=mapping_)
        for photo_ in self.photo:
            photo_.to_etree(element, name_='photo', mapping_=mapping_)
        for contact_ in self.contact:
            contact_.to_etree(element, name_='contact', mapping_=mapping_)
        if self.animal is not None:
            animal_ = self.animal
            animal_.to_etree(element, name_='animal', mapping_=mapping_)
        for communication_ in self.communication:
            communication_.to_etree(element, name_='communication', mapping_=mapping_)
        for careProvider_ in self.careProvider:
            careProvider_.to_etree(element, name_='careProvider', mapping_=mapping_)
        if self.managingOrganization is not None:
            managingOrganization_ = self.managingOrganization
            managingOrganization_.to_etree(element, name_='managingOrganization', mapping_=mapping_)
        for link_ in self.link:
            link_.to_etree(element, name_='link', mapping_=mapping_)
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
        super(Patient, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'identifier':
            obj_ = Identifier.factory()
            obj_.build(child_)
            self.identifier.append(obj_)
            obj_.original_tagname_ = 'identifier'
        elif nodeName_ == 'name':
            obj_ = HumanName.factory()
            obj_.build(child_)
            self.name.append(obj_)
            obj_.original_tagname_ = 'name'
        elif nodeName_ == 'telecom':
            obj_ = Contact.factory()
            obj_.build(child_)
            self.telecom.append(obj_)
            obj_.original_tagname_ = 'telecom'
        elif nodeName_ == 'gender':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.gender = obj_
            obj_.original_tagname_ = 'gender'
        elif nodeName_ == 'birthDate':
            obj_ = dateTime.factory()
            obj_.build(child_)
            self.birthDate = obj_
            obj_.original_tagname_ = 'birthDate'
        elif nodeName_ == 'deceasedBoolean':
            obj_ = boolean.factory()
            obj_.build(child_)
            self.deceasedBoolean = obj_
            obj_.original_tagname_ = 'deceasedBoolean'
        elif nodeName_ == 'deceasedDateTime':
            obj_ = dateTime.factory()
            obj_.build(child_)
            self.deceasedDateTime = obj_
            obj_.original_tagname_ = 'deceasedDateTime'
        elif nodeName_ == 'address':
            obj_ = Address.factory()
            obj_.build(child_)
            self.address.append(obj_)
            obj_.original_tagname_ = 'address'
        elif nodeName_ == 'maritalStatus':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.maritalStatus = obj_
            obj_.original_tagname_ = 'maritalStatus'
        elif nodeName_ == 'multipleBirthBoolean':
            obj_ = boolean.factory()
            obj_.build(child_)
            self.multipleBirthBoolean = obj_
            obj_.original_tagname_ = 'multipleBirthBoolean'
        elif nodeName_ == 'multipleBirthInteger':
            obj_ = integer.factory()
            obj_.build(child_)
            self.multipleBirthInteger = obj_
            obj_.original_tagname_ = 'multipleBirthInteger'
        elif nodeName_ == 'photo':
            obj_ = Attachment.factory()
            obj_.build(child_)
            self.photo.append(obj_)
            obj_.original_tagname_ = 'photo'
        elif nodeName_ == 'contact':
            obj_ = Patient_Contact.factory()
            obj_.build(child_)
            self.contact.append(obj_)
            obj_.original_tagname_ = 'contact'
        elif nodeName_ == 'animal':
            obj_ = Patient_Animal.factory()
            obj_.build(child_)
            self.animal = obj_
            obj_.original_tagname_ = 'animal'
        elif nodeName_ == 'communication':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.communication.append(obj_)
            obj_.original_tagname_ = 'communication'
        elif nodeName_ == 'careProvider':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.careProvider.append(obj_)
            obj_.original_tagname_ = 'careProvider'
        elif nodeName_ == 'managingOrganization':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.managingOrganization = obj_
            obj_.original_tagname_ = 'managingOrganization'
        elif nodeName_ == 'link':
            obj_ = Patient_Link.factory()
            obj_.build(child_)
            self.link.append(obj_)
            obj_.original_tagname_ = 'link'
        elif nodeName_ == 'active':
            obj_ = boolean.factory()
            obj_.build(child_)
            self.active = obj_
            obj_.original_tagname_ = 'active'
        super(Patient, self).buildChildren(child_, node, nodeName_, True)
# end class Patient


class Patient_Contact(BackboneElement):
    """Demographics and other administrative information about a person or
    animal receiving care or other health-related services."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, relationship=None, name=None, telecom=None, address=None, gender=None, organization=None):
        self.original_tagname_ = None
        super(Patient_Contact, self).__init__(id, extension, modifierExtension, )
        if relationship is None:
            self.relationship = []
        else:
            self.relationship = relationship
        self.name = name
        if telecom is None:
            self.telecom = []
        else:
            self.telecom = telecom
        self.address = address
        self.gender = gender
        self.organization = organization
    def factory(*args_, **kwargs_):
        if Patient_Contact.subclass:
            return Patient_Contact.subclass(*args_, **kwargs_)
        else:
            return Patient_Contact(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_relationship(self): return self.relationship
    def set_relationship(self, relationship): self.relationship = relationship
    def add_relationship(self, value): self.relationship.append(value)
    def insert_relationship(self, index, value): self.relationship[index] = value
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
    def get_organization(self): return self.organization
    def set_organization(self, organization): self.organization = organization
    def hasContent_(self):
        if (
            self.relationship or
            self.name is not None or
            self.telecom or
            self.address is not None or
            self.gender is not None or
            self.organization is not None or
            super(Patient_Contact, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Patient.Contact', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Patient.Contact')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Patient.Contact', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Patient.Contact'):
        super(Patient_Contact, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Patient.Contact')
    def exportChildren(self, outfile, level, namespace_='', name_='Patient.Contact', fromsubclass_=False, pretty_print=True):
        super(Patient_Contact, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for relationship_ in self.relationship:
            relationship_.export(outfile, level, namespace_, name_='relationship', pretty_print=pretty_print)
        if self.name is not None:
            self.name.export(outfile, level, namespace_, name_='name', pretty_print=pretty_print)
        for telecom_ in self.telecom:
            telecom_.export(outfile, level, namespace_, name_='telecom', pretty_print=pretty_print)
        if self.address is not None:
            self.address.export(outfile, level, namespace_, name_='address', pretty_print=pretty_print)
        if self.gender is not None:
            self.gender.export(outfile, level, namespace_, name_='gender', pretty_print=pretty_print)
        if self.organization is not None:
            self.organization.export(outfile, level, namespace_, name_='organization', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Patient.Contact', mapping_=None):
        element = super(Patient_Contact, self).to_etree(parent_element, name_, mapping_)
        for relationship_ in self.relationship:
            relationship_.to_etree(element, name_='relationship', mapping_=mapping_)
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
        if self.organization is not None:
            organization_ = self.organization
            organization_.to_etree(element, name_='organization', mapping_=mapping_)
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
        super(Patient_Contact, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'relationship':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.relationship.append(obj_)
            obj_.original_tagname_ = 'relationship'
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
        elif nodeName_ == 'organization':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.organization = obj_
            obj_.original_tagname_ = 'organization'
        super(Patient_Contact, self).buildChildren(child_, node, nodeName_, True)
# end class Patient_Contact


class Patient_Animal(BackboneElement):
    """Demographics and other administrative information about a person or
    animal receiving care or other health-related services."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, species=None, breed=None, genderStatus=None):
        self.original_tagname_ = None
        super(Patient_Animal, self).__init__(id, extension, modifierExtension, )
        self.species = species
        self.breed = breed
        self.genderStatus = genderStatus
    def factory(*args_, **kwargs_):
        if Patient_Animal.subclass:
            return Patient_Animal.subclass(*args_, **kwargs_)
        else:
            return Patient_Animal(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_species(self): return self.species
    def set_species(self, species): self.species = species
    def get_breed(self): return self.breed
    def set_breed(self, breed): self.breed = breed
    def get_genderStatus(self): return self.genderStatus
    def set_genderStatus(self, genderStatus): self.genderStatus = genderStatus
    def hasContent_(self):
        if (
            self.species is not None or
            self.breed is not None or
            self.genderStatus is not None or
            super(Patient_Animal, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Patient.Animal', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Patient.Animal')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Patient.Animal', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Patient.Animal'):
        super(Patient_Animal, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Patient.Animal')
    def exportChildren(self, outfile, level, namespace_='', name_='Patient.Animal', fromsubclass_=False, pretty_print=True):
        super(Patient_Animal, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.species is not None:
            self.species.export(outfile, level, namespace_, name_='species', pretty_print=pretty_print)
        if self.breed is not None:
            self.breed.export(outfile, level, namespace_, name_='breed', pretty_print=pretty_print)
        if self.genderStatus is not None:
            self.genderStatus.export(outfile, level, namespace_, name_='genderStatus', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Patient.Animal', mapping_=None):
        element = super(Patient_Animal, self).to_etree(parent_element, name_, mapping_)
        if self.species is not None:
            species_ = self.species
            species_.to_etree(element, name_='species', mapping_=mapping_)
        if self.breed is not None:
            breed_ = self.breed
            breed_.to_etree(element, name_='breed', mapping_=mapping_)
        if self.genderStatus is not None:
            genderStatus_ = self.genderStatus
            genderStatus_.to_etree(element, name_='genderStatus', mapping_=mapping_)
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
        super(Patient_Animal, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'species':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.species = obj_
            obj_.original_tagname_ = 'species'
        elif nodeName_ == 'breed':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.breed = obj_
            obj_.original_tagname_ = 'breed'
        elif nodeName_ == 'genderStatus':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.genderStatus = obj_
            obj_.original_tagname_ = 'genderStatus'
        super(Patient_Animal, self).buildChildren(child_, node, nodeName_, True)
# end class Patient_Animal


class Patient_Link(BackboneElement):
    """Demographics and other administrative information about a person or
    animal receiving care or other health-related services."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, other=None, type_=None):
        self.original_tagname_ = None
        super(Patient_Link, self).__init__(id, extension, modifierExtension, )
        self.other = other
        self.type_ = type_
    def factory(*args_, **kwargs_):
        if Patient_Link.subclass:
            return Patient_Link.subclass(*args_, **kwargs_)
        else:
            return Patient_Link(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_other(self): return self.other
    def set_other(self, other): self.other = other
    def get_type(self): return self.type_
    def set_type(self, type_): self.type_ = type_
    def hasContent_(self):
        if (
            self.other is not None or
            self.type_ is not None or
            super(Patient_Link, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Patient.Link', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Patient.Link')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Patient.Link', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Patient.Link'):
        super(Patient_Link, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Patient.Link')
    def exportChildren(self, outfile, level, namespace_='', name_='Patient.Link', fromsubclass_=False, pretty_print=True):
        super(Patient_Link, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.other is not None:
            self.other.export(outfile, level, namespace_, name_='other', pretty_print=pretty_print)
        if self.type_ is not None:
            self.type_.export(outfile, level, namespace_, name_='type', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Patient.Link', mapping_=None):
        element = super(Patient_Link, self).to_etree(parent_element, name_, mapping_)
        if self.other is not None:
            other_ = self.other
            other_.to_etree(element, name_='other', mapping_=mapping_)
        if self.type_ is not None:
            type__ = self.type_
            type__.to_etree(element, name_='type', mapping_=mapping_)
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
        super(Patient_Link, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'other':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.other = obj_
            obj_.original_tagname_ = 'other'
        elif nodeName_ == 'type':
            obj_ = LinkType.factory()
            obj_.build(child_)
            self.type_ = obj_
            obj_.original_tagname_ = 'type'
        super(Patient_Link, self).buildChildren(child_, node, nodeName_, True)
# end class Patient_Link


class LinkType(Element):
    """The type of link between this patient resource and another patient
    resource.If the element is present, it must have either a
    @value, an @id, or extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(LinkType, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if LinkType.subclass:
            return LinkType.subclass(*args_, **kwargs_)
        else:
            return LinkType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(LinkType, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='LinkType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='LinkType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='LinkType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='LinkType'):
        super(LinkType, self).exportAttributes(outfile, level, already_processed, namespace_, name_='LinkType')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='LinkType', fromsubclass_=False, pretty_print=True):
        super(LinkType, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='LinkType', mapping_=None):
        element = super(LinkType, self).to_etree(parent_element, name_, mapping_)
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
        super(LinkType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(LinkType, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class LinkType
