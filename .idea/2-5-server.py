#-*- coding: utf-8 -*-
import os
from socket import *
from time import ctime

HOST = '127.0.0.1'
PORT = 22222
BUFSIZE = 1024
ADDR = (HOST, PORT)

t_server = socket(AF_INET, SOCK_STREAM)
t_server.setblocking(1)
t_server.bind(ADDR)
t_server.listen(5)

while True:
    print('等待用户连接.....')
    t_client, addr = t_server.accept()
    print('连接到用户:',addr)

    while True:
        data = t_client.recv(BUFSIZE)
        if not data:
            break
        if data.decode('utf-8') == 'sys.date':
            t_client.send(bytes('['+ctime()+']','utf-8'))
        elif data.decode('utf-8') == 'sys.os':
            t_client.send(bytes('['+os.name+']','utf-8'))
        elif data.decode('utf-8') == 'sys.ls':
            t_client.send(bytes('['+str(os.listdir())+']','utf-8'))
        else:
            print("[client "+str(addr)+"]:"+bytes.decode(data))
            msg = input("> ")
            t_client.send(bytes(msg,'utf-8'))
    t_client.close()
t_server.close()
