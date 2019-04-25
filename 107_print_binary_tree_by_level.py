
# Print the nodes in a binary tree level-wise. For example, the following should print 1, 2, 3, 4, 5.

#   1
#  / \
# 2   3
#    / \
#   4   5


def print_binary_tree(tree):
	queue = [tree]
	
	while(queue):
		node = queue[0]
		queue = queue[1:]
		print(node.val)

		if node.left:
			queue.append(node.left)
		if node.right:
			queue.append(node.right)



class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


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


print_binary_tree(A)




