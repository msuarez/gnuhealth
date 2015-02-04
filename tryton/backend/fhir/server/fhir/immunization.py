from .base_classes import *
from .support_functions import *


class Immunization(Resource):
    """Immunization event information.If the element is present, it must
    have either a @value, an @id, or extensions"""
    subclass = None
    superclass = Resource
    def __init__(self, id=None, extension=None, modifierExtension=None, language=None, text=None, contained=None, identifier=None, date=None, vaccineType=None, subject=None, refusedIndicator=None, reported=None, performer=None, requester=None, manufacturer=None, location=None, lotNumber=None, expirationDate=None, site=None, route=None, doseQuantity=None, explanation=None, reaction=None, vaccinationProtocol=None):
        self.original_tagname_ = None
        super(Immunization, self).__init__(id, extension, modifierExtension, language, text, contained, )
        if identifier is None:
            self.identifier = []
        else:
            self.identifier = identifier
        self.date = date
        self.vaccineType = vaccineType
        self.subject = subject
        self.refusedIndicator = refusedIndicator
        self.reported = reported
        self.performer = performer
        self.requester = requester
        self.manufacturer = manufacturer
        self.location = location
        self.lotNumber = lotNumber
        self.expirationDate = expirationDate
        self.site = site
        self.route = route
        self.doseQuantity = doseQuantity
        self.explanation = explanation
        if reaction is None:
            self.reaction = []
        else:
            self.reaction = reaction
        if vaccinationProtocol is None:
            self.vaccinationProtocol = []
        else:
            self.vaccinationProtocol = vaccinationProtocol
    def factory(*args_, **kwargs_):
        if Immunization.subclass:
            return Immunization.subclass(*args_, **kwargs_)
        else:
            return Immunization(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_identifier(self): return self.identifier
    def set_identifier(self, identifier): self.identifier = identifier
    def add_identifier(self, value): self.identifier.append(value)
    def insert_identifier(self, index, value): self.identifier[index] = value
    def get_date(self): return self.date
    def set_date(self, date): self.date = date
    def get_vaccineType(self): return self.vaccineType
    def set_vaccineType(self, vaccineType): self.vaccineType = vaccineType
    def get_subject(self): return self.subject
    def set_subject(self, subject): self.subject = subject
    def get_refusedIndicator(self): return self.refusedIndicator
    def set_refusedIndicator(self, refusedIndicator): self.refusedIndicator = refusedIndicator
    def get_reported(self): return self.reported
    def set_reported(self, reported): self.reported = reported
    def get_performer(self): return self.performer
    def set_performer(self, performer): self.performer = performer
    def get_requester(self): return self.requester
    def set_requester(self, requester): self.requester = requester
    def get_manufacturer(self): return self.manufacturer
    def set_manufacturer(self, manufacturer): self.manufacturer = manufacturer
    def get_location(self): return self.location
    def set_location(self, location): self.location = location
    def get_lotNumber(self): return self.lotNumber
    def set_lotNumber(self, lotNumber): self.lotNumber = lotNumber
    def get_expirationDate(self): return self.expirationDate
    def set_expirationDate(self, expirationDate): self.expirationDate = expirationDate
    def get_site(self): return self.site
    def set_site(self, site): self.site = site
    def get_route(self): return self.route
    def set_route(self, route): self.route = route
    def get_doseQuantity(self): return self.doseQuantity
    def set_doseQuantity(self, doseQuantity): self.doseQuantity = doseQuantity
    def get_explanation(self): return self.explanation
    def set_explanation(self, explanation): self.explanation = explanation
    def get_reaction(self): return self.reaction
    def set_reaction(self, reaction): self.reaction = reaction
    def add_reaction(self, value): self.reaction.append(value)
    def insert_reaction(self, index, value): self.reaction[index] = value
    def get_vaccinationProtocol(self): return self.vaccinationProtocol
    def set_vaccinationProtocol(self, vaccinationProtocol): self.vaccinationProtocol = vaccinationProtocol
    def add_vaccinationProtocol(self, value): self.vaccinationProtocol.append(value)
    def insert_vaccinationProtocol(self, index, value): self.vaccinationProtocol[index] = value
    def hasContent_(self):
        if (
            self.identifier or
            self.date is not None or
            self.vaccineType is not None or
            self.subject is not None or
            self.refusedIndicator is not None or
            self.reported is not None or
            self.performer is not None or
            self.requester is not None or
            self.manufacturer is not None or
            self.location is not None or
            self.lotNumber is not None or
            self.expirationDate is not None or
            self.site is not None or
            self.route is not None or
            self.doseQuantity is not None or
            self.explanation is not None or
            self.reaction or
            self.vaccinationProtocol or
            super(Immunization, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Immunization', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Immunization')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Immunization', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Immunization'):
        super(Immunization, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Immunization')
    def exportChildren(self, outfile, level, namespace_='', name_='Immunization', fromsubclass_=False, pretty_print=True):
        super(Immunization, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for identifier_ in self.identifier:
            identifier_.export(outfile, level, namespace_, name_='identifier', pretty_print=pretty_print)
        if self.date is not None:
            self.date.export(outfile, level, namespace_, name_='date', pretty_print=pretty_print)
        if self.vaccineType is not None:
            self.vaccineType.export(outfile, level, namespace_, name_='vaccineType', pretty_print=pretty_print)
        if self.subject is not None:
            self.subject.export(outfile, level, namespace_, name_='subject', pretty_print=pretty_print)
        if self.refusedIndicator is not None:
            self.refusedIndicator.export(outfile, level, namespace_, name_='refusedIndicator', pretty_print=pretty_print)
        if self.reported is not None:
            self.reported.export(outfile, level, namespace_, name_='reported', pretty_print=pretty_print)
        if self.performer is not None:
            self.performer.export(outfile, level, namespace_, name_='performer', pretty_print=pretty_print)
        if self.requester is not None:
            self.requester.export(outfile, level, namespace_, name_='requester', pretty_print=pretty_print)
        if self.manufacturer is not None:
            self.manufacturer.export(outfile, level, namespace_, name_='manufacturer', pretty_print=pretty_print)
        if self.location is not None:
            self.location.export(outfile, level, namespace_, name_='location', pretty_print=pretty_print)
        if self.lotNumber is not None:
            self.lotNumber.export(outfile, level, namespace_, name_='lotNumber', pretty_print=pretty_print)
        if self.expirationDate is not None:
            self.expirationDate.export(outfile, level, namespace_, name_='expirationDate', pretty_print=pretty_print)
        if self.site is not None:
            self.site.export(outfile, level, namespace_, name_='site', pretty_print=pretty_print)
        if self.route is not None:
            self.route.export(outfile, level, namespace_, name_='route', pretty_print=pretty_print)
        if self.doseQuantity is not None:
            self.doseQuantity.export(outfile, level, namespace_, name_='doseQuantity', pretty_print=pretty_print)
        if self.explanation is not None:
            self.explanation.export(outfile, level, namespace_, name_='explanation', pretty_print=pretty_print)
        for reaction_ in self.reaction:
            reaction_.export(outfile, level, namespace_, name_='reaction', pretty_print=pretty_print)
        for vaccinationProtocol_ in self.vaccinationProtocol:
            vaccinationProtocol_.export(outfile, level, namespace_, name_='vaccinationProtocol', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Immunization', mapping_=None):
        element = super(Immunization, self).to_etree(parent_element, name_, mapping_)
        for identifier_ in self.identifier:
            identifier_.to_etree(element, name_='identifier', mapping_=mapping_)
        if self.date is not None:
            date_ = self.date
            date_.to_etree(element, name_='date', mapping_=mapping_)
        if self.vaccineType is not None:
            vaccineType_ = self.vaccineType
            vaccineType_.to_etree(element, name_='vaccineType', mapping_=mapping_)
        if self.subject is not None:
            subject_ = self.subject
            subject_.to_etree(element, name_='subject', mapping_=mapping_)
        if self.refusedIndicator is not None:
            refusedIndicator_ = self.refusedIndicator
            refusedIndicator_.to_etree(element, name_='refusedIndicator', mapping_=mapping_)
        if self.reported is not None:
            reported_ = self.reported
            reported_.to_etree(element, name_='reported', mapping_=mapping_)
        if self.performer is not None:
            performer_ = self.performer
            performer_.to_etree(element, name_='performer', mapping_=mapping_)
        if self.requester is not None:
            requester_ = self.requester
            requester_.to_etree(element, name_='requester', mapping_=mapping_)
        if self.manufacturer is not None:
            manufacturer_ = self.manufacturer
            manufacturer_.to_etree(element, name_='manufacturer', mapping_=mapping_)
        if self.location is not None:
            location_ = self.location
            location_.to_etree(element, name_='location', mapping_=mapping_)
        if self.lotNumber is not None:
            lotNumber_ = self.lotNumber
            lotNumber_.to_etree(element, name_='lotNumber', mapping_=mapping_)
        if self.expirationDate is not None:
            expirationDate_ = self.expirationDate
            expirationDate_.to_etree(element, name_='expirationDate', mapping_=mapping_)
        if self.site is not None:
            site_ = self.site
            site_.to_etree(element, name_='site', mapping_=mapping_)
        if self.route is not None:
            route_ = self.route
            route_.to_etree(element, name_='route', mapping_=mapping_)
        if self.doseQuantity is not None:
            doseQuantity_ = self.doseQuantity
            doseQuantity_.to_etree(element, name_='doseQuantity', mapping_=mapping_)
        if self.explanation is not None:
            explanation_ = self.explanation
            explanation_.to_etree(element, name_='explanation', mapping_=mapping_)
        for reaction_ in self.reaction:
            reaction_.to_etree(element, name_='reaction', mapping_=mapping_)
        for vaccinationProtocol_ in self.vaccinationProtocol:
            vaccinationProtocol_.to_etree(element, name_='vaccinationProtocol', mapping_=mapping_)
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
        super(Immunization, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'identifier':
            obj_ = Identifier.factory()
            obj_.build(child_)
            self.identifier.append(obj_)
            obj_.original_tagname_ = 'identifier'
        elif nodeName_ == 'date':
            obj_ = dateTime.factory()
            obj_.build(child_)
            self.date = obj_
            obj_.original_tagname_ = 'date'
        elif nodeName_ == 'vaccineType':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.vaccineType = obj_
            obj_.original_tagname_ = 'vaccineType'
        elif nodeName_ == 'subject':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.subject = obj_
            obj_.original_tagname_ = 'subject'
        elif nodeName_ == 'refusedIndicator':
            obj_ = boolean.factory()
            obj_.build(child_)
            self.refusedIndicator = obj_
            obj_.original_tagname_ = 'refusedIndicator'
        elif nodeName_ == 'reported':
            obj_ = boolean.factory()
            obj_.build(child_)
            self.reported = obj_
            obj_.original_tagname_ = 'reported'
        elif nodeName_ == 'performer':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.performer = obj_
            obj_.original_tagname_ = 'performer'
        elif nodeName_ == 'requester':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.requester = obj_
            obj_.original_tagname_ = 'requester'
        elif nodeName_ == 'manufacturer':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.manufacturer = obj_
            obj_.original_tagname_ = 'manufacturer'
        elif nodeName_ == 'location':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.location = obj_
            obj_.original_tagname_ = 'location'
        elif nodeName_ == 'lotNumber':
            obj_ = string.factory()
            obj_.build(child_)
            self.lotNumber = obj_
            obj_.original_tagname_ = 'lotNumber'
        elif nodeName_ == 'expirationDate':
            obj_ = date.factory()
            obj_.build(child_)
            self.expirationDate = obj_
            obj_.original_tagname_ = 'expirationDate'
        elif nodeName_ == 'site':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.site = obj_
            obj_.original_tagname_ = 'site'
        elif nodeName_ == 'route':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.route = obj_
            obj_.original_tagname_ = 'route'
        elif nodeName_ == 'doseQuantity':
            obj_ = Quantity.factory()
            obj_.build(child_)
            self.doseQuantity = obj_
            obj_.original_tagname_ = 'doseQuantity'
        elif nodeName_ == 'explanation':
            obj_ = Immunization_Explanation.factory()
            obj_.build(child_)
            self.explanation = obj_
            obj_.original_tagname_ = 'explanation'
        elif nodeName_ == 'reaction':
            obj_ = Immunization_Reaction.factory()
            obj_.build(child_)
            self.reaction.append(obj_)
            obj_.original_tagname_ = 'reaction'
        elif nodeName_ == 'vaccinationProtocol':
            obj_ = Immunization_VaccinationProtocol.factory()
            obj_.build(child_)
            self.vaccinationProtocol.append(obj_)
            obj_.original_tagname_ = 'vaccinationProtocol'
        super(Immunization, self).buildChildren(child_, node, nodeName_, True)
# end class Immunization


class Immunization_Explanation(BackboneElement):
    """Immunization event information."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, reason=None, refusalReason=None):
        self.original_tagname_ = None
        super(Immunization_Explanation, self).__init__(id, extension, modifierExtension, )
        if reason is None:
            self.reason = []
        else:
            self.reason = reason
        if refusalReason is None:
            self.refusalReason = []
        else:
            self.refusalReason = refusalReason
    def factory(*args_, **kwargs_):
        if Immunization_Explanation.subclass:
            return Immunization_Explanation.subclass(*args_, **kwargs_)
        else:
            return Immunization_Explanation(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_reason(self): return self.reason
    def set_reason(self, reason): self.reason = reason
    def add_reason(self, value): self.reason.append(value)
    def insert_reason(self, index, value): self.reason[index] = value
    def get_refusalReason(self): return self.refusalReason
    def set_refusalReason(self, refusalReason): self.refusalReason = refusalReason
    def add_refusalReason(self, value): self.refusalReason.append(value)
    def insert_refusalReason(self, index, value): self.refusalReason[index] = value
    def hasContent_(self):
        if (
            self.reason or
            self.refusalReason or
            super(Immunization_Explanation, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Immunization.Explanation', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Immunization.Explanation')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Immunization.Explanation', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Immunization.Explanation'):
        super(Immunization_Explanation, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Immunization.Explanation')
    def exportChildren(self, outfile, level, namespace_='', name_='Immunization.Explanation', fromsubclass_=False, pretty_print=True):
        super(Immunization_Explanation, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for reason_ in self.reason:
            reason_.export(outfile, level, namespace_, name_='reason', pretty_print=pretty_print)
        for refusalReason_ in self.refusalReason:
            refusalReason_.export(outfile, level, namespace_, name_='refusalReason', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Immunization.Explanation', mapping_=None):
        element = super(Immunization_Explanation, self).to_etree(parent_element, name_, mapping_)
        for reason_ in self.reason:
            reason_.to_etree(element, name_='reason', mapping_=mapping_)
        for refusalReason_ in self.refusalReason:
            refusalReason_.to_etree(element, name_='refusalReason', mapping_=mapping_)
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
        super(Immunization_Explanation, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'reason':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.reason.append(obj_)
            obj_.original_tagname_ = 'reason'
        elif nodeName_ == 'refusalReason':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.refusalReason.append(obj_)
            obj_.original_tagname_ = 'refusalReason'
        super(Immunization_Explanation, self).buildChildren(child_, node, nodeName_, True)
# end class Immunization_Explanation


class Immunization_Reaction(BackboneElement):
    """Immunization event information."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, date=None, detail=None, reported=None):
        self.original_tagname_ = None
        super(Immunization_Reaction, self).__init__(id, extension, modifierExtension, )
        self.date = date
        self.detail = detail
        self.reported = reported
    def factory(*args_, **kwargs_):
        if Immunization_Reaction.subclass:
            return Immunization_Reaction.subclass(*args_, **kwargs_)
        else:
            return Immunization_Reaction(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_date(self): return self.date
    def set_date(self, date): self.date = date
    def get_detail(self): return self.detail
    def set_detail(self, detail): self.detail = detail
    def get_reported(self): return self.reported
    def set_reported(self, reported): self.reported = reported
    def hasContent_(self):
        if (
            self.date is not None or
            self.detail is not None or
            self.reported is not None or
            super(Immunization_Reaction, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Immunization.Reaction', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Immunization.Reaction')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Immunization.Reaction', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Immunization.Reaction'):
        super(Immunization_Reaction, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Immunization.Reaction')
    def exportChildren(self, outfile, level, namespace_='', name_='Immunization.Reaction', fromsubclass_=False, pretty_print=True):
        super(Immunization_Reaction, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.date is not None:
            self.date.export(outfile, level, namespace_, name_='date', pretty_print=pretty_print)
        if self.detail is not None:
            self.detail.export(outfile, level, namespace_, name_='detail', pretty_print=pretty_print)
        if self.reported is not None:
            self.reported.export(outfile, level, namespace_, name_='reported', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Immunization.Reaction', mapping_=None):
        element = super(Immunization_Reaction, self).to_etree(parent_element, name_, mapping_)
        if self.date is not None:
            date_ = self.date
            date_.to_etree(element, name_='date', mapping_=mapping_)
        if self.detail is not None:
            detail_ = self.detail
            detail_.to_etree(element, name_='detail', mapping_=mapping_)
        if self.reported is not None:
            reported_ = self.reported
            reported_.to_etree(element, name_='reported', mapping_=mapping_)
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
        super(Immunization_Reaction, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'date':
            obj_ = dateTime.factory()
            obj_.build(child_)
            self.date = obj_
            obj_.original_tagname_ = 'date'
        elif nodeName_ == 'detail':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.detail = obj_
            obj_.original_tagname_ = 'detail'
        elif nodeName_ == 'reported':
            obj_ = boolean.factory()
            obj_.build(child_)
            self.reported = obj_
            obj_.original_tagname_ = 'reported'
        super(Immunization_Reaction, self).buildChildren(child_, node, nodeName_, True)
# end class Immunization_Reaction


class Immunization_VaccinationProtocol(BackboneElement):
    """Immunization event information."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, doseSequence=None, description=None, authority=None, series=None, seriesDoses=None, doseTarget=None, doseStatus=None, doseStatusReason=None):
        self.original_tagname_ = None
        super(Immunization_VaccinationProtocol, self).__init__(id, extension, modifierExtension, )
        self.doseSequence = doseSequence
        self.description = description
        self.authority = authority
        self.series = series
        self.seriesDoses = seriesDoses
        self.doseTarget = doseTarget
        self.doseStatus = doseStatus
        self.doseStatusReason = doseStatusReason
    def factory(*args_, **kwargs_):
        if Immunization_VaccinationProtocol.subclass:
            return Immunization_VaccinationProtocol.subclass(*args_, **kwargs_)
        else:
            return Immunization_VaccinationProtocol(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_doseSequence(self): return self.doseSequence
    def set_doseSequence(self, doseSequence): self.doseSequence = doseSequence
    def get_description(self): return self.description
    def set_description(self, description): self.description = description
    def get_authority(self): return self.authority
    def set_authority(self, authority): self.authority = authority
    def get_series(self): return self.series
    def set_series(self, series): self.series = series
    def get_seriesDoses(self): return self.seriesDoses
    def set_seriesDoses(self, seriesDoses): self.seriesDoses = seriesDoses
    def get_doseTarget(self): return self.doseTarget
    def set_doseTarget(self, doseTarget): self.doseTarget = doseTarget
    def get_doseStatus(self): return self.doseStatus
    def set_doseStatus(self, doseStatus): self.doseStatus = doseStatus
    def get_doseStatusReason(self): return self.doseStatusReason
    def set_doseStatusReason(self, doseStatusReason): self.doseStatusReason = doseStatusReason
    def hasContent_(self):
        if (
            self.doseSequence is not None or
            self.description is not None or
            self.authority is not None or
            self.series is not None or
            self.seriesDoses is not None or
            self.doseTarget is not None or
            self.doseStatus is not None or
            self.doseStatusReason is not None or
            super(Immunization_VaccinationProtocol, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Immunization.VaccinationProtocol', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Immunization.VaccinationProtocol')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Immunization.VaccinationProtocol', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Immunization.VaccinationProtocol'):
        super(Immunization_VaccinationProtocol, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Immunization.VaccinationProtocol')
    def exportChildren(self, outfile, level, namespace_='', name_='Immunization.VaccinationProtocol', fromsubclass_=False, pretty_print=True):
        super(Immunization_VaccinationProtocol, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
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
        if self.seriesDoses is not None:
            self.seriesDoses.export(outfile, level, namespace_, name_='seriesDoses', pretty_print=pretty_print)
        if self.doseTarget is not None:
            self.doseTarget.export(outfile, level, namespace_, name_='doseTarget', pretty_print=pretty_print)
        if self.doseStatus is not None:
            self.doseStatus.export(outfile, level, namespace_, name_='doseStatus', pretty_print=pretty_print)
        if self.doseStatusReason is not None:
            self.doseStatusReason.export(outfile, level, namespace_, name_='doseStatusReason', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Immunization.VaccinationProtocol', mapping_=None):
        element = super(Immunization_VaccinationProtocol, self).to_etree(parent_element, name_, mapping_)
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
        if self.seriesDoses is not None:
            seriesDoses_ = self.seriesDoses
            seriesDoses_.to_etree(element, name_='seriesDoses', mapping_=mapping_)
        if self.doseTarget is not None:
            doseTarget_ = self.doseTarget
            doseTarget_.to_etree(element, name_='doseTarget', mapping_=mapping_)
        if self.doseStatus is not None:
            doseStatus_ = self.doseStatus
            doseStatus_.to_etree(element, name_='doseStatus', mapping_=mapping_)
        if self.doseStatusReason is not None:
            doseStatusReason_ = self.doseStatusReason
            doseStatusReason_.to_etree(element, name_='doseStatusReason', mapping_=mapping_)
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
        super(Immunization_VaccinationProtocol, self).buildAttributes(node, attrs, already_processed)
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
        elif nodeName_ == 'seriesDoses':
            obj_ = integer.factory()
            obj_.build(child_)
            self.seriesDoses = obj_
            obj_.original_tagname_ = 'seriesDoses'
        elif nodeName_ == 'doseTarget':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.doseTarget = obj_
            obj_.original_tagname_ = 'doseTarget'
        elif nodeName_ == 'doseStatus':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.doseStatus = obj_
            obj_.original_tagname_ = 'doseStatus'
        elif nodeName_ == 'doseStatusReason':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.doseStatusReason = obj_
            obj_.original_tagname_ = 'doseStatusReason'
        super(Immunization_VaccinationProtocol, self).buildChildren(child_, node, nodeName_, True)
# end class Immunization_VaccinationProtocol
