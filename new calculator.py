from tkinter import *
from tkinter import messagebox
x=Tk()
x.geometry("500x500")
def get_input():
    a=int(first_input.get())
    b=int(second_input.get())
    return a,b
def add():
    a,b=get_input()
    print(a+b)
    z = Label(x, text=f'The Addition of given numbers is: = {a + b}')
    z.grid(row=6,column=0)
def sub():
    a,b=get_input()

    print(a-b)
    z=Label(x,text=f'The Sub of the given Numbers is: = {a-b}')
    z.grid(row=7,column=0)
def multiply():
    a,b=get_input()
    print(a*b)
    z = Label(x, text=f'The Multiplication of the given Numbers is: = {a * b}')
    z.grid(row=8,column=0)
def divide():
    a,b=get_input()
    print(b/a)
    z = Label(x, text=f'The Division of the given Numbers is: = {a / b}')
    z.grid(row=9,column=0)
b=Label(x,text="Calculator",fg="black",bg="violet")
b.grid(row=0,column=2)

g=Label(x,text="enter number 1",fg="purple")
g.grid(row=1,column=0)

first_input=Entry(x)
first_input.grid(row=1,column=1)
g1=Label(x,text="enter number 2",fg="purple")
g1.grid(row=2,column=0)
second_input=Entry(x)
second_input.grid(row=2,column=1)
add_button=Button(x,text="addition(+)",bg="skyblue",fg="black",command=add)
add_button.grid(row=4,column=3)
sub_button=Button(x,text="subtraction(-)",bg="skyblue",fg="black",command=sub)
sub_button.grid(row=4,column=4)
multiply_button=Button(x,text="multiplication(*)",bg="skyblue",fg="black",command=multiply)
multiply_button.grid(row=4,column=5)
divide_button=Button(x,text="divide(/)",bg="skyblue",fg="black",command=divide)
divide_button.grid(row=4,column=6)
x.mainloop()
