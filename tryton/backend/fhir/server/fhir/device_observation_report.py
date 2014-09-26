from .base_classes import *
from .support_functions import *


class DeviceObservationReport(Resource):
    """Describes the data produced by a device at a point in time.If the
    element is present, it must have either a @value, an @id, or
    extensions"""
    subclass = None
    superclass = Resource
    def __init__(self, id=None, extension=None, modifierExtension=None, language=None, text=None, contained=None, instant=None, identifier=None, source=None, subject=None, virtualDevice=None):
        self.original_tagname_ = None
        super(DeviceObservationReport, self).__init__(id, extension, modifierExtension, language, text, contained, )
        self.instant = instant
        self.identifier = identifier
        self.source = source
        self.subject = subject
        if virtualDevice is None:
            self.virtualDevice = []
        else:
            self.virtualDevice = virtualDevice
    def factory(*args_, **kwargs_):
        if DeviceObservationReport.subclass:
            return DeviceObservationReport.subclass(*args_, **kwargs_)
        else:
            return DeviceObservationReport(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_instant(self): return self.instant
    def set_instant(self, instant): self.instant = instant
    def get_identifier(self): return self.identifier
    def set_identifier(self, identifier): self.identifier = identifier
    def get_source(self): return self.source
    def set_source(self, source): self.source = source
    def get_subject(self): return self.subject
    def set_subject(self, subject): self.subject = subject
    def get_virtualDevice(self): return self.virtualDevice
    def set_virtualDevice(self, virtualDevice): self.virtualDevice = virtualDevice
    def add_virtualDevice(self, value): self.virtualDevice.append(value)
    def insert_virtualDevice(self, index, value): self.virtualDevice[index] = value
    def hasContent_(self):
        if (
            self.instant is not None or
            self.identifier is not None or
            self.source is not None or
            self.subject is not None or
            self.virtualDevice or
            super(DeviceObservationReport, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='DeviceObservationReport', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='DeviceObservationReport')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='DeviceObservationReport', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='DeviceObservationReport'):
        super(DeviceObservationReport, self).exportAttributes(outfile, level, already_processed, namespace_, name_='DeviceObservationReport')
    def exportChildren(self, outfile, level, namespace_='', name_='DeviceObservationReport', fromsubclass_=False, pretty_print=True):
        super(DeviceObservationReport, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.instant is not None:
            self.instant.export(outfile, level, namespace_, name_='instant', pretty_print=pretty_print)
        if self.identifier is not None:
            self.identifier.export(outfile, level, namespace_, name_='identifier', pretty_print=pretty_print)
        if self.source is not None:
            self.source.export(outfile, level, namespace_, name_='source', pretty_print=pretty_print)
        if self.subject is not None:
            self.subject.export(outfile, level, namespace_, name_='subject', pretty_print=pretty_print)
        for virtualDevice_ in self.virtualDevice:
            virtualDevice_.export(outfile, level, namespace_, name_='virtualDevice', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='DeviceObservationReport', mapping_=None):
        element = super(DeviceObservationReport, self).to_etree(parent_element, name_, mapping_)
        if self.instant is not None:
            instant_ = self.instant
            instant_.to_etree(element, name_='instant', mapping_=mapping_)
        if self.identifier is not None:
            identifier_ = self.identifier
            identifier_.to_etree(element, name_='identifier', mapping_=mapping_)
        if self.source is not None:
            source_ = self.source
            source_.to_etree(element, name_='source', mapping_=mapping_)
        if self.subject is not None:
            subject_ = self.subject
            subject_.to_etree(element, name_='subject', mapping_=mapping_)
        for virtualDevice_ in self.virtualDevice:
            virtualDevice_.to_etree(element, name_='virtualDevice', mapping_=mapping_)
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
        super(DeviceObservationReport, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'instant':
            obj_ = instant.factory()
            obj_.build(child_)
            self.instant = obj_
            obj_.original_tagname_ = 'instant'
        elif nodeName_ == 'identifier':
            obj_ = Identifier.factory()
            obj_.build(child_)
            self.identifier = obj_
            obj_.original_tagname_ = 'identifier'
        elif nodeName_ == 'source':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.source = obj_
            obj_.original_tagname_ = 'source'
        elif nodeName_ == 'subject':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.subject = obj_
            obj_.original_tagname_ = 'subject'
        elif nodeName_ == 'virtualDevice':
            obj_ = DeviceObservationReport_VirtualDevice.factory()
            obj_.build(child_)
            self.virtualDevice.append(obj_)
            obj_.original_tagname_ = 'virtualDevice'
        super(DeviceObservationReport, self).buildChildren(child_, node, nodeName_, True)
# end class DeviceObservationReport


class DeviceObservationReport_VirtualDevice(BackboneElement):
    """Describes the data produced by a device at a point in time."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, code=None, channel=None):
        self.original_tagname_ = None
        super(DeviceObservationReport_VirtualDevice, self).__init__(id, extension, modifierExtension, )
        self.code = code
        if channel is None:
            self.channel = []
        else:
            self.channel = channel
    def factory(*args_, **kwargs_):
        if DeviceObservationReport_VirtualDevice.subclass:
            return DeviceObservationReport_VirtualDevice.subclass(*args_, **kwargs_)
        else:
            return DeviceObservationReport_VirtualDevice(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_code(self): return self.code
    def set_code(self, code): self.code = code
    def get_channel(self): return self.channel
    def set_channel(self, channel): self.channel = channel
    def add_channel(self, value): self.channel.append(value)
    def insert_channel(self, index, value): self.channel[index] = value
    def hasContent_(self):
        if (
            self.code is not None or
            self.channel or
            super(DeviceObservationReport_VirtualDevice, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='DeviceObservationReport.VirtualDevice', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='DeviceObservationReport.VirtualDevice')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='DeviceObservationReport.VirtualDevice', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='DeviceObservationReport.VirtualDevice'):
        super(DeviceObservationReport_VirtualDevice, self).exportAttributes(outfile, level, already_processed, namespace_, name_='DeviceObservationReport.VirtualDevice')
    def exportChildren(self, outfile, level, namespace_='', name_='DeviceObservationReport.VirtualDevice', fromsubclass_=False, pretty_print=True):
        super(DeviceObservationReport_VirtualDevice, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.code is not None:
            self.code.export(outfile, level, namespace_, name_='code', pretty_print=pretty_print)
        for channel_ in self.channel:
            channel_.export(outfile, level, namespace_, name_='channel', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='DeviceObservationReport.VirtualDevice', mapping_=None):
        element = super(DeviceObservationReport_VirtualDevice, self).to_etree(parent_element, name_, mapping_)
        if self.code is not None:
            code_ = self.code
            code_.to_etree(element, name_='code', mapping_=mapping_)
        for channel_ in self.channel:
            channel_.to_etree(element, name_='channel', mapping_=mapping_)
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
        super(DeviceObservationReport_VirtualDevice, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'code':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.code = obj_
            obj_.original_tagname_ = 'code'
        elif nodeName_ == 'channel':
            obj_ = DeviceObservationReport_Channel.factory()
            obj_.build(child_)
            self.channel.append(obj_)
            obj_.original_tagname_ = 'channel'
        super(DeviceObservationReport_VirtualDevice, self).buildChildren(child_, node, nodeName_, True)
# end class DeviceObservationReport_VirtualDevice


class DeviceObservationReport_Channel(BackboneElement):
    """Describes the data produced by a device at a point in time."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, code=None, metric=None):
        self.original_tagname_ = None
        super(DeviceObservationReport_Channel, self).__init__(id, extension, modifierExtension, )
        self.code = code
        if metric is None:
            self.metric = []
        else:
            self.metric = metric
    def factory(*args_, **kwargs_):
        if DeviceObservationReport_Channel.subclass:
            return DeviceObservationReport_Channel.subclass(*args_, **kwargs_)
        else:
            return DeviceObservationReport_Channel(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_code(self): return self.code
    def set_code(self, code): self.code = code
    def get_metric(self): return self.metric
    def set_metric(self, metric): self.metric = metric
    def add_metric(self, value): self.metric.append(value)
    def insert_metric(self, index, value): self.metric[index] = value
    def hasContent_(self):
        if (
            self.code is not None or
            self.metric or
            super(DeviceObservationReport_Channel, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='DeviceObservationReport.Channel', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='DeviceObservationReport.Channel')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='DeviceObservationReport.Channel', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='DeviceObservationReport.Channel'):
        super(DeviceObservationReport_Channel, self).exportAttributes(outfile, level, already_processed, namespace_, name_='DeviceObservationReport.Channel')
    def exportChildren(self, outfile, level, namespace_='', name_='DeviceObservationReport.Channel', fromsubclass_=False, pretty_print=True):
        super(DeviceObservationReport_Channel, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.code is not None:
            self.code.export(outfile, level, namespace_, name_='code', pretty_print=pretty_print)
        for metric_ in self.metric:
            metric_.export(outfile, level, namespace_, name_='metric', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='DeviceObservationReport.Channel', mapping_=None):
        element = super(DeviceObservationReport_Channel, self).to_etree(parent_element, name_, mapping_)
        if self.code is not None:
            code_ = self.code
            code_.to_etree(element, name_='code', mapping_=mapping_)
        for metric_ in self.metric:
            metric_.to_etree(element, name_='metric', mapping_=mapping_)
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
        super(DeviceObservationReport_Channel, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'code':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.code = obj_
            obj_.original_tagname_ = 'code'
        elif nodeName_ == 'metric':
            obj_ = DeviceObservationReport_Metric.factory()
            obj_.build(child_)
            self.metric.append(obj_)
            obj_.original_tagname_ = 'metric'
        super(DeviceObservationReport_Channel, self).buildChildren(child_, node, nodeName_, True)
# end class DeviceObservationReport_Channel


class DeviceObservationReport_Metric(BackboneElement):
    """Describes the data produced by a device at a point in time."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, observation=None):
        self.original_tagname_ = None
        super(DeviceObservationReport_Metric, self).__init__(id, extension, modifierExtension, )
        self.observation = observation
    def factory(*args_, **kwargs_):
        if DeviceObservationReport_Metric.subclass:
            return DeviceObservationReport_Metric.subclass(*args_, **kwargs_)
        else:
            return DeviceObservationReport_Metric(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_observation(self): return self.observation
    def set_observation(self, observation): self.observation = observation
    def hasContent_(self):
        if (
            self.observation is not None or
            super(DeviceObservationReport_Metric, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='DeviceObservationReport.Metric', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='DeviceObservationReport.Metric')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='DeviceObservationReport.Metric', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='DeviceObservationReport.Metric'):
        super(DeviceObservationReport_Metric, self).exportAttributes(outfile, level, already_processed, namespace_, name_='DeviceObservationReport.Metric')
    def exportChildren(self, outfile, level, namespace_='', name_='DeviceObservationReport.Metric', fromsubclass_=False, pretty_print=True):
        super(DeviceObservationReport_Metric, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.observation is not None:
            self.observation.export(outfile, level, namespace_, name_='observation', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='DeviceObservationReport.Metric', mapping_=None):
        element = super(DeviceObservationReport_Metric, self).to_etree(parent_element, name_, mapping_)
        if self.observation is not None:
            observation_ = self.observation
            observation_.to_etree(element, name_='observation', mapping_=mapping_)
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
        super(DeviceObservationReport_Metric, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'observation':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.observation = obj_
            obj_.original_tagname_ = 'observation'
        super(DeviceObservationReport_Metric, self).buildChildren(child_, node, nodeName_, True)
# end class DeviceObservationReport_Metric
