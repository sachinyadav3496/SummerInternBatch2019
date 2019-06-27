from tkinter import *

root = Tk()
f1 = Frame(root)
f1.pack()
l1 = Label(f1,text="Enter your username : ")
l1.config(font=(None,20,'italic'))
l1.grid(row=0,column=0)
e1 = Entry(f1)
e1.grid(row=0,column=1)

l2 = Label(f1,text="Enter your password : ")
l2.config(font=(None,20,'italic'))
l2.grid(row=1,column=0)
e2 = Entry(f1,show="*")
e2.grid(row=1,column=1)
l4 = Label(f1,text="Welcome",fg="red")
l4.config(font=(None,10,'italic'))
l4.grid(row=4)
def show():
    #print(e1.get())
    #print(e2.get())
    text = "Welcome user {}".format(e1.get())
    l4.configure(text=text)
b1 = Button(f1,text="submit",fg="red",bg="black",height=1,width=7,command=show)
b1.grid(row=3,columnspan=3)


root.mainloop()
