import datetime
from datetime import date
from docx import Document

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    x = 10
    def name_yourself(self):
        print(f'{self.name} is {self.age} years old')

person = Person('Yauhen', 36)
print(person)
print(person.name)
print(person.age)
person.name_yourself()


class Publication:
    def __init__(self, title = 'New title', author = 'Yauhen'):
        self.title = title
        self.author = author
        self.year = datetime.datetime.now().year

    def __calculate_date(self):
        return date.today().isoformat()

    def print_date(self):
        print(f'date is {self.__calculate_date()} years old')

pubblication = Publication('New article', 'Yauhen')

print(pubblication.title)
print(pubblication.author)
print(pubblication.year)

class Advertisement(Publication):
    def __init__(self, customer, title, author):
        Publication.__init__(self, title, author)
        self.customer = customer
    def who_is_customer(self):
        print(f'customer is: {self.customer}')


advertisement = Advertisement('Google', 'New add', 'I am')
print(advertisement.title)
print(advertisement.author)
advertisement.who_is_customer()

class Video:
    def __init__(self, quality = '720'):
        self.quality = quality

    def show_quality(self):
        print(f'quality: {self.quality}')



class Movie(Video, Publication):
    def __init__(self, quality = '720', title = 'Yauhen'):
        Video.__init__(self, quality)
        Publication.__init__(self, title)
        # super().__init__()
        self.director = 'Cameroon'


movie = Movie()
movie.show_quality()
movie.print_date()
# movie.__calculate_date()

# test_path = "news_list.docx"
# doc = Document()
# doc.add_paragraph("Adding another paragraph.")
# doc.save(test_path)

# print(f"Test document created and modified successfully: {test_path}")