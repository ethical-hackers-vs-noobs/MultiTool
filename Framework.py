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
	"Argument test" : "argv.py"
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
	print "[Type quit to exit]"
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

def exeparam(indata, param):
	os.system("python modules/%s %s"%(indata, param))

# Menu
# The option method puts integer next to assigned string
# optKey only takes strings to find the file for it
# optArr only take integers to find the definition for it

# Print the banner before the menu
banner()

# output is what shows the status
output = "Type options to get the commands"

menu = True
while menu == True:
	
	print "[Console] %s" %output
	chosen = raw_input("> ")

	print
	arrChosen = chosen.split(" ")
	paramDelLast = chosen.split(" ")
	paramDelLast.pop(0)
	paramChosen = " ".join(map(str, paramDelLast))

	try:
		if len(arrChosen) == 1 and len(paramDelLast) == 0:
			execute(optKey[optArr[int(chosen)]])
		elif len(arrChosen) > 1 and len(paramDelLast) > 0:
			exeparam(optKey[optArr[int(arrChosen[0])]], paramChosen)

	except (IndexError):
		output = "Choose a number between %d and %d" %(0, len(optKey)-1)

	except (ValueError):
		if chosen == "quit":
			termination()
			break
		elif chosen == "banner":
			banner()
		elif chosen == "options":
			os.system("reset")
			options()

#http://www.techknow.one/forum/index.php?topic=9396.0
