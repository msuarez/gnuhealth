from .base_classes import *
from .support_functions import *


class RelatedPerson(Resource):
    """Information about a person that is involved in the care for a
    patient, but who is not the target of healthcare, nor has a
    formal responsibility in the care process.If the element is
    present, it must have either a @value, an @id, or extensions"""
    subclass = None
    superclass = Resource
    def __init__(self, id=None, extension=None, modifierExtension=None, language=None, text=None, contained=None, identifier=None, patient=None, relationship=None, name=None, telecom=None, gender=None, address=None, photo=None):
        self.original_tagname_ = None
        super(RelatedPerson, self).__init__(id, extension, modifierExtension, language, text, contained, )
        if identifier is None:
            self.identifier = []
        else:
            self.identifier = identifier
        self.patient = patient
        self.relationship = relationship
        self.name = name
        if telecom is None:
            self.telecom = []
        else:
            self.telecom = telecom
        self.gender = gender
        self.address = address
        if photo is None:
            self.photo = []
        else:
            self.photo = photo
    def factory(*args_, **kwargs_):
        if RelatedPerson.subclass:
            return RelatedPerson.subclass(*args_, **kwargs_)
        else:
            return RelatedPerson(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_identifier(self): return self.identifier
    def set_identifier(self, identifier): self.identifier = identifier
    def add_identifier(self, value): self.identifier.append(value)
    def insert_identifier(self, index, value): self.identifier[index] = value
    def get_patient(self): return self.patient
    def set_patient(self, patient): self.patient = patient
    def get_relationship(self): return self.relationship
    def set_relationship(self, relationship): self.relationship = relationship
    def get_name(self): return self.name
    def set_name(self, name): self.name = name
    def get_telecom(self): return self.telecom
    def set_telecom(self, telecom): self.telecom = telecom
    def add_telecom(self, value): self.telecom.append(value)
    def insert_telecom(self, index, value): self.telecom[index] = value
    def get_gender(self): return self.gender
    def set_gender(self, gender): self.gender = gender
    def get_address(self): return self.address
    def set_address(self, address): self.address = address
    def get_photo(self): return self.photo
    def set_photo(self, photo): self.photo = photo
    def add_photo(self, value): self.photo.append(value)
    def insert_photo(self, index, value): self.photo[index] = value
    def hasContent_(self):
        if (
            self.identifier or
            self.patient is not None or
            self.relationship is not None or
            self.name is not None or
            self.telecom or
            self.gender is not None or
            self.address is not None or
            self.photo or
            super(RelatedPerson, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='RelatedPerson', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='RelatedPerson')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='RelatedPerson', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='RelatedPerson'):
        super(RelatedPerson, self).exportAttributes(outfile, level, already_processed, namespace_, name_='RelatedPerson')
    def exportChildren(self, outfile, level, namespace_='', name_='RelatedPerson', fromsubclass_=False, pretty_print=True):
        super(RelatedPerson, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for identifier_ in self.identifier:
            identifier_.export(outfile, level, namespace_, name_='identifier', pretty_print=pretty_print)
        if self.patient is not None:
            self.patient.export(outfile, level, namespace_, name_='patient', pretty_print=pretty_print)
        if self.relationship is not None:
            self.relationship.export(outfile, level, namespace_, name_='relationship', pretty_print=pretty_print)
        if self.name is not None:
            self.name.export(outfile, level, namespace_, name_='name', pretty_print=pretty_print)
        for telecom_ in self.telecom:
            telecom_.export(outfile, level, namespace_, name_='telecom', pretty_print=pretty_print)
        if self.gender is not None:
            self.gender.export(outfile, level, namespace_, name_='gender', pretty_print=pretty_print)
        if self.address is not None:
            self.address.export(outfile, level, namespace_, name_='address', pretty_print=pretty_print)
        for photo_ in self.photo:
            photo_.export(outfile, level, namespace_, name_='photo', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='RelatedPerson', mapping_=None):
        element = super(RelatedPerson, self).to_etree(parent_element, name_, mapping_)
        for identifier_ in self.identifier:
            identifier_.to_etree(element, name_='identifier', mapping_=mapping_)
        if self.patient is not None:
            patient_ = self.patient
            patient_.to_etree(element, name_='patient', mapping_=mapping_)
        if self.relationship is not None:
            relationship_ = self.relationship
            relationship_.to_etree(element, name_='relationship', mapping_=mapping_)
        if self.name is not None:
            name_ = self.name
            name_.to_etree(element, name_='name', mapping_=mapping_)
        for telecom_ in self.telecom:
            telecom_.to_etree(element, name_='telecom', mapping_=mapping_)
        if self.gender is not None:
            gender_ = self.gender
            gender_.to_etree(element, name_='gender', mapping_=mapping_)
        if self.address is not None:
            address_ = self.address
            address_.to_etree(element, name_='address', mapping_=mapping_)
        for photo_ in self.photo:
            photo_.to_etree(element, name_='photo', mapping_=mapping_)
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
        super(RelatedPerson, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'identifier':
            obj_ = Identifier.factory()
            obj_.build(child_)
            self.identifier.append(obj_)
            obj_.original_tagname_ = 'identifier'
        elif nodeName_ == 'patient':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.patient = obj_
            obj_.original_tagname_ = 'patient'
        elif nodeName_ == 'relationship':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.relationship = obj_
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
        elif nodeName_ == 'gender':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.gender = obj_
            obj_.original_tagname_ = 'gender'
        elif nodeName_ == 'address':
            obj_ = Address.factory()
            obj_.build(child_)
            self.address = obj_
            obj_.original_tagname_ = 'address'
        elif nodeName_ == 'photo':
            obj_ = Attachment.factory()
            obj_.build(child_)
            self.photo.append(obj_)
            obj_.original_tagname_ = 'photo'
        super(RelatedPerson, self).buildChildren(child_, node, nodeName_, True)
# end class RelatedPerson
