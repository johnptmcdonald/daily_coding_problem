# Given an array of integers, return an array of two items
# the first item is the greatest sum that can be generated 
# from a strictly increasing subsequence of the array. 
# The second item should be an array of the numbers in that 
# subsequence. 


def max_sum_increasing_sebsequence(lst):
	res = []

	# use DP
	dp = [0]*len(lst)
	dp[0] = lst[0]

	best_sum = lst[0]
	best_i = 0

	# initialize array of indices of where to go for 
	dp2 = [0]*len(lst)

	# keep track of max sequence up to that point
	for i, i_num in enumerate(lst):
		sum = i_num
		chosen_j = None
		for j, j_num in enumerate(lst):
			if j_num < i_num:
				old_sum = sum
				sum = max(sum, dp[j] + i_num)
				if max(sum, dp[j] + i_num) > old_sum:
					chosen_j = j
		dp[i] = sum

		if sum > best_sum:
			best_sum = sum
			best_i = i

		dp2[i] = chosen_j


	while best_i is not None:
		res.append(lst[best_i])
		best_i = dp2[best_i]

	res.reverse()

	return [best_sum, res]

max_sum_increasing_sebsequence([10,70,20,30,50,11,30]) # => [110, [10,20,30,50]]
