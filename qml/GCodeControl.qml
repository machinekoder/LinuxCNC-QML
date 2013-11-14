import QtQuick 2.0
import QtQuick.Controls 1.0

Rectangle {
    id: main

    color: "#00000000"

    TextField {
        id: text_field1
        y: 122
        height: 22
        anchors.right: button2.left
        anchors.rightMargin: 5
        anchors.bottom: parent.bottom
        anchors.bottomMargin: 5
        anchors.left: parent.left
        anchors.leftMargin: 5
        placeholderText: "Enter GCode"
    }

    Button {
        id: button2
        x: 125
        y: 122
        width: 72
        height: 22
        text: "Send"
        anchors.bottom: parent.bottom
        anchors.bottomMargin: 5
        anchors.right: parent.right
        anchors.rightMargin: 5
    }

    Text {
        id: text7
        text: qsTr("<b>Active GCodes:</b>")
        anchors.top: parent.top
        anchors.topMargin: 5
        anchors.bottom: text_field1.top
        anchors.bottomMargin: 5
        anchors.right: parent.right
        anchors.rightMargin: 5
        anchors.left: parent.left
        anchors.leftMargin: 5
        font.pixelSize: 12
    }
}
