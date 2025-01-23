from tkinter import *
from tkinter import messagebox

a=Tk()
a.geometry("500x500")

def discount():
    amount1 = int(amount.get())
    if amount1 <= 3000:
        #print(f"{amount1-500:,}")
        print(f"{amount1 -(amount1 * (20/100)):,}")
    else:
        #print(f"{amount1 - 1000:,}")
        print(f"{amount1:,}")

b=Label(a,text="shopping discount",fg="pink",bg="black")
b.grid(row = 1 , column = 3)

c = Label(a, text = "Amount")
c.grid(row= 4, column = 2)
amount=Entry(a)
amount.grid(row = 4 , column = 3)

discount=Button(a,text="get discount",fg="pink",bg="black", command = discount)
discount.grid(row= 7, column =3 )

a.mainloop()
