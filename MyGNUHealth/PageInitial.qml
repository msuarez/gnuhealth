import QtQuick 2.7


PageInitialForm {
    mousearea1 {
        onClicked: stackView.push(Qt.resolvedUrl("PageLogin.qml"))
    }

}
