from tkinter import *

abl=Tk()

hitel=0
kamat=5
futamido=0
teljes_o=0
jovedelem=0

def torleszto():
    global hitel
    global kamat
    global futamido
    global teljes_o
    global jovedelem
    hitel=int(mezo1.get())
    futamido=int(mezo2.get())
    jovedelem=int(mezo3.get())
    if (hitel>0) and (futamido>0) and (jovedelem>0):
        if (jovedelem<=150000): 
            kamat=7
        elif (jovedelem<=250000):
            kamat=6.5
        elif (jovedelem<=350000):
            kamat=6
        elif (jovedelem<=450000):
            kamat=5.5
        else:
            kamat=9
        print(kamat)    
        teljes_o=hitel*((1+(kamat/100))**futamido)
        mezo4.delete(0,len(mezo4.get()))
        mezo4.insert(0,str('{:,d}'.format(int(teljes_o)).replace(","," ")))

Label(abl,text="Kezdő tőke: ").grid(row=1, sticky=E)
Label(abl,text="Ft   ").grid(row=1, column=3, sticky=W)
Label(abl,text="Futamidő :").grid(row=2, sticky=E)
Label(abl,text="év   ").grid(row=2, column=3, sticky=W)
Label(abl,text="Havi nettó jövedelem: ").grid(row=3, sticky=E)
Label(abl,text="Ft   ").grid(row=3, column=3, sticky=W)
Label(abl,text="Várható összeg a futamidő végén: ").grid(row=1, column=4, sticky=E)
Label(abl,text="Ft   ").grid(row=1, column=6, sticky=W)

mezo1=Entry(abl, bg="grey", justify=RIGHT)
mezo1.insert(0, "1000000")
mezo2=Entry(abl,bg="grey", justify=RIGHT)
mezo2.insert(0, 10)
mezo3=Entry(abl,bg="grey",justify=RIGHT)
mezo3.insert(0, 500000)
mezo4=Entry(abl,bg="grey",justify=RIGHT)

b1=Button(abl,text="Számol",command=torleszto).grid(row=4, column=7, padx=10, pady=10)


can1=Canvas(abl, width=160, height=107, bg="gray")
photo=PhotoImage(file="kis_groot.png")
item=can1.create_image(82,54, image=photo)


mezo1.grid(row=1, column=2)
mezo2.grid(row=2, column=2)
mezo3.grid(row=3, column=2)
mezo4.grid(row=1, column=5)
can1.grid(row=1, column=7, rowspan=3, padx=10, pady=10)

mezo1.focus()

abl.mainloop()

