#
# ARCADEPY BY FLIPP3RRR
#
# All code is licensed under the UNLICENSE
#

sysWorks = True
osWorks = True
try:
	import sys
except:
	sysWorks = False
try:
	import tkinter as tk
except:
	if sysWorks == True:
		sys.exit("Error: Couldn't import the tkinter module, is it installed?")
	elif osWorks == True:
		os._exit()
	else:
		try:
			exit("Error: Multiple modules couldn't be loaded!")
		except:
			quit()
try:
	import os
except:
	osWorks = False
	if sysWorks == True:
		sys.exit("Error: Couldn't import the os module, is it installed?")
	elif osWorks == True:
		os._exit()
	else:
		try:
			exit("Error: Multiple modules couldn't be loaded!")
		except:
			quit()
try:
	import random
	import time
except:
	if sysWorks

if sysWorks == False:
	if osWorks == True:
		os._exit("Error: The SYS isn't imported, this could be happening because Python isn't properly installed.")
	elif osWorks == False:
		try:
			exit("Error: The SYS and OS modules aren't imported, this could be happening because Python isn't properly installed.")
		except:
			quit()