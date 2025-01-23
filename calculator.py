from tkinter import *
from tkinter import messagebox
a=Tk()
a.geometry("500x500")
def get_input():
    a=int(first_input.get())
    b=int(second_input.get())
    return a,b
def add():
    a,b=get_input()
    print(a+b)
def sub():
    a,b=get_input()
    print(a-b)
def multiply():
    a,b=get_input()
    print(a*b)
def divide():
    a,b=get_input()
    print(b/a)
b=Label(a,text="Calculator",fg="green",bg="pink")
b.pack()
g=Label(a,text="enter number 1",fg=(pink))
first_input=Entry(a)
first_input.pack()
second_input=Entry(a)
second_input.pack()
add_button=Button(a,text="add",bg="pink",fg="black",command=add)
add_button.pack()
sub_button=Button(a,text="sub",bg="pink",fg="black",command=sub)
sub_button.pack()
multiply_button=Button(a,text="multiply",bg="pink",fg="black",command=multiply)
multiply_button.pack()
divide_button=Button(a,text="divide",bg="pink",fg="black",command=divide)
divide_button.pack()
a.mainloop()

