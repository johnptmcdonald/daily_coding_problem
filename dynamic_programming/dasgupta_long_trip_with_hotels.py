

# [0, 150, 180, 190, 380, 400, 550, 600]


# dp = [0, 0, 0, 0, 0, 0, 0, 0]

# def long_trip(arr):
# 	dp = [0] + [float('inf')] * (len(arr) + 1)
# 	path = []
# 	hotels = [0] + arr + [max(arr) + 201]

# 	for i in range(len(hotels)-1):
# 		j = i + 1
		
# 		while hotels[j] - hotels[i] <= 200:
# 			diff = hotels[j] - hotels[i]
# 			dp[j] = min(dp[j], dp[i] + (200 - diff)**2)

# 			j += 1

# 		print("\n")
		
		
# 	for j in range(len(dp)):
# 		index = len(dp)-2-j
# 		if dp[index] <= dp[index+1] and index is not 0:
# 			path.append(index-1)



# 	print(dp)
# 	print(list(reversed(path)))
# 	return list(reversed(path))


def long_trip(arr):
	dp = [0] * len(arr)
	
	for j in range(1, len(arr)):
		print("\n")
		dp[j] = (200 - arr[j])**2
		print(j)
		for i in range(1, j-1):
			print(i)
			dp[j] = min(dp[j], dp[i] + (200 -(arr[j]-arr[i]))**2 )

	# dp.reverse()
	print(dp)
	
	path = []
	for i in range(len(dp)-1, 0, -1):
		if i == len(dp)-1:
			path.append(i)
			mini = dp[i]
			flag = False
		elif dp[i] > mini:
			flag = True
		elif dp[i] <= mini and flag:
			path.append(i)

	path.reverse()

	print(path)
	return path
		

long_trip([150, 180, 380, 400, 550, 600, 700, 790, 800, 850])


