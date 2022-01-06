from tkinter import *
from PIL import ImageTk
from tkinter.tix import *
class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1200x749")
        self.root.resizable(False,False)
        # self.ws = self.root.winfo_screenwidth()
        # self.hs = self.root.winfo_screenheight() 
        self.bg=ImageTk.PhotoImage(file="image.jpg")
        self.bg_Image=Label(self.root,image=self.bg).pack(fill=BOTH,expand=YES)
        # self.root.attributes('-alpha', 0.1)
        Frame_login=Frame(self.root,bg="mistyrose")
        Frame_login.place(x=350,y=300,width=500,height=340)
        title=Label(Frame_login,text="Login Here",font=("Goudy old style", 35,"bold"),bg="mistyrose",fg="navy").place(x=110,y=30)
        #desc=Label(Frame_login,text="User Login area",font=("Goudy old style", 15,"bold"),bg="white",fg="dark orange").place(x=50,y=100)
        user=Label(Frame_login,text="Email",font=("Goudy old style", 15,"bold"),bg="mistyrose",fg="navy").place(x=50,y=115)
        self.user_entry=Entry(Frame_login,font=("times new roman", 15),bg="white",fg="navy").place(x=180,y=120)
        pass_=Label(Frame_login,text="Password",font=("Goudy old style", 15,"bold"),bg="mistyrose",fg="navy").place(x=50,y=190)
        self.passw=Entry(Frame_login,font=("times new roman", 15),bg="white",fg="navy").place(x=180,y=195)
        self.button=Button(Frame_login,text="Login",font=("times new roman", 15),fg="white",bg="red4").place(x=210,y=255)
if __name__ == "__main__":        
    root=Tk()
    obj=Login(root)
    root.mainloop()