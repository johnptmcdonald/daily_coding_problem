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
	if root is None:
		return '#'
	return '{} {} {}'.format(root.val, serialize(root.left), serialize(root.right))

#		   A
#		  / \
#		 /   \
#	    /     \
#	   X	   B
#     / \     /  \
#    Y   Z   C   D


Y = Node('Y')
Z = Node('Z')
X = Node('X', Y, Z)
C = Node('C')
D = Node('D')
B = Node('B', C, D)
A = Node('A', X, B)

print(A.left.val)


