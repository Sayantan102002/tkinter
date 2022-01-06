from tkinter import *
import tkinter.messagebox as tm
from testfile1 import tsc3
from tsc import calc
from testfile3 import Fees
import datetime as d
from I_P_C import IPC
# from tkinter.tix import *
from Probate import Probate
from plaintcf import plaint
# from MVAct import motor_vehicles
# import win10toast
# import notify2
d1=d.date(2020,7,15)
t3=d.date.today()
z3=(d1-t3).days
# from The_succession_Calculator import func
if z3==0 or z3<0:
    root56=Tk()
    # root56.iconbitmap(root56,"C:/Users/Sayantan/Desktop/Tkinter tutorials/favicon.ico")
    w=675
    h=450
    ws = root56.winfo_screenwidth()
    hs = root56.winfo_screenheight() 
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root56.geometry('%dx%d+%d+%d' % (w, h, x, y))
    # root56.minsize(675,700)
    # root56.maxsize(675,700)
    root56.resizable(False,False)
    #f=Frame(root56,width=ws,height=hs).pack()
    root56.config(bg="aquamarine2")
    root56.title("Alert!")
    Label(root56,text="Your license has been expired",font="Helvetica 17 bold",fg="red",bg="aquamarine2").pack(pady=30)
    #f1=Frame(root56,bg="white").pack()
    Label(root56,text="To continue the service please\ncontact with :-",fg="dark orange",font=("Goudy old style", 20,"bold"),bg="dark green").pack()
    Label(root56,text="Advocate Sri Suman Chakraborty\n or\n Sri Sayantan Chakraborty\n Ph. Nos. : - 9434 450 866 / 9126 264 166",bg="navy",fg="yellow",font="Helvetica 13 bold",padx=10,pady=15).pack(pady=30)
    # Label(root56,text="To continue the service please contact with developer for renewal.",fg="dark orange",font=("Goudy old style", 35,"bold"),bg="azure").pack()
    root56.mainloop()
