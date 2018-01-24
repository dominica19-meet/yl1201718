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





hideturtle()
turtle.getscreen().update()

mainloop()