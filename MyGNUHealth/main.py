from PySide2.QtWidgets import QApplication
from PySide2.QtQuick import QQuickView
from PySide2.QtCore import QUrl

app = QApplication([])
view = QQuickView()
url = QUrl("main.qml")

view.setSource(url)
view.show()
app.exec_()
