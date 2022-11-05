import tkinter as tk
from tkinter import*

root=tk.Tk()
root.geometry("700x700")
value_name=tk.StringVar()
var=tk.StringVar(root," ")
v3=tk.StringVar()
zip_=tk.IntVar()
var=tk.StringVar(root," ")




def sub():
    email=v3.get()
    email.set("@")

l1=Label(root,text="First Name: ",font=('Arial',10))
l1.place(x=5,y=0)

v1=Entry(root,textvariable=value_name)
v1.place(x=100,y=5)


l2=Label(root,text="Last Name: ",font=('Arial',10))
l2.place(x=5,y=25)

v2=Entry(root,textvariable=value_name)
v2.place(x=100,y=30)

l3=Label(root,text="Gender: ",font=('Arial',10))
l3.place(x=5,y=50)

l4=Label(root,text="Languages: ",font=('Arial',10))
l4.place(x=5,y=80)

l5=Label(root,text="Email: ",font=('Arial',10))
l5.place(x=5,y=110)

v3=Entry(root,textvariable=v3)
v3.place(x=100,y=115)

l6=Label(root,text="Address: ",font=('Arial',10))
l6.place(x=5,y=140)

l7=Label(root,text="State: ",font=("Arial",10))
l7.place(x=5,y=170)

l8=Label(root,text="zip: ",font=('Arail',10))
l8.place(x=5,y=190)

l9=Label(root,text="Credit Card Type: ",font=('Arial',10))
l9.place(x=5,y=220)

v7=Entry(root,textvariable=Menu)
v7.place(x=120,y=220)

v6=Entry(root,textvariable=zip_)
v6.place(x=100,y=195)

v5=Entry(root,textvariable=value_name)
v5.place(x=100,y=170)

v4=Entry(root,textvariable=value_name)
v4.place(x=100,y=140)

cb1=Checkbutton(root,text="Telugu",font=('Arial',10),onvalue=1,offvalue=0)
cb1.place(x=100,y=80)

cb2=Checkbutton(root,text="English",font=('Arial',10),onvalue=1,offvalue=0)
cb2.place(x=180,y=80)

cb3=Checkbutton(root,text="Hindi",font=('Arial',10),onvalue=1,offvalue=0)
cb3.place(x=270,y=80)

r1 = tk.Radiobutton(root,text='Male',variable=var, value='Male',font=('Arial',10))
r1.place(x=100,y=50)

r2 = tk.Radiobutton(root,text='Female',variable=var, value='Female',font=('Arial',10))
r2.place(x=160,y=50)

btn1=Button(text="Insert",width=15,height=2)
btn1.place(x=280,y=170)

btn2=Button(text="Delete",width=15,height=2)
btn2.place(x=280,y=250)

btn3=Button(text="Theme",width=15,height=2)
btn3.place(x=280,y=350)

root.mainloop()