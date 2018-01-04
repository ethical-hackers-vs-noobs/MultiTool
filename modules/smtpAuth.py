import os
import smtplib
import sys, argparse

def main(args):
	try:
		print smtp_auth(args.server, args.port, args.username, args.password)
	except:
		usage()

def banner():
	print "#################################"
	print "#       smtp_authcheck.py       #"
	print "#        by: sneakerhax         #"
	print "#################################"

def usage():
	#print "Usage: python smtpAuth.py --server <mail server> --port <SMTP port> --username <username> --password <password>"
	serverin = raw_input("Server: ")
	portin = raw_input("Port: ")
	userin = raw_input("Username: ")
	passin = raw_input("Password: ")
	os.system("python smtpAuth.py --server %s --port %s --username %s --password %s" %(serverin, portin, userin, passin))

def smtp_auth(server, port, username, password):
	s = smtplib.SMTP(server, port)
	s.starttls()
	s.settimeout(3)
	try:
		s.login(username, password)
		print "Authentication successful"
	except smtplib.SMTPAuthenticationError:
		print "Wrong username or password"

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("--server", action="store", dest='server', help="server address")
	parser.add_argument("--port", action="store", dest='port', help="server port", type=int)
	parser.add_argument("--username", action="store", dest='username', help="username")
	parser.add_argument("--password", action="store", dest='password', help="password")
	args = parser.parse_args()
	print "\n"
	banner()
	main(args)

