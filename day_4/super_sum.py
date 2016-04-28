def super_sum(*args):
	'''
		Returns a sum of numbers
		e.g.
			super_sum() ==> "Please enter input" 
			super_sum(1,2,3) ==> 6
			super_sum([1,2,3]) ==> 6
			super_sum([10],[20,30]) ==> 60
	'''
	if not args:
		return 0

	else:
		total = 0
		
		for x in args:
			total += x
		return total 



print super_sum(2, 5, 7)

