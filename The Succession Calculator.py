from tkinter import *
root=Tk()
root.geometry("500x300")
root.minsize(1000,500)
root.title("The Succession Calculator")
n=0
tax=0
l1=Label(root)
def result():
          global n
          global tax
          global l1
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
          l1.destroy()
          #print(f"Result={r}")
          f2=Frame(root,borderwidth=3,relief=SUNKEN,bg="green").grid(row=4,column=1)
          Label(root,text="Result:",font="Helvetica 13 bold",fg="green").grid(row=5,column=1,sticky=W,padx=250)
        #   Label(root,text="").grid(row=3,column=1)
          l1=Label(f2,text="Rs. "+r,fg="red",font="Helvetica 13 bold")
          l1.grid(row=5,column=1,columnspan=2)
        #   Label.destroy(l1)
# root.maxsize(1000,300)
f2=Frame(root,borderwidth=3,relief=SUNKEN,bg="yellow")
#f2.grid(row=0,column=1,padx=350,pady=25)
Label(root,text=" ").grid(row=0,column=1)
f2.place(x=1,y=1)
Label(f2,text="The Indian Succession Act 1925",borderwidth=3,bg="yellow",font="Helvetica 13 bold").grid(row=0,column=1)
f=Frame(root,borderwidth=3,relief=SUNKEN,bg="skyblue1")
f.grid(row=1,column=1,pady=10,padx=20)
Label(f,text="To know the value of Non-Judicial Stamp for obtaining Succession Certificate ",bg="skyblue1",fg="brown4",font="Helvetica 13 bold").grid(row=1,column=1,columnspan=2)
Label(f,text="U/s.372 of The Indian Succession Act. 1925 (For New Filing):-",bg="skyblue1",fg="brown4",font="Helvetica 13 bold").grid(row=2,column=1)
Label(root,text="Enter the amount :",pady=10,font="Helvetica 13 bold").grid(row=3,column=1,sticky=W,padx=200,pady=30)
amount=IntVar()
money=Entry(root,textvariable=amount).grid(row=3,column=1,columnspan=2,padx=400,sticky=E)
Button(root,text="Get result",fg="white",bg="red4",command=result,font="Helvetica 13 bold").grid(row=4,column=1)
root.mainloop() 
