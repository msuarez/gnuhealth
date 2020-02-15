from gnu_health_fhir.common import helper_mixin


class BaseConfig(helper_mixin):
    @classmethod
    def build_fhir_object_from_health(cls, health):
        raise NotImplementedError()

    @classmethod
    def build_health_object_from_fhir(cls, fhir):
        raise NotImplementedError()
