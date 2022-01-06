from firebase import firebase
import subprocess
from tkinter import *
import datetime as d
# import mysql.connector as m
# from mysql.connector.locales.eng import client_error
import tkinter.messagebox as t
from tkinter.ttk import Combobox
root=Tk() 
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
     t.showinfo("Rate","Thanks for rating")
     root2.destroy()
    root2=Tk()
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
def update():
    pass
root.configure(bg="LightBlue2")
root.title("Legal Assistant")

w = 700 
h = 585
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight() 
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
# root.geometry("600x333")
root.maxsize(700,585)
root.minsize(700,585)
current_machine_id = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
data2={"Unique ID":current_machine_id}
# firebase3=firebase.FirebaseApplication("https://uniqueid-b15a7.firebaseio.com/",None)
# UID=firebase3.post("/uniqueid-b15a7/UID-Clients",data2)
def vals():
    now =d.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    t1=d.date.today().day
    t2=d.date.today().month
    t3=d.date.today().year
    t=email_.get()
    # print(t)
    a=name_.get()
    b=phone_.get()
    c=gender_.get()
    h=contact_.get()
    e=payment_.get()
    # print(e)
    g=c.upper()
    firebase2=firebase.FirebaseApplication("https://pythonfirebase-db.firebaseio.com/",None)
    data={"Name":a,"Phone Number":b,"Email":t,"Gender":c,"Emergency Contact":h,"Payment mode":e,"UID":current_machine_id}
    result=firebase2.post("/pythonfirebase-db/Clients",data)
    # data2={"Unique ID":current_machine_id}
    # firebase3=firebase.FirebaseApplication("https://uniqueid-b15a7.firebaseio.com/",None)
    # UID=firebase3.post("/uniqueid-b15a7/UID-Clients",data2)
    # data2={"Unique ID":current_machine_id}
    # firebase3=firebase.FirebaseApplication("https://uniqueid-b15a7.firebaseio.com/",None)
    # UID=firebase3.post("/uniqueid-b15a7/UID-Clients",data2)
    root.destroy()
    import legalassistant
        # print()
f2=Frame(root,bg="lightgoldenrod2",borderwidth=6,relief=RAISED)
f2.grid(row=0,column=4,pady=30,sticky=N)
Label(f2,text="LEGAL PRACTIONERS' ASSISTANT",padx=23,fg="red",font=" Ariel 14 bold",pady=15,bg="lightgoldenrod2").grid(row=0,column=4)
Label(root,text="          ",bg="LightBlue2").grid(row=1,column=2)


Label(root,text="Name",bg="LightBlue2",pady=10,font="Ariel 12").grid(row=2,column=3,sticky=W,columnspan=4)
Label(root,text="Phone No.",bg="LightBlue2",pady=10,font="Ariel 12").grid(row=3,column=3,sticky=W,columnspan=4)
Label(root,text="Email ID.",bg="LightBlue2",pady=10,font="Ariel 12").grid(row=4,column=3,sticky=W,columnspan=4)
Label(root,text="Gender",bg="LightBlue2",pady=10,font="Ariel 12").grid(row=5,column=3,sticky=W,columnspan=4)
Label(root,text="Emergency \nContact No.",bg="LightBlue2",pady=10,font="Ariel 12").grid(row=6,column=3,sticky=W,columnspan=4)
Label(root,text="Payment mode",bg="LightBlue2",pady=10,font="Ariel 12").grid(row=7,column=3,sticky=W,columnspan=4)

email=StringVar()
name=StringVar()
phone=IntVar()
gender=StringVar()
contact=IntVar()
Payment_mode=StringVar()
# food_service=IntVar()


name_=Entry(root,textvariable=name,fg="DeepPink3",font=12,width=15)
name_.grid(row=2,column=4,columnspan=5,sticky=E)
phone_=Entry(root,textvariable=phone,fg="DeepPink3",font=12,width=15)
phone_.grid(row=3,column=4,columnspan=5,sticky=E)
email_=Entry(root,textvariable=email,fg="DeepPink3",font=12,width=15)
email_.grid(row=4,column=4,columnspan=5,sticky=E)
gender_=Entry(root,textvariable=gender,fg="DeepPink3",font=12,width=15)
gender_.grid(row=5,column=4,columnspan=5,sticky=E)
contact_=Entry(root,textvariable=contact,fg="DeepPink3",font=12,width=15)
contact_.grid(row=6,column=4,columnspan=5,sticky=E)
# payment_=Entry(root,textvariable=Payment_mode,fg="DeepPink3",font=12).grid(row=7,column=4,columnspan=5,sticky=E)
paymentmodes=("Debit Card","Paytm","Credit Card","Net Banking","PhonePe")
payment_=Combobox(root,values=paymentmodes)
payment_.grid(row=7,column=4,columnspan=5,sticky=E)

# Checkbutton(root,text="Do you want meal ?",variable=food_service,bg="LightBlue2").grid(row=7,column=5)
Label(root,text="                             ",bg="LightBlue2").grid(row=8,column=2)
button=Button(root,text="Sign Up",command=vals,fg="white",bg='red4',font="Cursive 12")
button.grid(row=9,column=4,columnspan=5,pady=10)
mainmenu=Menu(root)

mymenu=Menu(mainmenu,tearoff=0)
mymenu2=Menu(mainmenu,tearoff=0)
# mymenu3=Menu(mainmenu,tearoff=0)

mymenu.add_command(label="Save",command=save)
mymenu.add_command(label="Save As",command=save_as)
mymenu.add_command(label="Exit",command=exit_)
mymenu2.add_command(label="License",command=license_)
mymenu2.add_command(label="Registration",command=registration)
# mymenu3.add_command(label="Disclaimer",command=Disclaimer)
mainmenu.add_cascade(label="File",menu=mymenu)
mainmenu.add_cascade(label="License",menu=mymenu2)
mainmenu.add_command(label="Feedback",command=Feedback)
mainmenu.add_command(label="Help",command=Help)
mainmenu.add_command(label="Disclaimer",command=Disclaimer)

# mainmenu.add_cascade(label="Feedback",menu=mymenu)

root.config(menu=mainmenu)
root.mainloop()

