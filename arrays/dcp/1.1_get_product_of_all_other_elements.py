# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i. Don't use division.

in_data = [1,2,3,4,5]
out_data = [120,60,40,30,24]


def product_except_index(nums):
	# generate prefix and suffix sums
	prefix_products = []
	suffix_products = []

	for num in nums:
		if prefix_products:
			prefix_products.append(prefix_products[-1] * num)
		else:
			prefix_products.append(num)

	for num in reversed(nums):
		if suffix_products:
			suffix_products.append(suffix_products[-1] * num)
		else:
			suffix_products.append(num)

	suffix_products = list(reversed(suffix_products))

	res = []

	# generate res from prefix and suffix sums (with special case at first num and last num)
	for i in range(len(nums)):
		if i == 0:
			res.append(suffix_products[i+1])
		elif i == len(nums)-1:
			res.append(prefix_products[i-1])
		else:
			res.append(prefix_products[i-1] * suffix_products[i+1])

	print(res)
	return res


product_except_index(in_data)