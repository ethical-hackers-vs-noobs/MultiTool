# # # # # # # # # #
#coding:UTF-8
# # # # # # # # # 

# # # # # # # #
#!/usr/bin/env python2.7
# # # # # # #

# # # # # #
# Created Janury 7th 2018
# Copyright (c) 2017 Beyar N.
# # # #

# # #
# Name: argv.py
# #

# Importing Library
import os
import sys

# sys.argv[0] is the script name
try:
	counter = 1
	sys.argv.pop(0)
	for each in sys.argv:
		print "Your %sth argument: %s" %(counter, each)
		counter += 1
except IndexError:
	print "Usage: %s argument" %(sys.argv[0])
