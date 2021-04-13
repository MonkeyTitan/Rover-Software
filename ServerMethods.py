# imports
import socket
import sys

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
        if self.BUFFER_SIZE != 0:
            self.data = self.connection.recv(self.BUFFER_SIZE)
            self.message = str(self.data)
            print(sys.stderr, 'sending data back to the client')
            self.connection.sendall(self.data)

    def closeSocket(self):
        # Clean up the connection
        self.connection.close()