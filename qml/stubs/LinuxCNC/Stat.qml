import QtQuick 2.0

Rectangle {
    property list<Axis> axis
    property double actualPosition
    property bool homed



    readonly property int autoPause: 0 ; //AUTO_PAUSE: 0
    /* constant mockups */
    /*property int AUTO_PAUSE: 0
    property int AUTO_RESUME: 1
    property int AUTO_RUN: 2
    property int AUTO_STEP: 3*/


    function poll()
    {

    }
}
