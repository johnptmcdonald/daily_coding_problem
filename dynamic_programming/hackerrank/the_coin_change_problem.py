
# https://www.hackerrank.com/challenges/coin-change/problem


# n is the target = 8
# c is the denom array = [1, 2, 3, 8]

# let N(j, c) be the number of ways to get j (1 -> n) using only a subset of c
 
def get_ways(n, c):
	N = [1] + [0] * (n)

	for denom in c:
		for j in range(0, n + 1):
			if j >= denom:
				N[j] += N[j - denom]

	print(N)


get_ways(9, [1, 2, 3, 8])
	


