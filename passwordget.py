
from tkinter import *
from tkinter import messagebox
import pandas as pd
def fe():
    a=en.get()
    data=pd.read_csv("password_saved")
    ab=data[data.website==a]
    messagebox.showinfo(title="Displaying the details",message=f"{ab}")

ti=Tk()
ti.title("Get the Password")
ti.config(padx=20,pady=20)
can=Canvas(height=300,width=400)
im=PhotoImage(file="lock_bounce.gif")
can.create_image(200,150,image=im)
can.grid(row=0,column=1)
li=Label(text="Get your Email and password of the website",font=("arial",24,"bold"))
li.grid(row=1,column=0,columnspan=3)
la=Label(text="Website Name:",font=("arial",12,"bold"))
la.grid(row=2,column=0)
en=Entry(width=40)
en.grid(row=2,column=1)
en.focus()
fa=Button(text="Fetch the details",command=fe,width=15)
fa.grid(row=2,column=2)


ti.mainloop()



