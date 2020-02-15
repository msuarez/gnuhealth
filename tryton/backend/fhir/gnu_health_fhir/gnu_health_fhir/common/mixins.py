__all__ = ["helper_mixin"]


class helper_mixin(object):
    @classmethod
    def build_codeable_concept(cls, code, system=None, text=None, display=None):
        codeable_concept = {}
        if code:
            coding = {}
            if system:
                coding["system"] = system
            if text or display:
                coding["display"] = display or text
            coding["code"] = str(code)
            codeable_concept = {"coding": [coding]}
        if text:
            codeable_concept["text"] = text
        return codeable_concept

    @classmethod
    def get_code_from_codeable_concept(cls, concept):
        try:
            return concept["coding"][0]["code"]
        except:
            return None
