import QtQuick 2.0
import QtQuick.Controls 1.0

Rectangle {
    id: main

    property string title: "Title:"
    property string unit: "mm/s"
    property double speed: speedSlider.value
    property double minimumValue: 0
    property double maximumValue: 1000
    property double stepSize: 10

    function setSpeed(speed)
    {
        speedSlider.value = speed
    }

    width: 250
    height: 30
    color: "#00000000"

        Text {
                    id: titleLabel
                    text: main.title
                    verticalAlignment: Text.AlignVCenter
                    anchors.top: parent.top
                    anchors.topMargin: 0
                    anchors.bottom: parent.bottom
                    anchors.bottomMargin: 0
                    anchors.left: parent.left
                    anchors.leftMargin: 0
                    font.pixelSize: 12
                }

        Slider {
                    id: speedSlider
                    anchors.right: speedSpin.left
                    anchors.rightMargin: 5
                    anchors.top: parent.top
                    anchors.topMargin: 0
                    anchors.bottom: parent.bottom
                    anchors.bottomMargin: 0
                    anchors.left: titleLabel.right
                    anchors.leftMargin: 5
                    minimumValue: main.minimumValue
                    maximumValue: main.maximumValue
                    stepSize: main.stepSize
                    onValueChanged: {
                        speedSpin.value = value
                    }
            }

        SpinBox {
            id: speedSpin
            width: parent.width * 0.3
            anchors.top: parent.top
            anchors.topMargin: 0
            anchors.bottom: parent.bottom
            anchors.bottomMargin: 0
            anchors.right: parent.right
            anchors.rightMargin: 0
            maximumValue: main.maximumValue
            minimumValue: main.minimumValue
            stepSize: main.stepSize
            suffix: main.unit
            onValueChanged: {
                speedSlider.value = value
            }
        }
}
