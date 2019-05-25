'''
Created on Oct. 12, 2018

@author: solan
'''
#importing libraries for required functions
import socket
from pip._vendor.distlib.compat import raw_input
from _socket import timeout
import datetime
#sets the string serverName to hostname and serverPort to port no. of the server
serverName = "localhost"
serverPort = 12005
#Create a UDP socket
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sent=0 # to count number of pings sent
receive =0 # to count number of pings received
seq=1 # Initialize the sequence 
for ping in range(10):
    try:
        clientsocket.settimeout(5) # timeout set for socket
        now=datetime.datetime.now()
        # message created with 1st part as sequence no. and 2nd as timestamp separated by comma 
        message = str(seq),str(now)
        # attach the destination address to the message and send to clientsocket
        clientsocket.sendto(message.encode('utf-8'),(serverName, serverPort))
        sent+=1
        #receive client packet and the server IP address
        modifiedMessage, serverAddress = clientsocket.recvfrom(1024)
        receive+=1
        seq+=1 #sequence incremented
    except timeout:
        print('REQUEST TIMED OUT')
print('The packets sent:'+str(sent)+'packets received:'+str(receive),'sequence:'+str(seq))
#closes the socket
clientsocket.close()