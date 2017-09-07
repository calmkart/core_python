#-*- coding:utf-8 -*-
from socket import *
import time
import select
import threading

HOST = ''
PORT = 22222
BUFSIZ = 1024
ADDR = (HOST, PORT)

t_server = socket(AF_INET,SOCK_STREAM)
t_server.setsockopt(SOL_SOCKET,SO_REUSEADDR, 1)
t_server.bind(ADDR)
t_server.listen(5)

t = {}


def wakeit(t_client, tm):
	t_client.send("sleep")
	for i in range(0,tm):
		print i
		time.sleep(1)
	t_client.send("wake")
	t_client.close()

while True:
	print "waiting for connection..."
	t_client, addr = t_server.accept()
	print "...connected form: ",addr
	data = t_client.recv(BUFSIZ)
	if data == "exit"
		break
	t = threading.Thread(target = wakeit(t_client, int(data)))
	t.start()

t_server.close()


