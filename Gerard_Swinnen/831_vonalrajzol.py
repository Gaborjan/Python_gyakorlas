from tkinter import *
from random import randrange
import time
from turtledemo.lindenmayer import draw

# Azeseménykezelő függvények definíciója

MAX_ROW=800
MAX_COLUMN=800

def drawline():
    "Vonal rajzolása a can1 canvascra "
    global x1,y1,x2,y2, color
         
    #A koordináták módosítása a következő egyenes számára
    x1=randrange(MAX_COLUMN+1)
    y1=randrange(MAX_ROW+1)
    x2=randrange(MAX_COLUMN+1)
    y2=randrange(MAX_ROW+1)
    
    #Címkék aktualizálása
    label1.configure(text="x1: "+"{0:03d}".format(x1))
    label2.configure(text="y1: "+"{0:03d}".format(y1))
    label3.configure(text="x2: "+"{0:03d}".format(x2))
    label4.configure(text="y2: "+"{0:03d}".format(y2))
    
    #can1.create_line(x2,y2,x1,y1,width=2,fill=color) # x1 oszlop, y1 sor és x2 oszlop y2 sor közé
    can1.create_rectangle(x2,y2,x1,y1,width=2,fill=color)
    
def changecolor():
    "A rajz színének véletlenszerű megváltoztatása"
    global color
    pal=['white','cyan','cadetblue','green','lightgreen','blue','turquoise','skyblue',
         'palegreen','paleturquoise','navy','powderblue','greenyellow','lavender',
         'olivedrab','darkcyan','springgreen','aqua']
    c=randrange(18) #Véletlen szám 0 és 7 között.
    color=pal[c]

def lineandcolor():
    changecolor()
    drawline()

def lineandcolor10():
    for x in range(10):
        changecolor()
        drawline()
    
def lineandcolor100():
    for x in range(10):
        lineandcolor10()

def canvasdelete():
    can1.delete("all")

#Főprogram

#A következő változókat globális változókként használjuk:
x1,y1,x2,y2 = 0,0,0,0     #Az egyenes koordinátái
color='dark green'              #Az egyenes színe

#A fő-widget létrehozása ("master"):

abl1=Tk()
#A "slave" widgetek létrehozása:
can1=Canvas(abl1,bg='dark gray',height=MAX_ROW,width=MAX_COLUMN)
can1.pack(side=LEFT)
gomb1=Button(abl1, text='Kilép',command=abl1.quit)
gomb1.pack(side=BOTTOM)
gomb2=Button(abl1,text='Vonalat rajzol',command=drawline)
gomb2.pack()
gomb3=Button(abl1,text='Más szín',command=changecolor)
gomb3.pack()
gomb4=Button(abl1,text='Vonal és szín',command=lineandcolor)
gomb4.pack()
gomb5=Button(abl1,text='10 vonal&szín',command=lineandcolor10)
gomb5.pack()
gomb6=Button(abl1,text='100 vonal&szín',command=lineandcolor100)
gomb6.pack()
gomb7=Button(abl1,text='Tábla törlés',command=canvasdelete)
gomb7.pack()

label1=Label(abl1, text="x1: "+str(x1))
label2=Label(abl1, text="y1: "+str(y1))
label3=Label(abl1, text="x2: "+str(x1))
label4=Label(abl1, text="y2: "+str(y2))
label1.pack()
label2.pack()
label3.pack()
label4.pack()
  
abl1.mainloop()     #Az eseményfogadó indítása
abl1.destroy()      #Az ablak zárása

