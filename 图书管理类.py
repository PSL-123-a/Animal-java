class Book:
    def __init__(self,name,writer,isbn,year,status):
        self.name = name
        self.writer = writer
        self.isbn = isbn
        self.year = year
        self.status = status

    def check_out(self):
        self.status = '已借出'

    def check_in(self):
        self.status = '已归还'

    def display_info(self):
        print(f'{self.name}的作者是{self.writer},它的ISBN是{self.isbn},出版年份是{self.year},目前{self.status}')

class Library:
    def __init__(self):
        self.books = []

    def add_book(self,book):
        self.books.append(book)
        print('添加成功！')
        return

    def remove_book(self,isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print('删除成功！')
                return
            print('没找到这本书')

    def list_all_books(self):
        for book in self.books:
            book.display_info()

    def find_book_by_isbn(self,isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

book1 = Book("《三体》", "‘刘慈欣’", "‘9787536692932’", 2008, "在馆")
book2 = Book("《Python编程从入门到实践》", "‘埃里克·马瑟斯’", "‘9787115428027’", 2020, "在馆")

library = Library()

library.add_book(book1)
library.add_book(book2)

library.list_all_books()
