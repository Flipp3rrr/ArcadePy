# Imports
import tkinter as tk
import os

# Get script folder
base_folder = os.path.dirname(__file__)

# Create root widget
root = tk.Tk()

# Get logo directory
logo_path = os.path.join(base_folder, "images/PythonLogoTiny.png")
logo = tk.PhotoImage(file=logo_path)
w1 = tk.Label(root, image=logo).pack(side="left")
description = """ArcadePy is a small suite of arcade games written in Python."""
w2 = tk.Label(root, 
              justify=tk.LEFT,
              padx = 10, 
              text=description).pack(side="left")
root.mainloop()

# Make startup screen the correct size
StartupScreen.pack()

# Show startup screen
root.mainloop()