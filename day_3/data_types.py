def data_type (X):
	'''
		Takes in an argument, X:
			- For an integer, return X ** 2
			- For a float, return X / 2
			- For a string, returns "Hello" + X ~ see better way of doing this below 
			- For a Boolean, return "Boolean"
			- For a long, return square root (X)
	'''
		
	
	if type (X) == int: 
		return X ** 2
	elif type (X) == float:
		return X / 2
	elif type (X) == str:
		return "Hello {}".format(X) # curly brackets are like a place holder for X
	elif type (X) == bool: 
		return "Boolean"
	elif type (X) == long:
		return "Long"
	else:
		return "Invalid input"

print data_type (50)
print data_type (50**50)
print data_type ("I got this!!")
print data_type (False)
print data_type (.99676)













