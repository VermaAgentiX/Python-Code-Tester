class Book:

    def __init__(self, n, i, p, c, a):
        self.n = n
        self.i = i
        self.p = p
        self.c = c
        self.a = a


class Shop:

    def __init__(self):
        self.b = []

    def add(self, x):
        self.b.append(x)

    def price(self, i):
        for x in self.b:
            if x.i == i:
                return x.p

        return None

    def update(self, c, p):
        for x in self.b:
            if x.c.lower() == c.lower():
                x.p = x.p + p

    def show(self):
        for x in self.b:
            print(x.i, x.n, x.p, x.c, x.a)


s = Shop()

s.add(Book("The Shining", "B101", 499, "Horror", "Stephen King"))
s.add(Book("Pride and Prejudice", "B102", 399, "Romance", "Jane Austen"))
s.add(Book("Sapiens", "B103", 699, "Non-fiction", "Yuval Noah Harari"))
s.add(Book("It", "B104", 549, "Horror", "Stephen King"))

print("Books in the shop:")
s.show()

i = input("\nEnter book ID: ")

p = s.price(i)

if p is not None:
    print("Price of book:", p)
else:
    print("Book not found")

c = input("\nEnter category to update price: ")
p = float(input("Enter amount to add: "))

s.update(c, p)

print("\nUpdated book details:")
s.show()