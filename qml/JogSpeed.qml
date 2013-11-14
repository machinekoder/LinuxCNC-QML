import QtQuick 2.0
import QtQuick.Controls 1.0

Rectangle {
    id: jogSpeedGroup

    color: "#00000000"

    JogSpeedSelector {
        id: xAxisSelector

        height: 30
        anchors { top: parent.top; topMargin: 5; right: parent.right; rightMargin: 5; leftMargin: 5 }
        title: qsTr("X:")
    }

    JogSpeedSelector {
        id: yAxisSelector

        height: 30
        anchors { top: xAxisSelector.bottom; topMargin: 5; right: parent.right; rightMargin: 5; left: parent.left; leftMargin: 5 }
        title: qsTr("Y:")
    }

    JogSpeedSelector {
        id: zAxisSelector

        height: 30
        anchors { top: yAxisSelector.bottom; topMargin: 5; right: parent.right; rightMargin: 5; left: parent.left; leftMargin: 5 }
        title: qsTr("Z:")
    }

    JogSpeedSelector {
        id: aAxisSelector

        height: 30
        anchors { top: zAxisSelector.bottom; topMargin: 5; right: parent.right; rightMargin: 5; left: parent.left; leftMargin: 5 }
        title: qsTr("A:")
    }
}
