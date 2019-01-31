# Write a function that takes in two arrays of integers.
# The function should return two integers, one from each array,
# with the smallest difference between them

def smallest_difference(lst1, lst2):
	lst1.sort()
	lst2.sort()

	pointer1 = 0
	pointer2 = 0
	min_diff = float('inf')

	while pointer1 < len(lst1) and pointer2 < len(lst2):
		diff = abs(lst1[pointer1] - lst2[pointer2])
		if diff < min_diff:
			min_diff = diff
			res = [lst1[pointer1], lst2[pointer2]]
		if lst1[pointer1] < lst2[pointer2]:
			pointer1 += 1
		elif lst1[pointer1] > lst2[pointer2]:
			pointer2 += 1
		else:
			return [lst1[pointer1], lst2[pointer2]]

	return res

print(smallest_difference([-1,5,10,20,28,3], [26,134,135,15,17])) # => [28,26]