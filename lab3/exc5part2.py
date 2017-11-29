from turtle import *
register_shape
class hexagon(Turtle):
	def __init__(self,size):
		Turtle.__init__(self)
		self.shapesize(size)
		self.begin_poly()
		self.penup()
		self.goto(0,0)
		self.forward(50)
		self.left(60)
		self.forward(50)
		self.left(60)
		self.forward(50)
		self.left(60)
		self.forward(50)
		self.left(60)
		self.forward(50)

		self.end_poly()
		p = self.get_poly()
		register_shape("myfav",p)
		self.shape("myfav")

myhexagon = hexagon(2)


mainloop() 