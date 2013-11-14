import QtQuick 2.0

Rectangle {
    id: main

    color: "#00000000"
    width: 300; height: 400

    JogControl {
        id: jogControl

        height: parent.height * 0.65
        anchors { left: parent.left; leftMargin: 0; right: parent.right; rightMargin: 0; top: parent.top; topMargin: 0 }
    }

    JogSpeed {
        id: jogSpeed
        anchors.bottom: parent.bottom
        anchors.bottomMargin: 0

        anchors { left: parent.left; leftMargin: 0; right: parent.right; rightMargin: 0; top: jogControl.bottom; topMargin: 0 }
    }
}
