
# m is a list of possible locations, each value represents the number of miles from the start. Any two restaurants must be at least k miles apart.

# m = [10, 30, 40, 80, 200]
# k = 30

# 1 - subproblem:
# let P(j) be the maximum profit achievable using only the first j locations. Each restaurant has it's own profitability of p_j.

# 2 - recursive formulation:
# in figuring out P(j) we have two choices: place a restaurant at location j, or do NOT place a restaurant there
	# if we place a restaurant at j, we must skip all the locations fewer then k miles to the left of location j. We can define prev_j as the largest index to the left of location j that is far enough away. Thus P(j) is equal to p_j + P(prev_j)
	# If we do NOT place a restaurant at location j, then the P(j) at j is simply equal to the largest profit up to that point, which is P(j-1)


	

