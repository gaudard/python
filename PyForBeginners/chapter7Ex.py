#chapter 7

# validate string id:key
# valid id:key 09812354387623:adkc48sl283l4kf

string = '09812a34387623:0000!!!00000'

splitChar = ':'

temp = (string.split(splitChar))

idnum = temp[0]
key = temp[1]

if(idnum.isdigit() == True):
	if(key.isalnum() == True):
		if(len(idnum) == 14):
			if(len(key) > 10 and len(key) < 20):
				print('validated')
			else:
				print('invalid key length')
		else:
			print('invalid id length')
	else:
		print('invalid key')
else:
	print('invalid id')
