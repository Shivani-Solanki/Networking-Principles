'''
Created on Oct. 14, 2018

@author: solan
'''
#importing libraries for required functions
import socket
import sys
#creating an client object
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#checking if the argument length is greater than 1
#if len(sys.argv)>1:
host = sys.argv[1]
port = int(sys.argv[2])
filename = sys.argv[3]
#else:
    #if the length is not command line argument are not passed than taking some default values
 #   host = 'localhost'
  #  port = 11012
file_required = '/appleworld.html'

#acquiring the hostname
clientsocket_hostname = str(socket.gethostname())
# getting the socket type
clientsocket_timeout = str(clientSocket.gettimeout())
          
#connecting to the server
clientSocket.connect((host, port))
clientsocket_peername = str(clientSocket.getpeername())
#sending the request for the file
clientSocket.send(b"GET /"+filename.encode('utf_8')+b" HTTP/1.0\n\n")
#sending the client information to the server
clientSocket.send(b"\n CLIENT INFORMATION")
clientSocket.send(b"\n CLIENT HOSTNAME: "+clientsocket_hostname.encode('utf_8'))
#receive message client socket
modifiedMess= clientSocket.recv(2048)
modifiedMess = modifiedMess.decode()
print(modifiedMess)
newMess=''
for i in len(modifiedMess):
    newMess += modifiedMess[i]
print(modifiedMess)     
    
#closing the client socket
clientSocket.close()