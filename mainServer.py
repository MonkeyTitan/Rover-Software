#imports
import OdriveCommands
import ServerMethods
import ServoCommands
import re

#Object creation
Server = ServerMethods.MakeServer()
Odriver = OdriveCommands.Odriver()
Servo = ServoCommands.Servo()

#Data types
pattern0 = re.compile('@')
pattern1 = re.compile('!')
pattern2 = re.compile('{')
pattern3 = re.compile('}')
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
                for element in message:
                    if pattern1.search(element):
                        backToNormal = True
                        print("Going back to regular control.")
                        break
                for element in message:
                    if pattern2.search(element):
                        Odriver.setVelControl()
                for element in message:
                    if pattern3.search(element):
                        Odriver.setTorqueControl()
                for element in message:
                    y1Value = (re.search('startx1(.*)endx1', message))
                    y2Value = (re.search('starty1(.*)endy1', message))
                    Odriver.x1Value
                    print(Odriver.x1Value)
                    print(Odriver.y1Value)
                    if Odriver.y1Value <= 0:
                        Odriver.goBackwardCurConOne()
                    else:
                        Odriver.goForwardCurConOne()
                print(Odriver.x1Value)
                print(Odriver.y1Value)
Server.closeSocket()