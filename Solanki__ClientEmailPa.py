'''
Created on Nov 11, 2018

@author: solan
'''
import ssl
import base64
from socket import *

msg = "SUBJECT: SMTP MailClient Computer Networking\nI love computer network!\n.\n\r\n"
endmsg = "\r\n.\r\n"
# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = 'smtp.gmail.com'
# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, 587))
recv = clientSocket.recv(1024).decode()
print (recv)
if recv[:3] != '220':
    print ('220 reply not received from server.')

#Send HELO command and print server response
heloCommand = 'HELO Alice\r\n'
print ("Sending First HELO")
clientSocket.sendall(heloCommand.encode())
recvhelo = clientSocket.recv(1024).decode()
print (recvhelo)

if recvhelo[:3] != '250':
    print ('250 reply not received from server.')
#sending the STARTTLS command to server and print server response
command = 'STARTTLS\r\n'
clientSocket.send(command.encode())
Rec10 = clientSocket.recv(1024).decode()
print(Rec10)
    
#Send MAIL FROM command and print server response.
#Authentication
scc = ssl.wrap_socket(clientSocket, ssl_version=ssl.PROTOCOL_SSLv23)
base64_str = ("\x00"+'shivani201290@gmail.com'+"\x00"+'ebcbcfvdudrmfdri').encode()
base64_str = base64.b64encode(base64_str)
authMsg = "AUTH PLAIN ".encode()+base64_str+"\r\n".encode()
scc.send(authMsg)
recv2 = scc.recv(1024).decode()
print (recv2)

print ("Sending MAIL FROM Command")

mailid = 'MAIL From: <shivani201290@gmail.com>\r\n'
scc.sendall(mailid.encode())
recv2 = scc.recv(1024).decode()
print (recv2)

if recv2[:3] != '250':
    print ('250 reply not received from server.')

#Send RCPT TO command and print server response.
print ("Sending RCPT TO Command")
recieptid = 'RCPT TO: <shivani201290@gmail.com>\r\n'
scc.sendall(recieptid.encode())
recv3 = scc.recv(1024).decode()
print (recv3)

if recv3[:3] != '250':
    print ('250 reply not received from server.')

#Send DATA command and print server response.
print ("Sending DATA Command")
senddata = "DATA\r\n"
scc.sendall(senddata.encode())
recv4 = scc.recv(1024).decode()
print (recv4)
if recv4[:3] != '354':
    print ('354 reply not received from server.')

# Send message data.
# Message ends with a single period.
print ("Sending Data")
#msg = "SUBJECT: SMTP Mail Client Test\nSMTP Mail Client Test\r\n.\r\n"
scc.sendall(msg.encode())
scc.sendall(endmsg.encode())
recv5 = scc.recv(1024).decode()

print (recv5)
if recv5[:3] != '250':
    print ('250 reply not received from server.')

#Send QUIT and print server response.
print ("Sending QUIT")
bye = "QUIT\r\n"
scc.sendall(bye.encode())
recv6 = scc.recv(1024).decode()
print (recv6)

if recv6[:3] != '221':
    print ('221 reply not received from server.')

print ("Mail Sent")