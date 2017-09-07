#-*- coding:utf-8 -*-

from socket import *

HOST = '10.32.80.118'
PORT = 22222
BUFSIZE = 1024
ADDR = (HOST, PORT)

while True:
	t_client = socket(AF_INET, SOCK_STREAM)
	t_client.connect(ADDR)
	time = raw_input("输入你要睡眠的时间: ")
	t_client.send(time)
	data = t_client.recv(BUFSIZE)
	if data == "exit":
		break
	if data == "sleep":
		print "我TM开始睡觉了"
	data = t_client.recv(BUFSIZE)
	if data == "wake":
		print "他TM又起床了"

t_client.close()
