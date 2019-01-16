# Given an array of integers, 
# find the first missing positive integer in linear time and constant space. 
# In other words, find the lowest positive integer that does not exist in the array. 
# The array can contain duplicates and negative numbers as well.

# For example, the input [3, 4, -1, 1] should give 2. 
# The input [1, 2, 0] should give 3.

# You can modify the input array in-place.


def first_missing_positive_int_linear(nums):
	"""Linear time and space, but we need constant space"""
	
	# Here's the trick: the first missing positive number must be 
	# between 1 and len(array) + 1 	
	s = set(nums)
	
	for i in range(1, len(nums) + 1):
		if i not in s:
			return i




def first_missing_positive_int(nums):
	"""Linear time, CONSTANT space"""

	# Here's the trick again: the first missing positive number must be 
	# between 1 and len(array) + 1 

	# use the array to keep track of what numbers exist in the list
	# we can ignore any negative numbers and numbers bigger 
	# than len(array). 
	# The basic idea is to use the indices of the array itself to 
	# reorder the elements to where they should be
	
	for i, num in enumerate(nums):
		# keep swapping until we get a negative or too large number 
		while i+1 != nums[i] and 0 < nums[i] <= len(nums)+1:
			# perform swap
			x = nums[i]
			nums[i], nums[x-1] = nums[x-1], nums[i]

			# if there are dupes we need to break or else we swap forever, so as long as we have ONE record of there being this number, it doesn't matter about the rest:
			if nums[i] == nums[x-1]:
				break


	# now just iterate through our 'effectively' sorted array (not really sorted, just the portion that matters)
	for i, num in enumerate(nums):
		if num != i+1:
			return i+1



import unittest

class Test_first_missing_positive_int(unittest.TestCase):

	def test_case_one(self):
		self.assertEqual(first_missing_positive_int([3, 4, -1, 1]), 2)


	def test_case_two(self):
		self.assertEqual(first_missing_positive_int([1, 2, 0]), 3)


unittest.main()




