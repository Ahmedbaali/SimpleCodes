import socket # This is the module that will be used to establish the connection
              #and send data from one end to the other
import sys
import time

s = socket.socket() # initialising the socket object allowing connections and data transfer.
host = input(str("Please enter the hostname of the server : ")) # Getting the host address from the users input
port = 8080 # setting the port to the same port as the server program
s.connect((host,port)) # Finally connecting to the server using the host address and the port
print(" Connected to chat server")

while 1:
            """incoming_message = s.recv(1024)# Waiting to receive any incoming messages
            incoming_message = incoming_message.decode() # Decoding the incoming message into string
            print(" Server : ", incoming_message) #Displaying the incoming message
            print("")"""
            message = input(str(">> ")) # Gathering the input from the user as string
            message = message.encode() # Encoding the message so that it can send through the socket
            s.send(message) # Sending the message to the connection that connected to the server

            print("message has been sent...")

            print("")