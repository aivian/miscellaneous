import pdb
import datetime
import time
import socket

s_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_ip = '192.168.1.91'
port = 5005

s_server.bind(('', port))

while True:
    raw_input("Done with question?")
    a = datetime.datetime.utcnow()
    start_stamp = (
        a.hour * 3600.0 +
        a.minute * 60.0 +
        a.second +
        a.microsecond / 1.0e6)

    ding = False
    first = 100000000
    answerer = ''
    while not ding:
        time.sleep(0.25)
        try:
            data = s_server.recv(100)
        except:
            data = None

        while len(data) >= 14:
            identifier = data[:5]
            stamp = float(data[5:14])

            data = data[14:]

            if start_stamp < stamp and stamp < first:
                first = stamp
                answerer = identifier
                ding = True

    print('{} answered first'.format(answerer))


