# Map() function
# apply a function to a list and create a new list with these values
def func(x):
    return x * x


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(map(func, lst)))  # map
print([func(x) for x in lst])  # list comprehension
print([func(x) for x in lst if x > 5])  # list comprehension
