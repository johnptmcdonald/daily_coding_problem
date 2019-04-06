# Given an array of integers that are out of order, determine the bounds of the smallest window that must be sorted in order for the entire array to be sorted

in_data = [3,7,5,6,9]

out_data = (1,3) #the indices of the window which must be sorted for the whole array to become sorted

# APPROACH:
# traverse the array completely from L -> R, note if each element is less than the maximum up to that point. We can take the last element that is less than the running maximum and use it as our right bound.

# Then travese the array completely from R -> L, and do the same but note when an element is greater than the running minimum and use that as our left bound.  

def locate_smallest_window(arr):
	running_max = -float('inf')
	running_min = float('inf')
	
	right_bound = None
	left_bound = None

	for i in range(len(arr)):
		running_max = max(running_max, arr[i])
		if(arr[i] < running_max):
			right_bound = i

		running_min = min(running_min, arr[len(arr)-1-i])
		if(arr[len(arr)-1-i] > running_min):
			left_bound = len(arr)-1-i

	print(left_bound, right_bound)
	return (left_bound, right_bound)


locate_smallest_window(in_data)






