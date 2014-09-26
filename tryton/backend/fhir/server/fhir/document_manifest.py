from .base_classes import *
from .support_functions import *


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
