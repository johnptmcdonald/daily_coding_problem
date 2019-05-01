
# Find out if any (non-negative) numbers in an array can add up to a target

def subset_sum(target, arr):
	dp = [0]

	for num in arr:
		for i, d in enumerate(dp[:]):
			new_num = dp[i] + num
			
			if new_num == target:
				print('True')
				return True
			else:
				dp.append(dp[i] + num)


	# print(dp)
	print('False')
	return False




subset_sum(2, [1, 10, 5, 3]) # false
subset_sum(10, [1, 10, 5, 3]) # true
subset_sum(9, [1, 10, 5, 3]) # true
subset_sum(19, [1, 10, 5, 3]) # true
subset_sum(17, [1, 10, 5, 3]) # false