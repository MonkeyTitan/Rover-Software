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
pattern0 = re.compile('|')
pattern1 = re.compile('|')
pattern2 = re.compile('|')
pattern3 = re.compile('|')
pattern4 = re.compile('|')
pattern5 = re.compile('|')
pattern6 = re.compile('|')
pattern7 = re.compile('|')
pattern8 = re.compile('|')
pattern9 = re.compile('b')
pattern10 = re.compile('t')
pattern11 = re.compile('g')
pattern12 = re.compile('f')
pattern13 = re.compile('h')
pattern14 = re.compile('p')
pattern15 = re.compile(';')
pattern16 = re.compile('z')
pattern17 = re.compile('c')
pattern18 = re.compile('1')
pattern19 = re.compile('2')
pattern20 = re.compile('3')
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
                        Odriver.stopVel()
                for element11 in message:
                    if pattern10.search(element11):
                        Odriver.goForwardCur()
                for element12 in message:
                    if pattern11.search(element12):
                        Odriver.goBackwardCur()
                for element13 in message:
                    if pattern12.search(element13):
                        Odriver.goRightCur()
                for element14 in message:
                    if pattern13.search(element14):
                        Odriver.goLeftCur()
                for element15 in message:
                    if pattern14.search(element15):
                        Odriver.killTorque()
                for element16 in message:
                    if pattern15.search(element16):
                        Odriver.stopTorque()
                for element17 in message:
                    if pattern16.search(element17):
                        Odriver.decreaseCur()
                for element18 in message:
                    if pattern17.search(element18):
                        Odriver.increaseCur()
                for element17 in message:
                    if pattern16.search(element17):
                        Odriver.decreaseCur()
                for element18 in message:
                    if pattern17.search(element18):
                        Odriver.decreaseCur()
                for element19 in message:
                    if pattern18.search(element19):
                        Odriver.setVelControl()
                for element20 in message:
                    if pattern19.search(element20):
                        Odriver.setTorqueControl()
                for element21 in message:
                    y1Value = (re.search('startx1(.*)endx1', message))
                    y2Value = (re.search('starty1(.*)endy1', message))

                    print(Odriver.x1Value)
                    print(Odriver.y1Value)
                    if Odriver.y1Value <= 0:
                        Odriver.goBackwardCurConOne()
                    else:
                        Odriver.goForwardCurConOne()
                print(Odriver.x1Value)
                print(Odriver.y1Value)
Server.closeSocket()