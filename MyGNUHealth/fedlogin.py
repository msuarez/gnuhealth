from PySide2.QtCore import QObject, Signal, Property
import requests

class FederationLogin(QObject):
    def __init__(self):
        QObject.__init__(self)
        self.creds = {"account":'',"password":''}

    def getCredentials(self):
        print ("GETTER", self.creds)

    def setCredentials(self, credentials):
        self.creds = credentials
        self.loginRC.emit()



    def test_connection(self,acct, passwd):
        """ Make the connection test to Thalamus Server
            from the GNU Health HMIS using the institution
            associated admin and the related credentials
        """
        conn = ''
        host, port, user, password, ssl_conn, verify_ssl = \
            'localhost', 8443,  \
            acct, passwd, True, \
            False

        if (ssl_conn):
            protocol = 'https://'
        else:
            protocol = 'http://'

        if (not user or not password):
            print("Please provide login credentials")


        url = protocol + host + ':' + str(port) + '/people/' + user

        try:
            conn = requests.get(url,
                auth=(user, password), verify=verify_ssl)

        except:
            print ("ERROR authenticating to Server")
            login_status = -2


        if conn:
            print ("***** Connection to Thalamus Server OK !******")
            login_status = 0

        else:
            print ("##### Wrong credentials ####")
            login_status = -1

        return (login_status)

    # Signal to emit to QML as onLoginRC
    loginRC = Signal()

    # login credentials property from and to QML
    credentials = Property(dict, getCredentials, setCredentials,
                           notify=loginRC)
