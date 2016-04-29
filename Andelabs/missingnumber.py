def find_missing (a, b):
	if a==[] and b==[]:
	 	return 0
	elif a == b:
		return 0
	for item in a:
		if item not in b:
			return item 
	for item in b:
		if item not in a:
			return item


print MissingNumberTest([1, 2], [1, 2, 5])
print MissingNumberTest([2], [2])
print MissingNumberTest([], [])
print MissingNumberTest([5, 4, 7, 6, 11, 66], [5, 4, 1, 7, 6, 11, 66])

