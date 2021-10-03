# 7 -  Collections - namedtuple()

import collections
from collections import namedtuple

Point = namedtuple('Point', 'x y z')  # it accepts an iterable value as names of variables

newP = Point(3, 4, 5)

print(newP)
print(newP.x, newP[0])
print(newP._asdict())  # print is as dict
print(newP._fields)  # naems of fields

print(newP._replace(y=6))  # creates a new namedtuple with new values
print(newP.y)  # original value still the same

p2 = Point._make(['a', 'b', 'c'])  # another way of assiging values
print(p2)
