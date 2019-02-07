# given a BST and an integer, write a function that returns the value in the BST 
# closest to that integer

# Each node in the tree has the properties 'value', 'left', and 'right'

def findClosestValueInBst(tree, target):
    # Don't use recursion, as that takes up space on the call stack

    # initialize current distance, and the corresponding closest current node
	current_distance = abs(target - tree.value)
	closest_current_node = tree
	
	# start with the current node...
	current_node = tree

	# ...and while it is not none...
	while current_node is not None:
		if abs(current_node.value - target) < current_distance and current_node is not None:
			closest_current_node = current_node		
			current_distance = abs(current_node.value - target)
		if target > current_node.value:
			current_node = current_node.right

		elif target < current_node.value:
			current_node = current_node.left
		
		elif current_distance == 0:
			return target

		
	return closest_current_node.value
	