else:
    root100=Tk()
    # root100.iconbitmap(root100,"C:/Users/Sayantan/Desktop/Tkinter tutorials/favicon.ico")
    root100.configure(bg="Sky Blue1")
    root100.title("Legal Practioners' Assistant")
    root100.geometry("540x620")
    w=625
    h=600
    ws = root100.winfo_screenwidth()
    hs = root100.winfo_screenheight() 
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root100.geometry('%dx%d+%d+%d' % (w, h, x, y))
    # root100.minsize(685,700)
    # root100.maxsize(685,700)
    # root100.geometry("{0}x{1}+0+0".format(root100.winfo_screenwidth(), root100.winfo_screenheight()))
    # l1=Label(root100)
    l2=Label(root100)


    def Succession1():
        # global l1
        global l2
        root=Tk()
        # root.iconbitmap(root,"C:/Users/Sayantan/Desktop/Tkinter tutorials/favicon.ico")
        root.resizable(False,False)
        # l1=Label(root)
        l2=Label(root)
        w=960
        h=500
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight() 
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        # root.maxsize(1075,500)
        # root.minsize(1075,500)
        root.title("The Indian Succession Calculator U/s. 374 of I. Succ. Act. 1925")    
        root.configure(bg="Sky Blue1")
        def result1():
            # global l1
            global l2
            n1=money.get()
            n1=int(n1)
            # print(n1)
            ob=tsc3()
            tax1=ob.calculation(n1)     
            # print(tax1)
            r=str(round(tax1,2))   
            l2.destroy()
            # l1.destroy()
            if tax1<50000 and n1>1000:
                l2=Label(root,text="Court Fees to be paid of Rs. "+r,font="Helvetica 15 bold",fg="red",bg="Sky Blue1")
                l2.grid(row=4,column=0,columnspan=2,pady=25)
                # l1=Label(root,text="         Rs. "+r,fg="red",font="Helvetica 13 bold",bg="Sky Blue1")
                # l1.grid(row=4,column=0,padx=50)
            elif tax1>=50000:
                l2=Label(root,text="Maximum amount of Court Fees to be paid of Rs.50000/-" ,font="Helvetica 15 bold",fg="red",bg="Sky Blue1")
                l2.grid(row=4,column=0,columnspan=2,pady=25)
                # l1=Label(root,text="Rs.50000.0 ",fg="red",font="Helvetica 13 bold",bg="Sky Blue1")
                # l1.grid(row=4,column=1,columnspan=2)
            elif n1<1000:
                l2=Label(root,text="The amount should exceed Rs. 1,000/-",fg="red",font="Helvetica 15 bold",bg="Sky Blue1")
                l2.grid(row=4,column=0,columnspan=2,pady=25)
                # l2=Label(root,text="Rs. 1,000/-",bg="Sky Blue1",fg="red",font="Helvetica 13 bold")
                # l2.grid(row=4,column=1,columnspan=2)
        def result2(event):
            # global l1
            global l2
            n1=money.get()
            n1=int(n1)
            # print(n1)
            ob=tsc3()
            tax1=ob.calculation(n1)     
            # print(tax1)
            r=str(round(tax1,2))   
            l2.destroy()
            # l1.destroy()
            if tax1<50000 and n1>1000:
                l2=Label(root,text="Court Fees to be paid of Rs. "+r,font="Helvetica 15 bold",fg="red",bg="Sky Blue1")
                l2.grid(row=4,column=0,columnspan=2,pady=25)
                # l1=Label(root,text="         Rs. "+r,fg="red",font="Helvetica 13 bold",bg="Sky Blue1")
                # l1.grid(row=4,column=0,padx=50)
            elif tax1>=50000:
                l2=Label(root,text="Maximum amount of Court Fees to be paid of Rs.50000/-" ,font="Helvetica 15 bold",fg="red",bg="Sky Blue1")
                l2.grid(row=4,column=0,columnspan=2,pady=25)
                # l1=Label(root,text="Rs.50000.0 ",fg="red",font="Helvetica 13 bold",bg="Sky Blue1")
                # l1.grid(row=4,column=1,columnspan=2)
            elif n1<1000:
                l2=Label(root,text="The amount should exceed Rs. 1,000/-",fg="red",font="Helvetica 15 bold",bg="Sky Blue1")
                l2.grid(row=4,column=0,columnspan=2,pady=25)
                # l2=Label(root,text="Rs. 1,000/-",bg="Sky Blue1",fg="red",font="Helvetica 13 bold")
                # l2.grid(row=4,column=1,columnspan=2)
        t=Label(root,text="The Indian Succession Act 1925",borderwidth=6,relief=SUNKEN,bg="yellow",font="Helvetica 13 bold",fg="black")
        t.grid(row=0,column=0,columnspan=2,pady=25)
        Label(root,text="Know the exact amount of ad valorem Court Fees to be levied, when the amount\n or value of any debt or security specified in the certificate U/s. 374 of the act\nexceeds Rs.1,000/- (New Filing):-",bg="NavajoWhite2",fg="navy",font="Helvetica 13 bold",padx=10,borderwidth=6,relief=SUNKEN).grid(row=1,column=0,columnspan=2,padx=50,pady=10)
        Label(root,text="Enter the amount or value of any debt or security :",pady=10,font="Helvetica 15 bold",bg="Sky Blue1",fg="blue").grid(row=2,column=0,columnspan=1)
        amount=IntVar()
        money=Entry(root,textvariable=amount,fg="navy",font=("Ariel",13,"italic"),width=15,borderwidth=6,relief=SUNKEN)
        money.grid(row=2,column=1,pady=25)
        # money.config(highlightcolor="red",highlightbackground = "red")
        money.focus()
        b=Button(root,text="Get result",fg="white",bg="red4",command=result1,font="Helvetica 13 bold")
        b.grid(row=3,column=0,columnspan=2)
        root.bind("<Return>",result2)
        root.mainloop()




    # l3=Label(root100)
    l4=Label(root100)
    def Succession2():
        # global l3
        global l4
        root5=Tk()
        # root5.iconbitmap(root5,"C:/Users/Sayantan/Desktop/Tkinter tutorials/favicon.ico")
        root5.resizable(False,False)
        # l3=Label(root5)
        l4=Label(root5)
        root5.config(bg="Sky Blue1")
        w=1065
        h=500
        ws = root5.winfo_screenwidth()
        hs = root5.winfo_screenheight() 
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        root5.geometry('%dx%d+%d+%d' % (w, h, x, y))
        # root5.minsize(675,700)
        # root5.maxsize(1055,500)
        # root5.geometry("500x300")
        # root5.minsize(1055,500)
        root5.title("The Indian Succession Calculator U/s. 376 of I. Succ. Act. 1925")
        # l1=Label(root5)
        # l2=Label(root5)
        def cal1():
            # global l3
            global l4
            t1=money2.get()
            t1=int(t1)
            obj=calc()
            tax2=obj.cal(t1)
            r2=str(round(tax2,2))
            # l3.destroy()
            l4.destroy()
            if tax2<50000 and t1>1000:
                l4=Label(root5,text="Court Fees to be paid of Rs. "+r2,font="Helvetica 15 bold",fg="red",bg="Sky Blue1")
                l4.grid(row=4,column=0,columnspan=2,pady=15) 
                # l3=Label(root5,text="Rs. "+r2,fg="red",font="Helvetica 13 bold",bg="Sky Blue1")
                # l3.grid(row=4,column=0,columnspan=2,pady=15)
            elif tax2>=50000:
                l4=Label(root5,text="Maximum amount of Court Fees to be paid of Rs.50000/-",font="Helvetica 15 bold",fg="red",bg="Sky Blue1")
                l4.grid(row=4,column=0,columnspan=2,pady=15) 
                # l3=Label(root5,text="Rs.50000.0 ",fg="red",font="Helvetica 13 bold",bg="Sky Blue1")
                # l3.place(x=700,y=385)
            elif t1<1000:
                l4=Label(root5,text="The amount should exceed Rs. 1,000/-",fg="red",font="Helvetica 15 bold",bg="Sky Blue1")
                l4.grid(row=4,column=0,columnspan=2,pady=15) 
                # l3=Label(root5,text="Rs. 1,000/-",bg="Sky Blue1",fg="red",font="Helvetica 13 bold")
                # l3.place(x=625,y=385)
        def cal2(event):
            # global l3
            global l4
            t1=money2.get()
            t1=int(t1)
            obj=calc()
            tax2=obj.cal(t1)
            r2=str(round(tax2,2))
            # l3.destroy()
            l4.destroy()
            if tax2<50000 and t1>1000:
                l4=Label(root5,text="Court Fees to be paid of Rs. "+r2,font="Helvetica 15 bold",fg="red",bg="Sky Blue1")
                l4.grid(row=4,column=0,columnspan=2,pady=15) 
                # l3=Label(root5,text="Rs. "+r2,fg="red",font="Helvetica 13 bold",bg="Sky Blue1")
                # l3.grid(row=4,column=0,columnspan=2,pady=15)
            elif tax2>=50000:
                l4=Label(root5,text="Maximum amount of Court Fees to be paid of Rs.50000/-",font="Helvetica 15 bold",fg="red",bg="Sky Blue1")
                l4.grid(row=4,column=0,columnspan=2,pady=15) 
                # l3=Label(root5,text="Rs.50000.0 ",fg="red",font="Helvetica 13 bold",bg="Sky Blue1")
                # l3.place(x=700,y=385)
            elif t1<1000:
                l4=Label(root5,text="The amount should exceed Rs. 1,000/-",fg="red",font="Helvetica 15 bold",bg="Sky Blue1")
                l4.grid(row=4,column=0,columnspan=2,pady=15) 
                # l3=Label(root5,text="Rs. 1,000/-",bg="Sky Blue1",fg="red",font="Helvetica 13 bold")
                # l3.place(x=625,y=385)
        t=Label(root5,text="The Indian Succession Act 1925",borderwidth=6,relief=SUNKEN,bg="yellow",fg="black",font="Helvetica 13 bold")
        t.grid(row=0,column=0,columnspan=2,pady=25)
        Label(root5,text="Know the exact amount of ad valorem Court Fees to be levied, when the aggregate amount\n or value of any debt or security specified in the certificate and of any debt or security\nhas been extended U/s. 376 of the act, exceeds Rs. 1,000/- :-",bg="NavajoWhite2",fg="navy",font="Helvetica 13 bold",borderwidth=6,relief=SUNKEN,padx=10).grid(row=1,column=0,columnspan=2,padx=50,pady=10)
        Label(root5,text="Put aggregated amount or value of any debt or security",pady=10,font="Helvetica 15 bold",fg="blue",bg="Sky Blue1").grid(row=2,column=0,columnspan=1)
        amount2=IntVar()
        money2=Entry(root5,textvariable=amount2,fg="navy",font="Ariel 15 italic",width=15,borderwidth=6,relief=SUNKEN)
        money2.grid(row=2,column=1,pady=25)
        money2.focus()
        Button(root5,text="Get result",fg="white",bg="red4",command=cal1,font="Helvetica 13 bold").grid(row=3,column=0,columnspan=2)
        root5.bind("<Return>",cal2)
        root5.mainloop()


    lb1=Label(root100) 
    # lb2=Label(root100)
    def Court_Fees():
        global lb1
        # global lb2
        root11=Tk()
        # root11.iconbitmap(root11,"C:/Users/Sayantan/Desktop/Tkinter tutorials/favicon.ico")
        root11.title("The W.B Court Fees (Amendment) Act, 2002")
        root11.config(bg="Sky Blue1")
        lb1=Label(root11) 
        # lb2=Label(root11)
        root11.resizable(False,False)
        def fees1():
            global lb1
            # global lb2
            o=t.get()
            o=int(o)
            obj1=Fees()
            z=obj1.calculation(o)
            lb1.destroy()
            # lb2.destroy()
            if z<50000:
                lb1=Label(root11,text="Court Fees to be paid of Rs. "+str(z)+"/-",fg="red",font="Helvetica 15 bold",bg="Sky Blue1")
                lb1.grid(row=4,column=0,columnspan=2,pady=25) 
                # lb2=Label(root11,text="Rs. "+str(z)+".0",fg="red",font="Helvetica 13 bold",bg="Sky Blue1")
                # lb2.grid(row=4,column=0,columnspan=2,pady=15) 
            elif z>=50000:
                lb1=Label(root11,text="Maximum amount of Court Fees to be paid of Rs.50000/-",fg="red",font="Helvetica 15 bold",bg="Sky Blue1")
                lb1.grid(row=4,column=0,columnspan=2,pady=25) 
                # lb2=Label(root11,text="Rs.50000.0",fg="red",font="Helvetica 13 bold",bg="Sky Blue1")
                # lb2.grid(row=4,column=0,columnspan=2,pady=15) 
        def fees2(event):
            global lb1
            # global lb2
            o=t.get()
            o=int(o)
            obj1=Fees()
            z=obj1.calculation(o)
            lb1.destroy()
            # lb2.destroy()
            if z<50000:
                lb1=Label(root11,text="Court Fees to be paid of Rs. "+str(z)+"/-",fg="red",font="Helvetica 15 bold",bg="Sky Blue1")
                lb1.grid(row=4,column=0,columnspan=2,pady=25) 
                # lb2=Label(root11,text="Rs. "+str(z)+".0",fg="red",font="Helvetica 13 bold",bg="Sky Blue1")
                # lb2.grid(row=4,column=0,columnspan=2,pady=15) 
            elif z>=50000:
                lb1=Label(root11,text="Maximum amount of Court Fees to be paid of Rs.50000/-",fg="red",font="Helvetica 15 bold",bg="Sky Blue1")
                lb1.grid(row=4,column=0,columnspan=2,pady=25) 
                # lb2=Label(root11,text="Rs.50000.0",fg="red",font="Helvetica 13 bold",bg="Sky Blue1")
                # lb2.grid(row=4,column=0,columnspan=2,pady=15)   
        w=1050
        h=500
        ws = root11.winfo_screenwidth()
        hs = root11.winfo_screenheight() 
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        root11.geometry('%dx%d+%d+%d' % (w, h, x, y))
        # root11.minsize(675,700)
        # root11.maxsize(1070,500)
        # root11.geometry("500x300")
        # root11.minsize(1000,500)
        Label(root11,text="The W.B Court Fees (Amendment) Act, 2002",borderwidth=6,relief=SUNKEN,bg="yellow",font="Helvetica 15 bold").grid(row=0,column=0,columnspan=2,pady=25)
        Label(root11,text="Know the amount of ad valorem Court Fees leviable on the institution of suits,\n as per the W.B Court Fees (Amendment) Act, 2002",borderwidth=6,relief=SUNKEN,bg="NavajoWhite2",font="Helvetica 15 bold",padx=10,fg="navy").grid(row=1,column=0,columnspan=2,padx=50,pady=10)
        Label(root11,text="   Enter value of the subject matter of suit:",fg="blue",font="Helvetica 15 bold",bg="Sky Blue1").grid(row=2,column=0,columnspan=1)
        value=IntVar()
        t=Entry(root11,textvariable=value,font="Helvetica 15 italic",width=15,borderwidth=6,relief=SUNKEN,fg="navy")
        t.grid(row=2,column=1,pady=25)
        # Label(root100,text="                      ").grid(row=2,column=2)
        t.focus()
        Button(root11,text="Get Result",fg="white",bg="red4",font="Helvetica 15 bold",command=fees1).grid(row=3,column=0,columnspan=2)
        root11.bind("<Return>",fees2)
        root11.mainloop()

        
    label11=Label(root100)
    # label12=Label(root100)
    def probate():
        global label11
        # global label12
        root4=Tk()
        # root4.iconbitmap(root4,"C:/Users/Sayantan/Desktop/Tkinter tutorials/favicon.ico")
        root4.config(bg="Sky Blue1")
        root4.title("C.F payable in Probate or L.A.")
        label11=Label(root4)
        # label12=Label(root4)
        root4.resizable(False,False)
        def press1():
            global label11
            # global label12
            ob=Probate()
            n=entry.get()
            n=int(n)
            z=ob.calculation(n)
            label11.destroy()
            # label12.destroy()
            if n>10000:
                label11=Label(root4,text="Court Fees to be paid of Rs. "+z,fg="red",font="Helvetica 15 bold",bg="Sky Blue1")
                label11.grid(row=4,column=0,columnspan=2,pady=15) 
                # label12=Label(root4,text="Rs. "+z,fg="red",font="Helvetica 13 bold",bg="Sky Blue1")
                # label12.grid(row=4,column=0,columnspan=2,pady=15) 
            else:
                label11=Label(root4,text="The amount should exceed Rs. 10,000/-",fg="red",font="Helvetica 15 bold",bg="Sky Blue1")
                label11.grid(row=4,column=0,columnspan=2,pady=15) 
                # label12=Label(root4,text="Rs. 10,000/-",bg="Sky Blue1",fg="red",font="Helvetica 13 bold")
                # label12.grid(row=4,column=0,columnspan=2,pady=15)                  
        def press2(event):
            global label11
            # global label12
            ob=Probate()
            n=entry.get()
            n=int(n)
            z=ob.calculation(n)
            label11.destroy()
            # label12.destroy()
            if n>10000:
                label11=Label(root4,text="Court Fees to be paid of Rs. "+z,fg="red",font="Helvetica 15 bold",bg="Sky Blue1")
                label11.grid(row=4,column=0,columnspan=2,pady=15) 
                # label12=Label(root4,text="Rs. "+z,fg="red",font="Helvetica 13 bold",bg="Sky Blue1")
                # label12.grid(row=4,column=0,columnspan=2,pady=15) 
            else:
                label11=Label(root4,text="The amount should exceed Rs. 10,000/-",fg="red",font="Helvetica 15 bold",bg="Sky Blue1")
                label11.grid(row=4,column=0,columnspan=2,pady=15) 
                # label12=Label(root4,text="Rs. 10,000/-",bg="Sky Blue1",fg="red",font="Helvetica 13 bold")
                # label12.grid(row=4,column=0,columnspan=2,pady=15)               
        w=1010
        h=650
        ws = root4.winfo_screenwidth()
        hs = root4.winfo_screenheight() 
        x = (ws/2) - (w/2)
        # y = (hs/2) - (h/2)
        root4.geometry('%dx%d+%d+%d' % (w, h, x, 0))
        # root4.maxsize(1075,650)
        # root4.minsize(1075,650)  
        Label(root4,text="Plz. consider the proviso of No. 10 of schedule I of this act.:-",borderwidth=6,relief=SUNKEN,fg="red",font="Helvetica 11 bold",bg="khaki1").grid(row=5,column=0,pady=30,sticky=W,padx=50)
        Label(root4,text="Provided that when, after the grant of certificate under the Indian Succession Act, 1925 (39 of\n1925), in  respect of any property included in an estate, a grant of probate or letters of\nadministration is made in respect of the same estate, the fee payable in respect of the latter\ngrant shall be reduced by the amount of the fee paid in respect of the former grant.",font="Helvetica 12 bold",borderwidth=6,relief=SUNKEN,fg="yellow",bg="navy").grid(row=6,column=0,columnspan=2,sticky=W,padx=50)
        Label(root4,text="The W.B Court Fees (Amendment) Act, 2002",borderwidth=6,relief=SUNKEN,bg="yellow",font="Helvetica 13 bold").grid(row=0,column=0,columnspan=2,pady=25)
        Label(root4,text="Know the amount of ad valorem Court Fees leviable on probate case or L.A\nwith or without will annexed, as per the W.B C.F (Amendment) Act, 2002",borderwidth=6,relief=SUNKEN,bg="NavajoWhite2",font="Helvetica 15 bold",padx=10,fg="navy").grid(row=1,column=0,columnspan=2,padx=50,pady=10)  
        Label(root4,text="Enter value of property on which probate is granted",fg="blue2",font="Ariel 15 bold",bg="Sky Blue1").grid(row=2,column=0,columnspan=1)
        amount=IntVar()
        entry=Entry(root4,textvariable=amount,font="Helvetica 15 italic",width=12,borderwidth=6,relief=SUNKEN,fg="navy")
        entry.grid(row=2,column=1,pady=25)
        entry.focus()
        Button(root4,text="Get Result",font="Helvetica 12 bold",fg="white",bg="red4",command=press1).grid(row=3,column=0,columnspan=2,pady=25)
        root4.bind("<Return>",press2)
        root4.mainloop()

    label111=Label(root100)
    label122=Label(root100)   

    
    # f.grid(row=0,column=0)
    f2=Frame(root100,bg="dark Green",borderwidth=6,relief=RAISED)
    f2.grid(row=0,column=1,columnspan=2,padx=150,pady=10)
    f=Frame(root100,borderwidth=10,relief=RAISED,bg="navy")
    f.grid(row=1,column=1,columnspan=2,padx=40,pady=8)
    root100.resizable(False,False)
    Label(f2,text="LEGAL PRACTIONERS' ASSISTANT",padx=15,fg="red",font=" Ariel 12 bold",pady=5,bg="Yellow2").grid(row=0,column=0)
    # Label(root100,text="-: FOR CIVIL SUITS :-",fg="brown4",bg="light sky blue",font=("Goudy old style", 12,"bold")).place(x=240,y=240)
    Label(f,text="- : Developed by : -\n Sri Sayantan Chakraborty\n - : Legal advisor : -\n Advocate Sri Suman Chakraborty\n Ph. Nos. : - 9434 450 866 / 9126 264 166",bg="navy",fg="yellow",font="Helvetica 12 bold",padx=3).grid(row=0,column=0)
    Label(root100,text="-: KNOW THE AD VALOREM C.F FOR :-",fg="Blue2",bg="Sky Blue1",font=("Goudy old style", 12,"bold")).grid(row=2,column=1,columnspan=2)
    

    
    Button(root100,text="1. Instituition of Suit",font="Ariel 12",command=Court_Fees,padx=42,pady=10,bg="pale green",fg="red2",bd=8).grid(row=3,column=1,pady=10,columnspan=2)
    Button(root100,text="2. Sucession Certificate\n(New Filling)",font="Ariel 12",command=Succession1,padx=25,bg="pale green",fg="red2",bd=8).grid(row=4,column=1,pady=10,columnspan=2)
    Button(root100,text="3. Sucession Certificate\n(Additional Value)",font="Ariel 12",command=Succession2,padx=25,bg="pale green",fg="red2",bd=8).grid(row=5,column=1,pady=10,columnspan=2)
    Button(root100,text="4. Probate of a will",font="Ariel 12",command=probate,padx=45,pady=9,bg="pale green",fg="red2",bd=8).grid(row=6,column=1,pady=10,columnspan=2)
    
   
    root100.mainloop()                       