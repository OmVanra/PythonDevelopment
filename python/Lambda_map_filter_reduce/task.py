
square = lambda x : x*x
cube = lambda x : x*x*x

print(cube(5))
print(square(5))

numbers = [2, 4, 6, 8, 10]

mul_by_3 = map(lambda x : x * 3, numbers)
print(list(mul_by_3))

numbers = [10, 15, 20, 25, 30, 35, 40]

num_greater_than_20 = filter(lambda x : x > 20, numbers)
print(list(num_greater_than_20))

numbers = [2, 3, 4, 5]

from functools import reduce
product = reduce(lambda x,y : x*y, numbers)
print(product)
