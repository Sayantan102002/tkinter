from tkinter import *
root=Tk()
def func():
    print("You have made a successful menubar.")
mainmenu=Menu(root)
m1=Menu(mainmenu,tearoff=0)
m1.add_command(label="Add",command=func)
m1.add_command(label="Delete",command=func)
m1.add_separator()
m1.add_command(label="Save",command=func)
m1.add_command(label="Exit",command=quit)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="File",menu=m1)
root.mainloop()