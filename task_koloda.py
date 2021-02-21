class Constr:
    def __init__(self, in_name, in_rang, in_psev, in_mast):

        self.name = in_name
        self.rang = in_rang
        self.psev = in_psev
        self.mast = in_mast

class Prisv(Constr):
    def __init__(self, constr):
        Constr.__init__(self, constr.name, constr.rang, constr.psev, constr.mast)


class Koloda():
    def __init__(self):
        self.box=[]

    def add (self, constr) :
        vhod=Prisv(constr)
        for i in self.box:
            if i.psev ==vhod.psev:
                print('Карта не добавлена, карта есть в колоде')
                
                break
        else:
            self.box.append(vhod)
            

    def get_all(self):
        for i in self.box:
            print('Карта в колоде '+ i.name + ' '+ i.mast)
       
    def ran(self):
      import random
      
      for i in self.box:        
          random.shuffle(self.box)        
      
      print(self.box)

      
    def choice(self):
        import random
        q=random.choice(self.box)
        print('Случайная карта ' + q.name, q.mast )
        for i in self.box:
            if i==q:
                self.box.remove(i)
                x=len(self.box)
                print('Осталось в колоде ' + str(x) + ' карта')

        
m=Constr('Two', 'b', '1b', 'bybna')
m1=Constr('Three', 't', '2t', 'tref')
m2=Constr('Four', 'ch', '3ch', 'churva')
m3=Constr('Five', 'p', '4p', 'pika')
m4=Constr('Five', 'p', '4p', 'pika')
m5=Constr('Two', 'p', '1p', 'pika')
m6=Constr('Two', 'ch', '1ch', 'churva')
m7=Constr('Two', 't', '1tr', 'tref')
m8=Constr('Three', 'b', '2b', 'bybna')
m9=Constr('Three', 'ch', '2ch', 'churva')


d=Koloda()

d.add(m)
d.add(m1)
d.add(m2)
d.add(m3)
d.add(m4)
d.add(m5)
d.add(m6)
d.add(m7)
d.add(m8)
d.add(m9)

d.get_all()
d.ran()
d.choice()



    
