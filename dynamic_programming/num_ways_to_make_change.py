# given an array of positive integers representing coin denominations
# and a single integer representing a target value
# implement a function that returns the number of ways to make change for that target value.
# You have an unlimited number of coins at your disposal

def number_of_ways_to_make_change(n, denominations):
	# Use dynamic programming to build up the answer starting at target 0 up to target 6
	# each col represents a target
	dp = [0]*(n+1)
	dp[0] = 1

	for denom in denominations:
		for amount in range(1, n+1):
			if denom <= amount:
				dp[amount] += dp[amount-denom]

	return dp[n]


number_of_ways_to_make_change(6, [1,5]) # => 2