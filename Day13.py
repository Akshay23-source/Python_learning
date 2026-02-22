print(10 / 0)


try:
    num = int(input("Enter number: "))
    print(10 / num)
except:
    print("Something went wrong")
    
    
    
    
    try:
    num = int(input("Enter number: "))
    print(10 / num)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Invalid input")
    
    
    
    
    
    try:
    num = int(input("Enter number: "))
    result = 10 / num

except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print("Result is", result)
    
    
    
    try:
    print("Try block")
except:
    print("Error")
finally:
    print("Always runs")
    
    
    
    age = int(input("Enter age: "))

if age < 18:
    raise Exception("Not eligible")