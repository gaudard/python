#chapter 10 lab

#create a class with 3 functions. Functions init, read, write.


class FileLogMessage:
	def __init__(self,filename):
		self.filename = filename

	def write(self, message):
		output = open('logfile.txt', 'a')
		output.write(message)
		
		
	def read(self):
		f = open(self.filename, 'r')
		lines = f.readlines()
		for each in lines:
			print(each, end='')
		

		
'''
test = FileLogMessage('test.txt')
test.write('testing..' + '\n')
test.read()
'''

