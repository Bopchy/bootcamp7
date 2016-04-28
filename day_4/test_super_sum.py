'''
Test suite for super_sum
'''
from unittest import TestCase
from super_sum import super_sum




class SuperSumTestCase (TestCase):
# can also be done as: class SuperSumTestCase (unittest.TestCase)
# everything in this class is mostly from TestCase class ~ which has predefined how you run tests 
	'''
	Test case for super_sum
	'''

	def test_empty_input(self): 
	#remember classes ~ because its a method in a class it takes self as argument 
	#self refers to the class, as in the class' objects
		'''
		Test empty input 
		'''
		self.assertEqual(0, super_sum())
		# means, when you call super_sum without input, code 
		# should return "Pleas enter numbers"  
		# the statement you are checking for must be the same that 
		# you are testing for
		# arguments for self.assertEqual are what you expect from given input
		# and the input itself
	  

	def test_sum_of_integers(self):
		'''
		Test sum of integers 
		'''
		self.assertEqual(super_sum(1, 2, 3), 6)

