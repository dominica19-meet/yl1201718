from turtle import *
import turtle 

class Ball(object):
	"""docstring for Ball"""
	def __init__(self, x ,y,dx,dy,r,color,shape):
		turtle.__init__(self)
		self.goto(x,y)
		self.dx = dx
		self.dy = dy
		self.r = r
		self.color(color)
		self.shape("circle")
		self.shapesize(r/10)
		turtle.penup()

def move(self,screen_width,screen_height):
	current_x = self.xcor()
	new_x = current_x + self.dx
	current_y = self.ycor()
	new_y = current_y + self.dy
	right_side_ball = new_x + self.r
	left_side_ball = new_x - self.r
	up_side_ball = new_y + self.r
	down_side_ball = new_y - self.r
	self.goto(new_x,new_y)
