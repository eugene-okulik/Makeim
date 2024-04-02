class Books:
    material = 'бумага'
    presence_of_text = True

    def __init__(self, book_name, author, count_pages, isbn, reserved_status=False):
        self.book_name = book_name
        self.author = author
        self.count_pages = count_pages
        self.isbn = isbn
        self.reserved_status = reserved_status


class Textbooks(Books):
    avail_task = True

    def __init__(self, book_name, author, count_pages, isbn, subject, group, reserved_status=False):
        super().__init__(book_name, author, count_pages, isbn, reserved_status)
        self.subject = subject
        self.group = group


textbook_1 = Textbooks('Алгебра', 'Иванов', '180', '2-262-11256-6', 'Математика', '10')
textbook_2 = Textbooks('География России', 'Паркшатов', '250', '978-2210043987', 'География', '7')
textbook_3 = Textbooks('История Руси', 'Иванина', '432', '911-5080043981', 'История', '9')
textbook_4 = Textbooks('Обществознание', 'Марцун', '201', '978-5555543987', 'Обществознание и Право', '11')

textbooks = [textbook_1, textbook_2, textbook_3, textbook_4]
textbook_3.reserved_status = True

for textbook in textbooks:
    if textbook.reserved_status:
        print('Название: ' + textbook.book_name + ', Автор: ' + textbook.author + ', страниц: ' + textbook.count_pages
              + ', предмет: ' + textbook.subject + ', класс: ' + textbook.group + ', зарезервирована')
    else:
        print('Название: ' + textbook.book_name + ', Автор: ' + textbook.author + ', страниц: ' + textbook.count_pages
              + ', предмет: ' + textbook.subject + ', класс: ' + textbook.group)
