import QtQuick 2.0
import QtQuick.Controls 1.0

Rectangle {
    id: machineControlGroup

    color: "#00000000"

    TouchButton {
        id: stopButton
        width: 50
        height: 50
        text: ""
        checked: true
        checkable: true
        anchors.left: parent.left
        anchors.verticalCenter: parent.verticalCenter
        iconSource: "icons/process-stop.png"
        onClicked: {
            if (checked) {
                command.state(stat.STATE_ESTOP_RESET)
            }
            else {
                command.state(stat.STATE_ESTOP)
            }
        }
    }
    TouchButton {
        id: powerButton
        width: 50
        height: 50
        text: ""
        checkable: true
        checked: false
        anchors.left: stopButton.right
        anchors.leftMargin: 10
        anchors.verticalCenter: parent.verticalCenter
        iconSource: "icons/system-shutdown.png"
        onClicked: {
            if (checked) {
                command.state(stat.STATE_ON)
            }
            else {
                command.state(stat.STATE_OFF)
            }
        }
    }
    TouchButton {
        id: abortButton
        width: 50
        height: 50
        text: ""
        anchors.left: powerButton.right
        anchors.leftMargin: 10
        anchors.verticalCenter: parent.verticalCenter
        iconSource: "icons/dialog-cancel.png"
        onClicked: command.state(stat.STATE_ON)
    }
}
