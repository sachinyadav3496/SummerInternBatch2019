from tkinter import *

root = Tk()

f1 = Frame(root)

f2 = Frame(root)
f2.pack()
f1.pack()
l1 = Label(f1,text="Label 1 on frame 1",fg="red")
l1.pack()
b1 = Button(f1,text="Button1 on frame 1",fg="red")
b1.pack()
l2 = Label(f2,text="Label2 on frame 2",fg="blue")
l2.pack()
def show():
    l2.configure(text="Label2")
    l2.configure(fg="black")
b2 = Button(f2,text="Button2 on frame 2",fg="blue",command=show)
b2.pack(side="right")

root.mainloop()