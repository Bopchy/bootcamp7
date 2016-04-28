def super_sum(*args):
	'''
		Returns a sum of numbers
		e.g.
			super_sum() ==> "Please enter input" 
			super_sum(1,2,3) ==> 6
			super_sum("string", 2, 5) ==> 0
			super_sum([1,2,3]) ==> 6
			super_sum([10],[20,30]) ==> 60
	'''
	
	total = 0
	if not args: # means if there are no arguments at all
		return 0
		
	else:
		for x in args:
			if type(x) == list:
			# here x is now ([1, 2, 3]) ~ from test
				for i in x: # iterates through members of x 
					total += i # can also be sum(x) ~ calls sum fuction 
			elif type(x) == str:
				return 0
			else:
				total += x
		return total # returns total of list items 
			


print super_sum(2, 5, 7)
print super_sum([4, 1, 2])
print super_sum("Bopchy", 2, 4)


