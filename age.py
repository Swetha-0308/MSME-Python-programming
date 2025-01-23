from tkinter import *
from tkinter import messagebox

a=Tk()
a.geometry("500x500")

def age_error():
    age=int(age_e.get())
    if age<=18:
        messagebox.showerror("invalid","less than 18")
    else:
        print(age)

def name_error():
    name=name_e.get()
    if "123456789" in name:
        print("name cannot contain a number")
    else:
        print(name)

def login():
    name_input=name_e.get()
    print(name_input)
    age_error()
b=Label(a,text="login page",bg="pink",fg="black")
b.pack()
name_e=Entry(a)
name_e.pack()

age_e=Entry(a)
age_e.pack()

button=Button(a,text="Login",command=login)
button.pack()
a.mainloop()







































































































































































































































































