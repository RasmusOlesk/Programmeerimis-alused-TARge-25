"""Teemad:
1.	Klassi loomine (konstruktori ja väljadega)
a.	Vähemalt 2 välja ja 2 meetodit (ei lähe arvesse Getterid ja Setterid)
2.	Klassimuutuja
3.	Pärilus
a.	Vähemalt 1 väli ja 1 meetod
b.	Konstruktor vaikeväärtusega
4.	Katsetamine
a.	Kõik meetodid ja klassimuutuja
5.	Järjendi loomine
a.	Peab sisaldama kokku 100 isendit suhtarvuga 60/40
b.	Kasutama vähemalt üht meetodit kõigi peal
Objektid:
Raamat - Randla
"""

class Book:
    """class variable"""
    Book_count = 0

    def __init__(self, title, author):
        """ Instance fields"""
        self.title = title
        self.author = author
        self.read = False
        Book.Book_count += 1


    """Method 1: Marks the books as read"""
    def mark_as_read(self):
        self.read = True
        return f"the book '{self.title}' has been read."

    """Method 2: return formatted information about the book"""
    def info(self):
        return f"'{self.title}' - {self.author} (read: {self.read})"


"""Inheritance"""
class Textbook(Book):
    def __init__(self, title="Mathematics Textbook", author="Randla", subject="Mathematics"):
        """Call parent constructor"""
        super().__init__(title, author)
        self.subject = subject

    # Additional method
    def subject_info(self):
        return f"The textbook '{self.subject}' is for the subject: '{self.subject}'."


"""Testing"""
print(" Testing ")

"""Create a Book object"""
b1 = Book("Empty Beach", "Randla")
print(b1.info())           #Before reading
print(b1.mark_as_read())   #Mark as read
print(b1.info())           #After reading

"""Create a Textbook object using default values"""
t1 = Textbook()
print(t1.info())
print(t1.subject_info())

"""Show how many total book/Textbook object exist"""
print("Total number of books:", Book.Book_count)


""" Creates a List of 100 instances (60 Books / 40 Textbooks"""

print("\n=== 100 INSTANCES (60 Books / 40 Textbooks) ")

books = []

"""Create 60 Books objects"""
for i in range(60):
    b = Book( f"Book {i+1}", "Randla")
    books.append(b)

"""Create 40 Textbooks objects"""
for i in range(40):
    t = Textbook(title=f"Textbook {i+1}", author="Randla", subject="General Studies")
    books.append(t)

"""Use a method on all instances"""
for b in books:
    b.mark_as_read()

"""Prints summary"""
print("Total instances created:", len (books))
print("Class variable value:", Book.Book_count)



