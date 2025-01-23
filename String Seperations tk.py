# String Sepeartion GUI(Graphical User Interface) using tkinter library




from tkinter import *
from tkinter import messagebox

def Str_seperation():

    # string = input("Enter an String: ")
    string = string_entry.get()
    if string == "":
        messagebox.showerror( "Error", "You wanna Enter an String")
           # print("You wanna enter an String")
    lower_letters = ''
    upper_letters = ''
    special_char = ''
    for i in string:
        if i.islower():
            lower_letters += i
        elif (i.isupper()):
            upper_letters += i
        else:
            special_char+=i

    print(f"The lower case letters are {lower_letters}")
    print(f"The upper case letters are {upper_letters}")
    if special_char == '':
        print()
    else:
        print(f"The special characters are {special_char}")
        # wc = input("Do you want to continue? Enter y/n: ")
        # if wc == 'y':
        #     continue
        # else:
        #     break

a = Tk()
a.geometry("500x500")

label_1 = Label(a, text = "String Seperation")
label_1.pack()

string_entry = Entry(a)
string_entry.pack()

string_button = Button(a, text = "Seperate", command = Str_seperation)
string_button.pack()

a.mainloop()
