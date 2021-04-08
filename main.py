#imports
import ClientMethods

#Object creation
Client = ClientMethods.MakeClient()

#Fuction execution
Client.makeSocket()
Client.connectToSock()
Client.manageCon()
Client.closeSocket()
