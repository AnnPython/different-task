import random
import tkinter as tk
root = tk.Tk()
root.title('"Однорукий бандит"')
root.geometry('300x400')
root["bg"] = "#2F9865"
def change():
  for i in range(3):
    f=random.randint(0,9)
    b3['text']=f
    f1=random.randint(0,9)
    b4['text']=f1
    f2=random.randint(0,9)
    b5['text']=f2


  if f==f1  and f1==f2:
    print("Поздравляем ты выиграл")
  elif f==f2 and f2==f1:
    print("Поздравляем ты выиграл!!!")
  else:
    print("ты проиграл-лузер")  

b2=label = tk.Label(text='тебе повезет \n ги ги г и', font=("Comic Sans MS", 20, 'bold'), fg='green',bg='#85B59E')
label.grid(row=0, column=1) 

b3=label = tk.Label(width=3, height=3, bg='#B2D159', text='///', font=("Calibri", 24, 'bold'),fg='black')
label.grid(row=2, column=0)   

b4=label = tk.Label(width=3, height=3, 
           bg='#B2D159', text='///', font=("Calibri", 24, 'bold'),fg='black')

label.grid(row=2, column=1) 
b5=label = tk.Label(width=3, height=3, 
           bg='#B2D159', text='///', font=("Calibri", 24, 'bold'),fg='black')
label.grid(row=2, column=3) 
frame = tk.Frame(root)
frame['borderwidth'] = 30    
frame['relief'] = 'groove'
frame['border']=20

b1 = tk.Button(text='сыграем;)', font=("Calibri", 24, 'bold'),width=8, height=1,bg='#85B59E',fg='green')
b1.config(command=change )
b1.grid(row=7, column=1) 
root.mainloop()
