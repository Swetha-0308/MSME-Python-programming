from tkinter import *
import os
a=Tk()
a.geometry("500x500")
def abc():
    s=e.get()
    print(s)
b=Label(a,text="python",bg="pink",fg="blue")
b.pack()
e=Entry(a)
e.pack()
c=Button(a,text='button',command=abc)
c.pack()
a.mainloop()