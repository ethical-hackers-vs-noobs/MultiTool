import socket
import sys
import time

def port_scanner(url,ports):
	try:
		print "[+] Connecting to: " + url + " port: " + str(ports) +" [+]"
		s = socket.socket()
		s.connect((url,int(ports)))
		sock.settimeout(5)
		s.send('EHVN \n')
		banner = s.recv(1024)
		if banner:
			print "[+] Port " +str(ports)+ " open [+] \n"+ banner
			s.close()
			time.sleep(2)
	except:
		print "[+] Port " +str(ports)+ " closed [+] \n"
		time.sleep(2)


def main():
	url = raw_input("IP: ")
	ports = raw_input("Port: ")
	port_scanner(url, ports)
	
if __name__ == "__main__":
    main()
