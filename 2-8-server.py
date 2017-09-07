#!/usr/bin/python  
#-*- coding:utf-8 -*-
  
'test TCP server'  
  
from socket import *  
from time import ctime  
import select  
import sys  
import re
  
HOST = ''  
PORT = 22222  
BUFSIZ = 1024  
ADDR = (HOST, PORT)  
  
tcpSerSock = socket(AF_INET, SOCK_STREAM)  
tcpSerSock.setsockopt(SOL_SOCKET,SO_REUSEADDR, 1)
tcpSerSock.bind(ADDR)  
tcpSerSock.listen(5)  
input = [tcpSerSock]  
clientdict = {}
user = "No name user"
roomnumber = 0
print "start the chat server..." 



while True:  
	print 'waiting for connection...'
	rs, ws, es = select.select(input,[],[])
	for r in rs:
		if r==tcpSerSock:
			tcpCliSock, addr = tcpSerSock.accept()
			print '...connected from:',addr
			input.append(tcpCliSock)
			clientdict[tcpCliSock] = [tcpCliSock, addr, user, roomnumber]

		else:
			try:
				data = r.recv(1024)
				matchname = re.match(r'(.+)\sjoin the server',data)
				matchroom = re.match(r'Join the room(\d)',data)
				if matchname:
					for x in input:
						if x == tcpSerSock or x==r:
							pass
						else:
							if clientdict[x][2] == "No name user" or clientdict[x][3] == 0:
								pass
							else:
								x.send(data)
					username = matchname.group(1)
					clientdict[r][2] = username
					r.send("Welcome,%s"%username)
				elif matchroom:
					print '%s'%clientdict[r][2],data
					roomnumber = matchroom.group(1)
					clientdict[r][3] = roomnumber
					r.send('You join room%s'%roomnumber)
					for x in input:
						if x == tcpSerSock or x ==r:
							pass
						else:
							if clientdict[x][3] == clientdict[r][3]:
								x.send('%s join this room'%clientdict[r][2])
				elif data=='exit':
					diconnected = True
				else:
					senddata = "%s said:%s"%(clientdict[r][2], data)
					for x in input:
						if x == tcpSerSock:
							pass
						else:
							if clientdict[x][3] == clientdict[r][3]:
								x.send(senddata)
				disconnected = False

			except:
				disconnected = True

			if disconnected:
				leftdata = "%s has left"%clientdict[r][2]
				print leftdata
				for x in input:
					if x == tcpSerSock or x==r:
						pass
					else:
						x.send(leftdata)
				input.remove(r)
