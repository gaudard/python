#chapter 11 lab

#create a class with 3 functions. Functions init, read, write.

import sqlite3

class LogMessage:
	def __init__(self,dbname):
		self.dbname = dbname
		db = sqlite3.connect(self.dbname)
		db.execute('create table if not exists LogMessage (message)')
		db.commit()
		db.close()
		
	def read(self):
		db = sqlite3.connect(self.dbname)
		data = db.execute('select * from LogMessage')
		for each in data:
			print(each)
		db.close()
		
	def write(self, message):
		db = sqlite3.connect(self.dbname)
		db.execute('insert into LogMessage (message) values (?)', (message,))
		db.commit()
		db.close()

test = LogMessage('firstDatabase.db')
test.write('testing')
test.read()

