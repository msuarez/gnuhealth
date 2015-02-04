from .base_classes import *
from .support_functions import *


class Binary(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, contentType=None, id=None, valueOf_=None):
        self.original_tagname_ = None
        self.contentType = _cast(None, contentType)
        self.id = _cast(None, id)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if Binary.subclass:
            return Binary.subclass(*args_, **kwargs_)
        else:
            return Binary(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_contentType(self): return self.contentType
    def set_contentType(self, contentType): self.contentType = contentType
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Binary', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Binary')
        if self.hasContent_():
            outfile.write('>')
            outfile.write(str(self.valueOf_).encode(ExternalEncoding))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Binary', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Binary'):
        if self.contentType is not None and 'contentType' not in already_processed:
            already_processed.add('contentType')
            outfile.write(' contentType=%s' % (self.gds_format_string(quote_attrib(self.contentType).encode(ExternalEncoding), input_name='contentType'), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (quote_attrib(self.id), ))
    def exportChildren(self, outfile, level, namespace_='', name_='Binary', fromsubclass_=False, pretty_print=True):
        pass
    def to_etree(self, parent_element=None, name_='Binary', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://hl7.org/fhir}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://hl7.org/fhir}' + name_)
        if self.contentType is not None:
            element.set('contentType', self.gds_format_string(self.contentType))
        if self.id is not None:
            element.set('id', self.id)
        if mapping_ is not None:
            mapping_[self] = element
        return element
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('contentType', node)
        if value is not None and 'contentType' not in already_processed:
            already_processed.add('contentType')
            self.contentType = value
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class Binary
