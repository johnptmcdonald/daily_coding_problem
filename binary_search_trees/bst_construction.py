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


	def remove(self, value):
		# get the min value in the right subtree beneath the value you want to delete
		pass





