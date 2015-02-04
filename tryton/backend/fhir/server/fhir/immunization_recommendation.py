from .base_classes import *
from .support_functions import *


class ImmunizationRecommendation(Resource):
    """A patient's point-of-time immunization status and recommendation
    with optional supporting justification.If the element is
    present, it must have either a @value, an @id, or extensions"""
    subclass = None
    superclass = Resource
    def __init__(self, id=None, extension=None, modifierExtension=None, language=None, text=None, contained=None, identifier=None, subject=None, recommendation=None):
        self.original_tagname_ = None
        super(ImmunizationRecommendation, self).__init__(id, extension, modifierExtension, language, text, contained, )
        if identifier is None:
            self.identifier = []
        else:
            self.identifier = identifier
        self.subject = subject
        if recommendation is None:
            self.recommendation = []
        else:
            self.recommendation = recommendation
    def factory(*args_, **kwargs_):
        if ImmunizationRecommendation.subclass:
            return ImmunizationRecommendation.subclass(*args_, **kwargs_)
        else:
            return ImmunizationRecommendation(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_identifier(self): return self.identifier
    def set_identifier(self, identifier): self.identifier = identifier
    def add_identifier(self, value): self.identifier.append(value)
    def insert_identifier(self, index, value): self.identifier[index] = value
    def get_subject(self): return self.subject
    def set_subject(self, subject): self.subject = subject
    def get_recommendation(self): return self.recommendation
    def set_recommendation(self, recommendation): self.recommendation = recommendation
    def add_recommendation(self, value): self.recommendation.append(value)
    def insert_recommendation(self, index, value): self.recommendation[index] = value
    def hasContent_(self):
        if (
            self.identifier or
            self.subject is not None or
            self.recommendation or
            super(ImmunizationRecommendation, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='ImmunizationRecommendation', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ImmunizationRecommendation')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='ImmunizationRecommendation', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='ImmunizationRecommendation'):
        super(ImmunizationRecommendation, self).exportAttributes(outfile, level, already_processed, namespace_, name_='ImmunizationRecommendation')
    def exportChildren(self, outfile, level, namespace_='', name_='ImmunizationRecommendation', fromsubclass_=False, pretty_print=True):
        super(ImmunizationRecommendation, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for identifier_ in self.identifier:
            identifier_.export(outfile, level, namespace_, name_='identifier', pretty_print=pretty_print)
        if self.subject is not None:
            self.subject.export(outfile, level, namespace_, name_='subject', pretty_print=pretty_print)
        for recommendation_ in self.recommendation:
            recommendation_.export(outfile, level, namespace_, name_='recommendation', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='ImmunizationRecommendation', mapping_=None):
        element = super(ImmunizationRecommendation, self).to_etree(parent_element, name_, mapping_)
        for identifier_ in self.identifier:
            identifier_.to_etree(element, name_='identifier', mapping_=mapping_)
        if self.subject is not None:
            subject_ = self.subject
            subject_.to_etree(element, name_='subject', mapping_=mapping_)
        for recommendation_ in self.recommendation:
            recommendation_.to_etree(element, name_='recommendation', mapping_=mapping_)
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
        super(ImmunizationRecommendation, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'identifier':
            obj_ = Identifier.factory()
            obj_.build(child_)
            self.identifier.append(obj_)
            obj_.original_tagname_ = 'identifier'
        elif nodeName_ == 'subject':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.subject = obj_
            obj_.original_tagname_ = 'subject'
        elif nodeName_ == 'recommendation':
            obj_ = ImmunizationRecommendation_Recommendation.factory()
            obj_.build(child_)
            self.recommendation.append(obj_)
            obj_.original_tagname_ = 'recommendation'
        super(ImmunizationRecommendation, self).buildChildren(child_, node, nodeName_, True)
# end class ImmunizationRecommendation


class ImmunizationRecommendation_Recommendation(BackboneElement):
    """A patient's point-of-time immunization status and recommendation
    with optional supporting justification."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, date=None, vaccineType=None, doseNumber=None, forecastStatus=None, dateCriterion=None, protocol=None, supportingImmunization=None, supportingPatientInformation=None):
        self.original_tagname_ = None
        super(ImmunizationRecommendation_Recommendation, self).__init__(id, extension, modifierExtension, )
        self.date = date
        self.vaccineType = vaccineType
        self.doseNumber = doseNumber
        self.forecastStatus = forecastStatus
        if dateCriterion is None:
            self.dateCriterion = []
        else:
            self.dateCriterion = dateCriterion
        self.protocol = protocol
        if supportingImmunization is None:
            self.supportingImmunization = []
        else:
            self.supportingImmunization = supportingImmunization
        if supportingPatientInformation is None:
            self.supportingPatientInformation = []
        else:
            self.supportingPatientInformation = supportingPatientInformation
    def factory(*args_, **kwargs_):
        if ImmunizationRecommendation_Recommendation.subclass:
            return ImmunizationRecommendation_Recommendation.subclass(*args_, **kwargs_)
        else:
            return ImmunizationRecommendation_Recommendation(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_date(self): return self.date
    def set_date(self, date): self.date = date
    def get_vaccineType(self): return self.vaccineType
    def set_vaccineType(self, vaccineType): self.vaccineType = vaccineType
    def get_doseNumber(self): return self.doseNumber
    def set_doseNumber(self, doseNumber): self.doseNumber = doseNumber
    def get_forecastStatus(self): return self.forecastStatus
    def set_forecastStatus(self, forecastStatus): self.forecastStatus = forecastStatus
    def get_dateCriterion(self): return self.dateCriterion
    def set_dateCriterion(self, dateCriterion): self.dateCriterion = dateCriterion
    def add_dateCriterion(self, value): self.dateCriterion.append(value)
    def insert_dateCriterion(self, index, value): self.dateCriterion[index] = value
    def get_protocol(self): return self.protocol
    def set_protocol(self, protocol): self.protocol = protocol
    def get_supportingImmunization(self): return self.supportingImmunization
    def set_supportingImmunization(self, supportingImmunization): self.supportingImmunization = supportingImmunization
    def add_supportingImmunization(self, value): self.supportingImmunization.append(value)
    def insert_supportingImmunization(self, index, value): self.supportingImmunization[index] = value
    def get_supportingPatientInformation(self): return self.supportingPatientInformation
    def set_supportingPatientInformation(self, supportingPatientInformation): self.supportingPatientInformation = supportingPatientInformation
    def add_supportingPatientInformation(self, value): self.supportingPatientInformation.append(value)
    def insert_supportingPatientInformation(self, index, value): self.supportingPatientInformation[index] = value
    def hasContent_(self):
        if (
            self.date is not None or
            self.vaccineType is not None or
            self.doseNumber is not None or
            self.forecastStatus is not None or
            self.dateCriterion or
            self.protocol is not None or
            self.supportingImmunization or
            self.supportingPatientInformation or
            super(ImmunizationRecommendation_Recommendation, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='ImmunizationRecommendation.Recommendation', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ImmunizationRecommendation.Recommendation')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='ImmunizationRecommendation.Recommendation', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='ImmunizationRecommendation.Recommendation'):
        super(ImmunizationRecommendation_Recommendation, self).exportAttributes(outfile, level, already_processed, namespace_, name_='ImmunizationRecommendation.Recommendation')
    def exportChildren(self, outfile, level, namespace_='', name_='ImmunizationRecommendation.Recommendation', fromsubclass_=False, pretty_print=True):
        super(ImmunizationRecommendation_Recommendation, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.date is not None:
            self.date.export(outfile, level, namespace_, name_='date', pretty_print=pretty_print)
        if self.vaccineType is not None:
            self.vaccineType.export(outfile, level, namespace_, name_='vaccineType', pretty_print=pretty_print)
        if self.doseNumber is not None:
            self.doseNumber.export(outfile, level, namespace_, name_='doseNumber', pretty_print=pretty_print)
        if self.forecastStatus is not None:
            self.forecastStatus.export(outfile, level, namespace_, name_='forecastStatus', pretty_print=pretty_print)
        for dateCriterion_ in self.dateCriterion:
            dateCriterion_.export(outfile, level, namespace_, name_='dateCriterion', pretty_print=pretty_print)
        if self.protocol is not None:
            self.protocol.export(outfile, level, namespace_, name_='protocol', pretty_print=pretty_print)
        for supportingImmunization_ in self.supportingImmunization:
            supportingImmunization_.export(outfile, level, namespace_, name_='supportingImmunization', pretty_print=pretty_print)
        for supportingPatientInformation_ in self.supportingPatientInformation:
            supportingPatientInformation_.export(outfile, level, namespace_, name_='supportingPatientInformation', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='ImmunizationRecommendation.Recommendation', mapping_=None):
        element = super(ImmunizationRecommendation_Recommendation, self).to_etree(parent_element, name_, mapping_)
        if self.date is not None:
            date_ = self.date
            date_.to_etree(element, name_='date', mapping_=mapping_)
        if self.vaccineType is not None:
            vaccineType_ = self.vaccineType
            vaccineType_.to_etree(element, name_='vaccineType', mapping_=mapping_)
        if self.doseNumber is not None:
            doseNumber_ = self.doseNumber
            doseNumber_.to_etree(element, name_='doseNumber', mapping_=mapping_)
        if self.forecastStatus is not None:
            forecastStatus_ = self.forecastStatus
            forecastStatus_.to_etree(element, name_='forecastStatus', mapping_=mapping_)
        for dateCriterion_ in self.dateCriterion:
            dateCriterion_.to_etree(element, name_='dateCriterion', mapping_=mapping_)
        if self.protocol is not None:
            protocol_ = self.protocol
            protocol_.to_etree(element, name_='protocol', mapping_=mapping_)
        for supportingImmunization_ in self.supportingImmunization:
            supportingImmunization_.to_etree(element, name_='supportingImmunization', mapping_=mapping_)
        for supportingPatientInformation_ in self.supportingPatientInformation:
            supportingPatientInformation_.to_etree(element, name_='supportingPatientInformation', mapping_=mapping_)
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
        super(ImmunizationRecommendation_Recommendation, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'date':
            obj_ = dateTime.factory()
            obj_.build(child_)
            self.date = obj_
            obj_.original_tagname_ = 'date'
        elif nodeName_ == 'vaccineType':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.vaccineType = obj_
            obj_.original_tagname_ = 'vaccineType'
        elif nodeName_ == 'doseNumber':
            obj_ = integer.factory()
            obj_.build(child_)
            self.doseNumber = obj_
            obj_.original_tagname_ = 'doseNumber'
        elif nodeName_ == 'forecastStatus':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.forecastStatus = obj_
            obj_.original_tagname_ = 'forecastStatus'
        elif nodeName_ == 'dateCriterion':
            obj_ = ImmunizationRecommendation_DateCriterion.factory()
            obj_.build(child_)
            self.dateCriterion.append(obj_)
            obj_.original_tagname_ = 'dateCriterion'
        elif nodeName_ == 'protocol':
            obj_ = ImmunizationRecommendation_Protocol.factory()
            obj_.build(child_)
            self.protocol = obj_
            obj_.original_tagname_ = 'protocol'
        elif nodeName_ == 'supportingImmunization':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.supportingImmunization.append(obj_)
            obj_.original_tagname_ = 'supportingImmunization'
        elif nodeName_ == 'supportingPatientInformation':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.supportingPatientInformation.append(obj_)
            obj_.original_tagname_ = 'supportingPatientInformation'
        super(ImmunizationRecommendation_Recommendation, self).buildChildren(child_, node, nodeName_, True)
# end class ImmunizationRecommendation_Recommendation


class ImmunizationRecommendation_DateCriterion(BackboneElement):
    """A patient's point-of-time immunization status and recommendation
    with optional supporting justification."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, code=None, value=None):
        self.original_tagname_ = None
        super(ImmunizationRecommendation_DateCriterion, self).__init__(id, extension, modifierExtension, )
        self.code = code
        self.value = value
    def factory(*args_, **kwargs_):
        if ImmunizationRecommendation_DateCriterion.subclass:
            return ImmunizationRecommendation_DateCriterion.subclass(*args_, **kwargs_)
        else:
            return ImmunizationRecommendation_DateCriterion(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_code(self): return self.code
    def set_code(self, code): self.code = code
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            self.code is not None or
            self.value is not None or
            super(ImmunizationRecommendation_DateCriterion, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='ImmunizationRecommendation.DateCriterion', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ImmunizationRecommendation.DateCriterion')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='ImmunizationRecommendation.DateCriterion', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='ImmunizationRecommendation.DateCriterion'):
        super(ImmunizationRecommendation_DateCriterion, self).exportAttributes(outfile, level, already_processed, namespace_, name_='ImmunizationRecommendation.DateCriterion')
    def exportChildren(self, outfile, level, namespace_='', name_='ImmunizationRecommendation.DateCriterion', fromsubclass_=False, pretty_print=True):
        super(ImmunizationRecommendation_DateCriterion, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.code is not None:
            self.code.export(outfile, level, namespace_, name_='code', pretty_print=pretty_print)
        if self.value is not None:
            self.value.export(outfile, level, namespace_, name_='value', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='ImmunizationRecommendation.DateCriterion', mapping_=None):
        element = super(ImmunizationRecommendation_DateCriterion, self).to_etree(parent_element, name_, mapping_)
        if self.code is not None:
            code_ = self.code
            code_.to_etree(element, name_='code', mapping_=mapping_)
        if self.value is not None:
            value_ = self.value
            value_.to_etree(element, name_='value', mapping_=mapping_)
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
        super(ImmunizationRecommendation_DateCriterion, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'code':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.code = obj_
            obj_.original_tagname_ = 'code'
        elif nodeName_ == 'value':
            obj_ = dateTime.factory()
            obj_.build(child_)
            self.value = obj_
            obj_.original_tagname_ = 'value'
        super(ImmunizationRecommendation_DateCriterion, self).buildChildren(child_, node, nodeName_, True)
# end class ImmunizationRecommendation_DateCriterion


class ImmunizationRecommendation_Protocol(BackboneElement):
    """A patient's point-of-time immunization status and recommendation
    with optional supporting justification."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, doseSequence=None, description=None, authority=None, series=None):
        self.original_tagname_ = None
        super(ImmunizationRecommendation_Protocol, self).__init__(id, extension, modifierExtension, )
        self.doseSequence = doseSequence
        self.description = description
        self.authority = authority
        self.series = series
    def factory(*args_, **kwargs_):
        if ImmunizationRecommendation_Protocol.subclass:
            return ImmunizationRecommendation_Protocol.subclass(*args_, **kwargs_)
        else:
            return ImmunizationRecommendation_Protocol(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_doseSequence(self): return self.doseSequence
    def set_doseSequence(self, doseSequence): self.doseSequence = doseSequence
    def get_description(self): return self.description
    def set_description(self, description): self.description = description
    def get_authority(self): return self.authority
    def set_authority(self, authority): self.authority = authority
    def get_series(self): return self.series
    def set_series(self, series): self.series = series
    def hasContent_(self):
        if (
            self.doseSequence is not None or
            self.description is not None or
            self.authority is not None or
            self.series is not None or
            super(ImmunizationRecommendation_Protocol, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='ImmunizationRecommendation.Protocol', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ImmunizationRecommendation.Protocol')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='ImmunizationRecommendation.Protocol', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='ImmunizationRecommendation.Protocol'):
        super(ImmunizationRecommendation_Protocol, self).exportAttributes(outfile, level, already_processed, namespace_, name_='ImmunizationRecommendation.Protocol')
    def exportChildren(self, outfile, level, namespace_='', name_='ImmunizationRecommendation.Protocol', fromsubclass_=False, pretty_print=True):
        super(ImmunizationRecommendation_Protocol, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.doseSequence is not None:
            self.doseSequence.export(outfile, level, namespace_, name_='doseSequence', pretty_print=pretty_print)
        if self.description is not None:
            self.description.export(outfile, level, namespace_, name_='description', pretty_print=pretty_print)
        if self.authority is not None:
            self.authority.export(outfile, level, namespace_, name_='authority', pretty_print=pretty_print)
        if self.series is not None:
            self.series.export(outfile, level, namespace_, name_='series', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='ImmunizationRecommendation.Protocol', mapping_=None):
        element = super(ImmunizationRecommendation_Protocol, self).to_etree(parent_element, name_, mapping_)
        if self.doseSequence is not None:
            doseSequence_ = self.doseSequence
            doseSequence_.to_etree(element, name_='doseSequence', mapping_=mapping_)
        if self.description is not None:
            description_ = self.description
            description_.to_etree(element, name_='description', mapping_=mapping_)
        if self.authority is not None:
            authority_ = self.authority
            authority_.to_etree(element, name_='authority', mapping_=mapping_)
        if self.series is not None:
            series_ = self.series
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
        super(ImmunizationRecommendation_Protocol, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'doseSequence':
            obj_ = integer.factory()
            obj_.build(child_)
            self.doseSequence = obj_
            obj_.original_tagname_ = 'doseSequence'
        elif nodeName_ == 'description':
            obj_ = string.factory()
            obj_.build(child_)
            self.description = obj_
            obj_.original_tagname_ = 'description'
        elif nodeName_ == 'authority':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.authority = obj_
            obj_.original_tagname_ = 'authority'
        elif nodeName_ == 'series':
            obj_ = string.factory()
            obj_.build(child_)
            self.series = obj_
            obj_.original_tagname_ = 'series'
        super(ImmunizationRecommendation_Protocol, self).buildChildren(child_, node, nodeName_, True)
# end class ImmunizationRecommendation_Protocol
