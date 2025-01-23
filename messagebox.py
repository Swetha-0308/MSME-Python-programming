from tkinter import*
from tkinter import messagebox
a=Tk()
a.geometry("500x500")
messagebox.showinfo("info","information")
messagebox.showwarning("alert","warning")
messagebox.showerror("error","wrong input")
messagebox.askyesnocancel("info","accept")
messagebox.askyesno("info","information")
messagebox.askretrycancel("info","try again")
messagebox.askquestion("message","chat")
a.mainloop()