from tkinter import *
from bisect import insort_left
from tkinter.constants import BOTTOM

def mozog(gd, hb):
    global x1, y1
    x1, y1 = x1 + gd, y1+hb
    can1.coords(oval1, x1, y1, x1+kormeret, y1+kormeret)
    
def mozdit_balra():
    mozog(-10,0)
    
def mozdit_jobbra():
    mozog(10,0)
    
def mozdit_fel():
    mozog(0,-10)
    
def mozdit_le():
    mozog(0,10)

def kor_novel():
    global kormeret
    if kormeret<250: 
        kormeret=kormeret+10
        can1.coords(oval1,x1,y1,x1+kormeret,y1+kormeret)
        
def kor_csokken():
    global kormeret
    if kormeret>10: 
        kormeret=kormeret-10
        can1.coords(oval1,x1,y1,x1+kormeret,y1+kormeret)

def piros():        
    can1.itemconfigure(oval1, fill='red')

def kek():        
    can1.itemconfigure(oval1, fill='blue')
    
def zold():        
    can1.itemconfigure(oval1, fill='green')    
    
def sarga():        
    can1.itemconfigure(oval1, fill='yellow')     
           
def fekete_hatter():        
    can1.configure(bg='#00BFFF')      

def zold_hatter():        
    can1.configure(bg='#3CB371')   

def levendula_hatter():        
    can1.configure(bg='#E6E6FA')    
           
x1, y1 = 10, 10
kormeret = 40
abl1=Tk()
abl1.title('Animációs gyakorlat Tkinter-rel')

can1=Canvas(abl1,bg='#CD853F',height=400,width=400)
oval1=can1.create_oval(x1,y1,x1+kormeret,y1+kormeret,width=2,fill='green')

can1.pack(side=LEFT)
Button(abl1, text='Kilép',command=abl1.quit).pack(side=BOTTOM)
Button(abl1, text='Balra',command=mozdit_balra).pack()
Button(abl1, text='Jobbra',command=mozdit_jobbra).pack()
Button(abl1, text='Föl',command=mozdit_fel).pack()
Button(abl1, text='Le',command=mozdit_le).pack()
Button(abl1, text='Kör növel',command=kor_novel).pack()
Button(abl1, text='Kör csökkent',command=kor_csokken).pack()
Button(abl1, text='Piros kör',command=piros).pack()
Button(abl1, text='Kék kör',command=kek).pack()
Button(abl1, text='Zöld kör',command=zold).pack()
Button(abl1, text='Sárga kör',command=sarga).pack()
Button(abl1, text='Kék háttér',command=fekete_hatter).pack() 
Button(abl1, text='Zöld háttér',command=zold_hatter).pack() 
Button(abl1, text='Levendula háttér',command=levendula_hatter).pack() 

abl1.mainloop()

