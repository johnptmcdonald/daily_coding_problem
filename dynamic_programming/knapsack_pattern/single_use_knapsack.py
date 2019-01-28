# given a knapsack of weight capacity C
# fill it with the most value from a selection of items.

# e.g. [[1,2], [4,3], [5,6], [6,7]]
# e.g. first item has value 1, weight 2

# We will build a 2D array to hold the greatest values 
# under certain restrictions

# Columns are increasing capacity up to actual knapsack capacity

		# -> capacity ->
		# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
dp = [
		 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],		# no items available []
		 [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],		# 1st item available [[1,2]]
		 [0, 0, 1, 4, 4, 5, 5, 5, 5, 5, 5],		# 1st, 2nd items available [[1,2], [4,3]]
		 [0, 0, 1, 4, 4, 5, 5, 5, 6, 9, 9],		# 1st, 2nd, 3rd items available [[1,2], [4,3], [5,6]]
		 [0, 0, 1, 4, 4, 5, 5, 6, 6, 9, 10]		# 1st, 2nd, 3rd, 4th items available [[1,2], [4,3], [5,6], [6,7]]
	]

# The values represent the max value under those restrictions of available items and max capacity
# The top row is our base case - no items, so value is 0 for every possible capacity
# We gradually fill in the dp table from top left to bottom right

# for each position in the dp table
# compare the value of adding it, to not adding it
# If we don't add it, our value is just the position right above the current position
# If we DO add it, our value is the value of the item, plus the max value for the remaining capacity
# (the max value of the remaining capacity is the value in the row above for the remaining capacity)

