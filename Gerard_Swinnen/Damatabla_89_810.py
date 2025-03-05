from tkinter import *
from random import randrange

MAX_WIDTH=800
MAX_HEIGH=800
KOCKA_OLDAL=80                      #A négyzet oldalának hossza
OSZLOP=int(MAX_WIDTH/KOCKA_OLDAL)                #Tábla oszlopainak száma
SOR=int(MAX_HEIGH/KOCKA_OLDAL)                   #Tábla sorainak száma
SZIN1="red"             #Tábla egyik színe
SZIN2="blue"            #Tábla másik színe
KORONG_SZIN="yellow"     #korong színe

def circle(x,y,r,color='black'):
    "r sugarú (x,y) középpontú kör rajzolása"
    can.create_oval(x-r, y-r, x+r, y+r, outline=color, fill=color)

def dama_tabla():
    "Dámatáblát rajzol"
    #Az algoritmus sokkal egyszerűbb is lehetne, ha soronként felváltva rajzoljuk meg az eltérő színű négyzeteket.
    #Azért lett bonyolult, mert az eredeti feladatban nem két színű táblát kellett rajzolni, hanem a csak egyszínű
    #négyzetrácsot úgy, hogy a nem színezett kockák a canvas színűek, vagyis mindig a négyzet oldalának hosszával
    #lépegetni kellett jobbra és ehhez igazítani a rectangle-nek adott koordinátákat.
    #Előszőr a meglévő rajz törlése
    can.delete(ALL)
    global koord
    koord.clear()
     
    for k in range(SOR):
        for i in range(OSZLOP):
            #Páratlan sor? Ha igen, SZIN1-el kell indítani az oszlop színezést
            if ((k % 2) == 1):
                #Páratlan oszlop? Ha igen, SZIN1-el kell indítani az oszlop színezést
                if ((i % 2) == 1):
                    can.create_rectangle(i*KOCKA_OLDAL,k*KOCKA_OLDAL,(i*KOCKA_OLDAL)+KOCKA_OLDAL,(k*KOCKA_OLDAL)+KOCKA_OLDAL, fill=SZIN1, width=0)
                else:
                    can.create_rectangle(i*KOCKA_OLDAL,k*KOCKA_OLDAL,(i*KOCKA_OLDAL)+KOCKA_OLDAL,(k*KOCKA_OLDAL)+KOCKA_OLDAL, fill=SZIN2, width=0)
            #Páros sor, ezért SZIN2-vel kell indítani az oszlop színezést
            else:
                #Páratlan oszlop? Ha igen, akkor SZIN2-vel kell indítani az oszlop színezést
                if ((i % 2) == 1):
                    can.create_rectangle(i*KOCKA_OLDAL,k*KOCKA_OLDAL,(i*KOCKA_OLDAL)+KOCKA_OLDAL,(k*KOCKA_OLDAL)+KOCKA_OLDAL, fill=SZIN2, width=0)
                else:
                    can.create_rectangle(i*KOCKA_OLDAL,k*KOCKA_OLDAL,(i*KOCKA_OLDAL)+KOCKA_OLDAL,(k*KOCKA_OLDAL)+KOCKA_OLDAL, fill=SZIN1, width=0)
    
    #EREDETI ALGORITMUS
    #Tele négyzettel (ha fekete/fehér lenne) kezdünk rajzolni, a páratlan sorokat"   
    '''sor_tolas=0
    for k in range(int(SOR/2)):
        oszlop_tolas=1
        for i in range(int(OSZLOP/2)):
            can.create_rectangle((oszlop_tolas*KOCKA_OLDAL)+1,(sor_tolas*KOCKA_OLDAL)+1,(i*(KOCKA_OLDAL*2))+1,((sor_tolas*KOCKA_OLDAL)+KOCKA_OLDAL)+1,
                                 fill=SZIN1,width=0)
            oszlop_tolas=oszlop_tolas+2
        sor_tolas=sor_tolas+2
    #Üres négyzettel indulunk (ha fekete/fehér lenne), ezek a páros sorok    
    sor_tolas=1
    for k in range(int(SOR/2)):
        oszlop_tolas=1
        for i in range(int(OSZLOP/2)):
            can.create_rectangle(((oszlop_tolas*KOCKA_OLDAL)+KOCKA_OLDAL)+1,(sor_tolas*KOCKA_OLDAL)+1,((i*(KOCKA_OLDAL*2))+KOCKA_OLDAL)+1,
                                 ((sor_tolas*KOCKA_OLDAL)+KOCKA_OLDAL)+1,fill=SZIN1,width=0)
            oszlop_tolas=oszlop_tolas+2
        #print(k)
        sor_tolas=sor_tolas+2       
    
    #Az előző ciklusban rajzolt sor üresen maradt négyzeteit rajzoljuk meg, vagyiks a páros sorokat. 
    sor_tolas=1
    for k in range(int(SOR/2)):
        oszlop_tolas=1
        for i in range(int(OSZLOP/2)):
            can.create_rectangle((oszlop_tolas*KOCKA_OLDAL)+1,(sor_tolas*KOCKA_OLDAL)+1,(i*(KOCKA_OLDAL*2))+1,((sor_tolas*KOCKA_OLDAL)+KOCKA_OLDAL)+1,
                                 fill=SZIN2,width=0)
            oszlop_tolas=oszlop_tolas+2
        sor_tolas=sor_tolas+2
    #Az első ciklusban rajzolt sor üresen maradt négyzeteit rajzoljuk meg, ezek a páratlan sorok    
    sor_tolas=0
    for k in range(int(SOR/2)):
        oszlop_tolas=1
        for i in range(int(OSZLOP/2)):
            can.create_rectangle(((oszlop_tolas*KOCKA_OLDAL)+KOCKA_OLDAL)+1,(sor_tolas*KOCKA_OLDAL)+1,((i*(KOCKA_OLDAL*2))+KOCKA_OLDAL)+1,
                                 ((sor_tolas*KOCKA_OLDAL)+KOCKA_OLDAL)+1,fill=SZIN2,width=0)
            oszlop_tolas=oszlop_tolas+2
        #print(k)
        sor_tolas=sor_tolas+2'''
                    
    b2.config(state=NORMAL)
    l1.configure(text="Szabad helyek száma a táblán: "+str(OSZLOP*SOR-len(koord)))
    
