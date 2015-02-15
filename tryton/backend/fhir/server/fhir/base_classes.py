from .support_functions import *
from .config import *
import re as re_
import base64
import datetime as datetime_


class GeneratedsSuper(object):
    tzoff_pattern = re_.compile(r'(\+|-)((0\d|1[0-3]):[0-5]\d|14:00)$')
    class _FixedOffsetTZ(datetime_.tzinfo):
        def __init__(self, offset, name):
            self.__offset = datetime_.timedelta(minutes=offset)
            self.__name = name
        def utcoffset(self, dt):
            return self.__offset
        def tzname(self, dt):
            return self.__name
        def dst(self, dt):
            return None
    def gds_format_string(self, input_data, input_name=''):
        return input_data
    def gds_validate_string(self, input_data, node, input_name=''):
        if not input_data:
            return ''
        else:
            return input_data
    def gds_format_base64(self, input_data, input_name=''):
        return base64.b64encode(input_data)
    def gds_validate_base64(self, input_data, node, input_name=''):
        return input_data
    def gds_format_integer(self, input_data, input_name=''):
        return '%d' % input_data
    def gds_validate_integer(self, input_data, node, input_name=''):
        return input_data
    def gds_format_integer_list(self, input_data, input_name=''):
        return '%s' % input_data
    def gds_validate_integer_list(self, input_data, node, input_name=''):
        values = input_data.split()
        for value in values:
            try:
                float(value)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires sequence of integers')
        return input_data
    def gds_format_float(self, input_data, input_name=''):
        return ('%.15f' % input_data).rstrip('0')
    def gds_validate_float(self, input_data, node, input_name=''):
        return input_data
    def gds_format_float_list(self, input_data, input_name=''):
        return '%s' % input_data
    def gds_validate_float_list(self, input_data, node, input_name=''):
        values = input_data.split()
        for value in values:
            try:
                float(value)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires sequence of floats')
        return input_data
    def gds_format_double(self, input_data, input_name=''):
        return '%e' % input_data
    def gds_validate_double(self, input_data, node, input_name=''):
        return input_data
    def gds_format_double_list(self, input_data, input_name=''):
        return '%s' % input_data
    def gds_validate_double_list(self, input_data, node, input_name=''):
        values = input_data.split()
        for value in values:
            try:
                float(value)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires sequence of doubles')
        return input_data
    def gds_format_boolean(self, input_data, input_name=''):
        return ('%s' % input_data).lower()
    def gds_validate_boolean(self, input_data, node, input_name=''):
        return input_data
    def gds_format_boolean_list(self, input_data, input_name=''):
        return '%s' % input_data
    def gds_validate_boolean_list(self, input_data, node, input_name=''):
        values = input_data.split()
        for value in values:
            if value not in ('true', '1', 'false', '0', ):
                raise_parse_error(
                    node,
                    'Requires sequence of booleans '
                    '("true", "1", "false", "0")')
        return input_data
    def gds_validate_datetime(self, input_data, node, input_name=''):
        return input_data
    def gds_format_datetime(self, input_data, input_name=''):
        if input_data.microsecond == 0:
            _svalue = '%04d-%02d-%02dT%02d:%02d:%02d' % (
                input_data.year,
                input_data.month,
                input_data.day,
                input_data.hour,
                input_data.minute,
                input_data.second,
            )
        else:
            _svalue = '%04d-%02d-%02dT%02d:%02d:%02d.%s' % (
                input_data.year,
                input_data.month,
                input_data.day,
                input_data.hour,
                input_data.minute,
                input_data.second,
                ('%f' % (float(input_data.microsecond) / 1000000))[2:],
            )
        if input_data.tzinfo is not None:
            tzoff = input_data.tzinfo.utcoffset(input_data)
            if tzoff is not None:
                total_seconds = tzoff.seconds + (86400 * tzoff.days)
                if total_seconds == 0:
                    _svalue += 'Z'
                else:
                    if total_seconds < 0:
                        _svalue += '-'
                        total_seconds *= -1
                    else:
                        _svalue += '+'
                    hours = total_seconds // 3600
                    minutes = (total_seconds - (hours * 3600)) // 60
                    _svalue += '{0:02d}:{1:02d}'.format(hours, minutes)
        return _svalue
    @classmethod
    def gds_parse_datetime(cls, input_data):
        tz = None
        if input_data[-1] == 'Z':
            tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
            input_data = input_data[:-1]
        else:
            results = GeneratedsSuper.tzoff_pattern.search(input_data)
            if results is not None:
                tzoff_parts = results.group(2).split(':')
                tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                if results.group(1) == '-':
                    tzoff *= -1
                tz = GeneratedsSuper._FixedOffsetTZ(
                    tzoff, results.group(0))
                input_data = input_data[:-6]
        if len(input_data.split('.')) > 1:
            dt = datetime_.datetime.strptime(
                input_data, '%Y-%m-%dT%H:%M:%S.%f')
        else:
            dt = datetime_.datetime.strptime(
                input_data, '%Y-%m-%dT%H:%M:%S')
        dt = dt.replace(tzinfo=tz)
        return dt
    def gds_validate_date(self, input_data, node, input_name=''):
        return input_data
    def gds_format_date(self, input_data, input_name=''):
        _svalue = '%04d-%02d-%02d' % (
            input_data.year,
            input_data.month,
            input_data.day,
        )
        try:
            if input_data.tzinfo is not None:
                tzoff = input_data.tzinfo.utcoffset(input_data)
                if tzoff is not None:
                    total_seconds = tzoff.seconds + (86400 * tzoff.days)
                    if total_seconds == 0:
                        _svalue += 'Z'
                    else:
                        if total_seconds < 0:
                            _svalue += '-'
                            total_seconds *= -1
                        else:
                            _svalue += '+'
                        hours = total_seconds // 3600
                        minutes = (total_seconds - (hours * 3600)) // 60
                        _svalue += '{0:02d}:{1:02d}'.format(hours, minutes)
        except AttributeError:
            pass
        return _svalue
    @classmethod
    def gds_parse_date(cls, input_data):
        tz = None
        if input_data[-1] == 'Z':
            tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
            input_data = input_data[:-1]
        else:
            results = GeneratedsSuper.tzoff_pattern.search(input_data)
            if results is not None:
                tzoff_parts = results.group(2).split(':')
                tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                if results.group(1) == '-':
                    tzoff *= -1
                tz = GeneratedsSuper._FixedOffsetTZ(
                    tzoff, results.group(0))
                input_data = input_data[:-6]
        dt = datetime_.datetime.strptime(input_data, '%Y-%m-%d')
        dt = dt.replace(tzinfo=tz)
        return dt.date()
    def gds_validate_time(self, input_data, node, input_name=''):
        return input_data
    def gds_format_time(self, input_data, input_name=''):
        if input_data.microsecond == 0:
            _svalue = '%02d:%02d:%02d' % (
                input_data.hour,
                input_data.minute,
                input_data.second,
            )
        else:
            _svalue = '%02d:%02d:%02d.%s' % (
                input_data.hour,
                input_data.minute,
                input_data.second,
                ('%f' % (float(input_data.microsecond) / 1000000))[2:],
            )
        if input_data.tzinfo is not None:
            tzoff = input_data.tzinfo.utcoffset(input_data)
            if tzoff is not None:
                total_seconds = tzoff.seconds + (86400 * tzoff.days)
                if total_seconds == 0:
                    _svalue += 'Z'
                else:
                    if total_seconds < 0:
                        _svalue += '-'
                        total_seconds *= -1
                    else:
                        _svalue += '+'
                    hours = total_seconds // 3600
                    minutes = (total_seconds - (hours * 3600)) // 60
                    _svalue += '{0:02d}:{1:02d}'.format(hours, minutes)
        return _svalue
    @classmethod
    def gds_parse_time(cls, input_data):
        tz = None
        if input_data[-1] == 'Z':
            tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
            input_data = input_data[:-1]
        else:
            results = GeneratedsSuper.tzoff_pattern.search(input_data)
            if results is not None:
                tzoff_parts = results.group(2).split(':')
                tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                if results.group(1) == '-':
                    tzoff *= -1
                tz = GeneratedsSuper._FixedOffsetTZ(
                    tzoff, results.group(0))
                input_data = input_data[:-6]
        if len(input_data.split('.')) > 1:
            dt = datetime_.datetime.strptime(input_data, '%H:%M:%S.%f')
        else:
            dt = datetime_.datetime.strptime(input_data, '%H:%M:%S')
        dt = dt.replace(tzinfo=tz)
        return dt.time()
    def gds_str_lower(self, instring):
        return instring.lower()
    def get_path_(self, node):
        path_list = []
        self.get_path_list_(node, path_list)
        path_list.reverse()
        path = '/'.join(path_list)
        return path
    Tag_strip_pattern_ = re_.compile(r'\{.*\}')
    def get_path_list_(self, node, path_list):
        if node is None:
            return
        tag = GeneratedsSuper.Tag_strip_pattern_.sub('', node.tag)
        if tag:
            path_list.append(tag)
        self.get_path_list_(node.getparent(), path_list)
    def get_class_obj_(self, node, default_class=None):
        class_obj1 = default_class
        if 'xsi' in node.nsmap:
            classname = node.get('{%s}type' % node.nsmap['xsi'])
            if classname is not None:
                names = classname.split(':')
                if len(names) == 2:
                    classname = names[1]
                class_obj2 = globals().get(classname)
                if class_obj2 is not None:
                    class_obj1 = class_obj2
        return class_obj1
    def gds_build_any(self, node, type_name=None):
        return None
    @classmethod
    def gds_reverse_node_mapping(cls, mapping):
        return dict(((v, k) for k, v in mapping.items()))


