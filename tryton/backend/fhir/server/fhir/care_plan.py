from .base_classes import *
from .support_functions import *


class CarePlan(Resource):
    """Describes the intention of how one or more practitioners intend to
    deliver care for a particular patient for a period of time,
    possibly limited to care for a specific condition or set of
    conditions.If the element is present, it must have either a
    @value, an @id, or extensions"""
    subclass = None
    superclass = Resource
    def __init__(self, id=None, extension=None, modifierExtension=None, language=None, text=None, contained=None, identifier=None, patient=None, status=None, period=None, modified=None, concern=None, participant=None, goal=None, activity=None, notes=None):
        self.original_tagname_ = None
        super(CarePlan, self).__init__(id, extension, modifierExtension, language, text, contained, )
        if identifier is None:
            self.identifier = []
        else:
            self.identifier = identifier
        self.patient = patient
        self.status = status
        self.period = period
        self.modified = modified
        if concern is None:
            self.concern = []
        else:
            self.concern = concern
        if participant is None:
            self.participant = []
        else:
            self.participant = participant
        if goal is None:
            self.goal = []
        else:
            self.goal = goal
        if activity is None:
            self.activity = []
        else:
            self.activity = activity
        self.notes = notes
    def factory(*args_, **kwargs_):
        if CarePlan.subclass:
            return CarePlan.subclass(*args_, **kwargs_)
        else:
            return CarePlan(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_identifier(self): return self.identifier
    def set_identifier(self, identifier): self.identifier = identifier
    def add_identifier(self, value): self.identifier.append(value)
    def insert_identifier(self, index, value): self.identifier[index] = value
    def get_patient(self): return self.patient
    def set_patient(self, patient): self.patient = patient
    def get_status(self): return self.status
    def set_status(self, status): self.status = status
    def get_period(self): return self.period
    def set_period(self, period): self.period = period
    def get_modified(self): return self.modified
    def set_modified(self, modified): self.modified = modified
    def get_concern(self): return self.concern
    def set_concern(self, concern): self.concern = concern
    def add_concern(self, value): self.concern.append(value)
    def insert_concern(self, index, value): self.concern[index] = value
    def get_participant(self): return self.participant
    def set_participant(self, participant): self.participant = participant
    def add_participant(self, value): self.participant.append(value)
    def insert_participant(self, index, value): self.participant[index] = value
    def get_goal(self): return self.goal
    def set_goal(self, goal): self.goal = goal
    def add_goal(self, value): self.goal.append(value)
    def insert_goal(self, index, value): self.goal[index] = value
    def get_activity(self): return self.activity
    def set_activity(self, activity): self.activity = activity
    def add_activity(self, value): self.activity.append(value)
    def insert_activity(self, index, value): self.activity[index] = value
    def get_notes(self): return self.notes
    def set_notes(self, notes): self.notes = notes
    def hasContent_(self):
        if (
            self.identifier or
            self.patient is not None or
            self.status is not None or
            self.period is not None or
            self.modified is not None or
            self.concern or
            self.participant or
            self.goal or
            self.activity or
            self.notes is not None or
            super(CarePlan, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='CarePlan', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='CarePlan')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='CarePlan', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='CarePlan'):
        super(CarePlan, self).exportAttributes(outfile, level, already_processed, namespace_, name_='CarePlan')
    def exportChildren(self, outfile, level, namespace_='', name_='CarePlan', fromsubclass_=False, pretty_print=True):
        super(CarePlan, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for identifier_ in self.identifier:
            identifier_.export(outfile, level, namespace_, name_='identifier', pretty_print=pretty_print)
        if self.patient is not None:
            self.patient.export(outfile, level, namespace_, name_='patient', pretty_print=pretty_print)
        if self.status is not None:
            self.status.export(outfile, level, namespace_, name_='status', pretty_print=pretty_print)
        if self.period is not None:
            self.period.export(outfile, level, namespace_, name_='period', pretty_print=pretty_print)
        if self.modified is not None:
            self.modified.export(outfile, level, namespace_, name_='modified', pretty_print=pretty_print)
        for concern_ in self.concern:
            concern_.export(outfile, level, namespace_, name_='concern', pretty_print=pretty_print)
        for participant_ in self.participant:
            participant_.export(outfile, level, namespace_, name_='participant', pretty_print=pretty_print)
        for goal_ in self.goal:
            goal_.export(outfile, level, namespace_, name_='goal', pretty_print=pretty_print)
        for activity_ in self.activity:
            activity_.export(outfile, level, namespace_, name_='activity', pretty_print=pretty_print)
        if self.notes is not None:
            self.notes.export(outfile, level, namespace_, name_='notes', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='CarePlan', mapping_=None):
        element = super(CarePlan, self).to_etree(parent_element, name_, mapping_)
        for identifier_ in self.identifier:
            identifier_.to_etree(element, name_='identifier', mapping_=mapping_)
        if self.patient is not None:
            patient_ = self.patient
            patient_.to_etree(element, name_='patient', mapping_=mapping_)
        if self.status is not None:
            status_ = self.status
            status_.to_etree(element, name_='status', mapping_=mapping_)
        if self.period is not None:
            period_ = self.period
            period_.to_etree(element, name_='period', mapping_=mapping_)
        if self.modified is not None:
            modified_ = self.modified
            modified_.to_etree(element, name_='modified', mapping_=mapping_)
        for concern_ in self.concern:
            concern_.to_etree(element, name_='concern', mapping_=mapping_)
        for participant_ in self.participant:
            participant_.to_etree(element, name_='participant', mapping_=mapping_)
        for goal_ in self.goal:
            goal_.to_etree(element, name_='goal', mapping_=mapping_)
        for activity_ in self.activity:
            activity_.to_etree(element, name_='activity', mapping_=mapping_)
        if self.notes is not None:
            notes_ = self.notes
            notes_.to_etree(element, name_='notes', mapping_=mapping_)
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
        super(CarePlan, self).buildAttributes(node, attrs, already_processed)
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
        elif nodeName_ == 'status':
            obj_ = CarePlanStatus.factory()
            obj_.build(child_)
            self.status = obj_
            obj_.original_tagname_ = 'status'
        elif nodeName_ == 'period':
            obj_ = Period.factory()
            obj_.build(child_)
            self.period = obj_
            obj_.original_tagname_ = 'period'
        elif nodeName_ == 'modified':
            obj_ = dateTime.factory()
            obj_.build(child_)
            self.modified = obj_
            obj_.original_tagname_ = 'modified'
        elif nodeName_ == 'concern':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.concern.append(obj_)
            obj_.original_tagname_ = 'concern'
        elif nodeName_ == 'participant':
            obj_ = CarePlan_Participant.factory()
            obj_.build(child_)
            self.participant.append(obj_)
            obj_.original_tagname_ = 'participant'
        elif nodeName_ == 'goal':
            obj_ = CarePlan_Goal.factory()
            obj_.build(child_)
            self.goal.append(obj_)
            obj_.original_tagname_ = 'goal'
        elif nodeName_ == 'activity':
            obj_ = CarePlan_Activity.factory()
            obj_.build(child_)
            self.activity.append(obj_)
            obj_.original_tagname_ = 'activity'
        elif nodeName_ == 'notes':
            obj_ = string.factory()
            obj_.build(child_)
            self.notes = obj_
            obj_.original_tagname_ = 'notes'
        super(CarePlan, self).buildChildren(child_, node, nodeName_, True)
# end class CarePlan


class CarePlan_Participant(BackboneElement):
    """Describes the intention of how one or more practitioners intend to
    deliver care for a particular patient for a period of time,
    possibly limited to care for a specific condition or set of
    conditions."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, role=None, member=None):
        self.original_tagname_ = None
        super(CarePlan_Participant, self).__init__(id, extension, modifierExtension, )
        self.role = role
        self.member = member
    def factory(*args_, **kwargs_):
        if CarePlan_Participant.subclass:
            return CarePlan_Participant.subclass(*args_, **kwargs_)
        else:
            return CarePlan_Participant(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_role(self): return self.role
    def set_role(self, role): self.role = role
    def get_member(self): return self.member
    def set_member(self, member): self.member = member
    def hasContent_(self):
        if (
            self.role is not None or
            self.member is not None or
            super(CarePlan_Participant, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='CarePlan.Participant', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='CarePlan.Participant')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='CarePlan.Participant', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='CarePlan.Participant'):
        super(CarePlan_Participant, self).exportAttributes(outfile, level, already_processed, namespace_, name_='CarePlan.Participant')
    def exportChildren(self, outfile, level, namespace_='', name_='CarePlan.Participant', fromsubclass_=False, pretty_print=True):
        super(CarePlan_Participant, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.role is not None:
            self.role.export(outfile, level, namespace_, name_='role', pretty_print=pretty_print)
        if self.member is not None:
            self.member.export(outfile, level, namespace_, name_='member', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='CarePlan.Participant', mapping_=None):
        element = super(CarePlan_Participant, self).to_etree(parent_element, name_, mapping_)
        if self.role is not None:
            role_ = self.role
            role_.to_etree(element, name_='role', mapping_=mapping_)
        if self.member is not None:
            member_ = self.member
            member_.to_etree(element, name_='member', mapping_=mapping_)
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
        super(CarePlan_Participant, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'role':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.role = obj_
            obj_.original_tagname_ = 'role'
        elif nodeName_ == 'member':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.member = obj_
            obj_.original_tagname_ = 'member'
        super(CarePlan_Participant, self).buildChildren(child_, node, nodeName_, True)
# end class CarePlan_Participant


class CarePlan_Goal(BackboneElement):
    """Describes the intention of how one or more practitioners intend to
    deliver care for a particular patient for a period of time,
    possibly limited to care for a specific condition or set of
    conditions."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, description=None, status=None, notes=None, concern=None):
        self.original_tagname_ = None
        super(CarePlan_Goal, self).__init__(id, extension, modifierExtension, )
        self.description = description
        self.status = status
        self.notes = notes
        if concern is None:
            self.concern = []
        else:
            self.concern = concern
    def factory(*args_, **kwargs_):
        if CarePlan_Goal.subclass:
            return CarePlan_Goal.subclass(*args_, **kwargs_)
        else:
            return CarePlan_Goal(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_description(self): return self.description
    def set_description(self, description): self.description = description
    def get_status(self): return self.status
    def set_status(self, status): self.status = status
    def get_notes(self): return self.notes
    def set_notes(self, notes): self.notes = notes
    def get_concern(self): return self.concern
    def set_concern(self, concern): self.concern = concern
    def add_concern(self, value): self.concern.append(value)
    def insert_concern(self, index, value): self.concern[index] = value
    def hasContent_(self):
        if (
            self.description is not None or
            self.status is not None or
            self.notes is not None or
            self.concern or
            super(CarePlan_Goal, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='CarePlan.Goal', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='CarePlan.Goal')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='CarePlan.Goal', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='CarePlan.Goal'):
        super(CarePlan_Goal, self).exportAttributes(outfile, level, already_processed, namespace_, name_='CarePlan.Goal')
    def exportChildren(self, outfile, level, namespace_='', name_='CarePlan.Goal', fromsubclass_=False, pretty_print=True):
        super(CarePlan_Goal, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.description is not None:
            self.description.export(outfile, level, namespace_, name_='description', pretty_print=pretty_print)
        if self.status is not None:
            self.status.export(outfile, level, namespace_, name_='status', pretty_print=pretty_print)
        if self.notes is not None:
            self.notes.export(outfile, level, namespace_, name_='notes', pretty_print=pretty_print)
        for concern_ in self.concern:
            concern_.export(outfile, level, namespace_, name_='concern', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='CarePlan.Goal', mapping_=None):
        element = super(CarePlan_Goal, self).to_etree(parent_element, name_, mapping_)
        if self.description is not None:
            description_ = self.description
            description_.to_etree(element, name_='description', mapping_=mapping_)
        if self.status is not None:
            status_ = self.status
            status_.to_etree(element, name_='status', mapping_=mapping_)
        if self.notes is not None:
            notes_ = self.notes
            notes_.to_etree(element, name_='notes', mapping_=mapping_)
        for concern_ in self.concern:
            concern_.to_etree(element, name_='concern', mapping_=mapping_)
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
        super(CarePlan_Goal, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'description':
            obj_ = string.factory()
            obj_.build(child_)
            self.description = obj_
            obj_.original_tagname_ = 'description'
        elif nodeName_ == 'status':
            obj_ = CarePlanGoalStatus.factory()
            obj_.build(child_)
            self.status = obj_
            obj_.original_tagname_ = 'status'
        elif nodeName_ == 'notes':
            obj_ = string.factory()
            obj_.build(child_)
            self.notes = obj_
            obj_.original_tagname_ = 'notes'
        elif nodeName_ == 'concern':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.concern.append(obj_)
            obj_.original_tagname_ = 'concern'
        super(CarePlan_Goal, self).buildChildren(child_, node, nodeName_, True)
# end class CarePlan_Goal


class CarePlan_Activity(BackboneElement):
    """Describes the intention of how one or more practitioners intend to
    deliver care for a particular patient for a period of time,
    possibly limited to care for a specific condition or set of
    conditions."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, goal=None, status=None, prohibited=None, actionResulting=None, notes=None, detail=None, simple=None):
        self.original_tagname_ = None
        super(CarePlan_Activity, self).__init__(id, extension, modifierExtension, )
        if goal is None:
            self.goal = []
        else:
            self.goal = goal
        self.status = status
        self.prohibited = prohibited
        if actionResulting is None:
            self.actionResulting = []
        else:
            self.actionResulting = actionResulting
        self.notes = notes
        self.detail = detail
        self.simple = simple
    def factory(*args_, **kwargs_):
        if CarePlan_Activity.subclass:
            return CarePlan_Activity.subclass(*args_, **kwargs_)
        else:
            return CarePlan_Activity(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_goal(self): return self.goal
    def set_goal(self, goal): self.goal = goal
    def add_goal(self, value): self.goal.append(value)
    def insert_goal(self, index, value): self.goal[index] = value
    def get_status(self): return self.status
    def set_status(self, status): self.status = status
    def get_prohibited(self): return self.prohibited
    def set_prohibited(self, prohibited): self.prohibited = prohibited
    def get_actionResulting(self): return self.actionResulting
    def set_actionResulting(self, actionResulting): self.actionResulting = actionResulting
    def add_actionResulting(self, value): self.actionResulting.append(value)
    def insert_actionResulting(self, index, value): self.actionResulting[index] = value
    def get_notes(self): return self.notes
    def set_notes(self, notes): self.notes = notes
    def get_detail(self): return self.detail
    def set_detail(self, detail): self.detail = detail
    def get_simple(self): return self.simple
    def set_simple(self, simple): self.simple = simple
    def validate_xmlIdRef(self, value):
        # Validate type xmlIdRef, a restriction on id-primitive.
        pass
    def hasContent_(self):
        if (
            self.goal or
            self.status is not None or
            self.prohibited is not None or
            self.actionResulting or
            self.notes is not None or
            self.detail is not None or
            self.simple is not None or
            super(CarePlan_Activity, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='CarePlan.Activity', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='CarePlan.Activity')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='CarePlan.Activity', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='CarePlan.Activity'):
        super(CarePlan_Activity, self).exportAttributes(outfile, level, already_processed, namespace_, name_='CarePlan.Activity')
    def exportChildren(self, outfile, level, namespace_='', name_='CarePlan.Activity', fromsubclass_=False, pretty_print=True):
        super(CarePlan_Activity, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for goal_ in self.goal:
            goal_.export(outfile, level, namespace_, name_='goal', pretty_print=pretty_print)
        if self.status is not None:
            self.status.export(outfile, level, namespace_, name_='status', pretty_print=pretty_print)
        if self.prohibited is not None:
            self.prohibited.export(outfile, level, namespace_, name_='prohibited', pretty_print=pretty_print)
        for actionResulting_ in self.actionResulting:
            actionResulting_.export(outfile, level, namespace_, name_='actionResulting', pretty_print=pretty_print)
        if self.notes is not None:
            self.notes.export(outfile, level, namespace_, name_='notes', pretty_print=pretty_print)
        if self.detail is not None:
            self.detail.export(outfile, level, namespace_, name_='detail', pretty_print=pretty_print)
        if self.simple is not None:
            self.simple.export(outfile, level, namespace_, name_='simple', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='CarePlan.Activity', mapping_=None):
        element = super(CarePlan_Activity, self).to_etree(parent_element, name_, mapping_)
        for goal_ in self.goal:
            goal_.to_etree(element, name_='goal', mapping_=mapping_)
        if self.status is not None:
            status_ = self.status
            status_.to_etree(element, name_='status', mapping_=mapping_)
        if self.prohibited is not None:
            prohibited_ = self.prohibited
            prohibited_.to_etree(element, name_='prohibited', mapping_=mapping_)
        for actionResulting_ in self.actionResulting:
            actionResulting_.to_etree(element, name_='actionResulting', mapping_=mapping_)
        if self.notes is not None:
            notes_ = self.notes
            notes_.to_etree(element, name_='notes', mapping_=mapping_)
        if self.detail is not None:
            detail_ = self.detail
            detail_.to_etree(element, name_='detail', mapping_=mapping_)
        if self.simple is not None:
            simple_ = self.simple
            simple_.to_etree(element, name_='simple', mapping_=mapping_)
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
        super(CarePlan_Activity, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'goal':
            obj_ = None
            self.goal.append(obj_)
            obj_.original_tagname_ = 'goal'
            self.validate_xmlIdRef(self.goal)    # validate type xmlIdRef
        elif nodeName_ == 'status':
            obj_ = CarePlanActivityStatus.factory()
            obj_.build(child_)
            self.status = obj_
            obj_.original_tagname_ = 'status'
        elif nodeName_ == 'prohibited':
            obj_ = boolean.factory()
            obj_.build(child_)
            self.prohibited = obj_
            obj_.original_tagname_ = 'prohibited'
        elif nodeName_ == 'actionResulting':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.actionResulting.append(obj_)
            obj_.original_tagname_ = 'actionResulting'
        elif nodeName_ == 'notes':
            obj_ = string.factory()
            obj_.build(child_)
            self.notes = obj_
            obj_.original_tagname_ = 'notes'
        elif nodeName_ == 'detail':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.detail = obj_
            obj_.original_tagname_ = 'detail'
        elif nodeName_ == 'simple':
            obj_ = CarePlan_Simple.factory()
            obj_.build(child_)
            self.simple = obj_
            obj_.original_tagname_ = 'simple'
        super(CarePlan_Activity, self).buildChildren(child_, node, nodeName_, True)
# end class CarePlan_Activity


class CarePlan_Simple(BackboneElement):
    """Describes the intention of how one or more practitioners intend to
    deliver care for a particular patient for a period of time,
    possibly limited to care for a specific condition or set of
    conditions.The period, timing or frequency upon which the
    described activity is to occur."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, category=None, code=None, timingSchedule=None, timingPeriod=None, timingString=None, location=None, performer=None, product=None, dailyAmount=None, quantity=None, details=None):
        self.original_tagname_ = None
        super(CarePlan_Simple, self).__init__(id, extension, modifierExtension, )
        self.category = category
        self.code = code
        self.timingSchedule = timingSchedule
        self.timingPeriod = timingPeriod
        self.timingString = timingString
        self.location = location
        if performer is None:
            self.performer = []
        else:
            self.performer = performer
        self.product = product
        self.dailyAmount = dailyAmount
        self.quantity = quantity
        self.details = details
    def factory(*args_, **kwargs_):
        if CarePlan_Simple.subclass:
            return CarePlan_Simple.subclass(*args_, **kwargs_)
        else:
            return CarePlan_Simple(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_category(self): return self.category
    def set_category(self, category): self.category = category
    def get_code(self): return self.code
    def set_code(self, code): self.code = code
    def get_timingSchedule(self): return self.timingSchedule
    def set_timingSchedule(self, timingSchedule): self.timingSchedule = timingSchedule
    def get_timingPeriod(self): return self.timingPeriod
    def set_timingPeriod(self, timingPeriod): self.timingPeriod = timingPeriod
    def get_timingString(self): return self.timingString
    def set_timingString(self, timingString): self.timingString = timingString
    def get_location(self): return self.location
    def set_location(self, location): self.location = location
    def get_performer(self): return self.performer
    def set_performer(self, performer): self.performer = performer
    def add_performer(self, value): self.performer.append(value)
    def insert_performer(self, index, value): self.performer[index] = value
    def get_product(self): return self.product
    def set_product(self, product): self.product = product
    def get_dailyAmount(self): return self.dailyAmount
    def set_dailyAmount(self, dailyAmount): self.dailyAmount = dailyAmount
    def get_quantity(self): return self.quantity
    def set_quantity(self, quantity): self.quantity = quantity
    def get_details(self): return self.details
    def set_details(self, details): self.details = details
    def hasContent_(self):
        if (
            self.category is not None or
            self.code is not None or
            self.timingSchedule is not None or
            self.timingPeriod is not None or
            self.timingString is not None or
            self.location is not None or
            self.performer or
            self.product is not None or
            self.dailyAmount is not None or
            self.quantity is not None or
            self.details is not None or
            super(CarePlan_Simple, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='CarePlan.Simple', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='CarePlan.Simple')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='CarePlan.Simple', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='CarePlan.Simple'):
        super(CarePlan_Simple, self).exportAttributes(outfile, level, already_processed, namespace_, name_='CarePlan.Simple')
    def exportChildren(self, outfile, level, namespace_='', name_='CarePlan.Simple', fromsubclass_=False, pretty_print=True):
        super(CarePlan_Simple, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.category is not None:
            self.category.export(outfile, level, namespace_, name_='category', pretty_print=pretty_print)
        if self.code is not None:
            self.code.export(outfile, level, namespace_, name_='code', pretty_print=pretty_print)
        if self.timingSchedule is not None:
            self.timingSchedule.export(outfile, level, namespace_, name_='timingSchedule', pretty_print=pretty_print)
        if self.timingPeriod is not None:
            self.timingPeriod.export(outfile, level, namespace_, name_='timingPeriod', pretty_print=pretty_print)
        if self.timingString is not None:
            self.timingString.export(outfile, level, namespace_, name_='timingString', pretty_print=pretty_print)
        if self.location is not None:
            self.location.export(outfile, level, namespace_, name_='location', pretty_print=pretty_print)
        for performer_ in self.performer:
            performer_.export(outfile, level, namespace_, name_='performer', pretty_print=pretty_print)
        if self.product is not None:
            self.product.export(outfile, level, namespace_, name_='product', pretty_print=pretty_print)
        if self.dailyAmount is not None:
            self.dailyAmount.export(outfile, level, namespace_, name_='dailyAmount', pretty_print=pretty_print)
        if self.quantity is not None:
            self.quantity.export(outfile, level, namespace_, name_='quantity', pretty_print=pretty_print)
        if self.details is not None:
            self.details.export(outfile, level, namespace_, name_='details', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='CarePlan.Simple', mapping_=None):
        element = super(CarePlan_Simple, self).to_etree(parent_element, name_, mapping_)
        if self.category is not None:
            category_ = self.category
            category_.to_etree(element, name_='category', mapping_=mapping_)
        if self.code is not None:
            code_ = self.code
            code_.to_etree(element, name_='code', mapping_=mapping_)
        if self.timingSchedule is not None:
            timingSchedule_ = self.timingSchedule
            timingSchedule_.to_etree(element, name_='timingSchedule', mapping_=mapping_)
        if self.timingPeriod is not None:
            timingPeriod_ = self.timingPeriod
            timingPeriod_.to_etree(element, name_='timingPeriod', mapping_=mapping_)
        if self.timingString is not None:
            timingString_ = self.timingString
            timingString_.to_etree(element, name_='timingString', mapping_=mapping_)
        if self.location is not None:
            location_ = self.location
            location_.to_etree(element, name_='location', mapping_=mapping_)
        for performer_ in self.performer:
            performer_.to_etree(element, name_='performer', mapping_=mapping_)
        if self.product is not None:
            product_ = self.product
            product_.to_etree(element, name_='product', mapping_=mapping_)
        if self.dailyAmount is not None:
            dailyAmount_ = self.dailyAmount
            dailyAmount_.to_etree(element, name_='dailyAmount', mapping_=mapping_)
        if self.quantity is not None:
            quantity_ = self.quantity
            quantity_.to_etree(element, name_='quantity', mapping_=mapping_)
        if self.details is not None:
            details_ = self.details
            details_.to_etree(element, name_='details', mapping_=mapping_)
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
        super(CarePlan_Simple, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'category':
            obj_ = CarePlanActivityCategory.factory()
            obj_.build(child_)
            self.category = obj_
            obj_.original_tagname_ = 'category'
        elif nodeName_ == 'code':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.code = obj_
            obj_.original_tagname_ = 'code'
        elif nodeName_ == 'timingSchedule':
            obj_ = Schedule.factory()
            obj_.build(child_)
            self.timingSchedule = obj_
            obj_.original_tagname_ = 'timingSchedule'
        elif nodeName_ == 'timingPeriod':
            obj_ = Period.factory()
            obj_.build(child_)
            self.timingPeriod = obj_
            obj_.original_tagname_ = 'timingPeriod'
        elif nodeName_ == 'timingString':
            obj_ = string.factory()
            obj_.build(child_)
            self.timingString = obj_
            obj_.original_tagname_ = 'timingString'
        elif nodeName_ == 'location':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.location = obj_
            obj_.original_tagname_ = 'location'
        elif nodeName_ == 'performer':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.performer.append(obj_)
            obj_.original_tagname_ = 'performer'
        elif nodeName_ == 'product':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.product = obj_
            obj_.original_tagname_ = 'product'
        elif nodeName_ == 'dailyAmount':
            obj_ = Quantity.factory()
            obj_.build(child_)
            self.dailyAmount = obj_
            obj_.original_tagname_ = 'dailyAmount'
        elif nodeName_ == 'quantity':
            obj_ = Quantity.factory()
            obj_.build(child_)
            self.quantity = obj_
            obj_.original_tagname_ = 'quantity'
        elif nodeName_ == 'details':
            obj_ = string.factory()
            obj_.build(child_)
            self.details = obj_
            obj_.original_tagname_ = 'details'
        super(CarePlan_Simple, self).buildChildren(child_, node, nodeName_, True)
# end class CarePlan_Simple


class CarePlanStatus(Element):
    """Indicates whether the plan is currently being acted upon, represents
    future intentions or is now just historical record.If the
    element is present, it must have either a @value, an @id, or
    extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(CarePlanStatus, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if CarePlanStatus.subclass:
            return CarePlanStatus.subclass(*args_, **kwargs_)
        else:
            return CarePlanStatus(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(CarePlanStatus, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='CarePlanStatus', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='CarePlanStatus')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='CarePlanStatus', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='CarePlanStatus'):
        super(CarePlanStatus, self).exportAttributes(outfile, level, already_processed, namespace_, name_='CarePlanStatus')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='CarePlanStatus', fromsubclass_=False, pretty_print=True):
        super(CarePlanStatus, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='CarePlanStatus', mapping_=None):
        element = super(CarePlanStatus, self).to_etree(parent_element, name_, mapping_)
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
        super(CarePlanStatus, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(CarePlanStatus, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class CarePlanStatus


class CarePlanActivityCategory(Element):
    """High-level categorization of the type of activity in a care plan.If
    the element is present, it must have either a @value, an @id, or
    extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(CarePlanActivityCategory, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if CarePlanActivityCategory.subclass:
            return CarePlanActivityCategory.subclass(*args_, **kwargs_)
        else:
            return CarePlanActivityCategory(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(CarePlanActivityCategory, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='CarePlanActivityCategory', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='CarePlanActivityCategory')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='CarePlanActivityCategory', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='CarePlanActivityCategory'):
        super(CarePlanActivityCategory, self).exportAttributes(outfile, level, already_processed, namespace_, name_='CarePlanActivityCategory')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='CarePlanActivityCategory', fromsubclass_=False, pretty_print=True):
        super(CarePlanActivityCategory, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='CarePlanActivityCategory', mapping_=None):
        element = super(CarePlanActivityCategory, self).to_etree(parent_element, name_, mapping_)
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
        super(CarePlanActivityCategory, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(CarePlanActivityCategory, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class CarePlanActivityCategory


class CarePlanGoalStatus(Element):
    """Indicates whether the goal has been met and is still being
    targetedIf the element is present, it must have either a @value,
    an @id, or extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(CarePlanGoalStatus, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if CarePlanGoalStatus.subclass:
            return CarePlanGoalStatus.subclass(*args_, **kwargs_)
        else:
            return CarePlanGoalStatus(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(CarePlanGoalStatus, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='CarePlanGoalStatus', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='CarePlanGoalStatus')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='CarePlanGoalStatus', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='CarePlanGoalStatus'):
        super(CarePlanGoalStatus, self).exportAttributes(outfile, level, already_processed, namespace_, name_='CarePlanGoalStatus')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='CarePlanGoalStatus', fromsubclass_=False, pretty_print=True):
        super(CarePlanGoalStatus, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='CarePlanGoalStatus', mapping_=None):
        element = super(CarePlanGoalStatus, self).to_etree(parent_element, name_, mapping_)
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
        super(CarePlanGoalStatus, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(CarePlanGoalStatus, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class CarePlanGoalStatus


class CarePlanActivityStatus(Element):
    """Indicates where the activity is at in its overall life cycleIf the
    element is present, it must have either a @value, an @id, or
    extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(CarePlanActivityStatus, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if CarePlanActivityStatus.subclass:
            return CarePlanActivityStatus.subclass(*args_, **kwargs_)
        else:
            return CarePlanActivityStatus(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(CarePlanActivityStatus, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='CarePlanActivityStatus', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='CarePlanActivityStatus')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='CarePlanActivityStatus', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='CarePlanActivityStatus'):
        super(CarePlanActivityStatus, self).exportAttributes(outfile, level, already_processed, namespace_, name_='CarePlanActivityStatus')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='CarePlanActivityStatus', fromsubclass_=False, pretty_print=True):
        super(CarePlanActivityStatus, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='CarePlanActivityStatus', mapping_=None):
        element = super(CarePlanActivityStatus, self).to_etree(parent_element, name_, mapping_)
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
        super(CarePlanActivityStatus, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(CarePlanActivityStatus, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class CarePlanActivityStatus
