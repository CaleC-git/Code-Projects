class_names = [] # an empty list for the class names

class_amount = int(input("How many classes are you taking? ")) # asks the amount of classes the user is taking

for I in range(class_amount): # loops through the class amount
    course_name = input("Enter class name: ")
    class_names.append(course_name) # adds the class name to the list

for I in range(len(class_names)): # loops through the number of class names
    print(class_names[I]) # prints out the class names