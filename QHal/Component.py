# -*- coding: utf-8 -*-
import hal

from . import Pin

from PyQt5.QtCore import pyqtSlot, pyqtSignal, pyqtProperty
from PyQt5.QtQuick import QQuickItem
from PyQt5.QtQml import QQmlListProperty


class Component(QQuickItem):
    def __init__(self, parent=None):
        super(QQuickItem, self).__init__(parent)

        # Initialise the value of the properties.
        self._name = ""

    @pyqtProperty('QString')
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name
        self.h = hal.component(self._name)

    @pyqtProperty(QQmlListProperty)
    def pins(self):
        return QQmlListProperty(Pin, self,
                append=lambda pie_ch, pie_sl: pie_sl.setParentItem(pie_ch))