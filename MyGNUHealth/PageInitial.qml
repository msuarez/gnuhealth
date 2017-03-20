import QtQuick 2.7


PageInitialForm {
    mousearea1 {
        onClicked: stackView.push(Qt.resolvedUrl("PagePhr.qml"))
    }
    mousearea2 {
        onClicked: print("To be implemented")
    }

}
