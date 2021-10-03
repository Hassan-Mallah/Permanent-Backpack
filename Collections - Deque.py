# Collections - Deque(deck)

from collections import deque

d = deque("Hello")
print(d)

d.append('4')
d.append(5)
print(d)

d.appendleft(6)
print('appendleft', d)

d.pop()  # remove last element
print(d)

d.popleft()  # remove 1st element
print(d)

d.clear()
print(d)

d.extend('World')
print((d))

d.extendleft('Hey')  # add in reverse order
print('extendleft', d)

d.rotate(-1)  # move deck one step backward
print('rotate -1', d)

d.rotate(2) # move deck two step backward
print('rotate +2', d)

# max length
d2 = deque('Hello', maxlen=5)
print('maxlen', d2)

d2.append(1)  # removes 1st value and adds new value
print(d2)

d2.extend([1, 2, 3])  # removes 3 values and adds new values
print(d2)