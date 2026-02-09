def greet():
    print("Hello, welcome to Python")
    greet()
    greet()
    
    



def greet(name):
    print("Hello", name)

greet("Akshay")
greet("Python")



def add(a,b):
    return a+b,a-b
result1=add(10,20)
print(result1)



def check_even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(check_even(1))
print(check_even(20))

