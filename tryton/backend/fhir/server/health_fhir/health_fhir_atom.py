from math import ceil
from werkzeug.urls import Href
from datetime import datetime
from StringIO import StringIO
import server.fhir as supermod

class Bundle(supermod.FeedType):
    """A bundle is an atom feed"""

    def __init__(self, *args, **kwargs):
        """Set default values"""

        self.request=kwargs.pop('request', None)
        id_=kwargs.pop('id', getattr(self.request, 'url'))
        title = kwargs.pop('title', 'Search results')
        author = kwargs.pop('author', 'GNU Health')
        updated = kwargs.pop('updated', datetime.utcnow())
        total = kwargs.pop('total', 1) or 1     # Assume one result
        per_page = kwargs.pop('per_page', 10) or 10
        page = kwargs.pop('page', 1) or 1
        super(Bundle, self).__init__(*args, **kwargs)

        self.set_id(id_)
        self.set_title(title)
        self.set_author(author)
        self.set_updated(updated)
        self.set_totalResults(total)
        self.set_link(page, per_page, total)
        self.entries

    @property
    def entries(self):
        return self.entry

    def set_id(self, id_):
        """Set id"""
        if id_:
            i = supermod.IdType()
            i.set_valueOf_(str(id_))
            super(Bundle, self).set_id([i])

    def set_author(self, author):
        """Set author"""
        if author:
            a = supermod.PersonType()
            a.add_name(str(author))
            super(Bundle, self).set_author([a])

    def set_title(self, title):
        """Set title"""
        if title:
            t = supermod.TextType(valueOf_=str(title))
            t.content_.append(t.mixedclass_(
                    supermod.MixedContainer.CategoryText,
                    supermod.MixedContainer.TypeNone, '', str(title)))
            super(Bundle, self).set_title([t])

    def set_updated(self, updated):
        """Set updated; datetime object"""
        if updated is not None:
            u = supermod.DateTimeType()
            u.set_valueOf_(updated.isoformat())
            super(Bundle, self).set_updated([u])

    def set_totalResults(self, total):
        """Set total results"""
        if total is not None:
            super(Bundle, self).set_totalResults([int(total)])

    def set_link(self, page, per_page, total):
        """Set links: rel, prev, self, next, last"""
        links = []
        total_pages= int(ceil(float(total)/per_page))
        args = self.request.args.copy()
        href = Href(self.request.base_url)

        l = supermod.linkType()

        # self link
        l.rel = 'self'
        l.href = href(args)
        links.append(l)

        if total_pages > 1:

            # first link
            if page > 1:
                args['page'] = 1
                l.rel = 'first'
                l.href = href(args)
                links.append(l)

            # last link
            if page < total_pages:
                args['page'] = total_pages
                l.rel = 'last'
                l.href = href(args)
                links.append(l)

            # next link
            if page < total_pages - 1:      # last link already generated
                args['page'] = page + 1
                l.rel = 'next'
                l.href = href(args)
                links.append(l)

            # prev link
            if page > 2:
                args['page'] = page-1
                l.rel = 'previous'
                l.href = href(args)
                links.append(l)

        super(Bundle, self).set_link(links)

    def add_entry(self, entry):
        """Add entry; expects FHIR class"""

        if entry.feed:
            e = supermod.EntryType()
            t=supermod.TextType(valueOf_=entry.feed['title'])
            t.content_.append(t.mixedclass_(
                    supermod.MixedContainer.CategoryText,
                    supermod.MixedContainer.TypeNone, '', entry.feed['title']))
            e.title=[t]
            e.id = [supermod.IdType(valueOf_=entry.feed['id'])]
            e.updated = [supermod.DateTimeType(valueOf_=entry.feed['updated'].isoformat())]
            e.published = [supermod.DateTimeType(valueOf_=entry.feed['published'].isoformat())]
            ct = supermod.ContentType(type_='text/xml') # only xml for now

            if isinstance(entry, supermod.Binary):
                t = 'Binary'
                ct.set_Binary(entry)
            elif isinstance(entry, supermod.AdverseReaction):
                t = 'AdverseReaction'
                ct.set_AdverseReaction(entry)
            elif isinstance(entry, supermod.Alert):
                t = 'Alert'
                ct.set_Alert(entry)
            elif isinstance(entry, supermod.AllergyIntolerance):
                t = 'AllergyIntolerance'
                ct.set_AllergyIntolerance(entry)
            elif isinstance(entry, supermod.CarePlan):
                t = 'CarePlan'
                ct.set_CarePlan(entry)
            elif isinstance(entry, supermod.Composition):
                t = 'Composition'
                ct.set_Composition(entry)
            elif isinstance(entry, supermod.ConceptMap):
                t = 'ConceptMap'
                ct.set_ConceptMap(entry)
            elif isinstance(entry, supermod.Condition):
                t = 'Condition'
                ct.set_Condition(entry)
            elif isinstance(entry, supermod.Conformance):
                t = 'Conformance'
                ct.set_Conformance(entry)
            elif isinstance(entry, supermod.Device):
                t = 'Device'
                ct.set_Device(entry)
            elif isinstance(entry, supermod.DeviceObservationReport):
                t = 'DeviceObservationReport'
                ct.set_DeviceObservationReport(entry)
            elif isinstance(entry, supermod.DiagnosticOrder):
                t = 'DiagnosticOrder'
                ct.set_DiagnosticOrder(entry)
            elif isinstance(entry, supermod.DiagnosticReport):
                t = 'DiagnosticReport'
                ct.set_DiagnosticReport(entry)
            elif isinstance(entry, supermod.DocumentManifest):
                t = 'DocumentManifest'
                ct.set_DocumentManifest(entry)
            elif isinstance(entry, supermod.DocumentReference):
                t = 'DocumentReference'
                ct.set_DocumentReference(entry)
            elif isinstance(entry, supermod.Encounter):
                t = 'Encounter'
                ct.set_Encounter(entry)
            elif isinstance(entry, supermod.FamilyHistory):
                t = 'FamilyHistory'
                ct.set_FamilyHistory(entry)
            elif isinstance(entry, supermod.Group):
                t = 'Group'
                ct.set_Group(entry)
            elif isinstance(entry, supermod.ImagingStudy):
                t = 'ImagingStudy'
                ct.set_ImagingStudy(entry)
            elif isinstance(entry, supermod.Immunization):
                t = 'Immunization'
                ct.set_Immunization(entry)
            elif isinstance(entry, supermod.ImmunizationRecommendation):
                t = 'ImmunizationRecommendation'
                ct.set_ImmunizationRecommendation(entry)
            elif isinstance(entry, supermod.List):
                t = 'List'
                ct.set_List(entry)
            elif isinstance(entry, supermod.Location):
                t = 'Location'
                ct.set_Location(entry)
            elif isinstance(entry, supermod.Media):
                t = 'Media'
                ct.set_Media(entry)
            elif isinstance(entry, supermod.Medication):
                t = 'Medication'
                ct.set_Medication(entry)
            elif isinstance(entry, supermod.MedicationAdministration):
                t = 'MedicationAdministration'
                ct.set_MedicationAdministration(entry)
            elif isinstance(entry, supermod.MedicationDispense):
                t = 'MedicationDispense'
                ct.set_MedicationDispense(entry)
            elif isinstance(entry, supermod.MedicationPrescription):
                t = 'MedicationPrescription'
                ct.set_MedicationPrescription(entry)
            elif isinstance(entry, supermod.MedicationStatement):
                t = 'MedicationStatement'
                ct.set_MedicationStatement(entry)
            elif isinstance(entry, supermod.MessageHeader):
                t = 'MessageHeader'
                ct.set_MessageHeader(entry)
            elif isinstance(entry, supermod.Observation):
                t = 'Observation'
                ct.set_Observation(entry)
            elif isinstance(entry, supermod.OperationOutcome):
                t = 'OperationOutcome'
                ct.set_OperationOutcome(entry)
            elif isinstance(entry, supermod.Order):
                t = 'Order'
                ct.set_Order(entry)
            elif isinstance(entry, supermod.OrderResponse):
                t = 'OrderResponse'
                ct.set_OrderResponse(entry)
            elif isinstance(entry, supermod.Organization):
                t = 'Organization'
                ct.set_Organization(entry)
            elif isinstance(entry, supermod.Other):
                t = 'Other'
                ct.set_Other(entry)
            elif isinstance(entry, supermod.Patient):
                t = 'Patient'
                ct.set_Patient(entry)
            elif isinstance(entry, supermod.Practitioner):
                t = 'Practitioner'
                ct.set_Practitioner(entry)
            elif isinstance(entry, supermod.Procedure):
                t = 'Procedure'
                ct.set_Procedure(entry)
            elif isinstance(entry, supermod.Profile):
                t = 'Profile'
                ct.set_Profile(entry)
            elif isinstance(entry, supermod.Provenance):
                t = 'Provenance'
                ct.set_Provenance(entry)
            elif isinstance(entry, supermod.Query):
                t = 'Query'
                ct.set_Query(entry)
            elif isinstance(entry, supermod.Questionnaire):
                t = 'Questionnaire'
                ct.set_Questionnaire(entry)
            elif isinstance(entry, supermod.RelatedPerson):
                t = 'RelatedPerson'
                ct.set_RelatedPerson(entry)
            elif isinstance(entry, supermod.SecurityEvent):
                t = 'SecurityEvent'
                ct.set_SecurityEvent(entry)
            elif isinstance(entry, supermod.Specimen):
                t = 'Specimen'
                ct.set_Specimen(entry)
            elif isinstance(entry, supermod.Substance):
                t = 'Substance'
                ct.set_Supply(entry)
            elif isinstance(entry, supermod.ValueSet):
                t = 'ValueSet'
                ct.set_ValueSet(entry)

            # Now tell the class what type it is holding
            ct.content_.append(
                    ct.mixedclass_(
                        supermod.MixedContainer.CategoryComplex,
                        supermod.MixedContainer.TypeNone, t, entry))

            e.content = [ct]
            super(Bundle, self).add_entry(e)

    def export_to_xml_string(self):
        """Export to atom format"""
        i = StringIO()
        self.export(i, level=0, namespace_='', name_='feed', namespacedef_='xmlns="http://www.w3.org/2005/Atom"')
        return i.getvalue()

supermod.FeedType.subclass = Bundle
