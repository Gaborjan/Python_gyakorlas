from tkinter import *
from tkinter import colorchooser
from random import randrange
#from numpy.core.defchararray import title
from test import test_sort

MAX_WIDTH=800
MAX_HEIGH=800
KOCKA_OLDAL=40                                   #A négyzet oldalának hossza
OSZLOP=int(MAX_WIDTH/KOCKA_OLDAL)                #Tábla oszlopainak száma
SOR=int(MAX_HEIGH/KOCKA_OLDAL)                   #Tábla sorainak száma
SZIN1="#0080ff"             #Tábla egyik színe (kezdőérték)
SZIN2="#00bb2f"             #Tábla másik színe (kezdőérték)
KORONG_SZIN="#ff8000"       #korong aktuális színe (kezdőérték)
frissit_flag=False          #Azt mutatja a táblázat színeit frissíteni kell-e? Ha hamis, akkor teljes törlés, ha igaz, csak frissítés

def circle(x,y,r,color='black'):
    " 'r' sugarú (x,y) középpontú kör rajzolása 'color' színnel"
    can.create_oval(x-r, y-r, x+r, y+r, outline=color, fill=color)

def dama_tabla():
    "Dámatáblát rajzol"
    #Előszőr a meglévő rajz törlése
    can.delete(ALL)
    
    global koord            #A korongok koorninátái (oszlop, sor!!!)
    global matrix_szin      #A mátrix egyes elemeinek színét mentjük el, illetve az adott helyen lévő korong színét is
    global frissit_flag     
    #Azt mutatja a táblázat színeit frissíteni kell-e? Ha hamis, akkor teljes törlés, ha igaz, csak frissítés. Frissítés esetén is újrarajzoljuk
    #a mátrixot az új színnel! De a meglévő korongok színinfóit megőrizzük, hogy újra tudjuk rajzolni azokat is.
    
    #Előszőr a meglévő rajz törlése
    can.delete(ALL)
    
    if not frissit_flag:    #Ha nem frissítés, hanem teljesen új tábla, minden infót törlünk.
        koord.clear()
        matrix_szin=[]
        
    for k in range(SOR):
        sor=[]      #Segédváltozó, ebbe gyűjtjük egy sornyi négyzet színeit
        for i in range(OSZLOP):
            poz_szin=[]     #Adott pozíció színei
            #Páratlan sor? Ha igen, SZIN1-el kell indítani az oszlop színezést
            if ((k % 2) == 1):
                #Páratlan oszlop? Ha igen, SZIN1-el kell indítani az oszlop színezést
                if ((i % 2) == 1):
                    can.create_rectangle(i*KOCKA_OLDAL,k*KOCKA_OLDAL,(i*KOCKA_OLDAL)+KOCKA_OLDAL,(k*KOCKA_OLDAL)+KOCKA_OLDAL, fill=SZIN1, width=0)
                    if not frissit_flag:                    #Ha nem frissítés, akkor a matrix szin mappa építése, az adotzz poz. színének mentése
                        poz_szin.append([k,i,SZIN1])
                    else:                                   #Ha frissítés, akkor csak a szín értéket ceréljük a pozicíón
                        matrix_szin[k][i][0][2]=SZIN1
                else:   #Páros oszlop, SZIN2-vel indulunk
                    can.create_rectangle(i*KOCKA_OLDAL,k*KOCKA_OLDAL,(i*KOCKA_OLDAL)+KOCKA_OLDAL,(k*KOCKA_OLDAL)+KOCKA_OLDAL, fill=SZIN2, width=0)
                    if not frissit_flag:                    #Ha nem frissítés, akkor a matrix szin mappa építése, az adotzz poz. színének mentése
                        poz_szin.append([k,i,SZIN2])
                    else:                                   #Ha frissítés, akkor csak a szín értéket ceréljük a pozicíón
                        matrix_szin[k][i][0][2]=SZIN2
            #Páros sor, ezért SZIN2-vel kell indítani az oszlop színezést
            else:
                #Páratlan oszlop? Ha igen, akkor SZIN2-vel kell indítani az oszlop színezést
                if ((i % 2) == 1):
                    can.create_rectangle(i*KOCKA_OLDAL,k*KOCKA_OLDAL,(i*KOCKA_OLDAL)+KOCKA_OLDAL,(k*KOCKA_OLDAL)+KOCKA_OLDAL, fill=SZIN2, width=0)
                    if not frissit_flag:                    #Ha nem frissítés, akkor a matrix szin mappa építése, az adotzz poz. színének mentése
                        poz_szin.append([k,i,SZIN2])
                    else:                                   #Ha frissítés, akkor csak a szín értéket ceréljük a pozicíón
                        matrix_szin[k][i][0][2]=SZIN2
                else:
                    can.create_rectangle(i*KOCKA_OLDAL,k*KOCKA_OLDAL,(i*KOCKA_OLDAL)+KOCKA_OLDAL,(k*KOCKA_OLDAL)+KOCKA_OLDAL, fill=SZIN1, width=0)
                    if not frissit_flag:                    #Ha nem frissítés, akkor a matrix szin mappa építése, az adotzz poz. színének mentése
                        poz_szin.append([k,i,SZIN1])
                    else:                                   #Ha frissítés, akkor csak a szín értéket ceréljük a pozicíón
                        matrix_szin[k][i][0][2]=SZIN1
            if not frissit_flag:                            #Ha nem frissítés, akkor a rácsponton nincs korong, a színét None-ra állítjuk
                poz_szin.append([None])
            if not frissit_flag:                            #Ha nem frissítés, akkor a sor infóhoz hozzáadjuk az aktuális pozicíció infót
                sor.append(poz_szin)
        if not frissit_flag:                                #Ha nem frissítés, akkor a mátrixhoz hozzáadjuk a belső ciklusban épített sort
            matrix_szin.append(sor)
        #belső ciklus vége
    #külső ciklus vége
    
    #print("MÁTRIX")
    #print(matrix_szin)  
    #print("Bal felső kocka színe:", matrix_szin[k][i][0][2])  
    if not frissit_flag:                                  #Ha nem frissítés, a véletlen gomb engedélyezése, szabad helyek max-ra állítása
        b2.config(state=NORMAL)
        l1.configure(text="Szabad helyek száma a táblán: "+str(OSZLOP*SOR-len(koord)))
