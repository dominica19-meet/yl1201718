from turtle import *
import random
import math
class Ball(Turtle):
	def __init__(self,radius,color,speed):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.color(color)
		self.speed(speed)
ball1 =Ball (30,"pink",1)
ball2 = Ball (40,"blue",1)

ball1.goto (100,100)
ball2.goto(-100,-100)

def check_collision(ball1, ball2):
	r1 = ball1.radius
	r2 = ball2.radius
	x1 = ball1.xcor()
	x2 = ball2.xcor()
	y1 = ball1.ycor()
	y2 = ball2.ycor()
	d = math.sqrt(math.pow(x2 - x1,2)+math.pow(y2 - y1,2))
	print (d)
	print (r1+r2)
	if(d < r1+r2):
		return True
	else:
		return False 

if (check_collision(ball1,ball2)) == True:
	print("Collide")
else:
	print("No Collide")
mainloop()