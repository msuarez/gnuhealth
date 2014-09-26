from .base_classes import *
from .support_functions import *


class DiagnosticReport(Resource):
    """The findings and interpretation of diagnostic tests performed on
    patients, groups of patients, devices, and locations, and/or
    specimens derived from these. The report includes clinical
    context such as requesting and provider information, and some
    mix of atomic results, images, textual and coded interpretation,
    and formatted representation of diagnostic reports.If the
    element is present, it must have either a @value, an @id, or
    extensionsThe time or time-period the observed values are
    related to. This is usually either the time of the procedure or
    of specimen collection(s), but very often the source of the
    date/time is not known, only the date/time itself."""
    subclass = None
    superclass = Resource
    def __init__(self, id=None, extension=None, modifierExtension=None, language=None, text=None, contained=None, name=None, status=None, issued=None, subject=None, performer=None, identifier=None, requestDetail=None, serviceCategory=None, diagnosticDateTime=None, diagnosticPeriod=None, specimen=None, result=None, imagingStudy=None, image=None, conclusion=None, codedDiagnosis=None, presentedForm=None):
        self.original_tagname_ = None
        super(DiagnosticReport, self).__init__(id, extension, modifierExtension, language, text, contained, )
        self.name = name
        self.status = status
        self.issued = issued
        self.subject = subject
        self.performer = performer
        self.identifier = identifier
        if requestDetail is None:
            self.requestDetail = []
        else:
            self.requestDetail = requestDetail
        self.serviceCategory = serviceCategory
        self.diagnosticDateTime = diagnosticDateTime
        self.diagnosticPeriod = diagnosticPeriod
        if specimen is None:
            self.specimen = []
        else:
            self.specimen = specimen
        if result is None:
            self.result = []
        else:
            self.result = result
        if imagingStudy is None:
            self.imagingStudy = []
        else:
            self.imagingStudy = imagingStudy
        if image is None:
            self.image = []
        else:
            self.image = image
        self.conclusion = conclusion
        if codedDiagnosis is None:
            self.codedDiagnosis = []
        else:
            self.codedDiagnosis = codedDiagnosis
        if presentedForm is None:
            self.presentedForm = []
        else:
            self.presentedForm = presentedForm
    def factory(*args_, **kwargs_):
        if DiagnosticReport.subclass:
            return DiagnosticReport.subclass(*args_, **kwargs_)
        else:
            return DiagnosticReport(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_name(self): return self.name
    def set_name(self, name): self.name = name
    def get_status(self): return self.status
    def set_status(self, status): self.status = status
    def get_issued(self): return self.issued
    def set_issued(self, issued): self.issued = issued
    def get_subject(self): return self.subject
    def set_subject(self, subject): self.subject = subject
    def get_performer(self): return self.performer
    def set_performer(self, performer): self.performer = performer
    def get_identifier(self): return self.identifier
    def set_identifier(self, identifier): self.identifier = identifier
    def get_requestDetail(self): return self.requestDetail
    def set_requestDetail(self, requestDetail): self.requestDetail = requestDetail
    def add_requestDetail(self, value): self.requestDetail.append(value)
    def insert_requestDetail(self, index, value): self.requestDetail[index] = value
    def get_serviceCategory(self): return self.serviceCategory
    def set_serviceCategory(self, serviceCategory): self.serviceCategory = serviceCategory
    def get_diagnosticDateTime(self): return self.diagnosticDateTime
    def set_diagnosticDateTime(self, diagnosticDateTime): self.diagnosticDateTime = diagnosticDateTime
    def get_diagnosticPeriod(self): return self.diagnosticPeriod
    def set_diagnosticPeriod(self, diagnosticPeriod): self.diagnosticPeriod = diagnosticPeriod
    def get_specimen(self): return self.specimen
    def set_specimen(self, specimen): self.specimen = specimen
    def add_specimen(self, value): self.specimen.append(value)
    def insert_specimen(self, index, value): self.specimen[index] = value
    def get_result(self): return self.result
    def set_result(self, result): self.result = result
    def add_result(self, value): self.result.append(value)
    def insert_result(self, index, value): self.result[index] = value
    def get_imagingStudy(self): return self.imagingStudy
    def set_imagingStudy(self, imagingStudy): self.imagingStudy = imagingStudy
    def add_imagingStudy(self, value): self.imagingStudy.append(value)
    def insert_imagingStudy(self, index, value): self.imagingStudy[index] = value
    def get_image(self): return self.image
    def set_image(self, image): self.image = image
    def add_image(self, value): self.image.append(value)
    def insert_image(self, index, value): self.image[index] = value
    def get_conclusion(self): return self.conclusion
    def set_conclusion(self, conclusion): self.conclusion = conclusion
    def get_codedDiagnosis(self): return self.codedDiagnosis
    def set_codedDiagnosis(self, codedDiagnosis): self.codedDiagnosis = codedDiagnosis
    def add_codedDiagnosis(self, value): self.codedDiagnosis.append(value)
    def insert_codedDiagnosis(self, index, value): self.codedDiagnosis[index] = value
    def get_presentedForm(self): return self.presentedForm
    def set_presentedForm(self, presentedForm): self.presentedForm = presentedForm
    def add_presentedForm(self, value): self.presentedForm.append(value)
    def insert_presentedForm(self, index, value): self.presentedForm[index] = value
    def hasContent_(self):
        if (
            self.name is not None or
            self.status is not None or
            self.issued is not None or
            self.subject is not None or
            self.performer is not None or
            self.identifier is not None or
            self.requestDetail or
            self.serviceCategory is not None or
            self.diagnosticDateTime is not None or
            self.diagnosticPeriod is not None or
            self.specimen or
            self.result or
            self.imagingStudy or
            self.image or
            self.conclusion is not None or
            self.codedDiagnosis or
            self.presentedForm or
            super(DiagnosticReport, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='DiagnosticReport', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='DiagnosticReport')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='DiagnosticReport', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='DiagnosticReport'):
        super(DiagnosticReport, self).exportAttributes(outfile, level, already_processed, namespace_, name_='DiagnosticReport')
    def exportChildren(self, outfile, level, namespace_='', name_='DiagnosticReport', fromsubclass_=False, pretty_print=True):
        super(DiagnosticReport, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.name is not None:
            self.name.export(outfile, level, namespace_, name_='name', pretty_print=pretty_print)
        if self.status is not None:
            self.status.export(outfile, level, namespace_, name_='status', pretty_print=pretty_print)
        if self.issued is not None:
            self.issued.export(outfile, level, namespace_, name_='issued', pretty_print=pretty_print)
        if self.subject is not None:
            self.subject.export(outfile, level, namespace_, name_='subject', pretty_print=pretty_print)
        if self.performer is not None:
            self.performer.export(outfile, level, namespace_, name_='performer', pretty_print=pretty_print)
        if self.identifier is not None:
            self.identifier.export(outfile, level, namespace_, name_='identifier', pretty_print=pretty_print)
        for requestDetail_ in self.requestDetail:
            requestDetail_.export(outfile, level, namespace_, name_='requestDetail', pretty_print=pretty_print)
        if self.serviceCategory is not None:
            self.serviceCategory.export(outfile, level, namespace_, name_='serviceCategory', pretty_print=pretty_print)
        if self.diagnosticDateTime is not None:
            self.diagnosticDateTime.export(outfile, level, namespace_, name_='diagnosticDateTime', pretty_print=pretty_print)
        if self.diagnosticPeriod is not None:
            self.diagnosticPeriod.export(outfile, level, namespace_, name_='diagnosticPeriod', pretty_print=pretty_print)
        for specimen_ in self.specimen:
            specimen_.export(outfile, level, namespace_, name_='specimen', pretty_print=pretty_print)
        for result_ in self.result:
            result_.export(outfile, level, namespace_, name_='result', pretty_print=pretty_print)
        for imagingStudy_ in self.imagingStudy:
            imagingStudy_.export(outfile, level, namespace_, name_='imagingStudy', pretty_print=pretty_print)
        for image_ in self.image:
            image_.export(outfile, level, namespace_, name_='image', pretty_print=pretty_print)
        if self.conclusion is not None:
            self.conclusion.export(outfile, level, namespace_, name_='conclusion', pretty_print=pretty_print)
        for codedDiagnosis_ in self.codedDiagnosis:
            codedDiagnosis_.export(outfile, level, namespace_, name_='codedDiagnosis', pretty_print=pretty_print)
        for presentedForm_ in self.presentedForm:
            presentedForm_.export(outfile, level, namespace_, name_='presentedForm', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='DiagnosticReport', mapping_=None):
        element = super(DiagnosticReport, self).to_etree(parent_element, name_, mapping_)
        if self.name is not None:
            name_ = self.name
            name_.to_etree(element, name_='name', mapping_=mapping_)
        if self.status is not None:
            status_ = self.status
            status_.to_etree(element, name_='status', mapping_=mapping_)
        if self.issued is not None:
            issued_ = self.issued
            issued_.to_etree(element, name_='issued', mapping_=mapping_)
        if self.subject is not None:
            subject_ = self.subject
            subject_.to_etree(element, name_='subject', mapping_=mapping_)
        if self.performer is not None:
            performer_ = self.performer
            performer_.to_etree(element, name_='performer', mapping_=mapping_)
        if self.identifier is not None:
            identifier_ = self.identifier
            identifier_.to_etree(element, name_='identifier', mapping_=mapping_)
        for requestDetail_ in self.requestDetail:
            requestDetail_.to_etree(element, name_='requestDetail', mapping_=mapping_)
        if self.serviceCategory is not None:
            serviceCategory_ = self.serviceCategory
            serviceCategory_.to_etree(element, name_='serviceCategory', mapping_=mapping_)
        if self.diagnosticDateTime is not None:
            diagnosticDateTime_ = self.diagnosticDateTime
            diagnosticDateTime_.to_etree(element, name_='diagnosticDateTime', mapping_=mapping_)
        if self.diagnosticPeriod is not None:
            diagnosticPeriod_ = self.diagnosticPeriod
            diagnosticPeriod_.to_etree(element, name_='diagnosticPeriod', mapping_=mapping_)
        for specimen_ in self.specimen:
            specimen_.to_etree(element, name_='specimen', mapping_=mapping_)
        for result_ in self.result:
            result_.to_etree(element, name_='result', mapping_=mapping_)
        for imagingStudy_ in self.imagingStudy:
            imagingStudy_.to_etree(element, name_='imagingStudy', mapping_=mapping_)
        for image_ in self.image:
            image_.to_etree(element, name_='image', mapping_=mapping_)
        if self.conclusion is not None:
            conclusion_ = self.conclusion
            conclusion_.to_etree(element, name_='conclusion', mapping_=mapping_)
        for codedDiagnosis_ in self.codedDiagnosis:
            codedDiagnosis_.to_etree(element, name_='codedDiagnosis', mapping_=mapping_)
        for presentedForm_ in self.presentedForm:
            presentedForm_.to_etree(element, name_='presentedForm', mapping_=mapping_)
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
        super(DiagnosticReport, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'name':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.name = obj_
            obj_.original_tagname_ = 'name'
        elif nodeName_ == 'status':
            obj_ = DiagnosticReportStatus.factory()
            obj_.build(child_)
            self.status = obj_
            obj_.original_tagname_ = 'status'
        elif nodeName_ == 'issued':
            obj_ = dateTime.factory()
            obj_.build(child_)
            self.issued = obj_
            obj_.original_tagname_ = 'issued'
        elif nodeName_ == 'subject':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.subject = obj_
            obj_.original_tagname_ = 'subject'
        elif nodeName_ == 'performer':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.performer = obj_
            obj_.original_tagname_ = 'performer'
        elif nodeName_ == 'identifier':
            obj_ = Identifier.factory()
            obj_.build(child_)
            self.identifier = obj_
            obj_.original_tagname_ = 'identifier'
        elif nodeName_ == 'requestDetail':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.requestDetail.append(obj_)
            obj_.original_tagname_ = 'requestDetail'
        elif nodeName_ == 'serviceCategory':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.serviceCategory = obj_
            obj_.original_tagname_ = 'serviceCategory'
        elif nodeName_ == 'diagnosticDateTime':
            obj_ = dateTime.factory()
            obj_.build(child_)
            self.diagnosticDateTime = obj_
            obj_.original_tagname_ = 'diagnosticDateTime'
        elif nodeName_ == 'diagnosticPeriod':
            obj_ = Period.factory()
            obj_.build(child_)
            self.diagnosticPeriod = obj_
            obj_.original_tagname_ = 'diagnosticPeriod'
        elif nodeName_ == 'specimen':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.specimen.append(obj_)
            obj_.original_tagname_ = 'specimen'
        elif nodeName_ == 'result':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.result.append(obj_)
            obj_.original_tagname_ = 'result'
        elif nodeName_ == 'imagingStudy':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.imagingStudy.append(obj_)
            obj_.original_tagname_ = 'imagingStudy'
        elif nodeName_ == 'image':
            obj_ = DiagnosticReport_Image.factory()
            obj_.build(child_)
            self.image.append(obj_)
            obj_.original_tagname_ = 'image'
        elif nodeName_ == 'conclusion':
            obj_ = string.factory()
            obj_.build(child_)
            self.conclusion = obj_
            obj_.original_tagname_ = 'conclusion'
        elif nodeName_ == 'codedDiagnosis':
            obj_ = CodeableConcept.factory()
            obj_.build(child_)
            self.codedDiagnosis.append(obj_)
            obj_.original_tagname_ = 'codedDiagnosis'
        elif nodeName_ == 'presentedForm':
            obj_ = Attachment.factory()
            obj_.build(child_)
            self.presentedForm.append(obj_)
            obj_.original_tagname_ = 'presentedForm'
        super(DiagnosticReport, self).buildChildren(child_, node, nodeName_, True)
# end class DiagnosticReport


class DiagnosticReport_Image(BackboneElement):
    """The findings and interpretation of diagnostic tests performed on
    patients, groups of patients, devices, and locations, and/or
    specimens derived from these. The report includes clinical
    context such as requesting and provider information, and some
    mix of atomic results, images, textual and coded interpretation,
    and formatted representation of diagnostic reports."""
    subclass = None
    superclass = BackboneElement
    def __init__(self, id=None, extension=None, modifierExtension=None, comment=None, link=None):
        self.original_tagname_ = None
        super(DiagnosticReport_Image, self).__init__(id, extension, modifierExtension, )
        self.comment = comment
        self.link = link
    def factory(*args_, **kwargs_):
        if DiagnosticReport_Image.subclass:
            return DiagnosticReport_Image.subclass(*args_, **kwargs_)
        else:
            return DiagnosticReport_Image(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_comment(self): return self.comment
    def set_comment(self, comment): self.comment = comment
    def get_link(self): return self.link
    def set_link(self, link): self.link = link
    def hasContent_(self):
        if (
            self.comment is not None or
            self.link is not None or
            super(DiagnosticReport_Image, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='DiagnosticReport.Image', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='DiagnosticReport.Image')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='DiagnosticReport.Image', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='DiagnosticReport.Image'):
        super(DiagnosticReport_Image, self).exportAttributes(outfile, level, already_processed, namespace_, name_='DiagnosticReport.Image')
    def exportChildren(self, outfile, level, namespace_='', name_='DiagnosticReport.Image', fromsubclass_=False, pretty_print=True):
        super(DiagnosticReport_Image, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.comment is not None:
            self.comment.export(outfile, level, namespace_, name_='comment', pretty_print=pretty_print)
        if self.link is not None:
            self.link.export(outfile, level, namespace_, name_='link', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='DiagnosticReport.Image', mapping_=None):
        element = super(DiagnosticReport_Image, self).to_etree(parent_element, name_, mapping_)
        if self.comment is not None:
            comment_ = self.comment
            comment_.to_etree(element, name_='comment', mapping_=mapping_)
        if self.link is not None:
            link_ = self.link
            link_.to_etree(element, name_='link', mapping_=mapping_)
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
        super(DiagnosticReport_Image, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'comment':
            obj_ = string.factory()
            obj_.build(child_)
            self.comment = obj_
            obj_.original_tagname_ = 'comment'
        elif nodeName_ == 'link':
            obj_ = ResourceReference.factory()
            obj_.build(child_)
            self.link = obj_
            obj_.original_tagname_ = 'link'
        super(DiagnosticReport_Image, self).buildChildren(child_, node, nodeName_, True)
# end class DiagnosticReport_Image


class DiagnosticReportStatus(Element):
    """The status of the diagnostic report as a wholeIf the element is
    present, it must have either a @value, an @id, or extensions"""
    subclass = None
    superclass = Element
    def __init__(self, id=None, extension=None, value=None):
        self.original_tagname_ = None
        super(DiagnosticReportStatus, self).__init__(id, extension, )
        self.value = _cast(None, value)
    def factory(*args_, **kwargs_):
        if DiagnosticReportStatus.subclass:
            return DiagnosticReportStatus.subclass(*args_, **kwargs_)
        else:
            return DiagnosticReportStatus(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def hasContent_(self):
        if (
            super(DiagnosticReportStatus, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='DiagnosticReportStatus', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='DiagnosticReportStatus')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='DiagnosticReportStatus', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='DiagnosticReportStatus'):
        super(DiagnosticReportStatus, self).exportAttributes(outfile, level, already_processed, namespace_, name_='DiagnosticReportStatus')
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (quote_attrib(self.value), ))
    def exportChildren(self, outfile, level, namespace_='', name_='DiagnosticReportStatus', fromsubclass_=False, pretty_print=True):
        super(DiagnosticReportStatus, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='DiagnosticReportStatus', mapping_=None):
        element = super(DiagnosticReportStatus, self).to_etree(parent_element, name_, mapping_)
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
        super(DiagnosticReportStatus, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(DiagnosticReportStatus, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class DiagnosticReportStatus
