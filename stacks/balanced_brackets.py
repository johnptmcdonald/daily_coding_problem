# The classic!

def balancedBrackets(string):
	stack = []

	matchingBrackets = {
		')': '(',
		']': '[',
		'}': '{'
	}

	for bracket in string:
		if bracket in matchingBrackets.values():
			stack.append(bracket)
		else:
			if len(stack) == 0:
				return False
			if matchingBrackets[bracket] == stack[-1]:
				stack.pop()
			else:
				return False

	return len(stack) == 0


print(balancedBrackets("(({{}}))"))

