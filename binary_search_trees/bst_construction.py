# construct BST that supports insert, search, remove

class BST:

	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

	def insert(self, value):
		current_node = self

		while True:
			if value >= current_node.value:
				if current_node.right is None:
					current_node.right = BST(value)
					break
				else:
					current_node = current_node.right
			elif value < current_node.value:
				if current_node.left is None:
					current_node.left = BST(value)
					break
				else:
					current_node = current_node.left

	def find(self, value):
		current_node = self
		
		while current_node is not None:
			if value == self.value:
				return True
			elif value > self.value:
				current_node = self.right
			elif value < self.value:
				current_node = self.left
		return False

	def get_min_value(self):
		current_node = self
		while True:
			if current_node.left == None:
				break
			else:
				current_node = current_node.left

		return current_node.value


	def remove(self, value):
		# get the min value in the right subtree beneath the value you want to delete
		
		# 1) find the value you want to remove
		while True:
			current_node = self
			if value < current_node.value:
				if current_node.left is not None:
					current_node = current_node.left
				else:
					return False
			elif value > current_node.value:
				if current_node.right is not None:
					current_node = current_node.right
				else:
					return False
			else:
				# we have found the item to remove
				# 2) find the min val in the right subtree
				min_val = current_node.right.get_min_value()
				current_node.value = min_val

				# 3) remove the min_val node we just swapped
				current_node = current_node.right
				while True:
					if current_node.value == min_val:
						current_node = None
						break
					else:
						current_node = current_node.left
						
x = BST(2)
x.insert(3)
x.insert(5)
x.insert(1)

print(x.get_min_value())
x.remove(3)

