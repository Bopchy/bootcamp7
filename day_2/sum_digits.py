def sum_digits (A):
	'''
	Takes in a list A and 
		returns sum of all the digits in the 
		list e.g. [10,30,45] should return 
		1 + 0 + 3 + 0+ 4 + 5 = 13

	'''
	total = 0
	
	for num in A:
		b = str(num)
		for a in b:

			total += int(a)
	return total

print sum_digits ([10, 30, 45])
print sum_digits ([15, 15, 14, 20])






	 
