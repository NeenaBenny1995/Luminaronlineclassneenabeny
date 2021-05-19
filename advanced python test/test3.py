#tostng method
###only return one string value.if u are added more than one value use string concat

class Book:
    def __init__(self,libname,bookname,author,bookpage):
        self.libname=libname
        self.author=author
        self.bookname=bookname
        self.bookpage=bookpage
        print(self.libname)
        print(self.author)
        print(self.bookname)
        print(self.bookpage)

bk=Book("abc","python","jeeva",654)

