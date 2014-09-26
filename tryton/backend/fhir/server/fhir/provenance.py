from .base_classes import *
from .support_functions import *


class Provenance(Resource):
    """Provenance information that describes the activity that led to the
    creation of a set of resources. This information can be used to
    help determine their reliability or trace where the information
    in them came from. The focus of the provenance resource is
    record keeping, audit and traceability, and not explicit
    statements of clinical significance.If the element is present,
    it must have either a @value, an @id, or extensions"""
    subclass = None
    superclass = Resource
    def __init__(self, id=None, extension=None, modifierExtension=None, language=None, text=None, contained=None, target=None, period=None, recorded=None, reason=None, location=None, policy=None, agent=None, entity=None, integritySignature=None):
        self.original_tagname_ = None
        super(Provenance, self).__init__(id, extension, modifierExtension, language, text, contained, )
        if target is None:
            self.target = []
        else:
            self.target = target
        self.period = period
        self.recorded = recorded
        self.reason = reason
        self.location = location
        if policy is None:
            self.policy = []
        else:
            self.policy = policy
        if agent is None:
            self.agent = []
        else:
            self.agent = agent
        if entity is None:
            self.entity = []
        else:
            self.entity = entity
        self.integritySignature = integritySignature
    def factory(*args_, **kwargs_):
        if Provenance.subclass:
            return Provenance.subclass(*args_, **kwargs_)
        else:
            return Provenance(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_target(self): return self.target
    def set_target(self, target): self.target = target
    def add_target(self, value): self.target.append(value)
    def insert_target(self, index, value): self.target[index] = value
    def get_period(self): return self.period
    def set_period(self, period): self.period = period
    def get_recorded(self): return self.recorded
    def set_recorded(self, recorded): self.recorded = recorded
    def get_reason(self): return self.reason
    def set_reason(self, reason): self.reason = reason
    def get_location(self): return self.location
    def set_location(self, location): self.location = location
    def get_policy(self): return self.policy
    def set_policy(self, policy): self.policy = policy
    def add_policy(self, value): self.policy.append(value)
    def insert_policy(self, index, value): self.policy[index] = value
    def get_agent(self): return self.agent
    def set_agent(self, agent): self.agent = agent
    def add_agent(self, value): self.agent.append(value)
    def insert_agent(self, index, value): self.agent[index] = value
    def get_entity(self): return self.entity
    def set_entity(self, entity): self.entity = entity
    def add_entity(self, value): self.entity.append(value)
    def insert_entity(self, index, value): self.entity[index] = value
    def get_integritySignature(self): return self.integritySignature
    def set_integritySignature(self, integritySignature): self.integritySignature = integritySignature
    def hasContent_(self):
        if (
            self.target or
            self.period is not None or
            self.recorded is not None or
            self.reason is not None or
            self.location is not None or
            self.policy or
            self.agent or
            self.entity or
            self.integritySignature is not None or
            super(Provenance, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Provenance', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Provenance')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Provenance', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Provenance'):
        super(Provenance, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Provenance')
    def exportChildren(self, outfile, level, namespace_='', name_='Provenance', fromsubclass_=False, pretty_print=True):
        super(Provenance, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for target_ in self.target:
            target_.export(outfile, level, namespace_, name_='target', pretty_print=pretty_print)
        if self.period is not None:
            self.period.export(outfile, level, namespace_, name_='period', pretty_print=pretty_print)
        if self.recorded is not None:
            self.recorded.export(outfile, level, namespace_, name_='recorded', pretty_print=pretty_print)
        if self.reason is not None:
            self.reason.export(outfile, level, namespace_, name_='reason', pretty_print=pretty_print)
        if self.location is not None:
            self.location.export(outfile, level, namespace_, name_='location', pretty_print=pretty_print)
        for policy_ in self.policy:
            policy_.export(outfile, level, namespace_, name_='policy', pretty_print=pretty_print)
        for agent_ in self.agent:
            agent_.export(outfile, level, namespace_, name_='agent', pretty_print=pretty_print)
        for entity_ in self.entity:
            entity_.export(outfile, level, namespace_, name_='entity', pretty_print=pretty_print)
        if self.integritySignature is not None:
            self.integritySignature.export(outfile, level, namespace_, name_='integritySignature', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Provenance', mapping_=None):
        element = super(Provenance, self).to_etree(parent_element, name_, mapping_)
        for target_ in self.target:
            target_.to_etree(element, name_='target', mapping_=mapping_)
        if self.period is not None:
            period_ = self.period
            period_.to_etree(element, name_='period', mapping_=mapping_)
        if self.recorded is not None:
            recorded_ = self.recorded
            recorded_.to_etree(element, name_='recorded', mapping_=mapping_)
        if self.reason is not None:
            reason_ = self.reason
            reason_.to_etree(element, name_='reason', mapping_=mapping_)
        if self.location is not None:
            location_ = self.location
            location_.to_etree(element, name_='location', mapping_=mapping_)
        for policy_ in self.policy:
            policy_.to_etree(element, name_='policy', mapping_=mapping_)
        for agent_ in self.agent:
            agent_.to_etree(element, name_='agent', mapping_=mapping_)
        for entity_ in self.entity:
            entity_.to_etree(element, name_='entity', mapping_=mapping_)
        if self.integritySignature is not None:
            integritySignature_ = self.integritySignature
            integritySignature_.to_etree(element, name_='integritySignature', mapping_=mapping_)
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
        super(Provenance, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'target':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.target.append(obj_)
            obj_.original_tagname_ = 'target'
        elif nodeName_ == 'period':
            obj_ = Period.factory()
            obj_.build(child_)
            self.period = obj_
            obj_.original_tagname_ = 'period'
        elif nodeName_ == 'recorded':
            obj_ = instant.factory()
            obj_.build(child_)
            self.recorded = obj_
            obj_.original_tagname_ = 'recorded'
        elif nodeName_ == 'reason':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.reason = obj_
            obj_.original_tagname_ = 'reason'
        elif nodeName_ == 'location':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.location = obj_
            obj_.original_tagname_ = 'location'
        elif nodeName_ == 'policy':
            obj_ = uri.factory()
            obj_.build(child_)
            self.policy.append(obj_)
            obj_.original_tagname_ = 'policy'
        elif nodeName_ == 'agent':
            obj_ = Provenance_Agent.factory()
            obj_.build(child_)
            self.agent.append(obj_)
            obj_.original_tagname_ = 'agent'
        elif nodeName_ == 'entity':
            obj_ = Provenance_Entity.factory()
            obj_.build(child_)
            self.entity.append(obj_)
            obj_.original_tagname_ = 'entity'
        elif nodeName_ == 'integritySignature':
            obj_ = string.factory()
            obj_.build(child_)
            self.integritySignature = obj_
            obj_.original_tagname_ = 'integritySignature'
        super(Provenance, self).buildChildren(child_, node, nodeName_, True)
# end class Provenance


class Provenance_Agent(BackboneElement):
    """Provenance information that describes the activity that led to the
    creation of a set of resources. This information can be used to
    help determine their reliability or trace where the information
    in them came from. The focus of the provenance resource is
    record keeping, audit and traceability, and not explicit
    statements of clinical significance."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, role=None, type_=None, reference=None, display=None):
        self.original_tagname_ = None
        super(Provenance_Agent, self).__init__(id, extension, modifierExtension, )
        self.role = role
        self.type_ = type_
        self.reference = reference
        self.display = display
    def factory(*args_, **kwargs_):
        if Provenance_Agent.subclass:
            return Provenance_Agent.subclass(*args_, **kwargs_)
        else:
            return Provenance_Agent(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_role(self): return self.role
    def set_role(self, role): self.role = role
    def get_type(self): return self.type_
    def set_type(self, type_): self.type_ = type_
    def get_reference(self): return self.reference
    def set_reference(self, reference): self.reference = reference
    def get_display(self): return self.display
    def set_display(self, display): self.display = display
    def hasContent_(self):
        if (
            self.role is not None or
            self.type_ is not None or
            self.reference is not None or
            self.display is not None or
            super(Provenance_Agent, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Provenance.Agent', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Provenance.Agent')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Provenance.Agent', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Provenance.Agent'):
        super(Provenance_Agent, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Provenance.Agent')
    def exportChildren(self, outfile, level, namespace_='', name_='Provenance.Agent', fromsubclass_=False, pretty_print=True):
        super(Provenance_Agent, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.role is not None:
            self.role.export(outfile, level, namespace_, name_='role', pretty_print=pretty_print)
        if self.type_ is not None:
            self.type_.export(outfile, level, namespace_, name_='type', pretty_print=pretty_print)
        if self.reference is not None:
            self.reference.export(outfile, level, namespace_, name_='reference', pretty_print=pretty_print)
        if self.display is not None:
            self.display.export(outfile, level, namespace_, name_='display', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Provenance.Agent', mapping_=None):
        element = super(Provenance_Agent, self).to_etree(parent_element, name_, mapping_)
        if self.role is not None:
            role_ = self.role
            role_.to_etree(element, name_='role', mapping_=mapping_)
        if self.type_ is not None:
            type__ = self.type_
            type__.to_etree(element, name_='type', mapping_=mapping_)
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
        super(Provenance_Agent, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'role':
            obj_ = Coding.factory()
            obj_.build(child_)
            self.role = obj_
            obj_.original_tagname_ = 'role'
        elif nodeName_ == 'type':
            obj_ = Coding.factory()
            obj_.build(child_)
            self.type_ = obj_
            obj_.original_tagname_ = 'type'
        elif nodeName_ == 'reference':
            obj_ = uri.factory()
            obj_.build(child_)
            self.reference = obj_
            obj_.original_tagname_ = 'reference'
        elif nodeName_ == 'display':
            obj_ = string.factory()
            obj_.build(child_)
            self.display = obj_
            obj_.original_tagname_ = 'display'
        super(Provenance_Agent, self).buildChildren(child_, node, nodeName_, True)
# end class Provenance_Agent


class Provenance_Entity(BackboneElement):
    """Provenance information that describes the activity that led to the
    creation of a set of resources. This information can be used to
    help determine their reliability or trace where the information
    in them came from. The focus of the provenance resource is
    record keeping, audit and traceability, and not explicit
    statements of clinical significance."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, role=None, type_=None, reference=None, display=None, agent=None):
        self.original_tagname_ = None
        super(Provenance_Entity, self).__init__(id, extension, modifierExtension, )
        self.role = role
        self.type_ = type_
        self.reference = reference
        self.display = display
        self.agent = agent
    def factory(*args_, **kwargs_):
        if Provenance_Entity.subclass:
            return Provenance_Entity.subclass(*args_, **kwargs_)
        else:
            return Provenance_Entity(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_role(self): return self.role
    def set_role(self, role): self.role = role
    def get_type(self): return self.type_
    def set_type(self, type_): self.type_ = type_
    def get_reference(self): return self.reference
    def set_reference(self, reference): self.reference = reference
    def get_display(self): return self.display
    def set_display(self, display): self.display = display
    def get_agent(self): return self.agent
    def set_agent(self, agent): self.agent = agent
    def hasContent_(self):
        if (
            self.role is not None or
            self.type_ is not None or
            self.reference is not None or
            self.display is not None or
            self.agent is not None or
            super(Provenance_Entity, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Provenance.Entity', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Provenance.Entity')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Provenance.Entity', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Provenance.Entity'):
        super(Provenance_Entity, self).exportAttributes(outfile, level, already_processed, namespace_, name_='Provenance.Entity')
    def exportChildren(self, outfile, level, namespace_='', name_='Provenance.Entity', fromsubclass_=False, pretty_print=True):
        super(Provenance_Entity, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.role is not None:
            self.role.export(outfile, level, namespace_, name_='role', pretty_print=pretty_print)
        if self.type_ is not None:
            self.type_.export(outfile, level, namespace_, name_='type', pretty_print=pretty_print)
        if self.reference is not None:
            self.reference.export(outfile, level, namespace_, name_='reference', pretty_print=pretty_print)
        if self.display is not None:
            self.display.export(outfile, level, namespace_, name_='display', pretty_print=pretty_print)
        if self.agent is not None:
            self.agent.export(outfile, level, namespace_, name_='agent', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Provenance.Entity', mapping_=None):
        element = super(Provenance_Entity, self).to_etree(parent_element, name_, mapping_)
        if self.role is not None:
            role_ = self.role
            role_.to_etree(element, name_='role', mapping_=mapping_)
        if self.type_ is not None:
            type__ = self.type_
            type__.to_etree(element, name_='type', mapping_=mapping_)
        if self.reference is not None:
            reference_ = self.reference
            reference_.to_etree(element, name_='reference', mapping_=mapping_)
        if self.display is not None:
            display_ = self.display
            display_.to_etree(element, name_='display', mapping_=mapping_)
        if self.agent is not None:
            agent_ = self.agent
            agent_.to_etree(element, name_='agent', mapping_=mapping_)
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
        super(Provenance_Entity, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'role':
            obj_ = ProvenanceEntityRole.factory()
            obj_.build(child_)
            self.role = obj_
            obj_.original_tagname_ = 'role'
        elif nodeName_ == 'type':
            obj_ = Coding.factory()
            obj_.build(child_)
            self.type_ = obj_
            obj_.original_tagname_ = 'type'
        elif nodeName_ == 'reference':
            obj_ = uri.factory()
            obj_.build(child_)
            self.reference = obj_
            obj_.original_tagname_ = 'reference'
        elif nodeName_ == 'display':
            obj_ = string.factory()
            obj_.build(child_)
            self.display = obj_
            obj_.original_tagname_ = 'display'
        elif nodeName_ == 'agent':
            obj_ = Provenance_Agent.factory()
            obj_.build(child_)
            self.agent = obj_
            obj_.original_tagname_ = 'agent'
        super(Provenance_Entity, self).buildChildren(child_, node, nodeName_, True)
# end class Provenance_Entity


class ProvenanceEntityRole(Element):
    """How an entity was used in an activityIf the element is present, it
    must have either a @value, an @id, or extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(ProvenanceEntityRole, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if ProvenanceEntityRole.subclass:
            return ProvenanceEntityRole.subclass(*args_, **kwargs_)
        else:
            return ProvenanceEntityRole(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(ProvenanceEntityRole, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='ProvenanceEntityRole', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ProvenanceEntityRole')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='ProvenanceEntityRole', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='ProvenanceEntityRole'):
        super(ProvenanceEntityRole, self).exportAttributes(outfile, level, already_processed, namespace_, name_='ProvenanceEntityRole')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='ProvenanceEntityRole', fromsubclass_=False, pretty_print=True):
        super(ProvenanceEntityRole, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='ProvenanceEntityRole', mapping_=None):
        element = super(ProvenanceEntityRole, self).to_etree(parent_element, name_, mapping_)
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
        super(ProvenanceEntityRole, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(ProvenanceEntityRole, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class ProvenanceEntityRole
