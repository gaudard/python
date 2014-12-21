#chapter 4 exercise
#create fibonacci sequence and stop at the first number greater than 100
#Fn = Fn-2+Fn-1, inital values F0=0 and F1=1

Fn = 0
F0 = 0
F1 = 1
check = False

while True:
	Fn = F0 + F1
	F1 = F0
	F0 = Fn
	if(Fn > 100):
		check = True
		#print('check true')
	else:
		check = False
	print(Fn)
	if(check == True):
		#print('break')
		break
	

	
