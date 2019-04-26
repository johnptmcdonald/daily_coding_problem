
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









