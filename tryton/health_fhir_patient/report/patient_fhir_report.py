import pytz
from datetime import datetime
from trytond.pool import Pool
from trytond.transaction import Transaction
from trytond.report import Report

__all__ = ['PatientFhirReport']


class PatientFhirReport(Report):
    __name__ = 'patient.fhir'

    @classmethod
    def parse(cls, report, objects, data, localcontext):
        Company = Pool().get('company.company')

        timezone = None
        company_id = Transaction().context.get('company')
        if company_id:
            company = Company(company_id)
            if company.timezone:
                timezone = pytz.timezone(company.timezone)

        dt = datetime.now()
        localcontext['print_date'] = datetime.astimezone(dt.replace(
            tzinfo=pytz.utc), timezone)
        localcontext['print_time'] = localcontext['print_date'].time()

        return super(PatientFhirReport, cls).parse(report, objects, data, 
            localcontext)
