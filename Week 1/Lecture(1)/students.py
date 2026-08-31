class Student: # creates class
    def __init__(self, name, school_id, gpa): # adds the attributes to the class
        self.name = name
        self.school_id = school_id
        self.gpa = gpa

    def __str__(self):
        return f"Student name: {self.name}, ID: {self.school_id}, GPA: {self.gpa}"

alex = Student("Alex", "ababab", 3.12)
print(alex.name)
print(alex.school_id)
print(alex)
#example of the class being utilized

sam = Student("Sam", "qwerty", 4.0)
print(sam)