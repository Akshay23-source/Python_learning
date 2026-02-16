file = open("filename.txt", "mode")



file = open("demo.txt", "w")
file.write("Hello Akshay\n")
file.write("Python is powerful")
file.close()





file = open("demo.txt", "r")
content = file.read()
print(content)
file.close()




file = open("demo.txt", "a")
file.write("\nNew line added")
file.close()




with open("demo.txt", "r") as file:
    print(file.read())


with open("demo.txt", "r") as file:
    for line in file:
        print(line)
