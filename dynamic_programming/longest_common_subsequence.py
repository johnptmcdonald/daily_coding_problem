
# find the length of the longest common subsequence given two strings

# e.g. 
# [ABCED] 
# [BEDCA] => 3 (BED)


# [FBCED] 
# [BEDCA] 


def longest_common_subsequence(arr1, arr2):

	longest = max(len(arr1), len(arr2))
	dp = [[0 for i in arr1] for j in arr2]
	
	for i in range(1, len(arr1)):
		for j in range(1, len(arr2)):
			if arr1[i] == arr2[j]:
				dp[i][j] = 1 + dp[i-1][j-1]
			else:
				dp[i][j] = max(dp[i-1][j], dp[i][j-1])

	print(dp)
	print(dp[len(arr1)-1][len(arr2)-1])
	return dp[len(arr1)-1][len(arr2)-1]


longest_common_subsequence(['A','B','C','E','D'], ['A','B','C','E','D'])




