from tkinter import *
import tkinter.messagebox as tm
root5=Tk()
root5.config(bg="LightGoldenrod1")
w=1055
h=500
ws = root5.winfo_screenwidth()
hs = root5.winfo_screenheight() 
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root5.geometry('%dx%d+%d+%d' % (w, h, x, y))
# root5.minsize(675,700)
root5.maxsize(1055,500)
# root5.geometry("500x300")
root5.minsize(1055,500)
root5.title("The Indian Succession Calculator U/s. 376 of I. Succ. Act. 1925")
l1=Label(root5)
l2=Label(root5)
def cal():
          global l1
          global l2
          n=amount.get()
          print(n)
          if(n<=10000):
           tax=0.04*n
          elif (n>10000 and n<=50000):				
           tax=(0.04*10000)+(0.045*(n-10000))
          elif(n>50000 and n<=100000):
           tax=(0.04*10000)+(0.045*40000)+(0.06*(n-50000))
          elif(n>100000 and n<=250000):
           tax=(0.04*10000)+(0.045*40000)+(0.06*50000)+(0.075*(n-100000))
          elif(n>250000 and n<=300000):
           tax=(0.04*10000)+(0.045*40000)+(0.06*50000)+(0.075*150000)+(0.0825*(n-250000))
          elif(n>300000 and n<=400000):  
           tax=(0.04*10000)+(0.045*40000)+(0.06*50000)+(0.075*150000)+(0.0825*50000)+(0.09*(n-300000))
          elif(n>400000 and n<=500000):
           tax=(0.04*10000)+(0.045*40000)+(0.06*50000)+(0.075*150000)+(0.0825*50000)+(0.09*100000)+(0.0975*(n-400000))
          else:
           tax=(0.04*10000)+(0.045*40000)+(0.06*50000)+(0.075*150000)+(0.0825*50000)+(0.09*100000)+(0.0975*100000)+(0.105*(n-500000))
          r=str(round(tax,2))
          l2.destroy()
          l1.destroy()
          #print(f"Result={r}")
        #   f2=Frame(root5,borderwidth=3,relief=SUNKEN,bg="green").grid(row=4,column=1)
        #   Label(root5,text="").grid(row=3,column=1)
          print(r)  
          if tax<50000:
           l2=Label(root5,text="Court fees to be paid of",font="Helvetica 13 bold",fg="green",bg="LightGoldenrod1")
           l2.place(x=340,y=385)   
           l1=Label(root5,text="Rs. "+r,fg="red",font="Helvetica 13 bold",bg="LightGoldenrod1")
           l1.place(x=590,y=385)
          elif tax>=50000:
           l2=Label(root5,text="Maximum amount of Court fees to be paid of",font="Helvetica 13 bold",fg="green",bg="LightGoldenrod1")
           l2.place(x=240,y=385)   
           l1=Label(root5,text="Rs.50000.0 ",fg="red",font="Helvetica 13 bold",bg="LightGoldenrod1")
           l1.place(x=700,y=385)
# f=Frame(root5,borderwidth=3,relief=SUNKEN).grid(row=0,column=1)
t=Label(root5,text="The Indian Succession Act 1925",borderwidth=6,relief=SUNKEN,bg="light pink",font="Helvetica 13 bold")
t.place(x=350,y=30)
Label(root5,text="Know the exact amount of Ad valorem Court Fees to be levied, when the aggregate amount\n or value of any date or security specified in the certificate and of any date or security \nhas been extended U/s. 376 of the act, exceeds Rs. 1,000/- :-",bg="skyblue1",fg="red",font="Helvetica 13 bold",borderwidth=6,relief=SUNKEN,padx=10).place(x=50,y=110)
Label(root5,text="Enter the amount :",pady=10,font="Helvetica 15 bold",fg="blue",bg="LightGoldenrod1").place(x=305,y=235)
amount=IntVar()
money=Entry(root5,textvariable=amount,fg="blue",font=12,width=15).place(x=545,y=250)
Button(root5,text="Get result",fg="white",bg="red4",command=cal,font="Helvetica 13 bold").place(x=455,y=315)
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
     root52.destroy()
    w=200
    h=200
    root52=Tk()
    ws = root52.winfo_screenwidth()
    hs = root52.winfo_screenheight() 
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root52.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root52.minsize(200,200)
    root52.maxsize(200,200)
    Label(root52,text="Rate us from 1 to 10:").pack()
    myslider=Scale(root52,from_=0,to=10,orient=HORIZONTAL)
    myslider.pack()
    Button(root52,text="Submit",pady=10,command=rate).pack()
    root52.mainloop()
def Help():
    pass
def quit_():
    root5.destroy()
def license_():
    pass
mainmenu=Menu(root5)

mymenu=Menu(mainmenu,tearoff=0)
mymenu2=Menu(mainmenu,tearoff=0)
# mymenu3=Menu(mainmenu,tearoff=0)

mymenu.add_command(label="Save",command=save)
mymenu.add_command(label="Save As",command=save_as)
mymenu.add_command(label="Exit",command=quit_)
mymenu2.add_command(label="License",command=license_)
mymenu2.add_command(label="Registration",command=registration)
# mymenu3.add_command(label="Disclaimer",command=Disclaimer)
mainmenu.add_cascade(label="File",menu=mymenu)
mainmenu.add_cascade(label="License",menu=mymenu2)
mainmenu.add_command(label="Feedback",command=Feedback)
mainmenu.add_command(label="Help",command=Help)
mainmenu.add_command(label="Disclaimer",command=Disclaimer)
root5.config(menu=mainmenu)

root5.mainloop()