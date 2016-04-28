class Animal(object):
	pass

## OOP further explained 
class Person(object):
	def __init__(self, age, name):
		self.age
		self.name

class Poacher(Person):
	# using **kwargs  
	def __init__(self, name, age, **kwargs):
		Person.__init__(self, name, age)
		self.gun = kwargs.get('gun', 'AK-47')
		self.loc = kwargs.get('loc', 'Nairobi')
		self.gamepark = kwargs.get('gamepark', 'Tsavo')
		self.fav = kwargs.get('fav', 'Elephant')

	# using *args
	

class Tourist(object):
	pass
