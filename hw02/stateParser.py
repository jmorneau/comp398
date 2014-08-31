class Node:


	def __init__(self):
		self.state = None
		self.info = None
		self.next = None

	def return_state(self):
		return self.state

	def return_info(self):
		return self.info
	

class LinkedList:


	def __init__(self):
		self.current = None
		self.head = None

	def add_node(self, state, other):
		new_node = Node()
		new_node.state = state
		new_node.info = other

		if self.head == None:
			self.current = new_node
			self.head = new_node
		else:
			self.current.next = new_node
			self.current = self.current.next

	def find(self, find_state):
		pointer = self.head
		if pointer.state == find_state:
			return pointer.state
		else:
			while pointer.next != None:
				pointer = pointer.next
				if pointer.state == find_state:
					return pointer.state
		print "Sorry, your item was not found"
	
	def display(self):
		pointer = self.head
		while pointer != None:
			print pointer.state + "\t" + pointer.info	
			pointer = pointer.next
	
