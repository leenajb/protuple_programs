from tkinter import *

def add():
    global i
    lbx.insert(ACTIVE,f"{i}")
    i+=1
i=0
root=Tk()
root.geometry("455x233")
root.title("ListBox Tutorial")
lbx=Listbox(root)
lbx.pack()
lbx.insert(END,"first item of listbox")

Button(root,text="Add Item",command=add).pack()



root.mainloop()