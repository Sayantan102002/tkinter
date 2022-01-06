from tkinter import *
from PIL import Image, ImageTk
root=Tk()
root.geometry("800x200")
root.minsize(400,400)
root.maxsize(50000,999000)
root.title("Sayantan Chakraborty")
s=Label(text="My name is Sayantan Chakraborty.",bg="green",fg="black",font="ariel 19 bold",pady=50,borderwidth=3,relief=SUNKEN)
#  # p=PhotoImage(file="20161118_061814.png")
# image=Image.open("20161116_100249.jpg")
# photo=ImageTk.PhotoImage(image)
# s=Label(image=photo)
s.pack(side="top",anchor='n',fill=X,padx=34,pady=34)
root.mainloop()
