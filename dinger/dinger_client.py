import datetime
import time
import socket

s_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_ip = '192.168.1.91'
port = 5005

name = raw_input("your name?\n")
if len(name) < 5:
    name += ' '*(5-len(name))
if len(name) > 5:
    name = name[:5]

while True:
    raw_input("ding in?")
    a = datetime.datetime.utcnow()
    stamp = (
        a.hour * 3600.0 +
        a.minute * 60.0 +
        a.second +
        a.microsecond / 1.0e6)
    pkt = '{}{:9.2f}'.format(name, stamp)
    s_client.sendto(pkt, (server_ip, port))

