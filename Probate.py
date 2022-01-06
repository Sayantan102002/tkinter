# from tkinter import *
tax=0
class Probate:
    # root4=Tk()
    # w=1075
    # h=500
    # ws = root4.winfo_screenwidth()
    # hs = root4.winfo_screenheight() 
    # x = (ws/2) - (w/2)
    # y = (hs/2) - (h/2)
    # root4.geometry('%dx%d+%d+%d' % (w, h, x, y))
    # root4.maxsize(1075,500)
    # root4.minsize(1075,500)
    # # root44.overrideredirect(True)
    # # root44.geometry("{0}x{1}+0+0".format(root44.winfo_screenwidth(), root44.winfo_screenheight()))
    # # root4.focus_set()  
    # # root4.bind("<Escape>", lambda e: e.widget.quit())
    # section=IntVar()
    # def press(self):
    #     pass
    # Label(root4,text="Enter the Section no.",fg="black",font="Ariel 15 bold").place(x=250,y=250)
    # entry=Entry(root4,textvariable=section,font="Helvetica 15 bold")
    # entry.place(x=525,y=250)
    # Button(root4,text="Get details",font="Helvetica 12 bold",fg="white",bg="red4",command=press).place(x=450,y=300)
    def calculation(self,n):
        global tax
        if (n>10000 and n<=25000):	#750			
            tax=0.03*n
        elif(n>25000 and n<=100000):#
            tax=(0.03*25000)+(0.035*(n-25000))
        elif(n>100000 and n<=500000):
            tax=(0.03*25000)+(0.035*75000)+(0.045*(n-100000))
        elif(n>500000):
            tax=(0.03*25000)+(0.035*75000)+(0.045*400000)+(0.055*(n-500000))
        return str(round(tax,2))
    # root4.mainloop()
if __name__ == "__main__":
    obj=Probate()
    print(obj.calculation(25000))