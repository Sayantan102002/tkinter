from tkinter import *
root=Tk()
w=500
h=500
root.geometry("500x500")
def size():
    global w
    global h
    w=w_.get()
    h=h_.get()
    root.geometry(f"{w}x{h}")
Label(root,text="Enter the width:",font="HElvetica 13 bold").grid(row=0,column=0)
Label(root,text="Enter the height:",font="HElvetica 13 bold").grid(row=1,column=0)
w_=IntVar()
h_=IntVar()
Entry(root,textvariable=w_).grid(row=0,column=1)
Entry(root,textvariable=h_).grid(row=1,column=1)
Button(root,text="Apply",bg="red",fg="yellow",font="Helvetica 13 bold",command=size).grid(row=3,column=1)
root.mainloop()