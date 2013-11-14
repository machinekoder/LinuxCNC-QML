import QtQuick 2.0
import QtQuick.Controls 1.0

Rectangle {
    id: jogConrolGroup

    color: "#00000000"
    width: 250; height: 220

    VirtualJoystick {
        id: xyStick

        anchors.left: parent.left
        anchors.leftMargin: 10
        anchors.top: parent.top
        anchors.topMargin: 10
    }

    /*TouchButton {
        id: xPlusButton

        width: 50; height: 50
        anchors { top: yPlusButton.bottom; topMargin: 5; left: homeAllButton.right; leftMargin: 5}
        text: ""
        iconSource: "icons/go-next.png"

        onPressedChanged: {
            if (pressed)
            {
                command.jog(stat.JOG_CONTINUOUS, 0, xSpeedSpin.value)
            }
            else
            {
                command.jog(stat.JOG_STOP, 0)
            }
        }
    }

    TouchButton {
        id: yPlusButton

        width: 50; height: 50
        anchors { top: parent.top; topMargin: 5; horizontalCenter: homeAllButton.horizontalCenter }
        text: ""
        iconSource: "icons/go-up.png"

        onPressedChanged: {
            if (pressed)
            {
                command.jog(stat.JOG_CONTINUOUS, 1, ySpeedSpin.value)
            }
            else
            {
                command.jog(stat.JOG_STOP, 1)
            }
        }
    }

    TouchButton {
        id: zPlusButton

        width: 50; height: 50
        anchors { left: xPlusButton.right; leftMargin: 10; verticalCenter: yPlusButton.verticalCenter }
        text: ""
        iconSource: "icons/arrow-up.png"

        onPressedChanged: {
            if (pressed)
            {
                command.jog(stat.JOG_CONTINUOUS, 2, zSpeedSpin.value)
            }
            else
            {
                command.jog(stat.JOG_STOP, 2)
            }
        }
    }

    TouchButton {
        id: zMinusButton

        width: 50; height: 50
        anchors { left: xPlusButton.right; leftMargin: 10; verticalCenter: yMinusButton.verticalCenter }
        text: ""
        iconSource: "icons/arrow-down.png"

        onPressedChanged: {
            if (pressed)
            {
                command.jog(stat.JOG_CONTINUOUS, 2, -zSpeedSpin.value)
            }
            else
            {
                command.jog(stat.JOG_STOP, 2)
            }
        }
    }

    TouchButton {
        id: xMinusButton

        width: 50; height: 50
        anchors { top: yPlusButton.bottom; topMargin: 5; left: parent.left; leftMargin: 5 }
        text: ""
        iconSource: "icons/go-previous.png"

        onPressedChanged: {
            if (pressed)
            {
                command.jog(stat.JOG_CONTINUOUS, 0, -xSpeedSpin.value)
            }
            else
            {
                command.jog(stat.JOG_STOP, 0)
            }
        }
    }

    TouchButton {
        id: yMinusButton

        width: 50; height: 50
        anchors { horizontalCenter: homeAllButton.horizontalCenter; top: homeAllButton.bottom; topMargin: 5 }
        text: ""
        iconSource: "icons/go-down.png"

        onPressedChanged: {
            if (pressed)
            {
                command.jog(stat.JOG_CONTINUOUS, 1, -ySpeedSpin.value)
            }
            else
            {
                command.jog(stat.JOG_STOP, 1)
            }
        }
    }

    TouchButton {
        id: homeAllButton

        width: 50; height: 50
        anchors { top: yPlusButton.bottom; topMargin: 5; left: xMinusButton.right; leftMargin: 5 }
        text: ""
        iconSource: "icons/go-home.png"
    }

    TouchButton {
        id: homeXButton

        width: 50; height: 50
        anchors { right: yMinusButton.left; rightMargin: 5; top: xMinusButton.bottom; topMargin: 5 }
        text: ""
        iconSource: "icons/go-home.png"
    }

    TouchButton {
        id: homeYButton

        width: 50; height: 50
        anchors { left: yMinusButton.right; leftMargin: 5; top: xPlusButton.bottom; topMargin: 5 }
        text: ""
        iconSource: "icons/go-home.png"
    }

    TouchButton {
        id: homeZButton

        width: 50; height: 50
        anchors { left: xPlusButton.right; leftMargin: 10; top: zPlusButton.bottom; topMargin: 5 }
        text: ""
        iconSource: "icons/go-home.png"
    }

    TouchButton {
        id: extruderPlusButton

        width: 50; height: 50
        anchors { bottom: extruderMinusButton.top; bottomMargin: 5; left: homeZButton.right; leftMargin: 10 }
        text: ""
        iconSource: "icons/list-add.png"
    }

    TouchButton {
        id: extruderMinusButton

        width: 50; height: 50
        anchors { bottom: zMinusButton.bottom; bottomMargin: 0; left: zMinusButton.right; leftMargin: 10}
        text: ""
        iconSource: "icons/list-remove.png"
    }*/

    CheckBox {
        id: continousCheck

        anchors { top: xyStick.bottom; topMargin: 5; left: parent.left; leftMargin: 5 }
        text: qsTr("Continous")
        checked: true
    }

    CheckBox {
        id: mistCheck

        anchors { left: continousCheck.right; leftMargin: 5; top: xyStick.bottom; topMargin: 5 }
        text: qsTr("Mist")
    }

    CheckBox {
        id: floodCheck

        anchors { left: mistCheck.right; leftMargin: 5; top: xyStick.bottom; topMargin: 5 }
        text: qsTr("Flood")
    }
}
