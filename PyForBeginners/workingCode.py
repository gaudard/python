## playing with databases

import sqlite3

db = sqlite3.connect('firstDatabase.db')
db.row_factory = sqlite3.Row
findClothing = db.execute('select * from clothing')

for each in findClothing:
	print(dict(each))
