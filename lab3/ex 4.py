'''
class Animal(object):
	def __init__(self,sound,name,age,favorite_color):
		self.sound = sound
		self.name = name
		self.age = age
		self.favorite_color = favorite_color
	def eat(self,food):
		print("yummy!!"+self.name+"is eating"+food)
	def description(self):
		print(self.name+"is"+self.age+"yers old and loves the color"+self.favorite_color)
	def make_sound(self):
		print("rawands signature is"+ self.sound)

Animal1 = Animal("barking","rawand","5","blue")
Animal1.name
Animal1.eat("shawerma")
Animal1.description()
Animal1.make_sound()

'''
class person(object):
	"""docstring for person"""
	def __init__(self,name,age,city,gender):
		self.name = name
		self.age = age
		self.city = city
		self.gender = gender
	def eat(self,food):
		print(self.name+" is eating "+food)
	def play(self,sport):
		print(self.name+" is playing her favourite sport wich is "+ sport)


iam=person("dominica","15","bethlehem","female")
iam.eat("shawerma")
iam.play("fitness")

##
class Song(object):
	def __init__(self,lyrics):
		self.lyrics= lyrics
	def sing_me_a_song(self):
		for i in self.lyrics:
			print(i)
flower_song = Song(["roses are red,",
	           "violets are blue,","i wrote this poem for you."])
flower_song.sing_me_a_song()

		
		