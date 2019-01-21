# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

# Follow-up: Can you do this in O(N) time and constant space?

# A pretty bad (O(2^n)) solution as it is simple recursion
# we can either skip the first number, or not.
def largest_non_adjacent(arr):
	if not arr:
		return 0

	return max(
			largest_non_adjacent(arr[1:]),
			arr[0] + largest_non_adjacent(arr[2:]))


#i.e. largest_non_adjacent([2, 4, 6, 2, 5]) =
#		 max(largest_non_adjacent([4, 6, 2, 5]), 2 + largest_non_adjacent([6, 2, 5]))


# Sooo... we can memoize/cache it. We keep track of the largest_non_adjacent sum up to that point
# in the cache array. The when we encounter the next num, if we use it then we can't use the one before it.
def largest_non_adjacent(arr):
	if len(arr) <= 2:
		return max(0, max(arr))

	# initialize cache
	cache = [0 for i in arr]
	cache[0] = max(0, arr[0])
	cache[1] = max(cache[0], arr[1])
	print(cache)
	
	# go through the input array, at each point
	# we have already calculated the largest non adjacent sum UP to that point
	# so given the new num, we can add it (num + cache[i - 2]), or ignore it (cache[i - 1]).
	# so the largest non_adjacent_sum including that point is whichever is larger - including it, or ignoring it 
	for i in range(2, len(arr)):
		num = arr[i]
		cache[i] = max(num + cache[i - 2], cache[i - 1])
		print(cache)
	return cache[-1]


# we can improve it even further - we only need the most recent
# 2 items in the cache:
# def largest_non_adjacent(arr):
# 	if len(arr) <= 2:
# 		return max(0, max(arr))

# 	max_excluding_last= max(0, arr[0])
# 	max_including_last = max(max_excluding_last, arr[1])

# 	for num in arr[2:]:
# 		prev_max_including_last = max_including_last

# 		max_including_last = max(max_including_last, max_excluding_last + num)
# 		max_excluding_last = prev_max_including_last

# 	return max(max_including_last, max_excluding_last)

import unittest

class Test_largest_sum(unittest.TestCase):

	def test_case_one(self):
		self.assertEqual(largest_non_adjacent([2, 4, 6, 2, 5]), 13)

unittest.main()