#dama_tabla vége

    
def korong():              
    "Korongokat tesz a táblára véletlenszerűen"
    global koord            #A korongok koorninátái (oszlop, sor!!!)
    global KORONG_SZIN      #Korong aktuális színe
    global matrix_szin      #A mátrix egyes elemeinek színei illetve az adott helyen lévő korong színe
    
    if (str(b2['state'])!='DISABLED'):      #Még van szabad hely
        for i in (range(100)):            #Későbbre fenntartva, sok korong egyszerre 
            k_oszlop=randrange(OSZLOP)      #Melyik oszlopba legyen a korong? (véletlenszerű)
            k_sor=randrange(SOR)            #Melyik sorba legyen a korong?    (véletlenszerű)
            s=list([k_oszlop,k_sor])        #Segédváltozó, poz. tárolásra
            
            #Ebben a ciklusban vizsgáljuk meg, hogy az aktuálisan generált koordinátában van-e már korong,
            #és ha van, akkor új koordinátát generálunk. Ha már minden helyen van korong, akkor nem lépünk
            #be a ciklusba.
            while (s in koord) and (len(koord)<SOR*OSZLOP): 
                k_oszlop=randrange(OSZLOP)
                k_sor=randrange(SOR)
                s=list([k_oszlop,k_sor])
                
            if (len(koord)<SOR*OSZLOP):     #Még van üres hely a táblán
                koord.append(s)             #Koordináták mentése
                matrix_szin[k_sor][k_oszlop][1][0]=KORONG_SZIN                      #A mátrix-ba mentjük milyen színű korong kerül a pozicíóba?
                oszlop_poz=(k_oszlop*KOCKA_OLDAL)+int(KOCKA_OLDAL/2)                #Tábla oszlop transzformációja Canvas koordinátákra
                sor_poz=(k_sor*KOCKA_OLDAL)+int(KOCKA_OLDAL/2)                      #Tábla sor transzformációja Canvas koordinátákra
                circle(oszlop_poz,sor_poz,int((KOCKA_OLDAL/2))-2,KORONG_SZIN)       #Korong kirajzolása
                #Szabad helyek aktualizálása
                if (len(koord)<(OSZLOP*SOR)):
                    l1.configure(text="Szabad helyek száma a táblán: "+str(OSZLOP*SOR-len(koord))) 
                else:
                    l1.configure(text="A táblán nincs több szabad hely!")
                    b2.config(state=DISABLED)
