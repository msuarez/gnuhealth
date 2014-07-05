from .base_classes import *
from .support_functions import *


class Specimen(Resource):
    """Sample for analysis.If the element is present, it must have either a
    @value, an @id, or extensions"""
    subclass = None
    superclass = Resource
    def __init__(self, id=None, extension=None, modifierExtension=None, language=None, text=None, contained=None, identifier=None, type_=None, source=None, subject=None, accessionIdentifier=None, receivedTime=None, collection=None, treatment=None, container=None):
        self.original_tagname_ = None
        super(Specimen, self).__init__(id, extension, modifierExtension, language, text, contained, )
        if identifier is None:
            self.identifier = []
        else:
            self.identifier = identifier
        self.type_ = type_
        if source is None:
            self.source = []
        else:
            self.source = source
        self.subject = subject
        self.accessionIdentifier = accessionIdentifier
        self.receivedTime = receivedTime
        self.collection = collection
        if treatment is None:
            self.treatment = []
        else:
            self.treatment = treatment
        if container is None:
            self.container = []
        else:
            self.container = container
    def factory(*args_, **kwargs_):
        if Specimen.subclass:
            return Specimen.subclass(*args_, **kwargs_)
        else:
            return Specimen(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_identifier(self): return self.identifier
    def set_identifier(self, identifier): self.identifier = identifier
    def add_identifier(self, value): self.identifier.append(value)
    def insert_identifier(self, index, value): self.identifier[index] = value
    def get_type(self): return self.type_
    def set_type(self, type_): self.type_ = type_
    def get_source(self): return self.source
    def set_source(self, source): self.source = source
    def add_source(self, value): self.source.append(value)
    def insert_source(self, index, value): self.source[index] = value
    def get_subject(self): return self.subject
    def set_subject(self, subject): self.subject = subject
    def get_accessionIdentifier(self): return self.accessionIdentifier
    def set_accessionIdentifier(self, accessionIdentifier): self.accessionIdentifier = accessionIdentifier
    def get_receivedTime(self): return self.receivedTime
    def set_receivedTime(self, receivedTime): self.receivedTime = receivedTime
    def get_collection(self): return self.collection
    def set_collection(self, collection): self.collection = collection
    def get_treatment(self): return self.treatment
    def set_treatment(self, treatment): self.treatment = treatment
    def add_treatment(self, value): self.treatment.append(value)
    def insert_treatment(self, index, value): self.treatment[index] = value
    def get_container(self): return self.container
    def set_container(self, container): self.container = container
    def add_container(self, value): self.container.append(value)
    def insert_container(self, index, value): self.container[index] = value
    def hasContent_(self):
        if (
            self.identifier or
            self.type_ is not None or
            self.source or
            self.subject is not None or
            self.accessionIdentifier is not None or
            self.receivedTime is not None or
            self.collection is not None or
            self.treatment or
            self.container or
            super(Specimen, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Specimen', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Specimen')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Specimen', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Specimen'):
        super(Specimen, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Specimen')
    def exportChildren(self, outfile, level, namespace_='', name_='Specimen', fromsubclass_=False, pretty_print=True):
        super(Specimen, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for identifier_ in self.identifier:
            identifier_.export(outfile, level, namespace_, name_='identifier', pretty_print=pretty_print)
        if self.type_ is not None:
            self.type_.export(outfile, level, namespace_, name_='type', pretty_print=pretty_print)
        for source_ in self.source:
            source_.export(outfile, level, namespace_, name_='source', pretty_print=pretty_print)
        if self.subject is not None:
            self.subject.export(outfile, level, namespace_, name_='subject', pretty_print=pretty_print)
        if self.accessionIdentifier is not None:
            self.accessionIdentifier.export(outfile, level, namespace_, name_='accessionIdentifier', pretty_print=pretty_print)
        if self.receivedTime is not None:
            self.receivedTime.export(outfile, level, namespace_, name_='receivedTime', pretty_print=pretty_print)
        if self.collection is not None:
            self.collection.export(outfile, level, namespace_, name_='collection', pretty_print=pretty_print)
        for treatment_ in self.treatment:
            treatment_.export(outfile, level, namespace_, name_='treatment', pretty_print=pretty_print)
        for container_ in self.container:
            container_.export(outfile, level, namespace_, name_='container', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Specimen', mapping_=None):
        element = super(Specimen, self).to_etree(parent_element, name_, mapping_)
        for identifier_ in self.identifier:
            identifier_.to_etree(element, name_='identifier', mapping_=mapping_)
        if self.type_ is not None:
            type__ = self.type_
            type__.to_etree(element, name_='type', mapping_=mapping_)
        for source_ in self.source:
            source_.to_etree(element, name_='source', mapping_=mapping_)
        if self.subject is not None:
            subject_ = self.subject
            subject_.to_etree(element, name_='subject', mapping_=mapping_)
        if self.accessionIdentifier is not None:
            accessionIdentifier_ = self.accessionIdentifier
            accessionIdentifier_.to_etree(element, name_='accessionIdentifier', mapping_=mapping_)
        if self.receivedTime is not None:
            receivedTime_ = self.receivedTime
            receivedTime_.to_etree(element, name_='receivedTime', mapping_=mapping_)
        if self.collection is not None:
            collection_ = self.collection
            collection_.to_etree(element, name_='collection', mapping_=mapping_)
        for treatment_ in self.treatment:
            treatment_.to_etree(element, name_='treatment', mapping_=mapping_)
        for container_ in self.container:
            container_.to_etree(element, name_='container', mapping_=mapping_)
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
        super(Specimen, self).buildAttributes(node, attrs, already_processed)
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
        elif nodeName_ == 'source':
            obj_ = Specimen_Source.factory()
            obj_.build(child_)
            self.source.append(obj_)
            obj_.original_tagname_ = 'source'
        elif nodeName_ == 'subject':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.subject = obj_
            obj_.original_tagname_ = 'subject'
        elif nodeName_ == 'accessionIdentifier':
            obj_ = Identifier.factory()
            obj_.build(child_)
            self.accessionIdentifier = obj_
            obj_.original_tagname_ = 'accessionIdentifier'
        elif nodeName_ == 'receivedTime':
            obj_ = dateTime.factory()
            obj_.build(child_)
            self.receivedTime = obj_
            obj_.original_tagname_ = 'receivedTime'
        elif nodeName_ == 'collection':
            obj_ = Specimen_Collection.factory()
            obj_.build(child_)
            self.collection = obj_
            obj_.original_tagname_ = 'collection'
        elif nodeName_ == 'treatment':
            obj_ = Specimen_Treatment.factory()
            obj_.build(child_)
            self.treatment.append(obj_)
            obj_.original_tagname_ = 'treatment'
        elif nodeName_ == 'container':
            obj_ = Specimen_Container.factory()
            obj_.build(child_)
            self.container.append(obj_)
            obj_.original_tagname_ = 'container'
        super(Specimen, self).buildChildren(child_, node, nodeName_, True)
# end class Specimen


class Specimen_Source(BackboneElement):
    """Sample for analysis."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, relationship=None, target=None):
        self.original_tagname_ = None
        super(Specimen_Source, self).__init__(id, extension, modifierExtension, )
        self.relationship = relationship
        if target is None:
            self.target = []
        else:
            self.target = target
    def factory(*args_, **kwargs_):
        if Specimen_Source.subclass:
            return Specimen_Source.subclass(*args_, **kwargs_)
        else:
            return Specimen_Source(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_relationship(self): return self.relationship
    def set_relationship(self, relationship): self.relationship = relationship
    def get_target(self): return self.target
    def set_target(self, target): self.target = target
    def add_target(self, value): self.target.append(value)
    def insert_target(self, index, value): self.target[index] = value
    def hasContent_(self):
        if (
            self.relationship is not None or
            self.target or
            super(Specimen_Source, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Specimen.Source', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Specimen.Source')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Specimen.Source', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Specimen.Source'):
        super(Specimen_Source, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Specimen.Source')
    def exportChildren(self, outfile, level, namespace_='', name_='Specimen.Source', fromsubclass_=False, pretty_print=True):
        super(Specimen_Source, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.relationship is not None:
            self.relationship.export(outfile, level, namespace_, name_='relationship', pretty_print=pretty_print)
        for target_ in self.target:
            target_.export(outfile, level, namespace_, name_='target', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Specimen.Source', mapping_=None):
        element = super(Specimen_Source, self).to_etree(parent_element, name_, mapping_)
        if self.relationship is not None:
            relationship_ = self.relationship
            relationship_.to_etree(element, name_='relationship', mapping_=mapping_)
        for target_ in self.target:
            target_.to_etree(element, name_='target', mapping_=mapping_)
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
        super(Specimen_Source, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'relationship':
            obj_ = HierarchicalRelationshipType.factory()
            obj_.build(child_)
            self.relationship = obj_
            obj_.original_tagname_ = 'relationship'
        elif nodeName_ == 'target':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.target.append(obj_)
            obj_.original_tagname_ = 'target'
        super(Specimen_Source, self).buildChildren(child_, node, nodeName_, True)
# end class Specimen_Source


class Specimen_Collection(BackboneElement):
    """Sample for analysis.Time when specimen was collected from subject -
    the physiologically relevant time."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, collector=None, comment=None, collectedDateTime=None, collectedPeriod=None, quantity=None, method=None, sourceSite=None):
        self.original_tagname_ = None
        super(Specimen_Collection, self).__init__(id, extension, modifierExtension, )
        self.collector = collector
        if comment is None:
            self.comment = []
        else:
            self.comment = comment
        self.collectedDateTime = collectedDateTime
        self.collectedPeriod = collectedPeriod
        self.quantity = quantity
        self.method = method
        self.sourceSite = sourceSite
    def factory(*args_, **kwargs_):
        if Specimen_Collection.subclass:
            return Specimen_Collection.subclass(*args_, **kwargs_)
        else:
            return Specimen_Collection(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_collector(self): return self.collector
    def set_collector(self, collector): self.collector = collector
    def get_comment(self): return self.comment
    def set_comment(self, comment): self.comment = comment
    def add_comment(self, value): self.comment.append(value)
    def insert_comment(self, index, value): self.comment[index] = value
    def get_collectedDateTime(self): return self.collectedDateTime
    def set_collectedDateTime(self, collectedDateTime): self.collectedDateTime = collectedDateTime
    def get_collectedPeriod(self): return self.collectedPeriod
    def set_collectedPeriod(self, collectedPeriod): self.collectedPeriod = collectedPeriod
    def get_quantity(self): return self.quantity
    def set_quantity(self, quantity): self.quantity = quantity
    def get_method(self): return self.method
    def set_method(self, method): self.method = method
    def get_sourceSite(self): return self.sourceSite
    def set_sourceSite(self, sourceSite): self.sourceSite = sourceSite
    def hasContent_(self):
        if (
            self.collector is not None or
            self.comment or
            self.collectedDateTime is not None or
            self.collectedPeriod is not None or
            self.quantity is not None or
            self.method is not None or
            self.sourceSite is not None or
            super(Specimen_Collection, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Specimen.Collection', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Specimen.Collection')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Specimen.Collection', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Specimen.Collection'):
        super(Specimen_Collection, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Specimen.Collection')
    def exportChildren(self, outfile, level, namespace_='', name_='Specimen.Collection', fromsubclass_=False, pretty_print=True):
        super(Specimen_Collection, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.collector is not None:
            self.collector.export(outfile, level, namespace_, name_='collector', pretty_print=pretty_print)
        for comment_ in self.comment:
            comment_.export(outfile, level, namespace_, name_='comment', pretty_print=pretty_print)
        if self.collectedDateTime is not None:
            self.collectedDateTime.export(outfile, level, namespace_, name_='collectedDateTime', pretty_print=pretty_print)
        if self.collectedPeriod is not None:
            self.collectedPeriod.export(outfile, level, namespace_, name_='collectedPeriod', pretty_print=pretty_print)
        if self.quantity is not None:
            self.quantity.export(outfile, level, namespace_, name_='quantity', pretty_print=pretty_print)
        if self.method is not None:
            self.method.export(outfile, level, namespace_, name_='method', pretty_print=pretty_print)
        if self.sourceSite is not None:
            self.sourceSite.export(outfile, level, namespace_, name_='sourceSite', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Specimen.Collection', mapping_=None):
        element = super(Specimen_Collection, self).to_etree(parent_element, name_, mapping_)
        if self.collector is not None:
            collector_ = self.collector
            collector_.to_etree(element, name_='collector', mapping_=mapping_)
        for comment_ in self.comment:
            comment_.to_etree(element, name_='comment', mapping_=mapping_)
        if self.collectedDateTime is not None:
            collectedDateTime_ = self.collectedDateTime
            collectedDateTime_.to_etree(element, name_='collectedDateTime', mapping_=mapping_)
        if self.collectedPeriod is not None:
            collectedPeriod_ = self.collectedPeriod
            collectedPeriod_.to_etree(element, name_='collectedPeriod', mapping_=mapping_)
        if self.quantity is not None:
            quantity_ = self.quantity
            quantity_.to_etree(element, name_='quantity', mapping_=mapping_)
        if self.method is not None:
            method_ = self.method
            method_.to_etree(element, name_='method', mapping_=mapping_)
        if self.sourceSite is not None:
            sourceSite_ = self.sourceSite
            sourceSite_.to_etree(element, name_='sourceSite', mapping_=mapping_)
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
        super(Specimen_Collection, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'collector':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.collector = obj_
            obj_.original_tagname_ = 'collector'
        elif nodeName_ == 'comment':
            obj_ = string.factory()
            obj_.build(child_)
            self.comment.append(obj_)
            obj_.original_tagname_ = 'comment'
        elif nodeName_ == 'collectedDateTime':
            obj_ = dateTime.factory()
            obj_.build(child_)
            self.collectedDateTime = obj_
            obj_.original_tagname_ = 'collectedDateTime'
        elif nodeName_ == 'collectedPeriod':
            obj_ = Period.factory()
            obj_.build(child_)
            self.collectedPeriod = obj_
            obj_.original_tagname_ = 'collectedPeriod'
        elif nodeName_ == 'quantity':
            obj_ = Quantity.factory()
            obj_.build(child_)
            self.quantity = obj_
            obj_.original_tagname_ = 'quantity'
        elif nodeName_ == 'method':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.method = obj_
            obj_.original_tagname_ = 'method'
        elif nodeName_ == 'sourceSite':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.sourceSite = obj_
            obj_.original_tagname_ = 'sourceSite'
        super(Specimen_Collection, self).buildChildren(child_, node, nodeName_, True)
# end class Specimen_Collection


class Specimen_Treatment(BackboneElement):
    """Sample for analysis."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, description=None, procedure=None, additive=None):
        self.original_tagname_ = None
        super(Specimen_Treatment, self).__init__(id, extension, modifierExtension, )
        self.description = description
        self.procedure = procedure
        if additive is None:
            self.additive = []
        else:
            self.additive = additive
    def factory(*args_, **kwargs_):
        if Specimen_Treatment.subclass:
            return Specimen_Treatment.subclass(*args_, **kwargs_)
        else:
            return Specimen_Treatment(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_description(self): return self.description
    def set_description(self, description): self.description = description
    def get_procedure(self): return self.procedure
    def set_procedure(self, procedure): self.procedure = procedure
    def get_additive(self): return self.additive
    def set_additive(self, additive): self.additive = additive
    def add_additive(self, value): self.additive.append(value)
    def insert_additive(self, index, value): self.additive[index] = value
    def hasContent_(self):
        if (
            self.description is not None or
            self.procedure is not None or
            self.additive or
            super(Specimen_Treatment, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Specimen.Treatment', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Specimen.Treatment')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Specimen.Treatment', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Specimen.Treatment'):
        super(Specimen_Treatment, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Specimen.Treatment')
    def exportChildren(self, outfile, level, namespace_='', name_='Specimen.Treatment', fromsubclass_=False, pretty_print=True):
        super(Specimen_Treatment, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.description is not None:
            self.description.export(outfile, level, namespace_, name_='description', pretty_print=pretty_print)
        if self.procedure is not None:
            self.procedure.export(outfile, level, namespace_, name_='procedure', pretty_print=pretty_print)
        for additive_ in self.additive:
            additive_.export(outfile, level, namespace_, name_='additive', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Specimen.Treatment', mapping_=None):
        element = super(Specimen_Treatment, self).to_etree(parent_element, name_, mapping_)
        if self.description is not None:
            description_ = self.description
            description_.to_etree(element, name_='description', mapping_=mapping_)
        if self.procedure is not None:
            procedure_ = self.procedure
            procedure_.to_etree(element, name_='procedure', mapping_=mapping_)
        for additive_ in self.additive:
            additive_.to_etree(element, name_='additive', mapping_=mapping_)
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
        super(Specimen_Treatment, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'description':
            obj_ = string.factory()
            obj_.build(child_)
            self.description = obj_
            obj_.original_tagname_ = 'description'
        elif nodeName_ == 'procedure':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.procedure = obj_
            obj_.original_tagname_ = 'procedure'
        elif nodeName_ == 'additive':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.additive.append(obj_)
            obj_.original_tagname_ = 'additive'
        super(Specimen_Treatment, self).buildChildren(child_, node, nodeName_, True)
# end class Specimen_Treatment


class Specimen_Container(BackboneElement):
    """Sample for analysis."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, identifier=None, description=None, type_=None, capacity=None, specimenQuantity=None, additive=None):
        self.original_tagname_ = None
        super(Specimen_Container, self).__init__(id, extension, modifierExtension, )
        if identifier is None:
            self.identifier = []
        else:
            self.identifier = identifier
        self.description = description
        self.type_ = type_
        self.capacity = capacity
        self.specimenQuantity = specimenQuantity
        self.additive = additive
    def factory(*args_, **kwargs_):
        if Specimen_Container.subclass:
            return Specimen_Container.subclass(*args_, **kwargs_)
        else:
            return Specimen_Container(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_identifier(self): return self.identifier
    def set_identifier(self, identifier): self.identifier = identifier
    def add_identifier(self, value): self.identifier.append(value)
    def insert_identifier(self, index, value): self.identifier[index] = value
    def get_description(self): return self.description
    def set_description(self, description): self.description = description
    def get_type(self): return self.type_
    def set_type(self, type_): self.type_ = type_
    def get_capacity(self): return self.capacity
    def set_capacity(self, capacity): self.capacity = capacity
    def get_specimenQuantity(self): return self.specimenQuantity
    def set_specimenQuantity(self, specimenQuantity): self.specimenQuantity = specimenQuantity
    def get_additive(self): return self.additive
    def set_additive(self, additive): self.additive = additive
    def hasContent_(self):
        if (
            self.identifier or
            self.description is not None or
            self.type_ is not None or
            self.capacity is not None or
            self.specimenQuantity is not None or
            self.additive is not None or
            super(Specimen_Container, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Specimen.Container', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Specimen.Container')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Specimen.Container', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Specimen.Container'):
        super(Specimen_Container, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Specimen.Container')
    def exportChildren(self, outfile, level, namespace_='', name_='Specimen.Container', fromsubclass_=False, pretty_print=True):
        super(Specimen_Container, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for identifier_ in self.identifier:
            identifier_.export(outfile, level, namespace_, name_='identifier', pretty_print=pretty_print)
        if self.description is not None:
            self.description.export(outfile, level, namespace_, name_='description', pretty_print=pretty_print)
        if self.type_ is not None:
            self.type_.export(outfile, level, namespace_, name_='type', pretty_print=pretty_print)
        if self.capacity is not None:
            self.capacity.export(outfile, level, namespace_, name_='capacity', pretty_print=pretty_print)
        if self.specimenQuantity is not None:
            self.specimenQuantity.export(outfile, level, namespace_, name_='specimenQuantity', pretty_print=pretty_print)
        if self.additive is not None:
            self.additive.export(outfile, level, namespace_, name_='additive', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Specimen.Container', mapping_=None):
        element = super(Specimen_Container, self).to_etree(parent_element, name_, mapping_)
        for identifier_ in self.identifier:
            identifier_.to_etree(element, name_='identifier', mapping_=mapping_)
        if self.description is not None:
            description_ = self.description
            description_.to_etree(element, name_='description', mapping_=mapping_)
        if self.type_ is not None:
            type__ = self.type_
            type__.to_etree(element, name_='type', mapping_=mapping_)
        if self.capacity is not None:
            capacity_ = self.capacity
            capacity_.to_etree(element, name_='capacity', mapping_=mapping_)
        if self.specimenQuantity is not None:
            specimenQuantity_ = self.specimenQuantity
            specimenQuantity_.to_etree(element, name_='specimenQuantity', mapping_=mapping_)
        if self.additive is not None:
            additive_ = self.additive
            additive_.to_etree(element, name_='additive', mapping_=mapping_)
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
        super(Specimen_Container, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'identifier':
            obj_ = Identifier.factory()
            obj_.build(child_)
            self.identifier.append(obj_)
            obj_.original_tagname_ = 'identifier'
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
        elif nodeName_ == 'capacity':
            obj_ = Quantity.factory()
            obj_.build(child_)
            self.capacity = obj_
            obj_.original_tagname_ = 'capacity'
        elif nodeName_ == 'specimenQuantity':
            obj_ = Quantity.factory()
            obj_.build(child_)
            self.specimenQuantity = obj_
            obj_.original_tagname_ = 'specimenQuantity'
        elif nodeName_ == 'additive':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.additive = obj_
            obj_.original_tagname_ = 'additive'
        super(Specimen_Container, self).buildChildren(child_, node, nodeName_, True)
# end class Specimen_Container
