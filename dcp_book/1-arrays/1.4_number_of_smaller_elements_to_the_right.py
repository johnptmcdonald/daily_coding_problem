

# Given an array of integers, return a new array where each element in the new array is the number of smaller elements to the right of that element in the original input array

input_data = [3,4,9,6,1]

# output = [1,1,2,1,0]

def number_of_smaller_elements_to_right(arr):
	# iterate backwards and maintain a sorted list
	sorted_arr = []
	res = []
	for i, _ in enumerate(arr):
		num = arr[len(arr)-1-i]
		sorted_arr.append(num)
		sorted_arr.sort()
		print(sorted_arr)
		res.append(len(sorted_arr[:sorted_arr.index(num)]))

	res = list(reversed(res))
	
	print(res)
	return res


number_of_smaller_elements_to_right(input_data)

