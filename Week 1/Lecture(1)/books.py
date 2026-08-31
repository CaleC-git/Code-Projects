class Author: # creates the class 
    def __init__(self, name):
        self.name = name
        self.books = [] # makes an empty list for the class

    def publish(self, title):
        self.books.append(title) # adds the book title to class list

    def __str__(self):
        return self.name

matt = Author("Matt Dinniman")
matt.publish("Dungeon Crawler Carl")

print(matt)