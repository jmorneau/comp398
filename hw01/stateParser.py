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
			while(pointer.next != None):
				pointer = pointer.next
				if pointer.state == find_state:
					return pointer.state
		print "Sorry, your item was not found"
	
	def display(self):
		pointer = self.head
		while(pointer != None):
			print pointer.state + "\t" + pointer.info	
			pointer = pointer.next
	
def main():

# 1. Creating an empty Linked List
	linked_list = LinkedList()

# 2. Adding a single Node to Linked List
	linked_list.add_node( "States", "Population" )
	
# 3. Populating LinkedList with data collected from class
	f = open("Sheet1.csv","r")

	for line in f:
		temp = line.split(",")

		
		s = temp[0]
		i = "Population : " + temp[1]
#		"SquareRoot of Pop" : temp[2],
#		"Electoral College" : temp[3],
#		"Penrose" : temp[4],
#		"Banzhaf" : temp[5],
#		"Equitability Measure" : temp[6],
#		"weightRatio" : temp[7],
#		"New Electoral College" : temp[8],
#		"deltaWeight" : temp[9],
#		"New Penrose" : temp[10],
#		"New Bhanzaf" : temp[11],
#		"New Equitability" : temp[12]}

		linked_list.add_node( s, i )

	f.close()
	
# 4. Searching for "Texas" in LinkedList
	print linked_list.find("Texas")

# 5. Displaying LinkedList
	linked_list.display()


if __name__ == '__main__':
	main()
