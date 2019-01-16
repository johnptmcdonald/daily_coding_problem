# Given the root to a binary tree, implement serialize(root), 
# which serializes the tree into a string, and deserialize(s), 
# which deserializes the string back into the tree.

# For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# The following test should pass:

# node = Node('root', Node('left', Node('left.left')), Node('right'))

# assert deserialize(serialize(node)).left.left.val == 'left.left'

def serialize(root):
	# just a depth first traversal
	if root is None:
		return 'None'
	return '{} {} {}'.format(root.val, serialize(root.left), serialize(root.right))


def deserialize(data):
	def helper():
		val = next(vals)
		if val == 'None':
			return None

		node = Node(val)
		node.left = helper()
		node.right = helper()
		return node

	vals = iter(data.split())
		
	return helper()


#		   A
#		  / \
#		 /   \
#	    /     \
#	   X	   B
#     /       /  \
#    Y       C   D


Y = Node('Y')
X = Node('X', Y)
C = Node('C')
D = Node('D')
B = Node('B', C, D)
A = Node('A', X, B)

import unittest

class Test_serialize_and_deserialize_tree(unittest.TestCase):

	def setUp(self):

		Y = Node('Y')
		X = Node('X', Y)
		C = Node('C')
		D = Node('D')
		B = Node('B', C, D)
		self.A = Node('A', X, B)

	def test_serialize(self):
		self.assertEqual(serialize(self.A), "A X Y None None None B C None None D None None")

	def test_deserialize(self):
		self.assertEqual(serialize(deserialize("A X Y None None None B C None None D None None")), "A X Y None None None B C None None D None None")


unittest.main()
