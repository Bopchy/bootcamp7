def hello (name , age, class_=''):
	#demostrates list unpacking 
	'''
		Takes the name of the person as the first argument
		Takes their age as the second argument
	'''
	if class_ != '':
		return "I am {}, and I am {} years old, and i'm in {} class.".format (name, age, class_) 
	
	return "I am {}, and I am {} years old.".format (name, age)


people = [("Jane", 23, 'High'), ("Joe", 25, 'Low'), ("Brian", 60), ("Betty", 45)] #a list of tuples 

#for name, age in people:
	#print hello (name, age) 

for person in people:
	print hello(*person) # what happened here??

def super_sum (*args):

# *args is a conventional word (not reserved) which means that the 
# function can take in any number
# of arguments

	'''
		Takes in variable number of items,
		and returns the sum.
		e.g. super_sum (10, 20) = 30
		super_sum(10,20.40) = 70
		super_sum(1,4,5,6,7) = 23
	'''
	total = 0
	for i in args:
		total += i

	return total 

print super_sum (10, 20)
print super_sum (10, 20, 40)
print super_sum (1, 4, 5, 6, 7)

# unpacking from a
a = [10, 40, 60]
print super_sum (*a)


# kwargs is often used for unpacking dictionaries
def  hello_again (**kwargs):
	return "I am {}, and I am {} years old.".format (kwargs ['name'], kwargs ['age'])

print hello_again (name='Bopchy', age='22') # is providing arguments for above hello_again () 
print hello_again (name='Guy', age='13') # is providing arguments for above hello_again ()

# shows dictionary 
other_people = [

				{'name': 'Joe', 'age': 98},
				{'name': 'Jane', 'age': 60},
				{'name': 'Gyi', 'age': 89}

				]

# joe 
joe = {'name': 'Joe', 'age': 38}

print hello_again (**joe) # unpacking of joe
print hello_again (name='joe', age=98) # assigning arguments to hello_again

#u unpacking dictionary 
for person in other_people:
	hello_again (**person) # 

print hello_again ()