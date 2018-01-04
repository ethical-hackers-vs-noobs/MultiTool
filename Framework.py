# # # # # # # # # #
#coding:UTF-8
# # # # # # # # # 

# # # # # # # #
#!/usr/bin/env python2.7
# # # # # # #

# # # # # #
# Created January 3th 2017
# Copyright (c) 2017 Beyar N.
# # # #

# # #
# Name: Framework.py
# #

# Importing Library
import os

# Colors
red = "\033[01;31m"
green = "\033[01;32m"
white = "\033[0m"

# Clear
os.system("clear")

# Manually edit these
version = 2
optKey = {
	"Network scanner automode" : "LanScan.py", 
	"Network scanner with parameters" : "PYTHON FILE NAME",
	"File server" : "PYTHON FILE NAME",
	"Port scanner" : "PortScanner.py",
	"UDP flooder" : "EHVSNFlood.py",
	"Subnet lookup" : "PYTHON FILE NAME",
	"Geo-ip" : "PYTHON FILE NAME",
	"DNS enumerator" : "PYTHON FILE NAME",
	"Convert subnet mask to CIDR mask" : "PYTHON FILE NAME",
	"SMTP auth" : "smtpAuth.py",
	"Webserver-alive" : "PYTHON FILE NAME",
	"Webserver-check" : "PYTHON FILE NAME",
}

# Shows the array only
optArr = list(optKey.keys())

# Prints banner
def banner():
	print """
.------..------..------..------.
|E.--. ||H.--. ||V.--. ||N.--. |
| (\/) || :/\: || :(): || :(): |
| :\/: || (__) || ()() || ()() |
| '--'E|| '--'H|| '--'V|| '--'N|
`------'`------'`------'`------'
	  Framework v%d
"""%(version)

# Gives options
def options():
	counter = 0
	print "Type quit to exit"
	for each in optKey:
		print "%d) %s"%(counter, each)
		counter += 1

# Clears terminal and quits
def termination():
	os.system("clear")
	print "%sTermination executed...EHVN out!%s"%(red, white)

# Running the module
def execute(indata):
	os.system("python modules/%s"%(indata))

# Menu
menu = True
while menu == True:
	os.system("clear")
	banner()
	options()
	chosen = raw_input("> ")
	try:
		output = execute(optKey[optArr[int(chosen)]])
	except (IndexError, ValueError):
		print "Choose a number between %d and %d"%(0, len(optKey)-1)
	if chosen == "quit":
		termination()
		menu = False
	else:
		continue

#http://www.techknow.one/forum/index.php?topic=9396.0
