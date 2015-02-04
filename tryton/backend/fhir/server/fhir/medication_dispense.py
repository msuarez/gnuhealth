from .base_classes import *
from .support_functions import *


class MedicationDispense(Resource):
    """Dispensing a medication to a named patient. This includes a
    description of the supply provided and the instructions for
    administering the medication.If the element is present, it must
    have either a @value, an @id, or extensions"""
    subclass = None
    superclass = Resource
    def __init__(self, id=None, extension=None, modifierExtension=None, language=None, text=None, contained=None, identifier=None, status=None, patient=None, dispenser=None, authorizingPrescription=None, dispense=None, substitution=None):
        self.original_tagname_ = None
        super(MedicationDispense, self).__init__(id, extension, modifierExtension, language, text, contained, )
        self.identifier = identifier
        self.status = status
        self.patient = patient
        self.dispenser = dispenser
        if authorizingPrescription is None:
            self.authorizingPrescription = []
        else:
            self.authorizingPrescription = authorizingPrescription
        if dispense is None:
            self.dispense = []
        else:
            self.dispense = dispense
        self.substitution = substitution
    def factory(*args_, **kwargs_):
        if MedicationDispense.subclass:
            return MedicationDispense.subclass(*args_, **kwargs_)
        else:
            return MedicationDispense(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_identifier(self): return self.identifier
    def set_identifier(self, identifier): self.identifier = identifier
    def get_status(self): return self.status
    def set_status(self, status): self.status = status
    def get_patient(self): return self.patient
    def set_patient(self, patient): self.patient = patient
    def get_dispenser(self): return self.dispenser
    def set_dispenser(self, dispenser): self.dispenser = dispenser
    def get_authorizingPrescription(self): return self.authorizingPrescription
    def set_authorizingPrescription(self, authorizingPrescription): self.authorizingPrescription = authorizingPrescription
    def add_authorizingPrescription(self, value): self.authorizingPrescription.append(value)
    def insert_authorizingPrescription(self, index, value): self.authorizingPrescription[index] = value
    def get_dispense(self): return self.dispense
    def set_dispense(self, dispense): self.dispense = dispense
    def add_dispense(self, value): self.dispense.append(value)
    def insert_dispense(self, index, value): self.dispense[index] = value
    def get_substitution(self): return self.substitution
    def set_substitution(self, substitution): self.substitution = substitution
    def hasContent_(self):
        if (
            self.identifier is not None or
            self.status is not None or
            self.patient is not None or
            self.dispenser is not None or
            self.authorizingPrescription or
            self.dispense or
            self.substitution is not None or
            super(MedicationDispense, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='MedicationDispense', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='MedicationDispense')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='MedicationDispense', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='MedicationDispense'):
        super(MedicationDispense, self).exportAttributes(outfile, level, already_processed, namespace_, name_='MedicationDispense')
    def exportChildren(self, outfile, level, namespace_='', name_='MedicationDispense', fromsubclass_=False, pretty_print=True):
        super(MedicationDispense, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.identifier is not None:
            self.identifier.export(outfile, level, namespace_, name_='identifier', pretty_print=pretty_print)
        if self.status is not None:
            self.status.export(outfile, level, namespace_, name_='status', pretty_print=pretty_print)
        if self.patient is not None:
            self.patient.export(outfile, level, namespace_, name_='patient', pretty_print=pretty_print)
        if self.dispenser is not None:
            self.dispenser.export(outfile, level, namespace_, name_='dispenser', pretty_print=pretty_print)
        for authorizingPrescription_ in self.authorizingPrescription:
            authorizingPrescription_.export(outfile, level, namespace_, name_='authorizingPrescription', pretty_print=pretty_print)
        for dispense_ in self.dispense:
            dispense_.export(outfile, level, namespace_, name_='dispense', pretty_print=pretty_print)
        if self.substitution is not None:
            self.substitution.export(outfile, level, namespace_, name_='substitution', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='MedicationDispense', mapping_=None):
        element = super(MedicationDispense, self).to_etree(parent_element, name_, mapping_)
        if self.identifier is not None:
            identifier_ = self.identifier
            identifier_.to_etree(element, name_='identifier', mapping_=mapping_)
        if self.status is not None:
            status_ = self.status
            status_.to_etree(element, name_='status', mapping_=mapping_)
        if self.patient is not None:
            patient_ = self.patient
            patient_.to_etree(element, name_='patient', mapping_=mapping_)
        if self.dispenser is not None:
            dispenser_ = self.dispenser
            dispenser_.to_etree(element, name_='dispenser', mapping_=mapping_)
        for authorizingPrescription_ in self.authorizingPrescription:
            authorizingPrescription_.to_etree(element, name_='authorizingPrescription', mapping_=mapping_)
        for dispense_ in self.dispense:
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
        super(MedicationDispense, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'identifier':
            obj_ = Identifier.factory()
            obj_.build(child_)
            self.identifier = obj_
            obj_.original_tagname_ = 'identifier'
        elif nodeName_ == 'status':
            obj_ = MedicationDispenseStatus.factory()
            obj_.build(child_)
            self.status = obj_
            obj_.original_tagname_ = 'status'
        elif nodeName_ == 'patient':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.patient = obj_
            obj_.original_tagname_ = 'patient'
        elif nodeName_ == 'dispenser':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.dispenser = obj_
            obj_.original_tagname_ = 'dispenser'
        elif nodeName_ == 'authorizingPrescription':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.authorizingPrescription.append(obj_)
            obj_.original_tagname_ = 'authorizingPrescription'
        elif nodeName_ == 'dispense':
            obj_ = MedicationDispense_Dispense.factory()
            obj_.build(child_)
            self.dispense.append(obj_)
            obj_.original_tagname_ = 'dispense'
        elif nodeName_ == 'substitution':
            obj_ = MedicationDispense_Substitution.factory()
            obj_.build(child_)
            self.substitution = obj_
            obj_.original_tagname_ = 'substitution'
        super(MedicationDispense, self).buildChildren(child_, node, nodeName_, True)
# end class MedicationDispense


class MedicationDispense_Dispense(BackboneElement):
    """Dispensing a medication to a named patient. This includes a
    description of the supply provided and the instructions for
    administering the medication."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, identifier=None, status=None, type_=None, quantity=None, medication=None, whenPrepared=None, whenHandedOver=None, destination=None, receiver=None, dosage=None):
        self.original_tagname_ = None
        super(MedicationDispense_Dispense, self).__init__(id, extension, modifierExtension, )
        self.identifier = identifier
        self.status = status
        self.type_ = type_
        self.quantity = quantity
        self.medication = medication
        self.whenPrepared = whenPrepared
        self.whenHandedOver = whenHandedOver
        self.destination = destination
        if receiver is None:
            self.receiver = []
        else:
            self.receiver = receiver
        if dosage is None:
            self.dosage = []
        else:
            self.dosage = dosage
    def factory(*args_, **kwargs_):
        if MedicationDispense_Dispense.subclass:
            return MedicationDispense_Dispense.subclass(*args_, **kwargs_)
        else:
            return MedicationDispense_Dispense(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_identifier(self): return self.identifier
    def set_identifier(self, identifier): self.identifier = identifier
    def get_status(self): return self.status
    def set_status(self, status): self.status = status
    def get_type(self): return self.type_
    def set_type(self, type_): self.type_ = type_
    def get_quantity(self): return self.quantity
    def set_quantity(self, quantity): self.quantity = quantity
    def get_medication(self): return self.medication
    def set_medication(self, medication): self.medication = medication
    def get_whenPrepared(self): return self.whenPrepared
    def set_whenPrepared(self, whenPrepared): self.whenPrepared = whenPrepared
    def get_whenHandedOver(self): return self.whenHandedOver
    def set_whenHandedOver(self, whenHandedOver): self.whenHandedOver = whenHandedOver
    def get_destination(self): return self.destination
    def set_destination(self, destination): self.destination = destination
    def get_receiver(self): return self.receiver
    def set_receiver(self, receiver): self.receiver = receiver
    def add_receiver(self, value): self.receiver.append(value)
    def insert_receiver(self, index, value): self.receiver[index] = value
    def get_dosage(self): return self.dosage
    def set_dosage(self, dosage): self.dosage = dosage
    def add_dosage(self, value): self.dosage.append(value)
    def insert_dosage(self, index, value): self.dosage[index] = value
    def hasContent_(self):
        if (
            self.identifier is not None or
            self.status is not None or
            self.type_ is not None or
            self.quantity is not None or
            self.medication is not None or
            self.whenPrepared is not None or
            self.whenHandedOver is not None or
            self.destination is not None or
            self.receiver or
            self.dosage or
            super(MedicationDispense_Dispense, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='MedicationDispense.Dispense', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='MedicationDispense.Dispense')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='MedicationDispense.Dispense', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='MedicationDispense.Dispense'):
        super(MedicationDispense_Dispense, self).exportAttributes(outfile, level, already_processed, namespace_, name_='MedicationDispense.Dispense')
    def exportChildren(self, outfile, level, namespace_='', name_='MedicationDispense.Dispense', fromsubclass_=False, pretty_print=True):
        super(MedicationDispense_Dispense, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.identifier is not None:
            self.identifier.export(outfile, level, namespace_, name_='identifier', pretty_print=pretty_print)
        if self.status is not None:
            self.status.export(outfile, level, namespace_, name_='status', pretty_print=pretty_print)
        if self.type_ is not None:
            self.type_.export(outfile, level, namespace_, name_='type', pretty_print=pretty_print)
        if self.quantity is not None:
            self.quantity.export(outfile, level, namespace_, name_='quantity', pretty_print=pretty_print)
        if self.medication is not None:
            self.medication.export(outfile, level, namespace_, name_='medication', pretty_print=pretty_print)
        if self.whenPrepared is not None:
            self.whenPrepared.export(outfile, level, namespace_, name_='whenPrepared', pretty_print=pretty_print)
        if self.whenHandedOver is not None:
            self.whenHandedOver.export(outfile, level, namespace_, name_='whenHandedOver', pretty_print=pretty_print)
        if self.destination is not None:
            self.destination.export(outfile, level, namespace_, name_='destination', pretty_print=pretty_print)
        for receiver_ in self.receiver:
            receiver_.export(outfile, level, namespace_, name_='receiver', pretty_print=pretty_print)
        for dosage_ in self.dosage:
            dosage_.export(outfile, level, namespace_, name_='dosage', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='MedicationDispense.Dispense', mapping_=None):
        element = super(MedicationDispense_Dispense, self).to_etree(parent_element, name_, mapping_)
        if self.identifier is not None:
            identifier_ = self.identifier
            identifier_.to_etree(element, name_='identifier', mapping_=mapping_)
        if self.status is not None:
            status_ = self.status
            status_.to_etree(element, name_='status', mapping_=mapping_)
        if self.type_ is not None:
            type__ = self.type_
            type__.to_etree(element, name_='type', mapping_=mapping_)
        if self.quantity is not None:
            quantity_ = self.quantity
            quantity_.to_etree(element, name_='quantity', mapping_=mapping_)
        if self.medication is not None:
            medication_ = self.medication
            medication_.to_etree(element, name_='medication', mapping_=mapping_)
        if self.whenPrepared is not None:
            whenPrepared_ = self.whenPrepared
            whenPrepared_.to_etree(element, name_='whenPrepared', mapping_=mapping_)
        if self.whenHandedOver is not None:
            whenHandedOver_ = self.whenHandedOver
            whenHandedOver_.to_etree(element, name_='whenHandedOver', mapping_=mapping_)
        if self.destination is not None:
            destination_ = self.destination
            destination_.to_etree(element, name_='destination', mapping_=mapping_)
        for receiver_ in self.receiver:
            receiver_.to_etree(element, name_='receiver', mapping_=mapping_)
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
        super(MedicationDispense_Dispense, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'identifier':
            obj_ = Identifier.factory()
            obj_.build(child_)
            self.identifier = obj_
            obj_.original_tagname_ = 'identifier'
        elif nodeName_ == 'status':
            obj_ = MedicationDispenseStatus.factory()
            obj_.build(child_)
            self.status = obj_
            obj_.original_tagname_ = 'status'
        elif nodeName_ == 'type':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.type_ = obj_
            obj_.original_tagname_ = 'type'
        elif nodeName_ == 'quantity':
            obj_ = Quantity.factory()
            obj_.build(child_)
            self.quantity = obj_
            obj_.original_tagname_ = 'quantity'
        elif nodeName_ == 'medication':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.medication = obj_
            obj_.original_tagname_ = 'medication'
        elif nodeName_ == 'whenPrepared':
            obj_ = dateTime.factory()
            obj_.build(child_)
            self.whenPrepared = obj_
            obj_.original_tagname_ = 'whenPrepared'
        elif nodeName_ == 'whenHandedOver':
            obj_ = dateTime.factory()
            obj_.build(child_)
            self.whenHandedOver = obj_
            obj_.original_tagname_ = 'whenHandedOver'
        elif nodeName_ == 'destination':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.destination = obj_
            obj_.original_tagname_ = 'destination'
        elif nodeName_ == 'receiver':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.receiver.append(obj_)
            obj_.original_tagname_ = 'receiver'
        elif nodeName_ == 'dosage':
            obj_ = MedicationDispense_Dosage.factory()
            obj_.build(child_)
            self.dosage.append(obj_)
            obj_.original_tagname_ = 'dosage'
        super(MedicationDispense_Dispense, self).buildChildren(child_, node, nodeName_, True)
# end class MedicationDispense_Dispense


class MedicationDispense_Dosage(BackboneElement):
    """Dispensing a medication to a named patient. This includes a
    description of the supply provided and the instructions for
    administering the medication.The timing schedule for giving the
    medication to the patient. The Schedule data type allows many
    different expressions, for example. "Every 8 hours"; "Three
    times a day"; "1/2 an hour before breakfast for 10 days from
    23-Dec 2011:"; "15 Oct 2013, 17 Oct 2013 and 1 Nov 2013".If set
    to true or if specified as a CodeableConcept, indicates that the
    medication is only taken when needed within the specified
    schedule rather than at every scheduled dose. If a
    CodeableConcept is present, it indicates the pre-condition for
    taking the Medication."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, additionalInstructions=None, timingDateTime=None, timingPeriod=None, timingSchedule=None, asNeededBoolean=None, asNeededCodeableConcept=None, site=None, route=None, method=None, quantity=None, rate=None, maxDosePerPeriod=None):
        self.original_tagname_ = None
        super(MedicationDispense_Dosage, self).__init__(id, extension, modifierExtension, )
        self.additionalInstructions = additionalInstructions
        self.timingDateTime = timingDateTime
        self.timingPeriod = timingPeriod
        self.timingSchedule = timingSchedule
        self.asNeededBoolean = asNeededBoolean
        self.asNeededCodeableConcept = asNeededCodeableConcept
        self.site = site
        self.route = route
        self.method = method
        self.quantity = quantity
        self.rate = rate
        self.maxDosePerPeriod = maxDosePerPeriod
    def factory(*args_, **kwargs_):
        if MedicationDispense_Dosage.subclass:
            return MedicationDispense_Dosage.subclass(*args_, **kwargs_)
        else:
            return MedicationDispense_Dosage(*args_, **kwargs_)
    factory = staticmethod(factory)
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
    def get_quantity(self): return self.quantity
    def set_quantity(self, quantity): self.quantity = quantity
    def get_rate(self): return self.rate
    def set_rate(self, rate): self.rate = rate
    def get_maxDosePerPeriod(self): return self.maxDosePerPeriod
    def set_maxDosePerPeriod(self, maxDosePerPeriod): self.maxDosePerPeriod = maxDosePerPeriod
    def hasContent_(self):
        if (
            self.additionalInstructions is not None or
            self.timingDateTime is not None or
            self.timingPeriod is not None or
            self.timingSchedule is not None or
            self.asNeededBoolean is not None or
            self.asNeededCodeableConcept is not None or
            self.site is not None or
            self.route is not None or
            self.method is not None or
            self.quantity is not None or
            self.rate is not None or
            self.maxDosePerPeriod is not None or
            super(MedicationDispense_Dosage, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='MedicationDispense.Dosage', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='MedicationDispense.Dosage')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='MedicationDispense.Dosage', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='MedicationDispense.Dosage'):
        super(MedicationDispense_Dosage, self).exportAttributes(outfile, level, already_processed, namespace_, name_='MedicationDispense.Dosage')
    def exportChildren(self, outfile, level, namespace_='', name_='MedicationDispense.Dosage', fromsubclass_=False, pretty_print=True):
        super(MedicationDispense_Dosage, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
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
        if self.quantity is not None:
            self.quantity.export(outfile, level, namespace_, name_='quantity', pretty_print=pretty_print)
        if self.rate is not None:
            self.rate.export(outfile, level, namespace_, name_='rate', pretty_print=pretty_print)
        if self.maxDosePerPeriod is not None:
            self.maxDosePerPeriod.export(outfile, level, namespace_, name_='maxDosePerPeriod', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='MedicationDispense.Dosage', mapping_=None):
        element = super(MedicationDispense_Dosage, self).to_etree(parent_element, name_, mapping_)
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
        super(MedicationDispense_Dosage, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'additionalInstructions':
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
        super(MedicationDispense_Dosage, self).buildChildren(child_, node, nodeName_, True)
# end class MedicationDispense_Dosage


class MedicationDispense_Substitution(BackboneElement):
    """Dispensing a medication to a named patient. This includes a
    description of the supply provided and the instructions for
    administering the medication."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, type_=None, reason=None, responsibleParty=None):
        self.original_tagname_ = None
        super(MedicationDispense_Substitution, self).__init__(id, extension, modifierExtension, )
        self.type_ = type_
        if reason is None:
            self.reason = []
        else:
            self.reason = reason
        if responsibleParty is None:
            self.responsibleParty = []
        else:
            self.responsibleParty = responsibleParty
    def factory(*args_, **kwargs_):
        if MedicationDispense_Substitution.subclass:
            return MedicationDispense_Substitution.subclass(*args_, **kwargs_)
        else:
            return MedicationDispense_Substitution(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_type(self): return self.type_
    def set_type(self, type_): self.type_ = type_
    def get_reason(self): return self.reason
    def set_reason(self, reason): self.reason = reason
    def add_reason(self, value): self.reason.append(value)
    def insert_reason(self, index, value): self.reason[index] = value
    def get_responsibleParty(self): return self.responsibleParty
    def set_responsibleParty(self, responsibleParty): self.responsibleParty = responsibleParty
    def add_responsibleParty(self, value): self.responsibleParty.append(value)
    def insert_responsibleParty(self, index, value): self.responsibleParty[index] = value
    def hasContent_(self):
        if (
            self.type_ is not None or
            self.reason or
            self.responsibleParty or
            super(MedicationDispense_Substitution, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='MedicationDispense.Substitution', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='MedicationDispense.Substitution')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='MedicationDispense.Substitution', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='MedicationDispense.Substitution'):
        super(MedicationDispense_Substitution, self).exportAttributes(outfile, level, already_processed, namespace_, name_='MedicationDispense.Substitution')
    def exportChildren(self, outfile, level, namespace_='', name_='MedicationDispense.Substitution', fromsubclass_=False, pretty_print=True):
        super(MedicationDispense_Substitution, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.type_ is not None:
            self.type_.export(outfile, level, namespace_, name_='type', pretty_print=pretty_print)
        for reason_ in self.reason:
            reason_.export(outfile, level, namespace_, name_='reason', pretty_print=pretty_print)
        for responsibleParty_ in self.responsibleParty:
            responsibleParty_.export(outfile, level, namespace_, name_='responsibleParty', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='MedicationDispense.Substitution', mapping_=None):
        element = super(MedicationDispense_Substitution, self).to_etree(parent_element, name_, mapping_)
        if self.type_ is not None:
            type__ = self.type_
            type__.to_etree(element, name_='type', mapping_=mapping_)
        for reason_ in self.reason:
            reason_.to_etree(element, name_='reason', mapping_=mapping_)
        for responsibleParty_ in self.responsibleParty:
            responsibleParty_.to_etree(element, name_='responsibleParty', mapping_=mapping_)
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
        super(MedicationDispense_Substitution, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'type':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.type_ = obj_
            obj_.original_tagname_ = 'type'
        elif nodeName_ == 'reason':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.reason.append(obj_)
            obj_.original_tagname_ = 'reason'
        elif nodeName_ == 'responsibleParty':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.responsibleParty.append(obj_)
            obj_.original_tagname_ = 'responsibleParty'
        super(MedicationDispense_Substitution, self).buildChildren(child_, node, nodeName_, True)
# end class MedicationDispense_Substitution


class MedicationDispenseStatus(Element):
    """A code specifying the state of the dispense event.If the element is
    present, it must have either a @value, an @id, or extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(MedicationDispenseStatus, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if MedicationDispenseStatus.subclass:
            return MedicationDispenseStatus.subclass(*args_, **kwargs_)
        else:
            return MedicationDispenseStatus(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(MedicationDispenseStatus, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='MedicationDispenseStatus', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='MedicationDispenseStatus')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='MedicationDispenseStatus', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='MedicationDispenseStatus'):
        super(MedicationDispenseStatus, self).exportAttributes(outfile, level, already_processed, namespace_, name_='MedicationDispenseStatus')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='MedicationDispenseStatus', fromsubclass_=False, pretty_print=True):
        super(MedicationDispenseStatus, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='MedicationDispenseStatus', mapping_=None):
        element = super(MedicationDispenseStatus, self).to_etree(parent_element, name_, mapping_)
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
        super(MedicationDispenseStatus, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(MedicationDispenseStatus, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class MedicationDispenseStatus
