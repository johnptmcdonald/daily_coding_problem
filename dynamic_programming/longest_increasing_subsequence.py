

# find the longest strictly increasing subsequence given an array of integers

# e.g. [3, 1, 2, 5, 7, 12, 4] => 5 (due to 1, 2, 5, 7, 12)

def longest_increasing_subsequence(arr):
	dp = [1] * len(arr)

	for i in range(len(arr)):
		num = arr[i]
		for j in range(i):
			secondNum = arr[j]
			
			if secondNum < num:
				dp[i] = max(dp[i], dp[j] + 1)

	print(dp)


# dp = [1, 1, 2, 3, 4, 5, 3]














longest_increasing_subsequence([3, 1, 2, 5, 7, 12, 4])

