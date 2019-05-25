'''
Created on Nov 29, 2018

@author: solan
'''
# impoting libraries
import sys
import socket
import struct
from time import ctime

#mentiniong NTP server
NTP_SERVER = "0.us.pool.ntp.org"  
TIME1970 = 2208988800
#defining SNTP client function
def sntp_client():
    #creating scoket
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = '\x1b' + 47 * '\0'
    #connecting to server
    client.sendto(data.encode(), (NTP_SERVER, 123))
    #receiving data feom ,server
    data, address = client.recvfrom(1024)
    if data:
        print ("Response received from :", address) #server address
    #current timestamp
    t = struct.unpack('!12I', data)[10]
    t -= TIME1970
    print ('\t Time=%s ' % ctime(t))

if __name__ == '__main__':
    sntp_client() # calling SNTP CLIENT