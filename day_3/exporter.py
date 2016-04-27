# global variables ~~~ NOT good practise though 

people = [
			('Joe', 78), 	
			('Janet', 90), 
			('Brian', 67)
		]

def super_sum (*args):
	return sum(args)


def hello_again (name, age):
	return "I am {} and {} years old".format(name, age)

def max_min(A):
	'''
	returns max value - min value 
	e.g. [10, 20, -5, 6, 50, 8]
	'''
	#return max (A) - min (A) ~~~ is the shorter version of the for loop 
	max_, min_ = A[0], A [0] # pythonic mass assigning 

	for i in A:
		if i > max_:
			max_ = i
		if i < min_:  # use elif in situation where this second condition doesn't really need to be tested and can be skipped 
			min_ = i
	return max_ - min_