#korong vége    

def korong_manual(event):
    "Abba a tábla pozcicíóra tesz egy korongot, ahová a felhasználó kattint az egér bal gombjával"
    global koord            #A korongok koorninátái (oszlop, sor!!!)
    global matrix_szin      #A mátrix egyes elemeinek színei illetve az adott helyen lévő korong színe
    global KORONG_SZIN      #Korong aktuális színe
    
    l2.configure(text="Egér kattintás koordinátái: X= "+str(event.x)+ " Y= "+str(event.y))
    s=int(event.y/KOCKA_OLDAL)      #Kattintás koordinátájának tábla sorára konvertálása
    o=int(event.x/KOCKA_OLDAL)      #Kattintás koordinátájának tábla oszlopára konvertálása
    oszlop_poz=(o*KOCKA_OLDAL)+int(KOCKA_OLDAL/2)  #Tábla oszlop transzformációja Canvas koordinátákra, a négyzet közepe kb, ahol a kör origója lesz
    sor_poz=(s*KOCKA_OLDAL)+int(KOCKA_OLDAL/2)     #Tábla sor transzformációja Canvas koordinátákra, , a négyzet közepe kb, ahol a kör origója lesz
    poz=list([o,s])         #Segédváltozó, koordináták mentéséhez
    if poz not in koord:    #Ha ezen a helyen még nincs korong
        circle(oszlop_poz,sor_poz,int((KOCKA_OLDAL/2))-2,KORONG_SZIN)   #Korong kirajzolása
        koord.append(poz)                                               #Korong poziciójának mentése
        matrix_szin[s][o][1][0]=KORONG_SZIN                             #Elmentjük milyen színű korong van itt
    else: #Ha ezen a helyen már van korong
        circle(oszlop_poz,sor_poz,int((KOCKA_OLDAL/2))-2,matrix_szin[s] [o] [0] [2])    #Korongot rajzolunk, de a megfelelő négyzet színnel, így a kör "eltünik"
        matrix_szin[s][o][1][0]=None                                    #Itt nincs korong, tehát a szín None
        koord.remove(poz)                                               #Az aktuális helyet kivesszük a foglalt korong koornináták listájából
    #A szabad helyek aktualizálása a kijelzőn, korong gomb elérhetőségének aktualizálása
    if (len(koord)<(OSZLOP*SOR)):
        l1.configure(text="Szabad helyek száma a táblán: "+str(OSZLOP*SOR-len(koord)))
        b2.config(state=NORMAL) 
    else:
        l1.configure(text="A táblán nincs több szabad hely!")
        b2.config(state=DISABLED)
    
#korong_manual vége


def szin1_allit():
    "Mátrix háttérszínének állítása"
    global SZIN1
    
    color=colorchooser.askcolor(parent=can, color=SZIN1, title="Négyzet színe (bal felső sarokba kerülő)")
    if (color[1] is not None):
        SZIN1=color[1]
    b3.configure(bg=color[1])   #Gomb színét is állítjuk a választott színre

#szin1_allit vége

def szin2_allit():
    "Mátrix háttérszínének állítása"
    global SZIN2
    color=colorchooser.askcolor(parent=can, color=SZIN2, title="Négyzet színe (bal felső sarok melleti első jobbra)")
    if (color[1] is not None):
        SZIN2=color[1]
    b4.configure(bg=color[1])   #Gomb színét is állítjuk a választott színre
    
#szin2_allit vége

