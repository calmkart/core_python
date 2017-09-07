#-*- coding: utf-8 -*-

from socket import *

HOST ='www.calmkart.com'
PORT = 80
BUFSIZ = 1024
ADDR = (HOST, PORT)

t_client = socket(AF_INET, SOCK_STREAM)
t_client.connect(ADDR)
t_client.send('GET/ \n')
data = t_client.recv(BUFSIZ)
with open(r'wwwcalmkartcom.txt','w') as f:
    f.write(data)