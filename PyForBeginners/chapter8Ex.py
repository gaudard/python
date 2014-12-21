# chapter 8 exercise

# create a function that will return a string of the type of data passed

def checkType(var):
	var = str(var)
	if(var.isalpha()):
		return 'alpha'
	elif(var.isdigit()):
		return 'number'
	elif(var.isalnum()):
		return 'aphanum'
	else:
		return 'unknown'
	
	
var = input('input something:\n')

print(checkType(var))
