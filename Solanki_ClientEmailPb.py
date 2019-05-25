'''
Created on Nov 9, 2018

@author: solan
'''
import smtplib
from time import sleep
# Choose a mail server (e.g. Google mail server) and call it mailserver
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

sender = 'shivani201290@gmail.com'
password = "uywhxooncyiekuly"
recipient = 'shivani201290@gmail.com'
subject = 'My Assignment for Computer Networking'
body = "I love computer networks!"
headers = ["From: " + sender,
           "Subject: " + subject,
           "To: " + recipient,
           "MIME-Version: 1.0",
           "Content-Type: text/html"]
headers = "\r\n".join(headers)
session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT);
#Sending Help 
session.ehlo()
#Starting TLS
print("start tls...")
session.starttls()      # tls , secured
#then sending helo
session.ehlo()
print("Logging in e-mail account...")
session.login(sender, password)
print("Sending e-mail...")
session.sendmail(sender, recipient, headers + "\r\n\r\n" + body)
print("e-mail sent")
#quiting the session
sleep(2);               #prevent to soon to quit before sendmail terminate properly
session.quit()
