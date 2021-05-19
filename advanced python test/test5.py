class Book:
    def details(self,bookname, author, bookpage):
            self.author = author
            self.bookname = bookname
            self.bookpage = bookpage
            print(self.author)
            print(self.bookname)
            print(self.bookpage)
class Library(Book):
    def details(self,libname, place, totalbooks):
        self.libname=libname
        self.place=place
        self.totalbooks=totalbooks
        print(self.libname,self.place,self.totalbooks)
lib=Library()
lib.details("ABCD","Kolenchery",10000)

