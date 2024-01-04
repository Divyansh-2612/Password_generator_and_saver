from tkinter import *
from tkinter import messagebox
wind=Tk()
def ad():
    Website=website_entry.get()
    Email=Email_entry.get()
    Password=password_entry.get()
    if len(Website)==0 or len(Password)==0 or len(Email)<=10:
        messagebox.showinfo(title="Oop!",message="You have left with some of the field to be field")
    else:
        is_ok=messagebox.askokcancel(title=Website,message=f"These are the field value that you have entered have a look at it once more\nEmail:{Email}\nPassword:{Password}\nif all look good please Press ok")
        if is_ok:
            with open("password_saved","a") as data:
                data.write(f"{Website},{Email},{Password} \n")
                website_entry.delete(0,END)
                password_entry.delete(0,END)



def pg():
    import random
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']
    num = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    syml = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "?"]
    choices = ["alpha", "num", "syml"]
    a = random.randint(8, 10)
    n = random.randint(2, 4)
    s = random.randint(2, 4)
    l=[random.choice(alpha) for _ in range(a)]
    sy=[random.choice(syml) for _ in range(s)]
    nu=[random.choice(num) for _ in range(n)]
    li=l+sy+nu
    random.shuffle(li)
    ps="".join(li)
    password_entry.insert(0,ps)

wind.title("Password Generator")
wind.config(padx=50,pady=50)
canvas=Canvas(height=200,width=200)
logo_img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)
website_label=Label(text="Website:")
website_label.grid(row=1,column=0)
Email_label=Label(text="Email/username:")
Email_label.grid(row=2,column=0)
password_label=Label(text="Password:")
password_label.grid(row=3,column=0)
website_entry=Entry(width=62)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()
Email_entry=Entry(width=62)
Email_entry.grid(row=2,column=1,columnspan=2)
Email_entry.insert(END,"@gmail.com")
password_entry=Entry(width=43)
password_entry.grid(row=3,column=1)
generate=Button(text="Generate Password",command=pg)
generate.grid(row=3,column=2)
add=Button(text="Add",width=52,command=ad)
add.grid(row=4,column=1,columnspan=2)



wind.mainloop()