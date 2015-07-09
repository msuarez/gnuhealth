import server.fhir as supermod
from server.common import safe_attrgetter
from StringIO import StringIO
from operator import attrgetter
from .health_mixin import ExportXMLMixin

try:
    from flask import url_for
    RUN_FLASK=True
except:
    from .datastore import dumb_url_generate
    RUN_FLASK=False

class DiagnosticReport_Map:
    """
    The model mapping for the DiagnosticReport Resource
    """
    # Must be completed (i.e., have date)
    root_search=[('date_analysis', '!=', None)]

    # No other models, just use row id
    url_prefixes={}

    model_mapping={
            'gnuhealth.lab': {
                'subject': 'patient',
                'performer': 'pathologist',
                'conclusion': 'results', #or diagnosis?
                'codedDiagnosis': 'diagnosis',
                'result': 'critearea',
                'date': 'date_analysis',
                'test': 'test',
                'code': 'test.code',
                'name': 'test.name'}
                }
    resource_search_params={
                    '_id': 'token',
                    '_language': None,
                    'date': None,
                    'diagnosis': None, 
                    'identifier': None,
                    'image': None,
                    'issued': 'date',
                    'name': 'token',
                    'performer': 'reference',
                    'request': None,
                    'result': 'reference',
                    'service': None,
                    'specimen': None,
                    'status': None,
                    'subject': 'reference'}

    # Reference parameters to resource type
    chain_map={
            'subject': 'Patient',
            'result': 'Observation',
            'performer': 'Practitioner'}

    search_mapping={
                    '_id': ['id'],
                    'issued': ['date_analysis'],
                    'name': ['test.code'],
                    'name:text': ['test.name'],
                    'performer': ['pathologist'],
                    'result': ['critearea'],
                    'subject': ['patient']}

