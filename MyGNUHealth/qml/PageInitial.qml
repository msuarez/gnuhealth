import QtQuick 2.7
import QtQuick.Controls 2.0
import QtQuick.Layouts 1.3
import org.kde.kirigami 2.5 as Kirigami

Kirigami.Page {
    ColumnLayout {
        anchors.fill: parent
        Kirigami.Heading {
            Layout.alignment: Qt.AlignHCenter
            text: qsTr("Welcome to")
        }
        Image {
            Layout.fillWidth: true
            Layout.fillHeight: true
            fillMode: Image.PreserveAspectFit
            source: "../images/my-gnu-health.png"
        }
    }

    actions.main: Kirigami.Action {
        text: qsTr("Log in")
        onTriggered: pageStack.push(Qt.resolvedUrl("PageLogin.qml"))
    }
}
