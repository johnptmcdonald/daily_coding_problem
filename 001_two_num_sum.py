#1 - Do two numbers in a list add up to a target number?
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

import unittest

def two_num_sum(lst, k):
	hash = {}

	for num in lst:
		if num in hash:
			return True
		else:
			hash[k-num] = True

	return False

class Test_two_num_sum(unittest.TestCase):
	""" tests for two num sum """
	def test_case_one(self):
		self.assertEqual(two_num_sum([1,2,3,4], 5), True)

	def test_case_two(self):
		self.assertEqual(two_num_sum([1,2,3,4], 10), False)

	def test_case_three(self):
		self.assertEqual(two_num_sum([1,2,3,4], 3), True)				

	def test_case_four(self):
		self.assertEqual(two_num_sum([1,-2], -1), True)

	def test_case_five(self):
		self.assertEqual(two_num_sum([10, 15, 3, 7], 17), True)


unittest.main()
