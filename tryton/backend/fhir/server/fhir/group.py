from .base_classes import *
from .support_functions import *


class Group(Resource):
    """Represents a defined collection of entities that may be discussed or
    acted upon collectively but which are not expected to act
    collectively and are not formally or legally recognized. I.e. A
    collection of entities that isn't an Organization.If the element
    is present, it must have either a @value, an @id, or extensions"""
    subclass = None
    superclass = Resource
    def __init__(self, id=None, extension=None, modifierExtension=None, language=None, text=None, contained=None, identifier=None, type_=None, actual=None, code=None, name=None, quantity=None, characteristic=None, member=None):
        self.original_tagname_ = None
        super(Group, self).__init__(id, extension, modifierExtension, language, text, contained, )
        self.identifier = identifier
        self.type_ = type_
        self.actual = actual
        self.code = code
        self.name = name
        self.quantity = quantity
        if characteristic is None:
            self.characteristic = []
        else:
            self.characteristic = characteristic
        if member is None:
            self.member = []
        else:
            self.member = member
    def factory(*args_, **kwargs_):
        if Group.subclass:
            return Group.subclass(*args_, **kwargs_)
        else:
            return Group(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_identifier(self): return self.identifier
    def set_identifier(self, identifier): self.identifier = identifier
    def get_type(self): return self.type_
    def set_type(self, type_): self.type_ = type_
    def get_actual(self): return self.actual
    def set_actual(self, actual): self.actual = actual
    def get_code(self): return self.code
    def set_code(self, code): self.code = code
    def get_name(self): return self.name
    def set_name(self, name): self.name = name
    def get_quantity(self): return self.quantity
    def set_quantity(self, quantity): self.quantity = quantity
    def get_characteristic(self): return self.characteristic
    def set_characteristic(self, characteristic): self.characteristic = characteristic
    def add_characteristic(self, value): self.characteristic.append(value)
    def insert_characteristic(self, index, value): self.characteristic[index] = value
    def get_member(self): return self.member
    def set_member(self, member): self.member = member
    def add_member(self, value): self.member.append(value)
    def insert_member(self, index, value): self.member[index] = value
    def hasContent_(self):
        if (
            self.identifier is not None or
            self.type_ is not None or
            self.actual is not None or
            self.code is not None or
            self.name is not None or
            self.quantity is not None or
            self.characteristic or
            self.member or
            super(Group, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Group', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Group')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Group', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Group'):
        super(Group, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Group')
    def exportChildren(self, outfile, level, namespace_='', name_='Group', fromsubclass_=False, pretty_print=True):
        super(Group, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.identifier is not None:
            self.identifier.export(outfile, level, namespace_, name_='identifier', pretty_print=pretty_print)
        if self.type_ is not None:
            self.type_.export(outfile, level, namespace_, name_='type', pretty_print=pretty_print)
        if self.actual is not None:
            self.actual.export(outfile, level, namespace_, name_='actual', pretty_print=pretty_print)
        if self.code is not None:
            self.code.export(outfile, level, namespace_, name_='code', pretty_print=pretty_print)
        if self.name is not None:
            self.name.export(outfile, level, namespace_, name_='name', pretty_print=pretty_print)
        if self.quantity is not None:
            self.quantity.export(outfile, level, namespace_, name_='quantity', pretty_print=pretty_print)
        for characteristic_ in self.characteristic:
            characteristic_.export(outfile, level, namespace_, name_='characteristic', pretty_print=pretty_print)
        for member_ in self.member:
            member_.export(outfile, level, namespace_, name_='member', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Group', mapping_=None):
        element = super(Group, self).to_etree(parent_element, name_, mapping_)
        if self.identifier is not None:
            identifier_ = self.identifier
            identifier_.to_etree(element, name_='identifier', mapping_=mapping_)
        if self.type_ is not None:
            type__ = self.type_
            type__.to_etree(element, name_='type', mapping_=mapping_)
        if self.actual is not None:
            actual_ = self.actual
            actual_.to_etree(element, name_='actual', mapping_=mapping_)
        if self.code is not None:
            code_ = self.code
            code_.to_etree(element, name_='code', mapping_=mapping_)
        if self.name is not None:
            name_ = self.name
            name_.to_etree(element, name_='name', mapping_=mapping_)
        if self.quantity is not None:
            quantity_ = self.quantity
            quantity_.to_etree(element, name_='quantity', mapping_=mapping_)
        for characteristic_ in self.characteristic:
            characteristic_.to_etree(element, name_='characteristic', mapping_=mapping_)
        for member_ in self.member:
            member_.to_etree(element, name_='member', mapping_=mapping_)
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
        super(Group, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'identifier':
            obj_ = Identifier.factory()
            obj_.build(child_)
            self.identifier = obj_
            obj_.original_tagname_ = 'identifier'
        elif nodeName_ == 'type':
            obj_ = GroupType.factory()
            obj_.build(child_)
            self.type_ = obj_
            obj_.original_tagname_ = 'type'
        elif nodeName_ == 'actual':
            obj_ = boolean.factory()
            obj_.build(child_)
            self.actual = obj_
            obj_.original_tagname_ = 'actual'
        elif nodeName_ == 'code':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.code = obj_
            obj_.original_tagname_ = 'code'
        elif nodeName_ == 'name':
            obj_ = string.factory()
            obj_.build(child_)
            self.name = obj_
            obj_.original_tagname_ = 'name'
        elif nodeName_ == 'quantity':
            obj_ = integer.factory()
            obj_.build(child_)
            self.quantity = obj_
            obj_.original_tagname_ = 'quantity'
        elif nodeName_ == 'characteristic':
            obj_ = Group_Characteristic.factory()
            obj_.build(child_)
            self.characteristic.append(obj_)
            obj_.original_tagname_ = 'characteristic'
        elif nodeName_ == 'member':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.member.append(obj_)
            obj_.original_tagname_ = 'member'
        super(Group, self).buildChildren(child_, node, nodeName_, True)
# end class Group


class Group_Characteristic(BackboneElement):
    """Represents a defined collection of entities that may be discussed or
    acted upon collectively but which are not expected to act
    collectively and are not formally or legally recognized. I.e. A
    collection of entities that isn't an Organization.The value of
    the trait that holds (or does not hold - see 'exclude') for
    members of the group."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, code=None, valueCodeableConcept=None, valueBoolean=None, valueQuantity=None, valueRange=None, exclude=None):
        self.original_tagname_ = None
        super(Group_Characteristic, self).__init__(id, extension, modifierExtension, )
        self.code = code
        self.valueCodeableConcept = valueCodeableConcept
        self.valueBoolean = valueBoolean
        self.valueQuantity = valueQuantity
        self.valueRange = valueRange
        self.exclude = exclude
    def factory(*args_, **kwargs_):
        if Group_Characteristic.subclass:
            return Group_Characteristic.subclass(*args_, **kwargs_)
        else:
            return Group_Characteristic(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_code(self): return self.code
    def set_code(self, code): self.code = code
    def get_valueCodeableConcept(self): return self.valueCodeableConcept
    def set_valueCodeableConcept(self, valueCodeableConcept): self.valueCodeableConcept = valueCodeableConcept
    def get_valueBoolean(self): return self.valueBoolean
    def set_valueBoolean(self, valueBoolean): self.valueBoolean = valueBoolean
    def get_valueQuantity(self): return self.valueQuantity
    def set_valueQuantity(self, valueQuantity): self.valueQuantity = valueQuantity
    def get_valueRange(self): return self.valueRange
    def set_valueRange(self, valueRange): self.valueRange = valueRange
    def get_exclude(self): return self.exclude
    def set_exclude(self, exclude): self.exclude = exclude
    def hasContent_(self):
        if (
            self.code is not None or
            self.valueCodeableConcept is not None or
            self.valueBoolean is not None or
            self.valueQuantity is not None or
            self.valueRange is not None or
            self.exclude is not None or
            super(Group_Characteristic, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Group.Characteristic', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Group.Characteristic')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Group.Characteristic', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Group.Characteristic'):
        super(Group_Characteristic, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Group.Characteristic')
    def exportChildren(self, outfile, level, namespace_='', name_='Group.Characteristic', fromsubclass_=False, pretty_print=True):
        super(Group_Characteristic, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.code is not None:
            self.code.export(outfile, level, namespace_, name_='code', pretty_print=pretty_print)
        if self.valueCodeableConcept is not None:
            self.valueCodeableConcept.export(outfile, level, namespace_, name_='valueCodeableConcept', pretty_print=pretty_print)
        if self.valueBoolean is not None:
            self.valueBoolean.export(outfile, level, namespace_, name_='valueBoolean', pretty_print=pretty_print)
        if self.valueQuantity is not None:
            self.valueQuantity.export(outfile, level, namespace_, name_='valueQuantity', pretty_print=pretty_print)
        if self.valueRange is not None:
            self.valueRange.export(outfile, level, namespace_, name_='valueRange', pretty_print=pretty_print)
        if self.exclude is not None:
            self.exclude.export(outfile, level, namespace_, name_='exclude', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Group.Characteristic', mapping_=None):
        element = super(Group_Characteristic, self).to_etree(parent_element, name_, mapping_)
        if self.code is not None:
            code_ = self.code
            code_.to_etree(element, name_='code', mapping_=mapping_)
        if self.valueCodeableConcept is not None:
            valueCodeableConcept_ = self.valueCodeableConcept
            valueCodeableConcept_.to_etree(element, name_='valueCodeableConcept', mapping_=mapping_)
        if self.valueBoolean is not None:
            valueBoolean_ = self.valueBoolean
            valueBoolean_.to_etree(element, name_='valueBoolean', mapping_=mapping_)
        if self.valueQuantity is not None:
            valueQuantity_ = self.valueQuantity
            valueQuantity_.to_etree(element, name_='valueQuantity', mapping_=mapping_)
        if self.valueRange is not None:
            valueRange_ = self.valueRange
            valueRange_.to_etree(element, name_='valueRange', mapping_=mapping_)
        if self.exclude is not None:
            exclude_ = self.exclude
            exclude_.to_etree(element, name_='exclude', mapping_=mapping_)
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
        super(Group_Characteristic, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'code':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.code = obj_
            obj_.original_tagname_ = 'code'
        elif nodeName_ == 'valueCodeableConcept':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.valueCodeableConcept = obj_
            obj_.original_tagname_ = 'valueCodeableConcept'
        elif nodeName_ == 'valueBoolean':
            obj_ = boolean.factory()
            obj_.build(child_)
            self.valueBoolean = obj_
            obj_.original_tagname_ = 'valueBoolean'
        elif nodeName_ == 'valueQuantity':
            obj_ = Quantity.factory()
            obj_.build(child_)
            self.valueQuantity = obj_
            obj_.original_tagname_ = 'valueQuantity'
        elif nodeName_ == 'valueRange':
            obj_ = Range.factory()
            obj_.build(child_)
            self.valueRange = obj_
            obj_.original_tagname_ = 'valueRange'
        elif nodeName_ == 'exclude':
            obj_ = boolean.factory()
            obj_.build(child_)
            self.exclude = obj_
            obj_.original_tagname_ = 'exclude'
        super(Group_Characteristic, self).buildChildren(child_, node, nodeName_, True)
# end class Group_Characteristic


class GroupType(Element):
    """Types of resources that are part of groupIf the element is present,
    it must have either a @value, an @id, or extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(GroupType, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if GroupType.subclass:
            return GroupType.subclass(*args_, **kwargs_)
        else:
            return GroupType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(GroupType, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='GroupType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='GroupType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='GroupType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='GroupType'):
        super(GroupType, self).exportAttributes(outfile, level, already_processed, namespace_, name_='GroupType')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='GroupType', fromsubclass_=False, pretty_print=True):
        super(GroupType, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='GroupType', mapping_=None):
        element = super(GroupType, self).to_etree(parent_element, name_, mapping_)
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
        super(GroupType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(GroupType, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class GroupType
