import QtQuick 2.7
import QtQuick.Controls 2.0
import QtQuick.Layouts 1.0

Item {
    property alias item1 : item1
    id: item1
    visible: true
    Image {
        id: image
        x: 43
        y: 59
        width: 315
        height: 137
        fillMode: Image.PreserveAspectFit
        source: "images/my-gnu-health.png"
    }

    Rectangle {
        id: rectangle
        x: 0
        y: 52
        width: 400
        height: 148
        color: "#eff0f0"
        z: -1
    }

    MouseArea {
        id: mousearea1
        x: 125
        y: 252
        width: 125
        height: 125
        Image {
            id: image_phr
            anchors.fill: parent
            fillMode: Image.PreserveAspectFit
            source: "images/index-phr.png"
        }
    }


    property alias mousearea2 : mousearea2
    property alias mousearea1: mousearea1
    MouseArea {
        id: mousearea2
        x: 125
        y: 440
        width: 125
        height: 125
        Image {
            id: image_healthsystem
            anchors.fill: parent
            fillMode: Image.PreserveAspectFit
            source: "images/index-health_system.png"
        }
    }


    Rectangle {
        id: rectangle1
        width: 400
        height: 52
        color: "#1b9191"
    }

    Image {
        id: image3
        x: 330
        y: 12
        width: 30
        height: 30
        fillMode: Image.PreserveAspectFit
        source: "images/settings-b.png"
    }

}
