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
		print(dp)

	print(dp[n])
	return dp[n]


	




number_of_ways_to_make_change(6, [1,5]) # => 2




# Step 1: How to recognize a Dynamic Programming problem. ...
	# the problems has subproblems that can be used to solve the whole problem

# Step 2: Identify problem variables. ...
	# amount, denom

# Step 3: Clearly express the recurrence relation. ...
	# num_ways(amount, denom) = 1 + num_ways(amount - denom) IF denom < amount

# Step 4: Identify the base cases. ...
	# num_ways(0, any) === 0

# Step 5: Decide if you want to implement it iteratively or recursively. ...
	# iteratively
# Step 6: Add memoization. ...
	# dp is an array 

# Step 7: Determine Time complexity.


