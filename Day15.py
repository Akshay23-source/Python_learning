numbers = []

for i in range(1, 6):
    numbers.append(i)

print(numbers)


numbers = [i for i in range(1, 6)]
print(numbers)


even = []

for i in range(1, 11):
    if i % 2 == 0:
        even.append(i)
        
       
        
        
     even = [i for i in range(1, 11) if i % 2 == 0]
print(even)



   squares = [i*i for i in range(1, 6)]
print(squares)



words = ["python", "java", "c++"]

upper_words = [word.upper() for word in words]
print(upper_words)


squares = {i: i*i for i in range(1, 6)}
print(squares)





unique_squares = {i*i for i in range(1, 6)}
print(unique_squares)
