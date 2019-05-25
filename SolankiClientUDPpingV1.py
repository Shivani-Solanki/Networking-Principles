'''
Created on Oct. 11, 2018

@author: solan
'''
#importing libraries for required functions
import time
import socket
from pip._vendor.distlib.compat import raw_input
from _socket import timeout
from math import sqrt
import matplotlib.pyplot as plt
#sets the string serverName to hostname and serverPort to port no. of the server
serverName = "localhost"
serverPort = 12000
#input asked from the enduser
message = raw_input("Input lowercase sentence:")
#Create a UDP socket
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# list created to hold the RRTs
List_time=[] 
# to hold the no. of packets sent
sent=0 
# to hold the no. of packets received
count=0 
# 200 pings will be sent
for ping in range(200):
    #incrementing the sent counter
    sent+=1
    try:
        # timeout set for socket
        clientsocket.settimeout(2.0)
        #client start time when it sends the packet
        start = time.time()
        # attach the destination address to the message and send to clientsocket
        clientsocket.sendto(message.encode('utf-8'),(serverName, serverPort))
        #receive client packet and the server IP address
        modifiedMessage, serverAddress = clientsocket.recvfrom(1024)
        count+=1
        #client end time when it receives the packet from the server
        end = time.time()
    #exception
    except timeout:
        print('REQUEST TIMED OUT')
    else:
        #each RTT is added to the list
        List_time.append(end-start)
        #printing the message received from server, no. of pings and RTT for each packet.
        print(f'{modifiedMessage} {ping} ms:'+ str(end-start))
#calculation for standard deviation
totalSum=0
for i in range (len(List_time)):
    totalSum+= (List_time[i]-(sum(List_time)/len(List_time)))**2
underRoot= totalSum/len(List_time)
SD=sqrt(underRoot)
# calculated and printed RTT min.,max. and ave.
print('The round trip times in milli-seconds: Minimum='+str(min(List_time))+ ', Maximum='+str(max(List_time))+', Average='+ str(sum(List_time)/len(List_time)))
# print standard deviation
print('The Standard Deviation :'+ str(SD))
# calculated and Printed packet loss %
print('packets sent:'+str(sent)+', packets lost:'+str(sent-count)+', loss rate:'+str((1-(count/sent))*100)+'%')
#plotting histogram for RRT
#defined bins, title, x-axis and y-axis label
plt.hist(List_time,bins=20)
plt.title('RTTS')
plt.xlabel('RTT range(milliseconds)')
plt.ylabel('no. of RTTs') 
plt.show()
#closes the socket
clientsocket.close()