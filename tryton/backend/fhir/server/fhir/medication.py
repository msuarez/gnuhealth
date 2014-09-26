from .base_classes import *
from .support_functions import *


class Medication(Resource):
    """Primarily used for identification and definition of Medication, but
    also covers ingredients and packaging.If the element is present,
    it must have either a @value, an @id, or extensions"""
    subclass = None
    superclass = Resource
    def __init__(self, id=None, extension=None, modifierExtension=None, language=None, text=None, contained=None, name=None, code=None, isBrand=None, manufacturer=None, kind=None, product=None, package=None):
        self.original_tagname_ = None
        super(Medication, self).__init__(id, extension, modifierExtension, language, text, contained, )
        self.name = name
        self.code = code
        self.isBrand = isBrand
        self.manufacturer = manufacturer
        self.kind = kind
        self.product = product
        self.package = package
    def factory(*args_, **kwargs_):
        if Medication.subclass:
            return Medication.subclass(*args_, **kwargs_)
        else:
            return Medication(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_name(self): return self.name
    def set_name(self, name): self.name = name
    def get_code(self): return self.code
    def set_code(self, code): self.code = code
    def get_isBrand(self): return self.isBrand
    def set_isBrand(self, isBrand): self.isBrand = isBrand
    def get_manufacturer(self): return self.manufacturer
    def set_manufacturer(self, manufacturer): self.manufacturer = manufacturer
    def get_kind(self): return self.kind
    def set_kind(self, kind): self.kind = kind
    def get_product(self): return self.product
    def set_product(self, product): self.product = product
    def get_package(self): return self.package
    def set_package(self, package): self.package = package
    def hasContent_(self):
        if (
            self.name is not None or
            self.code is not None or
            self.isBrand is not None or
            self.manufacturer is not None or
            self.kind is not None or
            self.product is not None or
            self.package is not None or
            super(Medication, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Medication', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Medication')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Medication', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Medication'):
        super(Medication, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Medication')
    def exportChildren(self, outfile, level, namespace_='', name_='Medication', fromsubclass_=False, pretty_print=True):
        super(Medication, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.name is not None:
            self.name.export(outfile, level, namespace_, name_='name', pretty_print=pretty_print)
        if self.code is not None:
            self.code.export(outfile, level, namespace_, name_='code', pretty_print=pretty_print)
        if self.isBrand is not None:
            self.isBrand.export(outfile, level, namespace_, name_='isBrand', pretty_print=pretty_print)
        if self.manufacturer is not None:
            self.manufacturer.export(outfile, level, namespace_, name_='manufacturer', pretty_print=pretty_print)
        if self.kind is not None:
            self.kind.export(outfile, level, namespace_, name_='kind', pretty_print=pretty_print)
        if self.product is not None:
            self.product.export(outfile, level, namespace_, name_='product', pretty_print=pretty_print)
        if self.package is not None:
            self.package.export(outfile, level, namespace_, name_='package', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Medication', mapping_=None):
        element = super(Medication, self).to_etree(parent_element, name_, mapping_)
        if self.name is not None:
            name_ = self.name
            name_.to_etree(element, name_='name', mapping_=mapping_)
        if self.code is not None:
            code_ = self.code
            code_.to_etree(element, name_='code', mapping_=mapping_)
        if self.isBrand is not None:
            isBrand_ = self.isBrand
            isBrand_.to_etree(element, name_='isBrand', mapping_=mapping_)
        if self.manufacturer is not None:
            manufacturer_ = self.manufacturer
            manufacturer_.to_etree(element, name_='manufacturer', mapping_=mapping_)
        if self.kind is not None:
            kind_ = self.kind
            kind_.to_etree(element, name_='kind', mapping_=mapping_)
        if self.product is not None:
            product_ = self.product
            product_.to_etree(element, name_='product', mapping_=mapping_)
        if self.package is not None:
            package_ = self.package
            package_.to_etree(element, name_='package', mapping_=mapping_)
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
        super(Medication, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'name':
            obj_ = string.factory()
            obj_.build(child_)
            self.name = obj_
            obj_.original_tagname_ = 'name'
        elif nodeName_ == 'code':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.code = obj_
            obj_.original_tagname_ = 'code'
        elif nodeName_ == 'isBrand':
            obj_ = boolean.factory()
            obj_.build(child_)
            self.isBrand = obj_
            obj_.original_tagname_ = 'isBrand'
        elif nodeName_ == 'manufacturer':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.manufacturer = obj_
            obj_.original_tagname_ = 'manufacturer'
        elif nodeName_ == 'kind':
            obj_ = MedicationKind.factory()
            obj_.build(child_)
            self.kind = obj_
            obj_.original_tagname_ = 'kind'
        elif nodeName_ == 'product':
            obj_ = Medication_Product.factory()
            obj_.build(child_)
            self.product = obj_
            obj_.original_tagname_ = 'product'
        elif nodeName_ == 'package':
            obj_ = Medication_Package.factory()
            obj_.build(child_)
            self.package = obj_
            obj_.original_tagname_ = 'package'
        super(Medication, self).buildChildren(child_, node, nodeName_, True)
# end class Medication


class Medication_Product(BackboneElement):
    """Primarily used for identification and definition of Medication, but
    also covers ingredients and packaging."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, form=None, ingredient=None):
        self.original_tagname_ = None
        super(Medication_Product, self).__init__(id, extension, modifierExtension, )
        self.form = form
        if ingredient is None:
            self.ingredient = []
        else:
            self.ingredient = ingredient
    def factory(*args_, **kwargs_):
        if Medication_Product.subclass:
            return Medication_Product.subclass(*args_, **kwargs_)
        else:
            return Medication_Product(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_form(self): return self.form
    def set_form(self, form): self.form = form
    def get_ingredient(self): return self.ingredient
    def set_ingredient(self, ingredient): self.ingredient = ingredient
    def add_ingredient(self, value): self.ingredient.append(value)
    def insert_ingredient(self, index, value): self.ingredient[index] = value
    def hasContent_(self):
        if (
            self.form is not None or
            self.ingredient or
            super(Medication_Product, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Medication.Product', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Medication.Product')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Medication.Product', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Medication.Product'):
        super(Medication_Product, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Medication.Product')
    def exportChildren(self, outfile, level, namespace_='', name_='Medication.Product', fromsubclass_=False, pretty_print=True):
        super(Medication_Product, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.form is not None:
            self.form.export(outfile, level, namespace_, name_='form', pretty_print=pretty_print)
        for ingredient_ in self.ingredient:
            ingredient_.export(outfile, level, namespace_, name_='ingredient', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Medication.Product', mapping_=None):
        element = super(Medication_Product, self).to_etree(parent_element, name_, mapping_)
        if self.form is not None:
            form_ = self.form
            form_.to_etree(element, name_='form', mapping_=mapping_)
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
        super(Medication_Product, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'form':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.form = obj_
            obj_.original_tagname_ = 'form'
        elif nodeName_ == 'ingredient':
            obj_ = Medication_Ingredient.factory()
            obj_.build(child_)
            self.ingredient.append(obj_)
            obj_.original_tagname_ = 'ingredient'
        super(Medication_Product, self).buildChildren(child_, node, nodeName_, True)
# end class Medication_Product


class Medication_Ingredient(BackboneElement):
    """Primarily used for identification and definition of Medication, but
    also covers ingredients and packaging."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, item=None, amount=None):
        self.original_tagname_ = None
        super(Medication_Ingredient, self).__init__(id, extension, modifierExtension, )
        self.item = item
        self.amount = amount
    def factory(*args_, **kwargs_):
        if Medication_Ingredient.subclass:
            return Medication_Ingredient.subclass(*args_, **kwargs_)
        else:
            return Medication_Ingredient(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_item(self): return self.item
    def set_item(self, item): self.item = item
    def get_amount(self): return self.amount
    def set_amount(self, amount): self.amount = amount
    def hasContent_(self):
        if (
            self.item is not None or
            self.amount is not None or
            super(Medication_Ingredient, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Medication.Ingredient', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Medication.Ingredient')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Medication.Ingredient', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Medication.Ingredient'):
        super(Medication_Ingredient, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Medication.Ingredient')
    def exportChildren(self, outfile, level, namespace_='', name_='Medication.Ingredient', fromsubclass_=False, pretty_print=True):
        super(Medication_Ingredient, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.item is not None:
            self.item.export(outfile, level, namespace_, name_='item', pretty_print=pretty_print)
        if self.amount is not None:
            self.amount.export(outfile, level, namespace_, name_='amount', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Medication.Ingredient', mapping_=None):
        element = super(Medication_Ingredient, self).to_etree(parent_element, name_, mapping_)
        if self.item is not None:
            item_ = self.item
            item_.to_etree(element, name_='item', mapping_=mapping_)
        if self.amount is not None:
            amount_ = self.amount
            amount_.to_etree(element, name_='amount', mapping_=mapping_)
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
        super(Medication_Ingredient, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'item':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.item = obj_
            obj_.original_tagname_ = 'item'
        elif nodeName_ == 'amount':
            obj_ = Ratio.factory()
            obj_.build(child_)
            self.amount = obj_
            obj_.original_tagname_ = 'amount'
        super(Medication_Ingredient, self).buildChildren(child_, node, nodeName_, True)
# end class Medication_Ingredient


class Medication_Package(BackboneElement):
    """Primarily used for identification and definition of Medication, but
    also covers ingredients and packaging."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, container=None, content=None):
        self.original_tagname_ = None
        super(Medication_Package, self).__init__(id, extension, modifierExtension, )
        self.container = container
        if content is None:
            self.content = []
        else:
            self.content = content
    def factory(*args_, **kwargs_):
        if Medication_Package.subclass:
            return Medication_Package.subclass(*args_, **kwargs_)
        else:
            return Medication_Package(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_container(self): return self.container
    def set_container(self, container): self.container = container
    def get_content(self): return self.content
    def set_content(self, content): self.content = content
    def add_content(self, value): self.content.append(value)
    def insert_content(self, index, value): self.content[index] = value
    def hasContent_(self):
        if (
            self.container is not None or
            self.content or
            super(Medication_Package, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Medication.Package', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Medication.Package')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Medication.Package', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Medication.Package'):
        super(Medication_Package, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Medication.Package')
    def exportChildren(self, outfile, level, namespace_='', name_='Medication.Package', fromsubclass_=False, pretty_print=True):
        super(Medication_Package, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.container is not None:
            self.container.export(outfile, level, namespace_, name_='container', pretty_print=pretty_print)
        for content_ in self.content:
            content_.export(outfile, level, namespace_, name_='content', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Medication.Package', mapping_=None):
        element = super(Medication_Package, self).to_etree(parent_element, name_, mapping_)
        if self.container is not None:
            container_ = self.container
            container_.to_etree(element, name_='container', mapping_=mapping_)
        for content_ in self.content:
            content_.to_etree(element, name_='content', mapping_=mapping_)
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
        super(Medication_Package, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'container':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.container = obj_
            obj_.original_tagname_ = 'container'
        elif nodeName_ == 'content':
            obj_ = Medication_Content.factory()
            obj_.build(child_)
            self.content.append(obj_)
            obj_.original_tagname_ = 'content'
        super(Medication_Package, self).buildChildren(child_, node, nodeName_, True)
# end class Medication_Package


class Medication_Content(BackboneElement):
    """Primarily used for identification and definition of Medication, but
    also covers ingredients and packaging."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, item=None, amount=None):
        self.original_tagname_ = None
        super(Medication_Content, self).__init__(id, extension, modifierExtension, )
        self.item = item
        self.amount = amount
    def factory(*args_, **kwargs_):
        if Medication_Content.subclass:
            return Medication_Content.subclass(*args_, **kwargs_)
        else:
            return Medication_Content(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_item(self): return self.item
    def set_item(self, item): self.item = item
    def get_amount(self): return self.amount
    def set_amount(self, amount): self.amount = amount
    def hasContent_(self):
        if (
            self.item is not None or
            self.amount is not None or
            super(Medication_Content, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Medication.Content', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Medication.Content')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Medication.Content', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Medication.Content'):
        super(Medication_Content, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Medication.Content')
    def exportChildren(self, outfile, level, namespace_='', name_='Medication.Content', fromsubclass_=False, pretty_print=True):
        super(Medication_Content, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.item is not None:
            self.item.export(outfile, level, namespace_, name_='item', pretty_print=pretty_print)
        if self.amount is not None:
            self.amount.export(outfile, level, namespace_, name_='amount', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Medication.Content', mapping_=None):
        element = super(Medication_Content, self).to_etree(parent_element, name_, mapping_)
        if self.item is not None:
            item_ = self.item
            item_.to_etree(element, name_='item', mapping_=mapping_)
        if self.amount is not None:
            amount_ = self.amount
            amount_.to_etree(element, name_='amount', mapping_=mapping_)
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
        super(Medication_Content, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'item':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.item = obj_
            obj_.original_tagname_ = 'item'
        elif nodeName_ == 'amount':
            obj_ = Quantity.factory()
            obj_.build(child_)
            self.amount = obj_
            obj_.original_tagname_ = 'amount'
        super(Medication_Content, self).buildChildren(child_, node, nodeName_, True)
# end class Medication_Content


class MedicationKind(Element):
    """Whether the medication is a product or a packageIf the element is
    present, it must have either a @value, an @id, or extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(MedicationKind, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if MedicationKind.subclass:
            return MedicationKind.subclass(*args_, **kwargs_)
        else:
            return MedicationKind(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(MedicationKind, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='MedicationKind', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='MedicationKind')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='MedicationKind', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='MedicationKind'):
        super(MedicationKind, self).exportAttributes(outfile, level, already_processed, namespace_, name_='MedicationKind')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='MedicationKind', fromsubclass_=False, pretty_print=True):
        super(MedicationKind, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='MedicationKind', mapping_=None):
        element = super(MedicationKind, self).to_etree(parent_element, name_, mapping_)
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
        super(MedicationKind, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(MedicationKind, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class MedicationKind
