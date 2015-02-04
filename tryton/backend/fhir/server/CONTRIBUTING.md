### README

Expect frequent changes. Unfortunately.

The bulk of heavy-lifting will be handled care by generated code. The FHIR standard **will** change. However, they do publish XML schema documents that define the standards. Luckily, there are python libraries that can turn these schema documents into python classes. Consequently, if we separate our own code from these changing standards, we can write quasi-forward-compatible code.

Handling FHIR XML documents is simple with the generated code. The developers main goal is to interface the generated classes with the GNU Health models. This isn't as simple as it may sound. The FHIR standard does not look like GNU Health and common concepts in FHIR are not easily transferred to GNU Health (e.g., versions, resources, etc.). What we will do is write sub-classes that extend the generated classes to give this extended functionality. For example, there is a Patient class in our generated class. We write a subclass that can take a GNU Health patient, extract its relevant data, and implement it correctly in the super class. Then we can use the generated class to handle the exporting, type assurance, parsing, etc. There is a lot of glue to write, but, hey, that's coding.

JSON... what a terrible and great format. The FHIR standard defines a JSON standard, too. But what makes JSON great also makes it... awkward with robust standards. However, JSON is optional in FHIR. Consequently, after we have a working XML standard, we'll start working on JSON implementation.

The substantive part of the server can be used in any server setup or framework. However, Flask (the python micro-framework) handles REST design very well, so we will use that, at least to get a minimally functioning product. Flask stays out of the way and having no experience with Flask is fine if you want to help develop.

Functioning endpoints:

- Patient
- DiagnosticReport
- Practitioner
- Procedure
- Observation

Functioning interactions:

- search
- read
- validate
- create (on patient, *but can fail spectacularly, and disabled*)

What is **NOT** working:

- vread/history (no version support, *yet*)
- update (no version support)
- delete (never allow this?)

What needs to be done:

- Testing (Work-in-progress)
- More endpoints
- Version support
