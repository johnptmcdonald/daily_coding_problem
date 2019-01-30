# given an array of positive integers representing coin denominations
# and a single target, find the minimum number of coins to make that target

# bleughs 
def min_number_of_coins_for_change(n, denoms):
	denoms = sorted(denoms)
	dp = [0] * (n+1)

	for denom in denoms:
		for amount in range(denom, n+1):
			
			temp2 = dp[amount]

			num_current_denom = amount//denom
			remainder = amount%denom

			temp = dp[amount]
			dp[amount] = num_current_denom

			if dp[remainder] == 0:
				if remainder != 0:
					dp[amount] = 0

			dp[amount] += dp[remainder]

			if dp[amount] == 0:
				dp[amount] = temp

			if dp[amount] > temp2 and temp2 is not 0:
				dp[amount] = temp2

	return dp[n]

min_number_of_coins_for_change(3, [2,1])




