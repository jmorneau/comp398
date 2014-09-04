import theinnerworkings

def main():
    
    
    """
    Creating a linked list using my own linked list moduel 
    """
    
    alst = theinnerworkings.Lst()
 
    
    phylagrabber = open('phyla.txt', 'r')  #file open
    
    """
    for loop to grab data from file
    """
    for line in phylagrabber:
            
            
            x = line
            
            x.split()
            
            number = x.find(":")
            alst.add_stuff(x[0:number])
            
    
    phylagrabber.close()  #file closed
    
    print "Is Rotifera in the list?"
    print "\n"
    x = alst.pulloneout("Rotifera")  #search for Rotifera
    
    print x
    print "\n"
    print "Is Zonicefria in the list?"
    print "\n"
    x = alst.pull_one_out("Zonicefria")  #search for Zonicefria
    
    print x
    print "\n"
    print "Here is the full list"
    print "\n"
    alst.return_all()  #print out the list
    
    
if __name__ == '__main__':
    main()

    
        
    