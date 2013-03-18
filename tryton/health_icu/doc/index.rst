GNU Health Intensive Care Unit Module
#####################################

Health ICU includes functionality in a Intensive Care Unit.

It incorporates scoring systems, such :

- GSC : Glasgow Coma Scale
- APACHE II : Acute Physiology and Chronic Health Evaluation II

The functionality is divided into two major sections :

- Patient ICU Information
- Patient Roundings

1) Patient ICU Information : Health -> Hospitalization -> Intensive Care -> Patient ICU Info
All the information is linked to the Inpatient record. This form allows you to have an idea of the patient status, days since admission at ICU and use of mechanical ventilation, among other functionalities.
From this form, you can directly create and evaluate :

- Electrocardiograms
- APACHE II Scoring
- Glasgow Coma Scale scoring

This is the preferred method to create new tests and evaluations on the patient, since it automatically takes the Inpatient Registration number and the patient information associated to it. This eliminates the error of assigning another inpatient record.

2) Patient Rounding : Health -> Nursing -> Roundings
All the ICU related information is on the new "ICU" tab. The assessment is divided in different systems :

- Neurological
- Respiratory
- Cardiovascular
- Blood and Skin
- Digestive

In this assesment (that can have different frequencies, depending on the center policies ), you should enter the information starting at the left tab (Main) and once you are done with this section, switch to the ICU tab.

The information in for the Glasgow Coma Scale and Electrocardiogram can be entered at that very same moment (if the EKG is done at bed side at evaluation time), or can be selected from the list. Please ask to put a short interpretation on the EKG.
For each EKG, in addition to fill in as much information as possible, please take a picture or scan the ECG strip, since it can provide valuable information for further evaluations ! The information related to the ECG in the rounding will be the Interpretation, so please be clear.
Of course, you can access to the rest of the information related to the ECG by opening the resource.

Xray picture : The ICU rounding allows to place an Xray (or other imaging diagnosis image). Unlike attachments related to the object, that you can also use, this image is even more contextual and graphic. Of course, this image should be very recent to the evaluation itself.

Drainages : Chest drainages are input  from a One2Many widget. This permits to have as many as in the patient, and with their own characteristics.


