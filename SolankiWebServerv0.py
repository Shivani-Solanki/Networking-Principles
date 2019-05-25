'''
Created on Oct. 13, 2018

@author: solan
'''
#import socket module
from socket import *
import sys # In order to terminate the program
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
serverPort = 60000
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
#binds the socket with the server port
serverSocket.bind(('localhost', serverPort))
#server listens to atleast one connection
serverSocket.listen(1)
while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr =serverSocket.accept()
    try:
        #received message extracted from connection socket
        message =connectionSocket.recv(2048)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        #Send one HTTP header line into socket
        message1 = b"HTTP/1.1 200 OK\r\n\r\n"
        #sends message into client socket
        connectionSocket.send(message1)
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        #Send response message for file not found 
        message2=b"HTTP/1.1 404 Not Found\r\n\r\n"
        connectionSocket.send(message2)
        message2=b"HTTP/1.1 404 Not Found\r\n\r\n"
        connectionSocket.send(message2)
        #message3="<html>%s<head>%s</head>%s<body>%s<h1>404 Not Found</h1>%s</body>%s</html>\r\n"
        #connectionSocket.send(message3.encode("utf_8"))
        #Close client socket
        connectionSocket.close()
#closes server socket
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data