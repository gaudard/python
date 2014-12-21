#lesson 12


from chapter11Ex import DBLogMessage
from chapter10Ex import FileLogMessage

test = DBLogMessage('secondDatabase.db')
test.write('This is for Chapter 12!!!')
test.read()

test2 = FileLogMessage('chapter12.txt')
test2.write('This is also for Chapter 12!!' + '\n')
test2.read()



