# -*- coding: utf-8 -*-
import linuxcnc

from PyQt5.QtCore import pyqtSlot, pyqtSignal, pyqtProperty
from PyQt5.QtQuick import QQuickItem
from PyQt5.QtQml import QQmlListProperty

from .Axis import Axis


class Stat(QQuickItem):
    def __init__(self, parent=None):
        super(QQuickItem, self).__init__(parent)

        # Initialise the value of the properties.
        self.s = linuxcnc.stat()  # create a connection to the status channel
        self._acceleration = 0.0
        self._activeQueue = 0
        self._actualPosition = ()
        self._adaptiveFeedEnabled = True
        self._ain = ()
        self._angularUnits = 0.0
        self._aout = ()
        self._axes = 0
        self._axis = []
        self._axisTemp = (0, 0, 0, 0, 0, 0, 0, 0, 0)
        self._axisMask = 0
        self._blockDelete = 0
        self._command = ""
        self._currentLine = 0
        self._currentVel = 0.0
        self._cycleTime = 0.0
        self._debug = 0
        self._delayLeft = 0.0
        self._din = ()
        self._distanceToGo = 0.0
        self._dout = ()
        self._dtg = ()
        self._echoSerialNumber = 0
        self._enabled = 0
        self._estop = 0
        self._execState = 0
        self._feedHoldEnabled = 0
        self._feedOverrideEnabled = 0
        self._feedrate = 0.0
        self._fileName = ""
        self._flood = 0
        self._g5xIndex = 0
        self._g5xOffset = ()
        self._g92Offset = ()
        self._gcodes = ()
        self._homed = 0
        self._motionId = 0
        self._inpos = 0
        self._inputTimeout = 0
        self._interpState = 0
        self._interpreterErrcode = 0
        self._jointActualPosition = ()
        self._jointPosition = ()
        self._kinematicsType = 0
        self._limit = ()
        self._linearUnits = 0.0
        self._lube = 0
        self._lubeLevel = 0
        self._maxAcceleration = 0.0
        self._maxVelocity = 0.0
        self._mcodes = ()
        self._mist = 0
        self._motionLine = 0
        self._motionMode = 0
        self._motionType = 0
        self._optionalStop = 0
        self._paused = 0
        self._pocketPrepped = 0
        self._position = ()
        self._probeTripped = 0
        self._probeVal = 0
        self._probedPosition = ()
        self._probing = 0
        self._programUnits = 0
        self._queue = 0
        self._queueFull = 0
        self._readLine = 0
        self._rotationXY = 0.0
        self._settings = ()
        self._spindleBrake = 0
        self._spindleDirection = 0
        self._spindleEnabled = 0
        self._spindleIncreasing = 0
        self._spindleOverrideEnabled = 0
        self._spindleSpeed = 0.0
        self._spindlerate = 0.0
        self._state = 0
        self._taskMode = 0
        self._taskPaused = 0
        self._taskState = 0
        self._toolInSpindle = 0
        self._toolOffset = ()
        self._toolTable = ()
        self._velocity = 0.0

    @pyqtSlot()
    def poll(self):
        try:
            self.s.poll()  # get current values
            self.setAcceleration(self.s.acceleration)
            self.setActiveQueue(self.s.active_queue)
            self.setActualPosition(self.s.actual_position)
            self.setAdaptiveFeedEnabled(self.s.adaptive_feed_enabled)
            self.setAin(self.s.ain)
            self.setAngularUnits(self.s.angular_units)
            self.setAout(self.s.aout)
            self.setAxes(self.s.axes)
            self.setAxisMask(self.s.axis_mask)
            self.setBlockDelete(self.s.block_delete)
            self.setCommand(self.s.command)
            self.setCurrentLine(self.s.current_line)
            self.setCurrentVel(self.s.current_vel)
            self.setCycleTime(self.s.cycle_time)
            self.setDebug(self.s.debug)
            self.setDelayLeft(self.s.delay_left)
            self.setDin(self.s.din)
            self.setDistanceToGo(self.s.distance_to_go)
            self.setDout(self.s.dout)
            self.setDtg(self.s.dtg)
            self.setEchoSerialNumber(self.s.echo_serial_number)
            self.setEnabled(self.s.enabled)
            self.setEstop(self.s.estop)
            self.setExecState(self.s.exec_state)
            self.setFeedHoldEnabled(self.s.feed_hold_enabled)
            self.setFeedOverrideEnabled(self.s.feed_override_enabled)
            self.setFeedrate(self.s.feedrate)
            self.setFileName(self.s.file)
            self.setFlood(self.s.flood)
            self.setG5xIndex(self.s.g5x_index)
            self.setG5xOffset(self.s.g5x_offset)
            self.setG92Offset(self.s.g92_offset)
            self.setGcodes(self.s.gcodes)
            self.setHomed(self.s.homed)
            self.setMotionId(self.s.id)
            self.setInpos(self.s.inpos)
            self.setInputTimeout(self.s.input_timeout)
            self.setInterpState(self.s.interp_state)
            self.setInterpreterErrcode(self.s.interpreter_errcode)
            self.setJointActualPosition(self.s.joint_actual_position)
            self.setJointPosition(self.s.joint_position)
            self.setKinematicsType(self.s.kinematics_type)
            self.setLimit(self.s.limit)
            self.setLinearUnits(self.s.linear_units)
            self.setLube(self.s.lube)
            self.setLubeLevel(self.s.lube_level)
            self.setMaxAcceleration(self.s.max_acceleration)
            self.setMaxVelocity(self.s.max_velocity)
            self.setMcodes(self.s.mcodes)
            self.setMist(self.s.mist)
            self.setMotionLine(self.s.motion_line)
            self.setMotionMode(self.s.motion_mode)
            self.setMotionType(self.s.motion_type)
            self.setOptionalStop(self.s.optional_stop)
            self.setPaused(self.s.paused)
            self.setPocketPrepped(self.s.pocket_prepped)
            self.setPosition(self.s.position)
            self.setProbeTripped(self.s.probe_tripped)
            self.setProbeVal(self.s.probe_val)
            self.setProbedPosition(self.s.probed_position)
            self.setProbing(self.s.probing)
            self.setProgramUnits(self.s.program_units)
            self.setQueue(self.s.queue)
            self.setQueueFull(self.s.queue_full)
            self.setReadLine(self.s.read_line)
            self.setRotationXY(self.s.rotation_xy)
            self.setSettings(self.s.settings)
            self.setSpindleBrake(self.s.spindle_brake)
            self.setSpindleDirection(self.s.spindle_direction)
            self.setSpindleEnabled(self.s.spindle_enabled)
            self.setSpindleIncreasing(self.s.spindle_increasing)
            self.setSpindleOverrideEnabled(self.s.spindle_override_enabled)
            self.setSpindleSpeed(self.s.spindle_speed)
            self.setSpindlerate(self.s.spindlerate)
            self.setState(self.s.state)
            self.setTaskMode(self.s.task_mode)
            self.setTaskPaused(self.s.task_paused)
            self.setTaskState(self.s.task_state)
            self.setToolInSpindle(self.s.tool_in_spindle)
            self.setToolOffset(self.s.tool_offset)
            self.setToolTable(self.s.tool_table)
            self.setVelocity(self.s.velocity)
            self.setAxis(self.s.axis)
        except linuxcnc.error as detail:
            print(("error", detail))

    AUTO_PAUSE = pyqtProperty(int, lambda c: linuxcnc.AUTO_PAUSE,
                                constant=True)
    AUTO_RESUME = pyqtProperty(int, lambda c: linuxcnc.AUTO_RESUME,
                                constant=True)
    AUTO_RUN = pyqtProperty(int, lambda c: linuxcnc.AUTO_RUN,
                                constant=True)
    AUTO_STEP = pyqtProperty(int, lambda c: linuxcnc.AUTO_STEP,
                           constant=True)
    AXIS_ANGULAR = pyqtProperty(int, lambda c: linuxcnc.AXIS_ANGULAR,
                           constant=True)
    AXIS_LINEAR = pyqtProperty(int, lambda c: linuxcnc.AXIS_LINEAR,
                           constant=True)
    BRAKE_ENGAGE = pyqtProperty(int, lambda c: linuxcnc.BRAKE_ENGAGE,
                           constant=True)
    BRAKE_RELEASE = pyqtProperty(int, lambda c: linuxcnc.BRAKE_RELEASE,
                           constant=True)
    DEBUG_CONFIG = pyqtProperty(int, lambda c: linuxcnc.DEBUG_CONFIG,
                           constant=True)
    DEBUG_INTERP = pyqtProperty(int, lambda c: linuxcnc.DEBUG_INTERP,
                           constant=True)
    DEBUG_INTERP_LIST = pyqtProperty(int, lambda c: linuxcnc.DEBUG_INTERP_LIST,
                           constant=True)
    DEBUG_MOTION_TIME = pyqtProperty(int, lambda c: linuxcnc.DEBUG_MOTION_TIME,
                           constant=True)
    DEBUG_NML = pyqtProperty(int, lambda c: linuxcnc.DEBUG_NML,
                           constant=True)
    DEBUG_RCS = pyqtProperty(int, lambda c: linuxcnc.DEBUG_RCS,
                           constant=True)
    DEBUG_TASK_ISSUE = pyqtProperty(int, lambda c: linuxcnc.DEBUG_TASK_ISSUE,
                           constant=True)
    DEBUG_VERSIONS = pyqtProperty(int, lambda c: linuxcnc.DEBUG_VERSIONS,
                           constant=True)
    EXEC_DONE = pyqtProperty(int, lambda c: linuxcnc.EXEC_DONE,
                           constant=True)
    EXEC_ERROR = pyqtProperty(int, lambda c: linuxcnc.EXEC_ERROR,
                           constant=True)
    EXEC_WAITING_FOR_DELAY = pyqtProperty(int,
                            lambda c: linuxcnc.EXEC_WAITING_FOR_DELAY,
                            constant=True)
    EXEC_WAITING_FOR_IO = pyqtProperty(int,
                            lambda c: linuxcnc.EXEC_WAITING_FOR_IO,
                            constant=True)
    EXEC_WAITING_FOR_MOTION = pyqtProperty(int,
                            lambda c: linuxcnc.EXEC_WAITING_FOR_MOTION,
                            constant=True)
    EXEC_WATING_FOR_MOTION_AND_IO = pyqtProperty(int,
                            lambda c: linuxcnc.EXEC_WATING_FOR_MOTION_AND_IO,
                            constant=True)
    EXEC_WAITING_FOR_MOTION_QUEUE = pyqtProperty(int,
                            lambda c: linuxcnc.EXEC_WAITING_FOR_MOTION_QUEUE,
                            constant=True)
    EXEC_WAITING_FOR_SYSTEM_CMD = pyqtProperty(int,
                            lambda c: linuxcnc.EXEC_WAITING_FOR_SYSTEM_CMD,
                            constant=True)
    FLOOD_OFF = pyqtProperty(int, lambda c: linuxcnc.FLOOD_OFF,
                           constant=True)
    FLOOD_ON = pyqtProperty(int, lambda c: linuxcnc.FLOOD_ON,
                           constant=True)
    INTERP_IDLE = pyqtProperty(int, lambda c: linuxcnc.INTERP_IDLE,
                           constant=True)
    INTERP_PAUSED = pyqtProperty(int, lambda c: linuxcnc.INTERP_PAUSED,
                           constant=True)
    INTERP_READING = pyqtProperty(int, lambda c: linuxcnc.INTERP_READING,
                           constant=True)
    INTERP_WAITING = pyqtProperty(int, lambda c: linuxcnc.INTERP_WAITING,
                           constant=True)
    JOG_CONTINUOUS = pyqtProperty(int, lambda c: linuxcnc.JOG_CONTINUOUS,
                           constant=True)
    JOG_INCREMENT = pyqtProperty(int, lambda c: linuxcnc.JOG_INCREMENT,
                           constant=True)
    JOG_STOP = pyqtProperty(int, lambda c: linuxcnc.JOG_STOP,
                           constant=True)
    KINEMATICS_BOTH = pyqtProperty(int, lambda c: linuxcnc.KINEMATICS_BOTH,
                           constant=True)
    KINEMATICS_BOTH = pyqtProperty(int, lambda c: linuxcnc.KINEMATICS_BOTH,
                           constant=True)
    KINEMATICS_IDENTITY = pyqtProperty(int,
                            lambda c: linuxcnc.KINEMATICS_IDENTITY,
                            constant=True)
    KINEMATICS_INVERSE_ONLY = pyqtProperty(int,
                            lambda c: linuxcnc.KINEMATICS_INVERSE_ONLY,
                            constant=True)
    MIST_OFF = pyqtProperty(int, lambda c: linuxcnc.MIST_OFF,
                           constant=True)
    MIST_ON = pyqtProperty(int, lambda c: linuxcnc.MIST_ON,
                           constant=True)
    MODE_AUTO = pyqtProperty(int, lambda c: linuxcnc.MODE_AUTO,
                           constant=True)
    MODE_MANUAL = pyqtProperty(int, lambda c: linuxcnc.MODE_MANUAL,
                           constant=True)
    MODE_MDI = pyqtProperty(int, lambda c: linuxcnc.MODE_MDI,
                           constant=True)
    NML_DISPLAY = pyqtProperty(int, lambda c: linuxcnc.NML_DISPLAY,
                           constant=True)
    NML_ERROR = pyqtProperty(int, lambda c: linuxcnc.NML_ERROR,
                           constant=True)
    NML_TEXT = pyqtProperty(int, lambda c: linuxcnc.NML_TEXT,
                           constant=True)
    OPERATOR_DISPLAY = pyqtProperty(int, lambda c: linuxcnc.OPERATOR_DISPLAY,
                           constant=True)
    OPERATOR_ERROR = pyqtProperty(int, lambda c: linuxcnc.OPERATOR_ERROR,
                           constant=True)
    OPERATOR_TEXT = pyqtProperty(int, lambda c: linuxcnc.OPERATOR_TEXT,
                           constant=True)
    RCS_DONE = pyqtProperty(int, lambda c: linuxcnc.RCS_DONE,
                           constant=True)
    RCS_ERROR = pyqtProperty(int, lambda c: linuxcnc.RCS_ERROR,
                           constant=True)
    RCS_EXEC = pyqtProperty(int, lambda c: linuxcnc.RCS_EXEC,
                           constant=True)
    SPINDLE_CONSTANT = pyqtProperty(int, lambda c: linuxcnc.SPINDLE_CONSTANT,
                           constant=True)
    SPINDLE_DECREASE = pyqtProperty(int, lambda c: linuxcnc.SPINDLE_DECREASE,
                           constant=True)
    SPINDLE_FORWARD = pyqtProperty(int, lambda c: linuxcnc.SPINDLE_FORWARD,
                           constant=True)
    SPINDLE_INCREASE = pyqtProperty(int, lambda c: linuxcnc.SPINDLE_INCREASE,
                           constant=True)
    SPINDLE_OFF = pyqtProperty(int, lambda c: linuxcnc.SPINDLE_OFF,
                           constant=True)
    SPINDLE_REVERSE = pyqtProperty(int, lambda c: linuxcnc.SPINDLE_REVERSE,
                           constant=True)
    STATE_ESTOP = pyqtProperty(int, lambda c: linuxcnc.STATE_ESTOP,
                           constant=True)
    STATE_ESTOP_RESET = pyqtProperty(int, lambda c: linuxcnc.STATE_ESTOP_RESET,
                           constant=True)
    STATE_OFF = pyqtProperty(int, lambda c: linuxcnc.STATE_OFF,
                           constant=True)
    STATE_ON = pyqtProperty(int, lambda c: linuxcnc.STATE_ON,
                           constant=True)
    TRAJ_MODE_COORD = pyqtProperty(int, lambda c: linuxcnc.TRAJ_MODE_COORD,
                           constant=True)
    TRAJ_MODE_FREE = pyqtProperty(int, lambda c: linuxcnc.TRAJ_MODE_FREE,
                           constant=True)
    TRAJ_MODE_TELEOP = pyqtProperty(int, lambda c: linuxcnc.TRAJ_MODE_TELEOP,
                           constant=True)

    #axis Property
    @pyqtProperty(QQmlListProperty)
    def axis(self):
        return QQmlListProperty(Axis, self,
                append=lambda parent, newItem: parent._axis.append(newItem),
                at=lambda parent, pos: parent._axis[pos],
                count=lambda parent: len(parent._axis))

    def setAxis(self, axisTemp):
        if (self._axisTemp != axisTemp):
            self._axisTemp = axisTemp
            for i in range(0, len(self._axis)):
                self._axis[i].setAxisType(self._axisTemp[i]['axisType'])
                self._axis[i].setBacklash(self._axisTemp[i]['backlash'])
                self._axis[i].setEnabled(self._axisTemp[i]['enabled'])
                self._axis[i].setFault(self._axisTemp[i]['fault'])
                self._axis[i].setFerrorCurrent(self._axisTemp[i]['ferror_current'])
                self._axis[i].setFerrorHighmark(self._axisTemp[i]['ferror_highmark'])
                self._axis[i].setHomed(self._axisTemp[i]['homed'])
                self._axis[i].setHoming(self._axisTemp[i]['homing'])
                self._axis[i].setInpos(self._axisTemp[i]['inpos'])
                self._axis[i].setInputPosition(self._axisTemp[i]['input'])
                self._axis[i].setMaxFerror(self._axisTemp[i]['max_ferror'])
                self._axis[i].setMaxHardLimit(self._axisTemp[i]['max_hard_limit'])
                self._axis[i].setMaxSoftLimit(self._axisTemp[i]['max_soft_limit'])
                self._axis[i].setMinFerror(self._axisTemp[i]['min_ferror'])
                self._axis[i].setMinHardLimit(self._axisTemp[i]['min_hard_limit'])
                self._axis[i].setMinPositionLimit(self._axisTemp[i]['min_position_limit'])
                self._axis[i].setMinSoftLimit(self._axisTemp[i]['min_soft_limit'])
                self._axis[i].setOutput(self._axisTemp[i]['output'])
                self._axis[i].setOverrideLimits(self._axisTemp[i]['override_limits'])
                self._axis[i].setUnits(self._axisTemp[i]['units'])
                self._axis[i].setVelocity(self._axisTemp[i]['velocity'])

    # acceleration Property
    accelerationChanged = pyqtSignal(float)

    def getAcceleration(self):
        return self._acceleration

    def setAcceleration(self, acceleration):
        if (self._acceleration != acceleration):
            self._acceleration = acceleration
            self.accelerationChanged.emit(self._acceleration)

    acceleration = pyqtProperty(float,
                                getAcceleration,
                                notify=accelerationChanged)

    # activeQueue Property
    activeQueueChanged = pyqtSignal(int)

    def getActiveQueue(self):
        return self._activeQueue

    def setActiveQueue(self, activeQueue):
        if (self._activeQueue != activeQueue):
            self._activeQueue = activeQueue
            self.activeQueueChanged.emit(self._activeQueue)

    activeQueue = pyqtProperty(int,
                            getActiveQueue,
                            notify=activeQueueChanged)

    # actualPosition Property
    actualPositionChanged = pyqtSignal('QVariant')

    def getActualPosition(self):
        return list(self._actualPosition)

    def setActualPosition(self, actualPosition):
        if (self._actualPosition != actualPosition):
            self._actualPosition = actualPosition
            self.actualPositionChanged.emit(list(self._actualPosition))

    actualPosition = pyqtProperty('QVariant',
                            getActualPosition,
                            notify=actualPositionChanged)

    # adaptiveFeedEnabled Property
    adaptiveFeedEnabledChanged = pyqtSignal(bool)

    def getAdaptiveFeedEnabled(self):
        return self._adaptiveFeedEnabled

    def setAdaptiveFeedEnabled(self, adaptiveFeedEnabled):
        if (self._adaptiveFeedEnabled != adaptiveFeedEnabled):
            self._adaptiveFeedEnabled = adaptiveFeedEnabled
            self.adaptiveFeedEnabledChanged.emit(self._adaptiveFeedEnabled)

    adaptiveFeedEnabled = pyqtProperty(bool,
                            getAdaptiveFeedEnabled,
                            notify=adaptiveFeedEnabledChanged)

    # ain Property
    ainChanged = pyqtSignal('QVariant')

    def getAin(self):
        return list(self._ain)

    def setAin(self, ain):
        if (self._ain != ain):
            self._ain = ain
            self.ainChanged.emit(self._ain)

    ain = pyqtProperty('QVariant',
                            getAin,
                            notify=ainChanged)

    # angularUnits Property
    angularUnitsChanged = pyqtSignal(float)

    def getAngularUnits(self):
        return self._angularUnits

    def setAngularUnits(self, angularUnits):
        if (self._angularUnits != angularUnits):
            self._angularUnits = angularUnits
            self.angularUnitsChanged.emit(self._angularUnits)

    angularUnits = pyqtProperty(float,
                            getAngularUnits,
                            notify=angularUnitsChanged)

    # aout Property
    aoutChanged = pyqtSignal('QVariant')

    def getAout(self):
        return list(self._aout)

    def setAout(self, aout):
        if (self._aout != aout):
            self._aout = aout
            self.aoutChanged.emit(list(self._aout))

    aout = pyqtProperty('QVariant',
                            getAout,
                            notify=aoutChanged)

    # axes Property
    axesChanged = pyqtSignal(int)

    def getAxes(self):
        return self._axes

    def setAxes(self, axes):
        if (self._axes != axes):
            self._axes = axes
            self.axesChanged.emit(self._axes)

    axes = pyqtProperty(int,
                            getAxes,
                            notify=axesChanged)

    # axisMask Property
    axisMaskChanged = pyqtSignal(int)

    def getAxisMask(self):
        return self._axisMask

    def setAxisMask(self, axisMask):
        if (self._axisMask != axisMask):
            self._axisMask = axisMask
            self.axisMaskChanged.emit(self._axisMask)

    axisMask = pyqtProperty(int,
                            getAxisMask,
                            notify=axisMaskChanged)

    # blockDelete Property
    blockDeleteChanged = pyqtSignal(int)

    def getBlockDelete(self):
        return self._blockDelete

    def setBlockDelete(self, blockDelete):
        if (self._blockDelete != blockDelete):
            self._blockDelete = blockDelete
            self.blockDeleteChanged.emit(self._blockDelete)

    blockDelete = pyqtProperty(int,
                            getBlockDelete,
                            notify=blockDeleteChanged)

    # command Property
    commandChanged = pyqtSignal('QString')

    def getCommand(self):
        return self._command

    def setCommand(self, command):
        if (self._command != command):
            self._command = command
            self.commandChanged.emit(self._command)

    command = pyqtProperty('QString',
                            getCommand,
                            notify=commandChanged)

    # currentLine Property
    currentLineChanged = pyqtSignal(int)

    def getCurrentLine(self):
        return self._currentLine

    def setCurrentLine(self, currentLine):
        if (self._currentLine != currentLine):
            self._currentLine = currentLine
            self.currentLineChanged.emit(self._currentLine)

    currentLine = pyqtProperty(int,
                            getCurrentLine,
                            notify=currentLineChanged)

    # currentVel Property
    currentVelChanged = pyqtSignal(float)

    def getCurrentVel(self):
        return self._currentVel

    def setCurrentVel(self, currentVel):
        if (self._currentVel != currentVel):
            self._currentVel = currentVel
            self.currentVelChanged.emit(self._currentVel)

    currentVel = pyqtProperty(float,
                            getCurrentVel,
                            notify=currentVelChanged)

    # cycleTime Property
    cycleTimeChanged = pyqtSignal(float)

    def getCycleTime(self):
        return self._cycleTime

    def setCycleTime(self, cycleTime):
        if (self._cycleTime != cycleTime):
            self._cycleTime = cycleTime
            self.cycleTimeChanged.emit(self._cycleTime)

    cycleTime = pyqtProperty(float,
                            getCycleTime,
                            notify=cycleTimeChanged)

    # debug Property
    debugChanged = pyqtSignal(int)

    def getDebug(self):
        return self._debug

    def setDebug(self, debug):
        if (self._debug != debug):
            self._debug = debug
            self.debugChanged.emit(self._debug)

    debug = pyqtProperty(int,
                            getDebug,
                            notify=debugChanged)

    # delayLeft Property
    delayLeftChanged = pyqtSignal(float)

    def getDelayLeft(self):
        return self._delayLeft

    def setDelayLeft(self, delayLeft):
        if (self._delayLeft != delayLeft):
            self._delayLeft = delayLeft
            self.delayLeftChanged.emit(self._delayLeft)

    delayLeft = pyqtProperty(float,
                            getDelayLeft,
                            notify=delayLeftChanged)

    # din Property
    dinChanged = pyqtSignal('QVariant')

    def getDin(self):
        return list(self._din)

    def setDin(self, din):
        if (self._din != din):
            self._din = din
            self.dinChanged.emit(list(self._din))

    din = pyqtProperty('QVariant',
                            getDin,
                            notify=dinChanged)

    # distanceToGo Property
    distanceToGoChanged = pyqtSignal(float)

    def getDistanceToGo(self):
        return self._distanceToGo

    def setDistanceToGo(self, distanceToGo):
        if (self._distanceToGo != distanceToGo):
            self._distanceToGo = distanceToGo
            self.distanceToGoChanged.emit(self._distanceToGo)

    distanceToGo = pyqtProperty(float,
                            getDistanceToGo,
                            notify=distanceToGoChanged)

    # dout Property
    doutChanged = pyqtSignal('QVariant')

    def getDout(self):
        return list(self._dout)

    def setDout(self, dout):
        if (self._dout != dout):
            self._dout = dout
            self.doutChanged.emit(list(self._dout))

    dout = pyqtProperty('QVariant',
                            getDout,
                            notify=doutChanged)

    # dtg Property
    dtgChanged = pyqtSignal('QVariant')

    def getDtg(self):
        return list(self._dtg)

    def setDtg(self, dtg):
        if (self._dtg != dtg):
            self._dtg = dtg
            self.dtgChanged.emit(list(self._dtg))

    dtg = pyqtProperty('QVariant',
                            getDtg,
                            notify=dtgChanged)

    # echoSerialNumber Property
    echoSerialNumberChanged = pyqtSignal(int)

    def getEchoSerialNumber(self):
        return self._echoSerialNumber

    def setEchoSerialNumber(self, echoSerialNumber):
        if (self._echoSerialNumber != echoSerialNumber):
            self._echoSerialNumber = echoSerialNumber
            self.echoSerialNumberChanged.emit(self._echoSerialNumber)

    echoSerialNumber = pyqtProperty(int,
                            getEchoSerialNumber,
                            notify=echoSerialNumberChanged)

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

    # estop Property
    estopChanged = pyqtSignal(int)

    def getEstop(self):
        return self._estop

    def setEstop(self, estop):
        if (self._estop != estop):
            self._estop = estop
            self.estopChanged.emit(self._estop)

    estop = pyqtProperty(int,
                            getEstop,
                            notify=estopChanged)

    # execState Property
    execStateChanged = pyqtSignal(int)

    def getExecState(self):
        return self._execState

    def setExecState(self, execState):
        if (self._execState != execState):
            self._execState = execState
            self.execStateChanged.emit(self._execState)

    execState = pyqtProperty(int,
                            getExecState,
                            notify=execStateChanged)

    # feedHoldEnabled Property
    feedHoldEnabledChanged = pyqtSignal(int)

    def getFeedHoldEnabled(self):
        return self._feedHoldEnabled

    def setFeedHoldEnabled(self, feedHoldEnabled):
        if (self._feedHoldEnabled != feedHoldEnabled):
            self._feedHoldEnabled = feedHoldEnabled
            self.feedHoldEnabledChanged.emit(self._feedHoldEnabled)

    feedHoldEnabled = pyqtProperty(int,
                            getFeedHoldEnabled,
                            notify=feedHoldEnabledChanged)

    # feedOverrideEnabled Property
    feedOverrideEnabledChanged = pyqtSignal(int)

    def getFeedOverrideEnabled(self):
        return self._feedOverrideEnabled

    def setFeedOverrideEnabled(self, feedOverrideEnabled):
        if (self._feedOverrideEnabled != feedOverrideEnabled):
            self._feedOverrideEnabled = feedOverrideEnabled
            self.feedOverrideEnabledChanged.emit(self._feedOverrideEnabled)

    feedOverrideEnabled = pyqtProperty(int,
                            getFeedOverrideEnabled,
                            notify=feedOverrideEnabledChanged)

    # feedrate Property
    feedrateChanged = pyqtSignal(float)

    def getFeedrate(self):
        return self._feedrate

    def setFeedrate(self, feedrate):
        if (self._feedrate != feedrate):
            self._feedrate = feedrate
            self.feedrateChanged.emit(self._feedrate)

    feedrate = pyqtProperty(float,
                            getFeedrate,
                            notify=feedrateChanged)

    # fileName Property
    fileNameChanged = pyqtSignal('QString')

    def getFileName(self):
        return self._fileName

    def setFileName(self, fileName):
        if (self._fileName != fileName):
            self._fileName = fileName
            self.fileChanged.emit(self._fileName)

    fileName = pyqtProperty('QString',
                            getFileName,
                            notify=fileNameChanged)

    # flood Property
    floodChanged = pyqtSignal(int)

    def getFlood(self):
        return self._flood

    def setFlood(self, flood):
        if (self._flood != flood):
            self._flood = flood
            self.floodChanged.emit(self._flood)

    flood = pyqtProperty(int,
                            getFlood,
                            notify=floodChanged)

    # g5xIndex Property
    g5xIndexChanged = pyqtSignal(int)

    def getG5xIndex(self):
        return self._g5xIndex

    def setG5xIndex(self, g5xIndex):
        if (self._g5xIndex != g5xIndex):
            self._g5xIndex = g5xIndex
            self.g5xIndexChanged.emit(self._g5xIndex)

    g5xIndex = pyqtProperty(int,
                            getG5xIndex,
                            notify=g5xIndexChanged)

    # g5xOffset Property
    g5xOffsetChanged = pyqtSignal('QVariant')

    def getG5xOffset(self):
        return list(self._g5xOffset)

    def setG5xOffset(self, g5xOffset):
        if (self._g5xOffset != g5xOffset):
            self._g5xOffset = g5xOffset
            self.g5xOffsetChanged.emit(list(self._g5xOffset))

    g5xOffset = pyqtProperty('QVariant',
                            getG5xOffset,
                            notify=g5xOffsetChanged)

    # g92Offset Property
    g92OffsetChanged = pyqtSignal('QVariant')

    def getG92Offset(self):
        return list(self._g92Offset)

    def setG92Offset(self, g92Offset):
        if (self._g92Offset != g92Offset):
            self._g92Offset = g92Offset
            self.g92OffsetChanged.emit(list(self._g92Offset))

    g92Offset = pyqtProperty('QVariant',
                            getG92Offset,
                            notify=g92OffsetChanged)

    # gcodes Property
    gcodesChanged = pyqtSignal('QVariant')

    def getGcodes(self):
        return list(self._gcodes)

    def setGcodes(self, gcodes):
        if (self._gcodes != gcodes):
            self._gcodes = gcodes
            self.gcodesChanged.emit(list(self._gcodes))

    gcodes = pyqtProperty('QVariant',
                            getGcodes,
                            notify=gcodesChanged)

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

    # motionId Property
    motionIdChanged = pyqtSignal(int)

    def getMotionId(self):
        return self._motionId

    def setMotionId(self, motionId):
        if (self._motionId != motionId):
            self._motionId = motionId
            self.motionIdChanged.emit(self._motionId)

    motionId = pyqtProperty(int,
                            getMotionId,
                            notify=motionIdChanged)

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

    # inputTimeout Property
    inputTimeoutChanged = pyqtSignal(int)

    def getInputTimeout(self):
        return self._inputTimeout

    def setInputTimeout(self, inputTimeout):
        if (self._inputTimeout != inputTimeout):
            self._inputTimeout = inputTimeout
            self.inputTimeoutChanged.emit(self._inputTimeout)

    inputTimeout = pyqtProperty(int,
                            getInputTimeout,
                            notify=inputTimeoutChanged)

    # interpState Property
    interpStateChanged = pyqtSignal(int)

    def getInterpState(self):
        return self._interpState

    def setInterpState(self, interpState):
        if (self._interpState != interpState):
            self._interpState = interpState
            self.interpStateChanged.emit(self._interpState)

    interpState = pyqtProperty(int,
                            getInterpState,
                            notify=interpStateChanged)

    # interpreterErrcode Property
    interpreterErrcodeChanged = pyqtSignal(int)

    def getInterpreterErrcode(self):
        return self._interpreterErrcode

    def setInterpreterErrcode(self, interpreterErrcode):
        if (self._interpreterErrcode != interpreterErrcode):
            self._interpreterErrcode = interpreterErrcode
            self.interpreterErrcodeChanged.emit(self._interpreterErrcode)

    interpreterErrcode = pyqtProperty(int,
                            getInterpreterErrcode,
                            notify=interpreterErrcodeChanged)

    # jointActualPosition Property
    jointActualPositionChanged = pyqtSignal('QVariant')

    def getJointActualPosition(self):
        return list(self._jointActualPosition)

    def setJointActualPosition(self, jointActualPosition):
        if (self._jointActualPosition != jointActualPosition):
            self._jointActualPosition = jointActualPosition
            self.jointActualPositionChanged.emit(
                list(self._jointActualPosition))

    jointActualPosition = pyqtProperty('QVariant',
                            getJointActualPosition,
                            notify=jointActualPositionChanged)

    # jointPosition Property
    jointPositionChanged = pyqtSignal('QVariant')

    def getJointPosition(self):
        return list(self._jointPosition)

    def setJointPosition(self, jointPosition):
        if (self._jointPosition != jointPosition):
            self._jointPosition = jointPosition
            self.jointPositionChanged.emit(list(self._jointPosition))

    jointPosition = pyqtProperty('QVariant',
                            getJointPosition,
                            notify=jointPositionChanged)

    # kinematicsType Property
    kinematicsTypeChanged = pyqtSignal(int)

    def getKinematicsType(self):
        return self._kinematicsType

    def setKinematicsType(self, kinematicsType):
        if (self._kinematicsType != kinematicsType):
            self._kinematicsType = kinematicsType
            self.kinematicsTypeChanged.emit(self._kinematicsType)

    kinematicsType = pyqtProperty(int,
                            getKinematicsType,
                            notify=kinematicsTypeChanged)

    # limit Property
    limitChanged = pyqtSignal('QVariant')

    def getLimit(self):
        return list(self._limit)

    def setLimit(self, limit):
        if (self._limit != limit):
            self._limit = limit
            self.limitChanged.emit(list(self._limit))

    limit = pyqtProperty('QVariant',
                            getLimit,
                            notify=limitChanged)

    # linearUnits Property
    linearUnitsChanged = pyqtSignal(float)

    def getLinearUnits(self):
        return self._linearUnits

    def setLinearUnits(self, linearUnits):
        if (self._linearUnits != linearUnits):
            self._linearUnits = linearUnits
            self.linearUnitsChanged.emit(self._linearUnits)

    linearUnits = pyqtProperty(float,
                            getLinearUnits,
                            notify=linearUnitsChanged)

    # lube Property
    lubeChanged = pyqtSignal(int)

    def getLube(self):
        return self._lube

    def setLube(self, lube):
        if (self._lube != lube):
            self._lube = lube
            self.lubeChanged.emit(self._lube)

    lube = pyqtProperty(int,
                            getLube,
                            notify=lubeChanged)

    # lubeLevel Property
    lubeLevelChanged = pyqtSignal(int)

    def getLubeLevel(self):
        return self._lubeLevel

    def setLubeLevel(self, lubeLevel):
        if (self._lubeLevel != lubeLevel):
            self._lubeLevel = lubeLevel
            self.lubeLevelChanged.emit(self._lubeLevel)

    lubeLevel = pyqtProperty(int,
                            getLubeLevel,
                            notify=lubeLevelChanged)

    # maxAcceleration Property
    maxAccelerationChanged = pyqtSignal(float)

    def getMaxAcceleration(self):
        return self._maxAcceleration

    def setMaxAcceleration(self, maxAcceleration):
        if (self._maxAcceleration != maxAcceleration):
            self._maxAcceleration = maxAcceleration
            self.maxAccelerationChanged.emit(self._maxAcceleration)

    maxAcceleration = pyqtProperty(float,
                            getMaxAcceleration,
                            notify=maxAccelerationChanged)

    # maxVelocity Property
    maxVelocityChanged = pyqtSignal(float)

    def getMaxVelocity(self):
        return self._maxVelocity

    def setMaxVelocity(self, maxVelocity):
        if (self._maxVelocity != maxVelocity):
            self._maxVelocity = maxVelocity
            self.maxVelocityChanged.emit(self._maxVelocity)

    maxVelocity = pyqtProperty(float,
                            getMaxVelocity,
                            notify=maxVelocityChanged)

    # mcodes Property
    mcodesChanged = pyqtSignal('QVariant')

    def getMcodes(self):
        return list(self._mcodes)

    def setMcodes(self, mcodes):
        if (self._mcodes != mcodes):
            self._mcodes = mcodes
            self.mcodesChanged.emit(list(self._mcodes))

    mcodes = pyqtProperty('QVariant',
                            getMcodes,
                            notify=mcodesChanged)

    # mist Property
    mistChanged = pyqtSignal(int)

    def getMist(self):
        return self._mist

    def setMist(self, mist):
        if (self._mist != mist):
            self._mist = mist
            self.mistChanged.emit(self._mist)

    mist = pyqtProperty(int,
                            getMist,
                            notify=mistChanged)

    # motionLine Property
    motionLineChanged = pyqtSignal(int)

    def getMotionLine(self):
        return self._motionLine

    def setMotionLine(self, motionLine):
        if (self._motionLine != motionLine):
            self._motionLine = motionLine
            self.motionLineChanged.emit(self._motionLine)

    motionLine = pyqtProperty(int,
                            getMotionLine,
                            notify=motionLineChanged)

    # motionMode Property
    motionModeChanged = pyqtSignal(int)

    def getMotionMode(self):
        return self._motionMode

    def setMotionMode(self, motionMode):
        if (self._motionMode != motionMode):
            self._motionMode = motionMode
            self.motionModeChanged.emit(self._motionMode)

    motionMode = pyqtProperty(int,
                            getMotionMode,
                            notify=motionModeChanged)

    # motionType Property
    motionTypeChanged = pyqtSignal(int)

    def getMotionType(self):
        return self._motionType

    def setMotionType(self, motionType):
        if (self._motionType != motionType):
            self._motionType = motionType
            self.motionTypeChanged.emit(self._motionType)

    motionType = pyqtProperty(int,
                            getMotionType,
                            notify=motionTypeChanged)

    # optionalStop Property
    optionalStopChanged = pyqtSignal(int)

    def getOptionalStop(self):
        return self._optionalStop

    def setOptionalStop(self, optionalStop):
        if (self._optionalStop != optionalStop):
            self._optionalStop = optionalStop
            self.optionalStopChanged.emit(self._optionalStop)

    optionalStop = pyqtProperty(int,
                            getOptionalStop,
                            notify=optionalStopChanged)

    # paused Property
    pausedChanged = pyqtSignal(int)

    def getPaused(self):
        return self._paused

    def setPaused(self, paused):
        if (self._paused != paused):
            self._paused = paused
            self.pausedChanged.emit(self._paused)

    paused = pyqtProperty(int,
                            getPaused,
                            notify=pausedChanged)

    # pocketPrepped Property
    pocketPreppedChanged = pyqtSignal(int)

    def getPocketPrepped(self):
        return self._pocketPrepped

    def setPocketPrepped(self, pocketPrepped):
        if (self._pocketPrepped != pocketPrepped):
            self._pocketPrepped = pocketPrepped
            self.pocketPreppedChanged.emit(self._pocketPrepped)

    pocketPrepped = pyqtProperty(int,
                            getPocketPrepped,
                            notify=pocketPreppedChanged)

    # position Property
    positionChanged = pyqtSignal('QVariant')

    def getPosition(self):
        return list(self._position)

    def setPosition(self, position):
        if (self._position != position):
            self._position = position
            self.positionChanged.emit(list(self._position))

    position = pyqtProperty('QVariant',
                            getPosition,
                            notify=positionChanged)

    # propeTripped Property
    probeTrippedChanged = pyqtSignal(int)

    def getProbeTripped(self):
        return self._probeTripped

    def setProbeTripped(self, probeTripped):
        if (self._probeTripped != probeTripped):
            self._probeTripped = probeTripped
            self.probeTrippedChanged.emit(self._probeTripped)

    probeTripped = pyqtProperty(int,
                            getProbeTripped,
                            notify=probeTrippedChanged)

    # propeVal Property
    probeValChanged = pyqtSignal(int)

    def getProbeVal(self):
        return self._probeVal

    def setProbeVal(self, probeVal):
        if (self._probeVal != probeVal):
            self._probeVal = probeVal
            self.probeValChanged.emit(self._probeVal)

    probeVal = pyqtProperty(int,
                            getProbeVal,
                            notify=probeValChanged)

    # probedPosition Property
    probedPositionChanged = pyqtSignal('QVariant')

    def getProbedPosition(self):
        return list(self._probedPosition)

    def setProbedPosition(self, probedPosition):
        if (self._probedPosition != probedPosition):
            self._probedPosition = probedPosition
            self.probedPositionChanged.emit(list(self._probedPosition))

    probedPosition = pyqtProperty('QVariant',
                            getProbedPosition,
                            notify=probedPositionChanged)

    # probing Property
    probingChanged = pyqtSignal(int)

    def getProbing(self):
        return self._probing

    def setProbing(self, probing):
        if (self._probing != probing):
            self._probing = probing
            self.probingChanged.emit(self._probing)

    probing = pyqtProperty(int,
                            getProbing,
                            notify=probingChanged)

    # programUnits Property
    programUnitsChanged = pyqtSignal(int)

    def getProgramUnits(self):
        return self._programUnits

    def setProgramUnits(self, programUnits):
        if (self._programUnits != programUnits):
            self._programUnits = programUnits
            self.programUnitsChanged.emit(self._programUnits)

    programUnits = pyqtProperty(int,
                            getProgramUnits,
                            notify=programUnitsChanged)

    # queue Property
    queueChanged = pyqtSignal(int)

    def getQueue(self):
        return self._queue

    def setQueue(self, queue):
        if (self._queue != queue):
            self._queue = queue
            self.queueChanged.emit(self._queue)

    queue = pyqtProperty(int,
                            getQueue,
                            notify=queueChanged)

    # queueFull Property
    queueFullChanged = pyqtSignal(int)

    def getQueueFull(self):
        return self._queueFull

    def setQueueFull(self, queueFull):
        if (self._queueFull != queueFull):
            self._queueFull = queueFull
            self.queueFullChanged.emit(self._queueFull)

    queueFull = pyqtProperty(int,
                            getQueueFull,
                            notify=queueFullChanged)

    # readLine Property
    readLineChanged = pyqtSignal(int)

    def getReadLine(self):
        return self._readLine

    def setReadLine(self, readLine):
        if (self._readLine != readLine):
            self._readLine = readLine
            self.readLineChanged.emit(self._readLine)

    readLine = pyqtProperty(int,
                            getReadLine,
                            notify=readLineChanged)

    # rotationXY Property
    rotationXYChanged = pyqtSignal(float)

    def getRotationXY(self):
        return self._rotationXY

    def setRotationXY(self, rotationXY):
        if (self._rotationXY != rotationXY):
            self._rotationXY = rotationXY
            self.rotationXYChanged.emit(self._rotationXY)

    rotationXY = pyqtProperty(float,
                            getRotationXY,
                            notify=rotationXYChanged)

    # settings Property
    settingsChanged = pyqtSignal('QVariant')

    def getSettings(self):
        return list(self._settings)

    def setSettings(self, settings):
        if (self._settings != settings):
            self._settings = settings
            self.settingsChanged.emit(list(self._settings))

    settings = pyqtProperty('QVariant',
                            getSettings,
                            notify=settingsChanged)

    # spindleBrake Property
    spindleBrakeChanged = pyqtSignal(int)

    def getSpindleBrake(self):
        return self._spindleBrake

    def setSpindleBrake(self, spindleBrake):
        if (self._spindleBrake != spindleBrake):
            self._spindleBrake = spindleBrake
            self.spindleBrakeChanged.emit(self._spindleBrake)

    spindleBrake = pyqtProperty(int,
                            getSpindleBrake,
                            notify=spindleBrakeChanged)

    # spindleDirection Property
    spindleDirectionChanged = pyqtSignal(int)

    def getSpindleDirection(self):
        return self._spindleDirection

    def setSpindleDirection(self, spindleDirection):
        if (self._spindleDirection != spindleDirection):
            self._spindleDirection = spindleDirection
            self.spindleDirectionChanged.emit(self._spindleDirection)

    spindleDirection = pyqtProperty(int,
                            getSpindleDirection,
                            notify=spindleDirectionChanged)

    # spindleEnabled Property
    spindleEnabledChanged = pyqtSignal(int)

    def getSpindleEnabled(self):
        return self._spindleEnabled

    def setSpindleEnabled(self, spindleEnabled):
        if (self._spindleEnabled != spindleEnabled):
            self._spindleEnabled = spindleEnabled
            self.spindleEnabledChanged.emit(self._spindleEnabled)

    spindleEnabled = pyqtProperty(int,
                            getSpindleEnabled,
                            notify=spindleEnabledChanged)

    # spindleIncreasing Property
    spindleIncreasingChanged = pyqtSignal(int)

    def getSpindleIncreasing(self):
        return self._spindleIncreasing

    def setSpindleIncreasing(self, spindleIncreasing):
        if (self._spindleIncreasing != spindleIncreasing):
            self._spindleIncreasing = spindleIncreasing
            self.spindleIncreasingChanged.emit(self._spindleIncreasing)

    spindleIncreasing = pyqtProperty(int,
                            getSpindleIncreasing,
                            notify=spindleIncreasingChanged)

    # spindleOverrideEnabled Property
    spindleOverrideEnabledChanged = pyqtSignal(int)

    def getSpindleOverrideEnabled(self):
        return self._spindleOverrideEnabled

    def setSpindleOverrideEnabled(self, spindleOverrideEnabled):
        if (self._spindleOverrideEnabled != spindleOverrideEnabled):
            self._spindleOverrideEnabled = spindleOverrideEnabled
            self.spindleOverrideEnabledChanged.emit(
                self._spindleOverrideEnabled)

    spindleOverrideEnabled = pyqtProperty(int,
                            getSpindleOverrideEnabled,
                            notify=spindleOverrideEnabledChanged)

    # spindleSpeed Property
    spindleSpeedChanged = pyqtSignal(float)

    def getSpindleSpeed(self):
        return self._spindleSpeed

    def setSpindleSpeed(self, spindleSpeed):
        if (self._spindleSpeed != spindleSpeed):
            self._spindleSpeed = spindleSpeed
            self.spindleSpeedChanged.emit(self._spindleSpeed)

    spindleSpeed = pyqtProperty(float,
                            getSpindleSpeed,
                            notify=spindleSpeedChanged)

    # spindlerate Property
    spindlerateChanged = pyqtSignal(float)

    def getSpindlerate(self):
        return self._spindlerate

    def setSpindlerate(self, spindlerate):
        if (self._spindlerate != spindlerate):
            self._spindlerate = spindlerate
            self.spindlerateChanged.emit(self._spindlerate)

    spindlerate = pyqtProperty(float,
                            getSpindlerate,
                            notify=spindlerateChanged)

    # state Property
    stateChanged = pyqtSignal(int)

    def getState(self):
        return self._state

    def setState(self, state):
        if (self._state != state):
            self._state = state
            self.stateChanged.emit(self._state)

    state = pyqtProperty(int,
                            getState,
                            notify=stateChanged)

    # taskMode Property
    taskModeChanged = pyqtSignal(int)

    def getTaskMode(self):
        return self._taskMode

    def setTaskMode(self, taskMode):
        if (self._taskMode != taskMode):
            self._taskMode = taskMode
            self.taskModeChanged.emit(self._taskMode)

    taskMode = pyqtProperty(int,
                            getTaskMode,
                            notify=taskModeChanged)

    # taskPaused Property
    taskPausedChanged = pyqtSignal(int)

    def getTaskPaused(self):
        return self._taskPaused

    def setTaskPaused(self, taskPaused):
        if (self._taskPaused != taskPaused):
            self._taskPaused = taskPaused
            self.taskPausedChanged.emit(self._taskPaused)

    taskPaused = pyqtProperty(int,
                            getTaskPaused,
                            notify=taskPausedChanged)

    # taskState Property
    taskStateChanged = pyqtSignal(int)

    def getTaskState(self):
        return self._taskState

    def setTaskState(self, taskState):
        if (self._taskState != taskState):
            self._taskState = taskState
            self.taskStateChanged.emit(self._taskState)

    taskState = pyqtProperty(int,
                            getTaskState,
                            notify=taskStateChanged)

    # toolInSpindle Property
    toolInSpindleChanged = pyqtSignal(int)

    def getToolInSpindle(self):
        return self._toolInSpindle

    def setToolInSpindle(self, toolInSpindle):
        if (self._toolInSpindle != toolInSpindle):
            self._toolInSpindle = toolInSpindle
            self.toolInSpindleChanged.emit(self._toolInSpindle)

    toolInSpindle = pyqtProperty(int,
                            getToolInSpindle,
                            notify=toolInSpindleChanged)

    # toolOffset Property
    toolOffsetChanged = pyqtSignal('QVariant')

    def getToolOffset(self):
        return list(self._toolOffset)

    def setToolOffset(self, toolOffset):
        if (self._toolOffset != toolOffset):
            self._toolOffset = toolOffset
            self.toolOffsetChanged.emit(list(self._toolOffset))

    toolOffset = pyqtProperty('QVariant',
                            getToolOffset,
                            notify=toolOffsetChanged)

    # toolTable Property
    toolTableChanged = pyqtSignal('QVariant')

    def getToolTable(self):
        return list(self._toolTable)

    def setToolTable(self, toolTable):
        if (self._toolTable != toolTable):
            self._toolTable = toolTable
            self.toolTableChanged.emit(list(self._toolTable))

    toolTable = pyqtProperty('QVariant',
                            getToolTable,
                            notify=toolTableChanged)

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
