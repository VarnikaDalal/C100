class Book(object):
    def __init__(self,name,author,cost):
        self.name=name
        self.author=author
        self.cost=20
    def start(self):
        print("Started Book")
    def end(self):
        print("Finished Book")
    def getAuthor(self,name,author):
        print("Name of book: " + self.name)
        print("Author of book: " + self.author)

books=Book("Harry Potter", "JKR", 10)
books.getAuthor("Harry Potter", "JKR")
print(books.cost)