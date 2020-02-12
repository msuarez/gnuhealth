import QtQuick 2.7
import org.kde.kirigami 2.5 as Kirigami
import QtQuick.Controls 2.0
import QtQuick.Layouts 1.3
import FedLogin 0.1

Kirigami.Page
{
id: loginPage
title: qsTr("Login")

    FedLogin { // FedLogin object registered at main.py to be used here
        id: fedlogin

        onLoginRC: {
            pageStack.push(Qt.resolvedUrl("PagePhr.qml"))
        }
    }

    Item {
        id: logininfo
        property variant accountinfo: ({"account":'',"password":''})
    }

    Kirigami.FormLayout {
        id: content
        anchors.fill: parent

        TextField {
            id: txtFedacct
            Kirigami.FormData.label: qsTr("GH Acct")
        }

        TextField {
            id: txtPassword
            Kirigami.FormData.label: qsTr("Password")
            echoMode: TextInput.Password
        }

        Button {
            text: qsTr("Login")
            flat: false
            Layout.alignment: Qt.AlignHCenter
            onClicked: {
                //fedlogin.credentials = txtFedacct.text
                logininfo.accountinfo.acct = txtFedacct.text
                logininfo.accountinfo.passwd = txtPassword.text
                fedlogin.credentials = logininfo.accountinfo
                console.log (fedlogin.credentials.account)
            }
        }
    }

}
