print("Hello Capstone") # prints out this message in terminal

# Variables
school = "MCTC" 
gpa = 3.7
students_in_class = 22
# adds variables to the code with assigned numbers or word values ^^^^


# if-statements
if gpa ==4:
    print("WOW!")
elif gpa > 3:
    print("Awesome!")
else:
    print("Cool!")
# This checks the variables from above what their value is, then gives an output dependent on those values and checks


# lists
schools = ["MCTC", "DCTC", "North Hennepin Technical College"]
if "MCTC" in schools:
    print("MCTC is one of the schools in the list")

schools.sort()
print(schools)
schools.append("Century College")
print(schools)

schools.reverse() # will return None
print(schools)


# strings
class_name = "Software Develpoment Capstone"
print(class_name.upper())
print(len(class_name))
print(class_name.split())
print(class_name.split("o"))

if "Capstone" in class_name:
    print("This must be the capstone")


# loops over a range
for x in range(10):
    print(x)


# loops over a sequence
for s in schools:
    print(s.upper())

for letter in school:
    print(letter * 10)

data = [0] * 10
print(data)

more_data = [None] * 10
print(more_data)


# while loops
name = input("Enter your name: ")
while not name:
    print("Please enter at least one character ")
    name = input("Enter your name: ")


# True and False and None
start_of_semester = True
winter = False

if winter:
    print("brr")
else:
    print("it is not winter")

# Disctionaries
class_codes = { 2905: "Capstone", 2560: "Web", 2545: "Java"}

print(class_codes[2560])

for code in class_codes:
    print(code)
    print(class_codes[code])

for code, name in class_codes.items():
    print("The class code is " + str(code) + " and the name is " + name)

for code, name in class_codes.items():
    print(f"The class code is {code} and the name is {name}")


# Slicing strings and lists
schools = ["MCTC", "DCTC", "North Hennepin Technical College"]
first_two = schools[:2]
print(first_two)

last_school = schools[-1]
print(last_school)
last_two_schools = schools[-2:]
print(last_two_schools)

school_name = "Minneapolis Community and Technical College"
city = school_name[:11]
print(city)


# File IO
with open('data.txt') as f:
    print(f.read())

with open("schools.txt", "w") as f:
    f.writelines(schools)


# Functions
def get_name():
    print("Hello, please enter your name!")
    name = input("Your name is: ")
    return name

name = get_name()