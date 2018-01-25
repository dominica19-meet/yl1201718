from turtle import *
import turtle 
import random 
import time
from ball import *

tracer(0)
hideturtle()
RUNNING=True
SLEEP=0.0077
SCREEN_WIDTH=turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT=turtle.getcanvas().winfo_height()/2


my_ball=Ball(100,0,5,10,100,"light blue")
my_ball.goto(10,10)
NUMBER_OF_BALLS=5
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 100
MINIMUM_BALL_DX = 5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5 
BALLS=[]
for i in range(NUMBER_OF_BALLS):
	x=random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS,SCREEN_WIDTH-MAXIMUM_BALL_RADIUS)
	y=random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT-MAXIMUM_BALL_RADIUS)
	dx = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS,SCREEN_WIDTH-MAXIMUM_BALL_RADIUS)
	dy = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT-MAXIMUM_BALL_RADIUS)
	r = random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
	shape = circle
	color =(random.random(),random.random(),random.random()) 
	ball2= Ball(x,y,dx,dy,r,color)
	BALLS.append(ball2)

def move_all_balls():
	for ball in BALLS:
		ball.move(SCREEN_WIDTH,SCREEN_HEIGHT)

def check_all_balls_collision(self):
	for ball_a in (BALLS):
		if collide (ball_a,ball_b)==True:
			ball_a_radious = ball_a.r()
			ball_b_radious = ball_b.r()
			if ball_a.ball_a_radious>ball_b_radious:
				ball_a_radious=+1
			else:
				ball_b_radious=+1
	X_COORDINATE=random.randint(round(-SCREEN_WIDTH),round(screen_width))
	y_COORDINATE= random.randint(round(-SCREEN_HEIGHT),round(screen-hieght))
	X_AXISPEED = random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
	Y_AXISPEED = random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
	while X_AXISPEED and Y_AXISPEED == 0:
		X_AXISPEED = random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
		Y_AXISPEED = random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
	radius = random.randint(MINIMUM_BALL_RADIUS , MAXIMUM_BALL_RADIUS)
	print(radius)
	color = (random.random(),random.random(),random.random())
	print(color)
		if ball_a.r >ball_b.r:
			ball_b.r = radius
			ball_b.x = X_COORDINATE
			ball_b.y = Y_COORDINATE
			ball_b.dx = X_AXISPEED
			ball_b.dy = Y_AXISPEED
			ball_b.color(color)
			ball_b.shapesize(ball_b.r/10)
			ball_a.r = ball_a.r+1
			ball_a.shapesize(ball_a.r/10)
		else:
			ball_a.r = radius
			ball_a.x = X_COORDINATE
			ball_a.y = Y_COORDINATE
			ball_a.dx = X_AXISPEED
			ball_a.dy = Y_AXISPEED
			ball_a.color(color)
			ball_a.shapesize(ball_a.r/10)
			ball_b.r = ball_a.r+1
			ball_b.shapesize(ball_b.r/10)	
def check_myball_collision():
	for ball in BALLS:
		if collide(MY_BALL,ball) == True:
			ball_r4 = ball.random
			my_ball_r4 = MY_BALL.r
			if my_ball_r4 and MY_BALL.shapesize() < BALL.shapesize():

				return False
			X_COORDINATE=random.randint(round(-SCREEN_WIDTH),round(SCREEN_WIDTH))
			y_COORDINATE= random.randint(round(-SCREEN_HEIGHT),round(SCREEN_HEIGHT))
			X_AXISPEED = random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
			Y_AXISPEED = random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
			while X_AXISPEED and Y_AXISPEED == 0
			X_AXISPEED = random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
			Y_AXISPEED = random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)

			radius = random.randint(MINIMUM_BALL_RADIUS , MAXIMUM_BALL_RADIUS)
			print(radius)
			color = (random.random(),random.random(),random.random())
			print(color)
	while True:
		for ball in BALLS:
			ball.move(SCREEN_WIDTH , SCREEN_HEIGHT)
	def collide (ball_a,ball_b):
		if ball_a == ball_b:
			return False
		if (math.pow(ball_a.x_ball_b.x))+(math.pow(ball_a.y-ball_b.py)):
		else:
			return False









hideturtle()
turtle.getscreen().update()

mainloop()