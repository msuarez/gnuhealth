from .base_classes import *
from .support_functions import *


class SecurityEvent(Resource):
    """A record of an event made for purposes of maintaining a security
    log. Typical uses include detection of intrusion attempts and
    monitoring for inappropriate usage.If the element is present, it
    must have either a @value, an @id, or extensions"""
    subclass = None
    superclass = Resource
    def __init__(self, id=None, extension=None, modifierExtension=None, language=None, text=None, contained=None, event=None, participant=None, source=None, object=None):
        self.original_tagname_ = None
        super(SecurityEvent, self).__init__(id, extension, modifierExtension, language, text, contained, )
        self.event = event
        if participant is None:
            self.participant = []
        else:
            self.participant = participant
        self.source = source
        if object is None:
            self.object = []
        else:
            self.object = object
    def factory(*args_, **kwargs_):
        if SecurityEvent.subclass:
            return SecurityEvent.subclass(*args_, **kwargs_)
        else:
            return SecurityEvent(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_event(self): return self.event
    def set_event(self, event): self.event = event
    def get_participant(self): return self.participant
    def set_participant(self, participant): self.participant = participant
    def add_participant(self, value): self.participant.append(value)
    def insert_participant(self, index, value): self.participant[index] = value
    def get_source(self): return self.source
    def set_source(self, source): self.source = source
    def get_object(self): return self.object
    def set_object(self, object): self.object = object
    def add_object(self, value): self.object.append(value)
    def insert_object(self, index, value): self.object[index] = value
    def hasContent_(self):
        if (
            self.event is not None or
            self.participant or
            self.source is not None or
            self.object or
            super(SecurityEvent, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='SecurityEvent', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='SecurityEvent')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='SecurityEvent', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='SecurityEvent'):
        super(SecurityEvent, self).exportAttributes(outfile, level, already_processed, namespace_, name_='SecurityEvent')
    def exportChildren(self, outfile, level, namespace_='', name_='SecurityEvent', fromsubclass_=False, pretty_print=True):
        super(SecurityEvent, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.event is not None:
            self.event.export(outfile, level, namespace_, name_='event', pretty_print=pretty_print)
        for participant_ in self.participant:
            participant_.export(outfile, level, namespace_, name_='participant', pretty_print=pretty_print)
        if self.source is not None:
            self.source.export(outfile, level, namespace_, name_='source', pretty_print=pretty_print)
        for object_ in self.object:
            object_.export(outfile, level, namespace_, name_='object', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='SecurityEvent', mapping_=None):
        element = super(SecurityEvent, self).to_etree(parent_element, name_, mapping_)
        if self.event is not None:
            event_ = self.event
            event_.to_etree(element, name_='event', mapping_=mapping_)
        for participant_ in self.participant:
            participant_.to_etree(element, name_='participant', mapping_=mapping_)
        if self.source is not None:
            source_ = self.source
            source_.to_etree(element, name_='source', mapping_=mapping_)
        for object_ in self.object:
            object_.to_etree(element, name_='object', mapping_=mapping_)
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
        super(SecurityEvent, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'event':
            obj_ = SecurityEvent_Event.factory()
            obj_.build(child_)
            self.event = obj_
            obj_.original_tagname_ = 'event'
        elif nodeName_ == 'participant':
            obj_ = SecurityEvent_Participant.factory()
            obj_.build(child_)
            self.participant.append(obj_)
            obj_.original_tagname_ = 'participant'
        elif nodeName_ == 'source':
            obj_ = SecurityEvent_Source.factory()
            obj_.build(child_)
            self.source = obj_
            obj_.original_tagname_ = 'source'
        elif nodeName_ == 'object':
            obj_ = SecurityEvent_Object.factory()
            obj_.build(child_)
            self.object.append(obj_)
            obj_.original_tagname_ = 'object'
        super(SecurityEvent, self).buildChildren(child_, node, nodeName_, True)
# end class SecurityEvent


class SecurityEvent_Event(BackboneElement):
    """A record of an event made for purposes of maintaining a security
    log. Typical uses include detection of intrusion attempts and
    monitoring for inappropriate usage."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, type_=None, subtype=None, action=None, dateTime=None, outcome=None, outcomeDesc=None):
        self.original_tagname_ = None
        super(SecurityEvent_Event, self).__init__(id, extension, modifierExtension, )
        self.type_ = type_
        if subtype is None:
            self.subtype = []
        else:
            self.subtype = subtype
        self.action = action
        self.dateTime = dateTime
        self.outcome = outcome
        self.outcomeDesc = outcomeDesc
    def factory(*args_, **kwargs_):
        if SecurityEvent_Event.subclass:
            return SecurityEvent_Event.subclass(*args_, **kwargs_)
        else:
            return SecurityEvent_Event(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_type(self): return self.type_
    def set_type(self, type_): self.type_ = type_
    def get_subtype(self): return self.subtype
    def set_subtype(self, subtype): self.subtype = subtype
    def add_subtype(self, value): self.subtype.append(value)
    def insert_subtype(self, index, value): self.subtype[index] = value
    def get_action(self): return self.action
    def set_action(self, action): self.action = action
    def get_dateTime(self): return self.dateTime
    def set_dateTime(self, dateTime): self.dateTime = dateTime
    def get_outcome(self): return self.outcome
    def set_outcome(self, outcome): self.outcome = outcome
    def get_outcomeDesc(self): return self.outcomeDesc
    def set_outcomeDesc(self, outcomeDesc): self.outcomeDesc = outcomeDesc
    def hasContent_(self):
        if (
            self.type_ is not None or
            self.subtype or
            self.action is not None or
            self.dateTime is not None or
            self.outcome is not None or
            self.outcomeDesc is not None or
            super(SecurityEvent_Event, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='SecurityEvent.Event', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='SecurityEvent.Event')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='SecurityEvent.Event', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='SecurityEvent.Event'):
        super(SecurityEvent_Event, self).exportAttributes(outfile, level, already_processed, namespace_, name_='SecurityEvent.Event')
    def exportChildren(self, outfile, level, namespace_='', name_='SecurityEvent.Event', fromsubclass_=False, pretty_print=True):
        super(SecurityEvent_Event, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.type_ is not None:
            self.type_.export(outfile, level, namespace_, name_='type', pretty_print=pretty_print)
        for subtype_ in self.subtype:
            subtype_.export(outfile, level, namespace_, name_='subtype', pretty_print=pretty_print)
        if self.action is not None:
            self.action.export(outfile, level, namespace_, name_='action', pretty_print=pretty_print)
        if self.dateTime is not None:
            self.dateTime.export(outfile, level, namespace_, name_='dateTime', pretty_print=pretty_print)
        if self.outcome is not None:
            self.outcome.export(outfile, level, namespace_, name_='outcome', pretty_print=pretty_print)
        if self.outcomeDesc is not None:
            self.outcomeDesc.export(outfile, level, namespace_, name_='outcomeDesc', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='SecurityEvent.Event', mapping_=None):
        element = super(SecurityEvent_Event, self).to_etree(parent_element, name_, mapping_)
        if self.type_ is not None:
            type__ = self.type_
            type__.to_etree(element, name_='type', mapping_=mapping_)
        for subtype_ in self.subtype:
            subtype_.to_etree(element, name_='subtype', mapping_=mapping_)
        if self.action is not None:
            action_ = self.action
            action_.to_etree(element, name_='action', mapping_=mapping_)
        if self.dateTime is not None:
            dateTime_ = self.dateTime
            dateTime_.to_etree(element, name_='dateTime', mapping_=mapping_)
        if self.outcome is not None:
            outcome_ = self.outcome
            outcome_.to_etree(element, name_='outcome', mapping_=mapping_)
        if self.outcomeDesc is not None:
            outcomeDesc_ = self.outcomeDesc
            outcomeDesc_.to_etree(element, name_='outcomeDesc', mapping_=mapping_)
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
        super(SecurityEvent_Event, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'type':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.type_ = obj_
            obj_.original_tagname_ = 'type'
        elif nodeName_ == 'subtype':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.subtype.append(obj_)
            obj_.original_tagname_ = 'subtype'
        elif nodeName_ == 'action':
            obj_ = SecurityEventAction.factory()
            obj_.build(child_)
            self.action = obj_
            obj_.original_tagname_ = 'action'
        elif nodeName_ == 'dateTime':
            obj_ = instant.factory()
            obj_.build(child_)
            self.dateTime = obj_
            obj_.original_tagname_ = 'dateTime'
        elif nodeName_ == 'outcome':
            obj_ = SecurityEventOutcome.factory()
            obj_.build(child_)
            self.outcome = obj_
            obj_.original_tagname_ = 'outcome'
        elif nodeName_ == 'outcomeDesc':
            obj_ = string.factory()
            obj_.build(child_)
            self.outcomeDesc = obj_
            obj_.original_tagname_ = 'outcomeDesc'
        super(SecurityEvent_Event, self).buildChildren(child_, node, nodeName_, True)
# end class SecurityEvent_Event


class SecurityEvent_Participant(BackboneElement):
    """A record of an event made for purposes of maintaining a security
    log. Typical uses include detection of intrusion attempts and
    monitoring for inappropriate usage."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, role=None, reference=None, userId=None, altId=None, name=None, requestor=None, media=None, network=None):
        self.original_tagname_ = None
        super(SecurityEvent_Participant, self).__init__(id, extension, modifierExtension, )
        if role is None:
            self.role = []
        else:
            self.role = role
        self.reference = reference
        self.userId = userId
        self.altId = altId
        self.name = name
        self.requestor = requestor
        self.media = media
        self.network = network
    def factory(*args_, **kwargs_):
        if SecurityEvent_Participant.subclass:
            return SecurityEvent_Participant.subclass(*args_, **kwargs_)
        else:
            return SecurityEvent_Participant(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_role(self): return self.role
    def set_role(self, role): self.role = role
    def add_role(self, value): self.role.append(value)
    def insert_role(self, index, value): self.role[index] = value
    def get_reference(self): return self.reference
    def set_reference(self, reference): self.reference = reference
    def get_userId(self): return self.userId
    def set_userId(self, userId): self.userId = userId
    def get_altId(self): return self.altId
    def set_altId(self, altId): self.altId = altId
    def get_name(self): return self.name
    def set_name(self, name): self.name = name
    def get_requestor(self): return self.requestor
    def set_requestor(self, requestor): self.requestor = requestor
    def get_media(self): return self.media
    def set_media(self, media): self.media = media
    def get_network(self): return self.network
    def set_network(self, network): self.network = network
    def hasContent_(self):
        if (
            self.role or
            self.reference is not None or
            self.userId is not None or
            self.altId is not None or
            self.name is not None or
            self.requestor is not None or
            self.media is not None or
            self.network is not None or
            super(SecurityEvent_Participant, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='SecurityEvent.Participant', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='SecurityEvent.Participant')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='SecurityEvent.Participant', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='SecurityEvent.Participant'):
        super(SecurityEvent_Participant, self).exportAttributes(outfile, level, already_processed, namespace_, name_='SecurityEvent.Participant')
    def exportChildren(self, outfile, level, namespace_='', name_='SecurityEvent.Participant', fromsubclass_=False, pretty_print=True):
        super(SecurityEvent_Participant, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for role_ in self.role:
            role_.export(outfile, level, namespace_, name_='role', pretty_print=pretty_print)
        if self.reference is not None:
            self.reference.export(outfile, level, namespace_, name_='reference', pretty_print=pretty_print)
        if self.userId is not None:
            self.userId.export(outfile, level, namespace_, name_='userId', pretty_print=pretty_print)
        if self.altId is not None:
            self.altId.export(outfile, level, namespace_, name_='altId', pretty_print=pretty_print)
        if self.name is not None:
            self.name.export(outfile, level, namespace_, name_='name', pretty_print=pretty_print)
        if self.requestor is not None:
            self.requestor.export(outfile, level, namespace_, name_='requestor', pretty_print=pretty_print)
        if self.media is not None:
            self.media.export(outfile, level, namespace_, name_='media', pretty_print=pretty_print)
        if self.network is not None:
            self.network.export(outfile, level, namespace_, name_='network', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='SecurityEvent.Participant', mapping_=None):
        element = super(SecurityEvent_Participant, self).to_etree(parent_element, name_, mapping_)
        for role_ in self.role:
            role_.to_etree(element, name_='role', mapping_=mapping_)
        if self.reference is not None:
            reference_ = self.reference
            reference_.to_etree(element, name_='reference', mapping_=mapping_)
        if self.userId is not None:
            userId_ = self.userId
            userId_.to_etree(element, name_='userId', mapping_=mapping_)
        if self.altId is not None:
            altId_ = self.altId
            altId_.to_etree(element, name_='altId', mapping_=mapping_)
        if self.name is not None:
            name_ = self.name
            name_.to_etree(element, name_='name', mapping_=mapping_)
        if self.requestor is not None:
            requestor_ = self.requestor
            requestor_.to_etree(element, name_='requestor', mapping_=mapping_)
        if self.media is not None:
            media_ = self.media
            media_.to_etree(element, name_='media', mapping_=mapping_)
        if self.network is not None:
            network_ = self.network
            network_.to_etree(element, name_='network', mapping_=mapping_)
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
        super(SecurityEvent_Participant, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'role':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.role.append(obj_)
            obj_.original_tagname_ = 'role'
        elif nodeName_ == 'reference':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.reference = obj_
            obj_.original_tagname_ = 'reference'
        elif nodeName_ == 'userId':
            obj_ = string.factory()
            obj_.build(child_)
            self.userId = obj_
            obj_.original_tagname_ = 'userId'
        elif nodeName_ == 'altId':
            obj_ = string.factory()
            obj_.build(child_)
            self.altId = obj_
            obj_.original_tagname_ = 'altId'
        elif nodeName_ == 'name':
            obj_ = string.factory()
            obj_.build(child_)
            self.name = obj_
            obj_.original_tagname_ = 'name'
        elif nodeName_ == 'requestor':
            obj_ = boolean.factory()
            obj_.build(child_)
            self.requestor = obj_
            obj_.original_tagname_ = 'requestor'
        elif nodeName_ == 'media':
            obj_ = Coding.factory()
            obj_.build(child_)
            self.media = obj_
            obj_.original_tagname_ = 'media'
        elif nodeName_ == 'network':
            obj_ = SecurityEvent_Network.factory()
            obj_.build(child_)
            self.network = obj_
            obj_.original_tagname_ = 'network'
        super(SecurityEvent_Participant, self).buildChildren(child_, node, nodeName_, True)
# end class SecurityEvent_Participant


class SecurityEvent_Network(BackboneElement):
    """A record of an event made for purposes of maintaining a security
    log. Typical uses include detection of intrusion attempts and
    monitoring for inappropriate usage."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, identifier=None, type_=None):
        self.original_tagname_ = None
        super(SecurityEvent_Network, self).__init__(id, extension, modifierExtension, )
        self.identifier = identifier
        self.type_ = type_
    def factory(*args_, **kwargs_):
        if SecurityEvent_Network.subclass:
            return SecurityEvent_Network.subclass(*args_, **kwargs_)
        else:
            return SecurityEvent_Network(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_identifier(self): return self.identifier
    def set_identifier(self, identifier): self.identifier = identifier
    def get_type(self): return self.type_
    def set_type(self, type_): self.type_ = type_
    def hasContent_(self):
        if (
            self.identifier is not None or
            self.type_ is not None or
            super(SecurityEvent_Network, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='SecurityEvent.Network', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='SecurityEvent.Network')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='SecurityEvent.Network', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='SecurityEvent.Network'):
        super(SecurityEvent_Network, self).exportAttributes(outfile, level, already_processed, namespace_, name_='SecurityEvent.Network')
    def exportChildren(self, outfile, level, namespace_='', name_='SecurityEvent.Network', fromsubclass_=False, pretty_print=True):
        super(SecurityEvent_Network, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.identifier is not None:
            self.identifier.export(outfile, level, namespace_, name_='identifier', pretty_print=pretty_print)
        if self.type_ is not None:
            self.type_.export(outfile, level, namespace_, name_='type', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='SecurityEvent.Network', mapping_=None):
        element = super(SecurityEvent_Network, self).to_etree(parent_element, name_, mapping_)
        if self.identifier is not None:
            identifier_ = self.identifier
            identifier_.to_etree(element, name_='identifier', mapping_=mapping_)
        if self.type_ is not None:
            type__ = self.type_
            type__.to_etree(element, name_='type', mapping_=mapping_)
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
        super(SecurityEvent_Network, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'identifier':
            obj_ = string.factory()
            obj_.build(child_)
            self.identifier = obj_
            obj_.original_tagname_ = 'identifier'
        elif nodeName_ == 'type':
            obj_ = SecurityEventParticipantNetworkType.factory()
            obj_.build(child_)
            self.type_ = obj_
            obj_.original_tagname_ = 'type'
        super(SecurityEvent_Network, self).buildChildren(child_, node, nodeName_, True)
# end class SecurityEvent_Network


class SecurityEvent_Source(BackboneElement):
    """A record of an event made for purposes of maintaining a security
    log. Typical uses include detection of intrusion attempts and
    monitoring for inappropriate usage."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, site=None, identifier=None, type_=None):
        self.original_tagname_ = None
        super(SecurityEvent_Source, self).__init__(id, extension, modifierExtension, )
        self.site = site
        self.identifier = identifier
        if type_ is None:
            self.type_ = []
        else:
            self.type_ = type_
    def factory(*args_, **kwargs_):
        if SecurityEvent_Source.subclass:
            return SecurityEvent_Source.subclass(*args_, **kwargs_)
        else:
            return SecurityEvent_Source(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_site(self): return self.site
    def set_site(self, site): self.site = site
    def get_identifier(self): return self.identifier
    def set_identifier(self, identifier): self.identifier = identifier
    def get_type(self): return self.type_
    def set_type(self, type_): self.type_ = type_
    def add_type(self, value): self.type_.append(value)
    def insert_type(self, index, value): self.type_[index] = value
    def hasContent_(self):
        if (
            self.site is not None or
            self.identifier is not None or
            self.type_ or
            super(SecurityEvent_Source, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='SecurityEvent.Source', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='SecurityEvent.Source')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='SecurityEvent.Source', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='SecurityEvent.Source'):
        super(SecurityEvent_Source, self).exportAttributes(outfile, level, already_processed, namespace_, name_='SecurityEvent.Source')
    def exportChildren(self, outfile, level, namespace_='', name_='SecurityEvent.Source', fromsubclass_=False, pretty_print=True):
        super(SecurityEvent_Source, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.site is not None:
            self.site.export(outfile, level, namespace_, name_='site', pretty_print=pretty_print)
        if self.identifier is not None:
            self.identifier.export(outfile, level, namespace_, name_='identifier', pretty_print=pretty_print)
        for type_ in self.type_:
            type_.export(outfile, level, namespace_, name_='type', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='SecurityEvent.Source', mapping_=None):
        element = super(SecurityEvent_Source, self).to_etree(parent_element, name_, mapping_)
        if self.site is not None:
            site_ = self.site
            site_.to_etree(element, name_='site', mapping_=mapping_)
        if self.identifier is not None:
            identifier_ = self.identifier
            identifier_.to_etree(element, name_='identifier', mapping_=mapping_)
        for type__ in self.type_:
            type__.to_etree(element, name_='type', mapping_=mapping_)
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
        super(SecurityEvent_Source, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'site':
            obj_ = string.factory()
            obj_.build(child_)
            self.site = obj_
            obj_.original_tagname_ = 'site'
        elif nodeName_ == 'identifier':
            obj_ = string.factory()
            obj_.build(child_)
            self.identifier = obj_
            obj_.original_tagname_ = 'identifier'
        elif nodeName_ == 'type':
            obj_ = Coding.factory()
            obj_.build(child_)
            self.type_.append(obj_)
            obj_.original_tagname_ = 'type'
        super(SecurityEvent_Source, self).buildChildren(child_, node, nodeName_, True)
# end class SecurityEvent_Source


class SecurityEvent_Object(BackboneElement):
    """A record of an event made for purposes of maintaining a security
    log. Typical uses include detection of intrusion attempts and
    monitoring for inappropriate usage."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, identifier=None, reference=None, type_=None, role=None, lifecycle=None, sensitivity=None, name=None, description=None, query=None, detail=None):
        self.original_tagname_ = None
        super(SecurityEvent_Object, self).__init__(id, extension, modifierExtension, )
        self.identifier = identifier
        self.reference = reference
        self.type_ = type_
        self.role = role
        self.lifecycle = lifecycle
        self.sensitivity = sensitivity
        self.name = name
        self.description = description
        self.query = query
        if detail is None:
            self.detail = []
        else:
            self.detail = detail
    def factory(*args_, **kwargs_):
        if SecurityEvent_Object.subclass:
            return SecurityEvent_Object.subclass(*args_, **kwargs_)
        else:
            return SecurityEvent_Object(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_identifier(self): return self.identifier
    def set_identifier(self, identifier): self.identifier = identifier
    def get_reference(self): return self.reference
    def set_reference(self, reference): self.reference = reference
    def get_type(self): return self.type_
    def set_type(self, type_): self.type_ = type_
    def get_role(self): return self.role
    def set_role(self, role): self.role = role
    def get_lifecycle(self): return self.lifecycle
    def set_lifecycle(self, lifecycle): self.lifecycle = lifecycle
    def get_sensitivity(self): return self.sensitivity
    def set_sensitivity(self, sensitivity): self.sensitivity = sensitivity
    def get_name(self): return self.name
    def set_name(self, name): self.name = name
    def get_description(self): return self.description
    def set_description(self, description): self.description = description
    def get_query(self): return self.query
    def set_query(self, query): self.query = query
    def get_detail(self): return self.detail
    def set_detail(self, detail): self.detail = detail
    def add_detail(self, value): self.detail.append(value)
    def insert_detail(self, index, value): self.detail[index] = value
    def hasContent_(self):
        if (
            self.identifier is not None or
            self.reference is not None or
            self.type_ is not None or
            self.role is not None or
            self.lifecycle is not None or
            self.sensitivity is not None or
            self.name is not None or
            self.description is not None or
            self.query is not None or
            self.detail or
            super(SecurityEvent_Object, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='SecurityEvent.Object', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='SecurityEvent.Object')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='SecurityEvent.Object', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='SecurityEvent.Object'):
        super(SecurityEvent_Object, self).exportAttributes(outfile, level, already_processed, namespace_, name_='SecurityEvent.Object')
    def exportChildren(self, outfile, level, namespace_='', name_='SecurityEvent.Object', fromsubclass_=False, pretty_print=True):
        super(SecurityEvent_Object, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.identifier is not None:
            self.identifier.export(outfile, level, namespace_, name_='identifier', pretty_print=pretty_print)
        if self.reference is not None:
            self.reference.export(outfile, level, namespace_, name_='reference', pretty_print=pretty_print)
        if self.type_ is not None:
            self.type_.export(outfile, level, namespace_, name_='type', pretty_print=pretty_print)
        if self.role is not None:
            self.role.export(outfile, level, namespace_, name_='role', pretty_print=pretty_print)
        if self.lifecycle is not None:
            self.lifecycle.export(outfile, level, namespace_, name_='lifecycle', pretty_print=pretty_print)
        if self.sensitivity is not None:
            self.sensitivity.export(outfile, level, namespace_, name_='sensitivity', pretty_print=pretty_print)
        if self.name is not None:
            self.name.export(outfile, level, namespace_, name_='name', pretty_print=pretty_print)
        if self.description is not None:
            self.description.export(outfile, level, namespace_, name_='description', pretty_print=pretty_print)
        if self.query is not None:
            self.query.export(outfile, level, namespace_, name_='query', pretty_print=pretty_print)
        for detail_ in self.detail:
            detail_.export(outfile, level, namespace_, name_='detail', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='SecurityEvent.Object', mapping_=None):
        element = super(SecurityEvent_Object, self).to_etree(parent_element, name_, mapping_)
        if self.identifier is not None:
            identifier_ = self.identifier
            identifier_.to_etree(element, name_='identifier', mapping_=mapping_)
        if self.reference is not None:
            reference_ = self.reference
            reference_.to_etree(element, name_='reference', mapping_=mapping_)
        if self.type_ is not None:
            type__ = self.type_
            type__.to_etree(element, name_='type', mapping_=mapping_)
        if self.role is not None:
            role_ = self.role
            role_.to_etree(element, name_='role', mapping_=mapping_)
        if self.lifecycle is not None:
            lifecycle_ = self.lifecycle
            lifecycle_.to_etree(element, name_='lifecycle', mapping_=mapping_)
        if self.sensitivity is not None:
            sensitivity_ = self.sensitivity
            sensitivity_.to_etree(element, name_='sensitivity', mapping_=mapping_)
        if self.name is not None:
            name_ = self.name
            name_.to_etree(element, name_='name', mapping_=mapping_)
        if self.description is not None:
            description_ = self.description
            description_.to_etree(element, name_='description', mapping_=mapping_)
        if self.query is not None:
            query_ = self.query
            query_.to_etree(element, name_='query', mapping_=mapping_)
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
        super(SecurityEvent_Object, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'identifier':
            obj_ = Identifier.factory()
            obj_.build(child_)
            self.identifier = obj_
            obj_.original_tagname_ = 'identifier'
        elif nodeName_ == 'reference':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.reference = obj_
            obj_.original_tagname_ = 'reference'
        elif nodeName_ == 'type':
            obj_ = SecurityEventObjectType.factory()
            obj_.build(child_)
            self.type_ = obj_
            obj_.original_tagname_ = 'type'
        elif nodeName_ == 'role':
            obj_ = SecurityEventObjectRole.factory()
            obj_.build(child_)
            self.role = obj_
            obj_.original_tagname_ = 'role'
        elif nodeName_ == 'lifecycle':
            obj_ = SecurityEventObjectLifecycle.factory()
            obj_.build(child_)
            self.lifecycle = obj_
            obj_.original_tagname_ = 'lifecycle'
        elif nodeName_ == 'sensitivity':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.sensitivity = obj_
            obj_.original_tagname_ = 'sensitivity'
        elif nodeName_ == 'name':
            obj_ = string.factory()
            obj_.build(child_)
            self.name = obj_
            obj_.original_tagname_ = 'name'
        elif nodeName_ == 'description':
            obj_ = string.factory()
            obj_.build(child_)
            self.description = obj_
            obj_.original_tagname_ = 'description'
        elif nodeName_ == 'query':
            obj_ = base64Binary.factory()
            obj_.build(child_)
            self.query = obj_
            obj_.original_tagname_ = 'query'
        elif nodeName_ == 'detail':
            obj_ = SecurityEvent_Detail.factory()
            obj_.build(child_)
            self.detail.append(obj_)
            obj_.original_tagname_ = 'detail'
        super(SecurityEvent_Object, self).buildChildren(child_, node, nodeName_, True)
# end class SecurityEvent_Object


class SecurityEvent_Detail(BackboneElement):
    """A record of an event made for purposes of maintaining a security
    log. Typical uses include detection of intrusion attempts and
    monitoring for inappropriate usage."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, type_=None, value=None):
        self.original_tagname_ = None
        super(SecurityEvent_Detail, self).__init__(id, extension, modifierExtension, )
        self.type_ = type_
        self.value = value
    def factory(*args_, **kwargs_):
        if SecurityEvent_Detail.subclass:
            return SecurityEvent_Detail.subclass(*args_, **kwargs_)
        else:
            return SecurityEvent_Detail(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_type(self): return self.type_
    def set_type(self, type_): self.type_ = type_
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            self.type_ is not None or
            self.value is not None or
            super(SecurityEvent_Detail, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='SecurityEvent.Detail', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='SecurityEvent.Detail')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='SecurityEvent.Detail', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='SecurityEvent.Detail'):
        super(SecurityEvent_Detail, self).exportAttributes(outfile, level, already_processed, namespace_, name_='SecurityEvent.Detail')
    def exportChildren(self, outfile, level, namespace_='', name_='SecurityEvent.Detail', fromsubclass_=False, pretty_print=True):
        super(SecurityEvent_Detail, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.type_ is not None:
            self.type_.export(outfile, level, namespace_, name_='type', pretty_print=pretty_print)
        if self.value is not None:
            self.value.export(outfile, level, namespace_, name_='value', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='SecurityEvent.Detail', mapping_=None):
        element = super(SecurityEvent_Detail, self).to_etree(parent_element, name_, mapping_)
        if self.type_ is not None:
            type__ = self.type_
            type__.to_etree(element, name_='type', mapping_=mapping_)
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
        super(SecurityEvent_Detail, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'type':
            obj_ = string.factory()
            obj_.build(child_)
            self.type_ = obj_
            obj_.original_tagname_ = 'type'
        elif nodeName_ == 'value':
            obj_ = base64Binary.factory()
            obj_.build(child_)
            self.value = obj_
            obj_.original_tagname_ = 'value'
        super(SecurityEvent_Detail, self).buildChildren(child_, node, nodeName_, True)
# end class SecurityEvent_Detail


class SecurityEventObjectRole(Element):
    """Code representing the functional application role of Participant
    Object being auditedIf the element is present, it must have
    either a @value, an @id, or extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(SecurityEventObjectRole, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if SecurityEventObjectRole.subclass:
            return SecurityEventObjectRole.subclass(*args_, **kwargs_)
        else:
            return SecurityEventObjectRole(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(SecurityEventObjectRole, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='SecurityEventObjectRole', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='SecurityEventObjectRole')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='SecurityEventObjectRole', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='SecurityEventObjectRole'):
        super(SecurityEventObjectRole, self).exportAttributes(outfile, level, already_processed, namespace_, name_='SecurityEventObjectRole')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='SecurityEventObjectRole', fromsubclass_=False, pretty_print=True):
        super(SecurityEventObjectRole, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='SecurityEventObjectRole', mapping_=None):
        element = super(SecurityEventObjectRole, self).to_etree(parent_element, name_, mapping_)
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
        super(SecurityEventObjectRole, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(SecurityEventObjectRole, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class SecurityEventObjectRole


class SecurityEventObjectType(Element):
    """Code for the participant object type being auditedIf the element is
    present, it must have either a @value, an @id, or extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(SecurityEventObjectType, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if SecurityEventObjectType.subclass:
            return SecurityEventObjectType.subclass(*args_, **kwargs_)
        else:
            return SecurityEventObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(SecurityEventObjectType, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='SecurityEventObjectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='SecurityEventObjectType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='SecurityEventObjectType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='SecurityEventObjectType'):
        super(SecurityEventObjectType, self).exportAttributes(outfile, level, already_processed, namespace_, name_='SecurityEventObjectType')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='SecurityEventObjectType', fromsubclass_=False, pretty_print=True):
        super(SecurityEventObjectType, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='SecurityEventObjectType', mapping_=None):
        element = super(SecurityEventObjectType, self).to_etree(parent_element, name_, mapping_)
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
        super(SecurityEventObjectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(SecurityEventObjectType, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class SecurityEventObjectType


class SecurityEventAction(Element):
    """Indicator for type of action performed during the event that
    generated the audit.If the element is present, it must have
    either a @value, an @id, or extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(SecurityEventAction, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if SecurityEventAction.subclass:
            return SecurityEventAction.subclass(*args_, **kwargs_)
        else:
            return SecurityEventAction(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(SecurityEventAction, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='SecurityEventAction', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='SecurityEventAction')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='SecurityEventAction', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='SecurityEventAction'):
        super(SecurityEventAction, self).exportAttributes(outfile, level, already_processed, namespace_, name_='SecurityEventAction')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='SecurityEventAction', fromsubclass_=False, pretty_print=True):
        super(SecurityEventAction, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='SecurityEventAction', mapping_=None):
        element = super(SecurityEventAction, self).to_etree(parent_element, name_, mapping_)
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
        super(SecurityEventAction, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(SecurityEventAction, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class SecurityEventAction


class SecurityEventObjectLifecycle(Element):
    """Identifier for the data life-cycle stage for the participant
    objectIf the element is present, it must have either a @value,
    an @id, or extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(SecurityEventObjectLifecycle, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if SecurityEventObjectLifecycle.subclass:
            return SecurityEventObjectLifecycle.subclass(*args_, **kwargs_)
        else:
            return SecurityEventObjectLifecycle(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(SecurityEventObjectLifecycle, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='SecurityEventObjectLifecycle', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='SecurityEventObjectLifecycle')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='SecurityEventObjectLifecycle', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='SecurityEventObjectLifecycle'):
        super(SecurityEventObjectLifecycle, self).exportAttributes(outfile, level, already_processed, namespace_, name_='SecurityEventObjectLifecycle')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='SecurityEventObjectLifecycle', fromsubclass_=False, pretty_print=True):
        super(SecurityEventObjectLifecycle, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='SecurityEventObjectLifecycle', mapping_=None):
        element = super(SecurityEventObjectLifecycle, self).to_etree(parent_element, name_, mapping_)
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
        super(SecurityEventObjectLifecycle, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(SecurityEventObjectLifecycle, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class SecurityEventObjectLifecycle


class SecurityEventParticipantNetworkType(Element):
    """The type of network access point that originated the audit eventIf
    the element is present, it must have either a @value, an @id, or
    extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(SecurityEventParticipantNetworkType, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if SecurityEventParticipantNetworkType.subclass:
            return SecurityEventParticipantNetworkType.subclass(*args_, **kwargs_)
        else:
            return SecurityEventParticipantNetworkType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(SecurityEventParticipantNetworkType, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='SecurityEventParticipantNetworkType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='SecurityEventParticipantNetworkType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='SecurityEventParticipantNetworkType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='SecurityEventParticipantNetworkType'):
        super(SecurityEventParticipantNetworkType, self).exportAttributes(outfile, level, already_processed, namespace_, name_='SecurityEventParticipantNetworkType')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='SecurityEventParticipantNetworkType', fromsubclass_=False, pretty_print=True):
        super(SecurityEventParticipantNetworkType, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='SecurityEventParticipantNetworkType', mapping_=None):
        element = super(SecurityEventParticipantNetworkType, self).to_etree(parent_element, name_, mapping_)
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
        super(SecurityEventParticipantNetworkType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(SecurityEventParticipantNetworkType, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class SecurityEventParticipantNetworkType


class SecurityEventOutcome(Element):
    """Indicates whether the event succeeded or failedIf the element is
    present, it must have either a @value, an @id, or extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(SecurityEventOutcome, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if SecurityEventOutcome.subclass:
            return SecurityEventOutcome.subclass(*args_, **kwargs_)
        else:
            return SecurityEventOutcome(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(SecurityEventOutcome, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='SecurityEventOutcome', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='SecurityEventOutcome')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='SecurityEventOutcome', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='SecurityEventOutcome'):
        super(SecurityEventOutcome, self).exportAttributes(outfile, level, already_processed, namespace_, name_='SecurityEventOutcome')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='SecurityEventOutcome', fromsubclass_=False, pretty_print=True):
        super(SecurityEventOutcome, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='SecurityEventOutcome', mapping_=None):
        element = super(SecurityEventOutcome, self).to_etree(parent_element, name_, mapping_)
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
        super(SecurityEventOutcome, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(SecurityEventOutcome, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class SecurityEventOutcome
