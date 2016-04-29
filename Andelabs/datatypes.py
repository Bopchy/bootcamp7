def data_type(A=None):
	if type(A) == str:
		return len(A)
	if A == None:
		return "no value"  
	if type(A) == bool:
		return A
	if type(A) == int: 
		if A == 100:
			return "equal to 100"
		elif A < 100:
			return "less than 100"
		return "more than 100"
	if type(A) == list:
		if len(A) <= 2:
			return None
		return A[2]

print data_type()
print data_type([1, 2, 3])
print data_type([1, 2])
print data_type(True)
print data_type(3)
print data_type(100)
print data_type(200)
print data_type("andela")








