def super_sum(A): 
	
	'''
	Takes a list A
	Halves every even number and 
	doubles every odd numbers, 
	and returns sum of all

	'''
	numbers = 0
	for num in A:
		if num % 2 == 0:
			numbers += num / 2 
			
		else:
			numbers += num * 2 
			
	return numbers
	
print super_sum ([1,2,3,4,5])

