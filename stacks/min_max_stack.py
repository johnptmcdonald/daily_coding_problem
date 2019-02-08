# Make a stack where you can always get the min and the max.
# This should all run in constant time


# I used a python list with builtin pop and append
# because making a regular stack is not the point of this exercise

# This could probably be optimized in space:
# no need for self.minMaxStack to be the same size as self.stack
# you should really only add or remove from self.minMaxStack IF the number you are pushing
# or popping is gte(max), or lte(min). 

# that way if you push 1, then 10, then 2, 3, 4, 5, 6, 
# self.minMaxStack will only be two objects high.

class MinMaxStack:

	def __init__(self):
		self.minMaxStack = []
		self.stack = []

	def peek(self):
		return self.stack[len(self.stack) - 1]
	
	def pop(self):
		self.minMaxStack.pop()
		return self.stack.pop()

	def push(self, number):
		newMinMax = {'min': number, 'max': number}
		if len(self.minMaxStack):
			lastMinMax = self.minMaxStack[len(self.minMaxStack)-1]
			newMinMax['min'] = min(lastMinMax['min'], number)
			newMinMax['max'] = max(lastMinMax['max'], number)

		self.minMaxStack.append(newMinMax)
		self.stack.append(number)
			
	def getMin(self):
		return self.minMaxStack[len(self.minMaxStack)-1]['min']

	def getMax(self):
		return self.minMaxStack[len(self.minMaxStack)-1]['max']







		