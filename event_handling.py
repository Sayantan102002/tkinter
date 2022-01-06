from tkinter import *
root=Tk()
def sayantan(event):
    print("You clicked.")
widget=Button(root,text="Click me please!")
widget.pack()
widget.bind("<Button-1>",sayantan)
widget.bind("<Double-1>",quit)
root.mainloop()