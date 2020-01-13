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
	exit("Fatal error: The SYS module couldn't be imported, this could be happening because Python isn't properly installed.")

try:
	import os
except:
	osWorks = False
	exit("Fatal error: The OS module couldn't be imported, this could be happening because Python isn't properly installed.")

try:
	import tkinter as tk
	import random
	import time
except:
	sys.exit("Fatal error: One or more default imports failed, this could be happening because Python isn't properly installed.")
