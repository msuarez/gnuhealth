from .base_classes import *
from .support_functions import *


class Encounter(Resource):
    """An interaction between a patient and healthcare provider(s) for the
    purpose of providing healthcare service(s) or assessing the
    health status of a patient.If the element is present, it must
    have either a @value, an @id, or extensions"""
    subclass = None
    superclass = Resource
    def __init__(self, id=None, extension=None, modifierExtension=None, language=None, text=None, contained=None, identifier=None, status=None, class_=None, type_=None, subject=None, participant=None, period=None, length=None, reason=None, indication=None, priority=None, hospitalization=None, location=None, serviceProvider=None, partOf=None):
        self.original_tagname_ = None
        super(Encounter, self).__init__(id, extension, modifierExtension, language, text, contained, )
        if identifier is None:
            self.identifier = []
        else:
            self.identifier = identifier
        self.status = status
        self.class_ = class_
        if type_ is None:
            self.type_ = []
        else:
            self.type_ = type_
        self.subject = subject
        if participant is None:
            self.participant = []
        else:
            self.participant = participant
        self.period = period
        self.length = length
        self.reason = reason
        self.indication = indication
        self.priority = priority
        self.hospitalization = hospitalization
        if location is None:
            self.location = []
        else:
            self.location = location
        self.serviceProvider = serviceProvider
        self.partOf = partOf
    def factory(*args_, **kwargs_):
        if Encounter.subclass:
            return Encounter.subclass(*args_, **kwargs_)
        else:
            return Encounter(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_identifier(self): return self.identifier
    def set_identifier(self, identifier): self.identifier = identifier
    def add_identifier(self, value): self.identifier.append(value)
    def insert_identifier(self, index, value): self.identifier[index] = value
    def get_status(self): return self.status
    def set_status(self, status): self.status = status
    def get_class(self): return self.class_
    def set_class(self, class_): self.class_ = class_
    def get_type(self): return self.type_
    def set_type(self, type_): self.type_ = type_
    def add_type(self, value): self.type_.append(value)
    def insert_type(self, index, value): self.type_[index] = value
    def get_subject(self): return self.subject
    def set_subject(self, subject): self.subject = subject
    def get_participant(self): return self.participant
    def set_participant(self, participant): self.participant = participant
    def add_participant(self, value): self.participant.append(value)
    def insert_participant(self, index, value): self.participant[index] = value
    def get_period(self): return self.period
    def set_period(self, period): self.period = period
    def get_length(self): return self.length
    def set_length(self, length): self.length = length
    def get_reason(self): return self.reason
    def set_reason(self, reason): self.reason = reason
    def get_indication(self): return self.indication
    def set_indication(self, indication): self.indication = indication
    def get_priority(self): return self.priority
    def set_priority(self, priority): self.priority = priority
    def get_hospitalization(self): return self.hospitalization
    def set_hospitalization(self, hospitalization): self.hospitalization = hospitalization
    def get_location(self): return self.location
    def set_location(self, location): self.location = location
    def add_location(self, value): self.location.append(value)
    def insert_location(self, index, value): self.location[index] = value
    def get_serviceProvider(self): return self.serviceProvider
    def set_serviceProvider(self, serviceProvider): self.serviceProvider = serviceProvider
    def get_partOf(self): return self.partOf
    def set_partOf(self, partOf): self.partOf = partOf
    def hasContent_(self):
        if (
            self.identifier or
            self.status is not None or
            self.class_ is not None or
            self.type_ or
            self.subject is not None or
            self.participant or
            self.period is not None or
            self.length is not None or
            self.reason is not None or
            self.indication is not None or
            self.priority is not None or
            self.hospitalization is not None or
            self.location or
            self.serviceProvider is not None or
            self.partOf is not None or
            super(Encounter, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Encounter', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Encounter')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Encounter', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Encounter'):
        super(Encounter, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Encounter')
    def exportChildren(self, outfile, level, namespace_='', name_='Encounter', fromsubclass_=False, pretty_print=True):
        super(Encounter, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for identifier_ in self.identifier:
            identifier_.export(outfile, level, namespace_, name_='identifier', pretty_print=pretty_print)
        if self.status is not None:
            self.status.export(outfile, level, namespace_, name_='status', pretty_print=pretty_print)
        if self.class_ is not None:
            self.class_.export(outfile, level, namespace_, name_='class', pretty_print=pretty_print)
        for type_ in self.type_:
            type_.export(outfile, level, namespace_, name_='type', pretty_print=pretty_print)
        if self.subject is not None:
            self.subject.export(outfile, level, namespace_, name_='subject', pretty_print=pretty_print)
        for participant_ in self.participant:
            participant_.export(outfile, level, namespace_, name_='participant', pretty_print=pretty_print)
        if self.period is not None:
            self.period.export(outfile, level, namespace_, name_='period', pretty_print=pretty_print)
        if self.length is not None:
            self.length.export(outfile, level, namespace_, name_='length', pretty_print=pretty_print)
        if self.reason is not None:
            self.reason.export(outfile, level, namespace_, name_='reason', pretty_print=pretty_print)
        if self.indication is not None:
            self.indication.export(outfile, level, namespace_, name_='indication', pretty_print=pretty_print)
        if self.priority is not None:
            self.priority.export(outfile, level, namespace_, name_='priority', pretty_print=pretty_print)
        if self.hospitalization is not None:
            self.hospitalization.export(outfile, level, namespace_, name_='hospitalization', pretty_print=pretty_print)
        for location_ in self.location:
            location_.export(outfile, level, namespace_, name_='location', pretty_print=pretty_print)
        if self.serviceProvider is not None:
            self.serviceProvider.export(outfile, level, namespace_, name_='serviceProvider', pretty_print=pretty_print)
        if self.partOf is not None:
            self.partOf.export(outfile, level, namespace_, name_='partOf', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Encounter', mapping_=None):
        element = super(Encounter, self).to_etree(parent_element, name_, mapping_)
        for identifier_ in self.identifier:
            identifier_.to_etree(element, name_='identifier', mapping_=mapping_)
        if self.status is not None:
            status_ = self.status
            status_.to_etree(element, name_='status', mapping_=mapping_)
        if self.class_ is not None:
            class__ = self.class_
            class__.to_etree(element, name_='class', mapping_=mapping_)
        for type__ in self.type_:
            type__.to_etree(element, name_='type', mapping_=mapping_)
        if self.subject is not None:
            subject_ = self.subject
            subject_.to_etree(element, name_='subject', mapping_=mapping_)
        for participant_ in self.participant:
            participant_.to_etree(element, name_='participant', mapping_=mapping_)
        if self.period is not None:
            period_ = self.period
            period_.to_etree(element, name_='period', mapping_=mapping_)
        if self.length is not None:
            length_ = self.length
            length_.to_etree(element, name_='length', mapping_=mapping_)
        if self.reason is not None:
            reason_ = self.reason
            reason_.to_etree(element, name_='reason', mapping_=mapping_)
        if self.indication is not None:
            indication_ = self.indication
            indication_.to_etree(element, name_='indication', mapping_=mapping_)
        if self.priority is not None:
            priority_ = self.priority
            priority_.to_etree(element, name_='priority', mapping_=mapping_)
        if self.hospitalization is not None:
            hospitalization_ = self.hospitalization
            hospitalization_.to_etree(element, name_='hospitalization', mapping_=mapping_)
        for location_ in self.location:
            location_.to_etree(element, name_='location', mapping_=mapping_)
        if self.serviceProvider is not None:
            serviceProvider_ = self.serviceProvider
            serviceProvider_.to_etree(element, name_='serviceProvider', mapping_=mapping_)
        if self.partOf is not None:
            partOf_ = self.partOf
            partOf_.to_etree(element, name_='partOf', mapping_=mapping_)
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
        super(Encounter, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'identifier':
            obj_ = Identifier.factory()
            obj_.build(child_)
            self.identifier.append(obj_)
            obj_.original_tagname_ = 'identifier'
        elif nodeName_ == 'status':
            obj_ = EncounterState.factory()
            obj_.build(child_)
            self.status = obj_
            obj_.original_tagname_ = 'status'
        elif nodeName_ == 'class':
            obj_ = EncounterClass.factory()
            obj_.build(child_)
            self.class_ = obj_
            obj_.original_tagname_ = 'class'
        elif nodeName_ == 'type':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.type_.append(obj_)
            obj_.original_tagname_ = 'type'
        elif nodeName_ == 'subject':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.subject = obj_
            obj_.original_tagname_ = 'subject'
        elif nodeName_ == 'participant':
            obj_ = Encounter_Participant.factory()
            obj_.build(child_)
            self.participant.append(obj_)
            obj_.original_tagname_ = 'participant'
        elif nodeName_ == 'period':
            obj_ = Period.factory()
            obj_.build(child_)
            self.period = obj_
            obj_.original_tagname_ = 'period'
        elif nodeName_ == 'length':
            obj_ = Duration.factory()
            obj_.build(child_)
            self.length = obj_
            obj_.original_tagname_ = 'length'
        elif nodeName_ == 'reason':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.reason = obj_
            obj_.original_tagname_ = 'reason'
        elif nodeName_ == 'indication':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.indication = obj_
            obj_.original_tagname_ = 'indication'
        elif nodeName_ == 'priority':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.priority = obj_
            obj_.original_tagname_ = 'priority'
        elif nodeName_ == 'hospitalization':
            obj_ = Encounter_Hospitalization.factory()
            obj_.build(child_)
            self.hospitalization = obj_
            obj_.original_tagname_ = 'hospitalization'
        elif nodeName_ == 'location':
            obj_ = Encounter_Location.factory()
            obj_.build(child_)
            self.location.append(obj_)
            obj_.original_tagname_ = 'location'
        elif nodeName_ == 'serviceProvider':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.serviceProvider = obj_
            obj_.original_tagname_ = 'serviceProvider'
        elif nodeName_ == 'partOf':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.partOf = obj_
            obj_.original_tagname_ = 'partOf'
        super(Encounter, self).buildChildren(child_, node, nodeName_, True)
# end class Encounter


class Encounter_Participant(BackboneElement):
    """An interaction between a patient and healthcare provider(s) for the
    purpose of providing healthcare service(s) or assessing the
    health status of a patient."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, type_=None, individual=None):
        self.original_tagname_ = None
        super(Encounter_Participant, self).__init__(id, extension, modifierExtension, )
        if type_ is None:
            self.type_ = []
        else:
            self.type_ = type_
        self.individual = individual
    def factory(*args_, **kwargs_):
        if Encounter_Participant.subclass:
            return Encounter_Participant.subclass(*args_, **kwargs_)
        else:
            return Encounter_Participant(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_type(self): return self.type_
    def set_type(self, type_): self.type_ = type_
    def add_type(self, value): self.type_.append(value)
    def insert_type(self, index, value): self.type_[index] = value
    def get_individual(self): return self.individual
    def set_individual(self, individual): self.individual = individual
    def hasContent_(self):
        if (
            self.type_ or
            self.individual is not None or
            super(Encounter_Participant, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Encounter.Participant', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Encounter.Participant')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Encounter.Participant', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Encounter.Participant'):
        super(Encounter_Participant, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Encounter.Participant')
    def exportChildren(self, outfile, level, namespace_='', name_='Encounter.Participant', fromsubclass_=False, pretty_print=True):
        super(Encounter_Participant, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for type_ in self.type_:
            type_.export(outfile, level, namespace_, name_='type', pretty_print=pretty_print)
        if self.individual is not None:
            self.individual.export(outfile, level, namespace_, name_='individual', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Encounter.Participant', mapping_=None):
        element = super(Encounter_Participant, self).to_etree(parent_element, name_, mapping_)
        for type__ in self.type_:
            type__.to_etree(element, name_='type', mapping_=mapping_)
        if self.individual is not None:
            individual_ = self.individual
            individual_.to_etree(element, name_='individual', mapping_=mapping_)
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
        super(Encounter_Participant, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'type':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.type_.append(obj_)
            obj_.original_tagname_ = 'type'
        elif nodeName_ == 'individual':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.individual = obj_
            obj_.original_tagname_ = 'individual'
        super(Encounter_Participant, self).buildChildren(child_, node, nodeName_, True)
# end class Encounter_Participant


class Encounter_Hospitalization(BackboneElement):
    """An interaction between a patient and healthcare provider(s) for the
    purpose of providing healthcare service(s) or assessing the
    health status of a patient."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, preAdmissionIdentifier=None, origin=None, admitSource=None, period=None, accomodation=None, diet=None, specialCourtesy=None, specialArrangement=None, destination=None, dischargeDisposition=None, dischargeDiagnosis=None, reAdmission=None):
        self.original_tagname_ = None
        super(Encounter_Hospitalization, self).__init__(id, extension, modifierExtension, )
        self.preAdmissionIdentifier = preAdmissionIdentifier
        self.origin = origin
        self.admitSource = admitSource
        self.period = period
        if accomodation is None:
            self.accomodation = []
        else:
            self.accomodation = accomodation
        self.diet = diet
        if specialCourtesy is None:
            self.specialCourtesy = []
        else:
            self.specialCourtesy = specialCourtesy
        if specialArrangement is None:
            self.specialArrangement = []
        else:
            self.specialArrangement = specialArrangement
        self.destination = destination
        self.dischargeDisposition = dischargeDisposition
        self.dischargeDiagnosis = dischargeDiagnosis
        self.reAdmission = reAdmission
    def factory(*args_, **kwargs_):
        if Encounter_Hospitalization.subclass:
            return Encounter_Hospitalization.subclass(*args_, **kwargs_)
        else:
            return Encounter_Hospitalization(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_preAdmissionIdentifier(self): return self.preAdmissionIdentifier
    def set_preAdmissionIdentifier(self, preAdmissionIdentifier): self.preAdmissionIdentifier = preAdmissionIdentifier
    def get_origin(self): return self.origin
    def set_origin(self, origin): self.origin = origin
    def get_admitSource(self): return self.admitSource
    def set_admitSource(self, admitSource): self.admitSource = admitSource
    def get_period(self): return self.period
    def set_period(self, period): self.period = period
    def get_accomodation(self): return self.accomodation
    def set_accomodation(self, accomodation): self.accomodation = accomodation
    def add_accomodation(self, value): self.accomodation.append(value)
    def insert_accomodation(self, index, value): self.accomodation[index] = value
    def get_diet(self): return self.diet
    def set_diet(self, diet): self.diet = diet
    def get_specialCourtesy(self): return self.specialCourtesy
    def set_specialCourtesy(self, specialCourtesy): self.specialCourtesy = specialCourtesy
    def add_specialCourtesy(self, value): self.specialCourtesy.append(value)
    def insert_specialCourtesy(self, index, value): self.specialCourtesy[index] = value
    def get_specialArrangement(self): return self.specialArrangement
    def set_specialArrangement(self, specialArrangement): self.specialArrangement = specialArrangement
    def add_specialArrangement(self, value): self.specialArrangement.append(value)
    def insert_specialArrangement(self, index, value): self.specialArrangement[index] = value
    def get_destination(self): return self.destination
    def set_destination(self, destination): self.destination = destination
    def get_dischargeDisposition(self): return self.dischargeDisposition
    def set_dischargeDisposition(self, dischargeDisposition): self.dischargeDisposition = dischargeDisposition
    def get_dischargeDiagnosis(self): return self.dischargeDiagnosis
    def set_dischargeDiagnosis(self, dischargeDiagnosis): self.dischargeDiagnosis = dischargeDiagnosis
    def get_reAdmission(self): return self.reAdmission
    def set_reAdmission(self, reAdmission): self.reAdmission = reAdmission
    def hasContent_(self):
        if (
            self.preAdmissionIdentifier is not None or
            self.origin is not None or
            self.admitSource is not None or
            self.period is not None or
            self.accomodation or
            self.diet is not None or
            self.specialCourtesy or
            self.specialArrangement or
            self.destination is not None or
            self.dischargeDisposition is not None or
            self.dischargeDiagnosis is not None or
            self.reAdmission is not None or
            super(Encounter_Hospitalization, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Encounter.Hospitalization', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Encounter.Hospitalization')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Encounter.Hospitalization', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Encounter.Hospitalization'):
        super(Encounter_Hospitalization, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Encounter.Hospitalization')
    def exportChildren(self, outfile, level, namespace_='', name_='Encounter.Hospitalization', fromsubclass_=False, pretty_print=True):
        super(Encounter_Hospitalization, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.preAdmissionIdentifier is not None:
            self.preAdmissionIdentifier.export(outfile, level, namespace_, name_='preAdmissionIdentifier', pretty_print=pretty_print)
        if self.origin is not None:
            self.origin.export(outfile, level, namespace_, name_='origin', pretty_print=pretty_print)
        if self.admitSource is not None:
            self.admitSource.export(outfile, level, namespace_, name_='admitSource', pretty_print=pretty_print)
        if self.period is not None:
            self.period.export(outfile, level, namespace_, name_='period', pretty_print=pretty_print)
        for accomodation_ in self.accomodation:
            accomodation_.export(outfile, level, namespace_, name_='accomodation', pretty_print=pretty_print)
        if self.diet is not None:
            self.diet.export(outfile, level, namespace_, name_='diet', pretty_print=pretty_print)
        for specialCourtesy_ in self.specialCourtesy:
            specialCourtesy_.export(outfile, level, namespace_, name_='specialCourtesy', pretty_print=pretty_print)
        for specialArrangement_ in self.specialArrangement:
            specialArrangement_.export(outfile, level, namespace_, name_='specialArrangement', pretty_print=pretty_print)
        if self.destination is not None:
            self.destination.export(outfile, level, namespace_, name_='destination', pretty_print=pretty_print)
        if self.dischargeDisposition is not None:
            self.dischargeDisposition.export(outfile, level, namespace_, name_='dischargeDisposition', pretty_print=pretty_print)
        if self.dischargeDiagnosis is not None:
            self.dischargeDiagnosis.export(outfile, level, namespace_, name_='dischargeDiagnosis', pretty_print=pretty_print)
        if self.reAdmission is not None:
            self.reAdmission.export(outfile, level, namespace_, name_='reAdmission', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Encounter.Hospitalization', mapping_=None):
        element = super(Encounter_Hospitalization, self).to_etree(parent_element, name_, mapping_)
        if self.preAdmissionIdentifier is not None:
            preAdmissionIdentifier_ = self.preAdmissionIdentifier
            preAdmissionIdentifier_.to_etree(element, name_='preAdmissionIdentifier', mapping_=mapping_)
        if self.origin is not None:
            origin_ = self.origin
            origin_.to_etree(element, name_='origin', mapping_=mapping_)
        if self.admitSource is not None:
            admitSource_ = self.admitSource
            admitSource_.to_etree(element, name_='admitSource', mapping_=mapping_)
        if self.period is not None:
            period_ = self.period
            period_.to_etree(element, name_='period', mapping_=mapping_)
        for accomodation_ in self.accomodation:
            accomodation_.to_etree(element, name_='accomodation', mapping_=mapping_)
        if self.diet is not None:
            diet_ = self.diet
            diet_.to_etree(element, name_='diet', mapping_=mapping_)
        for specialCourtesy_ in self.specialCourtesy:
            specialCourtesy_.to_etree(element, name_='specialCourtesy', mapping_=mapping_)
        for specialArrangement_ in self.specialArrangement:
            specialArrangement_.to_etree(element, name_='specialArrangement', mapping_=mapping_)
        if self.destination is not None:
            destination_ = self.destination
            destination_.to_etree(element, name_='destination', mapping_=mapping_)
        if self.dischargeDisposition is not None:
            dischargeDisposition_ = self.dischargeDisposition
            dischargeDisposition_.to_etree(element, name_='dischargeDisposition', mapping_=mapping_)
        if self.dischargeDiagnosis is not None:
            dischargeDiagnosis_ = self.dischargeDiagnosis
            dischargeDiagnosis_.to_etree(element, name_='dischargeDiagnosis', mapping_=mapping_)
        if self.reAdmission is not None:
            reAdmission_ = self.reAdmission
            reAdmission_.to_etree(element, name_='reAdmission', mapping_=mapping_)
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
        super(Encounter_Hospitalization, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'preAdmissionIdentifier':
            obj_ = Identifier.factory()
            obj_.build(child_)
            self.preAdmissionIdentifier = obj_
            obj_.original_tagname_ = 'preAdmissionIdentifier'
        elif nodeName_ == 'origin':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.origin = obj_
            obj_.original_tagname_ = 'origin'
        elif nodeName_ == 'admitSource':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.admitSource = obj_
            obj_.original_tagname_ = 'admitSource'
        elif nodeName_ == 'period':
            obj_ = Period.factory()
            obj_.build(child_)
            self.period = obj_
            obj_.original_tagname_ = 'period'
        elif nodeName_ == 'accomodation':
            obj_ = Encounter_Accomodation.factory()
            obj_.build(child_)
            self.accomodation.append(obj_)
            obj_.original_tagname_ = 'accomodation'
        elif nodeName_ == 'diet':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.diet = obj_
            obj_.original_tagname_ = 'diet'
        elif nodeName_ == 'specialCourtesy':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.specialCourtesy.append(obj_)
            obj_.original_tagname_ = 'specialCourtesy'
        elif nodeName_ == 'specialArrangement':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.specialArrangement.append(obj_)
            obj_.original_tagname_ = 'specialArrangement'
        elif nodeName_ == 'destination':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.destination = obj_
            obj_.original_tagname_ = 'destination'
        elif nodeName_ == 'dischargeDisposition':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.dischargeDisposition = obj_
            obj_.original_tagname_ = 'dischargeDisposition'
        elif nodeName_ == 'dischargeDiagnosis':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.dischargeDiagnosis = obj_
            obj_.original_tagname_ = 'dischargeDiagnosis'
        elif nodeName_ == 'reAdmission':
            obj_ = boolean.factory()
            obj_.build(child_)
            self.reAdmission = obj_
            obj_.original_tagname_ = 'reAdmission'
        super(Encounter_Hospitalization, self).buildChildren(child_, node, nodeName_, True)
# end class Encounter_Hospitalization


class Encounter_Accomodation(BackboneElement):
    """An interaction between a patient and healthcare provider(s) for the
    purpose of providing healthcare service(s) or assessing the
    health status of a patient."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, bed=None, period=None):
        self.original_tagname_ = None
        super(Encounter_Accomodation, self).__init__(id, extension, modifierExtension, )
        self.bed = bed
        self.period = period
    def factory(*args_, **kwargs_):
        if Encounter_Accomodation.subclass:
            return Encounter_Accomodation.subclass(*args_, **kwargs_)
        else:
            return Encounter_Accomodation(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_bed(self): return self.bed
    def set_bed(self, bed): self.bed = bed
    def get_period(self): return self.period
    def set_period(self, period): self.period = period
    def hasContent_(self):
        if (
            self.bed is not None or
            self.period is not None or
            super(Encounter_Accomodation, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Encounter.Accomodation', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Encounter.Accomodation')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Encounter.Accomodation', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Encounter.Accomodation'):
        super(Encounter_Accomodation, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Encounter.Accomodation')
    def exportChildren(self, outfile, level, namespace_='', name_='Encounter.Accomodation', fromsubclass_=False, pretty_print=True):
        super(Encounter_Accomodation, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.bed is not None:
            self.bed.export(outfile, level, namespace_, name_='bed', pretty_print=pretty_print)
        if self.period is not None:
            self.period.export(outfile, level, namespace_, name_='period', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Encounter.Accomodation', mapping_=None):
        element = super(Encounter_Accomodation, self).to_etree(parent_element, name_, mapping_)
        if self.bed is not None:
            bed_ = self.bed
            bed_.to_etree(element, name_='bed', mapping_=mapping_)
        if self.period is not None:
            period_ = self.period
            period_.to_etree(element, name_='period', mapping_=mapping_)
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
        super(Encounter_Accomodation, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'bed':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.bed = obj_
            obj_.original_tagname_ = 'bed'
        elif nodeName_ == 'period':
            obj_ = Period.factory()
            obj_.build(child_)
            self.period = obj_
            obj_.original_tagname_ = 'period'
        super(Encounter_Accomodation, self).buildChildren(child_, node, nodeName_, True)
# end class Encounter_Accomodation


class Encounter_Location(BackboneElement):
    """An interaction between a patient and healthcare provider(s) for the
    purpose of providing healthcare service(s) or assessing the
    health status of a patient."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, location=None, period=None):
        self.original_tagname_ = None
        super(Encounter_Location, self).__init__(id, extension, modifierExtension, )
        self.location = location
        self.period = period
    def factory(*args_, **kwargs_):
        if Encounter_Location.subclass:
            return Encounter_Location.subclass(*args_, **kwargs_)
        else:
            return Encounter_Location(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_location(self): return self.location
    def set_location(self, location): self.location = location
    def get_period(self): return self.period
    def set_period(self, period): self.period = period
    def hasContent_(self):
        if (
            self.location is not None or
            self.period is not None or
            super(Encounter_Location, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Encounter.Location', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Encounter.Location')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Encounter.Location', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Encounter.Location'):
        super(Encounter_Location, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Encounter.Location')
    def exportChildren(self, outfile, level, namespace_='', name_='Encounter.Location', fromsubclass_=False, pretty_print=True):
        super(Encounter_Location, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.location is not None:
            self.location.export(outfile, level, namespace_, name_='location', pretty_print=pretty_print)
        if self.period is not None:
            self.period.export(outfile, level, namespace_, name_='period', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Encounter.Location', mapping_=None):
        element = super(Encounter_Location, self).to_etree(parent_element, name_, mapping_)
        if self.location is not None:
            location_ = self.location
            location_.to_etree(element, name_='location', mapping_=mapping_)
        if self.period is not None:
            period_ = self.period
            period_.to_etree(element, name_='period', mapping_=mapping_)
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
        super(Encounter_Location, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'location':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.location = obj_
            obj_.original_tagname_ = 'location'
        elif nodeName_ == 'period':
            obj_ = Period.factory()
            obj_.build(child_)
            self.period = obj_
            obj_.original_tagname_ = 'period'
        super(Encounter_Location, self).buildChildren(child_, node, nodeName_, True)
# end class Encounter_Location


class EncounterClass(Element):
    """Classification of the encounterIf the element is present, it must
    have either a @value, an @id, or extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(EncounterClass, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if EncounterClass.subclass:
            return EncounterClass.subclass(*args_, **kwargs_)
        else:
            return EncounterClass(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(EncounterClass, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='EncounterClass', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='EncounterClass')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='EncounterClass', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='EncounterClass'):
        super(EncounterClass, self).exportAttributes(outfile, level, already_processed, namespace_, name_='EncounterClass')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='EncounterClass', fromsubclass_=False, pretty_print=True):
        super(EncounterClass, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='EncounterClass', mapping_=None):
        element = super(EncounterClass, self).to_etree(parent_element, name_, mapping_)
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
        super(EncounterClass, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(EncounterClass, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class EncounterClass


class EncounterState(Element):
    """Current state of the encounterIf the element is present, it must
    have either a @value, an @id, or extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(EncounterState, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if EncounterState.subclass:
            return EncounterState.subclass(*args_, **kwargs_)
        else:
            return EncounterState(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(EncounterState, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='EncounterState', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='EncounterState')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='EncounterState', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='EncounterState'):
        super(EncounterState, self).exportAttributes(outfile, level, already_processed, namespace_, name_='EncounterState')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='EncounterState', fromsubclass_=False, pretty_print=True):
        super(EncounterState, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='EncounterState', mapping_=None):
        element = super(EncounterState, self).to_etree(parent_element, name_, mapping_)
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
        super(EncounterState, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(EncounterState, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class EncounterState
