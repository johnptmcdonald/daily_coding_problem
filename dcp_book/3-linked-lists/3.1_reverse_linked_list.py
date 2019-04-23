
# Given the head of a singly linked list, reverse it in place

# 
# head
#  \
#   \
#  [23]->[12]->[4]->[8]->[34]->null

# ==> 

# head
#  \
#	\	
#  [34]->[8]->[4]->[12]->[23]->null



def reverse_linked_list(ll):
	prev, node = None, ll.head

	while node:
		temp = node.next

		node.next = prev
		prev = node
		node = temp

	return prev



class LinkedList:
	def __init__(self, head=None):
		self.head = head

	def prepend(self, value):
		# head						# head
		#  \						#  \
		#   \						#   \
		#  [23]->[12]->null			#   [4]->[23]->[12]->null

		self.head = Node(value=value, next=self.head)

	def append(self, value):
		# head						# head
		#  \						#  \
		#   \						#   \
		#  [23]->[12]->null			#  [23]->[12]->[4]->null	
			
		node = self.head
		while node.next:
			node = node.next

		node.next = Node(value=value)

	def __repr__(self):
		node = self.head
		nodes = []
		while node:
			nodes.append(repr(node))
			node = node.next
		return '[' + ', '.join(nodes) + ']'


class Node:
	def __init__(self, value=None, next=None):
		self.value = value
		self.next = next

	def __repr__(self):
		return repr(self.value)


firstNode = Node(23)
ll = LinkedList(firstNode)
ll.append(Node(44))
ll.append(Node(54))
print(repr(ll))

ll.head = reverse_linked_list(ll)
print(repr(ll))
