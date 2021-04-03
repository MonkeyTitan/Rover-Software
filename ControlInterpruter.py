# imports
import odrive
import time
import math

# Class creation
class Interpreter:
    def __init__(self):
        # Data types
        self.drive1 = odrive.find_any(serial_number = '2069388F304E') #left
        self.drive2 = odrive.find_any(serial_number = '20683882304E')
        self.drive3 = odrive.find_any(serial_number = '207F3890304E') #right
        self.velocity = 0 #In turns a second

    def getBusVoltage(self):
        print(str(self.drive1.vbus_voltage))
        print(str(self.drive2.vbus_voltage))
        print(str(self.drive3.vbus_voltage))

    def goForward(self):
        drive1.axis0.controller.input_vel(-1 * self.velocity)
        drive1.axis1.controller.input_vel(-1 * self.velocity)
        drive3.axis0.controller.input_vel(self.velocity)
        drive3.axis1.controller.input_vel(self.velocity)

    def goBackward(self):
        drive1.axis0.controller.input_vel(self.velocity)
        drive1.axis1.controller.input_vel(self.velocity)
        drive3.axis0.controller.input_vel(-1 * self.velocity)
        drive3.axis1.controller.input_vel(-1 * self.velocity)

    def increaseVel(self):
        self.velocity = self.velocity + 5

    def decreaseVel(self):
        self.velocity = self.velocity - 5

    def killVel(self):
        self.velocity = 0





