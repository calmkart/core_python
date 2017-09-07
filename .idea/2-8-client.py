#-*- coding: utf-8 -*-

from socket import *
import select
import sys

HOST = '127.0.0.1'
PORT = 22222
BUFSIZ = 1024
ADDR = (HOST, PORT)

t_client= socket(AF_INET, SOCK_STREAM)
t_client.connect(ADDR)

inputs = [t_client,sys.stdin]

while True:
    rs,ws,es = select.select(inputs,[],[])
    for r in rs:
        if r==t_client:
            data = t_client.recv(BUFSIZ)
            print(bytes.decode(data))
            if data==b'exit':
                break
        else:
            data = input('>')
            if data=='exit':
                t_client.send(bytes("用户退出连接！",'utf-8'))
                break
            t_client.send(bytes(data,'utf-8'))
        if data=='exit' or data==b'exit':
            break
t_client.close()
