from gnu_health_fhir.adapters import (
    Patient,
    Condition,
    Procedure,
    Practitioner,
    Observation,
    DiagnosticReport,
    Immunization,
    FamilyMemberHistory,
    MedicationStatement,
    Encounter,
    ClinicalImpression,
    Coverage,
)
from proteus import config, Model
import pytest

config = config.set_xmlrpc(
    "http://admin:gnusolidario@federation.gnuhealth.org:8000/health36/"
)

# @pytest.mark.skip
def test_ci_info():
    CI = Model.get("gnuhealth.patient.evaluation")
    for ci in CI.find():
        info = ClinicalImpression.to_fhir_object(ci)


# @pytest.mark.skip
def test_enc_info():
    ENC = Model.get("gnuhealth.patient.evaluation")
    for enc in ENC.find():
        info = Encounter.to_fhir_object(enc)


# @pytest.mark.skip
def test_ms_info():
    MS = Model.get("gnuhealth.patient.medication")
    for ms in MS.find():
        info = MedicationStatement.to_fhir_object(ms)


# @pytest.mark.skip
def test_fh_info():
    FH = Model.get("gnuhealth.patient.family.diseases")
    for fh in FH.find():
        info = FamilyMemberHistory.to_fhir_object(fh)


# @pytest.mark.skip
def test_dr_info():
    DR = Model.get("gnuhealth.lab")
    for dr in DR.find([("date_analysis", "!=", None)]):
        report = DiagnosticReport.to_fhir_object(dr)


# @pytest.mark.skip
def test_vac_info():
    VAC = Model.get("gnuhealth.vaccination")
    for vac in VAC.find():
        v = Immunization.to_fhir_object(vac)


# @pytest.mark.skip
def test_patient_info():
    Pat = Model.get("gnuhealth.patient")
    for p in Pat.find():
        patient = Patient.to_fhir_object(p)
        # assert set(keys).issubset(p.keys())
        # for key in keys:
        # print(getattr(patient.resource, key))


# @pytest.mark.skip
def test_condition_info():
    Cond = Model.get("gnuhealth.patient.disease")
    for c in Cond.find():
        condition = Condition.to_fhir_object(c)


# @pytest.mark.skip
def test_procedure_info():
    Proc = Model.get("gnuhealth.operation")
    for p in Proc.find():
        procedure = Procedure.to_fhir_object(p)


# @pytest.mark.skip
def test_practitioner_info():
    HP = Model.get("gnuhealth.healthprofessional")
    for hp in HP.find():
        hprof = Practitioner.to_fhir_object(hp)


# @pytest.mark.skip
def test_obs_info():
    Obs = Model.get("gnuhealth.lab.test.critearea")
    for obs in Obs.find([[("gnuhealth_lab_id", "!=", None)]]):
        observ = Observation.to_fhir_object(obs)


# @pytest.mark.skip
def test_cov_info():
    Cov = Model.get("gnuhealth.insurance")
    for cov in Cov.find():
        c = Coverage.to_fhir_object(cov)
