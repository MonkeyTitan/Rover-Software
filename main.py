#imports
import ServerMethods
import ControlInterpruter
import re

#Data types
backToNormal = True

#Object init
Server = ServerMethods.MakeServer()

#Execution of functions
Server.makeSocket()
Server.bindSocket()
Server.listen()
while Server.connection.recv != "shutdown":
    Server.manageCon()

    print(Server.velocity)
Server.closeSocket()


