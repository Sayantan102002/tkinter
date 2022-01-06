from tkinter import *
root=Tk()
root.geometry("655x333")
def hi():
    print("hi")
f=Frame(root,borderwidth=6,bg="grey",relief=SUNKEN)
f.pack(side=LEFT,anchor="nw")
b=Button(f,fg="red",text="hi",command=hi)
b.pack(side=LEFT)
root.mainloop()