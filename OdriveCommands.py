#imports
import odrive
import time
import math

# Class creation
class Odriver:
    def __init__(self):
        self.drive1 = odrive.find_any(serial_number='2069388F304E')  # left
        # self.drive2 = odrive.find_any(serial_number='20683882304E')
        self.drive3 = odrive.find_any(serial_number='207F3890304E')  # right
        self.velocity = 0.1 #In Turns/sec
        self.torque = 3.0 #In Nm
        self.x1Value = 0.0
        self.y1Value = 0.0
        self.x2Value = 0.0
        self.y2Value = 0.0

    def getBusVoltage(self):
        print(str(self.drive1.vbus_voltage))
        #print(str(self.drive2.vbus_voltage))
        print(str(self.drive3.vbus_voltage))

    def goForwardVel(self):
        self.drive1.axis0.controller.input_vel = (self.velocity)
        self.drive1.axis1.controller.input_vel = (self.velocity)
        self.drive3.axis0.controller.input_vel = (-1.0 * self.velocity)
        self.drive3.axis1.controller.input_vel = (-1.0 * self.velocity)

    def goBackwardVel(self):
        self.drive1.axis0.controller.input_vel = (-1.0 * self.velocity)
        self.drive1.axis1.controller.input_vel = (-1.0 * self.velocity)
        self.drive3.axis0.controller.input_vel = (self.velocity)
        self.drive3.axis1.controller.input_vel = (self.velocity)

    def goLeftVel(self):
        self.drive1.axis0.controller.input_vel = (self.velocity)
        self.drive1.axis1.controller.input_vel = (self.velocity)
        self.drive3.axis0.controller.input_vel = (self.velocity)
        self.drive3.axis1.controller.input_vel = (self.velocity)

    def goRightVel(self):
        self.drive1.axis0.controller.input_vel = (-1.0 * self.velocity)
        self.drive1.axis1.controller.input_vel = (-1.0 * self.velocity)
        self.drive3.axis0.controller.input_vel = (-1.0 * self.velocity)
        self.drive3.axis1.controller.input_vel = (-1.0 * self.velocity)

    def increaseVel(self):
        self.velocity = self.velocity + 1.0

    def decreaseVel(self):
        self.velocity = self.velocity - 1.0

    def increaseCur(self):
        self.torque = self.torque + 0.25

    def decreaseCur(self):
        self.torque = self.torque - 0.25

    def killVel(self):
        self.drive1.axis0.controller.input_vel = (0.0)
        self.drive1.axis1.controller.input_vel = (0.0)
        self.drive3.axis0.controller.input_vel = (0.0)
        self.drive3.axis1.controller.input_vel = (0.0)
        self.velocity = 0.0

    def stopVel(self):
        self.drive1.axis0.controller.input_vel = (0.0)
        self.drive1.axis1.controller.input_vel = (0.0)
        self.drive3.axis0.controller.input_vel = (0.0)
        self.drive3.axis1.controller.input_vel = (0.0)

    def stopTorque(self):
        self.drive1.axis0.controller.input_torque = (0.0)
        self.drive1.axis1.controller.input_torque = (0.0)
        self.drive3.axis0.controller.input_torque = (0.0)
        self.drive3.axis1.controller.input_torque = (0.0)

    def killTorque(self):
        self.drive1.axis0.controller.input_torque = (0.0)
        self.drive1.axis1.controller.input_torque = (0.0)
        self.drive3.axis0.controller.input_torque = (0.0)
        self.drive3.axis1.controller.input_torque = (0.0)
        self.torque = 0.0

    def goForwardCur(self):
        self.drive1.axis0.controller.input_torque = (self.torque)
        self.drive1.axis1.controller.input_torque = (self.torque)
        self.drive3.axis0.controller.input_torque = (-1 * self.torque)
        self.drive3.axis1.controller.input_torque = (-1 * self.torque)

    def goBackwardCur(self):
        self.drive1.axis0.controller.input_torque = (-1 * self.torque)
        self.drive1.axis1.controller.input_torque = (-1 * self.torque)
        self.drive3.axis0.controller.input_torque = (self.torque)
        self.drive3.axis1.controller.input_torque = (self.torque)

    def goLeftCur(self):
        self.drive1.axis0.controller.input_torque = (self.torque)
        self.drive1.axis1.controller.input_torque = (self.torque)
        self.drive3.axis0.controller.input_torque = (self.torque)
        self.drive3.axis1.controller.input_torque = (self.torque)

    def goRightCur(self):
        self.drive1.axis0.controller.input_torque = (-1 * self.torque)
        self.drive1.axis1.controller.input_torque = (-1 * self.torque)
        self.drive3.axis0.controller.input_torque = (-1 * self.torque)
        self.drive3.axis1.controller.input_torque = (-1 * self.torque)

    def setVelControl(self):
        self.drive1.axis0.controller.config.control_mode = 2
        self.drive1.axis1.controller.config.control_mode = 2
        self.drive3.axis0.controller.config.control_mode = 2
        self.drive3.axis1.controller.config.control_mode = 2

    def setTorqueControl(self):
        self.drive1.axis0.controller.config.control_mode = 1
        self.drive1.axis1.controller.config.control_mode = 1
        self.drive3.axis0.controller.config.control_mode = 1
        self.drive3.axis1.controller.config.control_mode = 1

    def goForwardCurConOne(self):
        self.drive1.axis0.controller.input_torque = self.y1Value
        self.drive1.axis1.controller.input_torque = self.y1Value
        self.drive3.axis0.controller.input_torque = -1 * self.y1Value
        self.drive3.axis1.controller.input_torque = -1 * self.y1Value

    def goBackwardCurConOne(self):
        self.drive1.axis0.controller.input_torque = -1 * self.y1Value
        self.drive1.axis1.controller.input_torque = -1 * self.y1Value
        self.drive3.axis0.controller.input_torque = self.y1Value
        self.drive3.axis1.controller.input_torque = self.y1Value
