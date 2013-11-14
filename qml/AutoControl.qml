import QtQuick 2.0
import QtQuick.Controls 1.0
import QtQuick.Dialogs 1.0

Rectangle {
    id: main

    color: "#00000000"
    width: 100
    height: 62

    TouchButton {
        id: openButton

        width: 50; height: 50
        anchors {left: parent.left; leftMargin: 0; verticalCenter: parent.verticalCenter}
        text: ""
        iconSource: "icons/document-open.png"

        onClicked: {
            fileDialog.open()
        }
    }

    TouchButton {
        id: reloadButton

        width: 50; height: 50
        anchors {left: openButton.right; leftMargin: 10; verticalCenter: parent.verticalCenter}
        text: ""
        iconSource: "icons/view-refresh.png"
    }

    TouchButton {
        id: playPauseButton

        width: 50; height: 50
        anchors {left: reloadButton.right; leftMargin: 10; verticalCenter: parent.verticalCenter}
        text: ""
        iconSource: "icons/media-playback-start.png"
    }

    TouchButton {
        id: stepButton

        width: 50; height: 50
        anchors {left: playPauseButton.right; leftMargin: 10; verticalCenter: parent.verticalCenter}
        text: ""
        iconSource: "icons/media-skip-forward.png"
    }

    TouchButton {
        id: stopButton

        width: 50; height: 50
        anchors {left: stepButton.right; leftMargin: 10; verticalCenter: parent.verticalCenter}
        text: ""
        iconSource: "icons/media-playback-stop.png"
    }

    FileDialog {
        id: fileDialog
        selectMultiple: false
        selectFolder: false
        selectExisting: true
        nameFilters: [ qsTr("GCode files (*.ngc *.gcode)"), qsTr("STL files (*.stl)"), qsTr("SCAD files (*.scad)") ,qsTr("All files (*)") ]
        title: qsTr("Open file")
        onFileUrlChanged: console.log(fileUrl)
    }
}
