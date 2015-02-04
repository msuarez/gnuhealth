from .base_classes import *
from .support_functions import *


class List(Resource):
    """A set of information summarized from a list of other resources.If
    the element is present, it must have either a @value, an @id, or
    extensions"""
    subclass = None
    superclass = Resource
    def __init__(self, id=None, extension=None, modifierExtension=None, language=None, text=None, contained=None, identifier=None, code=None, subject=None, source=None, date=None, ordered=None, mode=None, entry=None, emptyReason=None):
        self.original_tagname_ = None
        super(List, self).__init__(id, extension, modifierExtension, language, text, contained, )
        if identifier is None:
            self.identifier = []
        else:
            self.identifier = identifier
        self.code = code
        self.subject = subject
        self.source = source
        self.date = date
        self.ordered = ordered
        self.mode = mode
        if entry is None:
            self.entry = []
        else:
            self.entry = entry
        self.emptyReason = emptyReason
    def factory(*args_, **kwargs_):
        if List.subclass:
            return List.subclass(*args_, **kwargs_)
        else:
            return List(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_identifier(self): return self.identifier
    def set_identifier(self, identifier): self.identifier = identifier
    def add_identifier(self, value): self.identifier.append(value)
    def insert_identifier(self, index, value): self.identifier[index] = value
    def get_code(self): return self.code
    def set_code(self, code): self.code = code
    def get_subject(self): return self.subject
    def set_subject(self, subject): self.subject = subject
    def get_source(self): return self.source
    def set_source(self, source): self.source = source
    def get_date(self): return self.date
    def set_date(self, date): self.date = date
    def get_ordered(self): return self.ordered
    def set_ordered(self, ordered): self.ordered = ordered
    def get_mode(self): return self.mode
    def set_mode(self, mode): self.mode = mode
    def get_entry(self): return self.entry
    def set_entry(self, entry): self.entry = entry
    def add_entry(self, value): self.entry.append(value)
    def insert_entry(self, index, value): self.entry[index] = value
    def get_emptyReason(self): return self.emptyReason
    def set_emptyReason(self, emptyReason): self.emptyReason = emptyReason
    def hasContent_(self):
        if (
            self.identifier or
            self.code is not None or
            self.subject is not None or
            self.source is not None or
            self.date is not None or
            self.ordered is not None or
            self.mode is not None or
            self.entry or
            self.emptyReason is not None or
            super(List, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='List', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='List')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='List', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='List'):
        super(List, self).exportAttributes(outfile, level, already_processed, namespace_, name_='List')
    def exportChildren(self, outfile, level, namespace_='', name_='List', fromsubclass_=False, pretty_print=True):
        super(List, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
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
        if self.source is not None:
            self.source.export(outfile, level, namespace_, name_='source', pretty_print=pretty_print)
        if self.date is not None:
            self.date.export(outfile, level, namespace_, name_='date', pretty_print=pretty_print)
        if self.ordered is not None:
            self.ordered.export(outfile, level, namespace_, name_='ordered', pretty_print=pretty_print)
        if self.mode is not None:
            self.mode.export(outfile, level, namespace_, name_='mode', pretty_print=pretty_print)
        for entry_ in self.entry:
            entry_.export(outfile, level, namespace_, name_='entry', pretty_print=pretty_print)
        if self.emptyReason is not None:
            self.emptyReason.export(outfile, level, namespace_, name_='emptyReason', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='List', mapping_=None):
        element = super(List, self).to_etree(parent_element, name_, mapping_)
        for identifier_ in self.identifier:
            identifier_.to_etree(element, name_='identifier', mapping_=mapping_)
        if self.code is not None:
            code_ = self.code
            code_.to_etree(element, name_='code', mapping_=mapping_)
        if self.subject is not None:
            subject_ = self.subject
            subject_.to_etree(element, name_='subject', mapping_=mapping_)
        if self.source is not None:
            source_ = self.source
            source_.to_etree(element, name_='source', mapping_=mapping_)
        if self.date is not None:
            date_ = self.date
            date_.to_etree(element, name_='date', mapping_=mapping_)
        if self.ordered is not None:
            ordered_ = self.ordered
            ordered_.to_etree(element, name_='ordered', mapping_=mapping_)
        if self.mode is not None:
            mode_ = self.mode
            mode_.to_etree(element, name_='mode', mapping_=mapping_)
        for entry_ in self.entry:
            entry_.to_etree(element, name_='entry', mapping_=mapping_)
        if self.emptyReason is not None:
            emptyReason_ = self.emptyReason
            emptyReason_.to_etree(element, name_='emptyReason', mapping_=mapping_)
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
        super(List, self).buildAttributes(node, attrs, already_processed)
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
        elif nodeName_ == 'source':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.source = obj_
            obj_.original_tagname_ = 'source'
        elif nodeName_ == 'date':
            obj_ = dateTime.factory()
            obj_.build(child_)
            self.date = obj_
            obj_.original_tagname_ = 'date'
        elif nodeName_ == 'ordered':
            obj_ = boolean.factory()
            obj_.build(child_)
            self.ordered = obj_
            obj_.original_tagname_ = 'ordered'
        elif nodeName_ == 'mode':
            obj_ = ListMode.factory()
            obj_.build(child_)
            self.mode = obj_
            obj_.original_tagname_ = 'mode'
        elif nodeName_ == 'entry':
            obj_ = List_Entry.factory()
            obj_.build(child_)
            self.entry.append(obj_)
            obj_.original_tagname_ = 'entry'
        elif nodeName_ == 'emptyReason':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.emptyReason = obj_
            obj_.original_tagname_ = 'emptyReason'
        super(List, self).buildChildren(child_, node, nodeName_, True)
# end class List


class List_Entry(BackboneElement):
    """A set of information summarized from a list of other resources."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, flag=None, deleted=None, date=None, item=None):
        self.original_tagname_ = None
        super(List_Entry, self).__init__(id, extension, modifierExtension, )
        if flag is None:
            self.flag = []
        else:
            self.flag = flag
        self.deleted = deleted
        self.date = date
        self.item = item
    def factory(*args_, **kwargs_):
        if List_Entry.subclass:
            return List_Entry.subclass(*args_, **kwargs_)
        else:
            return List_Entry(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_flag(self): return self.flag
    def set_flag(self, flag): self.flag = flag
    def add_flag(self, value): self.flag.append(value)
    def insert_flag(self, index, value): self.flag[index] = value
    def get_deleted(self): return self.deleted
    def set_deleted(self, deleted): self.deleted = deleted
    def get_date(self): return self.date
    def set_date(self, date): self.date = date
    def get_item(self): return self.item
    def set_item(self, item): self.item = item
    def hasContent_(self):
        if (
            self.flag or
            self.deleted is not None or
            self.date is not None or
            self.item is not None or
            super(List_Entry, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='List.Entry', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='List.Entry')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='List.Entry', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='List.Entry'):
        super(List_Entry, self).exportAttributes(outfile, level, already_processed, namespace_, name_='List.Entry')
    def exportChildren(self, outfile, level, namespace_='', name_='List.Entry', fromsubclass_=False, pretty_print=True):
        super(List_Entry, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for flag_ in self.flag:
            flag_.export(outfile, level, namespace_, name_='flag', pretty_print=pretty_print)
        if self.deleted is not None:
            self.deleted.export(outfile, level, namespace_, name_='deleted', pretty_print=pretty_print)
        if self.date is not None:
            self.date.export(outfile, level, namespace_, name_='date', pretty_print=pretty_print)
        if self.item is not None:
            self.item.export(outfile, level, namespace_, name_='item', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='List.Entry', mapping_=None):
        element = super(List_Entry, self).to_etree(parent_element, name_, mapping_)
        for flag_ in self.flag:
            flag_.to_etree(element, name_='flag', mapping_=mapping_)
        if self.deleted is not None:
            deleted_ = self.deleted
            deleted_.to_etree(element, name_='deleted', mapping_=mapping_)
        if self.date is not None:
            date_ = self.date
            date_.to_etree(element, name_='date', mapping_=mapping_)
        if self.item is not None:
            item_ = self.item
            item_.to_etree(element, name_='item', mapping_=mapping_)
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
        super(List_Entry, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'flag':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.flag.append(obj_)
            obj_.original_tagname_ = 'flag'
        elif nodeName_ == 'deleted':
            obj_ = boolean.factory()
            obj_.build(child_)
            self.deleted = obj_
            obj_.original_tagname_ = 'deleted'
        elif nodeName_ == 'date':
            obj_ = dateTime.factory()
            obj_.build(child_)
            self.date = obj_
            obj_.original_tagname_ = 'date'
        elif nodeName_ == 'item':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.item = obj_
            obj_.original_tagname_ = 'item'
        super(List_Entry, self).buildChildren(child_, node, nodeName_, True)
# end class List_Entry


class ListMode(Element):
    """The processing mode that applies to this listIf the element is
    present, it must have either a @value, an @id, or extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(ListMode, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if ListMode.subclass:
            return ListMode.subclass(*args_, **kwargs_)
        else:
            return ListMode(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(ListMode, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='ListMode', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ListMode')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='ListMode', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='ListMode'):
        super(ListMode, self).exportAttributes(outfile, level, already_processed, namespace_, name_='ListMode')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='ListMode', fromsubclass_=False, pretty_print=True):
        super(ListMode, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='ListMode', mapping_=None):
        element = super(ListMode, self).to_etree(parent_element, name_, mapping_)
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
        super(ListMode, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(ListMode, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class ListMode
