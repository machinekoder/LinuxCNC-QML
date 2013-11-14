# -*- coding: utf-8 -*-
import hal

from PyQt5.QtCore import pyqtSlot, pyqtSignal, pyqtProperty
from PyQt5.QtQuick import QQuickItem


class Pin(QQuickItem):
    def __init__(self, parent=None):
        super(QQuickItem, self).__init__(parent)

        self._name = ""

    @pyqtProperty('QString')
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name
        self.h = hal.component(name)