from tkinter import *
import tkinter.messagebox as tm
from testfile1 import tsc3
from tsc import calc
from testfile3 import Fees
import datetime as d
from I_P_C import IPC
from tkinter.tix import *
# import win10toast
# import notify2
d1=d.date(2030,6,30)
t3=d.date.today()
z3=(d1-t3).days
# from The_succession_Calculator import func
if z3==0 or z3<0:
    root56=Tk()
    w=675
    h=700
    ws = root56.winfo_screenwidth()
    hs = root56.winfo_screenheight() 
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root56.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root56.minsize(675,700)
    root56.maxsize(675,700)
    # f=Frame(root56,width=ws,height=hs).pack()
    Label(root56,text="Your license has expired",font="Helvetica 17 bold",fg="red").pack()
    Label(root56,text="- : Developed by : -\n Advocate Suman Chakraborty\n &\n Sayantan Chakraborty\n Ph. Nos. : - 9434 450 866 / 7908 375 185",bg="pink",fg="blue2",font="Helvetica 13 bold").pack()
    # f1=Frame(root56,bg="white").pack()
    Label(root56,text="Contact the developer \nfor assistance",fg="dark orange",font=("Goudy old style", 35,"bold"),bg="azure").pack()
    root56.mainloop()
else:
    root100=Tk()
    root100.configure(bg="light sky blue")
    root100.title("Legal Practioners' Assistant")
    root100.geometry("540x620")
    w=675
    h=700
    ws = root100.winfo_screenwidth()
    hs = root100.winfo_screenheight() 
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root100.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root100.minsize(675,700)
    root100.maxsize(650,700)
    # root100.geometry("{0}x{1}+0+0".format(root100.winfo_screenwidth(), root100.winfo_screenheight()))
    f=Frame(root100,borderwidth=3,relief=SUNKEN,bg="pink")
    f.grid(row=1,column=1,padx=60,pady=15)
    f2=Frame(root100,bg="yellow",borderwidth=6,relief=RAISED)
    f2.grid(row=0,column=1,pady=30,sticky=N)
    Label(f2,text="LEGAL PRACTIONERS' ASSISTANT",padx=15,fg="red",font=" Ariel 13 bold",pady=15,bg="yellow").grid(row=0,column=1)
    l1=Label(root100)
    l2=Label(root100)



    def g():
        global l1
        global l2
        root=Tk()
        l1=Label(root)
        l2=Label(root)
        w=1075
        h=500
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight() 
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        root.maxsize(1075,500)
        root.minsize(1075,500)
        root.title("The Indian Succession Calculator U/s. 374 of I. Succ. Act. 1925")    
        root.configure(bg="peach puff")
        # f = Frame(width="1075",height="500")
        # f.pack()
        # swin = ScrolledWindow(f, width=1075, height=500)
        # swin.pack(side=LEFT,fill=Y)
        # win = swin.window
        def result1():
            global l1
            global l2
            n1=money.get()
            n1=int(n1)
            # print(n1)
            ob=tsc3()
            tax1=ob.calculation(n1)     
            # print(tax1)
            r=str(round(tax1,2))   
            l2.destroy()
            l1.destroy()
            if tax1<50000:
                l2=Label(root,text="Court fees to be paid of",font="Helvetica 13 bold",fg="green",bg="peach puff")
                l2.place(x=338,y=400)
                l1=Label(root,text="Rs. "+r,fg="red",font="Helvetica 13 bold",bg="peach puff")
                l1.place(x=590,y=400)
            elif tax1>=50000:
                l2=Label(root,text="Maximum amount of Court fees to be paid of",font="Helvetica 13 bold",fg="green",bg="peach puff")
                l2.place(x=240,y=400)   
                l1=Label(root,text="Rs.50000.0 ",fg="red",font="Helvetica 13 bold",bg="peach puff")
                l1.place(x=700,y=400)
        t=Label(root,text="The Indian Succession Act 1925",borderwidth=6,relief=SUNKEN,bg="yellow",font="Helvetica 13 bold")
        t.place(x=370,y=30)
        Label(root,text="Know the exact amount of Ad valorem Court Fees to be levied, when the amount\n or value of any date or security specified in the certificate\n U/s. 374 of the act exceeds Rs.1,000/- (New Filing):-",bg="skyblue1",fg="red",font="Helvetica 13 bold",padx=10,borderwidth=6,relief=SUNKEN).place(x=110,y=110)
        Label(root,text="Enter the amount :",pady=10,font="Helvetica 15 bold",bg="peach puff",fg="blue").place(x=330,y=235)
        amount=IntVar()
        money=Entry(root,textvariable=amount,fg="blue",font=12,width=15)
        money.place(x=570,y=250)
        b=Button(root,text="Get result",fg="white",bg="red4",command=result1,font="Helvetica 13 bold")
        b.place(x=485,y=325)





    l3=Label(root100)
    l4=Label(root100)
    def h1():
        global l3
        global l4
        root5=Tk()
        l3=Label(root5)
        l4=Label(root5)
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
        # l1=Label(root5)
        # l2=Label(root5)
        def cal():
            global l3
            global l4
            t1=money2.get()
            t1=int(t1)
            obj=calc()
            tax2=obj.cal(t1)
            r2=str(round(tax2,2))
            l3.destroy()
            l4.destroy()
            if tax2<50000:
                l4=Label(root5,text="Court fees to be paid of",font="Helvetica 13 bold",fg="green",bg="LightGoldenrod1")
                l4.place(x=340,y=385)   
                l3=Label(root5,text="Rs. "+r2,fg="red",font="Helvetica 13 bold",bg="LightGoldenrod1")
                l3.place(x=590,y=385)
            elif tax2>=50000:
                l4=Label(root5,text="Maximum amount of Court fees to be paid of",font="Helvetica 13 bold",fg="green",bg="LightGoldenrod1")
                l4.place(x=240,y=385)   
                l3=Label(root5,text="Rs.50000.0 ",fg="red",font="Helvetica 13 bold",bg="LightGoldenrod1")
                l3.place(x=700,y=385)
        t=Label(root5,text="The Indian Succession Act 1925",borderwidth=6,relief=SUNKEN,bg="light pink",font="Helvetica 13 bold")
        t.place(x=350,y=30)
        Label(root5,text="Know the exact amount of Ad valorem Court Fees to be levied, when the aggregate amount\n or value of any date or security specified in the certificate and of any date or security \nhas been extended U/s. 376 of the act, exceeds Rs. 1,000/- :-",bg="skyblue1",fg="red",font="Helvetica 13 bold",borderwidth=6,relief=SUNKEN,padx=10).place(x=50,y=110)
        Label(root5,text="Enter the amount :",pady=10,font="Helvetica 15 bold",fg="blue",bg="LightGoldenrod1").place(x=305,y=235)
        amount2=IntVar()
        money2=Entry(root5,textvariable=amount2,fg="blue",font=12,width=15)
        money2.place(x=545,y=250)
        Button(root5,text="Get result",fg="white",bg="red4",command=cal,font="Helvetica 13 bold").place(x=455,y=315)



    lb1=Label(root100) 
    lb2=Label(root100)
    def i():
        global lb1
        global lb2
        root11=Tk()
        root11.title("The W.B Court-fees (Amendment) Act, 2002")
        root11.config(bg="khaki4")
        lb1=Label(root11) 
        lb2=Label(root11)
        def fees():
            global lb1
            global lb2
            o=t.get()
            o=int(o)
            obj1=Fees()
            z=obj1.calculation(o)
            lb1.destroy()
            lb2.destroy()
            if z<50000:
                lb1=Label(root11,text="Court Fees to be paid of ",fg="green",font="Helvetica 13 bold",bg="khaki4")
                lb1.place(x=375,y=365)
                lb2=Label(root11,text="Rs. "+str(z)+".0",fg="red",font="Helvetica 13 bold",bg="khaki4")
                lb2.place(x=630,y=365)
            elif z>=50000:
                lb1=Label(root11,text="Maximum amount of Court Fees to be paid of ",fg="green",font="Helvetica 13 bold",bg="khaki4")
                lb1.place(x=250,y=365)
                lb2=Label(root11,text="Rs.50000.0",fg="red",font="Helvetica 13 bold",bg="khaki4")
                lb2.place(x=715,y=365)    
        w=1070
        h=500
        ws = root11.winfo_screenwidth()
        hs = root11.winfo_screenheight() 
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        root11.geometry('%dx%d+%d+%d' % (w, h, x, y))
        # root11.minsize(675,700)
        root11.maxsize(1070,500)
        # root11.geometry("500x300")
        root11.minsize(1000,500)
        Label(root11,text="The W.B Court-fees (Amendment) Act, 2002",borderwidth=6,relief=SUNKEN,bg="yellow",font="Helvetica 13 bold").place(x=300,y=30)
        Label(root11,text="Know the rates of Ad valorem Court fees leviable on the institution of suits,\n as per the W.B Court-fees (Amendment) Act, 2002",borderwidth=6,relief=SUNKEN,bg="pink",font="Helvetica 13 bold",padx=10,fg="navy").place(x=140,y=110)
        Label(root11,text="Enter value of the subject matter of suit:",fg="blue",font="Helvetica 13 bold",bg="khaki4").place(x=215,y=220)
        value=IntVar()
        t=Entry(root11,textvariable=value,font="Helvetica 13 bold",width=15)
        t.place(x=650,y=220)
        Button(root11,text="Get Result",fg="white",bg="red4",font="Helvetica 13 bold",command=fees).place(x=480,y=290)
        root11.mainloop()



    def j():
        root12=Tk()
        w=1070
        h=500
        ws = root12.winfo_screenwidth()
        hs = root12.winfo_screenheight() 
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        root12.geometry('%dx%d+%d+%d' % (w, h, x, y))
        root12.maxsize(1000,500)
        root12.minsize(1000,500)
        root12.configure(bg="peach puff")
        section=IntVar()
        Label(root12,text="Enter the Section no.",fg="black",font="Ariel 15 bold",bg="peach puff").place(x=250,y=250)
        entry=Entry(root12,textvariable=section,font="Helvetica 15 bold")
        entry.place(x=525,y=250)
        def press():
            co_dict={298:['The person whose religious feelings are intended to be wounded',
                        'Uttering words, etc., with deliberate intent to wound the religious feelings of any person.'],
                    323:['The person to whom the hurt is caused',
                        'Voluntarily causing hurt.'],
                    334:['The person to whom the hurt is caused','Voluntarily causing hurt on provocation.'],
                    335:['The person to whom the hurt is caused','Voluntarily causing grievous hurt on grave and sudden provocation.'],
                    341:['The person restrained or confined','Wrongfully restraining or confining any person.'],
                    342:['The person restrained or confined','Wrongfully restraining or confining any person.'],
                    343:['The person confined','Wrongfully confining a person for three days or more.'],
                    344:['The person confined','Wrongfully confining a person for ten days or more.'],
                    346:['The person confined','Wrongfully confining a person in secret.'],
                    352:['The person assaulted or to whom criminal force is used','Assault or use of criminal force.'],
                    355:['The person assaulted or to whom criminal force is used','Assault or use of criminal force.'],
                    358:['The person assaulted or to whom criminal force is used','Assault or use of criminal force.'],
                    379:['The owner of the property stolen','Theft.'],
                    403:['The owner of the property misappropriated','Dishonest misappropriation of property.'],
                    407:['The owner of the property misappropriated','Criminal breach of trust by a carrier, wharfinger, etc.'],
                    411:['The owner of the property stolen','Dishonestly receiving stolen property knowing it to be stolen.'],
                    414:['The owner of the property stolen','Assisting in the concealment or disposal of stolen property, knowing it to be stolen.'],
                    417:['The person cheated','Cheating.'],
                    419:['The person cheated','Cheating by personation.'],
                    421:['The creditors who are affected thereby','Fraudulent removal or concealment of property, etc., to prevent distribution among creditors.'],
                    422:['The creditors who are affected thereby','Fraudulently preventing from being made available for his creditors a debt or demand due to the offender.'],
                    423:['The person affected thereby','Fraudulent execution of deed of transfer containing false statement of consideration.'],
                    424:['The person affected thereby','Fraudulent removal or concealment of property.'],
                    426:['The person to whom the loss or damage is caused','Mischief, when the only loss or damage caused is loss or damage to a private person.'],
                    427:['The person to whom the loss or damage is caused','Mischief, when the only loss or damage caused is loss or damage to a private person.'],
                    428:['The owner of the animal','Mischief by killing or maiming animal.'],
                    429:['The owner of the cattle or animal','Mischief by killing or maiming cattle, etc.'],
                    430:['The person to whom the loss or damage is caused',
                        'Mischief by injury to works of irrigation by wrongfully diverting water when the only loss or damage caused is loss or damage to private person.'],
                    447:['The person in possession of the property trespassed upon','Criminal trespass.'],
                    448:['The person in possession of the property trespassed upon','House-trespass.'],
                    451:['The person in possession of the house trespassed upon','House-trespass to commit an offence (other than theft) punishable with imprisonment.'],
                    482:['The person to whom loss or injury is caused by such use','Using a false trade or property mark.'],
                    483:['The person to whom loss or injury is caused by such use','Counterfeiting a trade or property mark used by another.'],
                    486:['The person to whom loss or injury is caused by such use',
                        'Knowingly selling, or exposing or possessing for sale or for manufacturing purpose, goods marked with a counterfeit property mark.'],
                    491:['The person with whom the offender has contracted','Criminal breach of contract of service.'],
                    497:['The husband of the woman','Adultery.'],
                    498:['The husband of the woman and the woman','Enticing or taking away or detaining with criminal intent a married woman.'],
                    500:['The person defamed',
                        'Defamation, except such cases as are specified against section 500 of the Indian Penal Code (45 of 1860) in column 1 of the Table under sub-section (2).'],
                    501:['The person defamed','Printing or engraving matter, knowing it to be defamatory.'],
                    502:['The person defamed','Sale of printed or engraved substance containing defamatory matter, knowing it to contain such matter.'],
                    504:['The person insulted','Insult intended to provoke a breach of the peace.'],
                    506:['The person intimidated','Criminal intimidation.'],
                    508:['The person induced','Inducing person to believe himself an object of divine displeasure.'],
                        }    
            co_dict2={312:['The woman to whom miscarriage is caused.','Causing miscarriage.'],
                    325:['The person to whom hurt is caused.','Voluntarily causing grievous hurt.'],
                    337:['The person to whom hurt is caused.','Causing hurt by doing an act so rashly and negligently as to safety of others.'],
                    338:['The person to whom hurt is caused.','Causing grievous hurt by doing an act so rashly and negligently as to endanger human life or the personal safety of others.'],
                    357:['The person assaulted or to whom the force was used.','Assault or criminal force in attempting wrongfully to confine a person.'],
                    381:['The owner of the property stolen.','Theft, by clerk or servant of property in possession of master.'],
                    406:['The owner of the property in respect of which the breach of trust has been committed.','Criminal breach of trust'],
                    408:['The owner of the property in respect of which the breach of trust has been committed.','Criminal breach of trust by a clerk or servant.'],
                    418:['The person cheated.','Cheating a person whose interest the offender was bound, either by law or by legal contract, to protect.'],
                    420:['The person cheated.','Cheating and dishonestly inducing delivery of property or the making, alteration or destruction of a valuable security.'],
                    494:['The husband or wife of the person so marrying.','Marrying again during the life-time of a husband or wife.'],
                    500:['The person defamed.','Defamation against the President or the Vice-President or the Governor of a State or the Administrator of a Union territory or a Minister in respect of his public functions when instituted upon a complaint made by the Public Prosecutor.'],
                    509:['The woman whom it was intended to insult or whose privacy was intruded upon.','Uttering words or sounds or making gestures or exhibiting any object intending to insult the modesty of a woman or intruding upon the privacy of a woman.']
                    }
            t=entry.get()
            t=int(t)
            s=False
            if t in co_dict.keys() or t in co_dict2.keys():  
                root13=Tk()
                if t in co_dict.keys():
                    for i,j in co_dict.items():
                        if t==i:
                            s=True
                            label1=Label(root13,text="Offence:-",fg="red",font="Helvetica 12 bold").place(x=0,y=0)
                            label2=Label(root13,text=j[1],fg="green").place(x=20,y=35)
                            label3=Label(root13,text='Person by whom offence may be compounded:-',fg='red',font="Helvetica 12 bold").place(x=0,y=60)
                            label4=Label(root13,text=j[0]+" according to section 320(1) of Cr.P.C. ").place(x=20,y=85)
                        else:
                            pass
                if t in co_dict2.keys():
                     for x,y in co_dict2.items():
                        if t==x and s==False:
                            label1=Label(root13,text="Offence:-",fg="red",font="Helvetica 12 bold").place(x=0,y=0)
                            label2=Label(root13,text=y[1],fg="green").place(x=20,y=35)
                            label3=Label(root13,text='Person by whom offence may be compounded:-',fg='red',font="Helvetica 12 bold").place(x=0,y=60)
                            label4=Label(root13,text=y[0]+" With the permission of the court as per section 320(2) of Cr.P.C. ").place(x=30,y=85)
                        elif t==x and s==True:
                            label1=Label(root13,text="Offence:-",fg="red",font="Helvetica 12 bold").place(x=0,y=95)
                            label2=Label(root13,text=y[1],fg="green").place(x=20,y=120)
                            label3=Label(root13,text='Person by whom offence may be compounded:-',fg='red',font="Helvetica 12 bold").place(x=0,y=145)
                            label4=Label(root13,text=y[0]+" With the permission of the court as per section 320(2) of Cr.P.C. ").place(x=30,y=175)
                root13.mainloop()
            else:
                root14=Tk()
                Label(root14,text="This offence is not compoundable according to section 320 of Cr.P.C.",fg="red4",font="Helvetica 18 bold").pack()
                root14.mainloop()
        Button(root12,text="Get details",font="Helvetica 12 bold",fg="white",bg="red4",command=press).place(x=450,y=300)
        root12.mainloop()


    def k():
        root9=Tk()
        w=1000
        h=500
        ws = root9.winfo_screenwidth()
        hs = root9.winfo_screenheight() 
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        root9.geometry('%dx%d+%d+%d' % (w, h, x, y))
        root9.maxsize(1000,500)
        root9.minsize(1000,500)
        def press():
            obj1=IPC()
            n=entry.get()
            obj1.check(n)
        root9.maxsize(1000,500)
        root9.minsize(1000,500)
        root9.configure(bg="peach puff")
        section=IntVar()
        Label(root9,text="Enter the Section no.",fg="black",font="Ariel 15 bold",bg="peach puff").place(x=250,y=250)
        entry=Entry(root9,textvariable=section,font="Helvetica 15 bold")
        entry.place(x=525,y=250)
        Button(root9,text="Get details",font="Helvetica 12 bold",fg="white",bg="red4",command=press).place(x=450,y=300)
    Label(f,text="- : Developed by : -\n Advocate Suman Chakraborty\n &\n Sayantan Chakraborty\n Ph. Nos. : - 9434 450 866 / 7908 375 185",bg="pink",fg="blue2",font="Helvetica 13 bold").grid(row=1,column=1,pady=5)
    Button(root100,text="Ad valorem C.F leviable for instituiton of Succession Case \nU/s. 374 of I.Succ.Act. in W.B.",font="Ariel 12",command=g,padx=13,pady=5,bg="pale green",fg="red2").grid(row=2,column=1,sticky=NW,padx=60,pady=5)
    Button(root100,text="Ad valorem C.F leviable to extend the amount of a \nSuccession Certificate U/s. 376 of I.Succ.Act. in W.B.",font="Ariel 12",command=h1,padx=33,pady=5,bg="pale green",fg="red2").grid(row=3,column=1,sticky=NW,padx=60,pady=5)
    Button(root100,text="Ad valorem C.F leviable for institution of suit in W.B.",font="Ariel 12",command=i,padx=41,pady=5,bg="pale green",fg="red2").grid(row=4,column=1,sticky=NW,padx=60,pady=5)
    Button(root100,text="Compoundable Offence U/s. 320 of Cr.P.C.",font="Ariel 12",command=j,pady=5,bg="pale green",fg="red2",padx=77).grid(row=5,column=1,sticky=NW,padx=60,pady=5)
    Button(root100,text="1st Schedule of Cr.P.C. I-Offences under the I.P.C.",font="Ariel 12",command=k,padx=42,pady=5,bg="pale green",fg="red2").grid(row=6,column=1,sticky=NW,padx=60,pady=5)
    root100.mainloop()