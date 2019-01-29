
# 1 - inefficient recursive solution (maybe 2^n time)
def maxSubsetSumNoAdjacent(lst, idx=0):
	# for every number I can either take it, OR the next one. I want to use DP to find the max up to that point.
	
	if idx >= len(lst):
		return 0

	largest = max(lst[idx] + maxSubsetSumNoAdjacent(lst, idx+2), maxSubsetSumNoAdjacent(lst, idx+1))

	return largest

# 2 - Better solution (n time and space)
def maxSubsetSumNoAdjacent(lst):
	# for every number I can either take it, OR the next one. I want to use DP to find the max up to that point.
	if len(lst) == 0:
		return 0
	if len(lst) == 1:
		return lst[0]

	dp = [0]*(len(lst))

	dp[0] = lst[0]
	dp[1] = max(lst[0], lst[1])
	
	for i in range(2, len(lst)):
		# max is either...
		# the max up to the one before last plus current 
		# OR the max up to the last one
		dp[i] = max(dp[i-2]+lst[i], dp[i-1])

	return dp[-1]

# 3 - Even better - we don't need the whole dp array, just the previous two numbers
def maxSubsetSumNoAdjacent(lst):
	# for every number I can either take it, OR the next one. I want to use DP to find the max up to that point.
	if len(lst) == 0:
		return 0
	if len(lst) == 1:
		return lst[0]

	dp = [lst[0], max(lst[0], lst[1])]
	
	for i in range(2, len(lst)):
		# max is either...
		# the max up to the one before last plus current 
		# OR the max up to the last one
		curr_largest = max(dp[0]+lst[i], dp[1])
		dp[0] = dp[1]
		dp[1] = curr_largest

	return dp[-1]


maxSubsetSumNoAdjacent([75,105,120,75,90,135])


