from tkinter import *
import tkinter.messagebox as tm
from testfile1 import tsc3
from tsc import calc
from testfile3 import Fees
import datetime as d
from I_P_C import IPC
# from tkinter.tix import *
from Probate import Probate
# from MVAct import motor_vehicles
# import win10toast
# import notify2
d1=d.date(2020,6,20)
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
    #f=Frame(root56,width=ws,height=hs).pack()
    Label(root56,text="Your license has expired",font="Helvetica 17 bold",fg="red").pack()
    Label(root56,text="- : Developed by : -\n Advocate Suman Chakraborty\n &\n Sayantan Chakraborty\n Ph. Nos. : - 9434 450 866 / 7908 375 185",bg="pink",fg="blue2",font="Helvetica 13 bold").pack()
    #f1=Frame(root56,bg="white").pack()
    Label(root56,text="Contact the developer \nfor assistance",fg="dark orange",font=("Goudy old style", 35,"bold"),bg="azure").pack()
    root56.mainloop()
else:
    root100=Tk()
    root100.configure(bg="light sky blue")
    root100.title("Legal Practioners' Assistant")
    root100.geometry("540x620")
    w=685
    h=700
    ws = root100.winfo_screenwidth()
    hs = root100.winfo_screenheight() 
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root100.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root100.minsize(685,700)
    root100.maxsize(685,700)
    # root100.geometry("{0}x{1}+0+0".format(root100.winfo_screenwidth(), root100.winfo_screenheight()))
    l1=Label(root100)
    l2=Label(root100)


    def Succession1():
        global l1
        global l2
        root=Tk()
        root.resizable(False,False)
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
        def result2(event):
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
        money=Entry(root,textvariable=amount,fg="blue",font=("Ariel",12,"bold"),width=15,borderwidth=6,relief=SUNKEN)
        money.place(x=570,y=250)
        b=Button(root,text="Get result",fg="white",bg="red4",command=result1,font="Helvetica 13 bold")
        b.place(x=485,y=325)
        root.bind("<Return>",result2)
        root.mainloop()




    l3=Label(root100)
    l4=Label(root100)
    def Succession2():
        global l3
        global l4
        root5=Tk()
        root5.resizable(False,False)
        l3=Label(root5)
        l4=Label(root5)
        root5.config(bg="MistyRose2")
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
        def cal1():
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
                l4=Label(root5,text="Court fees to be paid of",font="Helvetica 13 bold",fg="green",bg="MistyRose2")
                l4.place(x=340,y=385)   
                l3=Label(root5,text="Rs. "+r2,fg="red",font="Helvetica 13 bold",bg="MistyRose2")
                l3.place(x=590,y=385)
            elif tax2>=50000:
                l4=Label(root5,text="Maximum amount of Court fees to be paid of",font="Helvetica 13 bold",fg="green",bg="MistyRose2")
                l4.place(x=240,y=385)   
                l3=Label(root5,text="Rs.50000.0 ",fg="red",font="Helvetica 13 bold",bg="MistyRose2")
                l3.place(x=700,y=385)
        def cal2(event):
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
                l4=Label(root5,text="Court fees to be paid of",font="Helvetica 13 bold",fg="green",bg="MistyRose2")
                l4.place(x=340,y=385)   
                l3=Label(root5,text="Rs. "+r2,fg="red",font="Helvetica 13 bold",bg="MistyRose2")
                l3.place(x=590,y=385)
            elif tax2>=50000:
                l4=Label(root5,text="Maximum amount of Court fees to be paid of",font="Helvetica 13 bold",fg="green",bg="MistyRose2")
                l4.place(x=240,y=385)   
                l3=Label(root5,text="Rs.50000.0 ",fg="red",font="Helvetica 13 bold",bg="MistyRose2")
                l3.place(x=700,y=385)
        t=Label(root5,text="The Indian Succession Act 1925",borderwidth=6,relief=SUNKEN,bg="light pink",font="Helvetica 13 bold")
        t.place(x=350,y=30)
        Label(root5,text="Know the exact amount of Ad valorem Court Fees to be levied, when the aggregate amount\n or value of any date or security specified in the certificate and of any date or security \nhas been extended U/s. 376 of the act, exceeds Rs. 1,000/- :-",bg="pale turquoise",fg="red",font="Helvetica 13 bold",borderwidth=6,relief=SUNKEN,padx=10).place(x=50,y=110)
        Label(root5,text="Enter the amount :",pady=10,font="Helvetica 15 bold",fg="blue",bg="MistyRose2").place(x=305,y=235)
        amount2=IntVar()
        money2=Entry(root5,textvariable=amount2,fg="blue",font="Ariel 12 bold",width=15,borderwidth=6,relief=SUNKEN)
        money2.place(x=545,y=250)
        Button(root5,text="Get result",fg="white",bg="red4",command=cal1,font="Helvetica 13 bold").place(x=455,y=315)
        root5.bind("<Return>",cal2)
        root5.mainloop()


    lb1=Label(root100) 
    lb2=Label(root100)
    def Court_Fees():
        global lb1
        global lb2
        root11=Tk()
        root11.title("The W.B Court-fees (Amendment) Act, 2002")
        root11.config(bg="SlateGray2")
        lb1=Label(root11) 
        lb2=Label(root11)
        root11.resizable(False,False)
        def fees1():
            global lb1
            global lb2
            o=t.get()
            o=int(o)
            obj1=Fees()
            z=obj1.calculation(o)
            lb1.destroy()
            lb2.destroy()
            if z<50000:
                lb1=Label(root11,text="Court Fees to be paid of ",fg="green",font="Helvetica 13 bold",bg="SlateGray2")
                lb1.place(x=375,y=365)
                lb2=Label(root11,text="Rs. "+str(z)+".0",fg="red",font="Helvetica 13 bold",bg="SlateGray2")
                lb2.place(x=630,y=365)
            elif z>=50000:
                lb1=Label(root11,text="Maximum amount of Court Fees to be paid of ",fg="green",font="Helvetica 13 bold",bg="SlateGray2")
                lb1.place(x=250,y=365)
                lb2=Label(root11,text="Rs.50000.0",fg="red",font="Helvetica 13 bold",bg="SlateGray2")
                lb2.place(x=715,y=365) 
        def fees2(event):
            global lb1
            global lb2
            o=t.get()
            o=int(o)
            obj1=Fees()
            z=obj1.calculation(o)
            lb1.destroy()
            lb2.destroy()
            if z<50000:
                lb1=Label(root11,text="Court Fees to be paid of ",fg="green",font="Helvetica 13 bold",bg="SlateGray2")
                lb1.place(x=375,y=365)
                lb2=Label(root11,text="Rs. "+str(z)+".0",fg="red",font="Helvetica 13 bold",bg="SlateGray2")
                lb2.place(x=630,y=365)
            elif z>=50000:
                lb1=Label(root11,text="Maximum amount of Court Fees to be paid of ",fg="green",font="Helvetica 13 bold",bg="SlateGray2")
                lb1.place(x=250,y=365)
                lb2=Label(root11,text="Rs.50000.0",fg="red",font="Helvetica 13 bold",bg="SlateGray2")
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
        Label(root11,text="Enter value of the subject matter of suit:",fg="blue",font="Helvetica 13 bold",bg="SlateGray2").place(x=215,y=220)
        value=IntVar()
        t=Entry(root11,textvariable=value,font="Helvetica 13 bold",width=15,borderwidth=6,relief=SUNKEN)
        t.place(x=650,y=220)
        Button(root11,text="Get Result",fg="white",bg="red4",font="Helvetica 13 bold",command=fees1).place(x=480,y=290)
        root11.bind("<Return>",fees2)
        root11.mainloop()



    def Compoundable_Offence():
        root12=Tk()
        w=1070
        h=500
        root12.resizable(False,False)
        ws = root12.winfo_screenwidth()
        hs = root12.winfo_screenheight() 
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        root12.geometry('%dx%d+%d+%d' % (w, h, x, y))
        root12.maxsize(1000,500)
        root12.minsize(1000,500)
        root12.configure(bg="LavenderBlush3")
        section=IntVar()
        #f=Frame(root12,width=100,height=20).place(x=50,y=50)
        Label(root12,text="   Code of Criminal Procedure 1973   ",relief=SUNKEN,borderwidth=6,font="Helvetica 15 bold",fg="red",bg="navy").place(x=280,y=50)
        Label(root12,text="Know about the offence of I.P.C., whether is it compoundable or not? \nU/s. 320 of Cr.P.C :-",bg="khaki3",fg="red4",font="Helvetica 13 bold",padx=10,borderwidth=6,relief=SUNKEN).place(x=135,y=130)
        Label(root12,text="Enter the Section no.",fg="black",font="Ariel 15 bold",bg="LavenderBlush3").place(x=250,y=250)
        entry=Entry(root12,textvariable=section,font="Helvetica 15 bold",width=10,borderwidth=6,relief=SUNKEN)
        entry.place(x=525,y=250)
        def press1():
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
                    407:['The owner of the property in respect of which the breach of trust has been committed','Criminal breach of trust by a carrier, wharfinger, etc.'],
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
                    337:['The person to whom hurt is caused.','Causing hurt by doing an act so rashly and negligently as to endanger human life or the personal safety of others.'],
                    338:['The person to whom hurt is caused.','Causing grievous hurt by doing an act so rashly and negligently as to endanger human life or the personal safety of others.'],
                    357:['The person assaulted or to whom the force was used.','Assault or criminal force in attempting wrongfully to confine a person.'],
                    381:['The owner of the property stolen.','Theft, by clerk or servant of property in possession of master.'],
                    406:['The owner of property in respect of which breach of trust has been committed.','Criminal breach of trust.'],
                    408:['The owner of property in respect of which breach of trust has been committed.','Criminal breach of trust by a clerk or servant.'],
                    418:['The person cheated.','Cheating a person whose interest the offender was bound, either by law or by legal contract, to protect.'],
                    420:['The person cheated.','Cheating and dishonestly inducing delivery of property or the making, alteration or destruction of a valuable security.'],
                    494:['The husband or wife of the person so marrying.','Marrying again during the life-time of a husband or wife.'],
                    500:['The person defamed.','Defamation against the President or the Vice-President or the Governor of a State or the Administrator of a Union territory or a Minister in respect of his public functions when instituted upon a complaint made by the Public Prosecutor.'],
                    509:['The woman whom it was intended to insult or whose privacy was intruded upon.','Uttering words or sounds or making gestures or exhibiting any object intending to insult the modesty of a woman or intruding upon the privacy of a woman.']
                    }
        def press2(event):
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
                    407:['The owner of the property in respect of which the breach of trust has been committed','Criminal breach of trust by a carrier, wharfinger, etc.'],
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
                    337:['The person to whom hurt is caused.','Causing hurt by doing an act so rashly and negligently as to endanger human life or the personal safety of others.'],
                    338:['The person to whom hurt is caused.','Causing grievous hurt by doing an act so rashly and negligently as to endanger human life or the personal safety of others.'],
                    357:['The person assaulted or to whom the force was used.','Assault or criminal force in attempting wrongfully to confine a person.'],
                    381:['The owner of the property stolen.','Theft, by clerk or servant of property in possession of master.'],
                    406:['The owner of property in respect of which breach of trust has been committed.','Criminal breach of trust.'],
                    408:['The owner of property in respect of which breach of trust has been committed.','Criminal breach of trust by a clerk or servant.'],
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
                root13.resizable(False,False)
                root13.config(bg="gray30")
                root13.geometry("1250x500")
                root13.resizable(False,False)
                # root13.geometry("{0}x{1}+0+0".format(root13.winfo_screenwidth(), root13.winfo_screenheight()))
                if t in co_dict.keys():
                    for i,j in co_dict.items():
                        if t==i:
                            s=True
                            label1=Label(root13,text="Offence U/s. "+str(t)+" of I.P.C :-",fg="red",font="Helvetica 12 bold",bg="gray30").place(x=20,y=20)
                            label2=Label(root13,text=j[1],wraplengt=1200,fg="yellow",font=(("Goudy old style"),15,"bold"),justify=LEFT,bg="gray30").place(x=40,y=55)
                            label3=Label(root13,text='Person by whom offence may be compounded:-',fg='red',font="Helvetica 12 bold",bg="gray30").place(x=20,y=140)
                            label4=Label(root13,wraplengt=1200,text=j[0]+". Compoundable according to section 320(1) of Cr.P.C. ",bg="gray30",font=(("Goudy old style"),15,"bold"),fg="lawn green",justify=LEFT).place(x=40,y=165)
                        else:
                            pass
                if t in co_dict2.keys():
                     for x,y in co_dict2.items():
                        if t==x and s==False:
                            label1=Label(root13,text="Offence U/s. "+str(t)+" of I.P.C :-",fg="red",font="Helvetica 12 bold",bg="gray30").place(x=20,y=20)
                            label2=Label(root13,text=y[1],fg="yellow",font=(("Goudy old style"),15,"bold"),wraplengt=1200,justify=LEFT,bg="gray30").place(x=40,y=55)
                            label3=Label(root13,text='Person by whom offence may be compounded:-',fg='red',font="Helvetica 12 bold",bg="gray30").place(x=20,y=150)
                            label4=Label(root13,justify=LEFT,wraplengt=1200,text=y[0]+" Compoundable with the permission of the Ld. Court, as per section 320(2) of Cr.P.C. ",bg="gray30",font=(("Goudy old style"),15,"bold"),fg="lawn green").place(x=50,y=175)
                        elif t==x and s==True:
                            label1=Label(root13,text="Offence U/s. "+str(t)+" of I.P.C :-",fg="red",font="Helvetica 12 bold",bg="gray30").place(x=20,y=250)
                            label2=Label(root13,wraplengt=1200,text=y[1],fg="yellow",font=(("Goudy old style"),15,"bold"),justify=LEFT,bg="gray30").place(x=40,y=285)
                            label3=Label(root13,text='Person by whom offence may be compounded:-',fg='red',font="Helvetica 12 bold",bg="gray30").place(x=20,y=400)
                            label4=Label(root13,wraplengt=1200,text=y[0]+" Compoundable with the permission of the Ld. Court, as per section 320(2) of Cr.P.C. ",justify=LEFT,font=(("Goudy old style"),15,"bold"),bg="gray30",fg="lawn green").place(x=50,y=430)
                root13.mainloop()
            else:
                root14=Tk()
                Label(root14,text="This offence is not compoundable according to section 320 of Cr.P.C.",fg="red4",font="Helvetica 18 bold").pack()
                root14.mainloop()
        Button(root12,text="Get details",font="Helvetica 12 bold",fg="white",bg="red4",command=press1).place(x=450,y=350)
        root12.bind("<Return>",press2)
        root12.mainloop()
    label11=Label(root100)
    label12=Label(root100)
    def probate():
        global label11
        global label12
        root4=Tk()
        root4.config(bg="Lightblue2")
        label11=Label(root4)
        label12=Label(root4)
        root4.resizable(False,False)
        def press1():
            # print("Hi")
            global label11
            global label12
            ob=Probate()
            n=entry.get()
            n=int(n)
            z=ob.calculation(n)
            label11.destroy()
            label12.destroy()
            label11=Label(root4,text="Court Fees to be paid of ",fg="green",font="Helvetica 13 bold",bg="Lightblue2")
            label11.place(x=355,y=340)
            label12=Label(root4,text="Rs. "+z,fg="red",font="Helvetica 13 bold",bg="Lightblue2")
            label12.place(x=610,y=340)
        def press2(event):
            # print("Hi")
            global label11
            global label12
            ob=Probate()
            n=entry.get()
            n=int(n)
            z=ob.calculation(n)
            label11.destroy()
            label12.destroy()
            label11=Label(root4,text="Court Fees to be paid of ",fg="green",font="Helvetica 13 bold",bg="Lightblue2")
            label11.place(x=355,y=340)
            label12=Label(root4,text="Rs. "+z,fg="red",font="Helvetica 13 bold",bg="Lightblue2")
            label12.place(x=610,y=340)
        w=1075
        h=650
        ws = root4.winfo_screenwidth()
        hs = root4.winfo_screenheight() 
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        root4.geometry('%dx%d+%d+%d' % (w, h, x, y))
        root4.maxsize(1075,650)
        root4.minsize(1075,650)  
        Label(root4,text="Plz. consider the proviso of No. 10 of schedule I of this act.:-",borderwidth=6,relief=SUNKEN,fg="red",font="Helvetica 12 bold",bg="khaki1").place(x=90,y=410)
        Label(root4,text="Provided that when, after the grant of certificate under the Indian Succession Act, 1925\n(39 of 1925), in respect of any property included in an estate, a grant of probate or\nletters of administration is made in respect of the same estate, the fee payable in respect\nof the latter grant shall be reduced by the amount of the fee paid in respect of the former grant.",font="Helvetica,15,bold",borderwidth=6,relief=SUNKEN,fg="yellow",bg="navy").place(x=90,y=465)
        Label(root4,text="The W.B Court-fees (Amendment) Act, 2002",borderwidth=6,relief=SUNKEN,bg="yellow",font="Helvetica 13 bold").place(x=300,y=30)
        Label(root4,text="Know the rates of Ad valorem Court fees leviable on the institution of probate case,\n as per the W.B Court-fees (Amendment) Act, 2002",borderwidth=6,relief=SUNKEN,bg="pink",font="Helvetica 13 bold",padx=10,fg="navy").place(x=95,y=110)     
        Label(root4,text="Enter the amount",fg="black",font="Ariel 15 bold",bg="Lightblue2").place(x=294,y=210)
        amount=IntVar()
        entry=Entry(root4,textvariable=amount,font="Helvetica 15 bold",width=12,borderwidth=6,relief=SUNKEN)
        entry.place(x=570,y=210)
        Button(root4,text="Get Result",font="Helvetica 12 bold",fg="white",bg="red4",command=press1).place(x=470,y=280)
        root4.bind("<Return>",press2)
        root4.mainloop()
    def Second_schedule():
        root30=Tk()
        # root30.config(bg="gray30")
        root30.title("1st Schedule of Cr.P.C regarding offences against other laws")
        canvas_width=1260
        canvas_height=600
        root30.geometry(f"{canvas_width}x{canvas_height}")
        canvas1=Canvas(root30,width=canvas_width,height=canvas_height,bg="gray30")
        canvas1.pack()
        canvas1.create_line(0,80,canvas_width,80,width=3,fill="white")
        canvas1.create_line(0,160,canvas_width,160,width=3,fill="white")
        # canvas1.create_line(60,30,60,canvas_height)
        canvas1.create_line(520,80,520,canvas_height,width=3,fill="white")
        canvas1.create_line(780,80,780,canvas_height,width=3,fill="white")
        canvas1.create_line(1040,80,1040,canvas_height,width=3,fill="white")
        # canvas1.create_line(1000,30,1000,canvas_height)
        Label(root30,bg="gray30",text="Offence",fg="pink",font=(("Goudy old style"),15,"bold")).place(x=210,y=95)
        Label(root30,bg="gray30",text="Cognizable or\nnon-cognizable",fg="pink",font=(("Goudy old style"),15,"bold")).place(x=570,y=86)
        Label(root30,bg="gray30",text="Bailable or\nnon-bailable",fg="pink",font=(("Goudy old style"),15,"bold")).place(x=840,y=86)
        Label(root30,bg="gray30",text="By what Court\ntriable",fg="pink",font=(("Goudy old style"),15,"bold")).place(x=1070,y=86)

        root30.resizable(False,False)
        # frame30=Frame(root30,width=100,height=20).pack(anchor="n")
        frame31=Label(root30,bg="gray30",text="II. CLASSIFICATION OF OFFENCES AGAINST OTHER LAWS",font=(("Goudy old style"),15,"bold"),fg="pink")
        frame31.place(x=270,y=20)
        Label(root30,bg="gray30",justify=LEFT,text="If punishable with death, imprisonment\nfor life, or imprisonment for more than\n7 years.",fg="yellow",font=(("Goudy old style"),15,"bold")).place(x=50,y=170)
        Label(root30,bg="gray30",text="Cognizable",fg="red",font=(("Goudy old style"),15,"bold")).place(x=590,y=175)
        Label(root30,bg="gray30",text="Non-bailable",font=(("Goudy old style"),15,"bold"),fg="red").place(x=840,y=175)
        Label(root30,bg="gray30",text="Court of Session",font=(("Goudy old style"),15,"bold"),fg="red").place(x=1060,y=175)
        Label(root30,bg="gray30",text="If punishable with imprisonment for\n3 years, and upwards but not more than\n7 years.",fg="yellow",font=(("Goudy old style"),15,"bold"),justify=LEFT).place(x=50,y=315)
        Label(root30,bg="gray30",text="Non-bailable",font=(("Goudy old style"),15,"bold"),fg="red").place(x=840,y=325)
        Label(root30,bg="gray30",text="Cognizable",fg="red",font=(("Goudy old style"),15,"bold")).place(x=590,y=325)
        Label(root30,bg="gray30",text="Magistrate of the\nfirst class",fg="lawn green",font=(("Goudy old style"),15,"bold")).place(x=1060,y=325)
        Label(root30,bg="gray30",text="If punishable with imprisonment for less\nthan 3 years or with fine only.",fg="yellow",font=(("Goudy old style"),15,"bold"),justify=LEFT).place(x=50,y=465)
        Label(root30,bg="gray30",justify=LEFT,text="Non-cognizable",fg="lawn green",font=(("Goudy old style"),15,"bold")).place(x=570,y=475)
        Label(root30,bg="gray30",text="Bailable",font=(("Goudy old style"),15,"bold"),fg="lawn green").place(x=865,y=475)
        Label(root30,bg="gray30",text="Any Magistrate",font=(("Goudy old style"),15,"bold"),fg="lawn green").place(x=1070,y=475)


        root30.mainloop()

    label111=Label(root100)
    label122=Label(root100)
    c=0
    def accident():
        dict_act1={"177":["General provision for punishment of offences.","If no penalty is provided for the offence, shall be punishable for the first offence with fine which may extend to Rs. 100/- and for any second or subsequent offence with fine which may extend to Rs. 300/-."],
        "178":["Penalty for travelling without pass or ticket and for dereliction of duty on the part of conductor and refusal to ply contract carriage, etc.","1) Shall be punishable with fine, which may extend to Rs. 500/-."],
        
        "179":["Disobedience of orders, obstruction and refusal of information.","(1) If no other penalty is provided for the offence, shall be punishable with fine, which may extend to Rs. 500/-."],
        
        "180":["Allowing unauthorised persons to drive vehicles.","Shall be punishable with imprisonment for a term which may extend to THREE MONTHS, or with fine which may extend to Rs. 1000/-, or with both."],
        "181":["Driving vehicles in contravention of section 3 or section 4.","Shall be punishable with imprisonment for a term which may extend to THREE MONTHS, or with fine which may extend to Rs. 500/-, or with both."],
        "182":["Offences relating to licences.","1) Shall be punishable with imprisonment for a term which may extend to THREE MONTHS, or with fine which may extend to Rs. 500/-, or with both and any driving licence so obtained by him shall be of no effect."],
        "182A":["Punishment for offences relating to construction and maintenance of vehicles.","Shall be punishable with fine of Rs. 1,000/- for the first offence and with a fine of Rs. 5,000/- for any subsequent offences."],
        "183":["Driving at excessive speed, etc.","(1) Shall be punishable with fine which may extend to Rs. 400/-, if having been previously convicted of an offence under this sub-section is again convicted of an offence under this sub-section, with fine which may extend to Rs. 1,000/-."],
        "184":["Driving dangerously.","Shall be punishable for the first offence with imprisonment for a term which may extend to SIX MONTHS or with fine which may extend to Rs. 1,000./- and for any second or subsequent offence if committed within THREE YEARS of the commission of a previous similar offence with imprisonment for a term which may extend to TWO YEARS, or with fine which may extend to Rs. 2,000/- or with both."],
        "185":["Driving by a drunken person or by a person under the influence of drugs.","Shall be punished for the first offence with imprisonment for a term which may extend to SIX MONTHS, or with fine which may extend to Rs. 2,000/-, or with both; and for a second or subsequent offence, if committed within three  years of the commission of the pervious similar offence, with imprisonment for a term which may extend to TWO YEARS, or with fine, which may extend to of Rs. 3,000/- or with both."],
        "186":["Driving when mentally or physically unfit to drive.","Shall be punishable for the first offence with fine which may extend to Rs. 200/-and for a second or subsequent offence with fine which may extend to Rs. 500/-."],
        "187":["Punishment for offences relating to accident.","Shall be punishable with imprisonment for a term which may extend to THREE MONTHS, or with fine which may extend to Rs. 500/-, or with both, if having been previously convicted of an offence under this section, he is again convicted of an offence under this section, with imprisonment for a term which may extend to SIX MONTHS, or with fine which may extend to Rs. 1,000/-, or with both."],
        "188":["Punishment for abetment of certain offences.","Shall be punishable with the punishment provided for the offence."],
        "189":["Racing and trials of speed.","Shall be punishable with imprisonment for a term which may extend to ONE MONTH, or with a fine which may extend to Rs. 500/-, or with both."],
        "190":["Using vehicle in unsafe condition.","(1) Shall be punishable with fine which may extend to Rs. 250/- or, if as a result of such defect an accident is caused causing bodily injury or damage to property, with imprisonment for a term which may extend to THREE MONTHS, or with fine which may extend to Rs. 1,000/- or with both."],
        
        "191":["Sale of vehicle in or alteration of vehicle to condition contravening this Act.","Shall be punishable with fine which may extend to Rs. 500/-"],
        "192":["Using vehicle without registration.","Shall be punishable for the first offence with a fine which may extend to Rs. 5,000/- but shall not be less than Rs. 2,000/-, for the second or subsequent offence with imprisonment which may extend to ONE YEAR or with fine which may extend to Rs. 10,000/- but shall not be less than Rs. 5,000/- or with both."],
        "192A":["Using vehicle without permit.", "Shall be punishable for the first offence with a fine which may extend to Rs. 5,000/- but shall not be less than Rs. 2,000/- and for any subsequent offence with imprisonment which may extend to ONE YEAR but shall not be less than THREE MONTHS or with fine which may extend to Rs. 10,000/- but shall not be less than Rs. 5,000/- or with both."],
        "193":["Punishment of agents and canvasser without proper authority.","Shall be punishable for the first offence with fine which may extend to Rs. 1000/- and for any second or subsequent offence with imprisonment which may extend to SIX MONTHS, or with fine which may extend to Rs. 2,000/-, or with both."],
        "194":["Driving vehicle exceeding permissible weight.","(1) Shall be punishable with minimum fine of Rs. 2,000/- and an additional amount of Rs. 1,000/- per tonne of excess load, together with the liability to pay charges for off-loading of the excess load."],
        
        "196":["Driving uninsured vehicle.","Shall be punishable with imprisonment which may extend to THREE MONTHS, or with  fine which may extend to Rs. 1,000/-  or with both."],
        "197":["Taking vehicle without authority.","(1) Shall be punishable with imprisonment which may extend to THREE MONTHS, or with  fine which may extend to Rs. 500/-  or with both."],
        
        "198":["Unauthorised interference with vehicle.","Shall be punishable with a fine which may extend to Rs. 100/-."],
        "201":["Penalty for causing obstruction to free flow to traffic.","Shall be liable for penalty up to RS. 50/- PER HOUR, so long as it remains in that position."],
        }
        dict_act2={"178":["Penalty for travelling without pass or ticket and for dereliction of duty on the part of conductor and refusal to ply contract carriage, etc.","2) Shall be punishable with fine, which may extend to Rs. 500/-."],
                "179":["(2) Disobedience of orders, obstruction and refusal of information.","(2) If no other penalty is provided for the offence, shall be punishable with imprisonment for a term which may extend to ONE MONTH, or with fine which may extend to Rs. 500/- or with both."],
                "182":["Offence relating to licenses.","2) Shall be punishable with imprisonment for a term which may extend to ONE MONTH, or with fine which may extent to Rs. 100/-, or with both, and any conductor’s licence so obtained by him shall be of no effect."],
                "183":["Driving at excessive speed, etc.","(2) Shall be punished with fine, which may extend to Rs. 300/-, or if having been previously convicted of an offence under this sub-section, is again convicted of an offence under this sub-section, with fine which may extend to Rs. 500/-."],
                "190":["Using vehicle in unsafe condition.","(2) Shall be punishable for the first offence with a fine of Rs. 1,000/- and for any second or subsequent offence with a fine of Rs. 2,000/-."],
                "194":["Driving vehicle exceeding permissible weight.","(2) Shall be punishable with fine which may extend to Rs. 3,000/-."],
                "197":["Taking vehicle without authority.","(2) Shall be punishable, with imprisonment which may extend to THREE MONTHS, or with fine which may extend to Rs. 500/- or with both."]               
                }
        dict_act3={"178":["Penalty for travelling without pass or ticket and for dereliction of duty on the part of conductor and refusal to ply contract carriage, etc.","3) (a) Shall be punishable with fine, which may extend to Rs. 50/- in case of two-wheeled or three-wheeled motor vehicles and (b) Shall be punishable with fine which may extend to Rs. 200/- in any other case."],
                "190":["Using vehicle in unsafe condition.","(3) Shall be punishable for the first offence which may extend to of Rs. 3,000/-, or with imprisonment for a term which may extend to ONE YEAR or with both and for any second or subsequent offence with fine which may extend to Rs. 5,000/- or with imprisonment for a term which may extend to THREE YEARS, or with both."],
                }
        global label111
        global label122
        root14=Tk()
        root14.config(bg="Pale Turquoise4")
        label111=Label(root14)
        label122=Label(root14)
        section1=StringVar()
        root14.resizable(False,False)
        Label(root14,text="Enter the Section no.",fg="black",font="Ariel 15 bold",bg="Pale Turquoise4").place(x=330,y=230)
        def motorvehicelsact1():
            global label111
            global label122
            q=entry.get()
            t=str(q)
            global c
            if t in dict_act1.keys() or t in dict_act2.keys() or t in dict_act3.keys():  
                root25=Tk()
                root25.config(bg="gray30")
                root25.geometry("1325x500")
                root25.resizable(False,False)
                #root25.geometry("{0}x{1}+0+0".format(root25.winfo_screenwidth(), root25.winfo_screenheight()))
                if t in dict_act1.keys():
                    for i,j in dict_act1.items():
                        if t==i:
                            s=True
                            c+=1
                            label1=Label(root25,text="Offence U/s. "+t+" of M.V Act 1988 :-",fg="red",font="Helvetica 12 bold",bg="gray30").pack(anchor="w",pady=15,padx=25)
                            label2=Label(root25,text=j[0],wraplengt=1200,fg="yellow",font=(("Goudy old style"),15,"bold"),justify=LEFT,bg="gray30").pack(anchor="w",padx=65)
                            label3=Label(root25,text='Penalties:-',fg='red',font="Helvetica 12 bold",bg="gray30").pack(anchor="w",pady=10,padx=25)
                            label4=Label(root25,wraplengt=1200,text=j[1],bg="gray30",font=(("Goudy old style"),15,"bold"),fg="lawn green",justify=LEFT).pack(anchor="w",padx=65,pady=10)
                if t in dict_act2.keys():
                     for x,y in dict_act2.items():                           
                        if t==x and c>=1:
                            label114=Label(root25,wraplengt=1200,text=y[1],justify=LEFT,font=(("Goudy old style"),15,"bold"),bg="gray30",fg="lawn green").pack(anchor="w",padx=65,pady=10)
                        elif t==x and c==0:
                            c+=1
                            label111=Label(root25,text="Offence:-",fg="red",font="Helvetica 12 bold",bg="gray30").pack(anchor="w",pady=15,padx=25)
                            label112=Label(root25,wraplengt=1200,text=y[0],fg="yellow",font=(("Goudy old style"),15,"bold"),justify=LEFT,bg="gray30").pack(anchor="w",padx=65)
                            label113=Label(root25,text='Penalties:-',fg='red',font="Helvetica 12 bold",bg="gray30").pack(anchor="w",pady=10,padx=25)
                            label114=Label(root25,wraplengt=1200,text=y[1],justify=LEFT,font=(("Goudy old style"),15,"bold"),bg="gray30",fg="lawn green").pack(anchor="w",padx=65,pady=10)

                if t in dict_act3.keys():
                     for a,b in dict_act3.items():                          
                        if t==a and c>=1:
                            label114=Label(root25,wraplengt=1200,text=b[1],justify=LEFT,font=(("Goudy old style"),15,"bold"),bg="gray30",fg="lawn green").pack(anchor="w",padx=65,pady=10)
                        elif t==a and c==0:
                            c+=1
                            label111=Label(root25,text="Offence:-",fg="red",font="Helvetica 12 bold",bg="gray30").pack(anchor="w",pady=15,padx=25)
                            label112=Label(root25,wraplengt=1200,text=b[0],fg="yellow",font=(("Goudy old style"),15,"bold"),justify=LEFT,bg="gray30").pack(anchor="w",padx=65)
                            label113=Label(root25,text='Penalties:-',fg='red',font="Helvetica 12 bold",bg="gray30").pack(anchor="w",pady=10,padx=25)
                            label114=Label(root25,wraplengt=1200,text=b[1],justify=LEFT,font=(("Goudy old style"),15,"bold"),bg="gray30",fg="lawn green").pack(anchor="w",padx=65,pady=10)
                root25.mainloop()
        def motorvehicelsact2(event):
            global label111
            global label122
            q=entry.get()
            t=str(q)
            global c
            if t in dict_act1.keys() or t in dict_act2.keys() or t in dict_act3.keys():  
                root25=Tk()
                root25.config(bg="gray30")
                root25.geometry("1325x500")
                root25.resizable(False,False)
                #root25.geometry("{0}x{1}+0+0".format(root25.winfo_screenwidth(), root25.winfo_screenheight()))
                if t in dict_act1.keys():
                    for i,j in dict_act1.items():
                        if t==i:
                            s=True
                            c+=1
                            label1=Label(root25,text="Offence U/s. "+t+" of M.V Act 1988 :-",fg="red",font="Helvetica 12 bold",bg="gray30").pack(anchor="w",pady=15,padx=25)
                            label2=Label(root25,text=j[0],wraplengt=1200,fg="yellow",font=(("Goudy old style"),15,"bold"),justify=LEFT,bg="gray30").pack(anchor="w",padx=65)
                            label3=Label(root25,text='Penalties:-',fg='red',font="Helvetica 12 bold",bg="gray30").pack(anchor="w",pady=10,padx=25)
                            label4=Label(root25,wraplengt=1200,text=j[1],bg="gray30",font=(("Goudy old style"),15,"bold"),fg="lawn green",justify=LEFT).pack(anchor="w",padx=65,pady=10)
                if t in dict_act2.keys():
                     for x,y in dict_act2.items():                           
                        if t==x and c>=1:
                            label114=Label(root25,wraplengt=1200,text=y[1],justify=LEFT,font=(("Goudy old style"),15,"bold"),bg="gray30",fg="lawn green").pack(anchor="w",padx=65,pady=10)
                        elif t==x and c==0:
                            c+=1
                            label111=Label(root25,text="Offence:-",fg="red",font="Helvetica 12 bold",bg="gray30").pack(anchor="w",pady=15,padx=25)
                            label112=Label(root25,wraplengt=1200,text=y[0],fg="yellow",font=(("Goudy old style"),15,"bold"),justify=LEFT,bg="gray30").pack(anchor="w",padx=65)
                            label113=Label(root25,text='Penalties:-',fg='red',font="Helvetica 12 bold",bg="gray30").pack(anchor="w",pady=10,padx=25)
                            label114=Label(root25,wraplengt=1200,text=y[1],justify=LEFT,font=(("Goudy old style"),15,"bold"),bg="gray30",fg="lawn green").pack(anchor="w",padx=65,pady=10)

                if t in dict_act3.keys():
                     for a,b in dict_act3.items():                          
                        if t==a and c>=1:
                            label114=Label(root25,wraplengt=1200,text=b[1],justify=LEFT,font=(("Goudy old style"),15,"bold"),bg="gray30",fg="lawn green").pack(anchor="w",padx=65,pady=10)
                        elif t==a and c==0:
                            c+=1
                            label111=Label(root25,text="Offence:-",fg="red",font="Helvetica 12 bold",bg="gray30").pack(anchor="w",pady=15,padx=25)
                            label112=Label(root25,wraplengt=1200,text=b[0],fg="yellow",font=(("Goudy old style"),15,"bold"),justify=LEFT,bg="gray30").pack(anchor="w",padx=65)
                            label113=Label(root25,text='Penalties:-',fg='red',font="Helvetica 12 bold",bg="gray30").pack(anchor="w",pady=10,padx=25)
                            label114=Label(root25,wraplengt=1200,text=b[1],justify=LEFT,font=(("Goudy old style"),15,"bold"),bg="gray30",fg="lawn green").pack(anchor="w",padx=65,pady=10)
                root25.mainloop()
        t=Label(root14,text="The Motor Vehicles Act 1988",borderwidth=6,relief=SUNKEN,bg="IndianRed1",fg="navy",font="Helvetica 13 bold")
        t.place(x=370,y=40)
        Label(root14,text="Know the penalties against offences under M.V Act. 1988 (Old Act.)",bg="khaki1",fg="red",font="Helvetica 13 bold",padx=10,borderwidth=6,relief=SUNKEN).place(x=170,y=130)
        w=1075
        h=450
        ws = root14.winfo_screenwidth()
        hs = root14.winfo_screenheight() 
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        root14.geometry('%dx%d+%d+%d' % (w, h, x, y))
        root14.resizable(False,False)
        entry=Entry(root14,textvariable=section1,font="Helvetica 15 bold",width=10,borderwidth=6,relief=SUNKEN)
        entry.place(x=605,y=230)
        Button(root14,text="Get Result",font="Helvetica 12 bold",fg="white",bg="red4",command=motorvehicelsact1).place(x=470,y=320) 
        root14.bind("<Return>",motorvehicelsact2)
        root14.mainloop()
    def First_Schedule():
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
        def press1():
            obj1=IPC()
            n=entry.get()
            obj1.check(n)
        def press2(event):
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
        b1=Button(root9,text="Get details",font="Helvetica 12 bold",fg="white",bg="red4",command=press1)
        b1.place(x=450,y=300)
        root9.bind("<Return>",press2)
    f=Frame(root100,borderwidth=10,relief=RAISED,bg="navy")
    # f.grid(row=1,column=1,padx=60,pady=15)
    f.place(x=140,y=100,width=400,height=140)
    f2=Frame(root100,bg="dark Green",borderwidth=6,relief=RAISED)
    f2.place(x=150,y=30,width=380,height=50)
    root100.resizable(False,False)
    Label(f2,text="LEGAL PRACTIONERS' ASSISTANT",padx=15,fg="DarkOrange1",font=" Ariel 12 bold",pady=5,bg="dark Green").place(x=0,y=0)
    Label(root100,text="-: FOR CIVIL SUITS :-",fg="brown4",bg="light sky blue",font=("Goudy old style", 12,"bold")).place(x=240,y=240)
    Label(root100,text="-: KNOW THE AD VALOREM C.F FOR :-",fg="brown4",bg="light sky blue",font=("Goudy old style", 12,"bold")).place(x=150,y=270)
    Label(f,text="- : Developed by : -\n Advocate Sri Suman Chakraborty\n &\n Sri Sayantan Chakraborty\n Ph. Nos. : - 9434 450 866 / 7908 375 185",bg="navy",fg="yellow",font="Helvetica 12 bold").place(x=0,y=0)
    # Label(root100,text="1.",bg="light sky blue",font=("Goudy old style", 12,"bold")).place(x=50,y=300)
    Button(root100,text="1. For instituition of Suit",font="Ariel 12",command=Court_Fees,padx=41,pady=5,bg="pale green",fg="red2").place(x=50,y=305,width=268,height=60)
    Button(root100,text="2. Sucession Certificate\n(New Filling)",font="Ariel 12",command=Succession1,padx=13,pady=5,bg="pale green",fg="red2").place(x=370,y=305,height=60,width=265)
    Button(root100,text="3. Sucession Certificate\n(Additional Value)",font="Ariel 12",command=Succession2,padx=33,pady=5,bg="pale green",fg="red2").place(x=50,y=380,height=60,width=268)
    Button(root100,text="4. Probate of a will",font="Ariel 12",command=probate,padx=33,pady=5,bg="pale green",fg="red2").place(x=370,y=380,width=265,height=60)
    Label(root100,text="-: FOR CRIMINAL CASES :-",bg="light sky blue",fg="brown4",font=("Goudy old style", 12,"bold")).place(x=215,y=455)

    Button(root100,text="1. Compoundable Offence \nU/s. 320 of Cr.P.C.",font="Ariel 12",command=Compoundable_Offence,pady=5,bg="pale green",fg="red2",padx=77).place(x=50,y=495,width=268,height=60)
    Button(root100,text="2. 1st Schedule of Cr.P.C.\nOffences of The I.P.C.",font="Ariel 12",command=First_Schedule,padx=42,pady=5,bg="pale green",fg="red2").place(x=370,y=495,height=60,width=265)
    Button(root100,text="3. Penalties under \nM.V Act. 1988(Old Act.)",font="Ariel 12",command=accident,padx=42,pady=5,bg="pale green",fg="red2").place(x=50,y=570,height=60,width=268)
    Button(root100,text="4. 1st Schedule of Cr.P.C.\nOffences against other laws",font="Ariel 12",command=Second_schedule,padx=42,pady=5,bg="pale green",fg="red2").place(x=370,y=570,height=60,width=265)
    root100.mainloop()