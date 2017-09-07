#-*- coding: utf-8 -*-
import os
from socket import *
from time import ctime
import select
import sys

HOST = '127.0.0.1'
PORT = 22222
BUFSIZE = 1024
ADDR = (HOST, PORT)

t_server = socket(AF_INET, SOCK_STREAM)
t_server.setblocking(1)
t_server.bind(ADDR)
t_server.listen(5)

inputs = [t_server,sys.stdin]

while True:
    print('等待连接')
    t_client, addr = t_server.accept()
    print(str(addr)+"连接到服务器")
    inputs.append(t_client)

    while True:
        rs,ws,es = select.select(inputs,[],[])
        for r in rs:
            if r==t_client:
                data = t_client.recv(BUFSIZE)
                print(bytes.decode(data))
                if data==b'exit':
                    inputs.remove(t_client)
                    break
            else:
                data = input('>')
                if data=="exit":
                    t_client.send(bytes("服务端关闭连接！",'utf-8'))
                    inputs.remove(t_client)
                    break
                t_client.send(bytes(data,'utf-8'))
        if data=='exit' or data==b'exit':
            break
    t_client.close()
t_server.close()


