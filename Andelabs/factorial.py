def factorial(number):
	if number <= 1:
		return 1
	else:
		number = number * factorial(number - 1)
	return number

print factorial(2)
print factorial(5)
print factorial(10)