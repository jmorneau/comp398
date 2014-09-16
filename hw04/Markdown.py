# Julia Morneau

def get_file(self, filename):
	""" Gets the markdown file and splits it on every line

	args:
		filename: a markdown file
	returns:
		returns a list of every line in the file
	"""

	file = open(filename, "r")
	string = file.split("\n")

	file.close()	
	return string

def markdown(self, list):
	dict = {'#':<h1>,
		'##':<h2>,
		'###':<h3>,
		'####':<h4>,
		'#####':<h5>,
		'######:<h6>,
		'* ':<li>,
		'**':<em>,
		}
def replace_headers(self, dict, lst):
	for dict in lst:
		
		
	
