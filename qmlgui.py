#!/usr/bin/env python

import sys

from PyQt5.QtCore import QUrl
from PyQt5.QtQml import qmlRegisterType
from PyQt5.QtQuick import QQuickView
from PyQt5.QtWidgets import QApplication

import QLinuxCNC.Stat as Stat
import QLinuxCNC.Axis as Axis
import QLinuxCNC.Command as Command
import QLinuxCNC.ErrorChannel as ErrorChannel


def main():
    app = QApplication(sys.argv)

    # Register the Python type.
    # qmlRegisterType(Hal.Component, 'Hal', 1, 0, 'Component')
    # qmlRegisterType(Hal.Pin, 'Hal', 1, 0, 'Pin')
    qmlRegisterType(Stat.Stat, 'LinuxCNC', 1, 0, 'Stat')
    qmlRegisterType(Axis.Axis, 'LinuxCNC', 1, 0, 'Axis')
    qmlRegisterType(Command.Command, 'LinuxCNC', 1, 0, 'Command')
    qmlRegisterType(ErrorChannel.ErrorChannel, 'LinuxCNC', 1, 0, 'ErrorChannel')

    quickview = QQuickView()

    quickview.setSource(QUrl('gui/qml/main.qml'))
    quickview.showFullScreen()

    quickview.engine().quit.connect(app.quit)

    app.exec_()

if __name__ == "__main__":
    main()
