class Animal():
    def talk(self):
        pass


class Cat:
    def __init__(self, name):
        self.name=name


    def talk(self):      
        print('I am '+ self.name+':'+ ' " najv, najv,najv"')

class Dog:
    def __init__(self, name):
        self.name=name

    def talk(self):        
        print( 'I am '+ self.name+':'+ ' " gav, gav,gav"')

c=Cat('Murzik')
c1=Dog('Tyzik')
for i in (c,c1):
    i.talk()
    
