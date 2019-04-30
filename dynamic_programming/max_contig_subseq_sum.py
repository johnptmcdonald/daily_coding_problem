# question 6.1 from Dasputa

def max_contig_subset_sum(arr):
	dp = [0] * len(arr)
	
	for i, num in enumerate(arr):
		dp[i] = max(num, num + dp[i-1])

	print(dp)
	return max(dp)


max_contig_subset_sum([5,15,-30,10,-5,40,10])