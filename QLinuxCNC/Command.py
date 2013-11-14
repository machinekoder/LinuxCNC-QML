# -*- coding: utf-8 -*-
import linuxcnc

from PyQt5.QtCore import pyqtSlot, pyqtSignal, pyqtProperty
from PyQt5.QtQuick import QQuickItem


class Command(QQuickItem):
    def __init__(self, parent=None):
        super(QQuickItem, self).__init__(parent)

        self._serial = 0

        self.c = linuxcnc.command()
        self.setSerial(self.c.serial)

    @pyqtSlot()
    def abort(self):
        self.c.abort()

    @pyqtSlot(int, name="auto")
    def auto1(self, param1):
        self.c.auto(param1)

    @pyqtSlot(int, int, name="auto")
    def auto2(self, param1, param2):
        self.c.auto(param1, param2)

    @pyqtSlot(int)
    def brake(self, param1):
        self.c.brake(param1)

    @pyqtSlot(int)
    def debug(self, param1):
        self.c.debug(param1)

    @pyqtSlot(float)
    def feedrate(self, param1):
        self.c.feedrate(param1)

    @pyqtSlot(int)
    def flood(self, param1):
        self.c.flood(param1)

    @pyqtSlot(int)
    def home(self, param1):
        self.c.home(param1)

    @pyqtSlot(int, int, name="jog")
    def jog1(self, param1, param2):
        self.c.jog(param1, param2)

    @pyqtSlot(int, int, int, name="jog")
    def jog2(self, param1, param2, param3):
        self.c.jog(param1, param2, param3)

    @pyqtSlot(int, int, int, int, name="jog")
    def jog3(self, param1, param2, param3, param4):
        self.c.jog(param1, param2, param3, param4)

    @pyqtSlot()
    def loadToolTable(self):
        self.c.load_tool_table()

    @pyqtSlot(float)
    def maxvel(self, param1):
        self.c.maxvel(param1)

    @pyqtSlot('QString')
    def mdi(self, param1):
        self.c.mdi(param1)

    @pyqtSlot(int)
    def mist(self, param1):
        self.c.mist(param1)

    @pyqtSlot()
    def overrideLimits(self):
        self.c.override_limits()

    @pyqtSlot('QString')
    def programOpen(self, param1):
        self.c.program_open(param1)

    @pyqtSlot()
    def resetInterpreter(self):
        self.c.reset_interpreter()

    @pyqtSlot(int)
    def setAdaptiveFeed(self, param1):
        self.c.set_adaptive_feed(param1)

    @pyqtSlot(int, float)
    def setAnalogOutput(self, param1, param2):
        self.c.set_analog_output(param1, param2)

    @pyqtSlot(int)
    def setBlockDelete(self, param1):
        self.c.set_block_delete(param1)

    @pyqtSlot(int, int)
    def setDigitalOutput(self, param1, param2):
        self.c.set_digital_output(param1, param2)

    @pyqtSlot(int)
    def setFeedHold(self, param1):
        self.c.set_feed_hold(param1)

    @pyqtSlot(int)
    def setFeedOverride(self, param1):
        self.c.set_feed_override(param1)

    @pyqtSlot(int, float)
    def setMaxLimit(self, param1, param2):
        self.c.set_max_limit(param1, param2)

    @pyqtSlot(int, float)
    def setMinLimit(self, param1, param2):
        self.c.set_min_limit(param1, param2)

    @pyqtSlot(int)
    def setOptionalStop(self, param1):
        self.c.set_option_stop(param1)

    @pyqtSlot(int)
    def setSpindleOverride(self, param1):
        self.c.set_spindle_override(param1)

    @pyqtSlot(int)
    def spindle(self, param1):
        self.c.spindle(param1)

    @pyqtSlot(float)
    def spindleoverride(self, param1):
        self.c.spindleoverride(param1)

    @pyqtSlot(int)
    def state(self, param1):
        self.c.state(param1)

    @pyqtSlot(int)
    def teleopEnabled(self, param1):
        self.c.teleop_enable(param1)

    @pyqtSlot(float, float, float, name="teleopVector")
    def teleopVector1(self, param1, param2, param3):
        self.c.teleop_vector(param1, param2, param3)

    @pyqtSlot(float, float, float, float, name="teleopVector")
    def teleopVector2(self, param1, param2, param3, param4):
        self.c.teleop_vector(param1, param2, param3, param4)

    @pyqtSlot(float, float, float, float, float, name="teleopVector")
    def teleopVector3(self, param1, param2, param3, param4, param5):
        self.c.teleop_vector(param1, param2, param3, param4, param5)

    @pyqtSlot(float, float, float, float, float, float, name="teleopVector")
    def teleopVector4(self, param1, param2, param3, param4, param5, param6):
        self.c.teleop_vector(param1, param2, param3, param4, param5, param6)

    @pyqtSlot(int, float, float, float, float, float, int)
    def toolOffset(self, param1, param2, param3, param4, param5, param6,
                  param7):
        self.c.tool_offset(param1, param2, param3, param4, param5, param6)

    @pyqtSlot(int)
    def trajMode(self, param1):
        self.c.traj_mode(param1)

    @pyqtSlot(int)
    def unhome(self, param1):
        self.c.unhome(param1)

    @pyqtSlot(name="waitComplete")
    def waitComplete1(self):
        self.c.wait_complete()

    @pyqtSlot(float, name="waitComplete")
    def waitComplete2(self, param1):
        self.c.wait_complete(param1)

    # serial Property
    serialChanged = pyqtSignal(int)

    def getSerial(self):
        return self._serial

    def setSerial(self, serial):
        if (self._serial != serial):
            self._serial = serial
            self.serialChanged.emit(self._serial)

    serial = pyqtProperty(int,
                            getSerial,
                            notify=serialChanged)
