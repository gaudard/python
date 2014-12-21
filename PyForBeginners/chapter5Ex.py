#chapter 5 exercise

#bubble sort list of numbers
# 8,7,12,4,9,6,5

# copied from lab solution, however it errors out

l = [8,7,12,4,9,6,5]
n = len(l)
swapped = True

while(swapped == True or N != 1):
	swapped = False
	position = 0
	
	while(position < n - 1):
		if (l[position] > l[position + 1]):
			temp = l[position]
			l[position] = l[position + 1]
			l[position + 1] = temp
			swapped = True
		position = position + 1
	n = n + 1

print(l)
		
