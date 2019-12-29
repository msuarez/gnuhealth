import QtQuick 2.7
import QtQuick.Controls 2.0
import QtQuick.Layouts 1.0

Page {
   id: loginPage
   title: qsTr("Login")

   // Login area
   Rectangle {
     id: loginForm
     anchors.centerIn: parent
     color: "white"
     width: 300
     height: 200
     radius: 4
   }

   GridLayout {
     id: content
     anchors.centerIn: loginForm
     columnSpacing: 20
     rowSpacing: 10
     columns: 2

     Text {
       Layout.topMargin: 8
       Layout.bottomMargin: 12
       Layout.alignment: Qt.AlignHCenter
       text: "GH Acct"
     }

     TextField {
       id: txtFedacct
       Layout.preferredWidth: 200
       font.pixelSize: 15
     }

     Text {
       text: qsTr("Password")
       font.pixelSize: 12
     }

     TextField {
       id: txtPassword
       Layout.preferredWidth: 200
       font.pixelSize: 15
       echoMode: TextInput.Password
     }

     Column {
       Layout.fillWidth: true
       Layout.columnSpan: 2
       Layout.topMargin: 12

       // buttons
       Button {
         text: qsTr("Login")
         flat: false
         anchors.horizontalCenter: parent.horizontalCenter
         onClicked: {
           loginPage.forceActiveFocus()

           // call login action
           fedLogin.login(txtFedacct.text, txtPassword.text)
         }
       }

     }
   }
}
