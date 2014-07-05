from .base_classes import *
from .support_functions import *


class Narrative(Element):
    """A human-readable formatted text, including images.If the element is
    present, it must have a value for at least one of the defined
    elements, an @id referenced from the Narrative, or extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, status=None, div=None):
        self.original_tagname_ = None
        super(Narrative, self).__init__(id, extension, )
        self.status = status
        self.div = div
    def factory(*args_, **kwargs_):
        if Narrative.subclass:
            return Narrative.subclass(*args_, **kwargs_)
        else:
            return Narrative(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_status(self): return self.status
    def set_status(self, status): self.status = status
    def get_div(self): return self.div
    def set_div(self, div): self.div = div
    def hasContent_(self):
        if (
            self.status is not None or
            self.div is not None or
            super(Narrative, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Narrative', namespacedef_=' xmlns:xhtml="http://www.w3.org/1999/xhtml" ', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Narrative')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Narrative', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Narrative'):
        super(Narrative, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Narrative')
    def exportChildren(self, outfile, level, namespace_='', name_='Narrative', fromsubclass_=False, pretty_print=True):
        super(Narrative, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.status is not None:
            self.status.export(outfile, level, namespace_, name_='status', pretty_print=pretty_print)
        if self.div is not None:
            self.div.export(outfile, level, namespace_='xhtml:', name_='div', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Narrative', mapping_=None):
        element = super(Narrative, self).to_etree(parent_element, name_, mapping_)
        if self.status is not None:
            status_ = self.status
            status_.to_etree(element, name_='status', mapping_=mapping_)
        if self.div is not None:
            div_ = self.div
            div_.to_etree(element, name_='div', mapping_=mapping_)
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
        super(Narrative, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'status':
            obj_ = NarrativeStatus.factory()
            obj_.build(child_)
            self.status = obj_
            obj_.original_tagname_ = 'status'
        elif nodeName_ == 'div':
            obj_ = div.factory()
            obj_.build(child_)
            self.div = obj_
            obj_.original_tagname_ = 'div'
        super(Narrative, self).buildChildren(child_, node, nodeName_, True)
# end class Narrative


class NarrativeStatus(Element):
    """The status of a resource narrativeIf the element is present, it must
    have either a @value, an @id, or extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(NarrativeStatus, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if NarrativeStatus.subclass:
            return NarrativeStatus.subclass(*args_, **kwargs_)
        else:
            return NarrativeStatus(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(NarrativeStatus, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='NarrativeStatus', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='NarrativeStatus')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='NarrativeStatus', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='NarrativeStatus'):
        super(NarrativeStatus, self).exportAttributes(outfile, level, already_processed, namespace_, name_='NarrativeStatus')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='NarrativeStatus', fromsubclass_=False, pretty_print=True):
        super(NarrativeStatus, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='NarrativeStatus', mapping_=None):
        element = super(NarrativeStatus, self).to_etree(parent_element, name_, mapping_)
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
        super(NarrativeStatus, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(NarrativeStatus, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class NarrativeStatus
