1. The code would not run on my machine.

Style Guide Evaluation:
	1. Between methods there should be only one blank line, however for some you have two and others you have one, be consistant.
	2. The white spacing is good, however in your driverprogram.py, in your for loop there should be only one tab and you have two.  Both your Node and Lst class have the correct white spacing.  
	3. Comments for introducing classes could be more descriptive but follow the proper style guide.  However for your methods, you breifly explain what they do, however you do not discuss the Arguments or the Returns.  For the arguments you should discuss their types.  When you are explaining the returns, you should have an example as well as the description of the returns.
	4. All of your strings follow the style guide.
	5. All files are opened then closed using the style guide.
	6.Your main function also follows the style guide
	7. All importing files is completed properly and done by the style guide specifications.

Code Evaluation:
	1. There is an error on line 33 in the driverprogram.py therfore I could not get any output nor see if anything else worked properly. THis is because you call the method pulloneout(), however that does not exist because in your class definition it is called pull_one_out.  Make sure you are consistant with your naming or else errors will arise. 
	2. In your node class be consistant with your naming. in your __init__ the next node is up_next where in your next_node, the next node is upnext.  This will cause an error and not beable to run.	
	3. In your Lst class you use next_node() however that is not defined anywhere, did you mean new_up_next(). Because next_node() is not defined there will be an error.
	4. In your pull_one_out() method you are returning gotit, however it is definied earlier as got_it, this will also produce an error because gotit is not defined anywhere. Double check all variables when coding.
	5. The design of your code is all very simple and straight forward, everything flows and it is very easy to follow the code and know where to look when you are tracing through it.
