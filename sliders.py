from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.geometry("500x500")
def rate():
    tmsg.showinfo("Rate","Thanks for rating")    
myslider=Scale(root,from_=0,to=10,orient=HORIZONTAL)
myslider.pack()
Button(root,text="Submit",pady=10,command=rate).pack()
root.mainloop()