from tkinter import *
from random import randrange
import numpy as np
import time
import gc

MAX_WIDTH=900
MAX_HEIGH=900
KOCKA_OLDAL=3                                   #A négyzet oldalának hossza
OSZLOP=100               #Tábla oszlopainak száma
#SOR=int(MAX_HEIGH/KOCKA_OLDAL)                   #Tábla sorainak száma
SOR=100
SZIN1="red"             #Tábla egyik színe
SZIN2="blue"            #Tábla másik színe
KORONG_SZIN="yellow"     #korong színe
global oldLifeBoard
#oldLifeBoard=[]
oldLifeBoard=np.zeros(shape=(SOR,OSZLOP))
global newLifeBoard
#newLifeBoard=[]
global gen
gen=0

newLifeBoard=np.zeros(shape=(SOR,OSZLOP))

def tabla():
    can.delete(ALL)
    for k in range(SOR):
        for i in range(OSZLOP):
            can.create_rectangle((i*KOCKA_OLDAL)-KOCKA_OLDAL,(k*KOCKA_OLDAL)-KOCKA_OLDAL,(i*KOCKA_OLDAL),(k*KOCKA_OLDAL), fill=SZIN1, width=0)
            
def tabla1(sor,oszlop,szin):
    can.create_rectangle((oszlop*KOCKA_OLDAL)-KOCKA_OLDAL,(sor*KOCKA_OLDAL)-KOCKA_OLDAL,oszlop*KOCKA_OLDAL,sor*KOCKA_OLDAL, fill=szin, width=0)

def  create_new_grid(current, new):
    for i in range(SOR):
        for j in range(OSZLOP): 
            '''neighbours = oldLifeBoard[i-1][j-1]+oldLifeBoard[i][j-1]
            neighbours = neighbours + oldLifeBoard[i+1][j-1]
            neighbours = neighbours + oldLifeBoard[i-1][j] + oldLifeBoard[i+1][j]
            neighbours = neighbours + oldLifeBoard[i-1][j+1]
            neighbours = neighbours + oldLifeBoard[i][j+1]+oldLifeBoard[i+1][j+1]'''
            neighbours = 0
            for l in range(-1, 2):
                for m in range(-1, 2):
                # Make sure to count the center cell located at grid[row][col]
                    if not (l == 0 and m == 0):
                        # Using the modulo operator (%) the grid wraps around
                        neighbours += current[((i + l) % SOR)][((j + m) % OSZLOP)]
            
            if (neighbours<2) or (neighbours>3):
                new[i][j]=0
            elif (neighbours==3) and (current[i][j]==0):
                newLifeBoard[i][j]=1
            else:
                new[i][j]=current[i][j]
            
                
def print_grid(gen):
    global oldLifeBoard
    output_str = "Generáció: {0} \n\r".format(gen)
    for i in range(SOR):
        for j in range(OSZLOP):
            if oldLifeBoard[i][j]==0: 
                output_str += ". "
            else:
                output_str += "@ "
        output_str += "\n\r"
    print(output_str, end=" ")
    
def graf_print_grid(gen, current,new):  
    for i in range(SOR):
        for j in range(OSZLOP):
            if (current[i][j]!=new[i][j]):
                if current[i][j]==0: 
                    tabla1(i,j,"red")
                else:
                    tabla1(i,j,"yellow")
               
                

def next_gen():
    global oldLifeBoard
    global newLifeBoard
    global gen
    #for k in range (5):
    #time.sleep(1/2.0)
    gen+=1
    graf_print_grid(5, oldLifeBoard,newLifeBoard)
    l1.configure(text="Generáció: "+str(gen)) 
    create_new_grid(oldLifeBoard,newLifeBoard)
    #print_grid(0)
    oldLifeBoard, newLifeBoard = newLifeBoard, oldLifeBoard
    window.after(100, next_gen)

### FŐPROGRAM ###

window=Tk()
can=Canvas(window, width=KOCKA_OLDAL*OSZLOP, height=KOCKA_OLDAL*SOR, bg='ivory')
can.pack(side=TOP)
tabla()
b1=Button(window,text="Next Generation", command=next_gen)
b1.pack(side=LEFT, padx=3, pady=3)
b2=Button(window,text="Kilép", command=window.quit)
b2.pack(side=LEFT, padx=3, pady=3)
l1=Label(window, text="Generáció: ",padx=3, pady=3)
l1.pack()

'''for row in range(SOR):
    grid_rows = []
    for col in range(OSZLOP):
        #Generate a random number and based on that decide whether to add a live or dead cell to the grid
        grid_rows+=[0]
    oldLifeBoard+=[grid_rows]
    newLifeBoard+=[grid_rows]'''        

   
'''oldLifeBoard[3][5]=1
oldLifeBoard[4][5]=1
oldLifeBoard[5][5]=1
oldLifeBoard[4][4]=1
oldLifeBoard[4][6]=1'''

oldLifeBoard[8][10]=1
oldLifeBoard[8][11]=1
oldLifeBoard[8][12]=1
oldLifeBoard[8][13]=1
oldLifeBoard[8][14]=1
oldLifeBoard[8][15]=1
oldLifeBoard[8][16]=1
oldLifeBoard[8][17]=1
oldLifeBoard[8][18]=1
oldLifeBoard[8][19]=1
    
print_grid(0)   
window.mainloop()
