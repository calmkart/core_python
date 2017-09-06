#!/usr/bin/python  
#-*- coding:utf-8 -*-

import threading
from socket import *
from time import sleep

HOST = '10.32.80.118'
PORT = 22222
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET,SOCK_STREAM)
#tcpCliSock.setsockopt(SOL_SOCKET,SO_REUSEADDR, 1)
tcpCliSock.connect(ADDR)
username = raw_input("Please set your username:") 
tcpCliSock.send("%s join the server"%username)
data = tcpCliSock.recv(BUFSIZ)
print data
room = raw_input("Input room bumber (1-9):")
tcpCliSock.send("Join the room%s"%room)
data = tcpCliSock.recv(BUFSIZ)
print data

class handle(object):
	def __init__(self):
		self._running = True

	def send(self):
		while self._running:
			data = raw_input('>')
			tcpCliSock.send(data)
			if data=='exit':
				self._running = False
	def recv(self):
		while self._running:
			data = tcpCliSock.recv(BUFSIZ)
			print data
			print '>',

handles = handle()

t1 = threading.Thread(target = handles.send())
t2 = threading.Thread(target = handles.recv())
t1.start()
t2.start()
t1.join()
t2.join()

tcpCliSock.close()
