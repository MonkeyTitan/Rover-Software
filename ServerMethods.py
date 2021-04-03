# imports
import socket
import sys
import odrive
import time
import math
import re
import ControlInterpruter

# Class creation
class MakeServer:
    def __init__(self):
        # Data types
        self.server_address = ('192.168.0.187', 10000)
        self.sock = 1
        self.client_address = 1
        self.connection = 1
        self.data = ""
        self.BUFFER_SIZE = 1024
        self.message = str(self.data)
        self.backToNormal = True
        self.velocity = 0.0
        self.drive1 = odrive.find_any(serial_number='2069388F304E')  # left
        self.drive2 = odrive.find_any(serial_number='20683882304E')
        self.drive3 = odrive.find_any(serial_number='207F3890304E')  # right

    def getBusVoltage(self):
        print(str(self.drive1.vbus_voltage))
        print(str(self.drive2.vbus_voltage))
        print(str(self.drive3.vbus_voltage))

    def goForward(self):
        self.drive1.axis0.controller.input_vel = (-1 * self.velocity)
        self.drive1.axis1.controller.input_vel = (-1 * self.velocity)
        self.drive3.axis0.controller.input_vel = (self.velocity)
        self.drive3.axis1.controller.input_vel = (self.velocity)

    def goBackward(self):
        self.drive1.axis0.controller.input_vel = (self.velocity)
        self.drive1.axis1.controller.input_vel = (self.velocity)
        self.drive3.axis0.controller.input_vel = (-1 * self.velocity)
        self.drive3.axis1.controller.input_vel = (-1 * self.velocity)

    def goLeft(self):
        self.drive1.axis0.controller.input_vel = (self.velocity)
        self.drive1.axis1.controller.input_vel = (self.velocity)
        self.drive3.axis0.controller.input_vel = (self.velocity)
        self.drive3.axis1.controller.input_vel = (self.velocity)

    def goRight(self):
        self.drive1.axis0.controller.input_vel = (-1 * self.velocity)
        self.drive1.axis1.controller.input_vel = (-1 * self.velocity)
        self.drive3.axis0.controller.input_vel = (-1 * self.velocity)
        self.drive3.axis1.controller.input_vel = (-1 * self.velocity)

    def increaseVel(self):
        self.velocity = self.velocity + 1.0

    def decreaseVel(self):
        self.velocity = self.velocity - 1.0

    def killVel(self):
        self.drive1.axis0.controller.input_vel = (0.0)
        self.drive1.axis1.controller.input_vel = (0.0)
        self.drive3.axis0.controller.input_vel = (0.0)
        self.drive3.axis1.controller.input_vel = (0.0)
        self.velocity = 0.0

    # Create TCP Socket
    def makeSocket(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the Socket to the Port
    def bindSocket(self):
        print(sys.stderr, 'starting up on %s port %s' % self.server_address)
        self.sock.bind(self.server_address)

    # Listen for incoming connections
    def listen(self):
        self.sock.listen(1)

        while self.connection == 1:
            # Wait for a connection
            print(sys.stderr, 'waiting for a connection')
            self.connection, client_address = self.sock.accept()
            print(sys.stderr, 'connection from', self.client_address)

    # Observe connection
    def manageCon(self):
        # Receive the data in small chunks and retransmit it
        pattern0 = re.compile('@')
        pattern1 = re.compile('!')
        pattern2 = re.compile('o')
        pattern3 = re.compile('l')
        pattern4 = re.compile('w')
        pattern5 = re.compile('s')
        pattern6 = re.compile('a')
        pattern7 = re.compile('d')
        pattern8 = re.compile('x')

        if self.BUFFER_SIZE != 0:
            self.data = self.connection.recv(self.BUFFER_SIZE)
            message = str(self.data)
            for element1 in message:
                if pattern0.search(element1):
                    print("Entering remote control mode 1")
                    self.backToNormal = False
            if not self.backToNormal:
                while not self.backToNormal:
                    if self.BUFFER_SIZE != 0:
                        self.data = self.connection.recv(self.BUFFER_SIZE)
                        message = str(self.data)
                        for element2 in message:
                            if pattern1.search(element2):
                                self.backToNormal = True
                                print("Going back to regular control.")
                                break
                        for element3 in message:
                            if pattern2.search(element3):
                                self.increaseVel()
                        for element4 in message:
                            if pattern3.search(element4):
                                self.decreaseVel()
                        for element5 in message:
                            if pattern4.search(element5):
                                self.goForward()
                        for element6 in message:
                            if pattern5.search(element6):
                                self.goBackward()
                        for element7 in message:
                            if pattern6.search(element7):
                                self.goLeft()
                        for element8 in message:
                            if pattern7.search(element8):
                                self.goRight()
                        for element9 in message:
                            if pattern8.search(element9):
                                self.killVel()

            print(sys.stderr, 'sending data back to the client')
            self.connection.sendall(self.data)

    def closeSocket(self):
        # Clean up the connection
        self.connection.close()
