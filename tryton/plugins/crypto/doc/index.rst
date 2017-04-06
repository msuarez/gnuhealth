Tryton Crytpo Plugin
####################

This plugin has been developed as part of GNU Health [1], but you should 
be able to use it with any model in Tryton[2]

Functionality :
The Tryton crypto plugin interacts with GNU Privacy Guard [3] to digitally
sign and encrypt documents.

OS Requirements:

Model attributes :
The plugin requires - as a minimum - the following attributes on the model
in order to be able to sign the document. 

    "document_digest" of type fields.Char
    "digital_signature" of type fields.Text 


In real life, you will need others to make it meaningful. Please take a look
at the Prescription model on the health_crypto module for an example and
other fields used.



Usage:

References:

1.- GNU Health : http://health.gnu.org
2.- Tryton : http://www.tryton.org
3.- GNU Privacy Guard : http://www.gnupg.org
