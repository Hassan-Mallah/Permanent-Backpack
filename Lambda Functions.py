# 5. Lambda Functions - Anonymous function

# simple function
def func(x):
    return x + 5


# lambda inside function
def func3(x):
    func4 = lambda x: x + 10
    return func4(20)


func2 = lambda x: x + 5  # simple lambda
func5 = lambda x, y: x + y  # lambda with 2 variables
func6 = lambda x, y=5: x * y  # lambda with default value

# lambda, map, filter
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_list = list(map(lambda x: x + 5, a))  # lambda with map
new_list2 = list(filter(lambda x: x % 2 == 0, a))  # lambda with filter

print(new_list2)
