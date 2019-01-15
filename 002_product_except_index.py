#Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
#For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

#Follow-up: what if you can't use division?

import unittest

def product_except_index(lst):
	product = 1
	for l in lst:
		product *= l

	return [product/l for l in lst]

def product_except_index_no_division(lst):
	leftways = []
	rightways = []
	
	l_product = 1
	r_product = 1
	
	for i in range(len(lst)):

		r_product *= lst[i]
		l_product *= lst[len(lst)-1-i]
		
		rightways.append(l_product)
		leftways.append(r_product)

	rightways.reverse()
	res = [0]*len(lst)
	
	rightways = rightways[1:]
	leftways = leftways[:-1]
	
	res[0] = rightways[0]
	res[len(lst)-1] = leftways[-1]

	for i in range(1, len(rightways)):
		res[i] = rightways[i]*leftways[i-1]

	return res


class Test(unittest.TestCase):

	def test_product_except_index_case_one(self):
		self.assertEqual(product_except_index([1, 2, 3, 4, 5]), [120, 60, 40, 30, 24])

	def test_product_except_index_case_two(self):
		self.assertEqual(product_except_index([3, 2, 1]), [2, 3, 6])

	def test_product_except_index_no_division_case_one(self):
		self.assertEqual(product_except_index_no_division([1, 2, 3, 4, 5]), [120, 60, 40, 30, 24])

	def test_product_except_index_no_division_case_two(self):
		self.assertEqual(product_except_index_no_division([3, 2, 1]), [2, 3, 6])


unittest.main()


