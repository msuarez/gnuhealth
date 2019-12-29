import QtQuick 2.7
import QtQuick.Controls 2.0
import QtQuick.Layouts 1.0

Item {
    property alias item1: item1
    id: item1
    visible: true

    Rectangle {
        id: rectangle1
        width: 400
        height: 52
        color: "darkcyan"
        Image {
            id: image3
            x: 330
            y: 12
            width: 30
            height: 30
            anchors.right: rectangle1.right
            fillMode: Image.PreserveAspectFit
            source: "images/settings-b.png"
        }
    }

    MouseArea {
        id: mousearea1
        x: 0
        y: 252
        width: 400
        height: 148
        anchors.horizontalCenter: parent.horizontalCenter
        Image {
            id: image_phr
            anchors.fill: parent
            anchors.centerIn: parent.center
            fillMode: Image.PreserveAspectFit
            source: "images/my-gnu-health.png"
        }
    }

    property alias mousearea1: mousearea1
}
