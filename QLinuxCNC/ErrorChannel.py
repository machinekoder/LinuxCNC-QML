# -*- coding: utf-8 -*-
import linuxcnc

from PyQt5.QtCore import pyqtSlot, pyqtSignal, pyqtProperty
from PyQt5.QtQuick import QQuickItem


class ErrorChannel(QQuickItem):
    def __init__(self, parent=None):
        super(QQuickItem, self).__init__(parent)

        self._errorType = 0
        self._errorText = ""

        self.e = linuxcnc.error_channel()

    @pyqtSlot()
    def poll(self):
        error = self.e.poll()
        if error:
            kind, text = error
            self.setErrorType(kind)
            self.setErrorText(text)

    # errorType Property
    errorTypeChanged = pyqtSignal(int)

    def getErrorType(self):
        return self._errorType

    def setErrorType(self, errorType):
        if (self._errorType != errorType):
            self._errorType = errorType
            self.errorTypeChanged.emit(self._errorType)

    errorType = pyqtProperty(int,
                            getErrorType,
                            notify=errorTypeChanged)

    # errorText Property
    errorTextChanged = pyqtSignal('QString')

    def getErrorText(self):
        return self._errorText

    def setErrorText(self, errorText):
        if (self._errorText != errorText):
            self._errorText = errorText
            self.errorTextChanged.emit(self._errorText)

    errorText = pyqtProperty('QString',
                            getErrorText,
                            notify=errorTextChanged)