from StringIO import StringIO
from datetime import datetime
import server.fhir as supermod
from .health_mixin import ExportXMLMixin

# Sub-class OperationOutcome

class health_OperationOutcome(supermod.OperationOutcome, ExportXMLMixin):
    '''This provides an easy sub-class to operation outcomes'''

    def add_issue(self, severity=None, location=None, details=None):
        issue=health_OperationOutcome_Issue()
        issue.set_severity(severity)
        issue.set_details(details)
        issue.add_location(location)
        super(health_OperationOutcome, self).add_issue(issue)

supermod.OperationOutcome.subclass=health_OperationOutcome

class health_OperationOutcome_Issue(supermod.OperationOutcome_Issue):
    '''This provides an easy sub-class to operation outcome issues'''
    def set_details(self, details):
        if details:
            st = supermod.string(value=details)
            super(health_OperationOutcome_Issue, self).set_details(st)

    def add_location(self, location):
        if location:
            st = supermod.string(value=location)
            super(health_OperationOutcome_Issue, self).add_location(st)

    def set_severity(self, severity):
        if severity:
            sev=supermod.misc.IssueSeverity(value=severity)
            super(health_OperationOutcome_Issue, self).set_severity(sev)

supermod.OperationOutcome_Issue.subclass=health_OperationOutcome_Issue
