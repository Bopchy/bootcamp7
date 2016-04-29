def find_max_min(A):
	minimum = min(A) 
	maximum = max(A)

	if minimum == maximum:
		return [len(A)] # if min no. equals max no., length of string is returned 
	return [minimum, maximum]

print max_min([1, 2, 3, 4])
print max_min([23, 0, 7, 78])
print max_min([4, 66, 6, 44, 7, 78, 8, 68, 2])
