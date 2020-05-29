from tkinter import *
from random import randrange

KOCKA_OLDAL=40
M_WIDTH=600
M_HEIGH=600
OSZLOP=10
SOR=10
SZIN1="red"
SZIN2="blue"
KORONG_SZIN="green"

def circle(x,y,r,color='black'):
    "r sugarú (x,y) középpontú kör rajzolása"
    can.create_oval(x-r, y-r, x+r, y+r, outline=color, fill=color)

def dama_tabla():
    "Dámatáblát rajzol"
    #Előszőr a meglévő rajz törlése
    can.delete(ALL)
    global koord
    koord.clear()
    #A két egyenes rajzolása (függ és vissz.)
     
    sor_tolas=0
    for k in range(int(SOR/2)):
        oszlop_tolas=1
        for i in range(int(OSZLOP/2)):
            can.create_rectangle((oszlop_tolas*KOCKA_OLDAL)+1,(sor_tolas*KOCKA_OLDAL)+1,(i*(KOCKA_OLDAL*2))+1,((sor_tolas*KOCKA_OLDAL)+KOCKA_OLDAL)+1,
                                 fill=SZIN1,width=0)
            oszlop_tolas=oszlop_tolas+2
        sor_tolas=sor_tolas+2
        
    sor_tolas=1
    for k in range(int(SOR/2)):
        oszlop_tolas=1
        for i in range(int(OSZLOP/2)):
            can.create_rectangle(((oszlop_tolas*KOCKA_OLDAL)+KOCKA_OLDAL)+1,(sor_tolas*KOCKA_OLDAL)+1,((i*(KOCKA_OLDAL*2))+KOCKA_OLDAL)+1,
                                 ((sor_tolas*KOCKA_OLDAL)+KOCKA_OLDAL)+1,fill=SZIN1,width=0)
            oszlop_tolas=oszlop_tolas+2
        #print(k)
        sor_tolas=sor_tolas+2       

    sor_tolas=1
    for k in range(int(SOR/2)):
        oszlop_tolas=1
        for i in range(int(OSZLOP/2)):
            can.create_rectangle((oszlop_tolas*KOCKA_OLDAL)+1,(sor_tolas*KOCKA_OLDAL)+1,(i*(KOCKA_OLDAL*2))+1,((sor_tolas*KOCKA_OLDAL)+KOCKA_OLDAL)+1,
                                 fill=SZIN2,width=0)
            oszlop_tolas=oszlop_tolas+2
        sor_tolas=sor_tolas+2
        
    sor_tolas=0
    for k in range(int(SOR/2)):
        oszlop_tolas=1
        for i in range(int(OSZLOP/2)):
            can.create_rectangle(((oszlop_tolas*KOCKA_OLDAL)+KOCKA_OLDAL)+1,(sor_tolas*KOCKA_OLDAL)+1,((i*(KOCKA_OLDAL*2))+KOCKA_OLDAL)+1,
                                 ((sor_tolas*KOCKA_OLDAL)+KOCKA_OLDAL)+1,fill=SZIN2,width=0)
            oszlop_tolas=oszlop_tolas+2
        #print(k)
        sor_tolas=sor_tolas+2 

def korong():
    "Korongokat tesz a táblára"
    global koord
    oszlop=randrange(OSZLOP)
    sor=randrange(SOR)
    s=list([oszlop,sor])
    while (s in koord) and (len(koord)<SOR*OSZLOP):
        oszlop=randrange(OSZLOP)
        sor=randrange(SOR)
        s=list([oszlop,sor])
        print("ÚJ")
    if (len(koord)<SOR*OSZLOP):
        koord.append(s)
        print(koord)
        oszlop_poz=(oszlop*KOCKA_OLDAL)+int(KOCKA_OLDAL/2)
        sor_poz=(sor*KOCKA_OLDAL)+int(KOCKA_OLDAL/2)
        circle(oszlop_poz,sor_poz,int((KOCKA_OLDAL/2))-3,KORONG_SZIN)
    else:
        print("Tele a tábla!")
### FŐPROGRAM ###
koord=list()

window=Tk()
can=Canvas(window, width=M_WIDTH, height=M_HEIGH, bg='ivory')
can.pack(side=TOP)
b1=Button(window,text="Dámatábla", command=dama_tabla)
b1.pack(side=LEFT, padx=3, pady=3)
b2=Button(window,text="Korongok", command=korong)
b2.pack(side=RIGHT, padx=3, pady=3)
window.mainloop()