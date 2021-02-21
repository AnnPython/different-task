import random

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

    def play(self):
       self.box_chur=[]
       self.box_byb=[]
       self.box_tref=[]
       self.box_pika=[]
   
       for i in  self.box:
         if i.rang=='0' and i.mast=='bybna':
           self.box_byb.append(i)
         elif   i.rang=='0' and i.mast=='churva':
           self.box_chur.append(i)  
         elif   i.rang=='0' and i.mast=='tref':
           self.box_tref.append(i)
         elif   i.rang=='0' and i.mast=='pika':
           self.box_pika.append(i)

    def play2(self):
        for i in self.box:
            if i.mast=='churva':
                f=len(self.box_chur)
                if i.rang==str(f):
                    self.box_chur.append(i)
                   
            elif i.mast=='bybna':
                f1=len(self.box_byb)
                if i.rang==str(f1):
                    self.box_byb.append(i)
                    
            elif i.mast=='tref':
                f2=len(self.box_tref)
                if i.rang==str(f2):
                    self.box_tref.append(i)
                    
            elif i.mast=='pika':
                f2=len(self.box_pika)
                if i.rang==str(f2):
                    self.box_pika.append(i)
              
        print(self.box_chur[0].name,self.box_chur[0].mast,self.box_chur[1].name,self.box_chur[1].mast,self.box_chur[2].name,
              self.box_chur[2].mast,self.box_chur[3].name,self.box_chur[3].mast, self.box_chur[4].name,self.box_chur[4].mast,
              self.box_chur[5].name,self.box_chur[5].mast, self.box_chur[6].name,self.box_chur[6].mast, self.box_chur[7].name,
              self.box_chur[7].mast,self.box_chur[8].name,self.box_chur[8].mast)     
        print(self.box_byb[0].name, self.box_byb[0].mast, self.box_byb[1].name,self.box_byb[1].mast,self.box_byb[2].name,
              self.box_byb[2].mast,self.box_byb[3].name, self.box_byb[3].mast,self.box_byb[4].name, self.box_byb[4].mast, self.box_byb[5].name,
              self.box_byb[5].mast,self.box_byb[6].name,self.box_byb[6].name,self.box_byb[7].name, self.box_byb[7].mast, self.box_byb[8].name, self.box_byb[8].mast)

        print(self.box_tref[0].name, self.box_tref[0].mast, self.box_tref[1].name,self.box_tref[1].mast,self.box_tref[2].name,
              self.box_tref[2].mast,self.box_tref[3].name, self.box_tref[3].mast, self.box_tref[4].name, self.box_tref[4].mast, self.box_tref[5].name,self.box_tref[5].mast,
              self.box_tref[6].name,self.box_tref[6].mast,self.box_tref[7].name, self.box_tref[7].mast, self.box_tref[8].name, self.box_tref[8].mast)

        print(self.box_pika[0].name, self.box_pika[0].mast, self.box_pika[1].name,self.box_pika[1].mast,self.box_pika[2].name,
              self.box_pika[2].mast,self.box_pika[3].name, self.box_pika[3].mast, self.box_pika[4].name, self.box_pika[4].mast, self.box_pika[5].name,
              self.box_pika[5].mast,self.box_pika[6].name,self.box_pika[6].mast,self.box_pika[7].name, self.box_pika[7].mast, self.box_pika[8].name, self.box_pika[8].mast)


m=Constr('tyz', '0', '0b', 'bybna')
m1=Constr('tyz', '0', '0t', 'tref')
m2=Constr('tyz', '0', '0ch', 'churva')
m3=Constr('tyz', '0', '0p', 'pika')

m4=Constr('six', '1', '1b ', 'bybna')
m5=Constr('six', '1', '1p', 'pika')
m6=Constr('six', '1', '1ch', 'churva')
m7=Constr('six', '1', '1tr', 'tref')

m8=Constr('seven', '2', '2b', 'bybna')
m9=Constr('seven', '2', '2ch', 'churva')
m10=Constr('seven', '2', '2tr', 'tref')
m11=Constr('seven', '2', '2p', 'pika')

m12=Constr('eight', '3', '3p', 'pika')
m13=Constr('eight', '3', '3tr', 'tref')
m14=Constr('eight', '3', '3b', 'bybna')
m15=Constr('eight', '3', '3ch', 'churva')

m16=Constr('nine', '4', '4ch', 'churva')
m17=Constr('nine', '4', '4b', 'bybna')
m18=Constr('nine', '4', '4tr', 'tref')
m19=Constr('nine', '4', '4p', 'pika')

m20=Constr('ten', '5', '5p', 'pika')
m21=Constr('ten', '5', '5tr', 'tref')
m22=Constr('ten', '5', '5ch', 'churva')
m23=Constr('ten', '5', '5b', 'bybna')

m24=Constr('val', '6', '6p', 'pika')
m25=Constr('val', '6', '6tr', 'tref')
m26=Constr('val', '6', '6ch', 'churva')
m27=Constr('val', '6', '6b', 'bybna')

m28=Constr('dama', '7', '7p', 'pika')
m29=Constr('dama', '7', '7tr', 'tref')
m30=Constr('dama', '7', '7ch', 'churva')
m31=Constr('dama', '7', '7b', 'bybna')

m32=Constr('king', '8', '8p', 'pika')
m33=Constr('king', '8', '8tr', 'tref')
m34=Constr('king', '8', '8ch', 'churva')
m35=Constr('king', '8', '8b', 'bybna')

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
d.add(m10)
d.add(m11)
d.add(m12)
d.add(m13)
d.add(m14)
d.add(m15)
d.add(m16)
d.add(m17)
d.add(m18)
d.add(m19)
d.add(m20)
d.add(m21)
d.add(m22)
d.add(m23)
d.add(m24)
d.add(m25)
d.add(m26)
d.add(m27)
d.add(m28)
d.add(m29)
d.add(m30)

d.add(m31)
d.add(m32)
d.add(m33)
d.add(m34)
d.add(m35)



d.get_all()
d.play()
d.play2()
