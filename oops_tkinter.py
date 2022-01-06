from tkinter import *
class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("700x600")
    def status(self):
        self.var=StringVar()
        self.var.set("Ready")
        self.statusbar=Label(self,textvar=self.var,relief=SUNKEN,anchor="w").pack(side=BOTTOM,fill=X)
    def click(self):
        print("Button clicked.")
    def createbutton(self,text):
        Button(text=text,command=self.click).pack()

if __name__ == "__main__":
    obj=GUI()
    obj.status()
    obj.createbutton("Click Me!")
    obj.mainloop()