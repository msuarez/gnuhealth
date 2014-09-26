from .base_classes import *
from .support_functions import *


class Composition(Resource):
    """A set of healthcare-related information that is assembled together
    into a single logical document that provides a single coherent
    statement of meaning, establishes its own context and that has
    clinical attestation with regard to who is making the
    statement.If the element is present, it must have either a
    @value, an @id, or extensions"""
    subclass = None
    superclass = Resource
    def __init__(self, id=None, extension=None, modifierExtension=None, language=None, text=None, contained=None, identifier=None, date=None, type_=None, class_=None, title=None, status=None, confidentiality=None, subject=None, author=None, attester=None, custodian=None, event=None, encounter=None, section=None):
        self.original_tagname_ = None
        super(Composition, self).__init__(id, extension, modifierExtension, language, text, contained, )
        self.identifier = identifier
        self.date = date
        self.type_ = type_
        self.class_ = class_
        self.title = title
        self.status = status
        self.confidentiality = confidentiality
        self.subject = subject
        if author is None:
            self.author = []
        else:
            self.author = author
        if attester is None:
            self.attester = []
        else:
            self.attester = attester
        self.custodian = custodian
        self.event = event
        self.encounter = encounter
        if section is None:
            self.section = []
        else:
            self.section = section
    def factory(*args_, **kwargs_):
        if Composition.subclass:
            return Composition.subclass(*args_, **kwargs_)
        else:
            return Composition(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_identifier(self): return self.identifier
    def set_identifier(self, identifier): self.identifier = identifier
    def get_date(self): return self.date
    def set_date(self, date): self.date = date
    def get_type(self): return self.type_
    def set_type(self, type_): self.type_ = type_
    def get_class(self): return self.class_
    def set_class(self, class_): self.class_ = class_
    def get_title(self): return self.title
    def set_title(self, title): self.title = title
    def get_status(self): return self.status
    def set_status(self, status): self.status = status
    def get_confidentiality(self): return self.confidentiality
    def set_confidentiality(self, confidentiality): self.confidentiality = confidentiality
    def get_subject(self): return self.subject
    def set_subject(self, subject): self.subject = subject
    def get_author(self): return self.author
    def set_author(self, author): self.author = author
    def add_author(self, value): self.author.append(value)
    def insert_author(self, index, value): self.author[index] = value
    def get_attester(self): return self.attester
    def set_attester(self, attester): self.attester = attester
    def add_attester(self, value): self.attester.append(value)
    def insert_attester(self, index, value): self.attester[index] = value
    def get_custodian(self): return self.custodian
    def set_custodian(self, custodian): self.custodian = custodian
    def get_event(self): return self.event
    def set_event(self, event): self.event = event
    def get_encounter(self): return self.encounter
    def set_encounter(self, encounter): self.encounter = encounter
    def get_section(self): return self.section
    def set_section(self, section): self.section = section
    def add_section(self, value): self.section.append(value)
    def insert_section(self, index, value): self.section[index] = value
    def hasContent_(self):
        if (
            self.identifier is not None or
            self.date is not None or
            self.type_ is not None or
            self.class_ is not None or
            self.title is not None or
            self.status is not None or
            self.confidentiality is not None or
            self.subject is not None or
            self.author or
            self.attester or
            self.custodian is not None or
            self.event is not None or
            self.encounter is not None or
            self.section or
            super(Composition, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Composition', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Composition')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Composition', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Composition'):
        super(Composition, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Composition')
    def exportChildren(self, outfile, level, namespace_='', name_='Composition', fromsubclass_=False, pretty_print=True):
        super(Composition, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.identifier is not None:
            self.identifier.export(outfile, level, namespace_, name_='identifier', pretty_print=pretty_print)
        if self.date is not None:
            self.date.export(outfile, level, namespace_, name_='date', pretty_print=pretty_print)
        if self.type_ is not None:
            self.type_.export(outfile, level, namespace_, name_='type', pretty_print=pretty_print)
        if self.class_ is not None:
            self.class_.export(outfile, level, namespace_, name_='class', pretty_print=pretty_print)
        if self.title is not None:
            self.title.export(outfile, level, namespace_, name_='title', pretty_print=pretty_print)
        if self.status is not None:
            self.status.export(outfile, level, namespace_, name_='status', pretty_print=pretty_print)
        if self.confidentiality is not None:
            self.confidentiality.export(outfile, level, namespace_, name_='confidentiality', pretty_print=pretty_print)
        if self.subject is not None:
            self.subject.export(outfile, level, namespace_, name_='subject', pretty_print=pretty_print)
        for author_ in self.author:
            author_.export(outfile, level, namespace_, name_='author', pretty_print=pretty_print)
        for attester_ in self.attester:
            attester_.export(outfile, level, namespace_, name_='attester', pretty_print=pretty_print)
        if self.custodian is not None:
            self.custodian.export(outfile, level, namespace_, name_='custodian', pretty_print=pretty_print)
        if self.event is not None:
            self.event.export(outfile, level, namespace_, name_='event', pretty_print=pretty_print)
        if self.encounter is not None:
            self.encounter.export(outfile, level, namespace_, name_='encounter', pretty_print=pretty_print)
        for section_ in self.section:
            section_.export(outfile, level, namespace_, name_='section', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Composition', mapping_=None):
        element = super(Composition, self).to_etree(parent_element, name_, mapping_)
        if self.identifier is not None:
            identifier_ = self.identifier
            identifier_.to_etree(element, name_='identifier', mapping_=mapping_)
        if self.date is not None:
            date_ = self.date
            date_.to_etree(element, name_='date', mapping_=mapping_)
        if self.type_ is not None:
            type__ = self.type_
            type__.to_etree(element, name_='type', mapping_=mapping_)
        if self.class_ is not None:
            class__ = self.class_
            class__.to_etree(element, name_='class', mapping_=mapping_)
        if self.title is not None:
            title_ = self.title
            title_.to_etree(element, name_='title', mapping_=mapping_)
        if self.status is not None:
            status_ = self.status
            status_.to_etree(element, name_='status', mapping_=mapping_)
        if self.confidentiality is not None:
            confidentiality_ = self.confidentiality
            confidentiality_.to_etree(element, name_='confidentiality', mapping_=mapping_)
        if self.subject is not None:
            subject_ = self.subject
            subject_.to_etree(element, name_='subject', mapping_=mapping_)
        for author_ in self.author:
            author_.to_etree(element, name_='author', mapping_=mapping_)
        for attester_ in self.attester:
            attester_.to_etree(element, name_='attester', mapping_=mapping_)
        if self.custodian is not None:
            custodian_ = self.custodian
            custodian_.to_etree(element, name_='custodian', mapping_=mapping_)
        if self.event is not None:
            event_ = self.event
            event_.to_etree(element, name_='event', mapping_=mapping_)
        if self.encounter is not None:
            encounter_ = self.encounter
            encounter_.to_etree(element, name_='encounter', mapping_=mapping_)
        for section_ in self.section:
            section_.to_etree(element, name_='section', mapping_=mapping_)
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
        super(Composition, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'identifier':
            obj_ = Identifier.factory()
            obj_.build(child_)
            self.identifier = obj_
            obj_.original_tagname_ = 'identifier'
        elif nodeName_ == 'date':
            obj_ = dateTime.factory()
            obj_.build(child_)
            self.date = obj_
            obj_.original_tagname_ = 'date'
        elif nodeName_ == 'type':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.type_ = obj_
            obj_.original_tagname_ = 'type'
        elif nodeName_ == 'class':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.class_ = obj_
            obj_.original_tagname_ = 'class'
        elif nodeName_ == 'title':
            obj_ = string.factory()
            obj_.build(child_)
            self.title = obj_
            obj_.original_tagname_ = 'title'
        elif nodeName_ == 'status':
            obj_ = CompositionStatus.factory()
            obj_.build(child_)
            self.status = obj_
            obj_.original_tagname_ = 'status'
        elif nodeName_ == 'confidentiality':
            obj_ = Coding.factory()
            obj_.build(child_)
            self.confidentiality = obj_
            obj_.original_tagname_ = 'confidentiality'
        elif nodeName_ == 'subject':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.subject = obj_
            obj_.original_tagname_ = 'subject'
        elif nodeName_ == 'author':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.author.append(obj_)
            obj_.original_tagname_ = 'author'
        elif nodeName_ == 'attester':
            obj_ = Composition_Attester.factory()
            obj_.build(child_)
            self.attester.append(obj_)
            obj_.original_tagname_ = 'attester'
        elif nodeName_ == 'custodian':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.custodian = obj_
            obj_.original_tagname_ = 'custodian'
        elif nodeName_ == 'event':
            obj_ = Composition_Event.factory()
            obj_.build(child_)
            self.event = obj_
            obj_.original_tagname_ = 'event'
        elif nodeName_ == 'encounter':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.encounter = obj_
            obj_.original_tagname_ = 'encounter'
        elif nodeName_ == 'section':
            obj_ = Composition_Section.factory()
            obj_.build(child_)
            self.section.append(obj_)
            obj_.original_tagname_ = 'section'
        super(Composition, self).buildChildren(child_, node, nodeName_, True)
# end class Composition


class Composition_Attester(BackboneElement):
    """A set of healthcare-related information that is assembled together
    into a single logical document that provides a single coherent
    statement of meaning, establishes its own context and that has
    clinical attestation with regard to who is making the statement."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, mode=None, time=None, party=None):
        self.original_tagname_ = None
        super(Composition_Attester, self).__init__(id, extension, modifierExtension, )
        if mode is None:
            self.mode = []
        else:
            self.mode = mode
        self.time = time
        self.party = party
    def factory(*args_, **kwargs_):
        if Composition_Attester.subclass:
            return Composition_Attester.subclass(*args_, **kwargs_)
        else:
            return Composition_Attester(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_mode(self): return self.mode
    def set_mode(self, mode): self.mode = mode
    def add_mode(self, value): self.mode.append(value)
    def insert_mode(self, index, value): self.mode[index] = value
    def get_time(self): return self.time
    def set_time(self, time): self.time = time
    def get_party(self): return self.party
    def set_party(self, party): self.party = party
    def hasContent_(self):
        if (
            self.mode or
            self.time is not None or
            self.party is not None or
            super(Composition_Attester, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Composition.Attester', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Composition.Attester')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Composition.Attester', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Composition.Attester'):
        super(Composition_Attester, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Composition.Attester')
    def exportChildren(self, outfile, level, namespace_='', name_='Composition.Attester', fromsubclass_=False, pretty_print=True):
        super(Composition_Attester, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for mode_ in self.mode:
            mode_.export(outfile, level, namespace_, name_='mode', pretty_print=pretty_print)
        if self.time is not None:
            self.time.export(outfile, level, namespace_, name_='time', pretty_print=pretty_print)
        if self.party is not None:
            self.party.export(outfile, level, namespace_, name_='party', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Composition.Attester', mapping_=None):
        element = super(Composition_Attester, self).to_etree(parent_element, name_, mapping_)
        for mode_ in self.mode:
            mode_.to_etree(element, name_='mode', mapping_=mapping_)
        if self.time is not None:
            time_ = self.time
            time_.to_etree(element, name_='time', mapping_=mapping_)
        if self.party is not None:
            party_ = self.party
            party_.to_etree(element, name_='party', mapping_=mapping_)
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
        super(Composition_Attester, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'mode':
            obj_ = CompositionAttestationMode.factory()
            obj_.build(child_)
            self.mode.append(obj_)
            obj_.original_tagname_ = 'mode'
        elif nodeName_ == 'time':
            obj_ = dateTime.factory()
            obj_.build(child_)
            self.time = obj_
            obj_.original_tagname_ = 'time'
        elif nodeName_ == 'party':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.party = obj_
            obj_.original_tagname_ = 'party'
        super(Composition_Attester, self).buildChildren(child_, node, nodeName_, True)
# end class Composition_Attester


class Composition_Event(BackboneElement):
    """A set of healthcare-related information that is assembled together
    into a single logical document that provides a single coherent
    statement of meaning, establishes its own context and that has
    clinical attestation with regard to who is making the statement."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, code=None, period=None, detail=None):
        self.original_tagname_ = None
        super(Composition_Event, self).__init__(id, extension, modifierExtension, )
        if code is None:
            self.code = []
        else:
            self.code = code
        self.period = period
        if detail is None:
            self.detail = []
        else:
            self.detail = detail
    def factory(*args_, **kwargs_):
        if Composition_Event.subclass:
            return Composition_Event.subclass(*args_, **kwargs_)
        else:
            return Composition_Event(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_code(self): return self.code
    def set_code(self, code): self.code = code
    def add_code(self, value): self.code.append(value)
    def insert_code(self, index, value): self.code[index] = value
    def get_period(self): return self.period
    def set_period(self, period): self.period = period
    def get_detail(self): return self.detail
    def set_detail(self, detail): self.detail = detail
    def add_detail(self, value): self.detail.append(value)
    def insert_detail(self, index, value): self.detail[index] = value
    def hasContent_(self):
        if (
            self.code or
            self.period is not None or
            self.detail or
            super(Composition_Event, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Composition.Event', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Composition.Event')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Composition.Event', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Composition.Event'):
        super(Composition_Event, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Composition.Event')
    def exportChildren(self, outfile, level, namespace_='', name_='Composition.Event', fromsubclass_=False, pretty_print=True):
        super(Composition_Event, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for code_ in self.code:
            code_.export(outfile, level, namespace_, name_='code', pretty_print=pretty_print)
        if self.period is not None:
            self.period.export(outfile, level, namespace_, name_='period', pretty_print=pretty_print)
        for detail_ in self.detail:
            detail_.export(outfile, level, namespace_, name_='detail', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Composition.Event', mapping_=None):
        element = super(Composition_Event, self).to_etree(parent_element, name_, mapping_)
        for code_ in self.code:
            code_.to_etree(element, name_='code', mapping_=mapping_)
        if self.period is not None:
            period_ = self.period
            period_.to_etree(element, name_='period', mapping_=mapping_)
        for detail_ in self.detail:
            detail_.to_etree(element, name_='detail', mapping_=mapping_)
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
        super(Composition_Event, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'code':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.code.append(obj_)
            obj_.original_tagname_ = 'code'
        elif nodeName_ == 'period':
            obj_ = Period.factory()
            obj_.build(child_)
            self.period = obj_
            obj_.original_tagname_ = 'period'
        elif nodeName_ == 'detail':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.detail.append(obj_)
            obj_.original_tagname_ = 'detail'
        super(Composition_Event, self).buildChildren(child_, node, nodeName_, True)
# end class Composition_Event


class Composition_Section(BackboneElement):
    """A set of healthcare-related information that is assembled together
    into a single logical document that provides a single coherent
    statement of meaning, establishes its own context and that has
    clinical attestation with regard to who is making the statement."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, title=None, code=None, subject=None, content=None, section=None):
        self.original_tagname_ = None
        super(Composition_Section, self).__init__(id, extension, modifierExtension, )
        self.title = title
        self.code = code
        self.subject = subject
        self.content = content
        if section is None:
            self.section = []
        else:
            self.section = section
    def factory(*args_, **kwargs_):
        if Composition_Section.subclass:
            return Composition_Section.subclass(*args_, **kwargs_)
        else:
            return Composition_Section(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_title(self): return self.title
    def set_title(self, title): self.title = title
    def get_code(self): return self.code
    def set_code(self, code): self.code = code
    def get_subject(self): return self.subject
    def set_subject(self, subject): self.subject = subject
    def get_content(self): return self.content
    def set_content(self, content): self.content = content
    def get_section(self): return self.section
    def set_section(self, section): self.section = section
    def add_section(self, value): self.section.append(value)
    def insert_section(self, index, value): self.section[index] = value
    def hasContent_(self):
        if (
            self.title is not None or
            self.code is not None or
            self.subject is not None or
            self.content is not None or
            self.section or
            super(Composition_Section, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Composition.Section', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Composition.Section')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Composition.Section', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Composition.Section'):
        super(Composition_Section, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Composition.Section')
    def exportChildren(self, outfile, level, namespace_='', name_='Composition.Section', fromsubclass_=False, pretty_print=True):
        super(Composition_Section, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.title is not None:
            self.title.export(outfile, level, namespace_, name_='title', pretty_print=pretty_print)
        if self.code is not None:
            self.code.export(outfile, level, namespace_, name_='code', pretty_print=pretty_print)
        if self.subject is not None:
            self.subject.export(outfile, level, namespace_, name_='subject', pretty_print=pretty_print)
        if self.content is not None:
            self.content.export(outfile, level, namespace_, name_='content', pretty_print=pretty_print)
        for section_ in self.section:
            section_.export(outfile, level, namespace_, name_='section', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Composition.Section', mapping_=None):
        element = super(Composition_Section, self).to_etree(parent_element, name_, mapping_)
        if self.title is not None:
            title_ = self.title
            title_.to_etree(element, name_='title', mapping_=mapping_)
        if self.code is not None:
            code_ = self.code
            code_.to_etree(element, name_='code', mapping_=mapping_)
        if self.subject is not None:
            subject_ = self.subject
            subject_.to_etree(element, name_='subject', mapping_=mapping_)
        if self.content is not None:
            content_ = self.content
            content_.to_etree(element, name_='content', mapping_=mapping_)
        for section_ in self.section:
            section_.to_etree(element, name_='section', mapping_=mapping_)
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
        super(Composition_Section, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'title':
            obj_ = string.factory()
            obj_.build(child_)
            self.title = obj_
            obj_.original_tagname_ = 'title'
        elif nodeName_ == 'code':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.code = obj_
            obj_.original_tagname_ = 'code'
        elif nodeName_ == 'subject':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.subject = obj_
            obj_.original_tagname_ = 'subject'
        elif nodeName_ == 'content':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.content = obj_
            obj_.original_tagname_ = 'content'
        elif nodeName_ == 'section':
            obj_ = Composition_Section.factory()
            obj_.build(child_)
            self.section.append(obj_)
            obj_.original_tagname_ = 'section'
        super(Composition_Section, self).buildChildren(child_, node, nodeName_, True)
# end class Composition_Section


class CompositionStatus(Element):
    """The workflow/clinical status of the compositionIf the element is
    present, it must have either a @value, an @id, or extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(CompositionStatus, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if CompositionStatus.subclass:
            return CompositionStatus.subclass(*args_, **kwargs_)
        else:
            return CompositionStatus(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(CompositionStatus, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='CompositionStatus', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='CompositionStatus')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='CompositionStatus', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='CompositionStatus'):
        super(CompositionStatus, self).exportAttributes(outfile, level, already_processed, namespace_, name_='CompositionStatus')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='CompositionStatus', fromsubclass_=False, pretty_print=True):
        super(CompositionStatus, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='CompositionStatus', mapping_=None):
        element = super(CompositionStatus, self).to_etree(parent_element, name_, mapping_)
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
        super(CompositionStatus, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(CompositionStatus, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class CompositionStatus


class CompositionAttestationMode(Element):
    """The way in which a person authenticated a compositionIf the element
    is present, it must have either a @value, an @id, or extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(CompositionAttestationMode, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if CompositionAttestationMode.subclass:
            return CompositionAttestationMode.subclass(*args_, **kwargs_)
        else:
            return CompositionAttestationMode(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(CompositionAttestationMode, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='CompositionAttestationMode', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='CompositionAttestationMode')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='CompositionAttestationMode', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='CompositionAttestationMode'):
        super(CompositionAttestationMode, self).exportAttributes(outfile, level, already_processed, namespace_, name_='CompositionAttestationMode')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='CompositionAttestationMode', fromsubclass_=False, pretty_print=True):
        super(CompositionAttestationMode, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='CompositionAttestationMode', mapping_=None):
        element = super(CompositionAttestationMode, self).to_etree(parent_element, name_, mapping_)
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
        super(CompositionAttestationMode, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(CompositionAttestationMode, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class CompositionAttestationMode
