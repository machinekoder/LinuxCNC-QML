# -*- coding: utf-8 -*-
from PyQt5.QtCore import pyqtSignal, pyqtProperty
from PyQt5.QtQuick import QQuickItem


class Axis(QQuickItem):
    def __init__(self, parent=None):
        super(QQuickItem, self).__init__(parent)

        self._axisType = 0
        self._backlash = 0.0
        self._enabled = 0
        self._fault = 0
        self._ferrorCurrent = 0.0
        self._ferrorHighmark = 0.0
        self._homed = 0
        self._homing = 0
        self._inpos = 0
        self._inputPosition = 0.0
        self._maxFerror = 0.0
        self._maxHardLimit = 0
        self._maxPositionLimit = 0.0
        self._maxSoftLimit = 0
        self._minFerror = 0.0
        self._minHardLimit = 0
        self._minPositionLimit = 0.0
        self._minSoftLimit = 0
        self._output = 0.0
        self._overrideLimits = 0
        self._units = 0.0
        self._velocity = 0.0

    # axisType Property
    axisTypeChanged = pyqtSignal(int)

    def getAxisType(self):
        return self._axisType

    def setAxisType(self, axisType):
        if (self._axisType != axisType):
            self._axisType = axisType
            self.axisTypeChanged.emit(self._axisType)

    axisType = pyqtProperty(int,
                            getAxisType,
                            notify=axisTypeChanged)

    # backlash Property
    backlashChanged = pyqtSignal(float)

    def getBacklash(self):
        return self._backlash

    def setBacklash(self, backlash):
        if (self._backlash != backlash):
            self._backlash = backlash
            self.backlashChanged.emit(self._backlash)

    backlash = pyqtProperty(float,
                            getBacklash,
                            notify=backlashChanged)

    # enabled Property
    enabledChanged = pyqtSignal(int)

    def getEnabled(self):
        return self._enabled

    def setEnabled(self, enabled):
        if (self._enabled != enabled):
            self._enabled = enabled
            self.enabledChanged.emit(self._enabled)

    enabled = pyqtProperty(int,
                            getEnabled,
                            notify=enabledChanged)

    # fault Property
    faultChanged = pyqtSignal(int)

    def getFault(self):
        return self._fault

    def setFault(self, fault):
        if (self._fault != fault):
            self._fault = fault
            self.faultChanged.emit(self._fault)

    fault = pyqtProperty(int,
                            getFault,
                            notify=faultChanged)

    # ferrorCurrent Property
    ferrorCurrentChanged = pyqtSignal(float)

    def getFerrorCurrent(self):
        return self._ferrorCurrent

    def setFerrorCurrent(self, ferrorCurrent):
        if (self._ferrorCurrent != ferrorCurrent):
            self._ferrorCurrent = ferrorCurrent
            self.ferrorCurrentChanged.emit(self._ferrorCurrent)

    ferrorCurrent = pyqtProperty(float,
                            getFerrorCurrent,
                            notify=ferrorCurrentChanged)

    # ferrorHighmark Property
    ferrorHighmarkChanged = pyqtSignal(float)

    def getFerrorHighmark(self):
        return self._ferrorHighmark

    def setFerrorHighmark(self, ferrorHighmark):
        if (self._ferrorHighmark != ferrorHighmark):
            self._ferrorHighmark = ferrorHighmark
            self.ferrorHighmarkChanged.emit(self._ferrorHighmark)

    ferrorHighmark = pyqtProperty(float,
                            getFerrorHighmark,
                            notify=ferrorHighmarkChanged)

    # homed Property
    homedChanged = pyqtSignal(int)

    def getHomed(self):
        return self._homed

    def setHomed(self, homed):
        if (self._homed != homed):
            self._homed = homed
            self.homedChanged.emit(self._homed)

    homed = pyqtProperty(int,
                            getHomed,
                            notify=homedChanged)

    # homing Property
    homingChanged = pyqtSignal(int)

    def getHoming(self):
        return self._homing

    def setHoming(self, homing):
        if (self._homing != homing):
            self._homing = homing
            self.homingChanged.emit(self._homing)

    homing = pyqtProperty(int,
                            getHoming,
                            notify=homingChanged)

    # inpos Property
    inposChanged = pyqtSignal(int)

    def getInpos(self):
        return self._inpos

    def setInpos(self, inpos):
        if (self._inpos != inpos):
            self._inpos = inpos
            self.inposChanged.emit(self._inpos)

    inpos = pyqtProperty(int,
                            getInpos,
                            notify=inposChanged)

    # inputPosition Property
    inputPositionChanged = pyqtSignal(float)

    def getInputPosition(self):
        return self._inputPosition

    def setInputPosition(self, inputPosition):
        if (self._inputPosition != inputPosition):
            self._inputPosition = inputPosition
            self.inputPositionChanged.emit(self._inputPosition)

    inputPosition = pyqtProperty(float,
                            getInputPosition,
                            notify=inputPositionChanged)

    # maxFerror Property
    maxFerrorChanged = pyqtSignal(float)

    def getMaxFerror(self):
        return self._maxFerror

    def setMaxFerror(self, maxFerror):
        if (self._maxFerror != maxFerror):
            self._maxFerror = maxFerror
            self.maxFerrorChanged.emit(self._maxFerror)

    maxFerror = pyqtProperty(float,
                            getMaxFerror,
                            notify=maxFerrorChanged)

    # maxHardLimit Property
    maxHardLimitChanged = pyqtSignal(int)

    def getMaxHardLimit(self):
        return self._maxHardLimit

    def setMaxHardLimit(self, maxHardLimit):
        if (self._maxHardLimit != maxHardLimit):
            self._maxHardLimit = maxHardLimit
            self.maxHardLimitChanged.emit(self._maxHardLimit)

    maxHardLimit = pyqtProperty(int,
                            getMaxHardLimit,
                            notify=maxHardLimitChanged)

    # maxPositionLimit Property
    maxPositionLimitChanged = pyqtSignal(float)

    def getMaxPositionLimit(self):
        return self._maxPositionLimit

    def setMaxPositionLimit(self, maxPositionLimit):
        if (self._maxPositionLimit != maxPositionLimit):
            self._maxPositionLimit = maxPositionLimit
            self.maxPositionLimitChanged.emit(self._maxPositionLimit)

    maxPositionLimit = pyqtProperty(float,
                            getMaxPositionLimit,
                            notify=maxPositionLimitChanged)

    # maxSoftLimit Property
    maxSoftLimitChanged = pyqtSignal(int)

    def getMaxSoftLimit(self):
        return self._maxSoftLimit

    def setMaxSoftLimit(self, maxSoftLimit):
        if (self._maxSoftLimit != maxSoftLimit):
            self._maxSoftLimit = maxSoftLimit
            self.maxSoftLimitChanged.emit(self._maxSoftLimit)

    maxSoftLimit = pyqtProperty(int,
                            getMaxSoftLimit,
                            notify=maxSoftLimitChanged)

    # minFerror Property
    minFerrorChanged = pyqtSignal(float)

    def getMinFerror(self):
        return self._minFerror

    def setMinFerror(self, minFerror):
        if (self._minFerror != minFerror):
            self._minFerror = minFerror
            self.minFerrorChanged.emit(self._minFerror)

    minFerror = pyqtProperty(float,
                            getMinFerror,
                            notify=minFerrorChanged)

    # minHardLimit Property
    minHardLimitChanged = pyqtSignal(int)

    def getMinHardLimit(self):
        return self._minHardLimit

    def setMinHardLimit(self, minHardLimit):
        if (self._minHardLimit != minHardLimit):
            self._minHardLimit = minHardLimit
            self.minHardLimitChanged.emit(self._minHardLimit)

    minHardLimit = pyqtProperty(int,
                            getMinHardLimit,
                            notify=minHardLimitChanged)

    # minPositionLimit Property
    minPositionLimitChanged = pyqtSignal(float)

    def getMinPositionLimit(self):
        return self._minPositionLimit

    def setMinPositionLimit(self, minPositionLimit):
        if (self._minPositionLimit != minPositionLimit):
            self._minPositionLimit = minPositionLimit
            self.minPositionLimitChanged.emit(self._minPositionLimit)

    minPositionLimit = pyqtProperty(float,
                            getMinPositionLimit,
                            notify=minPositionLimitChanged)

    # minSoftLimit Property
    minSoftLimitChanged = pyqtSignal(int)

    def getMinSoftLimit(self):
        return self._minSoftLimit

    def setMinSoftLimit(self, minSoftLimit):
        if (self._minSoftLimit != minSoftLimit):
            self._minSoftLimit = minSoftLimit
            self.minSoftLimitChanged.emit(self._minSoftLimit)

    minSoftLimit = pyqtProperty(int,
                            getMinSoftLimit,
                            notify=minSoftLimitChanged)

    # output Property
    outputChanged = pyqtSignal(float)

    def getOutput(self):
        return self._output

    def setOutput(self, output):
        if (self._output != output):
            self._output = output
            self.outputChanged.emit(self._output)

    output = pyqtProperty(float,
                            getOutput,
                            notify=outputChanged)

    # overrideLimits Property
    overrideLimitsChanged = pyqtSignal(int)

    def getOverrideLimits(self):
        return self._overrideLimits

    def setOverrideLimits(self, overrideLimits):
        if (self._overrideLimits != overrideLimits):
            self._overrideLimits = overrideLimits
            self.overrideLimitsChanged.emit(self._overrideLimits)

    overrideLimits = pyqtProperty(int,
                            getOverrideLimits,
                            notify=overrideLimitsChanged)

    # units Property
    unitsChanged = pyqtSignal(float)

    def getUnits(self):
        return self._units

    def setUnits(self, units):
        if (self._units != units):
            self._units = units
            self.unitsChanged.emit(self._units)

    units = pyqtProperty(float,
                            getUnits,
                            notify=unitsChanged)

    # velocity Property
    velocityChanged = pyqtSignal(float)

    def getVelocity(self):
        return self._velocity

    def setVelocity(self, velocity):
        if (self._velocity != velocity):
            self._velocity = velocity
            self.velocityChanged.emit(self._velocity)

    velocity = pyqtProperty(float,
                            getVelocity,
                            notify=velocityChanged)