
def three_number_sum(arr, targetSum):
		res = []

		# [12,3,1,2,-6,5,-8,6]
		arr.sort()

		# [-8,-6,1,2,3,5,6,12]

		# iterate through, place left pointer on num to immediate right,
		# and right pointer at the end.

		for i, num in enumerate(arr):
			if i == len(arr)-2:
				break
			
			target = targetSum - num
			lp = i+1
			rp = len(arr)-1

			while lp != rp:
				if arr[lp] + arr[rp] == target:
					res.append(sorted([num, arr[lp], arr[rp]]))
					lp += 1
					rp += 1
				elif arr[lp] + arr[rp] > target:
					rp -= 1
				elif arr[lp] + arr[rp] < target:
					lp += 1

		return res

x = three_number_sum([12,3,1,2,-6,5,-8,6], 0)
print(x)