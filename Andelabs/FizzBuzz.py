def fizz_buzz(x):
	
	if x%3 == 0 and x%5 == 0:
		return "FizzBuzz"
	elif x%3 == 0:
		return "Fizz"
	elif x%5 == 0:
		return "Buzz"
	else:
		return x
	


print fizz_buzz(3)
print fizz_buzz(33)
print fizz_buzz(5)
print fizz_buzz(25)
print fizz_buzz(15)
print fizz_buzz(105)
print fizz_buzz(101)
print fizz_buzz(8) 
