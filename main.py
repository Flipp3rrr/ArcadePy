#
# ARCADEPY BY FLIPP3RRR
#
# All code is licensed under the UNLICENSE
#

# Imports for launcher
sysWorks = True
osWorks = True
try:
	import sys
except:
	sysWorks = False
try:
	import tkinter as tk
except:
	sys.exit("Error: Couldn't import the tkinter module, is it installed?")
try:
	import os
except:
	osWorks = False
	if sysWorks == True:
		sys.exit("Error: Couldn't import the os module, is it installed?")

if sysWorks == False:
	if osWorks == True:
		os._exit("Error: The SYS isn't imported, this could be happening because Python isn't properly installed.")
	elif osWorks == False:
		try:
			exit("Error: The SYS and OS modules aren't imported, this could be happening because Python isn't properly installed.")
		except:
			quit()


# Get script folder
base_folder = os.path.dirname(__file__)

# Make life easier
root = tk.Tk()

# Pong script
def PongCallback():
	print("Pong is work in progress! It may not function properly!")

# Exit script
def ExitCallback():
	sys.exit("Thanks for playing!")

# Get logo directory
logo_path = os.path.join(base_folder, "images/PythonLogoTiny.png")
logo = tk.PhotoImage(file=logo_path)

# Root widget content
root.title("ArcadePy Launcher")
root.resizable(0, 0)
PythonLogoWidget = tk.Label(root, image=logo).pack(side="left")
DescriptionText = """ArcadePy is a small suite of arcade games written in Python."""
DescriptionTextWidget = tk.Label(root, justify=tk.LEFT, padx = 10, text=DescriptionText).pack(side="left")
ExitButtonWidget = tk.Button(root, text="Exit", command=ExitCallback).pack(side="bottom")
PongButtonWidget = tk.Button(root, text="Play Pong", command=PongCallback).pack(side="bottom")

# Show startup screen
root.mainloop()
