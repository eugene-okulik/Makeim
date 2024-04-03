class Books:
    material = 'бумага'
    presence_of_text = True

    def __init__(self, book_name, author, count_pages, isbn, reserved_status=False):
        self.book_name = book_name
        self.author = author
        self.count_pages = count_pages
        self.isbn = isbn
        self.reserved_status = reserved_status


book_1 = Books('Идиот', 'Достоевский', '500', '2-266-11156-6')
book_2 = Books('Война и мир', 'Толстой', '1010', '978-5080043987')
book_3 = Books('Мастер и Маргарита', 'Булгаков', '650', '978-5080043981')
book_4 = Books('Маленький принц', 'Экзюпери', '259', '978-5082043987')
book_5 = Books('Метро 2033', 'Глуховский', '384', '2-266-22226-6')

books = [book_1, book_2, book_3, book_4, book_5]
book_5.reserved_status = True

for book in books:
    if book.reserved_status:
        print('Название: ' + book.book_name + ', Автор: ' + book.author + ', страниц: ' + book.count_pages
              + ', материал: ' + book.material + ', зарезервирована')
    else:
        print('Название: ' + book.book_name + ', Автор: ' + book.author + ', страниц: ' + book.count_pages
              + ', материал: ' + book.material)
