import turtle
turtle.speed(100)
def drawline():
	turtle.forward(200.200)
	turtle.right(50)
	turtle.forward(100.100)
	turtle.right(90)
	turtle.forward(60.60)
	turtle.home()

for x in range(360):
	turtle.right(x)
	drawline()



turtle.mainloop()