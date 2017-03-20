/***********************************************************************
 * MyGNUHealth 
 * 
 * Copyright 2008-2017 Luis Falcon <falcon@gnu.org>
 * Copyright 2008-2017 GNU Solidario <health@gnusolidario.org>
 * 
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3 of the License, or
 * (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
 * MA 02110-1301, USA.
 * 
 **********************************************************************/
 
import QtQuick 2.7
import QtQuick.Controls 2.0
import QtQuick.Layouts 1.0

ApplicationWindow {
    readonly property alias pageStack: stackView

    visible: true
    width: 400
    height: 600
    title: qsTr("MyGNUHealth")

    StackView {
        id: stackView
        anchors.fill: parent
        initialItem: PageInitial {}

    }

    onClosing: {
    if (Qt.platform.os == "android") {
    if (stackView.depth > 1) {
    close.accepted = false
    stackView.pop()
        }
        }

    }
}
