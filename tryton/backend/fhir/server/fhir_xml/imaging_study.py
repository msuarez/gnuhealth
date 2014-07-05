from .base_classes import *
from .support_functions import *


class ImagingStudy(Resource):
    """Manifest of a set of images produced in study. The set of images may
    include every image in the study, or it may be an incomplete
    sample, such as a list of key images.If the element is present,
    it must have either a @value, an @id, or extensions"""
    subclass = None
    superclass = Resource
    def __init__(self, id=None, extension=None, modifierExtension=None, language=None, text=None, contained=None, dateTime=None, subject=None, uid=None, accessionNo=None, identifier=None, order=None, modality=None, referrer=None, availability=None, url=None, numberOfSeries=None, numberOfInstances=None, clinicalInformation=None, procedure=None, interpreter=None, description=None, series=None):
        self.original_tagname_ = None
        super(ImagingStudy, self).__init__(id, extension, modifierExtension, language, text, contained, )
        self.dateTime = dateTime
        self.subject = subject
        self.uid = uid
        self.accessionNo = accessionNo
        if identifier is None:
            self.identifier = []
        else:
            self.identifier = identifier
        if order is None:
            self.order = []
        else:
            self.order = order
        if modality is None:
            self.modality = []
        else:
            self.modality = modality
        self.referrer = referrer
        self.availability = availability
        self.url = url
        self.numberOfSeries = numberOfSeries
        self.numberOfInstances = numberOfInstances
        self.clinicalInformation = clinicalInformation
        if procedure is None:
            self.procedure = []
        else:
            self.procedure = procedure
        self.interpreter = interpreter
        self.description = description
        if series is None:
            self.series = []
        else:
            self.series = series
    def factory(*args_, **kwargs_):
        if ImagingStudy.subclass:
            return ImagingStudy.subclass(*args_, **kwargs_)
        else:
            return ImagingStudy(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_dateTime(self): return self.dateTime
    def set_dateTime(self, dateTime): self.dateTime = dateTime
    def get_subject(self): return self.subject
    def set_subject(self, subject): self.subject = subject
    def get_uid(self): return self.uid
    def set_uid(self, uid): self.uid = uid
    def get_accessionNo(self): return self.accessionNo
    def set_accessionNo(self, accessionNo): self.accessionNo = accessionNo
    def get_identifier(self): return self.identifier
    def set_identifier(self, identifier): self.identifier = identifier
    def add_identifier(self, value): self.identifier.append(value)
    def insert_identifier(self, index, value): self.identifier[index] = value
    def get_order(self): return self.order
    def set_order(self, order): self.order = order
    def add_order(self, value): self.order.append(value)
    def insert_order(self, index, value): self.order[index] = value
    def get_modality(self): return self.modality
    def set_modality(self, modality): self.modality = modality
    def add_modality(self, value): self.modality.append(value)
    def insert_modality(self, index, value): self.modality[index] = value
    def get_referrer(self): return self.referrer
    def set_referrer(self, referrer): self.referrer = referrer
    def get_availability(self): return self.availability
    def set_availability(self, availability): self.availability = availability
    def get_url(self): return self.url
    def set_url(self, url): self.url = url
    def get_numberOfSeries(self): return self.numberOfSeries
    def set_numberOfSeries(self, numberOfSeries): self.numberOfSeries = numberOfSeries
    def get_numberOfInstances(self): return self.numberOfInstances
    def set_numberOfInstances(self, numberOfInstances): self.numberOfInstances = numberOfInstances
    def get_clinicalInformation(self): return self.clinicalInformation
    def set_clinicalInformation(self, clinicalInformation): self.clinicalInformation = clinicalInformation
    def get_procedure(self): return self.procedure
    def set_procedure(self, procedure): self.procedure = procedure
    def add_procedure(self, value): self.procedure.append(value)
    def insert_procedure(self, index, value): self.procedure[index] = value
    def get_interpreter(self): return self.interpreter
    def set_interpreter(self, interpreter): self.interpreter = interpreter
    def get_description(self): return self.description
    def set_description(self, description): self.description = description
    def get_series(self): return self.series
    def set_series(self, series): self.series = series
    def add_series(self, value): self.series.append(value)
    def insert_series(self, index, value): self.series[index] = value
    def hasContent_(self):
        if (
            self.dateTime is not None or
            self.subject is not None or
            self.uid is not None or
            self.accessionNo is not None or
            self.identifier or
            self.order or
            self.modality or
            self.referrer is not None or
            self.availability is not None or
            self.url is not None or
            self.numberOfSeries is not None or
            self.numberOfInstances is not None or
            self.clinicalInformation is not None or
            self.procedure or
            self.interpreter is not None or
            self.description is not None or
            self.series or
            super(ImagingStudy, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='ImagingStudy', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ImagingStudy')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='ImagingStudy', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='ImagingStudy'):
        super(ImagingStudy, self).exportAttributes(outfile, level, already_processed, namespace_, name_='ImagingStudy')
    def exportChildren(self, outfile, level, namespace_='', name_='ImagingStudy', fromsubclass_=False, pretty_print=True):
        super(ImagingStudy, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.dateTime is not None:
            self.dateTime.export(outfile, level, namespace_, name_='dateTime', pretty_print=pretty_print)
        if self.subject is not None:
            self.subject.export(outfile, level, namespace_, name_='subject', pretty_print=pretty_print)
        if self.uid is not None:
            self.uid.export(outfile, level, namespace_, name_='uid', pretty_print=pretty_print)
        if self.accessionNo is not None:
            self.accessionNo.export(outfile, level, namespace_, name_='accessionNo', pretty_print=pretty_print)
        for identifier_ in self.identifier:
            identifier_.export(outfile, level, namespace_, name_='identifier', pretty_print=pretty_print)
        for order_ in self.order:
            order_.export(outfile, level, namespace_, name_='order', pretty_print=pretty_print)
        for modality_ in self.modality:
            modality_.export(outfile, level, namespace_, name_='modality', pretty_print=pretty_print)
        if self.referrer is not None:
            self.referrer.export(outfile, level, namespace_, name_='referrer', pretty_print=pretty_print)
        if self.availability is not None:
            self.availability.export(outfile, level, namespace_, name_='availability', pretty_print=pretty_print)
        if self.url is not None:
            self.url.export(outfile, level, namespace_, name_='url', pretty_print=pretty_print)
        if self.numberOfSeries is not None:
            self.numberOfSeries.export(outfile, level, namespace_, name_='numberOfSeries', pretty_print=pretty_print)
        if self.numberOfInstances is not None:
            self.numberOfInstances.export(outfile, level, namespace_, name_='numberOfInstances', pretty_print=pretty_print)
        if self.clinicalInformation is not None:
            self.clinicalInformation.export(outfile, level, namespace_, name_='clinicalInformation', pretty_print=pretty_print)
        for procedure_ in self.procedure:
            procedure_.export(outfile, level, namespace_, name_='procedure', pretty_print=pretty_print)
        if self.interpreter is not None:
            self.interpreter.export(outfile, level, namespace_, name_='interpreter', pretty_print=pretty_print)
        if self.description is not None:
            self.description.export(outfile, level, namespace_, name_='description', pretty_print=pretty_print)
        for series_ in self.series:
            series_.export(outfile, level, namespace_, name_='series', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='ImagingStudy', mapping_=None):
        element = super(ImagingStudy, self).to_etree(parent_element, name_, mapping_)
        if self.dateTime is not None:
            dateTime_ = self.dateTime
            dateTime_.to_etree(element, name_='dateTime', mapping_=mapping_)
        if self.subject is not None:
            subject_ = self.subject
            subject_.to_etree(element, name_='subject', mapping_=mapping_)
        if self.uid is not None:
            uid_ = self.uid
            uid_.to_etree(element, name_='uid', mapping_=mapping_)
        if self.accessionNo is not None:
            accessionNo_ = self.accessionNo
            accessionNo_.to_etree(element, name_='accessionNo', mapping_=mapping_)
        for identifier_ in self.identifier:
            identifier_.to_etree(element, name_='identifier', mapping_=mapping_)
        for order_ in self.order:
            order_.to_etree(element, name_='order', mapping_=mapping_)
        for modality_ in self.modality:
            modality_.to_etree(element, name_='modality', mapping_=mapping_)
        if self.referrer is not None:
            referrer_ = self.referrer
            referrer_.to_etree(element, name_='referrer', mapping_=mapping_)
        if self.availability is not None:
            availability_ = self.availability
            availability_.to_etree(element, name_='availability', mapping_=mapping_)
        if self.url is not None:
            url_ = self.url
            url_.to_etree(element, name_='url', mapping_=mapping_)
        if self.numberOfSeries is not None:
            numberOfSeries_ = self.numberOfSeries
            numberOfSeries_.to_etree(element, name_='numberOfSeries', mapping_=mapping_)
        if self.numberOfInstances is not None:
            numberOfInstances_ = self.numberOfInstances
            numberOfInstances_.to_etree(element, name_='numberOfInstances', mapping_=mapping_)
        if self.clinicalInformation is not None:
            clinicalInformation_ = self.clinicalInformation
            clinicalInformation_.to_etree(element, name_='clinicalInformation', mapping_=mapping_)
        for procedure_ in self.procedure:
            procedure_.to_etree(element, name_='procedure', mapping_=mapping_)
        if self.interpreter is not None:
            interpreter_ = self.interpreter
            interpreter_.to_etree(element, name_='interpreter', mapping_=mapping_)
        if self.description is not None:
            description_ = self.description
            description_.to_etree(element, name_='description', mapping_=mapping_)
        for series_ in self.series:
            series_.to_etree(element, name_='series', mapping_=mapping_)
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
        super(ImagingStudy, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'dateTime':
            obj_ = dateTime.factory()
            obj_.build(child_)
            self.dateTime = obj_
            obj_.original_tagname_ = 'dateTime'
        elif nodeName_ == 'subject':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.subject = obj_
            obj_.original_tagname_ = 'subject'
        elif nodeName_ == 'uid':
            obj_ = oid.factory()
            obj_.build(child_)
            self.uid = obj_
            obj_.original_tagname_ = 'uid'
        elif nodeName_ == 'accessionNo':
            obj_ = Identifier.factory()
            obj_.build(child_)
            self.accessionNo = obj_
            obj_.original_tagname_ = 'accessionNo'
        elif nodeName_ == 'identifier':
            obj_ = Identifier.factory()
            obj_.build(child_)
            self.identifier.append(obj_)
            obj_.original_tagname_ = 'identifier'
        elif nodeName_ == 'order':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.order.append(obj_)
            obj_.original_tagname_ = 'order'
        elif nodeName_ == 'modality':
            obj_ = ImagingModality.factory()
            obj_.build(child_)
            self.modality.append(obj_)
            obj_.original_tagname_ = 'modality'
        elif nodeName_ == 'referrer':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.referrer = obj_
            obj_.original_tagname_ = 'referrer'
        elif nodeName_ == 'availability':
            obj_ = InstanceAvailability.factory()
            obj_.build(child_)
            self.availability = obj_
            obj_.original_tagname_ = 'availability'
        elif nodeName_ == 'url':
            obj_ = uri.factory()
            obj_.build(child_)
            self.url = obj_
            obj_.original_tagname_ = 'url'
        elif nodeName_ == 'numberOfSeries':
            obj_ = integer.factory()
            obj_.build(child_)
            self.numberOfSeries = obj_
            obj_.original_tagname_ = 'numberOfSeries'
        elif nodeName_ == 'numberOfInstances':
            obj_ = integer.factory()
            obj_.build(child_)
            self.numberOfInstances = obj_
            obj_.original_tagname_ = 'numberOfInstances'
        elif nodeName_ == 'clinicalInformation':
            obj_ = string.factory()
            obj_.build(child_)
            self.clinicalInformation = obj_
            obj_.original_tagname_ = 'clinicalInformation'
        elif nodeName_ == 'procedure':
            obj_ = Coding.factory()
            obj_.build(child_)
            self.procedure.append(obj_)
            obj_.original_tagname_ = 'procedure'
        elif nodeName_ == 'interpreter':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.interpreter = obj_
            obj_.original_tagname_ = 'interpreter'
        elif nodeName_ == 'description':
            obj_ = string.factory()
            obj_.build(child_)
            self.description = obj_
            obj_.original_tagname_ = 'description'
        elif nodeName_ == 'series':
            obj_ = ImagingStudy_Series.factory()
            obj_.build(child_)
            self.series.append(obj_)
            obj_.original_tagname_ = 'series'
        super(ImagingStudy, self).buildChildren(child_, node, nodeName_, True)
# end class ImagingStudy


class ImagingStudy_Series(BackboneElement):
    """Manifest of a set of images produced in study. The set of images may
    include every image in the study, or it may be an incomplete
    sample, such as a list of key images."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, number=None, modality=None, uid=None, description=None, numberOfInstances=None, availability=None, url=None, bodySite=None, dateTime=None, instance=None):
        self.original_tagname_ = None
        super(ImagingStudy_Series, self).__init__(id, extension, modifierExtension, )
        self.number = number
        self.modality = modality
        self.uid = uid
        self.description = description
        self.numberOfInstances = numberOfInstances
        self.availability = availability
        self.url = url
        self.bodySite = bodySite
        self.dateTime = dateTime
        if instance is None:
            self.instance = []
        else:
            self.instance = instance
    def factory(*args_, **kwargs_):
        if ImagingStudy_Series.subclass:
            return ImagingStudy_Series.subclass(*args_, **kwargs_)
        else:
            return ImagingStudy_Series(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_number(self): return self.number
    def set_number(self, number): self.number = number
    def get_modality(self): return self.modality
    def set_modality(self, modality): self.modality = modality
    def get_uid(self): return self.uid
    def set_uid(self, uid): self.uid = uid
    def get_description(self): return self.description
    def set_description(self, description): self.description = description
    def get_numberOfInstances(self): return self.numberOfInstances
    def set_numberOfInstances(self, numberOfInstances): self.numberOfInstances = numberOfInstances
    def get_availability(self): return self.availability
    def set_availability(self, availability): self.availability = availability
    def get_url(self): return self.url
    def set_url(self, url): self.url = url
    def get_bodySite(self): return self.bodySite
    def set_bodySite(self, bodySite): self.bodySite = bodySite
    def get_dateTime(self): return self.dateTime
    def set_dateTime(self, dateTime): self.dateTime = dateTime
    def get_instance(self): return self.instance
    def set_instance(self, instance): self.instance = instance
    def add_instance(self, value): self.instance.append(value)
    def insert_instance(self, index, value): self.instance[index] = value
    def hasContent_(self):
        if (
            self.number is not None or
            self.modality is not None or
            self.uid is not None or
            self.description is not None or
            self.numberOfInstances is not None or
            self.availability is not None or
            self.url is not None or
            self.bodySite is not None or
            self.dateTime is not None or
            self.instance or
            super(ImagingStudy_Series, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='ImagingStudy.Series', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ImagingStudy.Series')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='ImagingStudy.Series', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='ImagingStudy.Series'):
        super(ImagingStudy_Series, self).exportAttributes(outfile, level, already_processed, namespace_, name_='ImagingStudy.Series')
    def exportChildren(self, outfile, level, namespace_='', name_='ImagingStudy.Series', fromsubclass_=False, pretty_print=True):
        super(ImagingStudy_Series, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.number is not None:
            self.number.export(outfile, level, namespace_, name_='number', pretty_print=pretty_print)
        if self.modality is not None:
            self.modality.export(outfile, level, namespace_, name_='modality', pretty_print=pretty_print)
        if self.uid is not None:
            self.uid.export(outfile, level, namespace_, name_='uid', pretty_print=pretty_print)
        if self.description is not None:
            self.description.export(outfile, level, namespace_, name_='description', pretty_print=pretty_print)
        if self.numberOfInstances is not None:
            self.numberOfInstances.export(outfile, level, namespace_, name_='numberOfInstances', pretty_print=pretty_print)
        if self.availability is not None:
            self.availability.export(outfile, level, namespace_, name_='availability', pretty_print=pretty_print)
        if self.url is not None:
            self.url.export(outfile, level, namespace_, name_='url', pretty_print=pretty_print)
        if self.bodySite is not None:
            self.bodySite.export(outfile, level, namespace_, name_='bodySite', pretty_print=pretty_print)
        if self.dateTime is not None:
            self.dateTime.export(outfile, level, namespace_, name_='dateTime', pretty_print=pretty_print)
        for instance_ in self.instance:
            instance_.export(outfile, level, namespace_, name_='instance', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='ImagingStudy.Series', mapping_=None):
        element = super(ImagingStudy_Series, self).to_etree(parent_element, name_, mapping_)
        if self.number is not None:
            number_ = self.number
            number_.to_etree(element, name_='number', mapping_=mapping_)
        if self.modality is not None:
            modality_ = self.modality
            modality_.to_etree(element, name_='modality', mapping_=mapping_)
        if self.uid is not None:
            uid_ = self.uid
            uid_.to_etree(element, name_='uid', mapping_=mapping_)
        if self.description is not None:
            description_ = self.description
            description_.to_etree(element, name_='description', mapping_=mapping_)
        if self.numberOfInstances is not None:
            numberOfInstances_ = self.numberOfInstances
            numberOfInstances_.to_etree(element, name_='numberOfInstances', mapping_=mapping_)
        if self.availability is not None:
            availability_ = self.availability
            availability_.to_etree(element, name_='availability', mapping_=mapping_)
        if self.url is not None:
            url_ = self.url
            url_.to_etree(element, name_='url', mapping_=mapping_)
        if self.bodySite is not None:
            bodySite_ = self.bodySite
            bodySite_.to_etree(element, name_='bodySite', mapping_=mapping_)
        if self.dateTime is not None:
            dateTime_ = self.dateTime
            dateTime_.to_etree(element, name_='dateTime', mapping_=mapping_)
        for instance_ in self.instance:
            instance_.to_etree(element, name_='instance', mapping_=mapping_)
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
        super(ImagingStudy_Series, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'number':
            obj_ = integer.factory()
            obj_.build(child_)
            self.number = obj_
            obj_.original_tagname_ = 'number'
        elif nodeName_ == 'modality':
            obj_ = Modality.factory()
            obj_.build(child_)
            self.modality = obj_
            obj_.original_tagname_ = 'modality'
        elif nodeName_ == 'uid':
            obj_ = oid.factory()
            obj_.build(child_)
            self.uid = obj_
            obj_.original_tagname_ = 'uid'
        elif nodeName_ == 'description':
            obj_ = string.factory()
            obj_.build(child_)
            self.description = obj_
            obj_.original_tagname_ = 'description'
        elif nodeName_ == 'numberOfInstances':
            obj_ = integer.factory()
            obj_.build(child_)
            self.numberOfInstances = obj_
            obj_.original_tagname_ = 'numberOfInstances'
        elif nodeName_ == 'availability':
            obj_ = InstanceAvailability.factory()
            obj_.build(child_)
            self.availability = obj_
            obj_.original_tagname_ = 'availability'
        elif nodeName_ == 'url':
            obj_ = uri.factory()
            obj_.build(child_)
            self.url = obj_
            obj_.original_tagname_ = 'url'
        elif nodeName_ == 'bodySite':
            obj_ = Coding.factory()
            obj_.build(child_)
            self.bodySite = obj_
            obj_.original_tagname_ = 'bodySite'
        elif nodeName_ == 'dateTime':
            obj_ = dateTime.factory()
            obj_.build(child_)
            self.dateTime = obj_
            obj_.original_tagname_ = 'dateTime'
        elif nodeName_ == 'instance':
            obj_ = ImagingStudy_Instance.factory()
            obj_.build(child_)
            self.instance.append(obj_)
            obj_.original_tagname_ = 'instance'
        super(ImagingStudy_Series, self).buildChildren(child_, node, nodeName_, True)
# end class ImagingStudy_Series


class ImagingStudy_Instance(BackboneElement):
    """Manifest of a set of images produced in study. The set of images may
    include every image in the study, or it may be an incomplete
    sample, such as a list of key images."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, number=None, uid=None, sopclass=None, type_=None, title=None, url=None, attachment=None):
        self.original_tagname_ = None
        super(ImagingStudy_Instance, self).__init__(id, extension, modifierExtension, )
        self.number = number
        self.uid = uid
        self.sopclass = sopclass
        self.type_ = type_
        self.title = title
        self.url = url
        self.attachment = attachment
    def factory(*args_, **kwargs_):
        if ImagingStudy_Instance.subclass:
            return ImagingStudy_Instance.subclass(*args_, **kwargs_)
        else:
            return ImagingStudy_Instance(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_number(self): return self.number
    def set_number(self, number): self.number = number
    def get_uid(self): return self.uid
    def set_uid(self, uid): self.uid = uid
    def get_sopclass(self): return self.sopclass
    def set_sopclass(self, sopclass): self.sopclass = sopclass
    def get_type(self): return self.type_
    def set_type(self, type_): self.type_ = type_
    def get_title(self): return self.title
    def set_title(self, title): self.title = title
    def get_url(self): return self.url
    def set_url(self, url): self.url = url
    def get_attachment(self): return self.attachment
    def set_attachment(self, attachment): self.attachment = attachment
    def hasContent_(self):
        if (
            self.number is not None or
            self.uid is not None or
            self.sopclass is not None or
            self.type_ is not None or
            self.title is not None or
            self.url is not None or
            self.attachment is not None or
            super(ImagingStudy_Instance, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='ImagingStudy.Instance', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ImagingStudy.Instance')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='ImagingStudy.Instance', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='ImagingStudy.Instance'):
        super(ImagingStudy_Instance, self).exportAttributes(outfile, level, already_processed, namespace_, name_='ImagingStudy.Instance')
    def exportChildren(self, outfile, level, namespace_='', name_='ImagingStudy.Instance', fromsubclass_=False, pretty_print=True):
        super(ImagingStudy_Instance, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.number is not None:
            self.number.export(outfile, level, namespace_, name_='number', pretty_print=pretty_print)
        if self.uid is not None:
            self.uid.export(outfile, level, namespace_, name_='uid', pretty_print=pretty_print)
        if self.sopclass is not None:
            self.sopclass.export(outfile, level, namespace_, name_='sopclass', pretty_print=pretty_print)
        if self.type_ is not None:
            self.type_.export(outfile, level, namespace_, name_='type', pretty_print=pretty_print)
        if self.title is not None:
            self.title.export(outfile, level, namespace_, name_='title', pretty_print=pretty_print)
        if self.url is not None:
            self.url.export(outfile, level, namespace_, name_='url', pretty_print=pretty_print)
        if self.attachment is not None:
            self.attachment.export(outfile, level, namespace_, name_='attachment', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='ImagingStudy.Instance', mapping_=None):
        element = super(ImagingStudy_Instance, self).to_etree(parent_element, name_, mapping_)
        if self.number is not None:
            number_ = self.number
            number_.to_etree(element, name_='number', mapping_=mapping_)
        if self.uid is not None:
            uid_ = self.uid
            uid_.to_etree(element, name_='uid', mapping_=mapping_)
        if self.sopclass is not None:
            sopclass_ = self.sopclass
            sopclass_.to_etree(element, name_='sopclass', mapping_=mapping_)
        if self.type_ is not None:
            type__ = self.type_
            type__.to_etree(element, name_='type', mapping_=mapping_)
        if self.title is not None:
            title_ = self.title
            title_.to_etree(element, name_='title', mapping_=mapping_)
        if self.url is not None:
            url_ = self.url
            url_.to_etree(element, name_='url', mapping_=mapping_)
        if self.attachment is not None:
            attachment_ = self.attachment
            attachment_.to_etree(element, name_='attachment', mapping_=mapping_)
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
        super(ImagingStudy_Instance, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'number':
            obj_ = integer.factory()
            obj_.build(child_)
            self.number = obj_
            obj_.original_tagname_ = 'number'
        elif nodeName_ == 'uid':
            obj_ = oid.factory()
            obj_.build(child_)
            self.uid = obj_
            obj_.original_tagname_ = 'uid'
        elif nodeName_ == 'sopclass':
            obj_ = oid.factory()
            obj_.build(child_)
            self.sopclass = obj_
            obj_.original_tagname_ = 'sopclass'
        elif nodeName_ == 'type':
            obj_ = string.factory()
            obj_.build(child_)
            self.type_ = obj_
            obj_.original_tagname_ = 'type'
        elif nodeName_ == 'title':
            obj_ = string.factory()
            obj_.build(child_)
            self.title = obj_
            obj_.original_tagname_ = 'title'
        elif nodeName_ == 'url':
            obj_ = uri.factory()
            obj_.build(child_)
            self.url = obj_
            obj_.original_tagname_ = 'url'
        elif nodeName_ == 'attachment':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.attachment = obj_
            obj_.original_tagname_ = 'attachment'
        super(ImagingStudy_Instance, self).buildChildren(child_, node, nodeName_, True)
# end class ImagingStudy_Instance


class ImagingModality(Element):
    """Type of acquired image data in the instanceIf the element is
    present, it must have either a @value, an @id, or extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(ImagingModality, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if ImagingModality.subclass:
            return ImagingModality.subclass(*args_, **kwargs_)
        else:
            return ImagingModality(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(ImagingModality, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='ImagingModality', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ImagingModality')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='ImagingModality', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='ImagingModality'):
        super(ImagingModality, self).exportAttributes(outfile, level, already_processed, namespace_, name_='ImagingModality')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='ImagingModality', fromsubclass_=False, pretty_print=True):
        super(ImagingModality, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='ImagingModality', mapping_=None):
        element = super(ImagingModality, self).to_etree(parent_element, name_, mapping_)
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
        super(ImagingModality, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(ImagingModality, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class ImagingModality


class Modality(Element):
    """Type of data in the instanceIf the element is present, it must have
    either a @value, an @id, or extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(Modality, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if Modality.subclass:
            return Modality.subclass(*args_, **kwargs_)
        else:
            return Modality(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(Modality, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Modality', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Modality')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Modality', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Modality'):
        super(Modality, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Modality')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='Modality', fromsubclass_=False, pretty_print=True):
        super(Modality, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Modality', mapping_=None):
        element = super(Modality, self).to_etree(parent_element, name_, mapping_)
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
        super(Modality, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(Modality, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class Modality
