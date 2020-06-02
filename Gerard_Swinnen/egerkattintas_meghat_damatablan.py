from tkinter import *
from random import randrange

MAX_WIDTH=800
MAX_HEIGH=800
KOCKA_OLDAL=80                                   #A négyzet oldalának hossza
OSZLOP=int(MAX_WIDTH/KOCKA_OLDAL)                #Tábla oszlopainak száma
SOR=int(MAX_HEIGH/KOCKA_OLDAL)                   #Tábla sorainak száma
SZIN1="SpringGreen2"             #Tábla egyik színe
SZIN2="DeepSkyBlue3"            #Tábla másik színe
KORONG_SZIN="dark orange"     #korong színe

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
    global koord    #A korongok koorninátái
    koord.clear()
    global matrix_szin      #A mátrix egyes elemeinek színét mentjük el
    matrix_szin=[]
    for k in range(SOR):
        sor=[]      #Segédváltozó, ebbe gyűjtjük egy sornyi négyzet színeit
        for i in range(OSZLOP):
            #Páratlan sor? Ha igen, SZIN1-el kell indítani az oszlop színezést
            if ((k % 2) == 1):
                #Páratlan oszlop? Ha igen, SZIN1-el kell indítani az oszlop színezést
                if ((i % 2) == 1):
                    can.create_rectangle(i*KOCKA_OLDAL,k*KOCKA_OLDAL,(i*KOCKA_OLDAL)+KOCKA_OLDAL,(k*KOCKA_OLDAL)+KOCKA_OLDAL, fill=SZIN1, width=0)
                    sor.append([SZIN1])
                else:
                    can.create_rectangle(i*KOCKA_OLDAL,k*KOCKA_OLDAL,(i*KOCKA_OLDAL)+KOCKA_OLDAL,(k*KOCKA_OLDAL)+KOCKA_OLDAL, fill=SZIN2, width=0)
                    sor.append([SZIN2])
            #Páros sor, ezért SZIN2-vel kell indítani az oszlop színezést
            else:
                #Páratlan oszlop? Ha igen, akkor SZIN2-vel kell indítani az oszlop színezést
                if ((i % 2) == 1):
                    can.create_rectangle(i*KOCKA_OLDAL,k*KOCKA_OLDAL,(i*KOCKA_OLDAL)+KOCKA_OLDAL,(k*KOCKA_OLDAL)+KOCKA_OLDAL, fill=SZIN2, width=0)
                    sor.append([SZIN2])
                else:
                    can.create_rectangle(i*KOCKA_OLDAL,k*KOCKA_OLDAL,(i*KOCKA_OLDAL)+KOCKA_OLDAL,(k*KOCKA_OLDAL)+KOCKA_OLDAL, fill=SZIN1, width=0)
                    sor.append([SZIN1])
        matrix_szin.append(sor)
    #Színek kiírása ha szükséges
    #for k in range(len(matrix_szin[0])):
    #    for i in range (len(matrix_szin[k])):
    #        print(matrix_szin[k][i], end =" ")       
    #    print("")
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
                circle(oszlop_poz,sor_poz,int((KOCKA_OLDAL/2))-2,KORONG_SZIN)   #Korong kirajzolása
                if (len(koord)<(OSZLOP*SOR)):
                    l1.configure(text="Szabad helyek száma a táblán: "+str(OSZLOP*SOR-len(koord))) 
                else:
                    l1.configure(text="A táblán nincs több szabad hely!")
                    b2.config(state=DISABLED)
 

def korong_manual(event):
    "Abba a tábla pozcicíóra tesz egy korongot, ahová a felhasználó kattin az egér bal gombjával"
    global koord
    global matrix_szin
    l2.configure(text="Egér kattintás koordinátái: X= "+str(event.x)+ " Y= "+str(event.y))
    s=int(event.y/KOCKA_OLDAL)      #Kattintás koordinátájának tábla sorára konvertálása
    o=int(event.x/KOCKA_OLDAL)      #Kattintás koordinátájának tábla oszlopára konvertálása
    oszlop_poz=(o*KOCKA_OLDAL)+int(KOCKA_OLDAL/2)  #Tábla oszlop transzformációja Canvas koordinátákra, a négyzet közepe kb, ahol a kör origója lesz
    sor_poz=(s*KOCKA_OLDAL)+int(KOCKA_OLDAL/2)     #Tábla sor transzformációja Canvas koordinátákra, , a négyzet közepe kb, ahol a kör origója lesz
    poz=list([o,s])         #Segédváltozó
    if poz not in koord:    #Ha ezen a helyen még nincs korong
        circle(oszlop_poz,sor_poz,int((KOCKA_OLDAL/2))-2,KORONG_SZIN)   #Korong kirajzolása
        koord.append(poz)   #Korong poziciójának mentése
    else: #Ha ezen a helyen már van korong
        circle(oszlop_poz,sor_poz,int((KOCKA_OLDAL/2))-2,matrix_szin[s][o]) #Korongot rajzolunk, de a megfelelő négyzet színnel, így a kör "eltünik"
        koord.remove(poz)   #Az aktuális helyet kivesszük a foglalt korong koornináták listájából
    #A szabad helyek aktualizálása a kijelzőn, korong gomb elérhetőségének aktualizálása
    if (len(koord)<(OSZLOP*SOR)):
        l1.configure(text="Szabad helyek száma a táblán: "+str(OSZLOP*SOR-len(koord)))
        b2.config(state=NORMAL) 
    else:
        l1.configure(text="A táblán nincs több szabad hely!")
        b2.config(state=DISABLED)
### FŐPROGRAM ###

koord=list()        #korongok koordinátáit tárolós lista (a métrix sor és oszlopa, nem canvas hely)
matrix_szin=list()        #A mátrix egyes elemeinek színét mentjük el

window=Tk()
can=Canvas(window, width=KOCKA_OLDAL*OSZLOP, height=KOCKA_OLDAL*SOR, bg='ivory')
can.pack(side=TOP)
can.bind('<Button-1>',korong_manual)
b1=Button(window,text="Új tábla", command=dama_tabla)
b1.pack(side=LEFT, padx=3, pady=3)
b2=Button(window,text="Korong véletlen helyre", command=korong,state=DISABLED)
b2.pack(side=RIGHT, padx=3, pady=3)
l1=Label(window, text="Szabad helyek száma a táblán: "+str(OSZLOP*SOR-len(koord)),padx=3, pady=3)
l1.pack()
l2=Label(window, text="Egér kattintás koordinátái:", padx=3, pady=3)
l2.pack()
dama_tabla()
window.mainloop()