class Element(GeneratedsSuper):
    """The base element used for all FHIR elements and resources - allows
    for them to be extended with extensions"""
    subclass = None
    superclass = None
    def __init__(self, id=None, extension=None):
        self.original_tagname_ = None
        self.id = _cast(None, id)
        if extension is None:
            self.extension = []
        else:
            self.extension = extension
    def factory(*args_, **kwargs_):
        if Element.subclass:
            return Element.subclass(*args_, **kwargs_)
        else:
            return Element(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_extension(self): return self.extension
    def set_extension(self, extension): self.extension = extension
    def add_extension(self, value): self.extension.append(value)
    def insert_extension(self, index, value): self.extension[index] = value
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def hasContent_(self):
        if (
            self.extension
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Element', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Element')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Element', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Element'):
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (quote_attrib(self.id), ))
    def exportChildren(self, outfile, level, namespace_='', name_='Element', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for extension_ in self.extension:
            extension_.export(outfile, level, namespace_, name_='extension', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Element', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://hl7.org/fhir}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://hl7.org/fhir}' + name_)
        if self.id is not None:
            element.set('id', self.id)
        for extension_ in self.extension:
            extension_.to_etree(element, name_='extension', mapping_=mapping_)
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
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'extension':
            obj_ = Extension.factory()
            obj_.build(child_)
            self.extension.append(obj_)
            obj_.original_tagname_ = 'extension'
# end class Element


class BackboneElement(Element):
    """An element defined in a FHIR resources - can have modifierExtension
    elements"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, modifierExtension=None):
        self.original_tagname_ = None
        super(BackboneElement, self).__init__(id, extension, )
        if modifierExtension is None:
            self.modifierExtension = []
        else:
            self.modifierExtension = modifierExtension
    def factory(*args_, **kwargs_):
        if BackboneElement.subclass:
            return BackboneElement.subclass(*args_, **kwargs_)
        else:
            return BackboneElement(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_modifierExtension(self): return self.modifierExtension
    def set_modifierExtension(self, modifierExtension): self.modifierExtension = modifierExtension
    def add_modifierExtension(self, value): self.modifierExtension.append(value)
    def insert_modifierExtension(self, index, value): self.modifierExtension[index] = value
    def hasContent_(self):
        if (
            self.modifierExtension or
            super(BackboneElement, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='BackboneElement', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='BackboneElement')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='BackboneElement', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='BackboneElement'):
        super(BackboneElement, self).exportAttributes(outfile, level, already_processed, namespace_, name_='BackboneElement')
    def exportChildren(self, outfile, level, namespace_='', name_='BackboneElement', fromsubclass_=False, pretty_print=True):
        super(BackboneElement, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for modifierExtension_ in self.modifierExtension:
            modifierExtension_.export(outfile, level, namespace_, name_='modifierExtension', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='BackboneElement', mapping_=None):
        element = super(BackboneElement, self).to_etree(parent_element, name_, mapping_)
        for modifierExtension_ in self.modifierExtension:
            modifierExtension_.to_etree(element, name_='modifierExtension', mapping_=mapping_)
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
        super(BackboneElement, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'modifierExtension':
            obj_ = Extension.factory()
            obj_.build(child_)
            self.modifierExtension.append(obj_)
            obj_.original_tagname_ = 'modifierExtension'
        super(BackboneElement, self).buildChildren(child_, node, nodeName_, True)
# end class BackboneElement


class Resource_Inline(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, Binary=None, Provenance=None, Condition=None, CarePlan=None, Supply=None, Device=None, Query=None, Order=None, Organization=None, Procedure=None, Substance=None, DiagnosticReport=None, Group=None, ValueSet=None, Medication=None, MessageHeader=None, ImmunizationRecommendation=None, DocumentManifest=None, MedicationDispense=None, MedicationPrescription=None, MedicationAdministration=None, Encounter=None, SecurityEvent=None, MedicationStatement=None, List=None, Questionnaire=None, Composition=None, DeviceObservationReport=None, OperationOutcome=None, Conformance=None, Media=None, FamilyHistory=None, Other=None, Profile=None, Location=None, Observation=None, AllergyIntolerance=None, DocumentReference=None, Immunization=None, RelatedPerson=None, Specimen=None, OrderResponse=None, Alert=None, ConceptMap=None, Patient=None, Practitioner=None, AdverseReaction=None, ImagingStudy=None, DiagnosticOrder=None):
        self.original_tagname_ = None
        self.Binary = Binary
        self.Provenance = Provenance
        self.Condition = Condition
        self.CarePlan = CarePlan
        self.Supply = Supply
        self.Device = Device
        self.Query = Query
        self.Order = Order
        self.Organization = Organization
        self.Procedure = Procedure
        self.Substance = Substance
        self.DiagnosticReport = DiagnosticReport
        self.Group = Group
        self.ValueSet = ValueSet
        self.Medication = Medication
        self.MessageHeader = MessageHeader
        self.ImmunizationRecommendation = ImmunizationRecommendation
        self.DocumentManifest = DocumentManifest
        self.MedicationDispense = MedicationDispense
        self.MedicationPrescription = MedicationPrescription
        self.MedicationAdministration = MedicationAdministration
        self.Encounter = Encounter
        self.SecurityEvent = SecurityEvent
        self.MedicationStatement = MedicationStatement
        self.List = List
        self.Questionnaire = Questionnaire
        self.Composition = Composition
        self.DeviceObservationReport = DeviceObservationReport
        self.OperationOutcome = OperationOutcome
        self.Conformance = Conformance
        self.Media = Media
        self.FamilyHistory = FamilyHistory
        self.Other = Other
        self.Profile = Profile
        self.Location = Location
        self.Observation = Observation
        self.AllergyIntolerance = AllergyIntolerance
        self.DocumentReference = DocumentReference
        self.Immunization = Immunization
        self.RelatedPerson = RelatedPerson
        self.Specimen = Specimen
        self.OrderResponse = OrderResponse
        self.Alert = Alert
        self.ConceptMap = ConceptMap
        self.Patient = Patient
        self.Practitioner = Practitioner
        self.AdverseReaction = AdverseReaction
        self.ImagingStudy = ImagingStudy
        self.DiagnosticOrder = DiagnosticOrder
    def factory(*args_, **kwargs_):
        if Resource_Inline.subclass:
            return Resource_Inline.subclass(*args_, **kwargs_)
        else:
            return Resource_Inline(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Binary(self): return self.Binary
    def set_Binary(self, Binary): self.Binary = Binary
    def get_Provenance(self): return self.Provenance
    def set_Provenance(self, Provenance): self.Provenance = Provenance
    def get_Condition(self): return self.Condition
    def set_Condition(self, Condition): self.Condition = Condition
    def get_CarePlan(self): return self.CarePlan
    def set_CarePlan(self, CarePlan): self.CarePlan = CarePlan
    def get_Supply(self): return self.Supply
    def set_Supply(self, Supply): self.Supply = Supply
    def get_Device(self): return self.Device
    def set_Device(self, Device): self.Device = Device
    def get_Query(self): return self.Query
    def set_Query(self, Query): self.Query = Query
    def get_Order(self): return self.Order
    def set_Order(self, Order): self.Order = Order
    def get_Organization(self): return self.Organization
    def set_Organization(self, Organization): self.Organization = Organization
    def get_Procedure(self): return self.Procedure
    def set_Procedure(self, Procedure): self.Procedure = Procedure
    def get_Substance(self): return self.Substance
    def set_Substance(self, Substance): self.Substance = Substance
    def get_DiagnosticReport(self): return self.DiagnosticReport
    def set_DiagnosticReport(self, DiagnosticReport): self.DiagnosticReport = DiagnosticReport
    def get_Group(self): return self.Group
    def set_Group(self, Group): self.Group = Group
    def get_ValueSet(self): return self.ValueSet
    def set_ValueSet(self, ValueSet): self.ValueSet = ValueSet
    def get_Medication(self): return self.Medication
    def set_Medication(self, Medication): self.Medication = Medication
    def get_MessageHeader(self): return self.MessageHeader
    def set_MessageHeader(self, MessageHeader): self.MessageHeader = MessageHeader
    def get_ImmunizationRecommendation(self): return self.ImmunizationRecommendation
    def set_ImmunizationRecommendation(self, ImmunizationRecommendation): self.ImmunizationRecommendation = ImmunizationRecommendation
    def get_DocumentManifest(self): return self.DocumentManifest
    def set_DocumentManifest(self, DocumentManifest): self.DocumentManifest = DocumentManifest
    def get_MedicationDispense(self): return self.MedicationDispense
    def set_MedicationDispense(self, MedicationDispense): self.MedicationDispense = MedicationDispense
    def get_MedicationPrescription(self): return self.MedicationPrescription
    def set_MedicationPrescription(self, MedicationPrescription): self.MedicationPrescription = MedicationPrescription
    def get_MedicationAdministration(self): return self.MedicationAdministration
    def set_MedicationAdministration(self, MedicationAdministration): self.MedicationAdministration = MedicationAdministration
    def get_Encounter(self): return self.Encounter
    def set_Encounter(self, Encounter): self.Encounter = Encounter
    def get_SecurityEvent(self): return self.SecurityEvent
    def set_SecurityEvent(self, SecurityEvent): self.SecurityEvent = SecurityEvent
    def get_MedicationStatement(self): return self.MedicationStatement
    def set_MedicationStatement(self, MedicationStatement): self.MedicationStatement = MedicationStatement
    def get_List(self): return self.List
    def set_List(self, List): self.List = List
    def get_Questionnaire(self): return self.Questionnaire
    def set_Questionnaire(self, Questionnaire): self.Questionnaire = Questionnaire
    def get_Composition(self): return self.Composition
    def set_Composition(self, Composition): self.Composition = Composition
    def get_DeviceObservationReport(self): return self.DeviceObservationReport
    def set_DeviceObservationReport(self, DeviceObservationReport): self.DeviceObservationReport = DeviceObservationReport
    def get_OperationOutcome(self): return self.OperationOutcome
    def set_OperationOutcome(self, OperationOutcome): self.OperationOutcome = OperationOutcome
    def get_Conformance(self): return self.Conformance
    def set_Conformance(self, Conformance): self.Conformance = Conformance
    def get_Media(self): return self.Media
    def set_Media(self, Media): self.Media = Media
    def get_FamilyHistory(self): return self.FamilyHistory
    def set_FamilyHistory(self, FamilyHistory): self.FamilyHistory = FamilyHistory
    def get_Other(self): return self.Other
    def set_Other(self, Other): self.Other = Other
    def get_Profile(self): return self.Profile
    def set_Profile(self, Profile): self.Profile = Profile
    def get_Location(self): return self.Location
    def set_Location(self, Location): self.Location = Location
    def get_Observation(self): return self.Observation
    def set_Observation(self, Observation): self.Observation = Observation
    def get_AllergyIntolerance(self): return self.AllergyIntolerance
    def set_AllergyIntolerance(self, AllergyIntolerance): self.AllergyIntolerance = AllergyIntolerance
    def get_DocumentReference(self): return self.DocumentReference
    def set_DocumentReference(self, DocumentReference): self.DocumentReference = DocumentReference
    def get_Immunization(self): return self.Immunization
    def set_Immunization(self, Immunization): self.Immunization = Immunization
    def get_RelatedPerson(self): return self.RelatedPerson
    def set_RelatedPerson(self, RelatedPerson): self.RelatedPerson = RelatedPerson
    def get_Specimen(self): return self.Specimen
    def set_Specimen(self, Specimen): self.Specimen = Specimen
    def get_OrderResponse(self): return self.OrderResponse
    def set_OrderResponse(self, OrderResponse): self.OrderResponse = OrderResponse
    def get_Alert(self): return self.Alert
    def set_Alert(self, Alert): self.Alert = Alert
    def get_ConceptMap(self): return self.ConceptMap
    def set_ConceptMap(self, ConceptMap): self.ConceptMap = ConceptMap
    def get_Patient(self): return self.Patient
    def set_Patient(self, Patient): self.Patient = Patient
    def get_Practitioner(self): return self.Practitioner
    def set_Practitioner(self, Practitioner): self.Practitioner = Practitioner
    def get_AdverseReaction(self): return self.AdverseReaction
    def set_AdverseReaction(self, AdverseReaction): self.AdverseReaction = AdverseReaction
    def get_ImagingStudy(self): return self.ImagingStudy
    def set_ImagingStudy(self, ImagingStudy): self.ImagingStudy = ImagingStudy
    def get_DiagnosticOrder(self): return self.DiagnosticOrder
    def set_DiagnosticOrder(self, DiagnosticOrder): self.DiagnosticOrder = DiagnosticOrder
    def hasContent_(self):
        if (
            self.Binary is not None or
            self.Provenance is not None or
            self.Condition is not None or
            self.CarePlan is not None or
            self.Supply is not None or
            self.Device is not None or
            self.Query is not None or
            self.Order is not None or
            self.Organization is not None or
            self.Procedure is not None or
            self.Substance is not None or
            self.DiagnosticReport is not None or
            self.Group is not None or
            self.ValueSet is not None or
            self.Medication is not None or
            self.MessageHeader is not None or
            self.ImmunizationRecommendation is not None or
            self.DocumentManifest is not None or
            self.MedicationDispense is not None or
            self.MedicationPrescription is not None or
            self.MedicationAdministration is not None or
            self.Encounter is not None or
            self.SecurityEvent is not None or
            self.MedicationStatement is not None or
            self.List is not None or
            self.Questionnaire is not None or
            self.Composition is not None or
            self.DeviceObservationReport is not None or
            self.OperationOutcome is not None or
            self.Conformance is not None or
            self.Media is not None or
            self.FamilyHistory is not None or
            self.Other is not None or
            self.Profile is not None or
            self.Location is not None or
            self.Observation is not None or
            self.AllergyIntolerance is not None or
            self.DocumentReference is not None or
            self.Immunization is not None or
            self.RelatedPerson is not None or
            self.Specimen is not None or
            self.OrderResponse is not None or
            self.Alert is not None or
            self.ConceptMap is not None or
            self.Patient is not None or
            self.Practitioner is not None or
            self.AdverseReaction is not None or
            self.ImagingStudy is not None or
            self.DiagnosticOrder is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Resource.Inline', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Resource.Inline')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Resource.Inline', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Resource.Inline'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='Resource.Inline', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Binary is not None:
            self.Binary.export(outfile, level, namespace_, name_='Binary', pretty_print=pretty_print)
        if self.Provenance is not None:
            self.Provenance.export(outfile, level, namespace_, name_='Provenance', pretty_print=pretty_print)
        if self.Condition is not None:
            self.Condition.export(outfile, level, namespace_, name_='Condition', pretty_print=pretty_print)
        if self.CarePlan is not None:
            self.CarePlan.export(outfile, level, namespace_, name_='CarePlan', pretty_print=pretty_print)
        if self.Supply is not None:
            self.Supply.export(outfile, level, namespace_, name_='Supply', pretty_print=pretty_print)
        if self.Device is not None:
            self.Device.export(outfile, level, namespace_, name_='Device', pretty_print=pretty_print)
        if self.Query is not None:
            self.Query.export(outfile, level, namespace_, name_='Query', pretty_print=pretty_print)
        if self.Order is not None:
            self.Order.export(outfile, level, namespace_, name_='Order', pretty_print=pretty_print)
        if self.Organization is not None:
            self.Organization.export(outfile, level, namespace_, name_='Organization', pretty_print=pretty_print)
        if self.Procedure is not None:
            self.Procedure.export(outfile, level, namespace_, name_='Procedure', pretty_print=pretty_print)
        if self.Substance is not None:
            self.Substance.export(outfile, level, namespace_, name_='Substance', pretty_print=pretty_print)
        if self.DiagnosticReport is not None:
            self.DiagnosticReport.export(outfile, level, namespace_, name_='DiagnosticReport', pretty_print=pretty_print)
        if self.Group is not None:
            self.Group.export(outfile, level, namespace_, name_='Group', pretty_print=pretty_print)
        if self.ValueSet is not None:
            self.ValueSet.export(outfile, level, namespace_, name_='ValueSet', pretty_print=pretty_print)
        if self.Medication is not None:
            self.Medication.export(outfile, level, namespace_, name_='Medication', pretty_print=pretty_print)
        if self.MessageHeader is not None:
            self.MessageHeader.export(outfile, level, namespace_, name_='MessageHeader', pretty_print=pretty_print)
        if self.ImmunizationRecommendation is not None:
            self.ImmunizationRecommendation.export(outfile, level, namespace_, name_='ImmunizationRecommendation', pretty_print=pretty_print)
        if self.DocumentManifest is not None:
            self.DocumentManifest.export(outfile, level, namespace_, name_='DocumentManifest', pretty_print=pretty_print)
        if self.MedicationDispense is not None:
            self.MedicationDispense.export(outfile, level, namespace_, name_='MedicationDispense', pretty_print=pretty_print)
        if self.MedicationPrescription is not None:
            self.MedicationPrescription.export(outfile, level, namespace_, name_='MedicationPrescription', pretty_print=pretty_print)
        if self.MedicationAdministration is not None:
            self.MedicationAdministration.export(outfile, level, namespace_, name_='MedicationAdministration', pretty_print=pretty_print)
        if self.Encounter is not None:
            self.Encounter.export(outfile, level, namespace_, name_='Encounter', pretty_print=pretty_print)
        if self.SecurityEvent is not None:
            self.SecurityEvent.export(outfile, level, namespace_, name_='SecurityEvent', pretty_print=pretty_print)
        if self.MedicationStatement is not None:
            self.MedicationStatement.export(outfile, level, namespace_, name_='MedicationStatement', pretty_print=pretty_print)
        if self.List is not None:
            self.List.export(outfile, level, namespace_, name_='List', pretty_print=pretty_print)
        if self.Questionnaire is not None:
            self.Questionnaire.export(outfile, level, namespace_, name_='Questionnaire', pretty_print=pretty_print)
        if self.Composition is not None:
            self.Composition.export(outfile, level, namespace_, name_='Composition', pretty_print=pretty_print)
        if self.DeviceObservationReport is not None:
            self.DeviceObservationReport.export(outfile, level, namespace_, name_='DeviceObservationReport', pretty_print=pretty_print)
        if self.OperationOutcome is not None:
            self.OperationOutcome.export(outfile, level, namespace_, name_='OperationOutcome', pretty_print=pretty_print)
        if self.Conformance is not None:
            self.Conformance.export(outfile, level, namespace_, name_='Conformance', pretty_print=pretty_print)
        if self.Media is not None:
            self.Media.export(outfile, level, namespace_, name_='Media', pretty_print=pretty_print)
        if self.FamilyHistory is not None:
            self.FamilyHistory.export(outfile, level, namespace_, name_='FamilyHistory', pretty_print=pretty_print)
        if self.Other is not None:
            self.Other.export(outfile, level, namespace_, name_='Other', pretty_print=pretty_print)
        if self.Profile is not None:
            self.Profile.export(outfile, level, namespace_, name_='Profile', pretty_print=pretty_print)
        if self.Location is not None:
            self.Location.export(outfile, level, namespace_, name_='Location', pretty_print=pretty_print)
        if self.Observation is not None:
            self.Observation.export(outfile, level, namespace_, name_='Observation', pretty_print=pretty_print)
        if self.AllergyIntolerance is not None:
            self.AllergyIntolerance.export(outfile, level, namespace_, name_='AllergyIntolerance', pretty_print=pretty_print)
        if self.DocumentReference is not None:
            self.DocumentReference.export(outfile, level, namespace_, name_='DocumentReference', pretty_print=pretty_print)
        if self.Immunization is not None:
            self.Immunization.export(outfile, level, namespace_, name_='Immunization', pretty_print=pretty_print)
        if self.RelatedPerson is not None:
            self.RelatedPerson.export(outfile, level, namespace_, name_='RelatedPerson', pretty_print=pretty_print)
        if self.Specimen is not None:
            self.Specimen.export(outfile, level, namespace_, name_='Specimen', pretty_print=pretty_print)
        if self.OrderResponse is not None:
            self.OrderResponse.export(outfile, level, namespace_, name_='OrderResponse', pretty_print=pretty_print)
        if self.Alert is not None:
            self.Alert.export(outfile, level, namespace_, name_='Alert', pretty_print=pretty_print)
        if self.ConceptMap is not None:
            self.ConceptMap.export(outfile, level, namespace_, name_='ConceptMap', pretty_print=pretty_print)
        if self.Patient is not None:
            self.Patient.export(outfile, level, namespace_, name_='Patient', pretty_print=pretty_print)
        if self.Practitioner is not None:
            self.Practitioner.export(outfile, level, namespace_, name_='Practitioner', pretty_print=pretty_print)
        if self.AdverseReaction is not None:
            self.AdverseReaction.export(outfile, level, namespace_, name_='AdverseReaction', pretty_print=pretty_print)
        if self.ImagingStudy is not None:
            self.ImagingStudy.export(outfile, level, namespace_, name_='ImagingStudy', pretty_print=pretty_print)
        if self.DiagnosticOrder is not None:
            self.DiagnosticOrder.export(outfile, level, namespace_, name_='DiagnosticOrder', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Resource.Inline', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://hl7.org/fhir}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://hl7.org/fhir}' + name_)
        if self.Binary is not None:
            Binary_ = self.Binary
            Binary_.to_etree(element, name_='Binary', mapping_=mapping_)
        if self.Provenance is not None:
            Provenance_ = self.Provenance
            Provenance_.to_etree(element, name_='Provenance', mapping_=mapping_)
        if self.Condition is not None:
            Condition_ = self.Condition
            Condition_.to_etree(element, name_='Condition', mapping_=mapping_)
        if self.CarePlan is not None:
            CarePlan_ = self.CarePlan
            CarePlan_.to_etree(element, name_='CarePlan', mapping_=mapping_)
        if self.Supply is not None:
            Supply_ = self.Supply
            Supply_.to_etree(element, name_='Supply', mapping_=mapping_)
        if self.Device is not None:
            Device_ = self.Device
            Device_.to_etree(element, name_='Device', mapping_=mapping_)
        if self.Query is not None:
            Query_ = self.Query
            Query_.to_etree(element, name_='Query', mapping_=mapping_)
        if self.Order is not None:
            Order_ = self.Order
            Order_.to_etree(element, name_='Order', mapping_=mapping_)
        if self.Organization is not None:
            Organization_ = self.Organization
            Organization_.to_etree(element, name_='Organization', mapping_=mapping_)
        if self.Procedure is not None:
            Procedure_ = self.Procedure
            Procedure_.to_etree(element, name_='Procedure', mapping_=mapping_)
        if self.Substance is not None:
            Substance_ = self.Substance
            Substance_.to_etree(element, name_='Substance', mapping_=mapping_)
        if self.DiagnosticReport is not None:
            DiagnosticReport_ = self.DiagnosticReport
            DiagnosticReport_.to_etree(element, name_='DiagnosticReport', mapping_=mapping_)
        if self.Group is not None:
            Group_ = self.Group
            Group_.to_etree(element, name_='Group', mapping_=mapping_)
        if self.ValueSet is not None:
            ValueSet_ = self.ValueSet
            ValueSet_.to_etree(element, name_='ValueSet', mapping_=mapping_)
        if self.Medication is not None:
            Medication_ = self.Medication
            Medication_.to_etree(element, name_='Medication', mapping_=mapping_)
        if self.MessageHeader is not None:
            MessageHeader_ = self.MessageHeader
            MessageHeader_.to_etree(element, name_='MessageHeader', mapping_=mapping_)
        if self.ImmunizationRecommendation is not None:
            ImmunizationRecommendation_ = self.ImmunizationRecommendation
            ImmunizationRecommendation_.to_etree(element, name_='ImmunizationRecommendation', mapping_=mapping_)
        if self.DocumentManifest is not None:
            DocumentManifest_ = self.DocumentManifest
            DocumentManifest_.to_etree(element, name_='DocumentManifest', mapping_=mapping_)
        if self.MedicationDispense is not None:
            MedicationDispense_ = self.MedicationDispense
            MedicationDispense_.to_etree(element, name_='MedicationDispense', mapping_=mapping_)
        if self.MedicationPrescription is not None:
            MedicationPrescription_ = self.MedicationPrescription
            MedicationPrescription_.to_etree(element, name_='MedicationPrescription', mapping_=mapping_)
        if self.MedicationAdministration is not None:
            MedicationAdministration_ = self.MedicationAdministration
            MedicationAdministration_.to_etree(element, name_='MedicationAdministration', mapping_=mapping_)
        if self.Encounter is not None:
            Encounter_ = self.Encounter
            Encounter_.to_etree(element, name_='Encounter', mapping_=mapping_)
        if self.SecurityEvent is not None:
            SecurityEvent_ = self.SecurityEvent
            SecurityEvent_.to_etree(element, name_='SecurityEvent', mapping_=mapping_)
        if self.MedicationStatement is not None:
            MedicationStatement_ = self.MedicationStatement
            MedicationStatement_.to_etree(element, name_='MedicationStatement', mapping_=mapping_)
        if self.List is not None:
            List_ = self.List
            List_.to_etree(element, name_='List', mapping_=mapping_)
        if self.Questionnaire is not None:
            Questionnaire_ = self.Questionnaire
            Questionnaire_.to_etree(element, name_='Questionnaire', mapping_=mapping_)
        if self.Composition is not None:
            Composition_ = self.Composition
            Composition_.to_etree(element, name_='Composition', mapping_=mapping_)
        if self.DeviceObservationReport is not None:
            DeviceObservationReport_ = self.DeviceObservationReport
            DeviceObservationReport_.to_etree(element, name_='DeviceObservationReport', mapping_=mapping_)
        if self.OperationOutcome is not None:
            OperationOutcome_ = self.OperationOutcome
            OperationOutcome_.to_etree(element, name_='OperationOutcome', mapping_=mapping_)
        if self.Conformance is not None:
            Conformance_ = self.Conformance
            Conformance_.to_etree(element, name_='Conformance', mapping_=mapping_)
        if self.Media is not None:
            Media_ = self.Media
            Media_.to_etree(element, name_='Media', mapping_=mapping_)
        if self.FamilyHistory is not None:
            FamilyHistory_ = self.FamilyHistory
            FamilyHistory_.to_etree(element, name_='FamilyHistory', mapping_=mapping_)
        if self.Other is not None:
            Other_ = self.Other
            Other_.to_etree(element, name_='Other', mapping_=mapping_)
        if self.Profile is not None:
            Profile_ = self.Profile
            Profile_.to_etree(element, name_='Profile', mapping_=mapping_)
        if self.Location is not None:
            Location_ = self.Location
            Location_.to_etree(element, name_='Location', mapping_=mapping_)
        if self.Observation is not None:
            Observation_ = self.Observation
            Observation_.to_etree(element, name_='Observation', mapping_=mapping_)
        if self.AllergyIntolerance is not None:
            AllergyIntolerance_ = self.AllergyIntolerance
            AllergyIntolerance_.to_etree(element, name_='AllergyIntolerance', mapping_=mapping_)
        if self.DocumentReference is not None:
            DocumentReference_ = self.DocumentReference
            DocumentReference_.to_etree(element, name_='DocumentReference', mapping_=mapping_)
        if self.Immunization is not None:
            Immunization_ = self.Immunization
            Immunization_.to_etree(element, name_='Immunization', mapping_=mapping_)
        if self.RelatedPerson is not None:
            RelatedPerson_ = self.RelatedPerson
            RelatedPerson_.to_etree(element, name_='RelatedPerson', mapping_=mapping_)
        if self.Specimen is not None:
            Specimen_ = self.Specimen
            Specimen_.to_etree(element, name_='Specimen', mapping_=mapping_)
        if self.OrderResponse is not None:
            OrderResponse_ = self.OrderResponse
            OrderResponse_.to_etree(element, name_='OrderResponse', mapping_=mapping_)
        if self.Alert is not None:
            Alert_ = self.Alert
            Alert_.to_etree(element, name_='Alert', mapping_=mapping_)
        if self.ConceptMap is not None:
            ConceptMap_ = self.ConceptMap
            ConceptMap_.to_etree(element, name_='ConceptMap', mapping_=mapping_)
        if self.Patient is not None:
            Patient_ = self.Patient
            Patient_.to_etree(element, name_='Patient', mapping_=mapping_)
        if self.Practitioner is not None:
            Practitioner_ = self.Practitioner
            Practitioner_.to_etree(element, name_='Practitioner', mapping_=mapping_)
        if self.AdverseReaction is not None:
            AdverseReaction_ = self.AdverseReaction
            AdverseReaction_.to_etree(element, name_='AdverseReaction', mapping_=mapping_)
        if self.ImagingStudy is not None:
            ImagingStudy_ = self.ImagingStudy
            ImagingStudy_.to_etree(element, name_='ImagingStudy', mapping_=mapping_)
        if self.DiagnosticOrder is not None:
            DiagnosticOrder_ = self.DiagnosticOrder
            DiagnosticOrder_.to_etree(element, name_='DiagnosticOrder', mapping_=mapping_)
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
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Binary':
            obj_ = Binary.factory()
            obj_.build(child_)
            self.Binary = obj_
            obj_.original_tagname_ = 'Binary'
        elif nodeName_ == 'Provenance':
            obj_ = Provenance.factory()
            obj_.build(child_)
            self.Provenance = obj_
            obj_.original_tagname_ = 'Provenance'
        elif nodeName_ == 'Condition':
            obj_ = Condition.factory()
            obj_.build(child_)
            self.Condition = obj_
            obj_.original_tagname_ = 'Condition'
        elif nodeName_ == 'CarePlan':
            obj_ = CarePlan.factory()
            obj_.build(child_)
            self.CarePlan = obj_
            obj_.original_tagname_ = 'CarePlan'
        elif nodeName_ == 'Supply':
            obj_ = Supply.factory()
            obj_.build(child_)
            self.Supply = obj_
            obj_.original_tagname_ = 'Supply'
        elif nodeName_ == 'Device':
            obj_ = Device.factory()
            obj_.build(child_)
            self.Device = obj_
            obj_.original_tagname_ = 'Device'
        elif nodeName_ == 'Query':
            obj_ = Query.factory()
            obj_.build(child_)
            self.Query = obj_
            obj_.original_tagname_ = 'Query'
        elif nodeName_ == 'Order':
            obj_ = Order.factory()
            obj_.build(child_)
            self.Order = obj_
            obj_.original_tagname_ = 'Order'
        elif nodeName_ == 'Organization':
            obj_ = Organization.factory()
            obj_.build(child_)
            self.Organization = obj_
            obj_.original_tagname_ = 'Organization'
        elif nodeName_ == 'Procedure':
            obj_ = Procedure.factory()
            obj_.build(child_)
            self.Procedure = obj_
            obj_.original_tagname_ = 'Procedure'
        elif nodeName_ == 'Substance':
            obj_ = Substance.factory()
            obj_.build(child_)
            self.Substance = obj_
            obj_.original_tagname_ = 'Substance'
        elif nodeName_ == 'DiagnosticReport':
            obj_ = DiagnosticReport.factory()
            obj_.build(child_)
            self.DiagnosticReport = obj_
            obj_.original_tagname_ = 'DiagnosticReport'
        elif nodeName_ == 'Group':
            obj_ = Group.factory()
            obj_.build(child_)
            self.Group = obj_
            obj_.original_tagname_ = 'Group'
        elif nodeName_ == 'ValueSet':
            obj_ = ValueSet.factory()
            obj_.build(child_)
            self.ValueSet = obj_
            obj_.original_tagname_ = 'ValueSet'
        elif nodeName_ == 'Medication':
            obj_ = Medication.factory()
            obj_.build(child_)
            self.Medication = obj_
            obj_.original_tagname_ = 'Medication'
        elif nodeName_ == 'MessageHeader':
            obj_ = MessageHeader.factory()
            obj_.build(child_)
            self.MessageHeader = obj_
            obj_.original_tagname_ = 'MessageHeader'
        elif nodeName_ == 'ImmunizationRecommendation':
            obj_ = ImmunizationRecommendation.factory()
            obj_.build(child_)
            self.ImmunizationRecommendation = obj_
            obj_.original_tagname_ = 'ImmunizationRecommendation'
        elif nodeName_ == 'DocumentManifest':
            obj_ = DocumentManifest.factory()
            obj_.build(child_)
            self.DocumentManifest = obj_
            obj_.original_tagname_ = 'DocumentManifest'
        elif nodeName_ == 'MedicationDispense':
            obj_ = MedicationDispense.factory()
            obj_.build(child_)
            self.MedicationDispense = obj_
            obj_.original_tagname_ = 'MedicationDispense'
        elif nodeName_ == 'MedicationPrescription':
            obj_ = MedicationPrescription.factory()
            obj_.build(child_)
            self.MedicationPrescription = obj_
            obj_.original_tagname_ = 'MedicationPrescription'
        elif nodeName_ == 'MedicationAdministration':
            obj_ = MedicationAdministration.factory()
            obj_.build(child_)
            self.MedicationAdministration = obj_
            obj_.original_tagname_ = 'MedicationAdministration'
        elif nodeName_ == 'Encounter':
            obj_ = Encounter.factory()
            obj_.build(child_)
            self.Encounter = obj_
            obj_.original_tagname_ = 'Encounter'
        elif nodeName_ == 'SecurityEvent':
            obj_ = SecurityEvent.factory()
            obj_.build(child_)
            self.SecurityEvent = obj_
            obj_.original_tagname_ = 'SecurityEvent'
        elif nodeName_ == 'MedicationStatement':
            obj_ = MedicationStatement.factory()
            obj_.build(child_)
            self.MedicationStatement = obj_
            obj_.original_tagname_ = 'MedicationStatement'
        elif nodeName_ == 'List':
            obj_ = List.factory()
            obj_.build(child_)
            self.List = obj_
            obj_.original_tagname_ = 'List'
        elif nodeName_ == 'Questionnaire':
            obj_ = Questionnaire.factory()
            obj_.build(child_)
            self.Questionnaire = obj_
            obj_.original_tagname_ = 'Questionnaire'
        elif nodeName_ == 'Composition':
            obj_ = Composition.factory()
            obj_.build(child_)
            self.Composition = obj_
            obj_.original_tagname_ = 'Composition'
        elif nodeName_ == 'DeviceObservationReport':
            obj_ = DeviceObservationReport.factory()
            obj_.build(child_)
            self.DeviceObservationReport = obj_
            obj_.original_tagname_ = 'DeviceObservationReport'
        elif nodeName_ == 'OperationOutcome':
            obj_ = OperationOutcome.factory()
            obj_.build(child_)
            self.OperationOutcome = obj_
            obj_.original_tagname_ = 'OperationOutcome'
        elif nodeName_ == 'Conformance':
            obj_ = Conformance.factory()
            obj_.build(child_)
            self.Conformance = obj_
            obj_.original_tagname_ = 'Conformance'
        elif nodeName_ == 'Media':
            obj_ = Media.factory()
            obj_.build(child_)
            self.Media = obj_
            obj_.original_tagname_ = 'Media'
        elif nodeName_ == 'FamilyHistory':
            obj_ = FamilyHistory.factory()
            obj_.build(child_)
            self.FamilyHistory = obj_
            obj_.original_tagname_ = 'FamilyHistory'
        elif nodeName_ == 'Other':
            obj_ = Other.factory()
            obj_.build(child_)
            self.Other = obj_
            obj_.original_tagname_ = 'Other'
        elif nodeName_ == 'Profile':
            obj_ = Profile.factory()
            obj_.build(child_)
            self.Profile = obj_
            obj_.original_tagname_ = 'Profile'
        elif nodeName_ == 'Location':
            obj_ = Location.factory()
            obj_.build(child_)
            self.Location = obj_
            obj_.original_tagname_ = 'Location'
        elif nodeName_ == 'Observation':
            obj_ = Observation.factory()
            obj_.build(child_)
            self.Observation = obj_
            obj_.original_tagname_ = 'Observation'
        elif nodeName_ == 'AllergyIntolerance':
            obj_ = AllergyIntolerance.factory()
            obj_.build(child_)
            self.AllergyIntolerance = obj_
            obj_.original_tagname_ = 'AllergyIntolerance'
        elif nodeName_ == 'DocumentReference':
            obj_ = DocumentReference.factory()
            obj_.build(child_)
            self.DocumentReference = obj_
            obj_.original_tagname_ = 'DocumentReference'
        elif nodeName_ == 'Immunization':
            obj_ = Immunization.factory()
            obj_.build(child_)
            self.Immunization = obj_
            obj_.original_tagname_ = 'Immunization'
        elif nodeName_ == 'RelatedPerson':
            obj_ = RelatedPerson.factory()
            obj_.build(child_)
            self.RelatedPerson = obj_
            obj_.original_tagname_ = 'RelatedPerson'
        elif nodeName_ == 'Specimen':
            obj_ = Specimen.factory()
            obj_.build(child_)
            self.Specimen = obj_
            obj_.original_tagname_ = 'Specimen'
        elif nodeName_ == 'OrderResponse':
            obj_ = OrderResponse.factory()
            obj_.build(child_)
            self.OrderResponse = obj_
            obj_.original_tagname_ = 'OrderResponse'
        elif nodeName_ == 'Alert':
            obj_ = Alert.factory()
            obj_.build(child_)
            self.Alert = obj_
            obj_.original_tagname_ = 'Alert'
        elif nodeName_ == 'ConceptMap':
            obj_ = ConceptMap.factory()
            obj_.build(child_)
            self.ConceptMap = obj_
            obj_.original_tagname_ = 'ConceptMap'
        elif nodeName_ == 'Patient':
            obj_ = Patient.factory()
            obj_.build(child_)
            self.Patient = obj_
            obj_.original_tagname_ = 'Patient'
        elif nodeName_ == 'Practitioner':
            obj_ = Practitioner.factory()
            obj_.build(child_)
            self.Practitioner = obj_
            obj_.original_tagname_ = 'Practitioner'
        elif nodeName_ == 'AdverseReaction':
            obj_ = AdverseReaction.factory()
            obj_.build(child_)
            self.AdverseReaction = obj_
            obj_.original_tagname_ = 'AdverseReaction'
        elif nodeName_ == 'ImagingStudy':
            obj_ = ImagingStudy.factory()
            obj_.build(child_)
            self.ImagingStudy = obj_
            obj_.original_tagname_ = 'ImagingStudy'
        elif nodeName_ == 'DiagnosticOrder':
            obj_ = DiagnosticOrder.factory()
            obj_.build(child_)
            self.DiagnosticOrder = obj_
            obj_.original_tagname_ = 'DiagnosticOrder'
# end class Resource_Inline


class Resource(BackboneElement):
    """The base resource declaration used for all FHIR resource types -
    adds Narrative and xml:lang"""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, language=None, text=None, contained=None):
        self.original_tagname_ = None
        super(Resource, self).__init__(id, extension, modifierExtension, )
        self.language = language
        self.text = text
        if contained is None:
            self.contained = []
        else:
            self.contained = contained
    def factory(*args_, **kwargs_):
        if Resource.subclass:
            return Resource.subclass(*args_, **kwargs_)
        else:
            return Resource(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_language(self): return self.language
    def set_language(self, language): self.language = language
    def get_text(self): return self.text
    def set_text(self, text): self.text = text
    def get_contained(self): return self.contained
    def set_contained(self, contained): self.contained = contained
    def add_contained(self, value): self.contained.append(value)
    def insert_contained(self, index, value): self.contained[index] = value
    def hasContent_(self):
        if (
            self.language is not None or
            self.text is not None or
            self.contained or
            super(Resource, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Resource', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Resource')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Resource', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Resource'):
        super(Resource, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Resource')
    def exportChildren(self, outfile, level, namespace_='', name_='Resource', fromsubclass_=False, pretty_print=True):
        super(Resource, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.language is not None:
            self.language.export(outfile, level, namespace_, name_='language', pretty_print=pretty_print)
        if self.text is not None:
            self.text.export(outfile, level, namespace_, name_='text', pretty_print=pretty_print)
        for contained_ in self.contained:
            contained_.export(outfile, level, namespace_, name_='contained', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Resource', mapping_=None):
        element = super(Resource, self).to_etree(parent_element, name_, mapping_)
        if self.language is not None:
            language_ = self.language
            language_.to_etree(element, name_='language', mapping_=mapping_)
        if self.text is not None:
            text_ = self.text
            text_.to_etree(element, name_='text', mapping_=mapping_)
        for contained_ in self.contained:
            contained_.to_etree(element, name_='contained', mapping_=mapping_)
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
        super(Resource, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'language':
            obj_ = code.factory()
            obj_.build(child_)
            self.language = obj_
            obj_.original_tagname_ = 'language'
        elif nodeName_ == 'text':
            obj_ = Narrative.factory()
            obj_.build(child_)
            self.text = obj_
            obj_.original_tagname_ = 'text'
        elif nodeName_ == 'contained':
            obj_ = Resource_Inline.factory()
            obj_.build(child_)
            self.contained.append(obj_)
            obj_.original_tagname_ = 'contained'
        super(Resource, self).buildChildren(child_, node, nodeName_, True)
# end class Resource


class Inline(GeneratedsSuper):
    """ "Inline" covers inline or "text-level" elements """
    subclass = None
    superclass = None
    def __init__(self, a=None, br=None, span=None, bdo=None, map=None, img=None, tt=None, i=None, b=None, big=None, small=None, em=None, strong=None, dfn=None, code=None, q=None, samp=None, kbd=None, var=None, cite=None, abbr=None, acronym=None, sub=None, sup=None, valueOf_=None, mixedclass_=None, content_=None, extensiontype_=None):
        self.original_tagname_ = None
        self.a = a
        self.br = br
        self.span = span
        self.bdo = bdo
        self.map = map
        self.img = img
        self.tt = tt
        self.i = i
        self.b = b
        self.big = big
        self.small = small
        self.em = em
        self.strong = strong
        self.dfn = dfn
        self.code = code
        self.q = q
        self.samp = samp
        self.kbd = kbd
        self.var = var
        self.cite = cite
        self.abbr = abbr
        self.acronym = acronym
        self.sub = sub
        self.sup = sup
        self.valueOf_ = valueOf_
        self.extensiontype_ = extensiontype_
        if mixedclass_ is None:
            self.mixedclass_ = MixedContainer
        else:
            self.mixedclass_ = mixedclass_
        if content_ is None:
            self.content_ = []
        else:
            self.content_ = content_
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if Inline.subclass:
            return Inline.subclass(*args_, **kwargs_)
        else:
            return Inline(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_a(self): return self.a
    def set_a(self, a): self.a = a
    def get_br(self): return self.br
    def set_br(self, br): self.br = br
    def get_span(self): return self.span
    def set_span(self, span): self.span = span
    def get_bdo(self): return self.bdo
    def set_bdo(self, bdo): self.bdo = bdo
    def get_map(self): return self.map
    def set_map(self, map): self.map = map
    def get_img(self): return self.img
    def set_img(self, img): self.img = img
    def get_tt(self): return self.tt
    def set_tt(self, tt): self.tt = tt
    def get_i(self): return self.i
    def set_i(self, i): self.i = i
    def get_b(self): return self.b
    def set_b(self, b): self.b = b
    def get_big(self): return self.big
    def set_big(self, big): self.big = big
    def get_small(self): return self.small
    def set_small(self, small): self.small = small
    def get_em(self): return self.em
    def set_em(self, em): self.em = em
    def get_strong(self): return self.strong
    def set_strong(self, strong): self.strong = strong
    def get_dfn(self): return self.dfn
    def set_dfn(self, dfn): self.dfn = dfn
    def get_code(self): return self.code
    def set_code(self, code): self.code = code
    def get_q(self): return self.q
    def set_q(self, q): self.q = q
    def get_samp(self): return self.samp
    def set_samp(self, samp): self.samp = samp
    def get_kbd(self): return self.kbd
    def set_kbd(self, kbd): self.kbd = kbd
    def get_var(self): return self.var
    def set_var(self, var): self.var = var
    def get_cite(self): return self.cite
    def set_cite(self, cite): self.cite = cite
    def get_abbr(self): return self.abbr
    def set_abbr(self, abbr): self.abbr = abbr
    def get_acronym(self): return self.acronym
    def set_acronym(self, acronym): self.acronym = acronym
    def get_sub(self): return self.sub
    def set_sub(self, sub): self.sub = sub
    def get_sup(self): return self.sup
    def set_sup(self, sup): self.sup = sup
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def get_extensiontype_(self): return self.extensiontype_
    def set_extensiontype_(self, extensiontype_): self.extensiontype_ = extensiontype_
    def hasContent_(self):
        if (
            self.a is not None or
            self.br is not None or
            self.span is not None or
            self.bdo is not None or
            self.map is not None or
            self.img is not None or
            self.tt is not None or
            self.i is not None or
            self.b is not None or
            self.big is not None or
            self.small is not None or
            self.em is not None or
            self.strong is not None or
            self.dfn is not None or
            self.code is not None or
            self.q is not None or
            self.samp is not None or
            self.kbd is not None or
            self.var is not None or
            self.cite is not None or
            self.abbr is not None or
            self.acronym is not None or
            self.sub is not None or
            self.sup is not None or
            self.valueOf_
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Inline', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Inline')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Inline', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Inline'):
        if self.extensiontype_ is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            outfile.write(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            outfile.write(' xsi:type="%s"' % self.extensiontype_)
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='Inline', fromsubclass_=False, pretty_print=True):
        if not fromsubclass_:
            for item_ in self.content_:
                item_.export(outfile, level, item_.name, namespace_, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Inline', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://hl7.org/fhir}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://hl7.org/fhir}' + name_)
        if self.extensiontype_ is not None:
            element.set('{http://www.w3.org/2001/XMLSchema-instance}type', self.extensiontype_)
        for item_ in self.content_:
            item_.to_etree(element)
        if mapping_ is not None:
            mapping_[self] = element
        return element
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        if node.text is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', node.text)
            self.content_.append(obj_)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('xsi:type', node)
        if value is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            self.extensiontype_ = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'a':
            obj_ = a.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'a', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_a'):
              self.add_a(obj_.value)
            elif hasattr(self, 'set_a'):
              self.set_a(obj_.value)
        elif nodeName_ == 'br':
            obj_ = br.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'br', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_br'):
              self.add_br(obj_.value)
            elif hasattr(self, 'set_br'):
              self.set_br(obj_.value)
        elif nodeName_ == 'span':
            obj_ = span.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'span', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_span'):
              self.add_span(obj_.value)
            elif hasattr(self, 'set_span'):
              self.set_span(obj_.value)
        elif nodeName_ == 'bdo':
            obj_ = bdo.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'bdo', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_bdo'):
              self.add_bdo(obj_.value)
            elif hasattr(self, 'set_bdo'):
              self.set_bdo(obj_.value)
        elif nodeName_ == 'map':
            obj_ = map.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'map', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_map'):
              self.add_map(obj_.value)
            elif hasattr(self, 'set_map'):
              self.set_map(obj_.value)
        elif nodeName_ == 'img':
            obj_ = img.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'img', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_img'):
              self.add_img(obj_.value)
            elif hasattr(self, 'set_img'):
              self.set_img(obj_.value)
        elif nodeName_ == 'tt':
            obj_ = tt.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'tt', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_tt'):
              self.add_tt(obj_.value)
            elif hasattr(self, 'set_tt'):
              self.set_tt(obj_.value)
        elif nodeName_ == 'i':
            obj_ = i.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'i', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_i'):
              self.add_i(obj_.value)
            elif hasattr(self, 'set_i'):
              self.set_i(obj_.value)
        elif nodeName_ == 'b':
            obj_ = b.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'b', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_b'):
              self.add_b(obj_.value)
            elif hasattr(self, 'set_b'):
              self.set_b(obj_.value)
        elif nodeName_ == 'big':
            obj_ = big.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'big', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_big'):
              self.add_big(obj_.value)
            elif hasattr(self, 'set_big'):
              self.set_big(obj_.value)
        elif nodeName_ == 'small':
            obj_ = small.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'small', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_small'):
              self.add_small(obj_.value)
            elif hasattr(self, 'set_small'):
              self.set_small(obj_.value)
        elif nodeName_ == 'em':
            obj_ = em.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'em', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_em'):
              self.add_em(obj_.value)
            elif hasattr(self, 'set_em'):
              self.set_em(obj_.value)
        elif nodeName_ == 'strong':
            obj_ = strong.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'strong', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_strong'):
              self.add_strong(obj_.value)
            elif hasattr(self, 'set_strong'):
              self.set_strong(obj_.value)
        elif nodeName_ == 'dfn':
            obj_ = dfn.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'dfn', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_dfn'):
              self.add_dfn(obj_.value)
            elif hasattr(self, 'set_dfn'):
              self.set_dfn(obj_.value)
        elif nodeName_ == 'code':
            obj_ = code.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'code', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_code'):
              self.add_code(obj_.value)
            elif hasattr(self, 'set_code'):
              self.set_code(obj_.value)
        elif nodeName_ == 'q':
            obj_ = q.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'q', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_q'):
              self.add_q(obj_.value)
            elif hasattr(self, 'set_q'):
              self.set_q(obj_.value)
        elif nodeName_ == 'samp':
            obj_ = samp.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'samp', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_samp'):
              self.add_samp(obj_.value)
            elif hasattr(self, 'set_samp'):
              self.set_samp(obj_.value)
        elif nodeName_ == 'kbd':
            obj_ = kbd.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'kbd', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_kbd'):
              self.add_kbd(obj_.value)
            elif hasattr(self, 'set_kbd'):
              self.set_kbd(obj_.value)
        elif nodeName_ == 'var':
            obj_ = var.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'var', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_var'):
              self.add_var(obj_.value)
            elif hasattr(self, 'set_var'):
              self.set_var(obj_.value)
        elif nodeName_ == 'cite':
            obj_ = cite.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'cite', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_cite'):
              self.add_cite(obj_.value)
            elif hasattr(self, 'set_cite'):
              self.set_cite(obj_.value)
        elif nodeName_ == 'abbr':
            obj_ = abbr.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'abbr', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_abbr'):
              self.add_abbr(obj_.value)
            elif hasattr(self, 'set_abbr'):
              self.set_abbr(obj_.value)
        elif nodeName_ == 'acronym':
            obj_ = acronym.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'acronym', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_acronym'):
              self.add_acronym(obj_.value)
            elif hasattr(self, 'set_acronym'):
              self.set_acronym(obj_.value)
        elif nodeName_ == 'sub':
            obj_ = sub.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'sub', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_sub'):
              self.add_sub(obj_.value)
            elif hasattr(self, 'set_sub'):
              self.set_sub(obj_.value)
        elif nodeName_ == 'sup':
            obj_ = sup.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'sup', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_sup'):
              self.add_sup(obj_.value)
            elif hasattr(self, 'set_sup'):
              self.set_sup(obj_.value)
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
# end class Inline


class Block(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, p=None, h1=None, h2=None, h3=None, h4=None, h5=None, h6=None, div=None, ul=None, ol=None, dl=None, pre=None, hr=None, blockquote=None, table=None, extensiontype_=None):
        self.original_tagname_ = None
        self.p = p
        self.h1 = h1
        self.h2 = h2
        self.h3 = h3
        self.h4 = h4
        self.h5 = h5
        self.h6 = h6
        self.div = div
        self.ul = ul
        self.ol = ol
        self.dl = dl
        self.pre = pre
        self.hr = hr
        self.blockquote = blockquote
        self.table = table
        self.extensiontype_ = extensiontype_
    def factory(*args_, **kwargs_):
        if Block.subclass:
            return Block.subclass(*args_, **kwargs_)
        else:
            return Block(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_p(self): return self.p
    def set_p(self, p): self.p = p
    def get_h1(self): return self.h1
    def set_h1(self, h1): self.h1 = h1
    def get_h2(self): return self.h2
    def set_h2(self, h2): self.h2 = h2
    def get_h3(self): return self.h3
    def set_h3(self, h3): self.h3 = h3
    def get_h4(self): return self.h4
    def set_h4(self, h4): self.h4 = h4
    def get_h5(self): return self.h5
    def set_h5(self, h5): self.h5 = h5
    def get_h6(self): return self.h6
    def set_h6(self, h6): self.h6 = h6
    def get_div(self): return self.div
    def set_div(self, div): self.div = div
    def get_ul(self): return self.ul
    def set_ul(self, ul): self.ul = ul
    def get_ol(self): return self.ol
    def set_ol(self, ol): self.ol = ol
    def get_dl(self): return self.dl
    def set_dl(self, dl): self.dl = dl
    def get_pre(self): return self.pre
    def set_pre(self, pre): self.pre = pre
    def get_hr(self): return self.hr
    def set_hr(self, hr): self.hr = hr
    def get_blockquote(self): return self.blockquote
    def set_blockquote(self, blockquote): self.blockquote = blockquote
    def get_table(self): return self.table
    def set_table(self, table): self.table = table
    def get_extensiontype_(self): return self.extensiontype_
    def set_extensiontype_(self, extensiontype_): self.extensiontype_ = extensiontype_
    def hasContent_(self):
        if (
            self.p is not None or
            self.h1 is not None or
            self.h2 is not None or
            self.h3 is not None or
            self.h4 is not None or
            self.h5 is not None or
            self.h6 is not None or
            self.div is not None or
            self.ul is not None or
            self.ol is not None or
            self.dl is not None or
            self.pre is not None or
            self.hr is not None or
            self.blockquote is not None or
            self.table is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Block', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Block')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Block', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Block'):
        if self.extensiontype_ is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            outfile.write(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            outfile.write(' xsi:type="%s"' % self.extensiontype_)
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='Block', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.p is not None:
            self.p.export(outfile, level, namespace_, name_='p', pretty_print=pretty_print)
        if self.h1 is not None:
            self.h1.export(outfile, level, namespace_, name_='h1', pretty_print=pretty_print)
        if self.h2 is not None:
            self.h2.export(outfile, level, namespace_, name_='h2', pretty_print=pretty_print)
        if self.h3 is not None:
            self.h3.export(outfile, level, namespace_, name_='h3', pretty_print=pretty_print)
        if self.h4 is not None:
            self.h4.export(outfile, level, namespace_, name_='h4', pretty_print=pretty_print)
        if self.h5 is not None:
            self.h5.export(outfile, level, namespace_, name_='h5', pretty_print=pretty_print)
        if self.h6 is not None:
            self.h6.export(outfile, level, namespace_, name_='h6', pretty_print=pretty_print)
        if self.div is not None:
            self.div.export(outfile, level, namespace_, name_='div', pretty_print=pretty_print)
        if self.ul is not None:
            self.ul.export(outfile, level, namespace_, name_='ul', pretty_print=pretty_print)
        if self.ol is not None:
            self.ol.export(outfile, level, namespace_, name_='ol', pretty_print=pretty_print)
        if self.dl is not None:
            self.dl.export(outfile, level, namespace_, name_='dl', pretty_print=pretty_print)
        if self.pre is not None:
            self.pre.export(outfile, level, namespace_, name_='pre', pretty_print=pretty_print)
        if self.hr is not None:
            self.hr.export(outfile, level, namespace_, name_='hr', pretty_print=pretty_print)
        if self.blockquote is not None:
            self.blockquote.export(outfile, level, namespace_, name_='blockquote', pretty_print=pretty_print)
        if self.table is not None:
            self.table.export(outfile, level, namespace_, name_='table', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Block', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://hl7.org/fhir}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://hl7.org/fhir}' + name_)
        if self.extensiontype_ is not None:
            element.set('{http://www.w3.org/2001/XMLSchema-instance}type', self.extensiontype_)
        if self.p is not None:
            p_ = self.p
            p_.to_etree(element, name_='p', mapping_=mapping_)
        if self.h1 is not None:
            h1_ = self.h1
            h1_.to_etree(element, name_='h1', mapping_=mapping_)
        if self.h2 is not None:
            h2_ = self.h2
            h2_.to_etree(element, name_='h2', mapping_=mapping_)
        if self.h3 is not None:
            h3_ = self.h3
            h3_.to_etree(element, name_='h3', mapping_=mapping_)
        if self.h4 is not None:
            h4_ = self.h4
            h4_.to_etree(element, name_='h4', mapping_=mapping_)
        if self.h5 is not None:
            h5_ = self.h5
            h5_.to_etree(element, name_='h5', mapping_=mapping_)
        if self.h6 is not None:
            h6_ = self.h6
            h6_.to_etree(element, name_='h6', mapping_=mapping_)
        if self.div is not None:
            div_ = self.div
            div_.to_etree(element, name_='div', mapping_=mapping_)
        if self.ul is not None:
            ul_ = self.ul
            ul_.to_etree(element, name_='ul', mapping_=mapping_)
        if self.ol is not None:
            ol_ = self.ol
            ol_.to_etree(element, name_='ol', mapping_=mapping_)
        if self.dl is not None:
            dl_ = self.dl
            dl_.to_etree(element, name_='dl', mapping_=mapping_)
        if self.pre is not None:
            pre_ = self.pre
            pre_.to_etree(element, name_='pre', mapping_=mapping_)
        if self.hr is not None:
            hr_ = self.hr
            hr_.to_etree(element, name_='hr', mapping_=mapping_)
        if self.blockquote is not None:
            blockquote_ = self.blockquote
            blockquote_.to_etree(element, name_='blockquote', mapping_=mapping_)
        if self.table is not None:
            table_ = self.table
            table_.to_etree(element, name_='table', mapping_=mapping_)
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
        value = find_attr_value_('xsi:type', node)
        if value is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            self.extensiontype_ = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'p':
            obj_ = p.factory()
            obj_.build(child_)
            self.p = obj_
            obj_.original_tagname_ = 'p'
        elif nodeName_ == 'h1':
            obj_ = h1.factory()
            obj_.build(child_)
            self.h1 = obj_
            obj_.original_tagname_ = 'h1'
        elif nodeName_ == 'h2':
            obj_ = h2.factory()
            obj_.build(child_)
            self.h2 = obj_
            obj_.original_tagname_ = 'h2'
        elif nodeName_ == 'h3':
            obj_ = h3.factory()
            obj_.build(child_)
            self.h3 = obj_
            obj_.original_tagname_ = 'h3'
        elif nodeName_ == 'h4':
            obj_ = h4.factory()
            obj_.build(child_)
            self.h4 = obj_
            obj_.original_tagname_ = 'h4'
        elif nodeName_ == 'h5':
            obj_ = h5.factory()
            obj_.build(child_)
            self.h5 = obj_
            obj_.original_tagname_ = 'h5'
        elif nodeName_ == 'h6':
            obj_ = h6.factory()
            obj_.build(child_)
            self.h6 = obj_
            obj_.original_tagname_ = 'h6'
        elif nodeName_ == 'div':
            obj_ = div.factory()
            obj_.build(child_)
            self.div = obj_
            obj_.original_tagname_ = 'div'
        elif nodeName_ == 'ul':
            obj_ = ul.factory()
            obj_.build(child_)
            self.ul = obj_
            obj_.original_tagname_ = 'ul'
        elif nodeName_ == 'ol':
            obj_ = ol.factory()
            obj_.build(child_)
            self.ol = obj_
            obj_.original_tagname_ = 'ol'
        elif nodeName_ == 'dl':
            obj_ = dl.factory()
            obj_.build(child_)
            self.dl = obj_
            obj_.original_tagname_ = 'dl'
        elif nodeName_ == 'pre':
            obj_ = pre.factory()
            obj_.build(child_)
            self.pre = obj_
            obj_.original_tagname_ = 'pre'
        elif nodeName_ == 'hr':
            obj_ = hr.factory()
            obj_.build(child_)
            self.hr = obj_
            obj_.original_tagname_ = 'hr'
        elif nodeName_ == 'blockquote':
            obj_ = blockquote.factory()
            obj_.build(child_)
            self.blockquote = obj_
            obj_.original_tagname_ = 'blockquote'
        elif nodeName_ == 'table':
            obj_ = table.factory()
            obj_.build(child_)
            self.table = obj_
            obj_.original_tagname_ = 'table'
# end class Block


class Flow(GeneratedsSuper):
    """ "Flow" mixes block and inline and is used for list items etc. """
    subclass = None
    superclass = None
    def __init__(self, p=None, h1=None, h2=None, h3=None, h4=None, h5=None, h6=None, div=None, ul=None, ol=None, dl=None, pre=None, hr=None, blockquote=None, table=None, a=None, br=None, span=None, bdo=None, map=None, img=None, tt=None, i=None, b=None, big=None, small=None, em=None, strong=None, dfn=None, code=None, q=None, samp=None, kbd=None, var=None, cite=None, abbr=None, acronym=None, sub=None, sup=None, valueOf_=None, mixedclass_=None, content_=None, extensiontype_=None):
        self.original_tagname_ = None
        self.p = p
        self.h1 = h1
        self.h2 = h2
        self.h3 = h3
        self.h4 = h4
        self.h5 = h5
        self.h6 = h6
        self.div = div
        self.ul = ul
        self.ol = ol
        self.dl = dl
        self.pre = pre
        self.hr = hr
        self.blockquote = blockquote
        self.table = table
        self.a = a
        self.br = br
        self.span = span
        self.bdo = bdo
        self.map = map
        self.img = img
        self.tt = tt
        self.i = i
        self.b = b
        self.big = big
        self.small = small
        self.em = em
        self.strong = strong
        self.dfn = dfn
        self.code = code
        self.q = q
        self.samp = samp
        self.kbd = kbd
        self.var = var
        self.cite = cite
        self.abbr = abbr
        self.acronym = acronym
        self.sub = sub
        self.sup = sup
        self.valueOf_ = valueOf_
        self.extensiontype_ = extensiontype_
        if mixedclass_ is None:
            self.mixedclass_ = MixedContainer
        else:
            self.mixedclass_ = mixedclass_
        if content_ is None:
            self.content_ = []
        else:
            self.content_ = content_
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if Flow.subclass:
            return Flow.subclass(*args_, **kwargs_)
        else:
            return Flow(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_p(self): return self.p
    def set_p(self, p): self.p = p
    def get_h1(self): return self.h1
    def set_h1(self, h1): self.h1 = h1
    def get_h2(self): return self.h2
    def set_h2(self, h2): self.h2 = h2
    def get_h3(self): return self.h3
    def set_h3(self, h3): self.h3 = h3
    def get_h4(self): return self.h4
    def set_h4(self, h4): self.h4 = h4
    def get_h5(self): return self.h5
    def set_h5(self, h5): self.h5 = h5
    def get_h6(self): return self.h6
    def set_h6(self, h6): self.h6 = h6
    def get_div(self): return self.div
    def set_div(self, div): self.div = div
    def get_ul(self): return self.ul
    def set_ul(self, ul): self.ul = ul
    def get_ol(self): return self.ol
    def set_ol(self, ol): self.ol = ol
    def get_dl(self): return self.dl
    def set_dl(self, dl): self.dl = dl
    def get_pre(self): return self.pre
    def set_pre(self, pre): self.pre = pre
    def get_hr(self): return self.hr
    def set_hr(self, hr): self.hr = hr
    def get_blockquote(self): return self.blockquote
    def set_blockquote(self, blockquote): self.blockquote = blockquote
    def get_table(self): return self.table
    def set_table(self, table): self.table = table
    def get_a(self): return self.a
    def set_a(self, a): self.a = a
    def get_br(self): return self.br
    def set_br(self, br): self.br = br
    def get_span(self): return self.span
    def set_span(self, span): self.span = span
    def get_bdo(self): return self.bdo
    def set_bdo(self, bdo): self.bdo = bdo
    def get_map(self): return self.map
    def set_map(self, map): self.map = map
    def get_img(self): return self.img
    def set_img(self, img): self.img = img
    def get_tt(self): return self.tt
    def set_tt(self, tt): self.tt = tt
    def get_i(self): return self.i
    def set_i(self, i): self.i = i
    def get_b(self): return self.b
    def set_b(self, b): self.b = b
    def get_big(self): return self.big
    def set_big(self, big): self.big = big
    def get_small(self): return self.small
    def set_small(self, small): self.small = small
    def get_em(self): return self.em
    def set_em(self, em): self.em = em
    def get_strong(self): return self.strong
    def set_strong(self, strong): self.strong = strong
    def get_dfn(self): return self.dfn
    def set_dfn(self, dfn): self.dfn = dfn
    def get_code(self): return self.code
    def set_code(self, code): self.code = code
    def get_q(self): return self.q
    def set_q(self, q): self.q = q
    def get_samp(self): return self.samp
    def set_samp(self, samp): self.samp = samp
    def get_kbd(self): return self.kbd
    def set_kbd(self, kbd): self.kbd = kbd
    def get_var(self): return self.var
    def set_var(self, var): self.var = var
    def get_cite(self): return self.cite
    def set_cite(self, cite): self.cite = cite
    def get_abbr(self): return self.abbr
    def set_abbr(self, abbr): self.abbr = abbr
    def get_acronym(self): return self.acronym
    def set_acronym(self, acronym): self.acronym = acronym
    def get_sub(self): return self.sub
    def set_sub(self, sub): self.sub = sub
    def get_sup(self): return self.sup
    def set_sup(self, sup): self.sup = sup
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def get_extensiontype_(self): return self.extensiontype_
    def set_extensiontype_(self, extensiontype_): self.extensiontype_ = extensiontype_
    def hasContent_(self):
        if (
            self.p is not None or
            self.h1 is not None or
            self.h2 is not None or
            self.h3 is not None or
            self.h4 is not None or
            self.h5 is not None or
            self.h6 is not None or
            self.div is not None or
            self.ul is not None or
            self.ol is not None or
            self.dl is not None or
            self.pre is not None or
            self.hr is not None or
            self.blockquote is not None or
            self.table is not None or
            self.a is not None or
            self.br is not None or
            self.span is not None or
            self.bdo is not None or
            self.map is not None or
            self.img is not None or
            self.tt is not None or
            self.i is not None or
            self.b is not None or
            self.big is not None or
            self.small is not None or
            self.em is not None or
            self.strong is not None or
            self.dfn is not None or
            self.code is not None or
            self.q is not None or
            self.samp is not None or
            self.kbd is not None or
            self.var is not None or
            self.cite is not None or
            self.abbr is not None or
            self.acronym is not None or
            self.sub is not None or
            self.sup is not None or
            self.valueOf_
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Flow', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Flow')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Flow', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Flow'):
        if self.extensiontype_ is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            outfile.write(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            outfile.write(' xsi:type="%s"' % self.extensiontype_)
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='Flow', fromsubclass_=False, pretty_print=True):
        if not fromsubclass_:
            for item_ in self.content_:
                item_.export(outfile, level, item_.name, namespace_, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Flow', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://hl7.org/fhir}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://hl7.org/fhir}' + name_)
        if self.extensiontype_ is not None:
            element.set('{http://www.w3.org/2001/XMLSchema-instance}type', self.extensiontype_)
        for item_ in self.content_:
            item_.to_etree(element)
        if mapping_ is not None:
            mapping_[self] = element
        return element
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        if node.text is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', node.text)
            self.content_.append(obj_)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('xsi:type', node)
        if value is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            self.extensiontype_ = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'p':
            obj_ = p.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'p', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_p'):
              self.add_p(obj_.value)
            elif hasattr(self, 'set_p'):
              self.set_p(obj_.value)
        elif nodeName_ == 'h1':
            obj_ = h1.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'h1', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_h1'):
              self.add_h1(obj_.value)
            elif hasattr(self, 'set_h1'):
              self.set_h1(obj_.value)
        elif nodeName_ == 'h2':
            obj_ = h2.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'h2', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_h2'):
              self.add_h2(obj_.value)
            elif hasattr(self, 'set_h2'):
              self.set_h2(obj_.value)
        elif nodeName_ == 'h3':
            obj_ = h3.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'h3', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_h3'):
              self.add_h3(obj_.value)
            elif hasattr(self, 'set_h3'):
              self.set_h3(obj_.value)
        elif nodeName_ == 'h4':
            obj_ = h4.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'h4', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_h4'):
              self.add_h4(obj_.value)
            elif hasattr(self, 'set_h4'):
              self.set_h4(obj_.value)
        elif nodeName_ == 'h5':
            obj_ = h5.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'h5', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_h5'):
              self.add_h5(obj_.value)
            elif hasattr(self, 'set_h5'):
              self.set_h5(obj_.value)
        elif nodeName_ == 'h6':
            obj_ = h6.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'h6', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_h6'):
              self.add_h6(obj_.value)
            elif hasattr(self, 'set_h6'):
              self.set_h6(obj_.value)
        elif nodeName_ == 'div':
            obj_ = div.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'div', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_div'):
              self.add_div(obj_.value)
            elif hasattr(self, 'set_div'):
              self.set_div(obj_.value)
        elif nodeName_ == 'ul':
            obj_ = ul.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'ul', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_ul'):
              self.add_ul(obj_.value)
            elif hasattr(self, 'set_ul'):
              self.set_ul(obj_.value)
        elif nodeName_ == 'ol':
            obj_ = ol.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'ol', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_ol'):
              self.add_ol(obj_.value)
            elif hasattr(self, 'set_ol'):
              self.set_ol(obj_.value)
        elif nodeName_ == 'dl':
            obj_ = dl.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'dl', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_dl'):
              self.add_dl(obj_.value)
            elif hasattr(self, 'set_dl'):
              self.set_dl(obj_.value)
        elif nodeName_ == 'pre':
            obj_ = pre.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'pre', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_pre'):
              self.add_pre(obj_.value)
            elif hasattr(self, 'set_pre'):
              self.set_pre(obj_.value)
        elif nodeName_ == 'hr':
            obj_ = hr.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'hr', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_hr'):
              self.add_hr(obj_.value)
            elif hasattr(self, 'set_hr'):
              self.set_hr(obj_.value)
        elif nodeName_ == 'blockquote':
            obj_ = blockquote.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'blockquote', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_blockquote'):
              self.add_blockquote(obj_.value)
            elif hasattr(self, 'set_blockquote'):
              self.set_blockquote(obj_.value)
        elif nodeName_ == 'table':
            obj_ = table.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'table', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_table'):
              self.add_table(obj_.value)
            elif hasattr(self, 'set_table'):
              self.set_table(obj_.value)
        elif nodeName_ == 'a':
            obj_ = a.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'a', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_a'):
              self.add_a(obj_.value)
            elif hasattr(self, 'set_a'):
              self.set_a(obj_.value)
        elif nodeName_ == 'br':
            obj_ = br.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'br', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_br'):
              self.add_br(obj_.value)
            elif hasattr(self, 'set_br'):
              self.set_br(obj_.value)
        elif nodeName_ == 'span':
            obj_ = span.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'span', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_span'):
              self.add_span(obj_.value)
            elif hasattr(self, 'set_span'):
              self.set_span(obj_.value)
        elif nodeName_ == 'bdo':
            obj_ = bdo.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'bdo', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_bdo'):
              self.add_bdo(obj_.value)
            elif hasattr(self, 'set_bdo'):
              self.set_bdo(obj_.value)
        elif nodeName_ == 'map':
            obj_ = map.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'map', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_map'):
              self.add_map(obj_.value)
            elif hasattr(self, 'set_map'):
              self.set_map(obj_.value)
        elif nodeName_ == 'img':
            obj_ = img.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'img', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_img'):
              self.add_img(obj_.value)
            elif hasattr(self, 'set_img'):
              self.set_img(obj_.value)
        elif nodeName_ == 'tt':
            obj_ = tt.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'tt', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_tt'):
              self.add_tt(obj_.value)
            elif hasattr(self, 'set_tt'):
              self.set_tt(obj_.value)
        elif nodeName_ == 'i':
            obj_ = i.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'i', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_i'):
              self.add_i(obj_.value)
            elif hasattr(self, 'set_i'):
              self.set_i(obj_.value)
        elif nodeName_ == 'b':
            obj_ = b.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'b', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_b'):
              self.add_b(obj_.value)
            elif hasattr(self, 'set_b'):
              self.set_b(obj_.value)
        elif nodeName_ == 'big':
            obj_ = big.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'big', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_big'):
              self.add_big(obj_.value)
            elif hasattr(self, 'set_big'):
              self.set_big(obj_.value)
        elif nodeName_ == 'small':
            obj_ = small.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'small', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_small'):
              self.add_small(obj_.value)
            elif hasattr(self, 'set_small'):
              self.set_small(obj_.value)
        elif nodeName_ == 'em':
            obj_ = em.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'em', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_em'):
              self.add_em(obj_.value)
            elif hasattr(self, 'set_em'):
              self.set_em(obj_.value)
        elif nodeName_ == 'strong':
            obj_ = strong.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'strong', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_strong'):
              self.add_strong(obj_.value)
            elif hasattr(self, 'set_strong'):
              self.set_strong(obj_.value)
        elif nodeName_ == 'dfn':
            obj_ = dfn.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'dfn', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_dfn'):
              self.add_dfn(obj_.value)
            elif hasattr(self, 'set_dfn'):
              self.set_dfn(obj_.value)
        elif nodeName_ == 'code':
            obj_ = code.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'code', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_code'):
              self.add_code(obj_.value)
            elif hasattr(self, 'set_code'):
              self.set_code(obj_.value)
        elif nodeName_ == 'q':
            obj_ = q.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'q', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_q'):
              self.add_q(obj_.value)
            elif hasattr(self, 'set_q'):
              self.set_q(obj_.value)
        elif nodeName_ == 'samp':
            obj_ = samp.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'samp', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_samp'):
              self.add_samp(obj_.value)
            elif hasattr(self, 'set_samp'):
              self.set_samp(obj_.value)
        elif nodeName_ == 'kbd':
            obj_ = kbd.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'kbd', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_kbd'):
              self.add_kbd(obj_.value)
            elif hasattr(self, 'set_kbd'):
              self.set_kbd(obj_.value)
        elif nodeName_ == 'var':
            obj_ = var.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'var', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_var'):
              self.add_var(obj_.value)
            elif hasattr(self, 'set_var'):
              self.set_var(obj_.value)
        elif nodeName_ == 'cite':
            obj_ = cite.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'cite', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_cite'):
              self.add_cite(obj_.value)
            elif hasattr(self, 'set_cite'):
              self.set_cite(obj_.value)
        elif nodeName_ == 'abbr':
            obj_ = abbr.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'abbr', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_abbr'):
              self.add_abbr(obj_.value)
            elif hasattr(self, 'set_abbr'):
              self.set_abbr(obj_.value)
        elif nodeName_ == 'acronym':
            obj_ = acronym.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'acronym', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_acronym'):
              self.add_acronym(obj_.value)
            elif hasattr(self, 'set_acronym'):
              self.set_acronym(obj_.value)
        elif nodeName_ == 'sub':
            obj_ = sub.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'sub', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_sub'):
              self.add_sub(obj_.value)
            elif hasattr(self, 'set_sub'):
              self.set_sub(obj_.value)
        elif nodeName_ == 'sup':
            obj_ = sup.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'sup', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_sup'):
              self.add_sup(obj_.value)
            elif hasattr(self, 'set_sup'):
              self.set_sup(obj_.value)
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
# end class Flow


class Extension(Element):
    """Optional Extensions Element - found in all resources.If the element
    is present, it must have a value for at least one of the defined
    elements, an @id referenced from the Narrative, or
    extensionsValue of extension - may be a resource or one of a
    constrained set of the data types (see Extensibility in the spec
    for list)."""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, url=None, valueBoolean=None, valueInteger=None, valueDecimal=None, valueBase64Binary=None, valueInstant=None, valueString=None, valueUri=None, valueDate=None, valueDateTime=None, valueCode=None, valueAttachment=None, valueIdentifier=None, valueCodeableConcept=None, valueCoding=None, valueQuantity=None, valueRange=None, valuePeriod=None, valueRatio=None, valueResource=None, valueSampledData=None, valueHumanName=None, valueAddress=None, valueContact=None, valueSchedule=None):
        self.original_tagname_ = None
        super(Extension, self).__init__(id, extension, )
        self.url = _cast(None, url)
        self.valueBoolean = valueBoolean
        self.valueInteger = valueInteger
        self.valueDecimal = valueDecimal
        self.valueBase64Binary = valueBase64Binary
        self.valueInstant = valueInstant
        self.valueString = valueString
        self.valueUri = valueUri
        self.valueDate = valueDate
        self.valueDateTime = valueDateTime
        self.valueCode = valueCode
        self.valueAttachment = valueAttachment
        self.valueIdentifier = valueIdentifier
        self.valueCodeableConcept = valueCodeableConcept
        self.valueCoding = valueCoding
        self.valueQuantity = valueQuantity
        self.valueRange = valueRange
        self.valuePeriod = valuePeriod
        self.valueRatio = valueRatio
        self.valueResource = valueResource
        self.valueSampledData = valueSampledData
        self.valueHumanName = valueHumanName
        self.valueAddress = valueAddress
        self.valueContact = valueContact
        self.valueSchedule = valueSchedule
    def factory(*args_, **kwargs_):
        if Extension.subclass:
            return Extension.subclass(*args_, **kwargs_)
        else:
            return Extension(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_valueBoolean(self): return self.valueBoolean
    def set_valueBoolean(self, valueBoolean): self.valueBoolean = valueBoolean
    def get_valueInteger(self): return self.valueInteger
    def set_valueInteger(self, valueInteger): self.valueInteger = valueInteger
    def get_valueDecimal(self): return self.valueDecimal
    def set_valueDecimal(self, valueDecimal): self.valueDecimal = valueDecimal
    def get_valueBase64Binary(self): return self.valueBase64Binary
    def set_valueBase64Binary(self, valueBase64Binary): self.valueBase64Binary = valueBase64Binary
    def get_valueInstant(self): return self.valueInstant
    def set_valueInstant(self, valueInstant): self.valueInstant = valueInstant
    def get_valueString(self): return self.valueString
    def set_valueString(self, valueString): self.valueString = valueString
    def get_valueUri(self): return self.valueUri
    def set_valueUri(self, valueUri): self.valueUri = valueUri
    def get_valueDate(self): return self.valueDate
    def set_valueDate(self, valueDate): self.valueDate = valueDate
    def get_valueDateTime(self): return self.valueDateTime
    def set_valueDateTime(self, valueDateTime): self.valueDateTime = valueDateTime
    def get_valueCode(self): return self.valueCode
    def set_valueCode(self, valueCode): self.valueCode = valueCode
    def get_valueAttachment(self): return self.valueAttachment
    def set_valueAttachment(self, valueAttachment): self.valueAttachment = valueAttachment
    def get_valueIdentifier(self): return self.valueIdentifier
    def set_valueIdentifier(self, valueIdentifier): self.valueIdentifier = valueIdentifier
    def get_valueCodeableConcept(self): return self.valueCodeableConcept
    def set_valueCodeableConcept(self, valueCodeableConcept): self.valueCodeableConcept = valueCodeableConcept
    def get_valueCoding(self): return self.valueCoding
    def set_valueCoding(self, valueCoding): self.valueCoding = valueCoding
    def get_valueQuantity(self): return self.valueQuantity
    def set_valueQuantity(self, valueQuantity): self.valueQuantity = valueQuantity
    def get_valueRange(self): return self.valueRange
    def set_valueRange(self, valueRange): self.valueRange = valueRange
    def get_valuePeriod(self): return self.valuePeriod
    def set_valuePeriod(self, valuePeriod): self.valuePeriod = valuePeriod
    def get_valueRatio(self): return self.valueRatio
    def set_valueRatio(self, valueRatio): self.valueRatio = valueRatio
    def get_valueResource(self): return self.valueResource
    def set_valueResource(self, valueResource): self.valueResource = valueResource
    def get_valueSampledData(self): return self.valueSampledData
    def set_valueSampledData(self, valueSampledData): self.valueSampledData = valueSampledData
    def get_valueHumanName(self): return self.valueHumanName
    def set_valueHumanName(self, valueHumanName): self.valueHumanName = valueHumanName
    def get_valueAddress(self): return self.valueAddress
    def set_valueAddress(self, valueAddress): self.valueAddress = valueAddress
    def get_valueContact(self): return self.valueContact
    def set_valueContact(self, valueContact): self.valueContact = valueContact
    def get_valueSchedule(self): return self.valueSchedule
    def set_valueSchedule(self, valueSchedule): self.valueSchedule = valueSchedule
    def get_url(self): return self.url
    def set_url(self, url): self.url = url
    def hasContent_(self):
        if (
            self.valueBoolean is not None or
            self.valueInteger is not None or
            self.valueDecimal is not None or
            self.valueBase64Binary is not None or
            self.valueInstant is not None or
            self.valueString is not None or
            self.valueUri is not None or
            self.valueDate is not None or
            self.valueDateTime is not None or
            self.valueCode is not None or
            self.valueAttachment is not None or
            self.valueIdentifier is not None or
            self.valueCodeableConcept is not None or
            self.valueCoding is not None or
            self.valueQuantity is not None or
            self.valueRange is not None or
            self.valuePeriod is not None or
            self.valueRatio is not None or
            self.valueResource is not None or
            self.valueSampledData is not None or
            self.valueHumanName is not None or
            self.valueAddress is not None or
            self.valueContact is not None or
            self.valueSchedule is not None or
            super(Extension, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Extension', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Extension')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Extension', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Extension'):
        super(Extension, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Extension')
        if self.url is not None and 'url' not in already_processed:
            already_processed.add('url')
            outfile.write(' url=%s' % (quote_attrib(self.url), ))
    def exportChildren(self, outfile, level, namespace_='', name_='Extension', fromsubclass_=False, pretty_print=True):
        super(Extension, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.valueBoolean is not None:
            self.valueBoolean.export(outfile, level, namespace_, name_='valueBoolean', pretty_print=pretty_print)
        if self.valueInteger is not None:
            self.valueInteger.export(outfile, level, namespace_, name_='valueInteger', pretty_print=pretty_print)
        if self.valueDecimal is not None:
            self.valueDecimal.export(outfile, level, namespace_, name_='valueDecimal', pretty_print=pretty_print)
        if self.valueBase64Binary is not None:
            self.valueBase64Binary.export(outfile, level, namespace_, name_='valueBase64Binary', pretty_print=pretty_print)
        if self.valueInstant is not None:
            self.valueInstant.export(outfile, level, namespace_, name_='valueInstant', pretty_print=pretty_print)
        if self.valueString is not None:
            self.valueString.export(outfile, level, namespace_, name_='valueString', pretty_print=pretty_print)
        if self.valueUri is not None:
            self.valueUri.export(outfile, level, namespace_, name_='valueUri', pretty_print=pretty_print)
        if self.valueDate is not None:
            self.valueDate.export(outfile, level, namespace_, name_='valueDate', pretty_print=pretty_print)
        if self.valueDateTime is not None:
            self.valueDateTime.export(outfile, level, namespace_, name_='valueDateTime', pretty_print=pretty_print)
        if self.valueCode is not None:
            self.valueCode.export(outfile, level, namespace_, name_='valueCode', pretty_print=pretty_print)
        if self.valueAttachment is not None:
            self.valueAttachment.export(outfile, level, namespace_, name_='valueAttachment', pretty_print=pretty_print)
        if self.valueIdentifier is not None:
            self.valueIdentifier.export(outfile, level, namespace_, name_='valueIdentifier', pretty_print=pretty_print)
        if self.valueCodeableConcept is not None:
            self.valueCodeableConcept.export(outfile, level, namespace_, name_='valueCodeableConcept', pretty_print=pretty_print)
        if self.valueCoding is not None:
            self.valueCoding.export(outfile, level, namespace_, name_='valueCoding', pretty_print=pretty_print)
        if self.valueQuantity is not None:
            self.valueQuantity.export(outfile, level, namespace_, name_='valueQuantity', pretty_print=pretty_print)
        if self.valueRange is not None:
            self.valueRange.export(outfile, level, namespace_, name_='valueRange', pretty_print=pretty_print)
        if self.valuePeriod is not None:
            self.valuePeriod.export(outfile, level, namespace_, name_='valuePeriod', pretty_print=pretty_print)
        if self.valueRatio is not None:
            self.valueRatio.export(outfile, level, namespace_, name_='valueRatio', pretty_print=pretty_print)
        if self.valueResource is not None:
            self.valueResource.export(outfile, level, namespace_, name_='valueResource', pretty_print=pretty_print)
        if self.valueSampledData is not None:
            self.valueSampledData.export(outfile, level, namespace_, name_='valueSampledData', pretty_print=pretty_print)
        if self.valueHumanName is not None:
            self.valueHumanName.export(outfile, level, namespace_, name_='valueHumanName', pretty_print=pretty_print)
        if self.valueAddress is not None:
            self.valueAddress.export(outfile, level, namespace_, name_='valueAddress', pretty_print=pretty_print)
        if self.valueContact is not None:
            self.valueContact.export(outfile, level, namespace_, name_='valueContact', pretty_print=pretty_print)
        if self.valueSchedule is not None:
            self.valueSchedule.export(outfile, level, namespace_, name_='valueSchedule', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Extension', mapping_=None):
        element = super(Extension, self).to_etree(parent_element, name_, mapping_)
        if self.url is not None:
            element.set('url', self.url)
        if self.valueBoolean is not None:
            valueBoolean_ = self.valueBoolean
            valueBoolean_.to_etree(element, name_='valueBoolean', mapping_=mapping_)
        if self.valueInteger is not None:
            valueInteger_ = self.valueInteger
            valueInteger_.to_etree(element, name_='valueInteger', mapping_=mapping_)
        if self.valueDecimal is not None:
            valueDecimal_ = self.valueDecimal
            valueDecimal_.to_etree(element, name_='valueDecimal', mapping_=mapping_)
        if self.valueBase64Binary is not None:
            valueBase64Binary_ = self.valueBase64Binary
            valueBase64Binary_.to_etree(element, name_='valueBase64Binary', mapping_=mapping_)
        if self.valueInstant is not None:
            valueInstant_ = self.valueInstant
            valueInstant_.to_etree(element, name_='valueInstant', mapping_=mapping_)
        if self.valueString is not None:
            valueString_ = self.valueString
            valueString_.to_etree(element, name_='valueString', mapping_=mapping_)
        if self.valueUri is not None:
            valueUri_ = self.valueUri
            valueUri_.to_etree(element, name_='valueUri', mapping_=mapping_)
        if self.valueDate is not None:
            valueDate_ = self.valueDate
            valueDate_.to_etree(element, name_='valueDate', mapping_=mapping_)
        if self.valueDateTime is not None:
            valueDateTime_ = self.valueDateTime
            valueDateTime_.to_etree(element, name_='valueDateTime', mapping_=mapping_)
        if self.valueCode is not None:
            valueCode_ = self.valueCode
            valueCode_.to_etree(element, name_='valueCode', mapping_=mapping_)
        if self.valueAttachment is not None:
            valueAttachment_ = self.valueAttachment
            valueAttachment_.to_etree(element, name_='valueAttachment', mapping_=mapping_)
        if self.valueIdentifier is not None:
            valueIdentifier_ = self.valueIdentifier
            valueIdentifier_.to_etree(element, name_='valueIdentifier', mapping_=mapping_)
        if self.valueCodeableConcept is not None:
            valueCodeableConcept_ = self.valueCodeableConcept
            valueCodeableConcept_.to_etree(element, name_='valueCodeableConcept', mapping_=mapping_)
        if self.valueCoding is not None:
            valueCoding_ = self.valueCoding
            valueCoding_.to_etree(element, name_='valueCoding', mapping_=mapping_)
        if self.valueQuantity is not None:
            valueQuantity_ = self.valueQuantity
            valueQuantity_.to_etree(element, name_='valueQuantity', mapping_=mapping_)
        if self.valueRange is not None:
            valueRange_ = self.valueRange
            valueRange_.to_etree(element, name_='valueRange', mapping_=mapping_)
        if self.valuePeriod is not None:
            valuePeriod_ = self.valuePeriod
            valuePeriod_.to_etree(element, name_='valuePeriod', mapping_=mapping_)
        if self.valueRatio is not None:
            valueRatio_ = self.valueRatio
            valueRatio_.to_etree(element, name_='valueRatio', mapping_=mapping_)
        if self.valueResource is not None:
            valueResource_ = self.valueResource
            valueResource_.to_etree(element, name_='valueResource', mapping_=mapping_)
        if self.valueSampledData is not None:
            valueSampledData_ = self.valueSampledData
            valueSampledData_.to_etree(element, name_='valueSampledData', mapping_=mapping_)
        if self.valueHumanName is not None:
            valueHumanName_ = self.valueHumanName
            valueHumanName_.to_etree(element, name_='valueHumanName', mapping_=mapping_)
        if self.valueAddress is not None:
            valueAddress_ = self.valueAddress
            valueAddress_.to_etree(element, name_='valueAddress', mapping_=mapping_)
        if self.valueContact is not None:
            valueContact_ = self.valueContact
            valueContact_.to_etree(element, name_='valueContact', mapping_=mapping_)
        if self.valueSchedule is not None:
            valueSchedule_ = self.valueSchedule
            valueSchedule_.to_etree(element, name_='valueSchedule', mapping_=mapping_)
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
        value = find_attr_value_('url', node)
        if value is not None and 'url' not in already_processed:
            already_processed.add('url')
            self.url = value
        super(Extension, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'valueBoolean':
            obj_ = boolean.factory()
            obj_.build(child_)
            self.valueBoolean = obj_
            obj_.original_tagname_ = 'valueBoolean'
        elif nodeName_ == 'valueInteger':
            obj_ = integer.factory()
            obj_.build(child_)
            self.valueInteger = obj_
            obj_.original_tagname_ = 'valueInteger'
        elif nodeName_ == 'valueDecimal':
            obj_ = decimal.factory()
            obj_.build(child_)
            self.valueDecimal = obj_
            obj_.original_tagname_ = 'valueDecimal'
        elif nodeName_ == 'valueBase64Binary':
            obj_ = base64Binary.factory()
            obj_.build(child_)
            self.valueBase64Binary = obj_
            obj_.original_tagname_ = 'valueBase64Binary'
        elif nodeName_ == 'valueInstant':
            obj_ = instant.factory()
            obj_.build(child_)
            self.valueInstant = obj_
            obj_.original_tagname_ = 'valueInstant'
        elif nodeName_ == 'valueString':
            obj_ = string.factory()
            obj_.build(child_)
            self.valueString = obj_
            obj_.original_tagname_ = 'valueString'
        elif nodeName_ == 'valueUri':
            obj_ = uri.factory()
            obj_.build(child_)
            self.valueUri = obj_
            obj_.original_tagname_ = 'valueUri'
        elif nodeName_ == 'valueDate':
            obj_ = date.factory()
            obj_.build(child_)
            self.valueDate = obj_
            obj_.original_tagname_ = 'valueDate'
        elif nodeName_ == 'valueDateTime':
            obj_ = dateTime.factory()
            obj_.build(child_)
            self.valueDateTime = obj_
            obj_.original_tagname_ = 'valueDateTime'
        elif nodeName_ == 'valueCode':
            obj_ = code.factory()
            obj_.build(child_)
            self.valueCode = obj_
            obj_.original_tagname_ = 'valueCode'
        elif nodeName_ == 'valueAttachment':
            obj_ = Attachment.factory()
            obj_.build(child_)
            self.valueAttachment = obj_
            obj_.original_tagname_ = 'valueAttachment'
        elif nodeName_ == 'valueIdentifier':
            obj_ = Identifier.factory()
            obj_.build(child_)
            self.valueIdentifier = obj_
            obj_.original_tagname_ = 'valueIdentifier'
        elif nodeName_ == 'valueCodeableConcept':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.valueCodeableConcept = obj_
            obj_.original_tagname_ = 'valueCodeableConcept'
        elif nodeName_ == 'valueCoding':
            obj_ = Coding.factory()
            obj_.build(child_)
            self.valueCoding = obj_
            obj_.original_tagname_ = 'valueCoding'
        elif nodeName_ == 'valueQuantity':
            obj_ = Quantity.factory()
            obj_.build(child_)
            self.valueQuantity = obj_
            obj_.original_tagname_ = 'valueQuantity'
        elif nodeName_ == 'valueRange':
            obj_ = Range.factory()
            obj_.build(child_)
            self.valueRange = obj_
            obj_.original_tagname_ = 'valueRange'
        elif nodeName_ == 'valuePeriod':
            obj_ = Period.factory()
            obj_.build(child_)
            self.valuePeriod = obj_
            obj_.original_tagname_ = 'valuePeriod'
        elif nodeName_ == 'valueRatio':
            obj_ = Ratio.factory()
            obj_.build(child_)
            self.valueRatio = obj_
            obj_.original_tagname_ = 'valueRatio'
        elif nodeName_ == 'valueResource':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.valueResource = obj_
            obj_.original_tagname_ = 'valueResource'
        elif nodeName_ == 'valueSampledData':
            obj_ = SampledData.factory()
            obj_.build(child_)
            self.valueSampledData = obj_
            obj_.original_tagname_ = 'valueSampledData'
        elif nodeName_ == 'valueHumanName':
            obj_ = HumanName.factory()
            obj_.build(child_)
            self.valueHumanName = obj_
            obj_.original_tagname_ = 'valueHumanName'
        elif nodeName_ == 'valueAddress':
            obj_ = Address.factory()
            obj_.build(child_)
            self.valueAddress = obj_
            obj_.original_tagname_ = 'valueAddress'
        elif nodeName_ == 'valueContact':
            obj_ = Contact.factory()
            obj_.build(child_)
            self.valueContact = obj_
            obj_.original_tagname_ = 'valueContact'
        elif nodeName_ == 'valueSchedule':
            obj_ = Schedule.factory()
            obj_.build(child_)
            self.valueSchedule = obj_
            obj_.original_tagname_ = 'valueSchedule'
        super(Extension, self).buildChildren(child_, node, nodeName_, True)
# end class Extension


class ResourceReference(Element):
    """A reference from one resource to another.If the element is present,
    it must have a value for at least one of the defined elements,
    an @id referenced from the Narrative, or extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, reference=None, display=None):
        self.original_tagname_ = None
        super(ResourceReference, self).__init__(id, extension, )
        self.reference = reference
        self.display = display
    def factory(*args_, **kwargs_):
        if ResourceReference.subclass:
            return ResourceReference.subclass(*args_, **kwargs_)
        else:
            return ResourceReference(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_reference(self): return self.reference
    def set_reference(self, reference): self.reference = reference
    def get_display(self): return self.display
    def set_display(self, display): self.display = display
    def hasContent_(self):
        if (
            self.reference is not None or
            self.display is not None or
            super(ResourceReference, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='ResourceReference', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ResourceReference')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='ResourceReference', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='ResourceReference'):
        super(ResourceReference, self).exportAttributes(outfile, level, already_processed, namespace_, name_='ResourceReference')
    def exportChildren(self, outfile, level, namespace_='', name_='ResourceReference', fromsubclass_=False, pretty_print=True):
        super(ResourceReference, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.reference is not None:
            self.reference.export(outfile, level, namespace_, name_='reference', pretty_print=pretty_print)
        if self.display is not None:
            self.display.export(outfile, level, namespace_, name_='display', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='ResourceReference', mapping_=None):
        element = super(ResourceReference, self).to_etree(parent_element, name_, mapping_)
        if self.reference is not None:
            reference_ = self.reference
            reference_.to_etree(element, name_='reference', mapping_=mapping_)
        if self.display is not None:
            display_ = self.display
            display_.to_etree(element, name_='display', mapping_=mapping_)
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
        super(ResourceReference, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'reference':
            obj_ = string.factory()
            obj_.build(child_)
            self.reference = obj_
            obj_.original_tagname_ = 'reference'
        elif nodeName_ == 'display':
            obj_ = string.factory()
            obj_.build(child_)
            self.display = obj_
            obj_.original_tagname_ = 'display'
        super(ResourceReference, self).buildChildren(child_, node, nodeName_, True)
# end class ResourceReference


#Down here to avoid circular import problems (hopefully)
from .data_types import *
from .adverse_reaction import *
from .alert import *
from .binary import *
from .care_plan import *
from .composition import *
from .concept_map import *
from .condition import *
from .conformance import *
from .device import *
from .device_observation_report import *
from .diagnostic_order import *
from .diagnostic_report import *
from .document_manifest import *
from .document_reference import *
from .encounter import *
from .family_history import *
from .group import *
from .html import *
from .imaging_study import *
from .immunization import *
from .immunization_recommendation import *
from .list_ import *
from .location import *
from .media import *
from .medication import *
from .medication_administration import *
from .medication_dispense import *
from .medication_prescription import *
from .medication_statement import *
from .message_header import *
from .misc import *
from .narrative import *
from .observation import *
from .operation_outcome import *
from .order import *
from .order_response import *
from .organization import *
from .other import *
from .patient import *
from .practitioner import *
from .procedure import *
from .profile import *
from .provenance import *
from .query import *
from .questionnaire import *
from .related_person import *
from .security_event import *
from .specimen import *
from .substance import *
from .supply import *
from .value_set import *
from .atom import *
from .xmldsig import *
