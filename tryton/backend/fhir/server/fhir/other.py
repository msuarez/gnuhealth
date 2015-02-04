from .base_classes import *
from .support_functions import *


class Other(Resource):
    """Other is a conformant for handling resource concepts not yet defined
    for FHIR or outside HL7's scope of interest.If the element is
    present, it must have either a @value, an @id, or extensions"""
    subclass = None
    superclass = Resource
    def __init__(self, id=None, extension=None, modifierExtension=None, language=None, text=None, contained=None, identifier=None, code=None, subject=None, author=None, created=None):
        self.original_tagname_ = None
        super(Other, self).__init__(id, extension, modifierExtension, language, text, contained, )
        if identifier is None:
            self.identifier = []
        else:
            self.identifier = identifier
        self.code = code
        self.subject = subject
        self.author = author
        self.created = created
    def factory(*args_, **kwargs_):
        if Other.subclass:
            return Other.subclass(*args_, **kwargs_)
        else:
            return Other(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_identifier(self): return self.identifier
    def set_identifier(self, identifier): self.identifier = identifier
    def add_identifier(self, value): self.identifier.append(value)
    def insert_identifier(self, index, value): self.identifier[index] = value
    def get_code(self): return self.code
    def set_code(self, code): self.code = code
    def get_subject(self): return self.subject
    def set_subject(self, subject): self.subject = subject
    def get_author(self): return self.author
    def set_author(self, author): self.author = author
    def get_created(self): return self.created
    def set_created(self, created): self.created = created
    def hasContent_(self):
        if (
            self.identifier or
            self.code is not None or
            self.subject is not None or
            self.author is not None or
            self.created is not None or
            super(Other, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Other', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Other')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Other', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Other'):
        super(Other, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Other')
    def exportChildren(self, outfile, level, namespace_='', name_='Other', fromsubclass_=False, pretty_print=True):
        super(Other, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for identifier_ in self.identifier:
            identifier_.export(outfile, level, namespace_, name_='identifier', pretty_print=pretty_print)
        if self.code is not None:
            self.code.export(outfile, level, namespace_, name_='code', pretty_print=pretty_print)
        if self.subject is not None:
            self.subject.export(outfile, level, namespace_, name_='subject', pretty_print=pretty_print)
        if self.author is not None:
            self.author.export(outfile, level, namespace_, name_='author', pretty_print=pretty_print)
        if self.created is not None:
            self.created.export(outfile, level, namespace_, name_='created', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Other', mapping_=None):
        element = super(Other, self).to_etree(parent_element, name_, mapping_)
        for identifier_ in self.identifier:
            identifier_.to_etree(element, name_='identifier', mapping_=mapping_)
        if self.code is not None:
            code_ = self.code
            code_.to_etree(element, name_='code', mapping_=mapping_)
        if self.subject is not None:
            subject_ = self.subject
            subject_.to_etree(element, name_='subject', mapping_=mapping_)
        if self.author is not None:
            author_ = self.author
            author_.to_etree(element, name_='author', mapping_=mapping_)
        if self.created is not None:
            created_ = self.created
            created_.to_etree(element, name_='created', mapping_=mapping_)
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
        super(Other, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'identifier':
            obj_ = Identifier.factory()
            obj_.build(child_)
            self.identifier.append(obj_)
            obj_.original_tagname_ = 'identifier'
        elif nodeName_ == 'code':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.code = obj_
            obj_.original_tagname_ = 'code'
        elif nodeName_ == 'subject':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.subject = obj_
            obj_.original_tagname_ = 'subject'
        elif nodeName_ == 'author':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.author = obj_
            obj_.original_tagname_ = 'author'
        elif nodeName_ == 'created':
            obj_ = date.factory()
            obj_.build(child_)
            self.created = obj_
            obj_.original_tagname_ = 'created'
        super(Other, self).buildChildren(child_, node, nodeName_, True)
# end class Other
