class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages


    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):
        return self.num_pages < other.num_pages

    def __gt__(self, other):
        return self.num_pages > other.num_pages

    def __add__(self, other):
        return self.num_pages + other.num_pages

    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author

    def __getitem__(self, key):
        if key == "title":
            return self.title
        if key == "author":
            return self.author
        if key == "pages":
            return self.num_pages
        else:
            return f'Key {key} was not found.'



book1= Book("Hobbit", "Osman", 300)
book2= Book("Harry Potter", "JK Rowling", 500)
book3= Book("Aslan Kral","ÖMer",500)

print(book3)
print("Rowling" in book2)
print(book1['ages'])


