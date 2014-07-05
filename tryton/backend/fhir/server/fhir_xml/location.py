from .base_classes import *
from .support_functions import *


class Location(Resource):
    """Details and position information for a physical place where services
    are provided and resources and participants may be stored,
    found, contained or accommodated.If the element is present, it
    must have either a @value, an @id, or extensions"""
    subclass = None
    superclass = Resource
    def __init__(self, id=None, extension=None, modifierExtension=None, language=None, text=None, contained=None, identifier=None, name=None, description=None, type_=None, telecom=None, address=None, physicalType=None, position=None, managingOrganization=None, status=None, partOf=None, mode=None):
        self.original_tagname_ = None
        super(Location, self).__init__(id, extension, modifierExtension, language, text, contained, )
        self.identifier = identifier
        self.name = name
        self.description = description
        self.type_ = type_
        if telecom is None:
            self.telecom = []
        else:
            self.telecom = telecom
        self.address = address
        self.physicalType = physicalType
        self.position = position
        self.managingOrganization = managingOrganization
        self.status = status
        self.partOf = partOf
        self.mode = mode
    def factory(*args_, **kwargs_):
        if Location.subclass:
            return Location.subclass(*args_, **kwargs_)
        else:
            return Location(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_identifier(self): return self.identifier
    def set_identifier(self, identifier): self.identifier = identifier
    def get_name(self): return self.name
    def set_name(self, name): self.name = name
    def get_description(self): return self.description
    def set_description(self, description): self.description = description
    def get_type(self): return self.type_
    def set_type(self, type_): self.type_ = type_
    def get_telecom(self): return self.telecom
    def set_telecom(self, telecom): self.telecom = telecom
    def add_telecom(self, value): self.telecom.append(value)
    def insert_telecom(self, index, value): self.telecom[index] = value
    def get_address(self): return self.address
    def set_address(self, address): self.address = address
    def get_physicalType(self): return self.physicalType
    def set_physicalType(self, physicalType): self.physicalType = physicalType
    def get_position(self): return self.position
    def set_position(self, position): self.position = position
    def get_managingOrganization(self): return self.managingOrganization
    def set_managingOrganization(self, managingOrganization): self.managingOrganization = managingOrganization
    def get_status(self): return self.status
    def set_status(self, status): self.status = status
    def get_partOf(self): return self.partOf
    def set_partOf(self, partOf): self.partOf = partOf
    def get_mode(self): return self.mode
    def set_mode(self, mode): self.mode = mode
    def hasContent_(self):
        if (
            self.identifier is not None or
            self.name is not None or
            self.description is not None or
            self.type_ is not None or
            self.telecom or
            self.address is not None or
            self.physicalType is not None or
            self.position is not None or
            self.managingOrganization is not None or
            self.status is not None or
            self.partOf is not None or
            self.mode is not None or
            super(Location, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Location', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Location')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Location', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Location'):
        super(Location, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Location')
    def exportChildren(self, outfile, level, namespace_='', name_='Location', fromsubclass_=False, pretty_print=True):
        super(Location, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.identifier is not None:
            self.identifier.export(outfile, level, namespace_, name_='identifier', pretty_print=pretty_print)
        if self.name is not None:
            self.name.export(outfile, level, namespace_, name_='name', pretty_print=pretty_print)
        if self.description is not None:
            self.description.export(outfile, level, namespace_, name_='description', pretty_print=pretty_print)
        if self.type_ is not None:
            self.type_.export(outfile, level, namespace_, name_='type', pretty_print=pretty_print)
        for telecom_ in self.telecom:
            telecom_.export(outfile, level, namespace_, name_='telecom', pretty_print=pretty_print)
        if self.address is not None:
            self.address.export(outfile, level, namespace_, name_='address', pretty_print=pretty_print)
        if self.physicalType is not None:
            self.physicalType.export(outfile, level, namespace_, name_='physicalType', pretty_print=pretty_print)
        if self.position is not None:
            self.position.export(outfile, level, namespace_, name_='position', pretty_print=pretty_print)
        if self.managingOrganization is not None:
            self.managingOrganization.export(outfile, level, namespace_, name_='managingOrganization', pretty_print=pretty_print)
        if self.status is not None:
            self.status.export(outfile, level, namespace_, name_='status', pretty_print=pretty_print)
        if self.partOf is not None:
            self.partOf.export(outfile, level, namespace_, name_='partOf', pretty_print=pretty_print)
        if self.mode is not None:
            self.mode.export(outfile, level, namespace_, name_='mode', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Location', mapping_=None):
        element = super(Location, self).to_etree(parent_element, name_, mapping_)
        if self.identifier is not None:
            identifier_ = self.identifier
            identifier_.to_etree(element, name_='identifier', mapping_=mapping_)
        if self.name is not None:
            name_ = self.name
            name_.to_etree(element, name_='name', mapping_=mapping_)
        if self.description is not None:
            description_ = self.description
            description_.to_etree(element, name_='description', mapping_=mapping_)
        if self.type_ is not None:
            type__ = self.type_
            type__.to_etree(element, name_='type', mapping_=mapping_)
        for telecom_ in self.telecom:
            telecom_.to_etree(element, name_='telecom', mapping_=mapping_)
        if self.address is not None:
            address_ = self.address
            address_.to_etree(element, name_='address', mapping_=mapping_)
        if self.physicalType is not None:
            physicalType_ = self.physicalType
            physicalType_.to_etree(element, name_='physicalType', mapping_=mapping_)
        if self.position is not None:
            position_ = self.position
            position_.to_etree(element, name_='position', mapping_=mapping_)
        if self.managingOrganization is not None:
            managingOrganization_ = self.managingOrganization
            managingOrganization_.to_etree(element, name_='managingOrganization', mapping_=mapping_)
        if self.status is not None:
            status_ = self.status
            status_.to_etree(element, name_='status', mapping_=mapping_)
        if self.partOf is not None:
            partOf_ = self.partOf
            partOf_.to_etree(element, name_='partOf', mapping_=mapping_)
        if self.mode is not None:
            mode_ = self.mode
            mode_.to_etree(element, name_='mode', mapping_=mapping_)
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
        super(Location, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'identifier':
            obj_ = Identifier.factory()
            obj_.build(child_)
            self.identifier = obj_
            obj_.original_tagname_ = 'identifier'
        elif nodeName_ == 'name':
            obj_ = string.factory()
            obj_.build(child_)
            self.name = obj_
            obj_.original_tagname_ = 'name'
        elif nodeName_ == 'description':
            obj_ = string.factory()
            obj_.build(child_)
            self.description = obj_
            obj_.original_tagname_ = 'description'
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
            self.address = obj_
            obj_.original_tagname_ = 'address'
        elif nodeName_ == 'physicalType':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.physicalType = obj_
            obj_.original_tagname_ = 'physicalType'
        elif nodeName_ == 'position':
            obj_ = Location_Position.factory()
            obj_.build(child_)
            self.position = obj_
            obj_.original_tagname_ = 'position'
        elif nodeName_ == 'managingOrganization':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.managingOrganization = obj_
            obj_.original_tagname_ = 'managingOrganization'
        elif nodeName_ == 'status':
            obj_ = LocationStatus.factory()
            obj_.build(child_)
            self.status = obj_
            obj_.original_tagname_ = 'status'
        elif nodeName_ == 'partOf':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.partOf = obj_
            obj_.original_tagname_ = 'partOf'
        elif nodeName_ == 'mode':
            obj_ = LocationMode.factory()
            obj_.build(child_)
            self.mode = obj_
            obj_.original_tagname_ = 'mode'
        super(Location, self).buildChildren(child_, node, nodeName_, True)
# end class Location


class Location_Position(BackboneElement):
    """Details and position information for a physical place where services
    are provided and resources and participants may be stored,
    found, contained or accommodated."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, longitude=None, latitude=None, altitude=None):
        self.original_tagname_ = None
        super(Location_Position, self).__init__(id, extension, modifierExtension, )
        self.longitude = longitude
        self.latitude = latitude
        self.altitude = altitude
    def factory(*args_, **kwargs_):
        if Location_Position.subclass:
            return Location_Position.subclass(*args_, **kwargs_)
        else:
            return Location_Position(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_longitude(self): return self.longitude
    def set_longitude(self, longitude): self.longitude = longitude
    def get_latitude(self): return self.latitude
    def set_latitude(self, latitude): self.latitude = latitude
    def get_altitude(self): return self.altitude
    def set_altitude(self, altitude): self.altitude = altitude
    def hasContent_(self):
        if (
            self.longitude is not None or
            self.latitude is not None or
            self.altitude is not None or
            super(Location_Position, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Location.Position', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Location.Position')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Location.Position', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Location.Position'):
        super(Location_Position, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Location.Position')
    def exportChildren(self, outfile, level, namespace_='', name_='Location.Position', fromsubclass_=False, pretty_print=True):
        super(Location_Position, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.longitude is not None:
            self.longitude.export(outfile, level, namespace_, name_='longitude', pretty_print=pretty_print)
        if self.latitude is not None:
            self.latitude.export(outfile, level, namespace_, name_='latitude', pretty_print=pretty_print)
        if self.altitude is not None:
            self.altitude.export(outfile, level, namespace_, name_='altitude', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Location.Position', mapping_=None):
        element = super(Location_Position, self).to_etree(parent_element, name_, mapping_)
        if self.longitude is not None:
            longitude_ = self.longitude
            longitude_.to_etree(element, name_='longitude', mapping_=mapping_)
        if self.latitude is not None:
            latitude_ = self.latitude
            latitude_.to_etree(element, name_='latitude', mapping_=mapping_)
        if self.altitude is not None:
            altitude_ = self.altitude
            altitude_.to_etree(element, name_='altitude', mapping_=mapping_)
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
        super(Location_Position, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'longitude':
            obj_ = decimal.factory()
            obj_.build(child_)
            self.longitude = obj_
            obj_.original_tagname_ = 'longitude'
        elif nodeName_ == 'latitude':
            obj_ = decimal.factory()
            obj_.build(child_)
            self.latitude = obj_
            obj_.original_tagname_ = 'latitude'
        elif nodeName_ == 'altitude':
            obj_ = decimal.factory()
            obj_.build(child_)
            self.altitude = obj_
            obj_.original_tagname_ = 'altitude'
        super(Location_Position, self).buildChildren(child_, node, nodeName_, True)
# end class Location_Position


class LocationStatus(Element):
    """Indicates whether the location is still in useIf the element is
    present, it must have either a @value, an @id, or extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(LocationStatus, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if LocationStatus.subclass:
            return LocationStatus.subclass(*args_, **kwargs_)
        else:
            return LocationStatus(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(LocationStatus, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='LocationStatus', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='LocationStatus')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='LocationStatus', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='LocationStatus'):
        super(LocationStatus, self).exportAttributes(outfile, level, already_processed, namespace_, name_='LocationStatus')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='LocationStatus', fromsubclass_=False, pretty_print=True):
        super(LocationStatus, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='LocationStatus', mapping_=None):
        element = super(LocationStatus, self).to_etree(parent_element, name_, mapping_)
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
        super(LocationStatus, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(LocationStatus, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class LocationStatus


class LocationMode(Element):
    """Indicates whether a resource instance represents a specific location
    or a class of locationsIf the element is present, it must have
    either a @value, an @id, or extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(LocationMode, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if LocationMode.subclass:
            return LocationMode.subclass(*args_, **kwargs_)
        else:
            return LocationMode(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(LocationMode, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='LocationMode', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='LocationMode')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='LocationMode', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='LocationMode'):
        super(LocationMode, self).exportAttributes(outfile, level, already_processed, namespace_, name_='LocationMode')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='LocationMode', fromsubclass_=False, pretty_print=True):
        super(LocationMode, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='LocationMode', mapping_=None):
        element = super(LocationMode, self).to_etree(parent_element, name_, mapping_)
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
        super(LocationMode, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(LocationMode, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class LocationMode
