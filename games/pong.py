#
# ARCADEPY BY FLIPP3RRR
#
# All code is licensed under the UNLICENSE
#

# Imports
try:
	import os
except:
	exit("Fatal error: The OS module couldn't be imported, this could be happening because Python isn't properly installed.")

try:
	import tkinter as tk
	import random
	import time
except:
	exit("Fatal error: One or more imports failed, this could be happening because Python isn't properly installed.")

# Keep score
score = 0

# Quit game
def quitGame():
	exit()

# Ball class
class Ball:
	def __init__(self, canvas, color, paddle):
		self.canvas = canvas
		self.paddle = paddle
		self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
		self.canvas.move(self.id, 245, 100)
		starts = [-3, -2, -1, 1, 2, 3]
		random.shuffle(starts)
		self.x = starts[0]
		self.y = -3
		self.canvas_height = self.canvas.winfo_height()
		self.canvas_width = self.canvas.winfo_width()
		self.hit_bottom = False
	
	# Paddle detection
	def hit_paddle(self, pos):
		paddle_pos = self.canvas.coords(self.paddle.id)
		if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
			if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
				return True
			return False

	def draw(self):
		global score
		self.canvas.move(self.id, self.x, self.y)
		pos = self.canvas.coords(self.id)
		if pos[1] <= 0:
			self.y = 4

		# Detect hit bottom
		if pos[3] >= self.canvas_height:
			self.hit_bottom = True
		
		# Detect hit paddle
		if self.hit_paddle(pos) == True:
			self.y = -4
			score = score + 1
			return score

		if pos[0] <= 0:
			self.x = 4
		if pos[2] >= self.canvas_width:
			self.x = -4

# Paddle class
class Paddle:
	def __init__(self, canvas, color):
		self.canvas = canvas
		self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
		self.canvas.move(self.id, 250, 500)
		self.x = 0
		self.canvas_width = self.canvas.winfo_width()
		self.canvas.bind_all("<KeyPress-Left>", self.go_left)
		self.canvas.bind_all("<KeyPress-Right>", self.go_right)
	
	def go_left(self, evt):
		self.x = -2.5
	
	def go_right(self, evt):
		self.x = 2.5

	def  draw(self):
		self.canvas.move(self.id, self.x, 0)
		pos = self.canvas.coords(self.id)
		if pos[0] <= 0:
			self.x = 0
		if pos[2] >= self.canvas_width:
			self.x = 0

# Make life easier
root = tk.Tk()

# Ready the playing field
root.title("Pong")
root.resizable(0, 0)
root.wm_attributes("-topmost", 1)
canvas = tk.Canvas(root, width=600, height=600, bd=0, highlightthickness=0, bg="black")
canvas.pack()
root.update()

# Spawn paddle and ball
paddle = Paddle(canvas, "white")
ball = Ball(canvas, "white", paddle)

# Constant updates
while 1:
	if ball.hit_bottom == False:
		ball.draw()
		paddle.draw()
	else:
		break
	root.update_idletasks()
	root.update()
	time.sleep(0.01)

# Game over text
gameOverText = "Game over! Your score was %s." % score
gameOverWidget = tk.Label(root, justify=tk.LEFT, padx = 10, text=gameOverText).pack()

# Quit game button
gameOverButton = tk.Button(root, text="Quit", command=quitGame).pack()

# Show game over screen
root.mainloop()