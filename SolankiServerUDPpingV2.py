'''
Created on Oct. 12, 2018

@author: solan
'''
#importing libraries for required functions
import random
from socket import *
import datetime
# Create a UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)
# to allow address reuse in socket Server
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
# Bind server to port
serverSocket.bind(('', 12005))
while True:
    try:
        # if the server doesn't get pinged by the client for 20secs, then server has to assume that the client is closed
        serverSocket.settimeout(20)
        #random no. is generated in range 0 to 10
        rand = random.randint(0, 10)
        #client packet is received
        message, address = serverSocket.recvfrom(1024)
        #message is split into sequence no. and the timestamp
        modifiedMessage = message.split(',')
        message = datetime.datetime.strptime(modifiedMessage[1],"%Y-%m-%d_%H:%M:%S")
        # Dictionary to hold packet lost count,packet receive count and timestamp
        packet= {'pac rec':0,'pac lost':0,'timestamp':0}
        packet['pac rec'] += 1
        print ('Received packet no',packet['pac rec'],'from',address,'.')
        print ('The sequence number sent with the packet was',modifiedMessage[0])
        now = datetime.datetime.now()
        #delay between client packet sent and received by the server
        response = now - message
        # Timestamp of most recent ping from client
        packet['timestamp'] = now
        # If rand is less is than 3, we consider the packet lost and do not respond
        if rand < 3:
            print ('packet lost')
            packet['pac lost']+=1
            continue
        serReply="Packet delivery delay = "+str(response)+",packets lost in between = "+ packet['pac lost']
        # server sends the response into server socket
        serverSocket.sendto(serReply, address)
        print('Sent response to',address,'with a delay of',response.total_seconds())
    except timeout:
        print('REQUEST TIMED OUT')    
#close the socket
serverSocket.close()