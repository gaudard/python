# lesson 6 exercise

while True:
	g = input('enter your gender\n')
	if(g == 'm' or g == 'M' or g == 'f' or g == 'F'):
		break
	else:
		print('please try again\n')
	
print('your gender is {}'.format(g))
