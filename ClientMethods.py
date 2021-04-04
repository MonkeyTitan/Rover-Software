# imports
import socket
import sys
import keyboard


# Class creation
class MakeClient:
    def __init__(self):
        # Data members
        self.sock = 1
        self.server_address = ('192.168.0.187', 10000)
        self.message = ""
        self.control = False
        self.VelocitySetpoint = 0
        self.key1 = 'c'
        self.key2 = 'o'
        self.key3 = 'l'
        self.key4 = 'x'
        self.key5 = 'w'
        self.key6 = 's'
        self.key7 = 'a'
        self.key8 = 'd'
        self.key9 = 'b'
        self.keypress1 = False
        self.keypress2 = False
        self.keypress3 = False
        self.keypress4 = False
        self.keypress5 = False
        self.keypress6 = False
        self.keypress7 = False
        self.keypress8 = False
        self.keypress9 = False

    # Function creation
    def makeSocket(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connectToSock(self):
        print(sys.stderr, 'connecting to %s port %s' % self.server_address)
        self.sock.connect(self.server_address)

    def manageCon(self):
        while self.message != 'stopServer':
            # Send data
            self.message = raw_input("Input: ")
            if (self.message == 'remote_control'):
                print('Entering remote control mode')
                self.control = True
                self.sock.sendall('@')
                while self.control == True:
                    if keyboard.is_pressed('p'):
                        print
                        response = raw_input('Please enter "quit" to get out of controller mode: ')
                        if response == 'quit':
                            self.sock.sendall('!')
                            self.control = False
                            print('Leaving remote control mode')
                            break
                        else : continue

                    if self.keypress2 and not keyboard.is_pressed(self.key2):
                        self.VelocitySetpoint = (self.VelocitySetpoint + 1)
                        self.message = 'o'
                        self.sock.sendall(self.message)
                        print('')
                        print('The throttle is at: ' + str(self.VelocitySetpoint) + ' Turns a second')
                        self.keypress2 = False
                    elif keyboard.is_pressed(self.key2) and not self.keypress2:
                        self.keypress2 = True

                    if self.keypress3 and not keyboard.is_pressed(self.key3):
                        self.VelocitySetpoint = (self.VelocitySetpoint - 1)
                        self.message = 'l'
                        self.sock.sendall(self.message)
                        print('')
                        print('The throttle is at: ' + str(self.VelocitySetpoint) + ' Turns a second')
                        self.keypress3 = False
                    elif keyboard.is_pressed(self.key3) and not self.keypress3:
                        self.keypress3 = True

                    if self.keypress4 and not keyboard.is_pressed('x'):
                        self.VelocitySetpoint = 0
                        self.message = 'x'
                        self.sock.sendall(self.message)
                        print('')
                        print('The throttle reset to: ' + str(self.VelocitySetpoint) + ' Turns a second')
                        self.keypress4 = False
                    elif keyboard.is_pressed(self.key4) and not self.keypress4:
                        self.keypress4 = True

                    if self.keypress1 and not keyboard.is_pressed(self.key1):
                        print('')
                        print('The throttle is at: ' + str(self.VelocitySetpoint) + ' Turns a second')
                        self.keypress1 = False
                    elif keyboard.is_pressed(self.key1) and not self.keypress1:
                        self.keypress1 = True

                    if self.keypress5 and not keyboard.is_pressed(self.key5):
                        self.message = 'w'
                        print('')
                        self.sock.sendall(self.message)
                        self.keypress5 = False
                    elif keyboard.is_pressed(self.key5) and not self.keypress5:
                        self.keypress5 = True

                    if self.keypress6 and not keyboard.is_pressed(self.key6):
                        self.message = 's'
                        print('')
                        self.sock.sendall(self.message)
                        self.keypress6 = False
                    elif keyboard.is_pressed(self.key6) and not self.keypress6:
                        self.keypress6 = True

                    if self.keypress7 and not keyboard.is_pressed(self.key7):
                        self.message = 'a'
                        print('')
                        self.sock.sendall(self.message)
                        self.keypress7 = False
                    elif keyboard.is_pressed(self.key7) and not self.keypress7:
                        self.keypress7 = True

                    if self.keypress8 and not keyboard.is_pressed(self.key8):
                        self.message = 'd'
                        print('')
                        self.sock.sendall(self.message)
                        self.keypress8 = False
                    elif keyboard.is_pressed(self.key8) and not self.keypress8:
                        self.keypress8 = True

                    if self.keypress9 and not keyboard.is_pressed(self.key9):
                        self.message = 'c'
                        print('')
                        print('stopping')
                        self.sock.sendall(self.message)
                        self.keypress9 = False
                    elif keyboard.is_pressed(self.key9) and not self.keypress9:
                        self.keypress9 = True

            else:
                print(sys.stderr, 'sending "%s"' % self.message)
                self.sock.sendall(self.message)

                # Look for the response
                amount_received = 0
                amount_expected = len(self.message)

                while amount_received < amount_expected:
                    data = self.sock.recv(16)
                    amount_received += len(data)
                    print(sys.stderr, 'received "%s"' % data)

    def closeSocket(self):
        print(sys.stderr, 'closing socket')
        self.sock.close()
