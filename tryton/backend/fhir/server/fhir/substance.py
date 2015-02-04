from .base_classes import *
from .support_functions import *


class Substance(Resource):
    """A homogeneous material with a definite composition.If the element is
    present, it must have either a @value, an @id, or extensions"""
    subclass = None
    superclass = Resource
    def __init__(self, id=None, extension=None, modifierExtension=None, language=None, text=None, contained=None, type_=None, description=None, instance=None, ingredient=None):
        self.original_tagname_ = None
        super(Substance, self).__init__(id, extension, modifierExtension, language, text, contained, )
        self.type_ = type_
        self.description = description
        self.instance = instance
        if ingredient is None:
            self.ingredient = []
        else:
            self.ingredient = ingredient
    def factory(*args_, **kwargs_):
        if Substance.subclass:
            return Substance.subclass(*args_, **kwargs_)
        else:
            return Substance(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_type(self): return self.type_
    def set_type(self, type_): self.type_ = type_
    def get_description(self): return self.description
    def set_description(self, description): self.description = description
    def get_instance(self): return self.instance
    def set_instance(self, instance): self.instance = instance
    def get_ingredient(self): return self.ingredient
    def set_ingredient(self, ingredient): self.ingredient = ingredient
    def add_ingredient(self, value): self.ingredient.append(value)
    def insert_ingredient(self, index, value): self.ingredient[index] = value
    def hasContent_(self):
        if (
            self.type_ is not None or
            self.description is not None or
            self.instance is not None or
            self.ingredient or
            super(Substance, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Substance', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Substance')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Substance', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Substance'):
        super(Substance, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Substance')
    def exportChildren(self, outfile, level, namespace_='', name_='Substance', fromsubclass_=False, pretty_print=True):
        super(Substance, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.type_ is not None:
            self.type_.export(outfile, level, namespace_, name_='type', pretty_print=pretty_print)
        if self.description is not None:
            self.description.export(outfile, level, namespace_, name_='description', pretty_print=pretty_print)
        if self.instance is not None:
            self.instance.export(outfile, level, namespace_, name_='instance', pretty_print=pretty_print)
        for ingredient_ in self.ingredient:
            ingredient_.export(outfile, level, namespace_, name_='ingredient', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Substance', mapping_=None):
        element = super(Substance, self).to_etree(parent_element, name_, mapping_)
        if self.type_ is not None:
            type__ = self.type_
            type__.to_etree(element, name_='type', mapping_=mapping_)
        if self.description is not None:
            description_ = self.description
            description_.to_etree(element, name_='description', mapping_=mapping_)
        if self.instance is not None:
            instance_ = self.instance
            instance_.to_etree(element, name_='instance', mapping_=mapping_)
        for ingredient_ in self.ingredient:
            ingredient_.to_etree(element, name_='ingredient', mapping_=mapping_)
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
        super(Substance, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'type':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.type_ = obj_
            obj_.original_tagname_ = 'type'
        elif nodeName_ == 'description':
            obj_ = string.factory()
            obj_.build(child_)
            self.description = obj_
            obj_.original_tagname_ = 'description'
        elif nodeName_ == 'instance':
            obj_ = Substance_Instance.factory()
            obj_.build(child_)
            self.instance = obj_
            obj_.original_tagname_ = 'instance'
        elif nodeName_ == 'ingredient':
            obj_ = Substance_Ingredient.factory()
            obj_.build(child_)
            self.ingredient.append(obj_)
            obj_.original_tagname_ = 'ingredient'
        super(Substance, self).buildChildren(child_, node, nodeName_, True)
# end class Substance


class Substance_Instance(BackboneElement):
    """A homogeneous material with a definite composition."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, identifier=None, expiry=None, quantity=None):
        self.original_tagname_ = None
        super(Substance_Instance, self).__init__(id, extension, modifierExtension, )
        self.identifier = identifier
        self.expiry = expiry
        self.quantity = quantity
    def factory(*args_, **kwargs_):
        if Substance_Instance.subclass:
            return Substance_Instance.subclass(*args_, **kwargs_)
        else:
            return Substance_Instance(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_identifier(self): return self.identifier
    def set_identifier(self, identifier): self.identifier = identifier
    def get_expiry(self): return self.expiry
    def set_expiry(self, expiry): self.expiry = expiry
    def get_quantity(self): return self.quantity
    def set_quantity(self, quantity): self.quantity = quantity
    def hasContent_(self):
        if (
            self.identifier is not None or
            self.expiry is not None or
            self.quantity is not None or
            super(Substance_Instance, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Substance.Instance', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Substance.Instance')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Substance.Instance', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Substance.Instance'):
        super(Substance_Instance, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Substance.Instance')
    def exportChildren(self, outfile, level, namespace_='', name_='Substance.Instance', fromsubclass_=False, pretty_print=True):
        super(Substance_Instance, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.identifier is not None:
            self.identifier.export(outfile, level, namespace_, name_='identifier', pretty_print=pretty_print)
        if self.expiry is not None:
            self.expiry.export(outfile, level, namespace_, name_='expiry', pretty_print=pretty_print)
        if self.quantity is not None:
            self.quantity.export(outfile, level, namespace_, name_='quantity', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Substance.Instance', mapping_=None):
        element = super(Substance_Instance, self).to_etree(parent_element, name_, mapping_)
        if self.identifier is not None:
            identifier_ = self.identifier
            identifier_.to_etree(element, name_='identifier', mapping_=mapping_)
        if self.expiry is not None:
            expiry_ = self.expiry
            expiry_.to_etree(element, name_='expiry', mapping_=mapping_)
        if self.quantity is not None:
            quantity_ = self.quantity
            quantity_.to_etree(element, name_='quantity', mapping_=mapping_)
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
        super(Substance_Instance, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'identifier':
            obj_ = Identifier.factory()
            obj_.build(child_)
            self.identifier = obj_
            obj_.original_tagname_ = 'identifier'
        elif nodeName_ == 'expiry':
            obj_ = dateTime.factory()
            obj_.build(child_)
            self.expiry = obj_
            obj_.original_tagname_ = 'expiry'
        elif nodeName_ == 'quantity':
            obj_ = Quantity.factory()
            obj_.build(child_)
            self.quantity = obj_
            obj_.original_tagname_ = 'quantity'
        super(Substance_Instance, self).buildChildren(child_, node, nodeName_, True)
# end class Substance_Instance


class Substance_Ingredient(BackboneElement):
    """A homogeneous material with a definite composition."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, quantity=None, substance=None):
        self.original_tagname_ = None
        super(Substance_Ingredient, self).__init__(id, extension, modifierExtension, )
        self.quantity = quantity
        self.substance = substance
    def factory(*args_, **kwargs_):
        if Substance_Ingredient.subclass:
            return Substance_Ingredient.subclass(*args_, **kwargs_)
        else:
            return Substance_Ingredient(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_quantity(self): return self.quantity
    def set_quantity(self, quantity): self.quantity = quantity
    def get_substance(self): return self.substance
    def set_substance(self, substance): self.substance = substance
    def hasContent_(self):
        if (
            self.quantity is not None or
            self.substance is not None or
            super(Substance_Ingredient, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Substance.Ingredient', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Substance.Ingredient')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Substance.Ingredient', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Substance.Ingredient'):
        super(Substance_Ingredient, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Substance.Ingredient')
    def exportChildren(self, outfile, level, namespace_='', name_='Substance.Ingredient', fromsubclass_=False, pretty_print=True):
        super(Substance_Ingredient, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.quantity is not None:
            self.quantity.export(outfile, level, namespace_, name_='quantity', pretty_print=pretty_print)
        if self.substance is not None:
            self.substance.export(outfile, level, namespace_, name_='substance', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Substance.Ingredient', mapping_=None):
        element = super(Substance_Ingredient, self).to_etree(parent_element, name_, mapping_)
        if self.quantity is not None:
            quantity_ = self.quantity
            quantity_.to_etree(element, name_='quantity', mapping_=mapping_)
        if self.substance is not None:
            substance_ = self.substance
            substance_.to_etree(element, name_='substance', mapping_=mapping_)
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
        super(Substance_Ingredient, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'quantity':
            obj_ = Ratio.factory()
            obj_.build(child_)
            self.quantity = obj_
            obj_.original_tagname_ = 'quantity'
        elif nodeName_ == 'substance':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.substance = obj_
            obj_.original_tagname_ = 'substance'
        super(Substance_Ingredient, self).buildChildren(child_, node, nodeName_, True)
# end class Substance_Ingredient
