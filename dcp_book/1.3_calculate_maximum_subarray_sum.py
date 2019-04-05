

# Given an array of numbers, find the maximum sum of any contiguous subarray of the array.

# Use Kadane's algorithm

input_data = [34, -50, 42, 14, -5, 86] 
# output = 137 (by summing the subarray 42,14,-5,86)

def max_subarray_sum(arr):
	max_ending_here = 0
	max_so_far = 0

	for x in arr:
		# find the largest subarray that ends at each index
		# we could put this in its own array. 
		max_ending_here = max(x, max_ending_here+x)
		
		# find the max of largest subarray that ends at each index
		max_so_far = max(max_so_far, max_ending_here)
		print('max_ending_here', max_ending_here)
		print('max_so_far', max_so_far)

	return max_so_far


print(max_subarray_sum(input_data))
