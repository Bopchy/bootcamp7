#  person = module_name, Person = class_name
from person import Person 
from kenyan import Kenyan



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




k = Kenyan('Jane', 34)
k.probe (True)

print "Is {} corrupt? {}".format(k.name, k.is_corrupt())
print k.say_hello ()
print k.corrupt ###################?????????

 
