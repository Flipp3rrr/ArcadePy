#
# ARCADEPY BY FLIPP3RRR
#
# All code is licensed under the UNLICENSE
#

# Imports
try:
	import tkinter as tk
except:
	exit("Fatal error: One or more imports failed, this could be happening because Python isn't properly installed.")

try:
	import os
except:
	exit("Error: Couldn't import the os module, is it installed?")

# Get script folder
base_folder = os.path.dirname(__file__)

# Get needed paths and directories
pong_path = os.path.join(base_folder, "games/pong.py")

# Make life easier
root = tk.Tk()

# Pong
def PongCallback():
	print("WARN: Pong is WIP!")
	exec(open(pong_path).read())

# Exit
def ExitCallback():
	exit()

logo_path = os.path.join(base_folder, "images/PythonLogoTiny.png")
logo = tk.PhotoImage(file=logo_path)

# Root widget content
root.title("ArcadePy Launcher")
root.resizable(0, 0)
PythonLogoWidget = tk.Label(root, image=logo).pack(side="left")
DescriptionText = "ArcadePy is a small suite of arcade games written in Python."
DescriptionTextWidget = tk.Label(root, justify=tk.LEFT, padx = 10, text=DescriptionText).pack(side="left")
ExitButtonWidget = tk.Button(root, text="Exit", command=ExitCallback).pack(side="bottom")
PongButtonWidget = tk.Button(root, text="Play Pong", command=PongCallback).pack(side="bottom")

# Show startup screen
root.mainloop()
