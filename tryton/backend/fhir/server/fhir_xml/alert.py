from .base_classes import *
from .support_functions import *


class Alert(Resource):
    """Prospective warnings of potential issues when providing care to the
    patient.If the element is present, it must have either a @value,
    an @id, or extensions"""
    subclass = None
    superclass = Resource
    def __init__(self, id=None, extension=None, modifierExtension=None, language=None, text=None, contained=None, identifier=None, category=None, status=None, subject=None, author=None, note=None):
        self.original_tagname_ = None
        super(Alert, self).__init__(id, extension, modifierExtension, language, text, contained, )
        if identifier is None:
            self.identifier = []
        else:
            self.identifier = identifier
        self.category = category
        self.status = status
        self.subject = subject
        self.author = author
        self.note = note
    def factory(*args_, **kwargs_):
        if Alert.subclass:
            return Alert.subclass(*args_, **kwargs_)
        else:
            return Alert(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_identifier(self): return self.identifier
    def set_identifier(self, identifier): self.identifier = identifier
    def add_identifier(self, value): self.identifier.append(value)
    def insert_identifier(self, index, value): self.identifier[index] = value
    def get_category(self): return self.category
    def set_category(self, category): self.category = category
    def get_status(self): return self.status
    def set_status(self, status): self.status = status
    def get_subject(self): return self.subject
    def set_subject(self, subject): self.subject = subject
    def get_author(self): return self.author
    def set_author(self, author): self.author = author
    def get_note(self): return self.note
    def set_note(self, note): self.note = note
    def hasContent_(self):
        if (
            self.identifier or
            self.category is not None or
            self.status is not None or
            self.subject is not None or
            self.author is not None or
            self.note is not None or
            super(Alert, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Alert', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Alert')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Alert', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Alert'):
        super(Alert, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Alert')
    def exportChildren(self, outfile, level, namespace_='', name_='Alert', fromsubclass_=False, pretty_print=True):
        super(Alert, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for identifier_ in self.identifier:
            identifier_.export(outfile, level, namespace_, name_='identifier', pretty_print=pretty_print)
        if self.category is not None:
            self.category.export(outfile, level, namespace_, name_='category', pretty_print=pretty_print)
        if self.status is not None:
            self.status.export(outfile, level, namespace_, name_='status', pretty_print=pretty_print)
        if self.subject is not None:
            self.subject.export(outfile, level, namespace_, name_='subject', pretty_print=pretty_print)
        if self.author is not None:
            self.author.export(outfile, level, namespace_, name_='author', pretty_print=pretty_print)
        if self.note is not None:
            self.note.export(outfile, level, namespace_, name_='note', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Alert', mapping_=None):
        element = super(Alert, self).to_etree(parent_element, name_, mapping_)
        for identifier_ in self.identifier:
            identifier_.to_etree(element, name_='identifier', mapping_=mapping_)
        if self.category is not None:
            category_ = self.category
            category_.to_etree(element, name_='category', mapping_=mapping_)
        if self.status is not None:
            status_ = self.status
            status_.to_etree(element, name_='status', mapping_=mapping_)
        if self.subject is not None:
            subject_ = self.subject
            subject_.to_etree(element, name_='subject', mapping_=mapping_)
        if self.author is not None:
            author_ = self.author
            author_.to_etree(element, name_='author', mapping_=mapping_)
        if self.note is not None:
            note_ = self.note
            note_.to_etree(element, name_='note', mapping_=mapping_)
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
        super(Alert, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'identifier':
            obj_ = Identifier.factory()
            obj_.build(child_)
            self.identifier.append(obj_)
            obj_.original_tagname_ = 'identifier'
        elif nodeName_ == 'category':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.category = obj_
            obj_.original_tagname_ = 'category'
        elif nodeName_ == 'status':
            obj_ = AlertStatus.factory()
            obj_.build(child_)
            self.status = obj_
            obj_.original_tagname_ = 'status'
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
        elif nodeName_ == 'note':
            obj_ = string.factory()
            obj_.build(child_)
            self.note = obj_
            obj_.original_tagname_ = 'note'
        super(Alert, self).buildChildren(child_, node, nodeName_, True)
# end class Alert


class AlertStatus(Element):
    """Indicates whether this alert is active and needs to be displayed to
    a user, or whether it is no longer needed or entered in errorIf
    the element is present, it must have either a @value, an @id, or
    extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(AlertStatus, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if AlertStatus.subclass:
            return AlertStatus.subclass(*args_, **kwargs_)
        else:
            return AlertStatus(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(AlertStatus, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='AlertStatus', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='AlertStatus')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='AlertStatus', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='AlertStatus'):
        super(AlertStatus, self).exportAttributes(outfile, level, already_processed, namespace_, name_='AlertStatus')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='AlertStatus', fromsubclass_=False, pretty_print=True):
        super(AlertStatus, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='AlertStatus', mapping_=None):
        element = super(AlertStatus, self).to_etree(parent_element, name_, mapping_)
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
        super(AlertStatus, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(AlertStatus, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class AlertStatus
