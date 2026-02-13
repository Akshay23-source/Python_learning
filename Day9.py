student = {
    "name": "Akshay",
    "age": 20,
    "branch": "CSE"
}

print(student["name"])
print(student["age"])



student["age"] = 21
print(student)


student["college"] = "ABC University"



student.pop("branch")


print(student.keys())     # All keys
print(student.values())   # All values
print(student.items())    # Key-value pairs


for key in student:
    print(key, student[key])
