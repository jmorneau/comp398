# Julia Morneau

def get_file(self, filename):
	file = open(filename, "r")
	string = file.split("\n")

	file.close()	
