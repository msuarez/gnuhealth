from .base_classes import *
from .support_functions import *


class MedicationPrescription(Resource):
    """An order for both supply of the medication and the instructions for
    administration of the medicine to a patient.If the element is
    present, it must have either a @value, an @id, or extensionsCan
    be the reason or the indication for writing the prescription."""
    subclass = None
    superclass = Resource
    def __init__(self, id=None, extension=None, modifierExtension=None, language=None, text=None, contained=None, identifier=None, dateWritten=None, status=None, patient=None, prescriber=None, encounter=None, reasonCodeableConcept=None, reasonResource=None, medication=None, dosageInstruction=None, dispense=None, substitution=None):
        self.original_tagname_ = None
        super(MedicationPrescription, self).__init__(id, extension, modifierExtension, language, text, contained, )
        if identifier is None:
            self.identifier = []
        else:
            self.identifier = identifier
        self.dateWritten = dateWritten
        self.status = status
        self.patient = patient
        self.prescriber = prescriber
        self.encounter = encounter
        self.reasonCodeableConcept = reasonCodeableConcept
        self.reasonResource = reasonResource
        self.medication = medication
        if dosageInstruction is None:
            self.dosageInstruction = []
        else:
            self.dosageInstruction = dosageInstruction
        self.dispense = dispense
        self.substitution = substitution
    def factory(*args_, **kwargs_):
        if MedicationPrescription.subclass:
            return MedicationPrescription.subclass(*args_, **kwargs_)
        else:
            return MedicationPrescription(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_identifier(self): return self.identifier
    def set_identifier(self, identifier): self.identifier = identifier
    def add_identifier(self, value): self.identifier.append(value)
    def insert_identifier(self, index, value): self.identifier[index] = value
    def get_dateWritten(self): return self.dateWritten
    def set_dateWritten(self, dateWritten): self.dateWritten = dateWritten
    def get_status(self): return self.status
    def set_status(self, status): self.status = status
    def get_patient(self): return self.patient
    def set_patient(self, patient): self.patient = patient
    def get_prescriber(self): return self.prescriber
    def set_prescriber(self, prescriber): self.prescriber = prescriber
    def get_encounter(self): return self.encounter
    def set_encounter(self, encounter): self.encounter = encounter
    def get_reasonCodeableConcept(self): return self.reasonCodeableConcept
    def set_reasonCodeableConcept(self, reasonCodeableConcept): self.reasonCodeableConcept = reasonCodeableConcept
    def get_reasonResource(self): return self.reasonResource
    def set_reasonResource(self, reasonResource): self.reasonResource = reasonResource
    def get_medication(self): return self.medication
    def set_medication(self, medication): self.medication = medication
    def get_dosageInstruction(self): return self.dosageInstruction
    def set_dosageInstruction(self, dosageInstruction): self.dosageInstruction = dosageInstruction
    def add_dosageInstruction(self, value): self.dosageInstruction.append(value)
    def insert_dosageInstruction(self, index, value): self.dosageInstruction[index] = value
    def get_dispense(self): return self.dispense
    def set_dispense(self, dispense): self.dispense = dispense
    def get_substitution(self): return self.substitution
    def set_substitution(self, substitution): self.substitution = substitution
    def hasContent_(self):
        if (
            self.identifier or
            self.dateWritten is not None or
            self.status is not None or
            self.patient is not None or
            self.prescriber is not None or
            self.encounter is not None or
            self.reasonCodeableConcept is not None or
            self.reasonResource is not None or
            self.medication is not None or
            self.dosageInstruction or
            self.dispense is not None or
            self.substitution is not None or
            super(MedicationPrescription, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='MedicationPrescription', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='MedicationPrescription')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='MedicationPrescription', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='MedicationPrescription'):
        super(MedicationPrescription, self).exportAttributes(outfile, level, already_processed, namespace_, name_='MedicationPrescription')
    def exportChildren(self, outfile, level, namespace_='', name_='MedicationPrescription', fromsubclass_=False, pretty_print=True):
        super(MedicationPrescription, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for identifier_ in self.identifier:
            identifier_.export(outfile, level, namespace_, name_='identifier', pretty_print=pretty_print)
        if self.dateWritten is not None:
            self.dateWritten.export(outfile, level, namespace_, name_='dateWritten', pretty_print=pretty_print)
        if self.status is not None:
            self.status.export(outfile, level, namespace_, name_='status', pretty_print=pretty_print)
        if self.patient is not None:
            self.patient.export(outfile, level, namespace_, name_='patient', pretty_print=pretty_print)
        if self.prescriber is not None:
            self.prescriber.export(outfile, level, namespace_, name_='prescriber', pretty_print=pretty_print)
        if self.encounter is not None:
            self.encounter.export(outfile, level, namespace_, name_='encounter', pretty_print=pretty_print)
        if self.reasonCodeableConcept is not None:
            self.reasonCodeableConcept.export(outfile, level, namespace_, name_='reasonCodeableConcept', pretty_print=pretty_print)
        if self.reasonResource is not None:
            self.reasonResource.export(outfile, level, namespace_, name_='reasonResource', pretty_print=pretty_print)
        if self.medication is not None:
            self.medication.export(outfile, level, namespace_, name_='medication', pretty_print=pretty_print)
        for dosageInstruction_ in self.dosageInstruction:
            dosageInstruction_.export(outfile, level, namespace_, name_='dosageInstruction', pretty_print=pretty_print)
        if self.dispense is not None:
            self.dispense.export(outfile, level, namespace_, name_='dispense', pretty_print=pretty_print)
        if self.substitution is not None:
            self.substitution.export(outfile, level, namespace_, name_='substitution', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='MedicationPrescription', mapping_=None):
        element = super(MedicationPrescription, self).to_etree(parent_element, name_, mapping_)
        for identifier_ in self.identifier:
            identifier_.to_etree(element, name_='identifier', mapping_=mapping_)
        if self.dateWritten is not None:
            dateWritten_ = self.dateWritten
            dateWritten_.to_etree(element, name_='dateWritten', mapping_=mapping_)
        if self.status is not None:
            status_ = self.status
            status_.to_etree(element, name_='status', mapping_=mapping_)
        if self.patient is not None:
            patient_ = self.patient
            patient_.to_etree(element, name_='patient', mapping_=mapping_)
        if self.prescriber is not None:
            prescriber_ = self.prescriber
            prescriber_.to_etree(element, name_='prescriber', mapping_=mapping_)
        if self.encounter is not None:
            encounter_ = self.encounter
            encounter_.to_etree(element, name_='encounter', mapping_=mapping_)
        if self.reasonCodeableConcept is not None:
            reasonCodeableConcept_ = self.reasonCodeableConcept
            reasonCodeableConcept_.to_etree(element, name_='reasonCodeableConcept', mapping_=mapping_)
        if self.reasonResource is not None:
            reasonResource_ = self.reasonResource
            reasonResource_.to_etree(element, name_='reasonResource', mapping_=mapping_)
        if self.medication is not None:
            medication_ = self.medication
            medication_.to_etree(element, name_='medication', mapping_=mapping_)
        for dosageInstruction_ in self.dosageInstruction:
            dosageInstruction_.to_etree(element, name_='dosageInstruction', mapping_=mapping_)
        if self.dispense is not None:
            dispense_ = self.dispense
            dispense_.to_etree(element, name_='dispense', mapping_=mapping_)
        if self.substitution is not None:
            substitution_ = self.substitution
            substitution_.to_etree(element, name_='substitution', mapping_=mapping_)
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
        super(MedicationPrescription, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'identifier':
            obj_ = Identifier.factory()
            obj_.build(child_)
            self.identifier.append(obj_)
            obj_.original_tagname_ = 'identifier'
        elif nodeName_ == 'dateWritten':
            obj_ = dateTime.factory()
            obj_.build(child_)
            self.dateWritten = obj_
            obj_.original_tagname_ = 'dateWritten'
        elif nodeName_ == 'status':
            obj_ = MedicationPrescriptionStatus.factory()
            obj_.build(child_)
            self.status = obj_
            obj_.original_tagname_ = 'status'
        elif nodeName_ == 'patient':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.patient = obj_
            obj_.original_tagname_ = 'patient'
        elif nodeName_ == 'prescriber':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.prescriber = obj_
            obj_.original_tagname_ = 'prescriber'
        elif nodeName_ == 'encounter':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.encounter = obj_
            obj_.original_tagname_ = 'encounter'
        elif nodeName_ == 'reasonCodeableConcept':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.reasonCodeableConcept = obj_
            obj_.original_tagname_ = 'reasonCodeableConcept'
        elif nodeName_ == 'reasonResource':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.reasonResource = obj_
            obj_.original_tagname_ = 'reasonResource'
        elif nodeName_ == 'medication':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.medication = obj_
            obj_.original_tagname_ = 'medication'
        elif nodeName_ == 'dosageInstruction':
            obj_ = MedicationPrescription_DosageInstruction.factory()
            obj_.build(child_)
            self.dosageInstruction.append(obj_)
            obj_.original_tagname_ = 'dosageInstruction'
        elif nodeName_ == 'dispense':
            obj_ = MedicationPrescription_Dispense.factory()
            obj_.build(child_)
            self.dispense = obj_
            obj_.original_tagname_ = 'dispense'
        elif nodeName_ == 'substitution':
            obj_ = MedicationPrescription_Substitution.factory()
            obj_.build(child_)
            self.substitution = obj_
            obj_.original_tagname_ = 'substitution'
        super(MedicationPrescription, self).buildChildren(child_, node, nodeName_, True)
# end class MedicationPrescription


class MedicationPrescription_DosageInstruction(BackboneElement):
    """An order for both supply of the medication and the instructions for
    administration of the medicine to a patient.The timing schedule
    for giving the medication to the patient. The Schedule data type
    allows many different expressions, for example. "Every 8 hours";
    "Three times a day"; "1/2 an hour before breakfast for 10 days
    from 23-Dec 2011:"; "15 Oct 2013, 17 Oct 2013 and 1 Nov 2013".If
    set to true or if specified as a CodeableConcept, indicates that
    the medication is only taken when needed within the specified
    schedule rather than at every scheduled dose. If a
    CodeableConcept is present, it indicates the pre-condition for
    taking the Medication."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, text=None, additionalInstructions=None, timingDateTime=None, timingPeriod=None, timingSchedule=None, asNeededBoolean=None, asNeededCodeableConcept=None, site=None, route=None, method=None, doseQuantity=None, rate=None, maxDosePerPeriod=None):
        self.original_tagname_ = None
        super(MedicationPrescription_DosageInstruction, self).__init__(id, extension, modifierExtension, )
        self.text = text
        self.additionalInstructions = additionalInstructions
        self.timingDateTime = timingDateTime
        self.timingPeriod = timingPeriod
        self.timingSchedule = timingSchedule
        self.asNeededBoolean = asNeededBoolean
        self.asNeededCodeableConcept = asNeededCodeableConcept
        self.site = site
        self.route = route
        self.method = method
        self.doseQuantity = doseQuantity
        self.rate = rate
        self.maxDosePerPeriod = maxDosePerPeriod
    def factory(*args_, **kwargs_):
        if MedicationPrescription_DosageInstruction.subclass:
            return MedicationPrescription_DosageInstruction.subclass(*args_, **kwargs_)
        else:
            return MedicationPrescription_DosageInstruction(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_text(self): return self.text
    def set_text(self, text): self.text = text
    def get_additionalInstructions(self): return self.additionalInstructions
    def set_additionalInstructions(self, additionalInstructions): self.additionalInstructions = additionalInstructions
    def get_timingDateTime(self): return self.timingDateTime
    def set_timingDateTime(self, timingDateTime): self.timingDateTime = timingDateTime
    def get_timingPeriod(self): return self.timingPeriod
    def set_timingPeriod(self, timingPeriod): self.timingPeriod = timingPeriod
    def get_timingSchedule(self): return self.timingSchedule
    def set_timingSchedule(self, timingSchedule): self.timingSchedule = timingSchedule
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
    def get_doseQuantity(self): return self.doseQuantity
    def set_doseQuantity(self, doseQuantity): self.doseQuantity = doseQuantity
    def get_rate(self): return self.rate
    def set_rate(self, rate): self.rate = rate
    def get_maxDosePerPeriod(self): return self.maxDosePerPeriod
    def set_maxDosePerPeriod(self, maxDosePerPeriod): self.maxDosePerPeriod = maxDosePerPeriod
    def hasContent_(self):
        if (
            self.text is not None or
            self.additionalInstructions is not None or
            self.timingDateTime is not None or
            self.timingPeriod is not None or
            self.timingSchedule is not None or
            self.asNeededBoolean is not None or
            self.asNeededCodeableConcept is not None or
            self.site is not None or
            self.route is not None or
            self.method is not None or
            self.doseQuantity is not None or
            self.rate is not None or
            self.maxDosePerPeriod is not None or
            super(MedicationPrescription_DosageInstruction, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='MedicationPrescription.DosageInstruction', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='MedicationPrescription.DosageInstruction')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='MedicationPrescription.DosageInstruction', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='MedicationPrescription.DosageInstruction'):
        super(MedicationPrescription_DosageInstruction, self).exportAttributes(outfile, level, already_processed, namespace_, name_='MedicationPrescription.DosageInstruction')
    def exportChildren(self, outfile, level, namespace_='', name_='MedicationPrescription.DosageInstruction', fromsubclass_=False, pretty_print=True):
        super(MedicationPrescription_DosageInstruction, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.text is not None:
            self.text.export(outfile, level, namespace_, name_='text', pretty_print=pretty_print)
        if self.additionalInstructions is not None:
            self.additionalInstructions.export(outfile, level, namespace_, name_='additionalInstructions', pretty_print=pretty_print)
        if self.timingDateTime is not None:
            self.timingDateTime.export(outfile, level, namespace_, name_='timingDateTime', pretty_print=pretty_print)
        if self.timingPeriod is not None:
            self.timingPeriod.export(outfile, level, namespace_, name_='timingPeriod', pretty_print=pretty_print)
        if self.timingSchedule is not None:
            self.timingSchedule.export(outfile, level, namespace_, name_='timingSchedule', pretty_print=pretty_print)
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
        if self.doseQuantity is not None:
            self.doseQuantity.export(outfile, level, namespace_, name_='doseQuantity', pretty_print=pretty_print)
        if self.rate is not None:
            self.rate.export(outfile, level, namespace_, name_='rate', pretty_print=pretty_print)
        if self.maxDosePerPeriod is not None:
            self.maxDosePerPeriod.export(outfile, level, namespace_, name_='maxDosePerPeriod', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='MedicationPrescription.DosageInstruction', mapping_=None):
        element = super(MedicationPrescription_DosageInstruction, self).to_etree(parent_element, name_, mapping_)
        if self.text is not None:
            text_ = self.text
            text_.to_etree(element, name_='text', mapping_=mapping_)
        if self.additionalInstructions is not None:
            additionalInstructions_ = self.additionalInstructions
            additionalInstructions_.to_etree(element, name_='additionalInstructions', mapping_=mapping_)
        if self.timingDateTime is not None:
            timingDateTime_ = self.timingDateTime
            timingDateTime_.to_etree(element, name_='timingDateTime', mapping_=mapping_)
        if self.timingPeriod is not None:
            timingPeriod_ = self.timingPeriod
            timingPeriod_.to_etree(element, name_='timingPeriod', mapping_=mapping_)
        if self.timingSchedule is not None:
            timingSchedule_ = self.timingSchedule
            timingSchedule_.to_etree(element, name_='timingSchedule', mapping_=mapping_)
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
        if self.doseQuantity is not None:
            doseQuantity_ = self.doseQuantity
            doseQuantity_.to_etree(element, name_='doseQuantity', mapping_=mapping_)
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
        super(MedicationPrescription_DosageInstruction, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'text':
            obj_ = string.factory()
            obj_.build(child_)
            self.text = obj_
            obj_.original_tagname_ = 'text'
        elif nodeName_ == 'additionalInstructions':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.additionalInstructions = obj_
            obj_.original_tagname_ = 'additionalInstructions'
        elif nodeName_ == 'timingDateTime':
            obj_ = dateTime.factory()
            obj_.build(child_)
            self.timingDateTime = obj_
            obj_.original_tagname_ = 'timingDateTime'
        elif nodeName_ == 'timingPeriod':
            obj_ = Period.factory()
            obj_.build(child_)
            self.timingPeriod = obj_
            obj_.original_tagname_ = 'timingPeriod'
        elif nodeName_ == 'timingSchedule':
            obj_ = Schedule.factory()
            obj_.build(child_)
            self.timingSchedule = obj_
            obj_.original_tagname_ = 'timingSchedule'
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
        elif nodeName_ == 'doseQuantity':
            obj_ = Quantity.factory()
            obj_.build(child_)
            self.doseQuantity = obj_
            obj_.original_tagname_ = 'doseQuantity'
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
        super(MedicationPrescription_DosageInstruction, self).buildChildren(child_, node, nodeName_, True)
# end class MedicationPrescription_DosageInstruction


class MedicationPrescription_Dispense(BackboneElement):
    """An order for both supply of the medication and the instructions for
    administration of the medicine to a patient."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, medication=None, validityPeriod=None, numberOfRepeatsAllowed=None, quantity=None, expectedSupplyDuration=None):
        self.original_tagname_ = None
        super(MedicationPrescription_Dispense, self).__init__(id, extension, modifierExtension, )
        self.medication = medication
        self.validityPeriod = validityPeriod
        self.numberOfRepeatsAllowed = numberOfRepeatsAllowed
        self.quantity = quantity
        self.expectedSupplyDuration = expectedSupplyDuration
    def factory(*args_, **kwargs_):
        if MedicationPrescription_Dispense.subclass:
            return MedicationPrescription_Dispense.subclass(*args_, **kwargs_)
        else:
            return MedicationPrescription_Dispense(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_medication(self): return self.medication
    def set_medication(self, medication): self.medication = medication
    def get_validityPeriod(self): return self.validityPeriod
    def set_validityPeriod(self, validityPeriod): self.validityPeriod = validityPeriod
    def get_numberOfRepeatsAllowed(self): return self.numberOfRepeatsAllowed
    def set_numberOfRepeatsAllowed(self, numberOfRepeatsAllowed): self.numberOfRepeatsAllowed = numberOfRepeatsAllowed
    def get_quantity(self): return self.quantity
    def set_quantity(self, quantity): self.quantity = quantity
    def get_expectedSupplyDuration(self): return self.expectedSupplyDuration
    def set_expectedSupplyDuration(self, expectedSupplyDuration): self.expectedSupplyDuration = expectedSupplyDuration
    def hasContent_(self):
        if (
            self.medication is not None or
            self.validityPeriod is not None or
            self.numberOfRepeatsAllowed is not None or
            self.quantity is not None or
            self.expectedSupplyDuration is not None or
            super(MedicationPrescription_Dispense, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='MedicationPrescription.Dispense', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='MedicationPrescription.Dispense')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='MedicationPrescription.Dispense', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='MedicationPrescription.Dispense'):
        super(MedicationPrescription_Dispense, self).exportAttributes(outfile, level, already_processed, namespace_, name_='MedicationPrescription.Dispense')
    def exportChildren(self, outfile, level, namespace_='', name_='MedicationPrescription.Dispense', fromsubclass_=False, pretty_print=True):
        super(MedicationPrescription_Dispense, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.medication is not None:
            self.medication.export(outfile, level, namespace_, name_='medication', pretty_print=pretty_print)
        if self.validityPeriod is not None:
            self.validityPeriod.export(outfile, level, namespace_, name_='validityPeriod', pretty_print=pretty_print)
        if self.numberOfRepeatsAllowed is not None:
            self.numberOfRepeatsAllowed.export(outfile, level, namespace_, name_='numberOfRepeatsAllowed', pretty_print=pretty_print)
        if self.quantity is not None:
            self.quantity.export(outfile, level, namespace_, name_='quantity', pretty_print=pretty_print)
        if self.expectedSupplyDuration is not None:
            self.expectedSupplyDuration.export(outfile, level, namespace_, name_='expectedSupplyDuration', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='MedicationPrescription.Dispense', mapping_=None):
        element = super(MedicationPrescription_Dispense, self).to_etree(parent_element, name_, mapping_)
        if self.medication is not None:
            medication_ = self.medication
            medication_.to_etree(element, name_='medication', mapping_=mapping_)
        if self.validityPeriod is not None:
            validityPeriod_ = self.validityPeriod
            validityPeriod_.to_etree(element, name_='validityPeriod', mapping_=mapping_)
        if self.numberOfRepeatsAllowed is not None:
            numberOfRepeatsAllowed_ = self.numberOfRepeatsAllowed
            numberOfRepeatsAllowed_.to_etree(element, name_='numberOfRepeatsAllowed', mapping_=mapping_)
        if self.quantity is not None:
            quantity_ = self.quantity
            quantity_.to_etree(element, name_='quantity', mapping_=mapping_)
        if self.expectedSupplyDuration is not None:
            expectedSupplyDuration_ = self.expectedSupplyDuration
            expectedSupplyDuration_.to_etree(element, name_='expectedSupplyDuration', mapping_=mapping_)
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
        super(MedicationPrescription_Dispense, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'medication':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.medication = obj_
            obj_.original_tagname_ = 'medication'
        elif nodeName_ == 'validityPeriod':
            obj_ = Period.factory()
            obj_.build(child_)
            self.validityPeriod = obj_
            obj_.original_tagname_ = 'validityPeriod'
        elif nodeName_ == 'numberOfRepeatsAllowed':
            obj_ = integer.factory()
            obj_.build(child_)
            self.numberOfRepeatsAllowed = obj_
            obj_.original_tagname_ = 'numberOfRepeatsAllowed'
        elif nodeName_ == 'quantity':
            obj_ = Quantity.factory()
            obj_.build(child_)
            self.quantity = obj_
            obj_.original_tagname_ = 'quantity'
        elif nodeName_ == 'expectedSupplyDuration':
            obj_ = Duration.factory()
            obj_.build(child_)
            self.expectedSupplyDuration = obj_
            obj_.original_tagname_ = 'expectedSupplyDuration'
        super(MedicationPrescription_Dispense, self).buildChildren(child_, node, nodeName_, True)
# end class MedicationPrescription_Dispense


class MedicationPrescription_Substitution(BackboneElement):
    """An order for both supply of the medication and the instructions for
    administration of the medicine to a patient."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, type_=None, reason=None):
        self.original_tagname_ = None
        super(MedicationPrescription_Substitution, self).__init__(id, extension, modifierExtension, )
        self.type_ = type_
        self.reason = reason
    def factory(*args_, **kwargs_):
        if MedicationPrescription_Substitution.subclass:
            return MedicationPrescription_Substitution.subclass(*args_, **kwargs_)
        else:
            return MedicationPrescription_Substitution(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_type(self): return self.type_
    def set_type(self, type_): self.type_ = type_
    def get_reason(self): return self.reason
    def set_reason(self, reason): self.reason = reason
    def hasContent_(self):
        if (
            self.type_ is not None or
            self.reason is not None or
            super(MedicationPrescription_Substitution, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='MedicationPrescription.Substitution', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='MedicationPrescription.Substitution')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='MedicationPrescription.Substitution', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='MedicationPrescription.Substitution'):
        super(MedicationPrescription_Substitution, self).exportAttributes(outfile, level, already_processed, namespace_, name_='MedicationPrescription.Substitution')
    def exportChildren(self, outfile, level, namespace_='', name_='MedicationPrescription.Substitution', fromsubclass_=False, pretty_print=True):
        super(MedicationPrescription_Substitution, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.type_ is not None:
            self.type_.export(outfile, level, namespace_, name_='type', pretty_print=pretty_print)
        if self.reason is not None:
            self.reason.export(outfile, level, namespace_, name_='reason', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='MedicationPrescription.Substitution', mapping_=None):
        element = super(MedicationPrescription_Substitution, self).to_etree(parent_element, name_, mapping_)
        if self.type_ is not None:
            type__ = self.type_
            type__.to_etree(element, name_='type', mapping_=mapping_)
        if self.reason is not None:
            reason_ = self.reason
            reason_.to_etree(element, name_='reason', mapping_=mapping_)
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
        super(MedicationPrescription_Substitution, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'type':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.type_ = obj_
            obj_.original_tagname_ = 'type'
        elif nodeName_ == 'reason':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.reason = obj_
            obj_.original_tagname_ = 'reason'
        super(MedicationPrescription_Substitution, self).buildChildren(child_, node, nodeName_, True)
# end class MedicationPrescription_Substitution


class MedicationPrescriptionStatus(Element):
    """A code specifying the state of the prescribing event. Describes the
    lifecycle of the prescription.If the element is present, it must
    have either a @value, an @id, or extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(MedicationPrescriptionStatus, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if MedicationPrescriptionStatus.subclass:
            return MedicationPrescriptionStatus.subclass(*args_, **kwargs_)
        else:
            return MedicationPrescriptionStatus(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(MedicationPrescriptionStatus, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='MedicationPrescriptionStatus', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='MedicationPrescriptionStatus')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='MedicationPrescriptionStatus', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='MedicationPrescriptionStatus'):
        super(MedicationPrescriptionStatus, self).exportAttributes(outfile, level, already_processed, namespace_, name_='MedicationPrescriptionStatus')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='MedicationPrescriptionStatus', fromsubclass_=False, pretty_print=True):
        super(MedicationPrescriptionStatus, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='MedicationPrescriptionStatus', mapping_=None):
        element = super(MedicationPrescriptionStatus, self).to_etree(parent_element, name_, mapping_)
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
        super(MedicationPrescriptionStatus, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(MedicationPrescriptionStatus, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class MedicationPrescriptionStatus
