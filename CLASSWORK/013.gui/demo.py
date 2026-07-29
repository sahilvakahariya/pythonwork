from tkinter import *

root = Tk()
root.geometry("500x500")
root.title("MY APP")

b1 = Button(root,text="LEFT")
b1.pack(side=LEFT)
b2 = Button(root,text="RIGHT")
b2.pack(side=RIGHT)
b3 = Button(root,text="TOP")
b3.pack(side=TOP)
b4 = Button(root,text="BOTTOM")
b4.pack(side=BOTTOM)


name = Label(root,text="Username")
name.grid(row=1,column=1)
email = Label(root,text="Email")
email.grid(row=2,column=1)
phone = Label(root,text="Username")
phone.grid(row=3,column=1)

t1 = Entry(root)
t1.grid(row=1,column=2)
t2 = Entry(root)
t2.grid(row=2,column=2)
t3 = Entry(root)
t3.grid(row=3,column=2)

b  =Button(root,text="submit")
b.grid(row=4,column=2)

name = Label(root,text="Username")
name.place(x=100,y=100)
email = Label(root,text="Email")
email.place(x=100,y=150)
phone = Label(root,text="Username")
phone.place(x=100,y=200)

t1 = Entry(root)
t1.place(x=200,y=100)
t2 = Entry(root)
t2.place(x=200,y=150)
t3 = Entry(root)
t3.place(x=200,y=200)

b  =Button(root,text="submit",width=17)
b.place(x=200,y=230)
root.mainloop()