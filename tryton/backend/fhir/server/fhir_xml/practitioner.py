from .base_classes import *
from .support_functions import *


class Practitioner(Resource):
    """A person who is directly or indirectly involved in the provisioning
    of healthcare.If the element is present, it must have either a
    @value, an @id, or extensions"""
    subclass = None
    superclass = Resource
    def __init__(self, id=None, extension=None, modifierExtension=None, language=None, text=None, contained=None, identifier=None, name=None, telecom=None, address=None, gender=None, birthDate=None, photo=None, organization=None, role=None, specialty=None, period=None, location=None, qualification=None, communication=None):
        self.original_tagname_ = None
        super(Practitioner, self).__init__(id, extension, modifierExtension, language, text, contained, )
        if identifier is None:
            self.identifier = []
        else:
            self.identifier = identifier
        self.name = name
        if telecom is None:
            self.telecom = []
        else:
            self.telecom = telecom
        self.address = address
        self.gender = gender
        self.birthDate = birthDate
        if photo is None:
            self.photo = []
        else:
            self.photo = photo
        self.organization = organization
        if role is None:
            self.role = []
        else:
            self.role = role
        if specialty is None:
            self.specialty = []
        else:
            self.specialty = specialty
        self.period = period
        if location is None:
            self.location = []
        else:
            self.location = location
        if qualification is None:
            self.qualification = []
        else:
            self.qualification = qualification
        if communication is None:
            self.communication = []
        else:
            self.communication = communication
    def factory(*args_, **kwargs_):
        if Practitioner.subclass:
            return Practitioner.subclass(*args_, **kwargs_)
        else:
            return Practitioner(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_identifier(self): return self.identifier
    def set_identifier(self, identifier): self.identifier = identifier
    def add_identifier(self, value): self.identifier.append(value)
    def insert_identifier(self, index, value): self.identifier[index] = value
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
    def get_birthDate(self): return self.birthDate
    def set_birthDate(self, birthDate): self.birthDate = birthDate
    def get_photo(self): return self.photo
    def set_photo(self, photo): self.photo = photo
    def add_photo(self, value): self.photo.append(value)
    def insert_photo(self, index, value): self.photo[index] = value
    def get_organization(self): return self.organization
    def set_organization(self, organization): self.organization = organization
    def get_role(self): return self.role
    def set_role(self, role): self.role = role
    def add_role(self, value): self.role.append(value)
    def insert_role(self, index, value): self.role[index] = value
    def get_specialty(self): return self.specialty
    def set_specialty(self, specialty): self.specialty = specialty
    def add_specialty(self, value): self.specialty.append(value)
    def insert_specialty(self, index, value): self.specialty[index] = value
    def get_period(self): return self.period
    def set_period(self, period): self.period = period
    def get_location(self): return self.location
    def set_location(self, location): self.location = location
    def add_location(self, value): self.location.append(value)
    def insert_location(self, index, value): self.location[index] = value
    def get_qualification(self): return self.qualification
    def set_qualification(self, qualification): self.qualification = qualification
    def add_qualification(self, value): self.qualification.append(value)
    def insert_qualification(self, index, value): self.qualification[index] = value
    def get_communication(self): return self.communication
    def set_communication(self, communication): self.communication = communication
    def add_communication(self, value): self.communication.append(value)
    def insert_communication(self, index, value): self.communication[index] = value
    def hasContent_(self):
        if (
            self.identifier or
            self.name is not None or
            self.telecom or
            self.address is not None or
            self.gender is not None or
            self.birthDate is not None or
            self.photo or
            self.organization is not None or
            self.role or
            self.specialty or
            self.period is not None or
            self.location or
            self.qualification or
            self.communication or
            super(Practitioner, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Practitioner', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Practitioner')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Practitioner', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Practitioner'):
        super(Practitioner, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Practitioner')
    def exportChildren(self, outfile, level, namespace_='', name_='Practitioner', fromsubclass_=False, pretty_print=True):
        super(Practitioner, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for identifier_ in self.identifier:
            identifier_.export(outfile, level, namespace_, name_='identifier', pretty_print=pretty_print)
        if self.name is not None:
            self.name.export(outfile, level, namespace_, name_='name', pretty_print=pretty_print)
        for telecom_ in self.telecom:
            telecom_.export(outfile, level, namespace_, name_='telecom', pretty_print=pretty_print)
        if self.address is not None:
            self.address.export(outfile, level, namespace_, name_='address', pretty_print=pretty_print)
        if self.gender is not None:
            self.gender.export(outfile, level, namespace_, name_='gender', pretty_print=pretty_print)
        if self.birthDate is not None:
            self.birthDate.export(outfile, level, namespace_, name_='birthDate', pretty_print=pretty_print)
        for photo_ in self.photo:
            photo_.export(outfile, level, namespace_, name_='photo', pretty_print=pretty_print)
        if self.organization is not None:
            self.organization.export(outfile, level, namespace_, name_='organization', pretty_print=pretty_print)
        for role_ in self.role:
            role_.export(outfile, level, namespace_, name_='role', pretty_print=pretty_print)
        for specialty_ in self.specialty:
            specialty_.export(outfile, level, namespace_, name_='specialty', pretty_print=pretty_print)
        if self.period is not None:
            self.period.export(outfile, level, namespace_, name_='period', pretty_print=pretty_print)
        for location_ in self.location:
            location_.export(outfile, level, namespace_, name_='location', pretty_print=pretty_print)
        for qualification_ in self.qualification:
            qualification_.export(outfile, level, namespace_, name_='qualification', pretty_print=pretty_print)
        for communication_ in self.communication:
            communication_.export(outfile, level, namespace_, name_='communication', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Practitioner', mapping_=None):
        element = super(Practitioner, self).to_etree(parent_element, name_, mapping_)
        for identifier_ in self.identifier:
            identifier_.to_etree(element, name_='identifier', mapping_=mapping_)
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
        if self.birthDate is not None:
            birthDate_ = self.birthDate
            birthDate_.to_etree(element, name_='birthDate', mapping_=mapping_)
        for photo_ in self.photo:
            photo_.to_etree(element, name_='photo', mapping_=mapping_)
        if self.organization is not None:
            organization_ = self.organization
            organization_.to_etree(element, name_='organization', mapping_=mapping_)
        for role_ in self.role:
            role_.to_etree(element, name_='role', mapping_=mapping_)
        for specialty_ in self.specialty:
            specialty_.to_etree(element, name_='specialty', mapping_=mapping_)
        if self.period is not None:
            period_ = self.period
            period_.to_etree(element, name_='period', mapping_=mapping_)
        for location_ in self.location:
            location_.to_etree(element, name_='location', mapping_=mapping_)
        for qualification_ in self.qualification:
            qualification_.to_etree(element, name_='qualification', mapping_=mapping_)
        for communication_ in self.communication:
            communication_.to_etree(element, name_='communication', mapping_=mapping_)
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
        super(Practitioner, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'identifier':
            obj_ = Identifier.factory()
            obj_.build(child_)
            self.identifier.append(obj_)
            obj_.original_tagname_ = 'identifier'
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
        elif nodeName_ == 'birthDate':
            obj_ = dateTime.factory()
            obj_.build(child_)
            self.birthDate = obj_
            obj_.original_tagname_ = 'birthDate'
        elif nodeName_ == 'photo':
            obj_ = Attachment.factory()
            obj_.build(child_)
            self.photo.append(obj_)
            obj_.original_tagname_ = 'photo'
        elif nodeName_ == 'organization':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.organization = obj_
            obj_.original_tagname_ = 'organization'
        elif nodeName_ == 'role':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.role.append(obj_)
            obj_.original_tagname_ = 'role'
        elif nodeName_ == 'specialty':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.specialty.append(obj_)
            obj_.original_tagname_ = 'specialty'
        elif nodeName_ == 'period':
            obj_ = Period.factory()
            obj_.build(child_)
            self.period = obj_
            obj_.original_tagname_ = 'period'
        elif nodeName_ == 'location':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.location.append(obj_)
            obj_.original_tagname_ = 'location'
        elif nodeName_ == 'qualification':
            obj_ = Practitioner_Qualification.factory()
            obj_.build(child_)
            self.qualification.append(obj_)
            obj_.original_tagname_ = 'qualification'
        elif nodeName_ == 'communication':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.communication.append(obj_)
            obj_.original_tagname_ = 'communication'
        super(Practitioner, self).buildChildren(child_, node, nodeName_, True)
# end class Practitioner


class Practitioner_Qualification(BackboneElement):
    """A person who is directly or indirectly involved in the provisioning
    of healthcare."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, code=None, period=None, issuer=None):
        self.original_tagname_ = None
        super(Practitioner_Qualification, self).__init__(id, extension, modifierExtension, )
        self.code = code
        self.period = period
        self.issuer = issuer
    def factory(*args_, **kwargs_):
        if Practitioner_Qualification.subclass:
            return Practitioner_Qualification.subclass(*args_, **kwargs_)
        else:
            return Practitioner_Qualification(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_code(self): return self.code
    def set_code(self, code): self.code = code
    def get_period(self): return self.period
    def set_period(self, period): self.period = period
    def get_issuer(self): return self.issuer
    def set_issuer(self, issuer): self.issuer = issuer
    def hasContent_(self):
        if (
            self.code is not None or
            self.period is not None or
            self.issuer is not None or
            super(Practitioner_Qualification, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Practitioner.Qualification', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Practitioner.Qualification')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Practitioner.Qualification', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Practitioner.Qualification'):
        super(Practitioner_Qualification, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Practitioner.Qualification')
    def exportChildren(self, outfile, level, namespace_='', name_='Practitioner.Qualification', fromsubclass_=False, pretty_print=True):
        super(Practitioner_Qualification, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.code is not None:
            self.code.export(outfile, level, namespace_, name_='code', pretty_print=pretty_print)
        if self.period is not None:
            self.period.export(outfile, level, namespace_, name_='period', pretty_print=pretty_print)
        if self.issuer is not None:
            self.issuer.export(outfile, level, namespace_, name_='issuer', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Practitioner.Qualification', mapping_=None):
        element = super(Practitioner_Qualification, self).to_etree(parent_element, name_, mapping_)
        if self.code is not None:
            code_ = self.code
            code_.to_etree(element, name_='code', mapping_=mapping_)
        if self.period is not None:
            period_ = self.period
            period_.to_etree(element, name_='period', mapping_=mapping_)
        if self.issuer is not None:
            issuer_ = self.issuer
            issuer_.to_etree(element, name_='issuer', mapping_=mapping_)
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
        super(Practitioner_Qualification, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'code':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.code = obj_
            obj_.original_tagname_ = 'code'
        elif nodeName_ == 'period':
            obj_ = Period.factory()
            obj_.build(child_)
            self.period = obj_
            obj_.original_tagname_ = 'period'
        elif nodeName_ == 'issuer':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.issuer = obj_
            obj_.original_tagname_ = 'issuer'
        super(Practitioner_Qualification, self).buildChildren(child_, node, nodeName_, True)
# end class Practitioner_Qualification
