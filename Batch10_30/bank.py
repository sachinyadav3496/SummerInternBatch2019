import tkinter as tk


root = tk.Tk()

main_frame = tk.Frame(root)

label1 = tk.Label(main_frame,text="Hello World Welcome to Tkinter",font=("Times Roman",28,"bold") )

def do_something():
    r_new = tk.Tk()
    f = tk.Frame(r_new)
    eq = var.get()
    result = eval(eq)
    l1 = tk.Label(f,text=f"Result = {result}",font=("Times Roman",28,"bold") )
    l1.pack()
    f.pack()
    r_new.mainloop()

var  = tk.StringVar()
entry1 = tk.Entry(main_frame,textvariable=var,
        fg="blue",font=("Times Roman",28,"bold"))

button1 = tk.Button(main_frame,text="Click me", bg="black",fg="white",font=("Times Roman",28,"bold"),command=do_something)


label1.pack()

entry1.pack()
main_frame.pack()
button1.pack()

root.wm_minsize(500,500)
root.wm_title("My Application")

root.mainloop()