class health_DiagnosticReport(supermod.DiagnosticReport, DiagnosticReport_Map, ExportXMLMixin):
    """
    Class that manages the interface between FHIR Resource DiagnosticReport
    and GNU Health
    """
    def __init__(self, *args, **kwargs):
        rec = kwargs.pop('gnu_record', None)
        super(health_DiagnosticReport, self).__init__(*args, **kwargs)
        if rec:
            self.set_gnu_diagnostic_report(rec)

    def set_gnu_diagnostic_report(self, diagnostic_report):
        """Set the GNU Health model

        Keyword arguments:
        diagnostic_report -- the Health model
        """

        self.diagnostic_report = diagnostic_report
        self.model_type = self.diagnostic_report.__name__

        # Only certain models
        if self.model_type not in self.model_mapping:
            raise ValueError('Not a valid model')

        self.map = self.model_mapping[self.model_type]

        self.__import_from_gnu_diagnostic_report()
        self.__set_feed_info()

    def __import_from_gnu_diagnostic_report(self):
        """Import data from the model"""
        if self.diagnostic_report:
            self.set_conclusion(safe_attrgetter(self.diagnostic_report, self.map['conclusion']))
            self.set_subject(safe_attrgetter(self.diagnostic_report, self.map['subject']))
            self.set_performer(safe_attrgetter(self.diagnostic_report, self.map['performer']))
            self.set_issued(safe_attrgetter(self.diagnostic_report, self.map['date']))
            self.set_result(safe_attrgetter(self.diagnostic_report, self.map['result']))
            self.set_name(safe_attrgetter(self.diagnostic_report, self.map['test']))
            self.set_identifier(
                    safe_attrgetter(self.diagnostic_report, self.map['test']),
                    safe_attrgetter(self.diagnostic_report, 'patient.rec_name'),
                    safe_attrgetter(self.diagnostic_report, self.map['date']))

    def set_identifier(self, report, patient, date):
        """Extends superclass for convenience

        Keyword arguments:
        report -- the report (Health model)
        patient -- patient name
        date -- the date (datetime object)
        """

        if report and patient and date:
            label = '{0} for {1} on {2}'.format(report.name, patient, date.strftime('%Y/%m/%d'))
            if RUN_FLASK:
                value = url_for('dr_record', log_id=report.id)
            else:
                value = dumb_url_generate(['DiagnosticReport', report.id])
            ident = supermod.Identifier(
                        label=supermod.string(value=label),
                        value=supermod.string(value=value))
            super(health_DiagnosticReport, self).set_identifier(ident)

    def __set_feed_info(self):
        """Sets the feed-relevant data"""
        if self.diagnostic_report:
            if RUN_FLASK:
                uri = url_for('dr_record',
                                log_id=self.diagnostic_report.id,
                                _external=True)
            else:
                uri = dumb_url_generate(['DiagnosticReport',
                                self.diagnostic_report.id])
            self.feed={'id': uri,
                    'published': self.diagnostic_report.create_date,
                    'updated': self.diagnostic_report.write_date or self.diagnostic_report.create_date,
                    'title': self.diagnostic_report.rec_name
                        }

    def set_name(self, name):
        """Extends superclass for convenience

        Keyword arguments:
        name -- the test (Health model)
        """

        if name:
            conc = supermod.CodeableConcept()
            conc.coding=[supermod.Coding()]
            conc.coding[0].display=supermod.string(value=name.name)
            conc.coding[0].code = supermod.code(value=name.code)
            super(health_DiagnosticReport, self).set_name(conc)

        else:
            # If you don't know what is being tested,
            #   the data is useless
            raise ValueError('No test coding info')

    def set_issued(self, issued):
        """Extends superclass for convenience

        Keyword arguments:
        issued -- the date issued (datetime object)
        """

        if issued is not None:
            instant = supermod.instant(value=issued.strftime("%Y-%m-%dT%H:%M:%S"))
            super(health_DiagnosticReport, self).set_issued(instant)
        else:
            # If there is no date attached, this report is either not done
            #  or useless
            raise ValueError('No date')

    def set_result(self, result):
        """Extends superclass for convenience

        Keyword arguments:
        result -- the results
        """

        if result:
            for test in result:
                if RUN_FLASK:
                    uri = url_for('obs_record', log_id=test.id)
                else:
                    uri = dumb_url_generate(['Observation', test.id])
                display = test.rec_name
                ref=supermod.ResourceReference()
                ref.display = supermod.string(value=display)
                ref.reference = supermod.string(value=uri)
                super(health_DiagnosticReport, self).add_result(ref)

            # No data = useless
            if len(self.get_result()) == 0:
                raise ValueError('No data')

        else:
            # No data = useless
            raise ValueError('No data')

    def set_performer(self, performer):
        """Extends superclass for convenience

        Keyword arguments:
        performer -- the lab performer (Health model)
        """

        if performer:
            if RUN_FLASK:
                uri = url_for('hp_record', log_id=performer.id)
            else:
                uri = dumb_url_generate(['Practitioner', performer.id])
            display = performer.name.rec_name
            ref=supermod.ResourceReference()
            ref.display = supermod.string(value=display)
            ref.reference = supermod.string(value=uri)
            super(health_DiagnosticReport, self).set_performer(ref)

    def set_subject(self, subject):
        """Extends superclass for convenience

        Keyword arguments:
        subject -- the patient (Health model)
        """

        if subject:
            patient = attrgetter(self.map['subject'])(self.diagnostic_report)
            if RUN_FLASK:
                uri = url_for('pat_record', log_id=subject.id)
            else:
                uri = dumb_url_generate(['Patient', subject.id])
            display = subject.rec_name
            ref=supermod.ResourceReference()
            ref.display = supermod.string(value=display)
            ref.reference = supermod.string(value=uri)
            super(health_DiagnosticReport, self).set_subject(ref)

        else:
            # Without subject, useless information
            raise ValueError('No subject')

    def set_conclusion(self, conclusion):
        """Extends superclass for convenience

        Keyword arguments:
        conclusion -- the report's conclusion
        """

        if conclusion:
            c = supermod.string(value=conclusion)
            super(health_DiagnosticReport, self).set_conclusion(c)

supermod.DiagnosticReport.subclass=health_DiagnosticReport
