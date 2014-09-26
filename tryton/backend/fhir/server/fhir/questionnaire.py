from .base_classes import *
from .support_functions import *


class Questionnaire(Resource):
    """A structured set of questions and their answers. The Questionnaire
    may contain questions, answers or both. The questions are
    ordered and grouped into coherent subsets, corresponding to the
    structure of the grouping of the underlying questions.If the
    element is present, it must have either a @value, an @id, or
    extensions"""
    subclass = None
    superclass = Resource
    def __init__(self, id=None, extension=None, modifierExtension=None, language=None, text=None, contained=None, status=None, authored=None, subject=None, author=None, source=None, name=None, identifier=None, encounter=None, group=None):
        self.original_tagname_ = None
        super(Questionnaire, self).__init__(id, extension, modifierExtension, language, text, contained, )
        self.status = status
        self.authored = authored
        self.subject = subject
        self.author = author
        self.source = source
        self.name = name
        if identifier is None:
            self.identifier = []
        else:
            self.identifier = identifier
        self.encounter = encounter
        self.group = group
    def factory(*args_, **kwargs_):
        if Questionnaire.subclass:
            return Questionnaire.subclass(*args_, **kwargs_)
        else:
            return Questionnaire(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_status(self): return self.status
    def set_status(self, status): self.status = status
    def get_authored(self): return self.authored
    def set_authored(self, authored): self.authored = authored
    def get_subject(self): return self.subject
    def set_subject(self, subject): self.subject = subject
    def get_author(self): return self.author
    def set_author(self, author): self.author = author
    def get_source(self): return self.source
    def set_source(self, source): self.source = source
    def get_name(self): return self.name
    def set_name(self, name): self.name = name
    def get_identifier(self): return self.identifier
    def set_identifier(self, identifier): self.identifier = identifier
    def add_identifier(self, value): self.identifier.append(value)
    def insert_identifier(self, index, value): self.identifier[index] = value
    def get_encounter(self): return self.encounter
    def set_encounter(self, encounter): self.encounter = encounter
    def get_group(self): return self.group
    def set_group(self, group): self.group = group
    def hasContent_(self):
        if (
            self.status is not None or
            self.authored is not None or
            self.subject is not None or
            self.author is not None or
            self.source is not None or
            self.name is not None or
            self.identifier or
            self.encounter is not None or
            self.group is not None or
            super(Questionnaire, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Questionnaire', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Questionnaire')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Questionnaire', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Questionnaire'):
        super(Questionnaire, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Questionnaire')
    def exportChildren(self, outfile, level, namespace_='', name_='Questionnaire', fromsubclass_=False, pretty_print=True):
        super(Questionnaire, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.status is not None:
            self.status.export(outfile, level, namespace_, name_='status', pretty_print=pretty_print)
        if self.authored is not None:
            self.authored.export(outfile, level, namespace_, name_='authored', pretty_print=pretty_print)
        if self.subject is not None:
            self.subject.export(outfile, level, namespace_, name_='subject', pretty_print=pretty_print)
        if self.author is not None:
            self.author.export(outfile, level, namespace_, name_='author', pretty_print=pretty_print)
        if self.source is not None:
            self.source.export(outfile, level, namespace_, name_='source', pretty_print=pretty_print)
        if self.name is not None:
            self.name.export(outfile, level, namespace_, name_='name', pretty_print=pretty_print)
        for identifier_ in self.identifier:
            identifier_.export(outfile, level, namespace_, name_='identifier', pretty_print=pretty_print)
        if self.encounter is not None:
            self.encounter.export(outfile, level, namespace_, name_='encounter', pretty_print=pretty_print)
        if self.group is not None:
            self.group.export(outfile, level, namespace_, name_='group', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Questionnaire', mapping_=None):
        element = super(Questionnaire, self).to_etree(parent_element, name_, mapping_)
        if self.status is not None:
            status_ = self.status
            status_.to_etree(element, name_='status', mapping_=mapping_)
        if self.authored is not None:
            authored_ = self.authored
            authored_.to_etree(element, name_='authored', mapping_=mapping_)
        if self.subject is not None:
            subject_ = self.subject
            subject_.to_etree(element, name_='subject', mapping_=mapping_)
        if self.author is not None:
            author_ = self.author
            author_.to_etree(element, name_='author', mapping_=mapping_)
        if self.source is not None:
            source_ = self.source
            source_.to_etree(element, name_='source', mapping_=mapping_)
        if self.name is not None:
            name_ = self.name
            name_.to_etree(element, name_='name', mapping_=mapping_)
        for identifier_ in self.identifier:
            identifier_.to_etree(element, name_='identifier', mapping_=mapping_)
        if self.encounter is not None:
            encounter_ = self.encounter
            encounter_.to_etree(element, name_='encounter', mapping_=mapping_)
        if self.group is not None:
            group_ = self.group
            group_.to_etree(element, name_='group', mapping_=mapping_)
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
        super(Questionnaire, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'status':
            obj_ = QuestionnaireStatus.factory()
            obj_.build(child_)
            self.status = obj_
            obj_.original_tagname_ = 'status'
        elif nodeName_ == 'authored':
            obj_ = dateTime.factory()
            obj_.build(child_)
            self.authored = obj_
            obj_.original_tagname_ = 'authored'
        elif nodeName_ == 'subject':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.subject = obj_
            obj_.original_tagname_ = 'subject'
        elif nodeName_ == 'author':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.author = obj_
            obj_.original_tagname_ = 'author'
        elif nodeName_ == 'source':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.source = obj_
            obj_.original_tagname_ = 'source'
        elif nodeName_ == 'name':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.name = obj_
            obj_.original_tagname_ = 'name'
        elif nodeName_ == 'identifier':
            obj_ = Identifier.factory()
            obj_.build(child_)
            self.identifier.append(obj_)
            obj_.original_tagname_ = 'identifier'
        elif nodeName_ == 'encounter':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.encounter = obj_
            obj_.original_tagname_ = 'encounter'
        elif nodeName_ == 'group':
            obj_ = Questionnaire_Group.factory()
            obj_.build(child_)
            self.group = obj_
            obj_.original_tagname_ = 'group'
        super(Questionnaire, self).buildChildren(child_, node, nodeName_, True)
# end class Questionnaire


class Questionnaire_Group(BackboneElement):
    """A structured set of questions and their answers. The Questionnaire
    may contain questions, answers or both. The questions are
    ordered and grouped into coherent subsets, corresponding to the
    structure of the grouping of the underlying questions."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, name=None, header=None, text=None, subject=None, group=None, question=None):
        self.original_tagname_ = None
        super(Questionnaire_Group, self).__init__(id, extension, modifierExtension, )
        self.name = name
        self.header = header
        self.text = text
        self.subject = subject
        if group is None:
            self.group = []
        else:
            self.group = group
        if question is None:
            self.question = []
        else:
            self.question = question
    def factory(*args_, **kwargs_):
        if Questionnaire_Group.subclass:
            return Questionnaire_Group.subclass(*args_, **kwargs_)
        else:
            return Questionnaire_Group(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_name(self): return self.name
    def set_name(self, name): self.name = name
    def get_header(self): return self.header
    def set_header(self, header): self.header = header
    def get_text(self): return self.text
    def set_text(self, text): self.text = text
    def get_subject(self): return self.subject
    def set_subject(self, subject): self.subject = subject
    def get_group(self): return self.group
    def set_group(self, group): self.group = group
    def add_group(self, value): self.group.append(value)
    def insert_group(self, index, value): self.group[index] = value
    def get_question(self): return self.question
    def set_question(self, question): self.question = question
    def add_question(self, value): self.question.append(value)
    def insert_question(self, index, value): self.question[index] = value
    def hasContent_(self):
        if (
            self.name is not None or
            self.header is not None or
            self.text is not None or
            self.subject is not None or
            self.group or
            self.question or
            super(Questionnaire_Group, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Questionnaire.Group', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Questionnaire.Group')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Questionnaire.Group', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Questionnaire.Group'):
        super(Questionnaire_Group, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Questionnaire.Group')
    def exportChildren(self, outfile, level, namespace_='', name_='Questionnaire.Group', fromsubclass_=False, pretty_print=True):
        super(Questionnaire_Group, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.name is not None:
            self.name.export(outfile, level, namespace_, name_='name', pretty_print=pretty_print)
        if self.header is not None:
            self.header.export(outfile, level, namespace_, name_='header', pretty_print=pretty_print)
        if self.text is not None:
            self.text.export(outfile, level, namespace_, name_='text', pretty_print=pretty_print)
        if self.subject is not None:
            self.subject.export(outfile, level, namespace_, name_='subject', pretty_print=pretty_print)
        for group_ in self.group:
            group_.export(outfile, level, namespace_, name_='group', pretty_print=pretty_print)
        for question_ in self.question:
            question_.export(outfile, level, namespace_, name_='question', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Questionnaire.Group', mapping_=None):
        element = super(Questionnaire_Group, self).to_etree(parent_element, name_, mapping_)
        if self.name is not None:
            name_ = self.name
            name_.to_etree(element, name_='name', mapping_=mapping_)
        if self.header is not None:
            header_ = self.header
            header_.to_etree(element, name_='header', mapping_=mapping_)
        if self.text is not None:
            text_ = self.text
            text_.to_etree(element, name_='text', mapping_=mapping_)
        if self.subject is not None:
            subject_ = self.subject
            subject_.to_etree(element, name_='subject', mapping_=mapping_)
        for group_ in self.group:
            group_.to_etree(element, name_='group', mapping_=mapping_)
        for question_ in self.question:
            question_.to_etree(element, name_='question', mapping_=mapping_)
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
        super(Questionnaire_Group, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'name':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.name = obj_
            obj_.original_tagname_ = 'name'
        elif nodeName_ == 'header':
            obj_ = string.factory()
            obj_.build(child_)
            self.header = obj_
            obj_.original_tagname_ = 'header'
        elif nodeName_ == 'text':
            obj_ = string.factory()
            obj_.build(child_)
            self.text = obj_
            obj_.original_tagname_ = 'text'
        elif nodeName_ == 'subject':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.subject = obj_
            obj_.original_tagname_ = 'subject'
        elif nodeName_ == 'group':
            obj_ = Questionnaire_Group.factory()
            obj_.build(child_)
            self.group.append(obj_)
            obj_.original_tagname_ = 'group'
        elif nodeName_ == 'question':
            obj_ = Questionnaire_Question.factory()
            obj_.build(child_)
            self.question.append(obj_)
            obj_.original_tagname_ = 'question'
        super(Questionnaire_Group, self).buildChildren(child_, node, nodeName_, True)
# end class Questionnaire_Group


class Questionnaire_Question(BackboneElement):
    """A structured set of questions and their answers. The Questionnaire
    may contain questions, answers or both. The questions are
    ordered and grouped into coherent subsets, corresponding to the
    structure of the grouping of the underlying questions.Single-
    valued answer to the question.Structured answer in the form of a
    FHIR Resource or datatype."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, name=None, text=None, answerDecimal=None, answerInteger=None, answerBoolean=None, answerDate=None, answerString=None, answerDateTime=None, answerInstant=None, choice=None, options=None, dataBoolean=None, dataInteger=None, dataDecimal=None, dataBase64Binary=None, dataInstant=None, dataString=None, dataUri=None, dataDate=None, dataDateTime=None, dataCode=None, dataOid=None, dataUuid=None, dataId=None, dataAttachment=None, dataIdentifier=None, dataCodeableConcept=None, dataCoding=None, dataQuantity=None, dataRange=None, dataPeriod=None, dataRatio=None, dataResource=None, dataSampledData=None, dataHumanName=None, dataAddress=None, dataContact=None, dataSchedule=None, remarks=None, group=None):
        self.original_tagname_ = None
        super(Questionnaire_Question, self).__init__(id, extension, modifierExtension, )
        self.name = name
        self.text = text
        self.answerDecimal = answerDecimal
        self.answerInteger = answerInteger
        self.answerBoolean = answerBoolean
        self.answerDate = answerDate
        self.answerString = answerString
        self.answerDateTime = answerDateTime
        self.answerInstant = answerInstant
        if choice is None:
            self.choice = []
        else:
            self.choice = choice
        self.options = options
        self.dataBoolean = dataBoolean
        self.dataInteger = dataInteger
        self.dataDecimal = dataDecimal
        self.dataBase64Binary = dataBase64Binary
        self.dataInstant = dataInstant
        self.dataString = dataString
        self.dataUri = dataUri
        self.dataDate = dataDate
        self.dataDateTime = dataDateTime
        self.dataCode = dataCode
        self.dataOid = dataOid
        self.dataUuid = dataUuid
        self.dataId = dataId
        self.dataAttachment = dataAttachment
        self.dataIdentifier = dataIdentifier
        self.dataCodeableConcept = dataCodeableConcept
        self.dataCoding = dataCoding
        self.dataQuantity = dataQuantity
        self.dataRange = dataRange
        self.dataPeriod = dataPeriod
        self.dataRatio = dataRatio
        self.dataResource = dataResource
        self.dataSampledData = dataSampledData
        self.dataHumanName = dataHumanName
        self.dataAddress = dataAddress
        self.dataContact = dataContact
        self.dataSchedule = dataSchedule
        self.remarks = remarks
        if group is None:
            self.group = []
        else:
            self.group = group
    def factory(*args_, **kwargs_):
        if Questionnaire_Question.subclass:
            return Questionnaire_Question.subclass(*args_, **kwargs_)
        else:
            return Questionnaire_Question(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_name(self): return self.name
    def set_name(self, name): self.name = name
    def get_text(self): return self.text
    def set_text(self, text): self.text = text
    def get_answerDecimal(self): return self.answerDecimal
    def set_answerDecimal(self, answerDecimal): self.answerDecimal = answerDecimal
    def get_answerInteger(self): return self.answerInteger
    def set_answerInteger(self, answerInteger): self.answerInteger = answerInteger
    def get_answerBoolean(self): return self.answerBoolean
    def set_answerBoolean(self, answerBoolean): self.answerBoolean = answerBoolean
    def get_answerDate(self): return self.answerDate
    def set_answerDate(self, answerDate): self.answerDate = answerDate
    def get_answerString(self): return self.answerString
    def set_answerString(self, answerString): self.answerString = answerString
    def get_answerDateTime(self): return self.answerDateTime
    def set_answerDateTime(self, answerDateTime): self.answerDateTime = answerDateTime
    def get_answerInstant(self): return self.answerInstant
    def set_answerInstant(self, answerInstant): self.answerInstant = answerInstant
    def get_choice(self): return self.choice
    def set_choice(self, choice): self.choice = choice
    def add_choice(self, value): self.choice.append(value)
    def insert_choice(self, index, value): self.choice[index] = value
    def get_options(self): return self.options
    def set_options(self, options): self.options = options
    def get_dataBoolean(self): return self.dataBoolean
    def set_dataBoolean(self, dataBoolean): self.dataBoolean = dataBoolean
    def get_dataInteger(self): return self.dataInteger
    def set_dataInteger(self, dataInteger): self.dataInteger = dataInteger
    def get_dataDecimal(self): return self.dataDecimal
    def set_dataDecimal(self, dataDecimal): self.dataDecimal = dataDecimal
    def get_dataBase64Binary(self): return self.dataBase64Binary
    def set_dataBase64Binary(self, dataBase64Binary): self.dataBase64Binary = dataBase64Binary
    def get_dataInstant(self): return self.dataInstant
    def set_dataInstant(self, dataInstant): self.dataInstant = dataInstant
    def get_dataString(self): return self.dataString
    def set_dataString(self, dataString): self.dataString = dataString
    def get_dataUri(self): return self.dataUri
    def set_dataUri(self, dataUri): self.dataUri = dataUri
    def get_dataDate(self): return self.dataDate
    def set_dataDate(self, dataDate): self.dataDate = dataDate
    def get_dataDateTime(self): return self.dataDateTime
    def set_dataDateTime(self, dataDateTime): self.dataDateTime = dataDateTime
    def get_dataCode(self): return self.dataCode
    def set_dataCode(self, dataCode): self.dataCode = dataCode
    def get_dataOid(self): return self.dataOid
    def set_dataOid(self, dataOid): self.dataOid = dataOid
    def get_dataUuid(self): return self.dataUuid
    def set_dataUuid(self, dataUuid): self.dataUuid = dataUuid
    def get_dataId(self): return self.dataId
    def set_dataId(self, dataId): self.dataId = dataId
    def get_dataAttachment(self): return self.dataAttachment
    def set_dataAttachment(self, dataAttachment): self.dataAttachment = dataAttachment
    def get_dataIdentifier(self): return self.dataIdentifier
    def set_dataIdentifier(self, dataIdentifier): self.dataIdentifier = dataIdentifier
    def get_dataCodeableConcept(self): return self.dataCodeableConcept
    def set_dataCodeableConcept(self, dataCodeableConcept): self.dataCodeableConcept = dataCodeableConcept
    def get_dataCoding(self): return self.dataCoding
    def set_dataCoding(self, dataCoding): self.dataCoding = dataCoding
    def get_dataQuantity(self): return self.dataQuantity
    def set_dataQuantity(self, dataQuantity): self.dataQuantity = dataQuantity
    def get_dataRange(self): return self.dataRange
    def set_dataRange(self, dataRange): self.dataRange = dataRange
    def get_dataPeriod(self): return self.dataPeriod
    def set_dataPeriod(self, dataPeriod): self.dataPeriod = dataPeriod
    def get_dataRatio(self): return self.dataRatio
    def set_dataRatio(self, dataRatio): self.dataRatio = dataRatio
    def get_dataResource(self): return self.dataResource
    def set_dataResource(self, dataResource): self.dataResource = dataResource
    def get_dataSampledData(self): return self.dataSampledData
    def set_dataSampledData(self, dataSampledData): self.dataSampledData = dataSampledData
    def get_dataHumanName(self): return self.dataHumanName
    def set_dataHumanName(self, dataHumanName): self.dataHumanName = dataHumanName
    def get_dataAddress(self): return self.dataAddress
    def set_dataAddress(self, dataAddress): self.dataAddress = dataAddress
    def get_dataContact(self): return self.dataContact
    def set_dataContact(self, dataContact): self.dataContact = dataContact
    def get_dataSchedule(self): return self.dataSchedule
    def set_dataSchedule(self, dataSchedule): self.dataSchedule = dataSchedule
    def get_remarks(self): return self.remarks
    def set_remarks(self, remarks): self.remarks = remarks
    def get_group(self): return self.group
    def set_group(self, group): self.group = group
    def add_group(self, value): self.group.append(value)
    def insert_group(self, index, value): self.group[index] = value
    def hasContent_(self):
        if (
            self.name is not None or
            self.text is not None or
            self.answerDecimal is not None or
            self.answerInteger is not None or
            self.answerBoolean is not None or
            self.answerDate is not None or
            self.answerString is not None or
            self.answerDateTime is not None or
            self.answerInstant is not None or
            self.choice or
            self.options is not None or
            self.dataBoolean is not None or
            self.dataInteger is not None or
            self.dataDecimal is not None or
            self.dataBase64Binary is not None or
            self.dataInstant is not None or
            self.dataString is not None or
            self.dataUri is not None or
            self.dataDate is not None or
            self.dataDateTime is not None or
            self.dataCode is not None or
            self.dataOid is not None or
            self.dataUuid is not None or
            self.dataId is not None or
            self.dataAttachment is not None or
            self.dataIdentifier is not None or
            self.dataCodeableConcept is not None or
            self.dataCoding is not None or
            self.dataQuantity is not None or
            self.dataRange is not None or
            self.dataPeriod is not None or
            self.dataRatio is not None or
            self.dataResource is not None or
            self.dataSampledData is not None or
            self.dataHumanName is not None or
            self.dataAddress is not None or
            self.dataContact is not None or
            self.dataSchedule is not None or
            self.remarks is not None or
            self.group or
            super(Questionnaire_Question, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Questionnaire.Question', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Questionnaire.Question')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Questionnaire.Question', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Questionnaire.Question'):
        super(Questionnaire_Question, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Questionnaire.Question')
    def exportChildren(self, outfile, level, namespace_='', name_='Questionnaire.Question', fromsubclass_=False, pretty_print=True):
        super(Questionnaire_Question, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.name is not None:
            self.name.export(outfile, level, namespace_, name_='name', pretty_print=pretty_print)
        if self.text is not None:
            self.text.export(outfile, level, namespace_, name_='text', pretty_print=pretty_print)
        if self.answerDecimal is not None:
            self.answerDecimal.export(outfile, level, namespace_, name_='answerDecimal', pretty_print=pretty_print)
        if self.answerInteger is not None:
            self.answerInteger.export(outfile, level, namespace_, name_='answerInteger', pretty_print=pretty_print)
        if self.answerBoolean is not None:
            self.answerBoolean.export(outfile, level, namespace_, name_='answerBoolean', pretty_print=pretty_print)
        if self.answerDate is not None:
            self.answerDate.export(outfile, level, namespace_, name_='answerDate', pretty_print=pretty_print)
        if self.answerString is not None:
            self.answerString.export(outfile, level, namespace_, name_='answerString', pretty_print=pretty_print)
        if self.answerDateTime is not None:
            self.answerDateTime.export(outfile, level, namespace_, name_='answerDateTime', pretty_print=pretty_print)
        if self.answerInstant is not None:
            self.answerInstant.export(outfile, level, namespace_, name_='answerInstant', pretty_print=pretty_print)
        for choice_ in self.choice:
            choice_.export(outfile, level, namespace_, name_='choice', pretty_print=pretty_print)
        if self.options is not None:
            self.options.export(outfile, level, namespace_, name_='options', pretty_print=pretty_print)
        if self.dataBoolean is not None:
            self.dataBoolean.export(outfile, level, namespace_, name_='dataBoolean', pretty_print=pretty_print)
        if self.dataInteger is not None:
            self.dataInteger.export(outfile, level, namespace_, name_='dataInteger', pretty_print=pretty_print)
        if self.dataDecimal is not None:
            self.dataDecimal.export(outfile, level, namespace_, name_='dataDecimal', pretty_print=pretty_print)
        if self.dataBase64Binary is not None:
            self.dataBase64Binary.export(outfile, level, namespace_, name_='dataBase64Binary', pretty_print=pretty_print)
        if self.dataInstant is not None:
            self.dataInstant.export(outfile, level, namespace_, name_='dataInstant', pretty_print=pretty_print)
        if self.dataString is not None:
            self.dataString.export(outfile, level, namespace_, name_='dataString', pretty_print=pretty_print)
        if self.dataUri is not None:
            self.dataUri.export(outfile, level, namespace_, name_='dataUri', pretty_print=pretty_print)
        if self.dataDate is not None:
            self.dataDate.export(outfile, level, namespace_, name_='dataDate', pretty_print=pretty_print)
        if self.dataDateTime is not None:
            self.dataDateTime.export(outfile, level, namespace_, name_='dataDateTime', pretty_print=pretty_print)
        if self.dataCode is not None:
            self.dataCode.export(outfile, level, namespace_, name_='dataCode', pretty_print=pretty_print)
        if self.dataOid is not None:
            self.dataOid.export(outfile, level, namespace_, name_='dataOid', pretty_print=pretty_print)
        if self.dataUuid is not None:
            self.dataUuid.export(outfile, level, namespace_, name_='dataUuid', pretty_print=pretty_print)
        if self.dataId is not None:
            self.dataId.export(outfile, level, namespace_, name_='dataId', pretty_print=pretty_print)
        if self.dataAttachment is not None:
            self.dataAttachment.export(outfile, level, namespace_, name_='dataAttachment', pretty_print=pretty_print)
        if self.dataIdentifier is not None:
            self.dataIdentifier.export(outfile, level, namespace_, name_='dataIdentifier', pretty_print=pretty_print)
        if self.dataCodeableConcept is not None:
            self.dataCodeableConcept.export(outfile, level, namespace_, name_='dataCodeableConcept', pretty_print=pretty_print)
        if self.dataCoding is not None:
            self.dataCoding.export(outfile, level, namespace_, name_='dataCoding', pretty_print=pretty_print)
        if self.dataQuantity is not None:
            self.dataQuantity.export(outfile, level, namespace_, name_='dataQuantity', pretty_print=pretty_print)
        if self.dataRange is not None:
            self.dataRange.export(outfile, level, namespace_, name_='dataRange', pretty_print=pretty_print)
        if self.dataPeriod is not None:
            self.dataPeriod.export(outfile, level, namespace_, name_='dataPeriod', pretty_print=pretty_print)
        if self.dataRatio is not None:
            self.dataRatio.export(outfile, level, namespace_, name_='dataRatio', pretty_print=pretty_print)
        if self.dataResource is not None:
            self.dataResource.export(outfile, level, namespace_, name_='dataResource', pretty_print=pretty_print)
        if self.dataSampledData is not None:
            self.dataSampledData.export(outfile, level, namespace_, name_='dataSampledData', pretty_print=pretty_print)
        if self.dataHumanName is not None:
            self.dataHumanName.export(outfile, level, namespace_, name_='dataHumanName', pretty_print=pretty_print)
        if self.dataAddress is not None:
            self.dataAddress.export(outfile, level, namespace_, name_='dataAddress', pretty_print=pretty_print)
        if self.dataContact is not None:
            self.dataContact.export(outfile, level, namespace_, name_='dataContact', pretty_print=pretty_print)
        if self.dataSchedule is not None:
            self.dataSchedule.export(outfile, level, namespace_, name_='dataSchedule', pretty_print=pretty_print)
        if self.remarks is not None:
            self.remarks.export(outfile, level, namespace_, name_='remarks', pretty_print=pretty_print)
        for group_ in self.group:
            group_.export(outfile, level, namespace_, name_='group', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Questionnaire.Question', mapping_=None):
        element = super(Questionnaire_Question, self).to_etree(parent_element, name_, mapping_)
        if self.name is not None:
            name_ = self.name
            name_.to_etree(element, name_='name', mapping_=mapping_)
        if self.text is not None:
            text_ = self.text
            text_.to_etree(element, name_='text', mapping_=mapping_)
        if self.answerDecimal is not None:
            answerDecimal_ = self.answerDecimal
            answerDecimal_.to_etree(element, name_='answerDecimal', mapping_=mapping_)
        if self.answerInteger is not None:
            answerInteger_ = self.answerInteger
            answerInteger_.to_etree(element, name_='answerInteger', mapping_=mapping_)
        if self.answerBoolean is not None:
            answerBoolean_ = self.answerBoolean
            answerBoolean_.to_etree(element, name_='answerBoolean', mapping_=mapping_)
        if self.answerDate is not None:
            answerDate_ = self.answerDate
            answerDate_.to_etree(element, name_='answerDate', mapping_=mapping_)
        if self.answerString is not None:
            answerString_ = self.answerString
            answerString_.to_etree(element, name_='answerString', mapping_=mapping_)
        if self.answerDateTime is not None:
            answerDateTime_ = self.answerDateTime
            answerDateTime_.to_etree(element, name_='answerDateTime', mapping_=mapping_)
        if self.answerInstant is not None:
            answerInstant_ = self.answerInstant
            answerInstant_.to_etree(element, name_='answerInstant', mapping_=mapping_)
        for choice_ in self.choice:
            choice_.to_etree(element, name_='choice', mapping_=mapping_)
        if self.options is not None:
            options_ = self.options
            options_.to_etree(element, name_='options', mapping_=mapping_)
        if self.dataBoolean is not None:
            dataBoolean_ = self.dataBoolean
            dataBoolean_.to_etree(element, name_='dataBoolean', mapping_=mapping_)
        if self.dataInteger is not None:
            dataInteger_ = self.dataInteger
            dataInteger_.to_etree(element, name_='dataInteger', mapping_=mapping_)
        if self.dataDecimal is not None:
            dataDecimal_ = self.dataDecimal
            dataDecimal_.to_etree(element, name_='dataDecimal', mapping_=mapping_)
        if self.dataBase64Binary is not None:
            dataBase64Binary_ = self.dataBase64Binary
            dataBase64Binary_.to_etree(element, name_='dataBase64Binary', mapping_=mapping_)
        if self.dataInstant is not None:
            dataInstant_ = self.dataInstant
            dataInstant_.to_etree(element, name_='dataInstant', mapping_=mapping_)
        if self.dataString is not None:
            dataString_ = self.dataString
            dataString_.to_etree(element, name_='dataString', mapping_=mapping_)
        if self.dataUri is not None:
            dataUri_ = self.dataUri
            dataUri_.to_etree(element, name_='dataUri', mapping_=mapping_)
        if self.dataDate is not None:
            dataDate_ = self.dataDate
            dataDate_.to_etree(element, name_='dataDate', mapping_=mapping_)
        if self.dataDateTime is not None:
            dataDateTime_ = self.dataDateTime
            dataDateTime_.to_etree(element, name_='dataDateTime', mapping_=mapping_)
        if self.dataCode is not None:
            dataCode_ = self.dataCode
            dataCode_.to_etree(element, name_='dataCode', mapping_=mapping_)
        if self.dataOid is not None:
            dataOid_ = self.dataOid
            dataOid_.to_etree(element, name_='dataOid', mapping_=mapping_)
        if self.dataUuid is not None:
            dataUuid_ = self.dataUuid
            dataUuid_.to_etree(element, name_='dataUuid', mapping_=mapping_)
        if self.dataId is not None:
            dataId_ = self.dataId
            dataId_.to_etree(element, name_='dataId', mapping_=mapping_)
        if self.dataAttachment is not None:
            dataAttachment_ = self.dataAttachment
            dataAttachment_.to_etree(element, name_='dataAttachment', mapping_=mapping_)
        if self.dataIdentifier is not None:
            dataIdentifier_ = self.dataIdentifier
            dataIdentifier_.to_etree(element, name_='dataIdentifier', mapping_=mapping_)
        if self.dataCodeableConcept is not None:
            dataCodeableConcept_ = self.dataCodeableConcept
            dataCodeableConcept_.to_etree(element, name_='dataCodeableConcept', mapping_=mapping_)
        if self.dataCoding is not None:
            dataCoding_ = self.dataCoding
            dataCoding_.to_etree(element, name_='dataCoding', mapping_=mapping_)
        if self.dataQuantity is not None:
            dataQuantity_ = self.dataQuantity
            dataQuantity_.to_etree(element, name_='dataQuantity', mapping_=mapping_)
        if self.dataRange is not None:
            dataRange_ = self.dataRange
            dataRange_.to_etree(element, name_='dataRange', mapping_=mapping_)
        if self.dataPeriod is not None:
            dataPeriod_ = self.dataPeriod
            dataPeriod_.to_etree(element, name_='dataPeriod', mapping_=mapping_)
        if self.dataRatio is not None:
            dataRatio_ = self.dataRatio
            dataRatio_.to_etree(element, name_='dataRatio', mapping_=mapping_)
        if self.dataResource is not None:
            dataResource_ = self.dataResource
            dataResource_.to_etree(element, name_='dataResource', mapping_=mapping_)
        if self.dataSampledData is not None:
            dataSampledData_ = self.dataSampledData
            dataSampledData_.to_etree(element, name_='dataSampledData', mapping_=mapping_)
        if self.dataHumanName is not None:
            dataHumanName_ = self.dataHumanName
            dataHumanName_.to_etree(element, name_='dataHumanName', mapping_=mapping_)
        if self.dataAddress is not None:
            dataAddress_ = self.dataAddress
            dataAddress_.to_etree(element, name_='dataAddress', mapping_=mapping_)
        if self.dataContact is not None:
            dataContact_ = self.dataContact
            dataContact_.to_etree(element, name_='dataContact', mapping_=mapping_)
        if self.dataSchedule is not None:
            dataSchedule_ = self.dataSchedule
            dataSchedule_.to_etree(element, name_='dataSchedule', mapping_=mapping_)
        if self.remarks is not None:
            remarks_ = self.remarks
            remarks_.to_etree(element, name_='remarks', mapping_=mapping_)
        for group_ in self.group:
            group_.to_etree(element, name_='group', mapping_=mapping_)
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
        super(Questionnaire_Question, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'name':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.name = obj_
            obj_.original_tagname_ = 'name'
        elif nodeName_ == 'text':
            obj_ = string.factory()
            obj_.build(child_)
            self.text = obj_
            obj_.original_tagname_ = 'text'
        elif nodeName_ == 'answerDecimal':
            obj_ = decimal.factory()
            obj_.build(child_)
            self.answerDecimal = obj_
            obj_.original_tagname_ = 'answerDecimal'
        elif nodeName_ == 'answerInteger':
            obj_ = integer.factory()
            obj_.build(child_)
            self.answerInteger = obj_
            obj_.original_tagname_ = 'answerInteger'
        elif nodeName_ == 'answerBoolean':
            obj_ = boolean.factory()
            obj_.build(child_)
            self.answerBoolean = obj_
            obj_.original_tagname_ = 'answerBoolean'
        elif nodeName_ == 'answerDate':
            obj_ = date.factory()
            obj_.build(child_)
            self.answerDate = obj_
            obj_.original_tagname_ = 'answerDate'
        elif nodeName_ == 'answerString':
            obj_ = string.factory()
            obj_.build(child_)
            self.answerString = obj_
            obj_.original_tagname_ = 'answerString'
        elif nodeName_ == 'answerDateTime':
            obj_ = dateTime.factory()
            obj_.build(child_)
            self.answerDateTime = obj_
            obj_.original_tagname_ = 'answerDateTime'
        elif nodeName_ == 'answerInstant':
            obj_ = instant.factory()
            obj_.build(child_)
            self.answerInstant = obj_
            obj_.original_tagname_ = 'answerInstant'
        elif nodeName_ == 'choice':
            obj_ = Coding.factory()
            obj_.build(child_)
            self.choice.append(obj_)
            obj_.original_tagname_ = 'choice'
        elif nodeName_ == 'options':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.options = obj_
            obj_.original_tagname_ = 'options'
        elif nodeName_ == 'dataBoolean':
            obj_ = boolean.factory()
            obj_.build(child_)
            self.dataBoolean = obj_
            obj_.original_tagname_ = 'dataBoolean'
        elif nodeName_ == 'dataInteger':
            obj_ = integer.factory()
            obj_.build(child_)
            self.dataInteger = obj_
            obj_.original_tagname_ = 'dataInteger'
        elif nodeName_ == 'dataDecimal':
            obj_ = decimal.factory()
            obj_.build(child_)
            self.dataDecimal = obj_
            obj_.original_tagname_ = 'dataDecimal'
        elif nodeName_ == 'dataBase64Binary':
            obj_ = base64Binary.factory()
            obj_.build(child_)
            self.dataBase64Binary = obj_
            obj_.original_tagname_ = 'dataBase64Binary'
        elif nodeName_ == 'dataInstant':
            obj_ = instant.factory()
            obj_.build(child_)
            self.dataInstant = obj_
            obj_.original_tagname_ = 'dataInstant'
        elif nodeName_ == 'dataString':
            obj_ = string.factory()
            obj_.build(child_)
            self.dataString = obj_
            obj_.original_tagname_ = 'dataString'
        elif nodeName_ == 'dataUri':
            obj_ = uri.factory()
            obj_.build(child_)
            self.dataUri = obj_
            obj_.original_tagname_ = 'dataUri'
        elif nodeName_ == 'dataDate':
            obj_ = date.factory()
            obj_.build(child_)
            self.dataDate = obj_
            obj_.original_tagname_ = 'dataDate'
        elif nodeName_ == 'dataDateTime':
            obj_ = dateTime.factory()
            obj_.build(child_)
            self.dataDateTime = obj_
            obj_.original_tagname_ = 'dataDateTime'
        elif nodeName_ == 'dataCode':
            obj_ = code.factory()
            obj_.build(child_)
            self.dataCode = obj_
            obj_.original_tagname_ = 'dataCode'
        elif nodeName_ == 'dataOid':
            obj_ = oid.factory()
            obj_.build(child_)
            self.dataOid = obj_
            obj_.original_tagname_ = 'dataOid'
        elif nodeName_ == 'dataUuid':
            obj_ = uuid.factory()
            obj_.build(child_)
            self.dataUuid = obj_
            obj_.original_tagname_ = 'dataUuid'
        elif nodeName_ == 'dataId':
            obj_ = id.factory()
            obj_.build(child_)
            self.dataId = obj_
            obj_.original_tagname_ = 'dataId'
        elif nodeName_ == 'dataAttachment':
            obj_ = Attachment.factory()
            obj_.build(child_)
            self.dataAttachment = obj_
            obj_.original_tagname_ = 'dataAttachment'
        elif nodeName_ == 'dataIdentifier':
            obj_ = Identifier.factory()
            obj_.build(child_)
            self.dataIdentifier = obj_
            obj_.original_tagname_ = 'dataIdentifier'
        elif nodeName_ == 'dataCodeableConcept':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.dataCodeableConcept = obj_
            obj_.original_tagname_ = 'dataCodeableConcept'
        elif nodeName_ == 'dataCoding':
            obj_ = Coding.factory()
            obj_.build(child_)
            self.dataCoding = obj_
            obj_.original_tagname_ = 'dataCoding'
        elif nodeName_ == 'dataQuantity':
            obj_ = Quantity.factory()
            obj_.build(child_)
            self.dataQuantity = obj_
            obj_.original_tagname_ = 'dataQuantity'
        elif nodeName_ == 'dataRange':
            obj_ = Range.factory()
            obj_.build(child_)
            self.dataRange = obj_
            obj_.original_tagname_ = 'dataRange'
        elif nodeName_ == 'dataPeriod':
            obj_ = Period.factory()
            obj_.build(child_)
            self.dataPeriod = obj_
            obj_.original_tagname_ = 'dataPeriod'
        elif nodeName_ == 'dataRatio':
            obj_ = Ratio.factory()
            obj_.build(child_)
            self.dataRatio = obj_
            obj_.original_tagname_ = 'dataRatio'
        elif nodeName_ == 'dataResource':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.dataResource = obj_
            obj_.original_tagname_ = 'dataResource'
        elif nodeName_ == 'dataSampledData':
            obj_ = SampledData.factory()
            obj_.build(child_)
            self.dataSampledData = obj_
            obj_.original_tagname_ = 'dataSampledData'
        elif nodeName_ == 'dataHumanName':
            obj_ = HumanName.factory()
            obj_.build(child_)
            self.dataHumanName = obj_
            obj_.original_tagname_ = 'dataHumanName'
        elif nodeName_ == 'dataAddress':
            obj_ = Address.factory()
            obj_.build(child_)
            self.dataAddress = obj_
            obj_.original_tagname_ = 'dataAddress'
        elif nodeName_ == 'dataContact':
            obj_ = Contact.factory()
            obj_.build(child_)
            self.dataContact = obj_
            obj_.original_tagname_ = 'dataContact'
        elif nodeName_ == 'dataSchedule':
            obj_ = Schedule.factory()
            obj_.build(child_)
            self.dataSchedule = obj_
            obj_.original_tagname_ = 'dataSchedule'
        elif nodeName_ == 'remarks':
            obj_ = string.factory()
            obj_.build(child_)
            self.remarks = obj_
            obj_.original_tagname_ = 'remarks'
        elif nodeName_ == 'group':
            obj_ = Questionnaire_Group.factory()
            obj_.build(child_)
            self.group.append(obj_)
            obj_.original_tagname_ = 'group'
        super(Questionnaire_Question, self).buildChildren(child_, node, nodeName_, True)
# end class Questionnaire_Question


class QuestionnaireStatus(Element):
    """Lifecycle status of the questionnaireIf the element is present, it
    must have either a @value, an @id, or extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(QuestionnaireStatus, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if QuestionnaireStatus.subclass:
            return QuestionnaireStatus.subclass(*args_, **kwargs_)
        else:
            return QuestionnaireStatus(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(QuestionnaireStatus, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='QuestionnaireStatus', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='QuestionnaireStatus')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='QuestionnaireStatus', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='QuestionnaireStatus'):
        super(QuestionnaireStatus, self).exportAttributes(outfile, level, already_processed, namespace_, name_='QuestionnaireStatus')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='QuestionnaireStatus', fromsubclass_=False, pretty_print=True):
        super(QuestionnaireStatus, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='QuestionnaireStatus', mapping_=None):
        element = super(QuestionnaireStatus, self).to_etree(parent_element, name_, mapping_)
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
        super(QuestionnaireStatus, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(QuestionnaireStatus, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class QuestionnaireStatus
