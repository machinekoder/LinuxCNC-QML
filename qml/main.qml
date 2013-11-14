import QtQuick 2.1
import QtQuick.Controls 1.0
import LinuxCNC 1.0 as LinuxCNC

ApplicationWindow {
    id: mainRect

    width: 800; height: 500

    LinuxCNC.Stat {
        id: stat
        axis: [
                LinuxCNC.Axis {
                    id: xAxis
                },
                 LinuxCNC.Axis {
                    id: yAxis
                },
                 LinuxCNC.Axis {
                    id: zAxis
                }
            ]
    }
    LinuxCNC.Command {
        id: command
    }
    LinuxCNC.ErrorChannel {
        id: errorChannel
    }

    //HalComponent {
    //    id: halComponent
    //    name: "testComponent"
    //    pins: [ HalPin { id: pin1; name: "in" } ]
    //}
    Timer {
        id: updateTimer

        running: true
        repeat: true
        interval: 1000

        onTriggered: {
            stat.poll()
            errorChannel.poll()
        }
    }

    Image {
        id: backgroundImage

        anchors.fill: parent
        source: "images/light_alu.png"
        fillMode: Image.Tile
    }

    menuBar: MenuBar {
        Menu {
            title: qsTr("File")

            MenuItem { text: qsTr("Exit"); iconSource: "icons/application-exit.png"; onTriggered: Qt.quit() }
        }
    }

    GroupBox {
        id: temperatureControl

        width: 161; height: 291
        anchors { top: parent.top; topMargin: 10; right: parent.right; rightMargin: 10 }
        title: qsTr("Temperature Control")

        TemperatureControl {
            anchors.fill: parent
        }
    }

    GroupBox {
        id: machineControl

        title: qsTr("Machine Control")
        width: parent.width * 0.3; height: parent.height * 0.15
        anchors { top: parent.top; topMargin: 10; left: parent.left; leftMargin: 10 }

        MachineControl {
            anchors.fill: parent
        }
    }

    TabView {
        id: tabView

        width: parent.width * 0.3; height: parent.height * 0.7
        anchors { top: machineControl.bottom; topMargin: 10; left: parent.left; leftMargin: 10 }

        Tab { source: "ManualControl.qml"; title: qsTr("Manual") }
        Tab { source: "GCodeControl.qml"; title: qsTr("MDI") }
    }

    Text {
        id: titleLabel

        anchors { bottom: parent.bottom; bottomMargin: 10; right: parent.right; rightMargin: 10 }
        text: qsTr("LinuxCNC")
        font.bold: true
        font.pointSize: 30
    }

    GroupBox {
        id: autoControl

        title: qsTr("Auto")
        width: 260; height: 75
        anchors { left: machineControl.right; leftMargin: 10; top: parent.top; topMargin: 10 }

        AutoControl {
            anchors.fill: parent
        }
    }

    TabView {
        id: middleTabView

        width: 260; height: 240
        anchors { left: machineControl.right; leftMargin: 10; top: autoControl.bottom; topMargin: 10 }

        Tab { source: "StatusControl.qml"; title: qsTr("Status") }
    }
}
