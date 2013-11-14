import QtQuick 2.0
import QtQuick.Controls 1.0

Rectangle {
    id: statusGroup

    color: "#00000000"

    CheckBox {
        id: homedCheck
        x: -10
        y: -171
        text: "Homed"
        checked: stat.homed
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.top: parent.top
        anchors.topMargin: 10
    }

    Text {
        id: commandText
        x: -74
        y: -142
        text: "Command: " + stat.command //"Acceleration: "// + linuxcnc.acceleration //+ "\nFeedrate: " + linuxcnc.feedrate
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.top: homedCheck.bottom
        anchors.topMargin: 10
    }

    Text {
        id: positionText
        x: -97
        y: -118
        text: "X: " + stat.actualPosition[0]
        + "<br>Y: " + stat.actualPosition[1]
        + "<br>Z: " + stat.actualPosition[2]
        + "<br>Vel: " + stat.velocity
        + "<br>DTG: " + stat.dtg[0]
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.top: commandText.bottom
        anchors.topMargin: 10
    }

    Text {
        id: statusText
        text: "Status: " + (stat.state === stat.RCS_DONE)?"RCS_DONE":(stat.state === stat.RCS_EXEC)?"RCS_EXEC":"RCS_ERROR"
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.top: positionText.bottom
        anchors.topMargin: 10
    }

    Text {
        id: taskStateText
        text: "Task Status: " + (stat.taskState === stat.STATE_ESTOP)?"STATE_ESTOP":(stat.taskState === stat.STATE_ESTOP_RESET)?"STATE_ESTOP_RESET":(stat.taskState === stat.STATE_ON)?"STATE_ON":"STATE_OFF"
        anchors.horizontalCenterOffset: 0
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.top: statusText.bottom
        anchors.topMargin: 10
    }

    Text {
        id: modeText
        text: "Mode: " + (stat.mode === stat.MODE_MDI)?"MODE_MDI":(stat.mode === stat.MODE_AUTO)?"MODE_AUTO":"MODE_MANUAL"
        anchors.horizontalCenterOffset: 0
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.top: taskStateText.bottom
        anchors.topMargin: 10
    }


}
