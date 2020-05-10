import msvcrt
import time
from prompt_toolkit.keys import KEY_ALIASES
import sys

HIBA_UZ_MINTA='*'
TAJ_UZ_MINTA='-'

def egyszeruMenu(menuNev="", Menupont=list()) :
    db=len(Menupont)
    valasz=0;
    menuNev=menuNev.upper()
    seged=""
    for i in range(len(menuNev)) : 
        seged=seged+menuNev[i]+" "
    while (valasz<1 or valasz>db):
        print()
        print("----< "+seged+" >----")
        print()
        for i in range(db):
            print(Menupont[i])
        print()
        valasz=int(input("Válassz: "))
    return valasz 

def egesz_Beolvas(uzenet="", min_szam=None, max_szam=None, hibaUzenet=""):
    seged=""
    seged_int=None
    while (seged_int is None) or (seged_int<min_szam) or (seged_int>max_szam) :
        seged=input(uzenet)
        try:
            seged_int=int(seged)
            if (seged_int<min_szam or seged_int>max_szam) and (len(hibaUzenet)!=0):
                print(hibaUzenet)
        except:
            print("Nem egész szám, próbálja újra!")
    return seged_int


def hibaUzenet(uzenet_szoveg="", enter=None) :
    uzenet(uzenet_szoveg,enter,HIBA_UZ_MINTA)

def tajUzenet(uzenet_szoveg="",enter=None) :
    uzenet(uzenet_szoveg,enter,TAJ_UZ_MINTA)
    
def uzenet(uzenet_szoveg="", enter=None, minta='') :
    print()
    for i in range (len(uzenet_szoveg)):
        print(minta, end ="")
    print()
    print(uzenet_szoveg)
    print()
    for i in range (len(uzenet_szoveg)):
        print(minta, end ="")
    print()
    print()
    if (enter):
        print("Folytatáshoz nyomja meg az Enter gombot...")
        ch = sys.stdin.readline()


def karakter_Beolvas():
    while (True):
        try:
            ch=sys.stdin.readline()
        except IndexError:
            print("Nem karakter! Próbálja újra!") 
        if len(ch)!=2:
           print("Nem karakter! Próbálja újra!")
        else:
            return ch        
#print("Választott menüpont:",egyszeruMenu("fömenü",["1. Beolvasás","2. Kiírás","3. Program vége"]))
#print("A megadott szám:",egesz_Beolvas("Adj meg egy számot -100 és 100 között: ", -100, 100, "Érvénytelen érték!"))    
#hibaUzenet("Ezt elbasztad!!! :( ", False)
hibaUzenet("Üzenet", True)
print("Adjon megy egy karaktert:")
print(karakter_Beolvas())


        
        

