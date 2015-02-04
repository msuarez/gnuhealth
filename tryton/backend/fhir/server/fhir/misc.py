from .base_classes import *
from .support_functions import *


class MessageSignificanceCategory(Element):
    """The impact of the content of a messageIf the element is present, it
    must have either a @value, an @id, or extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(MessageSignificanceCategory, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if MessageSignificanceCategory.subclass:
            return MessageSignificanceCategory.subclass(*args_, **kwargs_)
        else:
            return MessageSignificanceCategory(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(MessageSignificanceCategory, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='MessageSignificanceCategory', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='MessageSignificanceCategory')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='MessageSignificanceCategory', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='MessageSignificanceCategory'):
        super(MessageSignificanceCategory, self).exportAttributes(outfile, level, already_processed, namespace_, name_='MessageSignificanceCategory')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='MessageSignificanceCategory', fromsubclass_=False, pretty_print=True):
        super(MessageSignificanceCategory, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='MessageSignificanceCategory', mapping_=None):
        element = super(MessageSignificanceCategory, self).to_etree(parent_element, name_, mapping_)
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
        super(MessageSignificanceCategory, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(MessageSignificanceCategory, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class MessageSignificanceCategory


class DocumentManifest(Resource):
    """A manifest that defines a set of documents.If the element is
    present, it must have either a @value, an @id, or extensions"""
    subclass = None
    superclass = Resource
    def __init__(self, id=None, extension=None, modifierExtension=None, language=None, text=None, contained=None, masterIdentifier=None, identifier=None, subject=None, recipient=None, type_=None, author=None, created=None, source=None, status=None, supercedes=None, description=None, confidentiality=None, content=None):
        self.original_tagname_ = None
        super(DocumentManifest, self).__init__(id, extension, modifierExtension, language, text, contained, )
        self.masterIdentifier = masterIdentifier
        if identifier is None:
            self.identifier = []
        else:
            self.identifier = identifier
        if subject is None:
            self.subject = []
        else:
            self.subject = subject
        if recipient is None:
            self.recipient = []
        else:
            self.recipient = recipient
        self.type_ = type_
        if author is None:
            self.author = []
        else:
            self.author = author
        self.created = created
        self.source = source
        self.status = status
        self.supercedes = supercedes
        self.description = description
        self.confidentiality = confidentiality
        if content is None:
            self.content = []
        else:
            self.content = content
    def factory(*args_, **kwargs_):
        if DocumentManifest.subclass:
            return DocumentManifest.subclass(*args_, **kwargs_)
        else:
            return DocumentManifest(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_masterIdentifier(self): return self.masterIdentifier
    def set_masterIdentifier(self, masterIdentifier): self.masterIdentifier = masterIdentifier
    def get_identifier(self): return self.identifier
    def set_identifier(self, identifier): self.identifier = identifier
    def add_identifier(self, value): self.identifier.append(value)
    def insert_identifier(self, index, value): self.identifier[index] = value
    def get_subject(self): return self.subject
    def set_subject(self, subject): self.subject = subject
    def add_subject(self, value): self.subject.append(value)
    def insert_subject(self, index, value): self.subject[index] = value
    def get_recipient(self): return self.recipient
    def set_recipient(self, recipient): self.recipient = recipient
    def add_recipient(self, value): self.recipient.append(value)
    def insert_recipient(self, index, value): self.recipient[index] = value
    def get_type(self): return self.type_
    def set_type(self, type_): self.type_ = type_
    def get_author(self): return self.author
    def set_author(self, author): self.author = author
    def add_author(self, value): self.author.append(value)
    def insert_author(self, index, value): self.author[index] = value
    def get_created(self): return self.created
    def set_created(self, created): self.created = created
    def get_source(self): return self.source
    def set_source(self, source): self.source = source
    def get_status(self): return self.status
    def set_status(self, status): self.status = status
    def get_supercedes(self): return self.supercedes
    def set_supercedes(self, supercedes): self.supercedes = supercedes
    def get_description(self): return self.description
    def set_description(self, description): self.description = description
    def get_confidentiality(self): return self.confidentiality
    def set_confidentiality(self, confidentiality): self.confidentiality = confidentiality
    def get_content(self): return self.content
    def set_content(self, content): self.content = content
    def add_content(self, value): self.content.append(value)
    def insert_content(self, index, value): self.content[index] = value
    def hasContent_(self):
        if (
            self.masterIdentifier is not None or
            self.identifier or
            self.subject or
            self.recipient or
            self.type_ is not None or
            self.author or
            self.created is not None or
            self.source is not None or
            self.status is not None or
            self.supercedes is not None or
            self.description is not None or
            self.confidentiality is not None or
            self.content or
            super(DocumentManifest, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='DocumentManifest', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='DocumentManifest')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='DocumentManifest', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='DocumentManifest'):
        super(DocumentManifest, self).exportAttributes(outfile, level, already_processed, namespace_, name_='DocumentManifest')
    def exportChildren(self, outfile, level, namespace_='', name_='DocumentManifest', fromsubclass_=False, pretty_print=True):
        super(DocumentManifest, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.masterIdentifier is not None:
            self.masterIdentifier.export(outfile, level, namespace_, name_='masterIdentifier', pretty_print=pretty_print)
        for identifier_ in self.identifier:
            identifier_.export(outfile, level, namespace_, name_='identifier', pretty_print=pretty_print)
        for subject_ in self.subject:
            subject_.export(outfile, level, namespace_, name_='subject', pretty_print=pretty_print)
        for recipient_ in self.recipient:
            recipient_.export(outfile, level, namespace_, name_='recipient', pretty_print=pretty_print)
        if self.type_ is not None:
            self.type_.export(outfile, level, namespace_, name_='type', pretty_print=pretty_print)
        for author_ in self.author:
            author_.export(outfile, level, namespace_, name_='author', pretty_print=pretty_print)
        if self.created is not None:
            self.created.export(outfile, level, namespace_, name_='created', pretty_print=pretty_print)
        if self.source is not None:
            self.source.export(outfile, level, namespace_, name_='source', pretty_print=pretty_print)
        if self.status is not None:
            self.status.export(outfile, level, namespace_, name_='status', pretty_print=pretty_print)
        if self.supercedes is not None:
            self.supercedes.export(outfile, level, namespace_, name_='supercedes', pretty_print=pretty_print)
        if self.description is not None:
            self.description.export(outfile, level, namespace_, name_='description', pretty_print=pretty_print)
        if self.confidentiality is not None:
            self.confidentiality.export(outfile, level, namespace_, name_='confidentiality', pretty_print=pretty_print)
        for content_ in self.content:
            content_.export(outfile, level, namespace_, name_='content', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='DocumentManifest', mapping_=None):
        element = super(DocumentManifest, self).to_etree(parent_element, name_, mapping_)
        if self.masterIdentifier is not None:
            masterIdentifier_ = self.masterIdentifier
            masterIdentifier_.to_etree(element, name_='masterIdentifier', mapping_=mapping_)
        for identifier_ in self.identifier:
            identifier_.to_etree(element, name_='identifier', mapping_=mapping_)
        for subject_ in self.subject:
            subject_.to_etree(element, name_='subject', mapping_=mapping_)
        for recipient_ in self.recipient:
            recipient_.to_etree(element, name_='recipient', mapping_=mapping_)
        if self.type_ is not None:
            type__ = self.type_
            type__.to_etree(element, name_='type', mapping_=mapping_)
        for author_ in self.author:
            author_.to_etree(element, name_='author', mapping_=mapping_)
        if self.created is not None:
            created_ = self.created
            created_.to_etree(element, name_='created', mapping_=mapping_)
        if self.source is not None:
            source_ = self.source
            source_.to_etree(element, name_='source', mapping_=mapping_)
        if self.status is not None:
            status_ = self.status
            status_.to_etree(element, name_='status', mapping_=mapping_)
        if self.supercedes is not None:
            supercedes_ = self.supercedes
            supercedes_.to_etree(element, name_='supercedes', mapping_=mapping_)
        if self.description is not None:
            description_ = self.description
            description_.to_etree(element, name_='description', mapping_=mapping_)
        if self.confidentiality is not None:
            confidentiality_ = self.confidentiality
            confidentiality_.to_etree(element, name_='confidentiality', mapping_=mapping_)
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
        super(DocumentManifest, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'masterIdentifier':
            obj_ = Identifier.factory()
            obj_.build(child_)
            self.masterIdentifier = obj_
            obj_.original_tagname_ = 'masterIdentifier'
        elif nodeName_ == 'identifier':
            obj_ = Identifier.factory()
            obj_.build(child_)
            self.identifier.append(obj_)
            obj_.original_tagname_ = 'identifier'
        elif nodeName_ == 'subject':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.subject.append(obj_)
            obj_.original_tagname_ = 'subject'
        elif nodeName_ == 'recipient':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.recipient.append(obj_)
            obj_.original_tagname_ = 'recipient'
        elif nodeName_ == 'type':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.type_ = obj_
            obj_.original_tagname_ = 'type'
        elif nodeName_ == 'author':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.author.append(obj_)
            obj_.original_tagname_ = 'author'
        elif nodeName_ == 'created':
            obj_ = dateTime.factory()
            obj_.build(child_)
            self.created = obj_
            obj_.original_tagname_ = 'created'
        elif nodeName_ == 'source':
            obj_ = uri.factory()
            obj_.build(child_)
            self.source = obj_
            obj_.original_tagname_ = 'source'
        elif nodeName_ == 'status':
            obj_ = DocumentReferenceStatus.factory()
            obj_.build(child_)
            self.status = obj_
            obj_.original_tagname_ = 'status'
        elif nodeName_ == 'supercedes':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.supercedes = obj_
            obj_.original_tagname_ = 'supercedes'
        elif nodeName_ == 'description':
            obj_ = string.factory()
            obj_.build(child_)
            self.description = obj_
            obj_.original_tagname_ = 'description'
        elif nodeName_ == 'confidentiality':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.confidentiality = obj_
            obj_.original_tagname_ = 'confidentiality'
        elif nodeName_ == 'content':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.content.append(obj_)
            obj_.original_tagname_ = 'content'
        super(DocumentManifest, self).buildChildren(child_, node, nodeName_, True)
# end class DocumentManifest


class DocumentRelationshipType(Element):
    """The type of relationship between documentsIf the element is present,
    it must have either a @value, an @id, or extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(DocumentRelationshipType, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if DocumentRelationshipType.subclass:
            return DocumentRelationshipType.subclass(*args_, **kwargs_)
        else:
            return DocumentRelationshipType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(DocumentRelationshipType, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='DocumentRelationshipType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='DocumentRelationshipType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='DocumentRelationshipType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='DocumentRelationshipType'):
        super(DocumentRelationshipType, self).exportAttributes(outfile, level, already_processed, namespace_, name_='DocumentRelationshipType')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='DocumentRelationshipType', fromsubclass_=False, pretty_print=True):
        super(DocumentRelationshipType, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='DocumentRelationshipType', mapping_=None):
        element = super(DocumentRelationshipType, self).to_etree(parent_element, name_, mapping_)
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
        super(DocumentRelationshipType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(DocumentRelationshipType, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class DocumentRelationshipType


class InstanceAvailability(Element):
    """Availability of the resourceIf the element is present, it must have
    either a @value, an @id, or extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(InstanceAvailability, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if InstanceAvailability.subclass:
            return InstanceAvailability.subclass(*args_, **kwargs_)
        else:
            return InstanceAvailability(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(InstanceAvailability, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='InstanceAvailability', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='InstanceAvailability')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='InstanceAvailability', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='InstanceAvailability'):
        super(InstanceAvailability, self).exportAttributes(outfile, level, already_processed, namespace_, name_='InstanceAvailability')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='InstanceAvailability', fromsubclass_=False, pretty_print=True):
        super(InstanceAvailability, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='InstanceAvailability', mapping_=None):
        element = super(InstanceAvailability, self).to_etree(parent_element, name_, mapping_)
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
        super(InstanceAvailability, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(InstanceAvailability, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class InstanceAvailability


class IssueSeverity(Element):
    """How the issue affects the success of the actionIf the element is
    present, it must have either a @value, an @id, or extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(IssueSeverity, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if IssueSeverity.subclass:
            return IssueSeverity.subclass(*args_, **kwargs_)
        else:
            return IssueSeverity(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(IssueSeverity, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='IssueSeverity', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='IssueSeverity')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='IssueSeverity', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='IssueSeverity'):
        super(IssueSeverity, self).exportAttributes(outfile, level, already_processed, namespace_, name_='IssueSeverity')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='IssueSeverity', fromsubclass_=False, pretty_print=True):
        super(IssueSeverity, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='IssueSeverity', mapping_=None):
        element = super(IssueSeverity, self).to_etree(parent_element, name_, mapping_)
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
        super(IssueSeverity, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(IssueSeverity, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class IssueSeverity


class BindingConformance(Element):
    """Binding conformance for applicationsIf the element is present, it
    must have either a @value, an @id, or extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(BindingConformance, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if BindingConformance.subclass:
            return BindingConformance.subclass(*args_, **kwargs_)
        else:
            return BindingConformance(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(BindingConformance, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='BindingConformance', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='BindingConformance')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='BindingConformance', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='BindingConformance'):
        super(BindingConformance, self).exportAttributes(outfile, level, already_processed, namespace_, name_='BindingConformance')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='BindingConformance', fromsubclass_=False, pretty_print=True):
        super(BindingConformance, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='BindingConformance', mapping_=None):
        element = super(BindingConformance, self).to_etree(parent_element, name_, mapping_)
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
        super(BindingConformance, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(BindingConformance, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class BindingConformance


class ConstraintSeverity(Element):
    """SHALL applications comply with this constraint?If the element is
    present, it must have either a @value, an @id, or extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(ConstraintSeverity, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if ConstraintSeverity.subclass:
            return ConstraintSeverity.subclass(*args_, **kwargs_)
        else:
            return ConstraintSeverity(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(ConstraintSeverity, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='ConstraintSeverity', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ConstraintSeverity')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='ConstraintSeverity', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='ConstraintSeverity'):
        super(ConstraintSeverity, self).exportAttributes(outfile, level, already_processed, namespace_, name_='ConstraintSeverity')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='ConstraintSeverity', fromsubclass_=False, pretty_print=True):
        super(ConstraintSeverity, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='ConstraintSeverity', mapping_=None):
        element = super(ConstraintSeverity, self).to_etree(parent_element, name_, mapping_)
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
        super(ConstraintSeverity, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(ConstraintSeverity, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class ConstraintSeverity


class PropertyRepresentation(Element):
    """How a property is represented on the wireIf the element is present,
    it must have either a @value, an @id, or extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(PropertyRepresentation, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if PropertyRepresentation.subclass:
            return PropertyRepresentation.subclass(*args_, **kwargs_)
        else:
            return PropertyRepresentation(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(PropertyRepresentation, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='PropertyRepresentation', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='PropertyRepresentation')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='PropertyRepresentation', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='PropertyRepresentation'):
        super(PropertyRepresentation, self).exportAttributes(outfile, level, already_processed, namespace_, name_='PropertyRepresentation')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='PropertyRepresentation', fromsubclass_=False, pretty_print=True):
        super(PropertyRepresentation, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='PropertyRepresentation', mapping_=None):
        element = super(PropertyRepresentation, self).to_etree(parent_element, name_, mapping_)
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
        super(PropertyRepresentation, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(PropertyRepresentation, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class PropertyRepresentation


class AggregationMode(Element):
    """How resource references can be aggregatedIf the element is present,
    it must have either a @value, an @id, or extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(AggregationMode, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if AggregationMode.subclass:
            return AggregationMode.subclass(*args_, **kwargs_)
        else:
            return AggregationMode(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(AggregationMode, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='AggregationMode', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='AggregationMode')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='AggregationMode', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='AggregationMode'):
        super(AggregationMode, self).exportAttributes(outfile, level, already_processed, namespace_, name_='AggregationMode')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='AggregationMode', fromsubclass_=False, pretty_print=True):
        super(AggregationMode, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='AggregationMode', mapping_=None):
        element = super(AggregationMode, self).to_etree(parent_element, name_, mapping_)
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
        super(AggregationMode, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(AggregationMode, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class AggregationMode


class ExtensionContext(Element):
    """How an extension context is interpretedIf the element is present, it
    must have either a @value, an @id, or extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(ExtensionContext, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if ExtensionContext.subclass:
            return ExtensionContext.subclass(*args_, **kwargs_)
        else:
            return ExtensionContext(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(ExtensionContext, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='ExtensionContext', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ExtensionContext')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='ExtensionContext', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='ExtensionContext'):
        super(ExtensionContext, self).exportAttributes(outfile, level, already_processed, namespace_, name_='ExtensionContext')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='ExtensionContext', fromsubclass_=False, pretty_print=True):
        super(ExtensionContext, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='ExtensionContext', mapping_=None):
        element = super(ExtensionContext, self).to_etree(parent_element, name_, mapping_)
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
        super(ExtensionContext, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(ExtensionContext, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class ExtensionContext


class SlicingRules(Element):
    """How slices are interpreted when evaluating an instanceIf the element
    is present, it must have either a @value, an @id, or extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(SlicingRules, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if SlicingRules.subclass:
            return SlicingRules.subclass(*args_, **kwargs_)
        else:
            return SlicingRules(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(SlicingRules, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='SlicingRules', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='SlicingRules')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='SlicingRules', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='SlicingRules'):
        super(SlicingRules, self).exportAttributes(outfile, level, already_processed, namespace_, name_='SlicingRules')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='SlicingRules', fromsubclass_=False, pretty_print=True):
        super(SlicingRules, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='SlicingRules', mapping_=None):
        element = super(SlicingRules, self).to_etree(parent_element, name_, mapping_)
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
        super(SlicingRules, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(SlicingRules, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class SlicingRules


class HierarchicalRelationshipType(Element):
    """Type indicating if this is a parent or child relationshipIf the
    element is present, it must have either a @value, an @id, or
    extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(HierarchicalRelationshipType, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if HierarchicalRelationshipType.subclass:
            return HierarchicalRelationshipType.subclass(*args_, **kwargs_)
        else:
            return HierarchicalRelationshipType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(HierarchicalRelationshipType, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='HierarchicalRelationshipType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='HierarchicalRelationshipType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='HierarchicalRelationshipType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='HierarchicalRelationshipType'):
        super(HierarchicalRelationshipType, self).exportAttributes(outfile, level, already_processed, namespace_, name_='HierarchicalRelationshipType')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='HierarchicalRelationshipType', fromsubclass_=False, pretty_print=True):
        super(HierarchicalRelationshipType, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='HierarchicalRelationshipType', mapping_=None):
        element = super(HierarchicalRelationshipType, self).to_etree(parent_element, name_, mapping_)
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
        super(HierarchicalRelationshipType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(HierarchicalRelationshipType, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class HierarchicalRelationshipType


class FilterOperator(Element):
    """The kind of operation to perform as a part of a property based
    filterIf the element is present, it must have either a @value,
    an @id, or extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(FilterOperator, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if FilterOperator.subclass:
            return FilterOperator.subclass(*args_, **kwargs_)
        else:
            return FilterOperator(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(FilterOperator, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='FilterOperator', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='FilterOperator')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='FilterOperator', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='FilterOperator'):
        super(FilterOperator, self).exportAttributes(outfile, level, already_processed, namespace_, name_='FilterOperator')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='FilterOperator', fromsubclass_=False, pretty_print=True):
        super(FilterOperator, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='FilterOperator', mapping_=None):
        element = super(FilterOperator, self).to_etree(parent_element, name_, mapping_)
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
        super(FilterOperator, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(FilterOperator, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class FilterOperator
