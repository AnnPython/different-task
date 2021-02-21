


class Book:
    def __init__(self, in_zagl, in_author,in_year_publsh, in_isbn):
        self.zagl=in_zagl
        self.author=in_author
        self.year_publsh=in_year_publsh
        self.isbn=in_isbn

class Booking(Book):
    def __init__(self, book,amount):
        Book.__init__(self, book.zagl,book.author, book.year_publsh,  book.isbn)
        self.amount=amount
        
    def  __str__(self):
        return 'Книга в каталоге: ' + "'\n" + self.zagl  + ' автор: ' + self.author +  ' год издания: ' + str(self.year_publsh) + ' количество: ' + str(self.amount) + ' шт '
class Catalog:

    def __init__(self):
        self.catal_book=[]
     

 
    def add_book(self, book, amount):
        vhod=Booking(book, amount)
        for i in self.catal_book:
            if i.zagl == vhod.zagl:
                i.amount=i.amount+vhod.amount
                break
        else:
            self.catal_book.append(vhod)

    def show_all_book(self):
        for i in self.catal_book:
            print(i.zagl,i.author, i.year_publsh,  i.isbn, i.amount)
           

    def remove_book(self,book, amount):
        vuhod=Booking(book, amount)
        for i in self.catal_book:
            if i.zagl==vuhod.zagl:
                if i.amount>=vuhod.amount:
                    i.amount=i.amount-vuhod.amount
                    break
        else:
            raise ValueError('Недостаточное количество')

    def search(self, search, type_search = 'zagl'):
        if type_search =='zagl':
            for i in self.catal_book:
                if i.zagl==search:
                    print('Есть книга '+ i.author, str(i.amount)+ 'шт')
                
                
        elif  type_search == 'author':
            for i in self.catal_book:
                if i.author==search:
                    print('Есть книга ' + i.zagl, str(i.amount)+ 'шт')
                        
                
        else:
            raise ValueError('Нет такой книги')
           
   

    def counter(self):
        for i in self.catal_book:
            if i.amount <=0:
                print('Нет в наличии книг '+ ' автор: '+ i.author, ' код: '+ i.isbn)

    def come_in(self):
        y=0
        for i in self.catal_book:
            y=y+i.amount
        print('Общая сумма книг в наличии ' + str(y) + ' шт')
            
        
f=Book('Мастер и Маргарита', 'Булгаков', 1940, '77777777')
f1=Book('Унесенные ветром' , 'Маргарет Митчелл' , 1936, '55555555')
f3=Book('Семейные узы', 'Даниэла Стил', 2011, '44444444')
f4=Book('Звезда', 'Даниэла Стил', 1993, '33333333')

d=Catalog()
        
d.add_book(f,13)
d.add_book(f1,10)
d.add_book(f3, 7)
d.add_book(f4, 3)


d.remove_book(f, 4)
d.remove_book(f1,10)
d.show_all_book()
d.search('Семейные узы',type_search = 'zagl' )    
d.search('Булгаков',type_search = 'author' )
d.search('Даниэла Стил',type_search = 'author' )
d.counter()
d.come_in()
