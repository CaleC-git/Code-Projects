class Author:
    def __init__(self, name):
        self.name = name
        self.books = []

    def publish(self, title):
        self.books.append(title)

    def __str__(self):
        return self.name

matt = Author("Matt Dinniman")
matt.publish("Dungeon Crawler Carl")

print(matt)