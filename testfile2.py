# from testfile1 import tsc3
# from tkinter import *
# root=Tk()
# root.geometry("900x500")
# Label(root,text="Enter the amount",fg="red").grid(row=0,column=0)
# amount=IntVar()
# l1=Label(root)
# def result():
#     global l1
#     e=amount.get()
#     obj=tsc3()
#     j=obj.calculation(e)
#     l1.destroy()
#     l1=Label(root,text="Amount="+str(j))
#     l1.grid(row=3,column=1)
# Entry(root,textvariable=amount).grid(row=0,column=1)
# Button(root,text="Get result",bg="red4",command=result,fg="white").grid(row=1,column=1)
# root.mainloop()
from tkinter import *
from sys import exit
def popupError(s):
    popupRoot = Tk()
    popupRoot.after(2000, exit)
    popupButton = Button(popupRoot, text = s, font = ("Verdana", 12), bg = "yellow", command = exit)
    popupButton.pack()
    popupRoot.geometry('400x50+700+500')
    popupRoot.mainloop()
popupError("Hi")