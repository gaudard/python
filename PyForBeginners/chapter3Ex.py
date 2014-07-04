# Chapter 3 exercise
# v = variable 1
# u = variable 2

v = int(input('variable v: '))
u = int(input('variable u: '))


var = True if v == True and u == True else False

print(var)

var = True if v == True or u == True else False

print(var)

var = True if v != True else False

print(var)
