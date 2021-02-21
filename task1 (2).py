class Book:
    def __init__(self, name, year, author, amount):
        self.name = name
        self.year = year
        self.author = author # должен быть объект класса Author
        self.amount = amount

    @property
    def author(self):
      return self._author

    @author.setter
    def author(self, _znach):
      if type( _znach) is not Author:
          raise ValueError( 'автор не добавлен')
      self._author = _znach      

    @author.deleter
    def author(self):
        del self._znach  


    def __str__(self):
        return self.name + ' -- ' + self.author.name + ' ' + str(self.year) + ' ' + str(self.amount) + ' шт.'

    def __repr__(self):
        return self.name + ' -- ' + self.author.name  + ' ' + str(self.year) + ' ' + str(self.amount) + ' шт.'



class Author:

    ''' name, country, birthday, books = [] '''

    def __init__(self, name, country, birthday, bibliography):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []
        self.bibliography = bibliography

    def appen_new_book(self, book_name):
        self.bibliography.append(book_name)

    def __str__(self):
        return self.name + ' -- ' + self.birthday

    def __repr__(self):
        return self.name + ' -- ' + self.birthday


g = Author('Andrzej Sapkowski', 'Poland', '1948-06-21',('Krew Elfów', 'Czas Pogardy'))
#t=Book('Nine princes in Amber', 2010, 'Andrzej Sapkowski', 10)
t1=Book('The Guns of Avalon', 2010, g, 10)
#print(t)
print(t1)
