
class Book():
    def display():
        raise NotImplementedError

#Write MyBook class
class MyBook(Book):
        def __init__(self, title, author, price):
            self.title = title
            self.author = author
            self.price = price

        def display(self):
            print(f'Title: {self.title}')
            print(f'Author: {self.author}')
            print(f'Price: {self.price}')


title=input('Insert title: ')
author=input('Insert author name: ')
price=int(input('Insert book price: '))
new_novel=MyBook(title,author,price)
new_novel.display()