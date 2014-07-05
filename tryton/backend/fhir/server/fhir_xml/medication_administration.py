from .base_classes import *
from .support_functions import *


class MedicationAdministration(Resource):
    """Describes the event of a patient being given a dose of a medication.
    This may be as simple as swallowing a tablet or it may be a long
    running infusion. Related resources tie this event to the
    authorizing prescription, and the specific encounter between
    patient and health care practitioner.If the element is present,
    it must have either a @value, an @id, or extensions"""
    subclass = None
    superclass = Resource
    def __init__(self, id=None, extension=None, modifierExtension=None, language=None, text=None, contained=None, identifier=None, status=None, patient=None, practitioner=None, encounter=None, prescription=None, wasNotGiven=None, reasonNotGiven=None, whenGiven=None, medication=None, device=None, dosage=None):
        self.original_tagname_ = None
        super(MedicationAdministration, self).__init__(id, extension, modifierExtension, language, text, contained, )
        if identifier is None:
            self.identifier = []
        else:
            self.identifier = identifier
        self.status = status
        self.patient = patient
        self.practitioner = practitioner
        self.encounter = encounter
        self.prescription = prescription
        self.wasNotGiven = wasNotGiven
        if reasonNotGiven is None:
            self.reasonNotGiven = []
        else:
            self.reasonNotGiven = reasonNotGiven
        self.whenGiven = whenGiven
        self.medication = medication
        if device is None:
            self.device = []
        else:
            self.device = device
        if dosage is None:
            self.dosage = []
        else:
            self.dosage = dosage
    def factory(*args_, **kwargs_):
        if MedicationAdministration.subclass:
            return MedicationAdministration.subclass(*args_, **kwargs_)
        else:
            return MedicationAdministration(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_identifier(self): return self.identifier
    def set_identifier(self, identifier): self.identifier = identifier
    def add_identifier(self, value): self.identifier.append(value)
    def insert_identifier(self, index, value): self.identifier[index] = value
    def get_status(self): return self.status
    def set_status(self, status): self.status = status
    def get_patient(self): return self.patient
    def set_patient(self, patient): self.patient = patient
    def get_practitioner(self): return self.practitioner
    def set_practitioner(self, practitioner): self.practitioner = practitioner
    def get_encounter(self): return self.encounter
    def set_encounter(self, encounter): self.encounter = encounter
    def get_prescription(self): return self.prescription
    def set_prescription(self, prescription): self.prescription = prescription
    def get_wasNotGiven(self): return self.wasNotGiven
    def set_wasNotGiven(self, wasNotGiven): self.wasNotGiven = wasNotGiven
    def get_reasonNotGiven(self): return self.reasonNotGiven
    def set_reasonNotGiven(self, reasonNotGiven): self.reasonNotGiven = reasonNotGiven
    def add_reasonNotGiven(self, value): self.reasonNotGiven.append(value)
    def insert_reasonNotGiven(self, index, value): self.reasonNotGiven[index] = value
    def get_whenGiven(self): return self.whenGiven
    def set_whenGiven(self, whenGiven): self.whenGiven = whenGiven
    def get_medication(self): return self.medication
    def set_medication(self, medication): self.medication = medication
    def get_device(self): return self.device
    def set_device(self, device): self.device = device
    def add_device(self, value): self.device.append(value)
    def insert_device(self, index, value): self.device[index] = value
    def get_dosage(self): return self.dosage
    def set_dosage(self, dosage): self.dosage = dosage
    def add_dosage(self, value): self.dosage.append(value)
    def insert_dosage(self, index, value): self.dosage[index] = value
    def hasContent_(self):
        if (
            self.identifier or
            self.status is not None or
            self.patient is not None or
            self.practitioner is not None or
            self.encounter is not None or
            self.prescription is not None or
            self.wasNotGiven is not None or
            self.reasonNotGiven or
            self.whenGiven is not None or
            self.medication is not None or
            self.device or
            self.dosage or
            super(MedicationAdministration, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='MedicationAdministration', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='MedicationAdministration')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='MedicationAdministration', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='MedicationAdministration'):
        super(MedicationAdministration, self).exportAttributes(outfile, level, already_processed, namespace_, name_='MedicationAdministration')
    def exportChildren(self, outfile, level, namespace_='', name_='MedicationAdministration', fromsubclass_=False, pretty_print=True):
        super(MedicationAdministration, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for identifier_ in self.identifier:
            identifier_.export(outfile, level, namespace_, name_='identifier', pretty_print=pretty_print)
        if self.status is not None:
            self.status.export(outfile, level, namespace_, name_='status', pretty_print=pretty_print)
        if self.patient is not None:
            self.patient.export(outfile, level, namespace_, name_='patient', pretty_print=pretty_print)
        if self.practitioner is not None:
            self.practitioner.export(outfile, level, namespace_, name_='practitioner', pretty_print=pretty_print)
        if self.encounter is not None:
            self.encounter.export(outfile, level, namespace_, name_='encounter', pretty_print=pretty_print)
        if self.prescription is not None:
            self.prescription.export(outfile, level, namespace_, name_='prescription', pretty_print=pretty_print)
        if self.wasNotGiven is not None:
            self.wasNotGiven.export(outfile, level, namespace_, name_='wasNotGiven', pretty_print=pretty_print)
        for reasonNotGiven_ in self.reasonNotGiven:
            reasonNotGiven_.export(outfile, level, namespace_, name_='reasonNotGiven', pretty_print=pretty_print)
        if self.whenGiven is not None:
            self.whenGiven.export(outfile, level, namespace_, name_='whenGiven', pretty_print=pretty_print)
        if self.medication is not None:
            self.medication.export(outfile, level, namespace_, name_='medication', pretty_print=pretty_print)
        for device_ in self.device:
            device_.export(outfile, level, namespace_, name_='device', pretty_print=pretty_print)
        for dosage_ in self.dosage:
            dosage_.export(outfile, level, namespace_, name_='dosage', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='MedicationAdministration', mapping_=None):
        element = super(MedicationAdministration, self).to_etree(parent_element, name_, mapping_)
        for identifier_ in self.identifier:
            identifier_.to_etree(element, name_='identifier', mapping_=mapping_)
        if self.status is not None:
            status_ = self.status
            status_.to_etree(element, name_='status', mapping_=mapping_)
        if self.patient is not None:
            patient_ = self.patient
            patient_.to_etree(element, name_='patient', mapping_=mapping_)
        if self.practitioner is not None:
            practitioner_ = self.practitioner
            practitioner_.to_etree(element, name_='practitioner', mapping_=mapping_)
        if self.encounter is not None:
            encounter_ = self.encounter
            encounter_.to_etree(element, name_='encounter', mapping_=mapping_)
        if self.prescription is not None:
            prescription_ = self.prescription
            prescription_.to_etree(element, name_='prescription', mapping_=mapping_)
        if self.wasNotGiven is not None:
            wasNotGiven_ = self.wasNotGiven
            wasNotGiven_.to_etree(element, name_='wasNotGiven', mapping_=mapping_)
        for reasonNotGiven_ in self.reasonNotGiven:
            reasonNotGiven_.to_etree(element, name_='reasonNotGiven', mapping_=mapping_)
        if self.whenGiven is not None:
            whenGiven_ = self.whenGiven
            whenGiven_.to_etree(element, name_='whenGiven', mapping_=mapping_)
        if self.medication is not None:
            medication_ = self.medication
            medication_.to_etree(element, name_='medication', mapping_=mapping_)
        for device_ in self.device:
            device_.to_etree(element, name_='device', mapping_=mapping_)
        for dosage_ in self.dosage:
            dosage_.to_etree(element, name_='dosage', mapping_=mapping_)
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
        super(MedicationAdministration, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'identifier':
            obj_ = Identifier.factory()
            obj_.build(child_)
            self.identifier.append(obj_)
            obj_.original_tagname_ = 'identifier'
        elif nodeName_ == 'status':
            obj_ = MedicationAdministrationStatus.factory()
            obj_.build(child_)
            self.status = obj_
            obj_.original_tagname_ = 'status'
        elif nodeName_ == 'patient':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.patient = obj_
            obj_.original_tagname_ = 'patient'
        elif nodeName_ == 'practitioner':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.practitioner = obj_
            obj_.original_tagname_ = 'practitioner'
        elif nodeName_ == 'encounter':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.encounter = obj_
            obj_.original_tagname_ = 'encounter'
        elif nodeName_ == 'prescription':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.prescription = obj_
            obj_.original_tagname_ = 'prescription'
        elif nodeName_ == 'wasNotGiven':
            obj_ = boolean.factory()
            obj_.build(child_)
            self.wasNotGiven = obj_
            obj_.original_tagname_ = 'wasNotGiven'
        elif nodeName_ == 'reasonNotGiven':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.reasonNotGiven.append(obj_)
            obj_.original_tagname_ = 'reasonNotGiven'
        elif nodeName_ == 'whenGiven':
            obj_ = Period.factory()
            obj_.build(child_)
            self.whenGiven = obj_
            obj_.original_tagname_ = 'whenGiven'
        elif nodeName_ == 'medication':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.medication = obj_
            obj_.original_tagname_ = 'medication'
        elif nodeName_ == 'device':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.device.append(obj_)
            obj_.original_tagname_ = 'device'
        elif nodeName_ == 'dosage':
            obj_ = MedicationAdministration_Dosage.factory()
            obj_.build(child_)
            self.dosage.append(obj_)
            obj_.original_tagname_ = 'dosage'
        super(MedicationAdministration, self).buildChildren(child_, node, nodeName_, True)
# end class MedicationAdministration


class MedicationAdministration_Dosage(BackboneElement):
    """Describes the event of a patient being given a dose of a medication.
    This may be as simple as swallowing a tablet or it may be a long
    running infusion. Related resources tie this event to the
    authorizing prescription, and the specific encounter between
    patient and health care practitioner.The timing schedule for
    giving the medication to the patient. This may be a single time
    point (using dateTime) or it may be a start and end dateTime
    (Period).If set to true or if specified as a CodeableConcept,
    indicates that the medication is only taken when needed within
    the specified schedule rather than at every scheduled dose. If a
    CodeableConcept is present, it indicates the pre-condition for
    taking the Medication."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, timingDateTime=None, timingPeriod=None, asNeededBoolean=None, asNeededCodeableConcept=None, site=None, route=None, method=None, quantity=None, rate=None, maxDosePerPeriod=None):
        self.original_tagname_ = None
        super(MedicationAdministration_Dosage, self).__init__(id, extension, modifierExtension, )
        self.timingDateTime = timingDateTime
        self.timingPeriod = timingPeriod
        self.asNeededBoolean = asNeededBoolean
        self.asNeededCodeableConcept = asNeededCodeableConcept
        self.site = site
        self.route = route
        self.method = method
        self.quantity = quantity
        self.rate = rate
        self.maxDosePerPeriod = maxDosePerPeriod
    def factory(*args_, **kwargs_):
        if MedicationAdministration_Dosage.subclass:
            return MedicationAdministration_Dosage.subclass(*args_, **kwargs_)
        else:
            return MedicationAdministration_Dosage(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_timingDateTime(self): return self.timingDateTime
    def set_timingDateTime(self, timingDateTime): self.timingDateTime = timingDateTime
    def get_timingPeriod(self): return self.timingPeriod
    def set_timingPeriod(self, timingPeriod): self.timingPeriod = timingPeriod
    def get_asNeededBoolean(self): return self.asNeededBoolean
    def set_asNeededBoolean(self, asNeededBoolean): self.asNeededBoolean = asNeededBoolean
    def get_asNeededCodeableConcept(self): return self.asNeededCodeableConcept
    def set_asNeededCodeableConcept(self, asNeededCodeableConcept): self.asNeededCodeableConcept = asNeededCodeableConcept
    def get_site(self): return self.site
    def set_site(self, site): self.site = site
    def get_route(self): return self.route
    def set_route(self, route): self.route = route
    def get_method(self): return self.method
    def set_method(self, method): self.method = method
    def get_quantity(self): return self.quantity
    def set_quantity(self, quantity): self.quantity = quantity
    def get_rate(self): return self.rate
    def set_rate(self, rate): self.rate = rate
    def get_maxDosePerPeriod(self): return self.maxDosePerPeriod
    def set_maxDosePerPeriod(self, maxDosePerPeriod): self.maxDosePerPeriod = maxDosePerPeriod
    def hasContent_(self):
        if (
            self.timingDateTime is not None or
            self.timingPeriod is not None or
            self.asNeededBoolean is not None or
            self.asNeededCodeableConcept is not None or
            self.site is not None or
            self.route is not None or
            self.method is not None or
            self.quantity is not None or
            self.rate is not None or
            self.maxDosePerPeriod is not None or
            super(MedicationAdministration_Dosage, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='MedicationAdministration.Dosage', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='MedicationAdministration.Dosage')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='MedicationAdministration.Dosage', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='MedicationAdministration.Dosage'):
        super(MedicationAdministration_Dosage, self).exportAttributes(outfile, level, already_processed, namespace_, name_='MedicationAdministration.Dosage')
    def exportChildren(self, outfile, level, namespace_='', name_='MedicationAdministration.Dosage', fromsubclass_=False, pretty_print=True):
        super(MedicationAdministration_Dosage, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.timingDateTime is not None:
            self.timingDateTime.export(outfile, level, namespace_, name_='timingDateTime', pretty_print=pretty_print)
        if self.timingPeriod is not None:
            self.timingPeriod.export(outfile, level, namespace_, name_='timingPeriod', pretty_print=pretty_print)
        if self.asNeededBoolean is not None:
            self.asNeededBoolean.export(outfile, level, namespace_, name_='asNeededBoolean', pretty_print=pretty_print)
        if self.asNeededCodeableConcept is not None:
            self.asNeededCodeableConcept.export(outfile, level, namespace_, name_='asNeededCodeableConcept', pretty_print=pretty_print)
        if self.site is not None:
            self.site.export(outfile, level, namespace_, name_='site', pretty_print=pretty_print)
        if self.route is not None:
            self.route.export(outfile, level, namespace_, name_='route', pretty_print=pretty_print)
        if self.method is not None:
            self.method.export(outfile, level, namespace_, name_='method', pretty_print=pretty_print)
        if self.quantity is not None:
            self.quantity.export(outfile, level, namespace_, name_='quantity', pretty_print=pretty_print)
        if self.rate is not None:
            self.rate.export(outfile, level, namespace_, name_='rate', pretty_print=pretty_print)
        if self.maxDosePerPeriod is not None:
            self.maxDosePerPeriod.export(outfile, level, namespace_, name_='maxDosePerPeriod', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='MedicationAdministration.Dosage', mapping_=None):
        element = super(MedicationAdministration_Dosage, self).to_etree(parent_element, name_, mapping_)
        if self.timingDateTime is not None:
            timingDateTime_ = self.timingDateTime
            timingDateTime_.to_etree(element, name_='timingDateTime', mapping_=mapping_)
        if self.timingPeriod is not None:
            timingPeriod_ = self.timingPeriod
            timingPeriod_.to_etree(element, name_='timingPeriod', mapping_=mapping_)
        if self.asNeededBoolean is not None:
            asNeededBoolean_ = self.asNeededBoolean
            asNeededBoolean_.to_etree(element, name_='asNeededBoolean', mapping_=mapping_)
        if self.asNeededCodeableConcept is not None:
            asNeededCodeableConcept_ = self.asNeededCodeableConcept
            asNeededCodeableConcept_.to_etree(element, name_='asNeededCodeableConcept', mapping_=mapping_)
        if self.site is not None:
            site_ = self.site
            site_.to_etree(element, name_='site', mapping_=mapping_)
        if self.route is not None:
            route_ = self.route
            route_.to_etree(element, name_='route', mapping_=mapping_)
        if self.method is not None:
            method_ = self.method
            method_.to_etree(element, name_='method', mapping_=mapping_)
        if self.quantity is not None:
            quantity_ = self.quantity
            quantity_.to_etree(element, name_='quantity', mapping_=mapping_)
        if self.rate is not None:
            rate_ = self.rate
            rate_.to_etree(element, name_='rate', mapping_=mapping_)
        if self.maxDosePerPeriod is not None:
            maxDosePerPeriod_ = self.maxDosePerPeriod
            maxDosePerPeriod_.to_etree(element, name_='maxDosePerPeriod', mapping_=mapping_)
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
        super(MedicationAdministration_Dosage, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'timingDateTime':
            obj_ = dateTime.factory()
            obj_.build(child_)
            self.timingDateTime = obj_
            obj_.original_tagname_ = 'timingDateTime'
        elif nodeName_ == 'timingPeriod':
            obj_ = Period.factory()
            obj_.build(child_)
            self.timingPeriod = obj_
            obj_.original_tagname_ = 'timingPeriod'
        elif nodeName_ == 'asNeededBoolean':
            obj_ = boolean.factory()
            obj_.build(child_)
            self.asNeededBoolean = obj_
            obj_.original_tagname_ = 'asNeededBoolean'
        elif nodeName_ == 'asNeededCodeableConcept':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.asNeededCodeableConcept = obj_
            obj_.original_tagname_ = 'asNeededCodeableConcept'
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
        elif nodeName_ == 'method':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.method = obj_
            obj_.original_tagname_ = 'method'
        elif nodeName_ == 'quantity':
            obj_ = Quantity.factory()
            obj_.build(child_)
            self.quantity = obj_
            obj_.original_tagname_ = 'quantity'
        elif nodeName_ == 'rate':
            obj_ = Ratio.factory()
            obj_.build(child_)
            self.rate = obj_
            obj_.original_tagname_ = 'rate'
        elif nodeName_ == 'maxDosePerPeriod':
            obj_ = Ratio.factory()
            obj_.build(child_)
            self.maxDosePerPeriod = obj_
            obj_.original_tagname_ = 'maxDosePerPeriod'
        super(MedicationAdministration_Dosage, self).buildChildren(child_, node, nodeName_, True)
# end class MedicationAdministration_Dosage


class MedicationAdministrationStatus(Element):
    """A set of codes indicating the current status of a
    MedicationAdministrationIf the element is present, it must have
    either a @value, an @id, or extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(MedicationAdministrationStatus, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if MedicationAdministrationStatus.subclass:
            return MedicationAdministrationStatus.subclass(*args_, **kwargs_)
        else:
            return MedicationAdministrationStatus(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(MedicationAdministrationStatus, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='MedicationAdministrationStatus', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='MedicationAdministrationStatus')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='MedicationAdministrationStatus', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='MedicationAdministrationStatus'):
        super(MedicationAdministrationStatus, self).exportAttributes(outfile, level, already_processed, namespace_, name_='MedicationAdministrationStatus')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='MedicationAdministrationStatus', fromsubclass_=False, pretty_print=True):
        super(MedicationAdministrationStatus, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='MedicationAdministrationStatus', mapping_=None):
        element = super(MedicationAdministrationStatus, self).to_etree(parent_element, name_, mapping_)
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
        super(MedicationAdministrationStatus, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(MedicationAdministrationStatus, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class MedicationAdministrationStatus
