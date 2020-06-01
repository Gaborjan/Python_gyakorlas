#Az interpretált nyelveknek mindig vannak olyan függvényei, amelyek lehetővé teszikk egy sztringnek a nyelv utasítássoraként való kiértékelését. 
#Az alábbi pogram erre példa. Az eval függvény használata. 

from tkinter import *
from math import *

#Annak az akciónak a definíciója amit akkor kell végrehajtani, ha a felhasználó az adatbeviteli mező szerkesztése 
#után Entert-t nyom.
def kiertekel(event):
    sor.configure(text="Eredmény = "+str(eval(mezo.get())))
    
#FŐPROGRAM

ablak=Tk()
mezo=Entry(ablak)
mezo.bind("<Return>", kiertekel)
mezo.pack()
sor=Label(ablak)
sor.pack()

ablak.mainloop()