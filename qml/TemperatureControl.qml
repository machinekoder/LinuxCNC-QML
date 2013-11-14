import QtQuick 2.0
import QtQuick.Controls 1.0

Rectangle {
    id: group_box1

    color: "#00000000"
    height: 200
    width: 200

    TemperatureSelector {
        id: temperatureSelector1
        title: "Extruder"
        anchors.bottom: parent.bottom
        anchors.bottomMargin: 0
        anchors.top: parent.top
        anchors.topMargin: 0
        anchors.left: parent.left
        anchors.leftMargin: 0
    }
    TemperatureSelector {
        id: temperatureSelector2
        criticalTempValue: 150
        currentValue: 40
        highTempValue: 120
        maximumValue: 150
        title: "Bed"
        anchors.top: parent.top
        anchors.topMargin: 0
        anchors.left: temperatureSelector1.right
        anchors.leftMargin: 5
        anchors.bottom: parent.bottom
        anchors.bottomMargin: 0
    }
}
