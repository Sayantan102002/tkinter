from tkinter import *
root=Tk()
canvas_height=800
canvas_width=700
root.geometry(f"{canvas_width}x{canvas_height}")
can_create=Canvas(root,height=canvas_height,width=canvas_width)
can_create.pack()
can_create.create_text(3,10,text="Python")
root.mainloop()
