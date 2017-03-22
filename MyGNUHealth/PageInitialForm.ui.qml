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

    Rectangle {
        id: rectangle
        x: 0
        y: 52
        width: 400
        height: 148
        color: "#eff0f0"
        z: -1
        Image {
            id: image
            anchors.centerIn: parent.center
            anchors.fill: parent
            fillMode: Image.PreserveAspectFit
            source: "images/my-gnu-health.png"
        }
    }

    MouseArea {
        id: mousearea1
        y: 252
        width: 125
        height: 125
        anchors.horizontalCenter: parent.horizontalCenter
        Image {
            id: image_phr
            anchors.fill: parent
            anchors.centerIn: parent.center
            fillMode: Image.PreserveAspectFit
            source: "images/index-phr.png"
        }
    }

    property alias mousearea2: mousearea2
    property alias mousearea1: mousearea1
    MouseArea {
        id: mousearea2
        anchors.centerIn: item1.center
        y: 440
        width: 125
        height: 125
        anchors.horizontalCenter: parent.horizontalCenter
        Image {
            id: image_healthsystem
            anchors.fill: parent
            anchors.centerIn: parent.center
            fillMode: Image.PreserveAspectFit
            source: "images/index-health_system.png"
        }
    }
}
