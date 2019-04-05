

# Given an array of numbers, find the maximum sum of any contiguous subarray of the array.

input_data = [34, -50, 42, 14, -5, 86] 
# output = 137 (by summing the subarray 42,14,-5,86)

def max_subarray_sum(arr):
	max_ending_here = 0
	max_so_far = 0

	for x in arr:
		max_ending_here = max(x, max_ending_here+x)
		max_so_far = max(max_so_far, max_ending_here)

	return max_so_far


print(max_subarray_sum(input_data))
