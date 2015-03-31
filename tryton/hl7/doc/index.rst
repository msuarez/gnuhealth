HL7 Module
##########

The HL7 module provides an MLLP Server that:
- listens for incoming HL7 messages
- forwards the incoming messages to the proper HL7 submodule, according to the type of the received message (such as the PDQ module) 
- sends the HL7 response obtained from the HL7 submodule in the previous step
- logs all the HL7 transactions to a logging table

HL7 Configuration
*****************

The HL7 Configuration page contains the following configuration parameters:

 - *Server Enabled*: it enables/disables the MLLP Server
 - *MLLP Server Port*: it is the listening port of the MLLP Server 
 - *Message Logger*: it enables/disables the Message Logger. When enabled, each HL7 transaction (i.e. both the HL7 request and the response) is logged into the *Transactions Logger* table
 - *Application code*: it is the value of the MSH.3 field used for all HL7 responses.

Transactions Logger
*******************

You can access the *Transactions Logger* page by selecting the path HL7->Transactions->Transactions Logger

This page shows the list of all HL7 transactions, provided that you have enabled the *Message Logger* from the *HL7 Configuration* page.

For each HL7 transaction, the following informations are logged:

 - *Creation Date*: the date and time of the incoming HL7 message
 - *HL7 Request*: the incoming HL7 message (the HL7 request received from the client)
 - *HL7 Response*: the outcoming HL7 message (the HL7 response sent to the client)
 - *HL7 Handler*: the module that handled the transaction (e.g PDQTransactionHandler for PDQ requests)