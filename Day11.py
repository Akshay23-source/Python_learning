class Student:
    name = "Akshay"


s1 = Student()
print(s1.name)


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Akshay", 20)
print(s1.name)
print(s1.age)


class Student:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, my name is", self.name)

s1 = Student("Akshay")
s1.greet()



s1 = Student("Akshay")
s2 = Student("Rahul")
