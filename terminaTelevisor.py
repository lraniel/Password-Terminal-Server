import os
import socket

HOST = ''
port = 3034
udp = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
orig = (HOST, port)
udp.bind(orig)

while True:
    msg = udp.recvfrom(1024)
    print(msg[0])