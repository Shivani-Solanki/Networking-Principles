#import socket module
from socket import *
#import thread module
from _thread import *
import threading
import sys # In order to terminate the program
#class defined for creating separate connection for client
class clientthread(threading.Thread):
    #function defined will take arguments as connection socket and address
    def __init__(self,connectionSocket,addr):
        threading.Thread.__init__(self)
        self.connectionSocket = connectionSocket
        self.addr = addr
    # function to share requested HTTP file with the client
    def run(self):
        try:
            #message received from client
            message =self.connectionSocket.recv(2048)
            filename = message.split()[1]
            f = open(filename[1:])
            outputdata = f.read()
        #Send one HTTP header line into socket
            message1 = "    HTTP/1.1 200 OK\r\n\r\n"
            self.connectionSocket.send(message1.encode('utf-8'))
        #Send the content of the requested file to the client
            for i in range(0, len(outputdata)):
                self.connectionSocket.send(outputdata[i].encode())
            self.connectionSocket.send("\r\n".encode())
            self.connectionSocket.close()
        except IOError:
        #Send response message for file not found
            message2="HTTP/1.1 404 Not Found\r\n\r\n"
            self.connectionSocket.send(message2.encode("utf_8"))
            message3="<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n"
            self.connectionSocket.send(message3.encode("utf_8"))
        #Close client socket
            self.connectionSocket.close()    
# main thread which listens for clients at a fixed port
def mainThread():
    # server socket created
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverPort = 12026
    # to allow address reuse in socket Server
    serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    # binds local host to the server port
    serverSocket.bind(('localhost',serverPort))
    # server will listen for atleast 5 connections
    serverSocket.listen(5)
    while True:
        #connection established
        print('Ready to serve...')
        connectionSocket, addr =serverSocket.accept()
        print('connected with'+str(addr))
        #calling client thread to establish a separate thread/TCP connection for each client
        try: 
            # passing arguments for the thread
            t1 = threading.Thread(target = clientthread, args=(connectionSocket,addr))
            #starts a new thread
            t1.start()
            #wait for t1thread to finish
            t1.join()
        except:
            print ("Error: unable to start thread2")
    #closes server socket
    serverSocket.close()
#starts the main thread
try:    
    M = threading.Thread(target = mainThread)
    M.start()
    M.join()
except:
    print ("Error: unable to thread")
sys.exit()#Terminate the program after sending the corresponding data