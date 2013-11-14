import QtQuick 2.0

Rectangle {
    width: 100
    height: 62


    Hal.Component {
        id: whatever
        name: "passtrough"
        pins: [
            Hal.Pin {
                id: inPin
                name: "in"
                type: Hal.float
                direction: Hal.out
            },
            Hal.Pin {
                id: outPin
                name: "out"
                type: Hal.float
                direction: Hal.out
                value: inPin.value
            }
        ]
    }
}
