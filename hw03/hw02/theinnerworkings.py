class Node:
    
    
    """
    The class Node is used in the linked list
    to store the data and a pointer to the next 
    Node object in the list.
    
    Attributes:
    word: stores the data
    up_next: stores the node pointer
    """
    
    def __init__(self, word):
        """
        Initilizes Node class with two varaibles 
        word, which stores the data, and
        up_next, which stores the pointer to the next node
        """
        
        self.word = word
        self.up_next = None 
        
    
    def here(self):
        """
        Returns the data stored in the Node's word varaible
        """
        
        return self.word
    
    def next_node(self):
        """
        Returns the data stored in the Node's up_next varaible
        """
        
        return self.upnext
    
    def new_word(self, werd):
        """
        Adds a word to the Node
        """
        
        self.word = werd
        
    def new_up_next(self, nxt):
        """
        Adds a new pointer node pointer to the node
        """
        
        self.up_next = nxt
        
        

class Lst:
    """
    The class Lst links the the Nodes together and adds data to the node
    Stores a head node for searching the list
    
    Attributes:
    head: used to point to the last item added to the list
    """
    
    def __init__(self):
        """
        Initlizes the Lst class with a pointer to the head of the list
        """
        
        self.head = None
        
    def add_stuff(self, stuff):
        """
        Adds a new item to the list using the Node class
        """
        
        temp = Node(stuff)
        temp.new_up_next(self.head)
        self.head = temp
    
    def pull_one_out(self, searchable):
        """
        Basic search function for the list
        """
        begin = self.head
        
        got_it = "It is not in the list"
        
        i=False
        
        
        while begin != None and not i:  
            #While loop to go over the list comparing the given item to the items in list
            if begin.here() == searchable:
                #if found
                got_it = "It is in the list"
                i=True
            else:
                #if not found
                begin = begin.next_node()
                
        return gotit
        
    def return_all(self):
        """
        Prints list
        """
        begin = self.head
        
        while begin != None:
            print begin.here()
            begin = begin.next_node()
        
        
def main():
    """
    nothing to see here
    """
    
    pass


if __name__ == '__main__':
    main()