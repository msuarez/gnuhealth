PDQ Module
##########

The PDQ module handles the HL7 PDQ and PDQV transactions.


PDQ Configuration
*****************

You can access the PDQ Configuration page by selecting the path HL7->Transactions->PDQ->Configuration.

The PDQ Configuration page contains the following configuration parameters:

- *Enabled*: if checked, it enables the PDQ module, so that it can handle incoming PDQ and PDQV requests and send a response to the client
- *Enable Allowed Apps Filter*: if checked, it enables the *Allowed Applications* filter for incoming messages. In this case,
   the module accepts only the incoming messages with the MSH.3 (Sending Application) value included into the *Allowed Applications Table*
- *Facility Name*: it is the value of the MSH.4 field used for all PDQ and PDQV responses
- *Encoding*: it is the expected encoding for incoming and outcoming PDQ and PDQV messages
- *Country*: it is the value of the MSH.17 field used for all PDQ and PDQV responses
- *Language*: it is the value of the MSH.19 field used for all PDQ and PDQV responses

Allowed Applications
********************

You can access the list of *Allowed Applications* by selecting the path HL7->Transactions->PDQ->Allowed Applications.

This list contains all sending application values (MSH 3 field) of the incoming PDQ requests accepted by the MLLP Server. 

Note that this filter is ignored if the *Allowed Apps Filter* is not enabled.


