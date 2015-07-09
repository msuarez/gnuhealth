from StringIO import StringIO

class ExportXMLMixin:
    def export_to_xml_string(self):
        """Export to string"""

        output = StringIO()
        self.export(outfile=output, namespacedef_='xmlns="http://hl7.org/fhir"', pretty_print=False, level=4)
        content = output.getvalue()
        output.close()
        return content