def korong_szin_allit():
    "A korong színének állítása"
    
    global KORONG_SZIN
    
    color=colorchooser.askcolor(parent=can, color=KORONG_SZIN, title="Korong színének beállítása")
    if (color[1] is not None):
        KORONG_SZIN=color[1]
    b6.configure(bg=color[1])
    
#korong_szin_allit vége


def tabla_frissit():
    "A tábla frissítés gomb megnyomásakor elvégzendő utasítások"
    
    global koord            #A korongok koorninátái (oszlop, sor!!!)
    global frissit_flag     #A dama_tabla függvény használja, teljesen töröljük a táblát (=false), vagy csak színfrissítés (=True)
    global matrix_szin      #A mátrix egyes elemeinek színei illetve az adott helyen lévő korong színe

    frissit_flag=True       #Frissítés
    dama_tabla()            #Tábla újra rajzolása színek frissítése
    frissit_flag=False      #Flag alaphelyeztbe állítása
    
    #A ciklus rajzolja meg a szín-frissített táblára a korongokat, olyan színnel, amilyennel meg lettek rajzolva 
    for i  in range(len(koord)):
        oszlop_poz=(koord[i][0]*KOCKA_OLDAL)+int(KOCKA_OLDAL/2)         #Tábla oszlop transzformációja Canvas koordinátákra
        sor_poz=(koord[i][1]*KOCKA_OLDAL)+int(KOCKA_OLDAL/2)            #Tábla sor transzformációja Canvas koordinátákra
        #Korong kirajzolása, színt a mátrixból vesszük, első index: koordináta sora, 2. ind.: koordináta oszlop, 3. ind.: korong színt tároló lista, 4. 
        #index: 0. eleme = a korong színét érjük el.
        circle(oszlop_poz,sor_poz,int((KOCKA_OLDAL/2))-2,matrix_szin[koord[i][1]] [koord[i][0]] [1] [0])   
        #A szabad helyek aktualizálása a kijelzőn, korong gomb elérhetőségének aktualizálása
        if (len(koord)<(OSZLOP*SOR)):
            l1.configure(text="Szabad helyek száma a táblán: "+str(OSZLOP*SOR-len(koord))) 
        else:
            l1.configure(text="A táblán nincs több szabad hely!")
            b2.config(state=DISABLED)

#tabla_frissit vége

### FŐPROGRAM ###

koord=list()                #korongok koordinátáit és színeit tároló lista (a métrix sor és oszlopa, nem canvas hely)
matrix_szin=list()          #A mátrix egyes elemeinek színét tárolja (négyzetek és korong)

window=Tk()
window.title("Dámatábla rajzoló program")

can=Canvas(window, width=KOCKA_OLDAL*OSZLOP, height=KOCKA_OLDAL*SOR, bg='ivory')
can.pack(side=TOP)
can.bind('<Button-1>',korong_manual)

b1=Button(window,text="Tábla törlése", command=dama_tabla).pack(side=LEFT, padx=3, pady=3)

b2=Button(window,text="Korong véletlen helyre", command=korong,state=DISABLED)
b2.pack(side=RIGHT, padx=3, pady=3)

b3=Button(window,text="Négyzet szín 1.", command=szin1_allit, bg=SZIN1)
b3.pack(side=LEFT, padx=3, pady=3)

b4=Button(window,text="Négyzet szín 2.", command=szin2_allit, bg=SZIN2)
b4.pack(side=LEFT, padx=3, pady=3)

b5=Button(window,text="Tábla frissít", command=tabla_frissit).pack(side=LEFT, padx=3, pady=3)

b6=Button(window,text="Korong szín", command=korong_szin_allit, bg=KORONG_SZIN)
b6.pack(side=LEFT, padx=3, pady=3)

l1=Label(window, text="Szabad helyek száma a táblán: "+str(OSZLOP*SOR-len(koord)),padx=3, pady=3)
l1.pack()
l2=Label(window, text="Egér kattintás koordinátái:", padx=3, pady=3)
l2.pack()

dama_tabla()
window.mainloop()

#FŐPROGRAM VÉGE

