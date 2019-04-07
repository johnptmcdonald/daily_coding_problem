from collections import defaultdict

# Given a word w and a string s, find all indices in s which are the starting locations of anagrams of w

word = 'ab'
s = 'abxaba'

# output = [0, 3, 4]

def del_if_zero(dict, char):
	if dict[char] == 0:
		del dict[char]

def find_anagram_indices(word, s):
	result = []

	freq = defaultdict(int)

	for char in word:
		freq[char] += 1

	for char in s[:len(word)]:
		freq[char] -= 1
		del_if_zero(freq, char)

	if not freq:
		result.append(0)

	
	for i in range(len(word), len(s)):

		start_char, end_char = s[i - len(word)], s[i]
		print()

		print(i, start_char, end_char)
		freq[start_char] += 1
		del_if_zero(freq, start_char)

		freq[end_char] -= 1
		del_if_zero(freq, end_char)

		if not freq:
			beginning_index = i - len(word) + 1
			print('empty dict', beginning_index)
			result.append(beginning_index)

	print(result)
	return result

find_anagram_indices(word, s)



