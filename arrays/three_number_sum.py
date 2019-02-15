# Write a function that take in an array of integers, and an integer representing a target sum.
# The function should return all the triplets that sum up to the target sum

def three_number_sum(array, targetSum):
	array.sort()
	triplets = []

	for i in range(len(array) - 2):
		left = i + 1
		right = len(array) - 1

		while left < right:
			currentSum = array[i] + array[left] + array[right]
			if currentSum == targetSum:
				triplets.append([array[i], array[left], array[right]])
				left += 1
				right -= 1
			elif currentSum < targetSum:
				left += 1
			elif currentSum > targetSum:
				right -= 1

	return triplets

print(three_number_sum([12,3,1,2,-6,5,-8,6],0))


# The key here is to sort the array and traverse it once. At each number, place a left pointer immediately to the right of the current number, and a right point on the final number in the array. 
