# Imports
import tkinter as tk
import os
import sys

# Get script folder
base_folder = os.path.dirname(__file__)

# Create root widget
root = tk.Tk()

# Exit script
def ExitCallback():
	sys.exit("Thanks for playing!")

# Pong script
def PongCallback():
	print("Pong is work in progress!")

# Get logo directory
logo_path = os.path.join(base_folder, "images/PythonLogoTiny.png")
logo = tk.PhotoImage(file=logo_path)
PythonLogoWidget = tk.Label(root, image=logo).pack(side="left")
DescriptionText = """ArcadePy is a small suite of arcade games written in Python."""
DescriptionTextWidget = tk.Label(root, justify=tk.LEFT, padx = 10, text=DescriptionText).pack(side="left")
PongButtonWidget = tk.Button(root, justify=tk.CENTER, text="Play Pong", command=PongCallback).pack(side="bottom")
ExitButtonWidget = tk.Button(root, justify=tk.CENTER, text="Exit", command=ExitCallback).pack(side="bottom")
root.mainloop()

# Make startup screen the correct size
StartupScreen.pack()

# Show startup screen
root.mainloop()