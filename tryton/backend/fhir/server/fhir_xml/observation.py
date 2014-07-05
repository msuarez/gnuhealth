from .base_classes import *
from .support_functions import *


class Observation(Resource):
    """Measurements and simple assertions made about a patient, device or
    other subject.If the element is present, it must have either a
    @value, an @id, or extensionsThe information determined as a
    result of making the observation, if the information has a
    simple value.The time or time-period the observed value is
    asserted as being true. For biological subjects - e.g. human
    patients - this is usually called the "physiologically relevant
    time". This is usually either the time of the procedure or of
    specimen collection, but very often the source of the date/time
    is not known, only the date/time itself."""
    subclass = None
    superclass = Resource
    def __init__(self, id=None, extension=None, modifierExtension=None, language=None, text=None, contained=None, name=None, valueQuantity=None, valueCodeableConcept=None, valueAttachment=None, valueRatio=None, valuePeriod=None, valueSampledData=None, valueString=None, interpretation=None, comments=None, appliesDateTime=None, appliesPeriod=None, issued=None, status=None, reliability=None, bodySite=None, method=None, identifier=None, subject=None, specimen=None, performer=None, referenceRange=None, related=None):
        self.original_tagname_ = None
        super(Observation, self).__init__(id, extension, modifierExtension, language, text, contained, )
        self.name = name
        self.valueQuantity = valueQuantity
        self.valueCodeableConcept = valueCodeableConcept
        self.valueAttachment = valueAttachment
        self.valueRatio = valueRatio
        self.valuePeriod = valuePeriod
        self.valueSampledData = valueSampledData
        self.valueString = valueString
        self.interpretation = interpretation
        self.comments = comments
        self.appliesDateTime = appliesDateTime
        self.appliesPeriod = appliesPeriod
        self.issued = issued
        self.status = status
        self.reliability = reliability
        self.bodySite = bodySite
        self.method = method
        self.identifier = identifier
        self.subject = subject
        self.specimen = specimen
        if performer is None:
            self.performer = []
        else:
            self.performer = performer
        if referenceRange is None:
            self.referenceRange = []
        else:
            self.referenceRange = referenceRange
        if related is None:
            self.related = []
        else:
            self.related = related
    def factory(*args_, **kwargs_):
        if Observation.subclass:
            return Observation.subclass(*args_, **kwargs_)
        else:
            return Observation(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_name(self): return self.name
    def set_name(self, name): self.name = name
    def get_valueQuantity(self): return self.valueQuantity
    def set_valueQuantity(self, valueQuantity): self.valueQuantity = valueQuantity
    def get_valueCodeableConcept(self): return self.valueCodeableConcept
    def set_valueCodeableConcept(self, valueCodeableConcept): self.valueCodeableConcept = valueCodeableConcept
    def get_valueAttachment(self): return self.valueAttachment
    def set_valueAttachment(self, valueAttachment): self.valueAttachment = valueAttachment
    def get_valueRatio(self): return self.valueRatio
    def set_valueRatio(self, valueRatio): self.valueRatio = valueRatio
    def get_valuePeriod(self): return self.valuePeriod
    def set_valuePeriod(self, valuePeriod): self.valuePeriod = valuePeriod
    def get_valueSampledData(self): return self.valueSampledData
    def set_valueSampledData(self, valueSampledData): self.valueSampledData = valueSampledData
    def get_valueString(self): return self.valueString
    def set_valueString(self, valueString): self.valueString = valueString
    def get_interpretation(self): return self.interpretation
    def set_interpretation(self, interpretation): self.interpretation = interpretation
    def get_comments(self): return self.comments
    def set_comments(self, comments): self.comments = comments
    def get_appliesDateTime(self): return self.appliesDateTime
    def set_appliesDateTime(self, appliesDateTime): self.appliesDateTime = appliesDateTime
    def get_appliesPeriod(self): return self.appliesPeriod
    def set_appliesPeriod(self, appliesPeriod): self.appliesPeriod = appliesPeriod
    def get_issued(self): return self.issued
    def set_issued(self, issued): self.issued = issued
    def get_status(self): return self.status
    def set_status(self, status): self.status = status
    def get_reliability(self): return self.reliability
    def set_reliability(self, reliability): self.reliability = reliability
    def get_bodySite(self): return self.bodySite
    def set_bodySite(self, bodySite): self.bodySite = bodySite
    def get_method(self): return self.method
    def set_method(self, method): self.method = method
    def get_identifier(self): return self.identifier
    def set_identifier(self, identifier): self.identifier = identifier
    def get_subject(self): return self.subject
    def set_subject(self, subject): self.subject = subject
    def get_specimen(self): return self.specimen
    def set_specimen(self, specimen): self.specimen = specimen
    def get_performer(self): return self.performer
    def set_performer(self, performer): self.performer = performer
    def add_performer(self, value): self.performer.append(value)
    def insert_performer(self, index, value): self.performer[index] = value
    def get_referenceRange(self): return self.referenceRange
    def set_referenceRange(self, referenceRange): self.referenceRange = referenceRange
    def add_referenceRange(self, value): self.referenceRange.append(value)
    def insert_referenceRange(self, index, value): self.referenceRange[index] = value
    def get_related(self): return self.related
    def set_related(self, related): self.related = related
    def add_related(self, value): self.related.append(value)
    def insert_related(self, index, value): self.related[index] = value
    def hasContent_(self):
        if (
            self.name is not None or
            self.valueQuantity is not None or
            self.valueCodeableConcept is not None or
            self.valueAttachment is not None or
            self.valueRatio is not None or
            self.valuePeriod is not None or
            self.valueSampledData is not None or
            self.valueString is not None or
            self.interpretation is not None or
            self.comments is not None or
            self.appliesDateTime is not None or
            self.appliesPeriod is not None or
            self.issued is not None or
            self.status is not None or
            self.reliability is not None or
            self.bodySite is not None or
            self.method is not None or
            self.identifier is not None or
            self.subject is not None or
            self.specimen is not None or
            self.performer or
            self.referenceRange or
            self.related or
            super(Observation, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Observation', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Observation')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Observation', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Observation'):
        super(Observation, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Observation')
    def exportChildren(self, outfile, level, namespace_='', name_='Observation', fromsubclass_=False, pretty_print=True):
        super(Observation, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.name is not None:
            self.name.export(outfile, level, namespace_, name_='name', pretty_print=pretty_print)
        if self.valueQuantity is not None:
            self.valueQuantity.export(outfile, level, namespace_, name_='valueQuantity', pretty_print=pretty_print)
        if self.valueCodeableConcept is not None:
            self.valueCodeableConcept.export(outfile, level, namespace_, name_='valueCodeableConcept', pretty_print=pretty_print)
        if self.valueAttachment is not None:
            self.valueAttachment.export(outfile, level, namespace_, name_='valueAttachment', pretty_print=pretty_print)
        if self.valueRatio is not None:
            self.valueRatio.export(outfile, level, namespace_, name_='valueRatio', pretty_print=pretty_print)
        if self.valuePeriod is not None:
            self.valuePeriod.export(outfile, level, namespace_, name_='valuePeriod', pretty_print=pretty_print)
        if self.valueSampledData is not None:
            self.valueSampledData.export(outfile, level, namespace_, name_='valueSampledData', pretty_print=pretty_print)
        if self.valueString is not None:
            self.valueString.export(outfile, level, namespace_, name_='valueString', pretty_print=pretty_print)
        if self.interpretation is not None:
            self.interpretation.export(outfile, level, namespace_, name_='interpretation', pretty_print=pretty_print)
        if self.comments is not None:
            self.comments.export(outfile, level, namespace_, name_='comments', pretty_print=pretty_print)
        if self.appliesDateTime is not None:
            self.appliesDateTime.export(outfile, level, namespace_, name_='appliesDateTime', pretty_print=pretty_print)
        if self.appliesPeriod is not None:
            self.appliesPeriod.export(outfile, level, namespace_, name_='appliesPeriod', pretty_print=pretty_print)
        if self.issued is not None:
            self.issued.export(outfile, level, namespace_, name_='issued', pretty_print=pretty_print)
        if self.status is not None:
            self.status.export(outfile, level, namespace_, name_='status', pretty_print=pretty_print)
        if self.reliability is not None:
            self.reliability.export(outfile, level, namespace_, name_='reliability', pretty_print=pretty_print)
        if self.bodySite is not None:
            self.bodySite.export(outfile, level, namespace_, name_='bodySite', pretty_print=pretty_print)
        if self.method is not None:
            self.method.export(outfile, level, namespace_, name_='method', pretty_print=pretty_print)
        if self.identifier is not None:
            self.identifier.export(outfile, level, namespace_, name_='identifier', pretty_print=pretty_print)
        if self.subject is not None:
            self.subject.export(outfile, level, namespace_, name_='subject', pretty_print=pretty_print)
        if self.specimen is not None:
            self.specimen.export(outfile, level, namespace_, name_='specimen', pretty_print=pretty_print)
        for performer_ in self.performer:
            performer_.export(outfile, level, namespace_, name_='performer', pretty_print=pretty_print)
        for referenceRange_ in self.referenceRange:
            referenceRange_.export(outfile, level, namespace_, name_='referenceRange', pretty_print=pretty_print)
        for related_ in self.related:
            related_.export(outfile, level, namespace_, name_='related', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Observation', mapping_=None):
        element = super(Observation, self).to_etree(parent_element, name_, mapping_)
        if self.name is not None:
            name_ = self.name
            name_.to_etree(element, name_='name', mapping_=mapping_)
        if self.valueQuantity is not None:
            valueQuantity_ = self.valueQuantity
            valueQuantity_.to_etree(element, name_='valueQuantity', mapping_=mapping_)
        if self.valueCodeableConcept is not None:
            valueCodeableConcept_ = self.valueCodeableConcept
            valueCodeableConcept_.to_etree(element, name_='valueCodeableConcept', mapping_=mapping_)
        if self.valueAttachment is not None:
            valueAttachment_ = self.valueAttachment
            valueAttachment_.to_etree(element, name_='valueAttachment', mapping_=mapping_)
        if self.valueRatio is not None:
            valueRatio_ = self.valueRatio
            valueRatio_.to_etree(element, name_='valueRatio', mapping_=mapping_)
        if self.valuePeriod is not None:
            valuePeriod_ = self.valuePeriod
            valuePeriod_.to_etree(element, name_='valuePeriod', mapping_=mapping_)
        if self.valueSampledData is not None:
            valueSampledData_ = self.valueSampledData
            valueSampledData_.to_etree(element, name_='valueSampledData', mapping_=mapping_)
        if self.valueString is not None:
            valueString_ = self.valueString
            valueString_.to_etree(element, name_='valueString', mapping_=mapping_)
        if self.interpretation is not None:
            interpretation_ = self.interpretation
            interpretation_.to_etree(element, name_='interpretation', mapping_=mapping_)
        if self.comments is not None:
            comments_ = self.comments
            comments_.to_etree(element, name_='comments', mapping_=mapping_)
        if self.appliesDateTime is not None:
            appliesDateTime_ = self.appliesDateTime
            appliesDateTime_.to_etree(element, name_='appliesDateTime', mapping_=mapping_)
        if self.appliesPeriod is not None:
            appliesPeriod_ = self.appliesPeriod
            appliesPeriod_.to_etree(element, name_='appliesPeriod', mapping_=mapping_)
        if self.issued is not None:
            issued_ = self.issued
            issued_.to_etree(element, name_='issued', mapping_=mapping_)
        if self.status is not None:
            status_ = self.status
            status_.to_etree(element, name_='status', mapping_=mapping_)
        if self.reliability is not None:
            reliability_ = self.reliability
            reliability_.to_etree(element, name_='reliability', mapping_=mapping_)
        if self.bodySite is not None:
            bodySite_ = self.bodySite
            bodySite_.to_etree(element, name_='bodySite', mapping_=mapping_)
        if self.method is not None:
            method_ = self.method
            method_.to_etree(element, name_='method', mapping_=mapping_)
        if self.identifier is not None:
            identifier_ = self.identifier
            identifier_.to_etree(element, name_='identifier', mapping_=mapping_)
        if self.subject is not None:
            subject_ = self.subject
            subject_.to_etree(element, name_='subject', mapping_=mapping_)
        if self.specimen is not None:
            specimen_ = self.specimen
            specimen_.to_etree(element, name_='specimen', mapping_=mapping_)
        for performer_ in self.performer:
            performer_.to_etree(element, name_='performer', mapping_=mapping_)
        for referenceRange_ in self.referenceRange:
            referenceRange_.to_etree(element, name_='referenceRange', mapping_=mapping_)
        for related_ in self.related:
            related_.to_etree(element, name_='related', mapping_=mapping_)
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
        super(Observation, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'name':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.name = obj_
            obj_.original_tagname_ = 'name'
        elif nodeName_ == 'valueQuantity':
            obj_ = Quantity.factory()
            obj_.build(child_)
            self.valueQuantity = obj_
            obj_.original_tagname_ = 'valueQuantity'
        elif nodeName_ == 'valueCodeableConcept':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.valueCodeableConcept = obj_
            obj_.original_tagname_ = 'valueCodeableConcept'
        elif nodeName_ == 'valueAttachment':
            obj_ = Attachment.factory()
            obj_.build(child_)
            self.valueAttachment = obj_
            obj_.original_tagname_ = 'valueAttachment'
        elif nodeName_ == 'valueRatio':
            obj_ = Ratio.factory()
            obj_.build(child_)
            self.valueRatio = obj_
            obj_.original_tagname_ = 'valueRatio'
        elif nodeName_ == 'valuePeriod':
            obj_ = Period.factory()
            obj_.build(child_)
            self.valuePeriod = obj_
            obj_.original_tagname_ = 'valuePeriod'
        elif nodeName_ == 'valueSampledData':
            obj_ = SampledData.factory()
            obj_.build(child_)
            self.valueSampledData = obj_
            obj_.original_tagname_ = 'valueSampledData'
        elif nodeName_ == 'valueString':
            obj_ = string.factory()
            obj_.build(child_)
            self.valueString = obj_
            obj_.original_tagname_ = 'valueString'
        elif nodeName_ == 'interpretation':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.interpretation = obj_
            obj_.original_tagname_ = 'interpretation'
        elif nodeName_ == 'comments':
            obj_ = string.factory()
            obj_.build(child_)
            self.comments = obj_
            obj_.original_tagname_ = 'comments'
        elif nodeName_ == 'appliesDateTime':
            obj_ = dateTime.factory()
            obj_.build(child_)
            self.appliesDateTime = obj_
            obj_.original_tagname_ = 'appliesDateTime'
        elif nodeName_ == 'appliesPeriod':
            obj_ = Period.factory()
            obj_.build(child_)
            self.appliesPeriod = obj_
            obj_.original_tagname_ = 'appliesPeriod'
        elif nodeName_ == 'issued':
            obj_ = instant.factory()
            obj_.build(child_)
            self.issued = obj_
            obj_.original_tagname_ = 'issued'
        elif nodeName_ == 'status':
            obj_ = ObservationStatus.factory()
            obj_.build(child_)
            self.status = obj_
            obj_.original_tagname_ = 'status'
        elif nodeName_ == 'reliability':
            obj_ = ObservationReliability.factory()
            obj_.build(child_)
            self.reliability = obj_
            obj_.original_tagname_ = 'reliability'
        elif nodeName_ == 'bodySite':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.bodySite = obj_
            obj_.original_tagname_ = 'bodySite'
        elif nodeName_ == 'method':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.method = obj_
            obj_.original_tagname_ = 'method'
        elif nodeName_ == 'identifier':
            obj_ = Identifier.factory()
            obj_.build(child_)
            self.identifier = obj_
            obj_.original_tagname_ = 'identifier'
        elif nodeName_ == 'subject':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.subject = obj_
            obj_.original_tagname_ = 'subject'
        elif nodeName_ == 'specimen':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.specimen = obj_
            obj_.original_tagname_ = 'specimen'
        elif nodeName_ == 'performer':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.performer.append(obj_)
            obj_.original_tagname_ = 'performer'
        elif nodeName_ == 'referenceRange':
            obj_ = Observation_ReferenceRange.factory()
            obj_.build(child_)
            self.referenceRange.append(obj_)
            obj_.original_tagname_ = 'referenceRange'
        elif nodeName_ == 'related':
            obj_ = Observation_Related.factory()
            obj_.build(child_)
            self.related.append(obj_)
            obj_.original_tagname_ = 'related'
        super(Observation, self).buildChildren(child_, node, nodeName_, True)
# end class Observation


class Observation_ReferenceRange(BackboneElement):
    """Measurements and simple assertions made about a patient, device or
    other subject."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, low=None, high=None, meaning=None, age=None):
        self.original_tagname_ = None
        super(Observation_ReferenceRange, self).__init__(id, extension, modifierExtension, )
        self.low = low
        self.high = high
        self.meaning = meaning
        self.age = age
    def factory(*args_, **kwargs_):
        if Observation_ReferenceRange.subclass:
            return Observation_ReferenceRange.subclass(*args_, **kwargs_)
        else:
            return Observation_ReferenceRange(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_low(self): return self.low
    def set_low(self, low): self.low = low
    def get_high(self): return self.high
    def set_high(self, high): self.high = high
    def get_meaning(self): return self.meaning
    def set_meaning(self, meaning): self.meaning = meaning
    def get_age(self): return self.age
    def set_age(self, age): self.age = age
    def hasContent_(self):
        if (
            self.low is not None or
            self.high is not None or
            self.meaning is not None or
            self.age is not None or
            super(Observation_ReferenceRange, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Observation.ReferenceRange', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Observation.ReferenceRange')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Observation.ReferenceRange', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Observation.ReferenceRange'):
        super(Observation_ReferenceRange, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Observation.ReferenceRange')
    def exportChildren(self, outfile, level, namespace_='', name_='Observation.ReferenceRange', fromsubclass_=False, pretty_print=True):
        super(Observation_ReferenceRange, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.low is not None:
            self.low.export(outfile, level, namespace_, name_='low', pretty_print=pretty_print)
        if self.high is not None:
            self.high.export(outfile, level, namespace_, name_='high', pretty_print=pretty_print)
        if self.meaning is not None:
            self.meaning.export(outfile, level, namespace_, name_='meaning', pretty_print=pretty_print)
        if self.age is not None:
            self.age.export(outfile, level, namespace_, name_='age', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Observation.ReferenceRange', mapping_=None):
        element = super(Observation_ReferenceRange, self).to_etree(parent_element, name_, mapping_)
        if self.low is not None:
            low_ = self.low
            low_.to_etree(element, name_='low', mapping_=mapping_)
        if self.high is not None:
            high_ = self.high
            high_.to_etree(element, name_='high', mapping_=mapping_)
        if self.meaning is not None:
            meaning_ = self.meaning
            meaning_.to_etree(element, name_='meaning', mapping_=mapping_)
        if self.age is not None:
            age_ = self.age
            age_.to_etree(element, name_='age', mapping_=mapping_)
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
        super(Observation_ReferenceRange, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'low':
            obj_ = Quantity.factory()
            obj_.build(child_)
            self.low = obj_
            obj_.original_tagname_ = 'low'
        elif nodeName_ == 'high':
            obj_ = Quantity.factory()
            obj_.build(child_)
            self.high = obj_
            obj_.original_tagname_ = 'high'
        elif nodeName_ == 'meaning':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.meaning = obj_
            obj_.original_tagname_ = 'meaning'
        elif nodeName_ == 'age':
            obj_ = Range.factory()
            obj_.build(child_)
            self.age = obj_
            obj_.original_tagname_ = 'age'
        super(Observation_ReferenceRange, self).buildChildren(child_, node, nodeName_, True)
# end class Observation_ReferenceRange


class Observation_Related(BackboneElement):
    """Measurements and simple assertions made about a patient, device or
    other subject."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, type_=None, target=None):
        self.original_tagname_ = None
        super(Observation_Related, self).__init__(id, extension, modifierExtension, )
        self.type_ = type_
        self.target = target
    def factory(*args_, **kwargs_):
        if Observation_Related.subclass:
            return Observation_Related.subclass(*args_, **kwargs_)
        else:
            return Observation_Related(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_type(self): return self.type_
    def set_type(self, type_): self.type_ = type_
    def get_target(self): return self.target
    def set_target(self, target): self.target = target
    def hasContent_(self):
        if (
            self.type_ is not None or
            self.target is not None or
            super(Observation_Related, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Observation.Related', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Observation.Related')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Observation.Related', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Observation.Related'):
        super(Observation_Related, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Observation.Related')
    def exportChildren(self, outfile, level, namespace_='', name_='Observation.Related', fromsubclass_=False, pretty_print=True):
        super(Observation_Related, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.type_ is not None:
            self.type_.export(outfile, level, namespace_, name_='type', pretty_print=pretty_print)
        if self.target is not None:
            self.target.export(outfile, level, namespace_, name_='target', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Observation.Related', mapping_=None):
        element = super(Observation_Related, self).to_etree(parent_element, name_, mapping_)
        if self.type_ is not None:
            type__ = self.type_
            type__.to_etree(element, name_='type', mapping_=mapping_)
        if self.target is not None:
            target_ = self.target
            target_.to_etree(element, name_='target', mapping_=mapping_)
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
        super(Observation_Related, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'type':
            obj_ = ObservationRelationshipType.factory()
            obj_.build(child_)
            self.type_ = obj_
            obj_.original_tagname_ = 'type'
        elif nodeName_ == 'target':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.target = obj_
            obj_.original_tagname_ = 'target'
        super(Observation_Related, self).buildChildren(child_, node, nodeName_, True)
# end class Observation_Related


class ObservationReliability(Element):
    """Codes that provide an estimate of the degree to which quality issues
    have impacted on the value of an observationIf the element is
    present, it must have either a @value, an @id, or extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(ObservationReliability, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if ObservationReliability.subclass:
            return ObservationReliability.subclass(*args_, **kwargs_)
        else:
            return ObservationReliability(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(ObservationReliability, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='ObservationReliability', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ObservationReliability')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='ObservationReliability', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='ObservationReliability'):
        super(ObservationReliability, self).exportAttributes(outfile, level, already_processed, namespace_, name_='ObservationReliability')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='ObservationReliability', fromsubclass_=False, pretty_print=True):
        super(ObservationReliability, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='ObservationReliability', mapping_=None):
        element = super(ObservationReliability, self).to_etree(parent_element, name_, mapping_)
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
        super(ObservationReliability, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(ObservationReliability, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class ObservationReliability


class ObservationStatus(Element):
    """Codes providing the status of an observationIf the element is
    present, it must have either a @value, an @id, or extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(ObservationStatus, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if ObservationStatus.subclass:
            return ObservationStatus.subclass(*args_, **kwargs_)
        else:
            return ObservationStatus(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(ObservationStatus, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='ObservationStatus', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ObservationStatus')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='ObservationStatus', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='ObservationStatus'):
        super(ObservationStatus, self).exportAttributes(outfile, level, already_processed, namespace_, name_='ObservationStatus')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='ObservationStatus', fromsubclass_=False, pretty_print=True):
        super(ObservationStatus, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='ObservationStatus', mapping_=None):
        element = super(ObservationStatus, self).to_etree(parent_element, name_, mapping_)
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
        super(ObservationStatus, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(ObservationStatus, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class ObservationStatus


class ObservationRelationshipType(Element):
    """Codes specifying how two observations are relatedIf the element is
    present, it must have either a @value, an @id, or extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(ObservationRelationshipType, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if ObservationRelationshipType.subclass:
            return ObservationRelationshipType.subclass(*args_, **kwargs_)
        else:
            return ObservationRelationshipType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(ObservationRelationshipType, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='ObservationRelationshipType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ObservationRelationshipType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='ObservationRelationshipType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='ObservationRelationshipType'):
        super(ObservationRelationshipType, self).exportAttributes(outfile, level, already_processed, namespace_, name_='ObservationRelationshipType')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='ObservationRelationshipType', fromsubclass_=False, pretty_print=True):
        super(ObservationRelationshipType, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='ObservationRelationshipType', mapping_=None):
        element = super(ObservationRelationshipType, self).to_etree(parent_element, name_, mapping_)
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
        super(ObservationRelationshipType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(ObservationRelationshipType, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class ObservationRelationshipType
