def square(x):
    return x * x

print(square(5))



square = lambda x: x * x
print(square(5))



add = lambda a, b: a + b
print(add(10, 20))


numbers = [1, 2, 3, 4]
squares = []

for n in numbers:
    squares.append(n * n)

print(squares)




numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x*x, numbers))
print(squares)





numbers = [1, 2, 3, 4, 5, 6]

even = list(filter(lambda x: x % 2 == 0, numbers))
print(even)




from functools import reduce

numbers = [1, 2, 3, 4]

total = reduce(lambda a, b: a + b, numbers)
print(total)





