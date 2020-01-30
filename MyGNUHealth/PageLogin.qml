import org.kde.kirigami 2.5 as Kirigami
import QtQuick.Controls 2.0
import QtQuick.Layouts 1.0

Kirigami.Page
{
   id: loginPage
   title: qsTr("Login")

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
                // call login action
                fedLogin.login(txtFedacct.text, txtPassword.text)
            }
        }
    }
}
