from tkinter import *
root=Tk()
root.geometry("600x600")
root.maxsize(600,500)
root.minsize(500,400)
root.title("The Succession Calculator")
s=Label(text='Ready',bg="red",fg="yellow",font="calibri 15 bold",borderwidth=3,relief=SUNKEN)
s.pack(side="bottom",anchor="s",fill=X,padx=30,pady=30)
root.mainloop()