from tkinter import *

root = Tk()
l1 = Label(root,text="This is label 1",fg="red")
l1.config(font=(None,30,'bold'))
b1 = Button(root,text="Button1",fg="yellow",bg="black")
b1.pack(side="right")
l1.pack()
l2 = Label(root,text="This is label2",fg="black")
l2.pack()
b2 = Button(root,text="Button2",fg="red",bg="black",height=1,width=30)
b2.pack()

root.geometry('500x500')
root.resizable(0,0)
root.mainloop()