class Person:
	# people_count is a class variable  
	people_count = 0 # counts the number of people objects being made 

	# __init__ always called the moment class is formed, when you want to do something the moment class is created  
	def __init__ (self, name, age): # works the same way as a constructor
		# these are instance variables 
		self.name = name
		self.age = age # to access instance variable use self 
		Person.people_count += 1 # assigning class variable 
		# to access class variable use class_name.instance_name 

	def say_hello (self):
		return "Hello, I am {} and I'm {} y/o".format(self.name, self.age)

	def __repr__(self): # internal function meaning represent 
		return "<object: {}, {}>".format(self.name, self.age)

# end of class		  
 
p = Person ('Joe', 23) # instance of class Person
p2 = Person ('George', 14)
p3 = Person ("Honey", 67)
print p.say_hello() # here you're calling the function say_hello so it works with person p 

a = [('Jane', 23), ('Bopchy', 22), ('Joe', 56), ('Jacob', 58), ('Ruth', 45), ('Yui', 14)]
b = [] # empty list for storage 

for name, age in a:
	person = Person(name, age) # person is just a place holder variable changing everytime, 
	# ie: once Jane is created, Jane is stored in b (leaving b empty), then Bopchy is made then pushed and so on  
	b.append(person) # appends / pushes / stores the person made into empty list b


print p.name 
print p.age
print p2.people_count
print b

# for loop calling function say_hello for all the people in b 
for person in b:
	print person.say_hello()


