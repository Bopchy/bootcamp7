# this is a super class 


class Person(object): # these brackets mean every object must inherit from an in built superclass called object 
	# people_count is a class variable  
	people_count = 0 # counts the number of people objects being made 

	
	# __init__ always called the moment class is formed, when you want to do something the moment class is created  
	def __init__ (self, name, age): # works the same way as a constructor
		# these are instance variables 
		self.name = name
		#if age == 0: ###### makes inputting age optional 
		self.age = age # to access instance variable use self 
		Person.people_count += 1 # assigning class variable 
		# to access class variable use class_name.instance_name 

	
	def __repr__(self): # internal function meaning represent 
		return "<object: {}, {}>".format(self.name, self.age) 


	def say_hello (self):
		return "Hello, I am {} and I'm {} y/o".format(self.name, self.age)


	
