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
		# and the input itself e.g. from super_sum() we expect it to return 0,
		# which equals the expected output 0, so test passes 

	def test_sum_of_integers(self):
		'''
		Test sum of integers 
		'''
		self.assertEqual(super_sum(1, 2, 3), 6)
		self.assertEqual(super_sum(-1, 1), 0)
		self.assertNotEqual(super_sum(10, 10, 30), 100)
		# see what self.NotAssertEqual does

	def test_string_input_returns(self):
		'''
		Test for string input returns 0
		'''
		self.assertEqual(super_sum('string', 1, 4), 0)
	
	def test_sum_of_items_in_one_list(self):
		'''
		Test sum of items in a single list
		''' 
		self.assertEqual(super_sum([1, 2, 3]), 6)

######## The number of tests  done by nosetest, matches the number of tests
######## in test module (this case test_super_sum.py)

	
	
