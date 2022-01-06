from tkinter import *
import tkinter.messagebox as t
root=Tk()
def func():
    print("You have made a successful menubar.")
def help():
    # print("")
    t.showinfo("Help","I will help you")
def rate():
    v=t.askquestion("Feedback","Was your experience good ?")
    if v=="yes":
        msg="Please rate us on microsoft store."
    else:
       msg="Please contact the developer to solve the problem."
    t.showinfo("Experience",msg)
def license():
    # print("LICENSE")
    t.showinfo("LICENSE","The software is copyright protected.No consumer should violate the copyright laws.")
mainmenu=Menu(root)
m1=Menu(mainmenu,tearoff=0)
m1.add_command(label="Add",command=func)
m1.add_command(label="Delete",command=func)
m1.add_separator()
m1.add_command(label="Save",command=func)
m1.add_command(label="Exit",command=quit)
m2=Menu(mainmenu,tearoff=0)
m3=Menu(mainmenu,tearoff=0)
m3.add_command(label="View License",command=license)
m2.add_command(label="Help",command=help)
m2.add_command(label="Rate us",command=rate)
mainmenu.add_cascade(label="File",menu=m1)
mainmenu.add_cascade(label="Help",menu=m2)
mainmenu.add_cascade(label="License",menu=m3)
root.config(menu=mainmenu)
root.mainloop()