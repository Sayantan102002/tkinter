from tkinter import *
import tkinter.messagebox as tm 
root=Tk()    
l1=Label(root) 
l2=Label(root)
w=1070
h=500
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight() 
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.maxsize(1000,500)
root.minsize(1000,500)
root.title("The Indian Succession Calculator U/s. 374 of I. Succ. Act. 1925")    
root.configure(bg="peach puff")
def result():
        global l1
        global l2
        tax=0
        n=amount.get()
        if(n<=10000):
            tax=0.03*n
        elif (n>10000 and n<=50000):				
            tax=(0.03*10000)+(0.04*(n-10000))
        elif(n>50000 and n<=100000):
            tax=(0.03*10000)+(0.04*40000)+(0.05*(n-50000))
        elif(n>100000 and n<=250000):
            tax=(0.03*10000)+(0.04*40000)+(0.05*50000)+(0.06*(n-100000))
        elif(n>250000 and n<=300000):
            tax=(0.03*10000)+(0.04*40000)+(0.05*50000)+(0.06*150000)+(0.065*(n-250000))
        elif(n>300000 and n<=400000):  
            tax=(0.03*10000)+(0.04*40000)+(0.05*50000)+(0.06*150000)+(0.065*50000)+(0.07*(n-300000))
        elif(n>400000 and n<=500000):
            tax=(0.03*10000)+(0.04*40000)+(0.05*50000)+(0.06*150000)+(0.065*50000)+(0.07*100000)+(0.075*(n-400000))
        else:
            tax=(0.03*10000)+(0.04*40000)+(0.05*50000)+(0.06*150000)+(0.065*50000)+(0.07*100000)+(0.075*100000)+(0.08*(n-500000))
        print()
        r=str(round(tax,2))
        l2.destroy()
        l1.destroy()
        if tax<50000:
           l2=Label(root,text="Court fees to be paid of",font="Helvetica 13 bold",fg="green",bg="peach puff")
           l2.place(x=338,y=400)
           l1=Label(root,text="Rs. "+r,fg="red",font="Helvetica 13 bold",bg="peach puff")
           l1.place(x=590,y=400)
        elif tax>=50000:
           l2=Label(root,text="Maximum amount of Court fees to be paid of",font="Helvetica 13 bold",fg="green",bg="peach puff")
           l2.place(x=240,y=400)   
           l1=Label(root,text="Rs.50000.0 ",fg="red",font="Helvetica 13 bold",bg="peach puff")
           l1.place(x=700,y=400)
t=Label(root,text="The Indian Succession Act 1925",borderwidth=6,relief=SUNKEN,bg="yellow",font="Helvetica 13 bold")
t.place(x=380,y=30)
Label(root,text="Know the exact amount of Ad valorem Court Fees to be levied, when the amount\n or value of any date or security specified in the certificate\n U/s. 374 of the act exceeds Rs.1,000/- (New Filing):-",bg="skyblue1",fg="red",font="Helvetica 13 bold",padx=10,borderwidth=6,relief=SUNKEN).place(x=110,y=110)
Label(root,text="Enter the amount :",pady=10,font="Helvetica 15 bold",bg="peach puff",fg="blue").place(x=330,y=235)
amount=IntVar()
money=Entry(root,textvariable=amount,fg="blue",font=12,width=15)
money.place(x=570,y=250)
Button(root,text="Get result",fg="white",bg="red4",command=result,font="Helvetica 13 bold").place(x=465,y=325)
def save():
    pass
def save_as():
    pass
def registration():
    pass
def Disclaimer():
    pass
def Feedback():
    def rate():
        tm.showinfo("Rate","Thanks for rating")
        root2.destroy()
    w=200
    h=200
    root2=Tk()
    ws = root2.winfo_screenwidth()
    hs = root2.winfo_screenheight() 
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root2.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root2.minsize(200,200)
    root2.maxsize(200,200)
    Label(root2,text="Rate us from 1 to 10:").pack()
    myslider=Scale(root2,from_=0,to=10,orient=HORIZONTAL)
    myslider.pack()
    Button(root2,text="Submit",pady=10,command=rate).pack()
    root2.mainloop()
def Help():
    pass
def exit_():
    root.destroy()
def license_():
    pass
mainmenu=Menu(root)

mymenu=Menu(mainmenu,tearoff=0)
mymenu2=Menu(mainmenu,tearoff=0)
mymenu.add_command(label="Save",command=save)
mymenu.add_command(label="Save As",command=save_as)
mymenu.add_command(label="Exit",command=exit_)
mymenu2.add_command(label="License",command=license_)
mymenu2.add_command(label="Registration",command=registration)
mainmenu.add_cascade(label="File",menu=mymenu)
mainmenu.add_cascade(label="License",menu=mymenu2)
mainmenu.add_command(label="Feedback",command=Feedback)
mainmenu.add_command(label="Help",command=Help)
mainmenu.add_command(label="Disclaimer",command=Disclaimer)
root.config(menu=mainmenu)

root.mainloop() 
if __name__ == "__main__":
    pass
