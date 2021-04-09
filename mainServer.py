#imports
import OdriveCommands
import ServerMethods
import ServoCommands
import re

#Object creation
Server = ServerMethods.MakeServer()
Odriver = OdriveCommands.Odriver()

#Data types
pattern0 = re.compile('@')
pattern1 = re.compile('!')
pattern2 = re.compile('o')
pattern3 = re.compile('l')
pattern4 = re.compile('w')
pattern5 = re.compile('s')
pattern6 = re.compile('a')
pattern7 = re.compile('d')
pattern8 = re.compile('x')
pattern9 = re.compile('b')
backToNormal = True

#Fuction execution
Server.makeSocket()
Server.bindSocket()
Server.listen()
while Server.message != "shutdown":
    Server.manageCon()
    for element1 in Server.message:
        if pattern0.search(element1):
            print("Entering remote control mode 1")
            backToNormal = False
    if not backToNormal:
        while not backToNormal:
            if Server.BUFFER_SIZE != 0:
                Server.data = Server.connection.recv(Server.BUFFER_SIZE)
                message = str(Server.data)
                for element2 in message:
                    if pattern1.search(element2):
                        backToNormal = True
                        print("Going back to regular control.")
                        break
                for element3 in message:
                    if pattern2.search(element3):
                        Odriver.increaseVel()
                for element4 in message:
                    if pattern3.search(element4):
                        Odriver.decreaseVel()
                for element5 in message:
                    if pattern4.search(element5):
                        Odriver.goForwardVel()
                for element6 in message:
                    if pattern5.search(element6):
                        Odriver.goBackwardVel()
                for element7 in message:
                    if pattern6.search(element7):
                        Odriver.goLeftVel()
                for element8 in message:
                    if pattern7.search(element8):
                        Odriver.goRightVel()
                for element9 in message:
                    if pattern8.search(element9):
                        Odriver.killVel()
                for element10 in message:
                    if pattern9.search(element10):
                        Odriver.stop()
Server.closeSocket()