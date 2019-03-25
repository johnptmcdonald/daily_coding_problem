# Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

# For example, given s = "bcba" and k = 2, the longest substring with k distinct characters is "bcb".

def longest_substring(str, k):
	p1 = 0
	p2 = 0

	distincts = {
		str[p2] = True
	}

	length = 0

	while p2 < len(str) - 1:
		if len(distincts) >= k+1:
			old_s = str[p1]
			p1 = p1 + 1
			new_s = str[p1]

			if old_s != new_s:
				del distincts[old_s]

		if distincts <= k:
			old_s = str[p2]
			p2 = p2 + 1
			new_s = str[p2]

			if old_s != new_s:
				distincts[new_s] = True

	return len(distincts)