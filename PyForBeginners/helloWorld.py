#version 2 method
c = "hello"
d = "%s world" % c

#version 3 method
a = "hello"
b = "{} world".format(a)

print d, b
