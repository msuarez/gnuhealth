from .base_classes import *
from .support_functions import *


class Media(Resource):
    """A photo, video, or audio recording acquired or used in healthcare.
    The actual content may be inline or provided by direct
    reference.If the element is present, it must have either a
    @value, an @id, or extensions"""
    subclass = None
    superclass = Resource
    def __init__(self, id=None, extension=None, modifierExtension=None, language=None, text=None, contained=None, type_=None, subtype=None, identifier=None, dateTime=None, subject=None, operator=None, view=None, deviceName=None, height=None, width=None, frames=None, length=None, content=None):
        self.original_tagname_ = None
        super(Media, self).__init__(id, extension, modifierExtension, language, text, contained, )
        self.type_ = type_
        self.subtype = subtype
        if identifier is None:
            self.identifier = []
        else:
            self.identifier = identifier
        self.dateTime = dateTime
        self.subject = subject
        self.operator = operator
        self.view = view
        self.deviceName = deviceName
        self.height = height
        self.width = width
        self.frames = frames
        self.length = length
        self.content = content
    def factory(*args_, **kwargs_):
        if Media.subclass:
            return Media.subclass(*args_, **kwargs_)
        else:
            return Media(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_type(self): return self.type_
    def set_type(self, type_): self.type_ = type_
    def get_subtype(self): return self.subtype
    def set_subtype(self, subtype): self.subtype = subtype
    def get_identifier(self): return self.identifier
    def set_identifier(self, identifier): self.identifier = identifier
    def add_identifier(self, value): self.identifier.append(value)
    def insert_identifier(self, index, value): self.identifier[index] = value
    def get_dateTime(self): return self.dateTime
    def set_dateTime(self, dateTime): self.dateTime = dateTime
    def get_subject(self): return self.subject
    def set_subject(self, subject): self.subject = subject
    def get_operator(self): return self.operator
    def set_operator(self, operator): self.operator = operator
    def get_view(self): return self.view
    def set_view(self, view): self.view = view
    def get_deviceName(self): return self.deviceName
    def set_deviceName(self, deviceName): self.deviceName = deviceName
    def get_height(self): return self.height
    def set_height(self, height): self.height = height
    def get_width(self): return self.width
    def set_width(self, width): self.width = width
    def get_frames(self): return self.frames
    def set_frames(self, frames): self.frames = frames
    def get_length(self): return self.length
    def set_length(self, length): self.length = length
    def get_content(self): return self.content
    def set_content(self, content): self.content = content
    def hasContent_(self):
        if (
            self.type_ is not None or
            self.subtype is not None or
            self.identifier or
            self.dateTime is not None or
            self.subject is not None or
            self.operator is not None or
            self.view is not None or
            self.deviceName is not None or
            self.height is not None or
            self.width is not None or
            self.frames is not None or
            self.length is not None or
            self.content is not None or
            super(Media, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Media', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Media')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Media', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Media'):
        super(Media, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Media')
    def exportChildren(self, outfile, level, namespace_='', name_='Media', fromsubclass_=False, pretty_print=True):
        super(Media, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.type_ is not None:
            self.type_.export(outfile, level, namespace_, name_='type', pretty_print=pretty_print)
        if self.subtype is not None:
            self.subtype.export(outfile, level, namespace_, name_='subtype', pretty_print=pretty_print)
        for identifier_ in self.identifier:
            identifier_.export(outfile, level, namespace_, name_='identifier', pretty_print=pretty_print)
        if self.dateTime is not None:
            self.dateTime.export(outfile, level, namespace_, name_='dateTime', pretty_print=pretty_print)
        if self.subject is not None:
            self.subject.export(outfile, level, namespace_, name_='subject', pretty_print=pretty_print)
        if self.operator is not None:
            self.operator.export(outfile, level, namespace_, name_='operator', pretty_print=pretty_print)
        if self.view is not None:
            self.view.export(outfile, level, namespace_, name_='view', pretty_print=pretty_print)
        if self.deviceName is not None:
            self.deviceName.export(outfile, level, namespace_, name_='deviceName', pretty_print=pretty_print)
        if self.height is not None:
            self.height.export(outfile, level, namespace_, name_='height', pretty_print=pretty_print)
        if self.width is not None:
            self.width.export(outfile, level, namespace_, name_='width', pretty_print=pretty_print)
        if self.frames is not None:
            self.frames.export(outfile, level, namespace_, name_='frames', pretty_print=pretty_print)
        if self.length is not None:
            self.length.export(outfile, level, namespace_, name_='length', pretty_print=pretty_print)
        if self.content is not None:
            self.content.export(outfile, level, namespace_, name_='content', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Media', mapping_=None):
        element = super(Media, self).to_etree(parent_element, name_, mapping_)
        if self.type_ is not None:
            type__ = self.type_
            type__.to_etree(element, name_='type', mapping_=mapping_)
        if self.subtype is not None:
            subtype_ = self.subtype
            subtype_.to_etree(element, name_='subtype', mapping_=mapping_)
        for identifier_ in self.identifier:
            identifier_.to_etree(element, name_='identifier', mapping_=mapping_)
        if self.dateTime is not None:
            dateTime_ = self.dateTime
            dateTime_.to_etree(element, name_='dateTime', mapping_=mapping_)
        if self.subject is not None:
            subject_ = self.subject
            subject_.to_etree(element, name_='subject', mapping_=mapping_)
        if self.operator is not None:
            operator_ = self.operator
            operator_.to_etree(element, name_='operator', mapping_=mapping_)
        if self.view is not None:
            view_ = self.view
            view_.to_etree(element, name_='view', mapping_=mapping_)
        if self.deviceName is not None:
            deviceName_ = self.deviceName
            deviceName_.to_etree(element, name_='deviceName', mapping_=mapping_)
        if self.height is not None:
            height_ = self.height
            height_.to_etree(element, name_='height', mapping_=mapping_)
        if self.width is not None:
            width_ = self.width
            width_.to_etree(element, name_='width', mapping_=mapping_)
        if self.frames is not None:
            frames_ = self.frames
            frames_.to_etree(element, name_='frames', mapping_=mapping_)
        if self.length is not None:
            length_ = self.length
            length_.to_etree(element, name_='length', mapping_=mapping_)
        if self.content is not None:
            content_ = self.content
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
        super(Media, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'type':
            obj_ = MediaType.factory()
            obj_.build(child_)
            self.type_ = obj_
            obj_.original_tagname_ = 'type'
        elif nodeName_ == 'subtype':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.subtype = obj_
            obj_.original_tagname_ = 'subtype'
        elif nodeName_ == 'identifier':
            obj_ = Identifier.factory()
            obj_.build(child_)
            self.identifier.append(obj_)
            obj_.original_tagname_ = 'identifier'
        elif nodeName_ == 'dateTime':
            obj_ = dateTime.factory()
            obj_.build(child_)
            self.dateTime = obj_
            obj_.original_tagname_ = 'dateTime'
        elif nodeName_ == 'subject':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.subject = obj_
            obj_.original_tagname_ = 'subject'
        elif nodeName_ == 'operator':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.operator = obj_
            obj_.original_tagname_ = 'operator'
        elif nodeName_ == 'view':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.view = obj_
            obj_.original_tagname_ = 'view'
        elif nodeName_ == 'deviceName':
            obj_ = string.factory()
            obj_.build(child_)
            self.deviceName = obj_
            obj_.original_tagname_ = 'deviceName'
        elif nodeName_ == 'height':
            obj_ = integer.factory()
            obj_.build(child_)
            self.height = obj_
            obj_.original_tagname_ = 'height'
        elif nodeName_ == 'width':
            obj_ = integer.factory()
            obj_.build(child_)
            self.width = obj_
            obj_.original_tagname_ = 'width'
        elif nodeName_ == 'frames':
            obj_ = integer.factory()
            obj_.build(child_)
            self.frames = obj_
            obj_.original_tagname_ = 'frames'
        elif nodeName_ == 'length':
            obj_ = integer.factory()
            obj_.build(child_)
            self.length = obj_
            obj_.original_tagname_ = 'length'
        elif nodeName_ == 'content':
            obj_ = Attachment.factory()
            obj_.build(child_)
            self.content = obj_
            obj_.original_tagname_ = 'content'
        super(Media, self).buildChildren(child_, node, nodeName_, True)
# end class Media


class MediaType(Element):
    """Whether the Media is a photo, video, or audioIf the element is
    present, it must have either a @value, an @id, or extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(MediaType, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if MediaType.subclass:
            return MediaType.subclass(*args_, **kwargs_)
        else:
            return MediaType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(MediaType, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='MediaType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='MediaType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='MediaType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='MediaType'):
        super(MediaType, self).exportAttributes(outfile, level, already_processed, namespace_, name_='MediaType')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='MediaType', fromsubclass_=False, pretty_print=True):
        super(MediaType, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='MediaType', mapping_=None):
        element = super(MediaType, self).to_etree(parent_element, name_, mapping_)
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
        super(MediaType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(MediaType, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class MediaType
