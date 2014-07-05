from .base_classes import *
from .support_functions import *


class MedicationStatement(Resource):
    """A record of medication being taken by a patient, or that the
    medication has been given to a patient where the record is the
    result of a report from the patient or another clinician.If the
    element is present, it must have either a @value, an @id, or
    extensions"""
    subclass = None
    superclass = Resource
    def __init__(self, id=None, extension=None, modifierExtension=None, language=None, text=None, contained=None, identifier=None, patient=None, wasNotGiven=None, reasonNotGiven=None, whenGiven=None, medication=None, device=None, dosage=None):
        self.original_tagname_ = None
        super(MedicationStatement, self).__init__(id, extension, modifierExtension, language, text, contained, )
        if identifier is None:
            self.identifier = []
        else:
            self.identifier = identifier
        self.patient = patient
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
        if MedicationStatement.subclass:
            return MedicationStatement.subclass(*args_, **kwargs_)
        else:
            return MedicationStatement(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_identifier(self): return self.identifier
    def set_identifier(self, identifier): self.identifier = identifier
    def add_identifier(self, value): self.identifier.append(value)
    def insert_identifier(self, index, value): self.identifier[index] = value
    def get_patient(self): return self.patient
    def set_patient(self, patient): self.patient = patient
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
            self.patient is not None or
            self.wasNotGiven is not None or
            self.reasonNotGiven or
            self.whenGiven is not None or
            self.medication is not None or
            self.device or
            self.dosage or
            super(MedicationStatement, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='MedicationStatement', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='MedicationStatement')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='MedicationStatement', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='MedicationStatement'):
        super(MedicationStatement, self).exportAttributes(outfile, level, already_processed, namespace_, name_='MedicationStatement')
    def exportChildren(self, outfile, level, namespace_='', name_='MedicationStatement', fromsubclass_=False, pretty_print=True):
        super(MedicationStatement, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for identifier_ in self.identifier:
            identifier_.export(outfile, level, namespace_, name_='identifier', pretty_print=pretty_print)
        if self.patient is not None:
            self.patient.export(outfile, level, namespace_, name_='patient', pretty_print=pretty_print)
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
    def to_etree(self, parent_element=None, name_='MedicationStatement', mapping_=None):
        element = super(MedicationStatement, self).to_etree(parent_element, name_, mapping_)
        for identifier_ in self.identifier:
            identifier_.to_etree(element, name_='identifier', mapping_=mapping_)
        if self.patient is not None:
            patient_ = self.patient
            patient_.to_etree(element, name_='patient', mapping_=mapping_)
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
        super(MedicationStatement, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'identifier':
            obj_ = Identifier.factory()
            obj_.build(child_)
            self.identifier.append(obj_)
            obj_.original_tagname_ = 'identifier'
        elif nodeName_ == 'patient':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.patient = obj_
            obj_.original_tagname_ = 'patient'
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
            obj_ = MedicationStatement_Dosage.factory()
            obj_.build(child_)
            self.dosage.append(obj_)
            obj_.original_tagname_ = 'dosage'
        super(MedicationStatement, self).buildChildren(child_, node, nodeName_, True)
# end class MedicationStatement


class MedicationStatement_Dosage(BackboneElement):
    """A record of medication being taken by a patient, or that the
    medication has been given to a patient where the record is the
    result of a report from the patient or another clinician.If set
    to true or if specified as a CodeableConcept, indicates that the
    medication is only taken when needed within the specified
    schedule rather than at every scheduled dose. If a
    CodeableConcept is present, it indicates the pre-condition for
    taking the Medication."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, timing=None, asNeededBoolean=None, asNeededCodeableConcept=None, site=None, route=None, method=None, quantity=None, rate=None, maxDosePerPeriod=None):
        self.original_tagname_ = None
        super(MedicationStatement_Dosage, self).__init__(id, extension, modifierExtension, )
        self.timing = timing
        self.asNeededBoolean = asNeededBoolean
        self.asNeededCodeableConcept = asNeededCodeableConcept
        self.site = site
        self.route = route
        self.method = method
        self.quantity = quantity
        self.rate = rate
        self.maxDosePerPeriod = maxDosePerPeriod
    def factory(*args_, **kwargs_):
        if MedicationStatement_Dosage.subclass:
            return MedicationStatement_Dosage.subclass(*args_, **kwargs_)
        else:
            return MedicationStatement_Dosage(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_timing(self): return self.timing
    def set_timing(self, timing): self.timing = timing
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
            self.timing is not None or
            self.asNeededBoolean is not None or
            self.asNeededCodeableConcept is not None or
            self.site is not None or
            self.route is not None or
            self.method is not None or
            self.quantity is not None or
            self.rate is not None or
            self.maxDosePerPeriod is not None or
            super(MedicationStatement_Dosage, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='MedicationStatement.Dosage', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='MedicationStatement.Dosage')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='MedicationStatement.Dosage', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='MedicationStatement.Dosage'):
        super(MedicationStatement_Dosage, self).exportAttributes(outfile, level, already_processed, namespace_, name_='MedicationStatement.Dosage')
    def exportChildren(self, outfile, level, namespace_='', name_='MedicationStatement.Dosage', fromsubclass_=False, pretty_print=True):
        super(MedicationStatement_Dosage, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.timing is not None:
            self.timing.export(outfile, level, namespace_, name_='timing', pretty_print=pretty_print)
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
    def to_etree(self, parent_element=None, name_='MedicationStatement.Dosage', mapping_=None):
        element = super(MedicationStatement_Dosage, self).to_etree(parent_element, name_, mapping_)
        if self.timing is not None:
            timing_ = self.timing
            timing_.to_etree(element, name_='timing', mapping_=mapping_)
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
        super(MedicationStatement_Dosage, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'timing':
            obj_ = Schedule.factory()
            obj_.build(child_)
            self.timing = obj_
            obj_.original_tagname_ = 'timing'
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
        super(MedicationStatement_Dosage, self).buildChildren(child_, node, nodeName_, True)
# end class MedicationStatement_Dosage
