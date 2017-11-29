from turtle import*
import random
import turtle
colormode(255)

class rectangle(Turtle):
	def __init__(self,shape,width,height):

		Turtle.__init__(self)
		register_shape("rect", ((0,0) , (width,0) , (width,height) , (0,height)))
		self.shape("rect")
	def random_color(self):
		r = random.randint(0,256)
		g = random.randint(0,256)
		b = random.randint(0,256)
		self.color((r,g,b))
		

RECT = rectangle(70,800,90)
RECT.random_color()

mainloop()