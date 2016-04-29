def reverse_string (string):
	if string == (""):
	  return None 

	A = list(string) # making A a list 
	A.reverse() # reverses list A
	r = "".join(A) # returns the reversed list to the data type that string was in to begin with
	# we use empty string ("") to show the data type we want 
	return r

	if r == string:
		True 
	
print reverse_string("")
print reverse_string("Hannah")
print reverse_string("anna")
print reverse_string("NaN")
print reverse_string("civic")
print reverse_string("books")
print reverse_string("solomon")
print reverse_string("misc")
