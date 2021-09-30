# 6 Collections and Counter

from collections import Counter

a = Counter('Hello')
print(a)
b = Counter(['a', 'a', 'b', 'c', 'c'])
print(b)
print(b.most_common(3))  # print top 3 most common keys

c = Counter({'a': 1, 'b': 2})
print(c)

d = Counter(cats=4, dogs=7)
print(d['cats'])  # show for a certain key
print(d['pet'])  # print 0, no error

print(list(d.elements()))  # list of all elements

# subtract + update
e = Counter(a=4, b=2, c=0, d=-2)
f = ['a', 'b', 'b', 'c']
e.subtract(f)  # removes f from e
print(e)

e.update(f)  # add elements
print(e)

e.clear()  # empties the counter
print(e)

# operators + Counters
g = Counter(a=4, b=2, c=0, d=-2)
h = Counter(['a', 'b', 'b', 'c'])
print(g + h)
print(g - h)
print(g & h)  # intersection of 2 counters
print(g | h)  # union - maximum elements
