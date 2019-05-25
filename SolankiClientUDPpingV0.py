'''
Created on Oct. 11, 2018

@author: solan
'''
#importing libraries for required functions
import time
import socket
from pip._vendor.distlib.compat import raw_input
from _socket import timeout
#sets the string serverName to hostname and serverPort to port no. of the server
serverName = "localhost"
serverPort = 12000
#input asked from the enduser
message = raw_input("Input lowercase sentence:")
#Create a UDP socket
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#will send 10 pings
for ping in range(10):
    try:
        # timeout set for socket
        clientsocket.settimeout(2.0)
        #client start time when it sends the packet
        start = time.time()
        # attach the destination address to the message and send to clientsocket
        clientsocket.sendto(message.encode('utf-8'),(serverName, serverPort))
        #receive client packet and the server IP address
        modifiedMessage, serverAddress = clientsocket.recvfrom(1024)
        #client end time when it receives the packet from the server
        end = time.time()
    except timeout:
        print('REQUEST TIMED OUT')
    else:
        #printing the message received from server, no. of pings and RTT for each packet.
        print(f'{modifiedMessage} {ping} ms:'+ str(end-start))
#closes the socket
clientsocket.close()