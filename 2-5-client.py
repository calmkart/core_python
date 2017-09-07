#-*- coding: utf-8 -*-

from socket import *

HOST = '127.0.0.1'
PORT = 22222
BUFSIZE = 1024
ADDR = (HOST, PORT)

t_client = socket(AF_INET, SOCK_STREAM)
t_client.setblocking(1)
t_client.connect(ADDR)

while True:
    data = input('> ')
    if not data:
        break
    t_client.send(bytes(data, 'utf-8'))
    data = t_client.recv(BUFSIZE)
    if not data:
        break
    print("[server]:"+data.decode('utf-8'))

t_client.close()
