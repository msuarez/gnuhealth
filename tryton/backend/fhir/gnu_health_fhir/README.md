# gnu_health_fhir

This package aims to provide a functional FHIR interface to GNU Health data models. With the provided classes, one should be able to work to and from the back-end data from GNU Health in a FHIR-compatible way. The module, ultimately, should provide a full interface - CRUD, type conversions, serializers, and so on.

#### Design

The ultimate goal is that for every appropriate FHIR Resource there will be an adapter which interfaces with the backend data models.

There are plans to extend some of the resources to better approximate the GNU Health data schemes. The FHIR specification and GNU Health storage format rarely overlap, many times requiring significant data contortions. This is an ongoing process and there is a decided lack of motivation to do too much heavy-lifting, consequently these 'hacks' should be kept to a minimum.

#### Resources

Currently, the package at least partially supports reads of these FHIR resources:

- Patient
- Practitioner
- Immunization
- Condition
- Observation
- DiagnosticReport
- MedicationStatement
- FamilyMemberHistory
- Procedure
- Encounter
- ClinicalImpression
- Coverage

Not every resource's element is currently supported. Some of the elements have no equivalent in GNU Health, do not apply, have not reached maturity, or are undesirable in other ways. The FHIR resources are still under active development which makes them a moving target. The goal is to support all the reasonable, appropriate elements.

#### Usage

The easiest example is to use Proteus with this package:

    from proteus import config, Model
    from gnu_health_fhir import Patient

    #Connect to the GNU Health demo server
    config = config.set_xmlrpc('http://admin:gnusolidario@health.gnusolidario.org:8000/health36/')

    #Get the patient model
    model = Model.get('gnuhealth.patient')

    #Find the first patient
    first_patient = model.find()[0]

    #Convert to a fhir data object
    patient = Patient.to_fhir_object(first_patient)

    #Now you can use the data just like in fhirclient
    print(patient.as_json())

#### Libraries used

- fhirclient (core FHIR data models)
- pendulum (sane datetimes)
