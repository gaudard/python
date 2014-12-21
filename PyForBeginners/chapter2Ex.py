# Chapter 2 exercise
# v = final velocity
# u = initial velocity
# a = acceleration (solving for)
# t = time
#int will error if a float is used, set all variables to floats

v = float(input('final velocity: '))
u = float(input('inital velocity: '))
t = float(input('time: '))

a = (v-u)/t

print(type(a), a) #prints type of a and value of a

