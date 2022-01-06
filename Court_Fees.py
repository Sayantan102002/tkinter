from tkinter import *
root=Tk()
l1=[]
l2=[]
root.title("The W.B Court-fees (Amendment) Act, 2002")
root.config(bg="khaki4")
d=0
lb1=Label(root) 
lb2=Label(root)
def court_Fees():
    global lb2
    global lb1
    lb2.destroy()
    lb1.destroy()
    def createList1(r1, r2,k): 
     return [item for item in range(r1, r2+100,k)] 
    def createList2(r1, r2,k): 
     return [item for item in range(r1, r2+1,k)]  
    def courtfees():
        global l1
        global l2
        l1=createList1(1,7500,100)
        l1+=createList1(7751,10000,250)
        l1+=createList1(10501,20000,500)
        l1+=createList1(21001,50000,1000)
        l1+=createList1(55001,300001,5000)
        l2+=createList2(10,100,10)
        l2+=createList2(108,620,8)
        l2+=createList2(636,780,16)
        l2+=createList2(810,1380,30)
        l2+=createList2(1430,2880,50)
        l2+=createList2(3230,6380,350)
        l2+=createList2(6750,13780,370)
        l2+=createList2(13990,17980,210)
        # print(l1,'\
        l2+=createList2(13990,17980,210)
        # print(l2)
    # courtfees()
    def calculation(a):
        courtfees()
        global d
        global t
        i=0
        for i in range(len(l1)):
            if a>=l1[i] and a<l1[i+1] and a<=300000:
                return (l2[i])
            elif a>300000:
                t=a-300000
                d=t//10000
                #  print(d)
                if d!=0 and (t%10000)==0:
                    return(17980+(d*100))
                elif d!=0 and (t%10000)!=0:
                     return(17980+(d*100)+100)
                elif t>=1 and t<=10000:
                     return(17980+100)
                else:
                     return(17980+(d*100))
    z=calculation(value.get())
    # print(z)+
    if z<50000:
        lb1=Label(root,text="Court Fees to be paid of ",fg="green",font="Helvetica 13 bold",bg="khaki4")
        lb1.place(x=375,y=365)
        lb2=Label(root,text="Rs. "+str(z)+".0",fg="red",font="Helvetica 13 bold",bg="khaki4")
        lb2.place(x=630,y=365)
    elif z>=50000:
        lb1=Label(root,text="Maximum amount of Court Fees to be paid of ",fg="green",font="Helvetica 13 bold",bg="khaki4")
        lb1.place(x=250,y=365)
        lb2=Label(root,text="Rs.50000.0",fg="red",font="Helvetica 13 bold",bg="khaki4")
        lb2.place(x=715,y=365)
n=0
tax=0      
w=1070
h=500
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight() 
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
# root.minsize(675,700)
root.maxsize(1070,500)
# root.geometry("500x300")
root.minsize(1000,500)
Label(root,text="The W.B Court-fees (Amendment) Act, 2002",borderwidth=6,relief=SUNKEN,bg="yellow",font="Helvetica 13 bold").place(x=300,y=30)
Label(root,text="Know the rates of Ad valorem Court fees leviable on the institution of suits,\n as per the W.B Court-fees (Amendment) Act, 2002",borderwidth=6,relief=SUNKEN,bg="pink",font="Helvetica 13 bold",padx=10,fg="navy").place(x=140,y=110)
Label(root,text="Enter value of the subject matter of suit:",fg="blue",font="Helvetica 13 bold",bg="khaki4").place(x=215,y=220)
value=IntVar()
t=Entry(root,textvariable=value,font="Helvetica 13 bold",width=15)
t.place(x=650,y=220)
Button(root,text="Get Result",fg="white",bg="red4",font="Helvetica 13 bold",command=court_Fees).place(x=480,y=290)
root.mainloop()
