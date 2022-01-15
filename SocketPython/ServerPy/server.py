import socket # This is the module that will be used to establish the connection
              #and send data from one end to the other
import sys
import time 

## end of imports ###

s = socket.socket() # initialising the socket object allowing connections and data transfer.
host = socket.gethostname() # Initialising the server address name
print(" server will start on host : ", host)
port = 8080 # Setting the server port ( can be changed )
s.bind((host,port)) # Binding the server to the configured  host address and port.
print("")
print(" Server done binding to host and port successfully")
print("")
print("Server is waiting for incoming connections")
print("")
s.listen(1) # Listening for 1 incoming connection
conn, addr = s.accept() # Accepting any incoming connections
print(addr, " Has connected to the server and is now online ...")
print("")
while 1:
            """message = input(str(">> ")) # Gathering the input from the user as string
            message = message.encode() # Encoding the message so that it can send through the socket
            conn.send(message) # Sending the message to the connection that connected to the server
            print("message has been sent...")
            print("")"""
            incoming_message = conn.recv(1024) # Waiting to receive any incoming messages
            incoming_message = incoming_message.decode() # Decoding the incoming message into string
            print(" Client : ", incoming_message) #Displaying the incoming message
            print("")