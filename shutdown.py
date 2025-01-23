from tkinter import *
import os
a=Tk()
a.geometry("500x500")
def abc():
    os.system("shutdown/r /t 10")
b=Label(a,text="python",bg="blue",fg="pink").pack()
c=Button(a,text='restart',command=abc).pack()
a.mainloop()