def korong():
    "Korongokat tesz a táblára"
    global koord #A korongok koorninátái
    if (str(b2['state'])!='DISABLED'):
        #for i in (range(1000)):
            oszlop=randrange(OSZLOP)    #Melyik oszlopba legyen a korong?
            sor=randrange(SOR)          #Melyik sorba legyen a korong?
            s=list([oszlop,sor])        #Segédváltozó
            #Ebben a ciklusban vizsgáljuk meg, hogy az aktuálisan generált koordinátában van-e már korong,
            #és ha van, akkor új koordinátát generálunk. Ha már minden helyen van korong, akkor nem lépünk
            #be a ciklusba.
            while (s in koord) and (len(koord)<SOR*OSZLOP): 
                oszlop=randrange(OSZLOP)
                sor=randrange(SOR)
                s=list([oszlop,sor])
                #print("ÚJ")
            if (len(koord)<SOR*OSZLOP): #Még van üres hely a táblán
                koord.append(s)
                #print(koord)
                oszlop_poz=(oszlop*KOCKA_OLDAL)+int(KOCKA_OLDAL/2)              #Tábla oszlop transzformációja Canvas koordinátákra
                sor_poz=(sor*KOCKA_OLDAL)+int(KOCKA_OLDAL/2)                    #Tábla sor transzformációja Canvas koordinátákra
                circle(oszlop_poz,sor_poz,int((KOCKA_OLDAL/2))-3,KORONG_SZIN)   #Korong kirajzolása
                if (len(koord)<(OSZLOP*SOR)):
                    l1.configure(text="Szabad helyek száma a táblán: "+str(OSZLOP*SOR-len(koord))) 
                else:
                    l1.configure(text="A táblán nincs több szabad hely!")
                    b2.config(state=DISABLED)
 
### FŐPROGRAM ###

koord=list()        #korongok koordinátáit tárolós lista

window=Tk()
can=Canvas(window, width=KOCKA_OLDAL*OSZLOP, height=KOCKA_OLDAL*SOR, bg='ivory')
can.pack(side=TOP)
b1=Button(window,text="Dámatábla", command=dama_tabla)
b1.pack(side=LEFT, padx=3, pady=3)
b2=Button(window,text="Korongok", command=korong,state=DISABLED)
b2.pack(side=RIGHT, padx=3, pady=3)
l1=Label(window, text="Szabad helyek száma a táblán: "+str(OSZLOP*SOR-len(koord)),padx=3, pady=3)
l1.pack()
window.mainloop()
