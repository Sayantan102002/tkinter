# from tkinter import *
# root13=Tk()
# canvas_width=1260
# canvas_height=600
# canvas1=Canvas(root13,width=canvas_width,height=canvas_height,bg="gray30")
# canvas1.pack(side = RIGHT, fill = BOTH, expand = True)
# frame13 = Frame(canvas1, bg = 'purple')
# canvas1.create_window((0,0),window=frame13, anchor = NW)
# mail_scroll = Scrollbar(canvas1, orient = "vertical", 
#     command = canvas1.yview)
# def OnFrameConfigure(event):
#         canvas1.configure(scrollregion=canvas1.bbox("all"))
# mail_scroll.pack(side = RIGHT, fill = Y)
# frame13.bind("<Configure>",OnFrameConfigure)
# canvas1.config(yscrollcommand = mail_scroll.set)
# for i in range(36):
#     Label(frame13,text="HI",font=30).place(x=0,y=0)

# root13.mainloop()
import tkinter as tk

def on_configure(event):
    canvas.configure(scrollregion=canvas.bbox('all'))

root = tk.Tk()

canvas = tk.Canvas(root,bg="gray30")
canvas.place(relx=0, rely=0, relheight=1, relwidth=1)

frame = tk.Frame(canvas,bg="gray30")
# resize the canvas scrollregion each time the size of the frame changes
frame.bind('<Configure>', on_configure)
# display frame inside the canvas
canvas.create_window(0, 0, window=frame)

scrolly = tk.Scrollbar(root, command=canvas.yview)
scrolly.place(relx=1, rely=0, relheight=1, anchor='ne')
canvas.configure(yscrollcommand=scrolly.set)

# populate the frame
n=0
for i in range(1000):
    n+=50
    tk.Label(frame, text='Label %i' % i,bg="gray30").pack(padx=50)

root.mainloop()
