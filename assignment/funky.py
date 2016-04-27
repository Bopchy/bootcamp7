def funky (a , b):
	if type (a) == str and type (b) == str:
		return a + b 
	elif type (a) == float and type (b) == float or type (a) == int and type (b) == int:
		return a + b
	elif type (a) == list and type (b) == list:
		return a + b
	elif type (a) == dict or type (b) == dict:
		c = dict (a.items() + b.items())
		return c
	else:
		return "Invalid input"
print funky ("Bopchy ", "Beau")
print funky (2 , 6)
print funky ([1, 2, 3, 4], [5, 6, 7])
print funky ({1: "banana", 2: "mango", 3: "pineapple"}, {"a": "one", "b": "two", "c": "three"})
