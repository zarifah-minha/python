class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print("Has been borrowed successfully.", self.title)

        else:
            print("It's already borrowed.", self.title)

    def return_book(self):
        self.is_borrowed = False
        print("Has been returned successfully.", self.title)

book1 = Book("Sherlock Holmes","Doyl Canon")
book2 = Book ("The Wimpy Kid", "Jeff Kinely")
book3 = Book ("Matilda", "Ronald Dali")

book1.borrow()
book1.return_book()

book2.borrow()
book2.return_book()

book3.borrow()
book3.return_book()    