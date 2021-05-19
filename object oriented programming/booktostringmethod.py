#tostng method
###only return one string value.if u are added more than one value use string concat

class Book:
    def __init__(self,author,bookname,bookpage):
        self.author=author
        self.bookname=bookname
        self.bookpage=bookpage
    def display(self):
        print(self.author)
        print(self.bookname)
        print(self.bookpage)
    def __str__(self):
        return self.bookname+self.author+str(self.bookpage)
bk=Book("abc","python",654)
bk.display()
print(bk)
