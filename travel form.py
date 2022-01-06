from tkinter import *
import datetime as d
root=Tk()

root.configure(bg="LightBlue2")
root.title("Sayantan Travels")

w = 700 
h = 500
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight() 
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
# root.geometry("600x333")
root.maxsize(700,450)
root.minsize(700,500)

def vals():
    # print(f"1.Name={name.get()}")
    # print(f"2.Phone NUmber={phone.get()}")
    # print(f"3.Gender={gender.get()}")
    # print(f"4.Emergency Contact Number={contact.get()}")
    # print(f"5.Payment Mode={Payment_mode.get()}")
    # print(f"6.Food Service={food_service.get()}")
    print("Submitting form")
    now =d.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    t1=d.date.today().day
    t2=d.date.today().month
    t3=d.date.today().year
    #print(f"{name.get(),phone.get(),gender.get(),contact.get(),Payment_mode.get(),food_service.get()}")
    with open("record.txt","a") as f:
        f.write(f"{name.get(),phone.get(),gender.get(),contact.get(),Payment_mode.get(),food_service.get(),t1,t2,t3,current_time}\n")
    print()
f2=Frame(root,bg="azure",borderwidth=3,relief=RAISED)
f2.grid(row=0,column=4,pady=30,sticky=N)
Label(f2,text="WELCOME TO SAYANTAN TRAVELS",fg="red",font=" Ariel 9 bold",pady=15,bg="azure").grid(row=0,column=4)
Label(root,text="                       ",bg="LightBlue2").grid(row=1,column=2)
Label(root,text="                       ",bg="LightBlue2").grid(row=2,column=2)
# Label(root,text="      ",bg="LightBlue2").grid(row=2,column=2)
# Label(root,text="      ",bg="LightBlue2").grid(row=2,column=2)
# Label(root,text="      ",bg="LightBlue2").grid(row=2,column=2)
# Label(root,text="      ",bg="LightBlue2").grid(row=2,column=2)

Label(root,text="Name",bg="LightBlue2",pady=10,font="Ariel 12").grid(row=2,column=3,sticky=W)
Label(root,text="Phone No.",bg="LightBlue2",pady=10,font="Ariel 12").grid(row=3,column=3,sticky=W)
Label(root,text="Gender",bg="LightBlue2",pady=10,font="Ariel 12").grid(row=4,column=3,sticky=W)
Label(root,text="Emergency \nContact No.",bg="LightBlue2",pady=10,font="Ariel 12").grid(row=5,column=3,sticky=W)
Label(root,text="Payment mode",bg="LightBlue2",pady=10,font="Ariel 12").grid(row=6,column=3,sticky=W)

name=StringVar()
phone=IntVar()
gender=StringVar()
contact=IntVar()
Payment_mode=StringVar()
food_service=IntVar()

name_=Entry(root,textvariable=name).grid(row=2,column=4)
phone_=Entry(root,textvariable=phone).grid(row=3,column=4)
gender_=Entry(root,textvariable=gender).grid(row=4,column=4)
contact_=Entry(root,textvariable=contact).grid(row=5,column=4)
payment_=Entry(root,textvariable=Payment_mode).grid(row=6,column=4)

Checkbutton(root,text="Do you want meal ?",variable=food_service,bg="LightBlue2").grid(row=7,column=4)
Button(root,text="Submit",command=vals,fg="white",bg='red4',font="Cursive 12").grid(row=8,column=4)

root.mainloop()