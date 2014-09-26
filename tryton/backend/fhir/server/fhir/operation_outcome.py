from .base_classes import *
from .support_functions import *


class OperationOutcome(Resource):
    """A collection of error, warning or information messages that result
    from a system action.If the element is present, it must have
    either a @value, an @id, or extensions"""
    subclass = None
    superclass = Resource
    def __init__(self, id=None, extension=None, modifierExtension=None, language=None, text=None, contained=None, issue=None):
        self.original_tagname_ = None
        super(OperationOutcome, self).__init__(id, extension, modifierExtension, language, text, contained, )
        if issue is None:
            self.issue = []
        else:
            self.issue = issue
    def factory(*args_, **kwargs_):
        if OperationOutcome.subclass:
            return OperationOutcome.subclass(*args_, **kwargs_)
        else:
            return OperationOutcome(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_issue(self): return self.issue
    def set_issue(self, issue): self.issue = issue
    def add_issue(self, value): self.issue.append(value)
    def insert_issue(self, index, value): self.issue[index] = value
    def hasContent_(self):
        if (
            self.issue or
            super(OperationOutcome, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='OperationOutcome', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='OperationOutcome')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='OperationOutcome', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='OperationOutcome'):
        super(OperationOutcome, self).exportAttributes(outfile, level, already_processed, namespace_, name_='OperationOutcome')
    def exportChildren(self, outfile, level, namespace_='', name_='OperationOutcome', fromsubclass_=False, pretty_print=True):
        super(OperationOutcome, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for issue_ in self.issue:
            issue_.export(outfile, level, namespace_, name_='issue', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='OperationOutcome', mapping_=None):
        element = super(OperationOutcome, self).to_etree(parent_element, name_, mapping_)
        for issue_ in self.issue:
            issue_.to_etree(element, name_='issue', mapping_=mapping_)
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
        super(OperationOutcome, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'issue':
            obj_ = OperationOutcome_Issue.factory()
            obj_.build(child_)
            self.issue.append(obj_)
            obj_.original_tagname_ = 'issue'
        super(OperationOutcome, self).buildChildren(child_, node, nodeName_, True)
# end class OperationOutcome


class OperationOutcome_Issue(BackboneElement):
    """A collection of error, warning or information messages that result
    from a system action."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, severity=None, type_=None, details=None, location=None):
        self.original_tagname_ = None
        super(OperationOutcome_Issue, self).__init__(id, extension, modifierExtension, )
        self.severity = severity
        self.type_ = type_
        self.details = details
        if location is None:
            self.location = []
        else:
            self.location = location
    def factory(*args_, **kwargs_):
        if OperationOutcome_Issue.subclass:
            return OperationOutcome_Issue.subclass(*args_, **kwargs_)
        else:
            return OperationOutcome_Issue(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_severity(self): return self.severity
    def set_severity(self, severity): self.severity = severity
    def get_type(self): return self.type_
    def set_type(self, type_): self.type_ = type_
    def get_details(self): return self.details
    def set_details(self, details): self.details = details
    def get_location(self): return self.location
    def set_location(self, location): self.location = location
    def add_location(self, value): self.location.append(value)
    def insert_location(self, index, value): self.location[index] = value
    def hasContent_(self):
        if (
            self.severity is not None or
            self.type_ is not None or
            self.details is not None or
            self.location or
            super(OperationOutcome_Issue, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='OperationOutcome.Issue', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='OperationOutcome.Issue')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='OperationOutcome.Issue', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='OperationOutcome.Issue'):
        super(OperationOutcome_Issue, self).exportAttributes(outfile, level, already_processed, namespace_, name_='OperationOutcome.Issue')
    def exportChildren(self, outfile, level, namespace_='', name_='OperationOutcome.Issue', fromsubclass_=False, pretty_print=True):
        super(OperationOutcome_Issue, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.severity is not None:
            self.severity.export(outfile, level, namespace_, name_='severity', pretty_print=pretty_print)
        if self.type_ is not None:
            self.type_.export(outfile, level, namespace_, name_='type', pretty_print=pretty_print)
        if self.details is not None:
            self.details.export(outfile, level, namespace_, name_='details', pretty_print=pretty_print)
        for location_ in self.location:
            location_.export(outfile, level, namespace_, name_='location', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='OperationOutcome.Issue', mapping_=None):
        element = super(OperationOutcome_Issue, self).to_etree(parent_element, name_, mapping_)
        if self.severity is not None:
            severity_ = self.severity
            severity_.to_etree(element, name_='severity', mapping_=mapping_)
        if self.type_ is not None:
            type__ = self.type_
            type__.to_etree(element, name_='type', mapping_=mapping_)
        if self.details is not None:
            details_ = self.details
            details_.to_etree(element, name_='details', mapping_=mapping_)
        for location_ in self.location:
            location_.to_etree(element, name_='location', mapping_=mapping_)
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
        super(OperationOutcome_Issue, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'severity':
            obj_ = IssueSeverity.factory()
            obj_.build(child_)
            self.severity = obj_
            obj_.original_tagname_ = 'severity'
        elif nodeName_ == 'type':
            obj_ = Coding.factory()
            obj_.build(child_)
            self.type_ = obj_
            obj_.original_tagname_ = 'type'
        elif nodeName_ == 'details':
            obj_ = string.factory()
            obj_.build(child_)
            self.details = obj_
            obj_.original_tagname_ = 'details'
        elif nodeName_ == 'location':
            obj_ = string.factory()
            obj_.build(child_)
            self.location.append(obj_)
            obj_.original_tagname_ = 'location'
        super(OperationOutcome_Issue, self).buildChildren(child_, node, nodeName_, True)
# end class OperationOutcome_Issue
