from tkinter import *
from tkinter import messagebox
import x
import pandas as pd

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    password=x.password
    entry_password.insert(0,password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website=entry_website.get()
    username=entry_username.get()
    password=entry_password.get()
    if website.strip()=="" or username.strip()=="" or password.strip()=="":
        x=messagebox.showerror(title="Opppsss",message="Please don't leave any fields empty!")
    else:
        is_true = messagebox.askokcancel(title=window, message=f"These are the details enterd\n"
                                                               f"Email: {username}\n"
                                                               f"Password: {password}\n"
                                                               f"it it ok to save? ")

        if is_true:
            data = f"{website} | {username} | {password}\n"
            with open("data.txt", "a") as file:
                file.write(data)
                entry_website.delete(0, END)
                entry_password.delete(0, END)
                entry_username.delete(0, END)
                entry_website.focus()





# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Password Manager")
window.config(pady=20, padx=20)

canvas = Canvas(width=200, height=200)
photo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(row=0, column=1)

label_website = Label(text="Website:")
label_website.grid(row=1, column=0)

label_username = Label(text="Email/Username:")
label_username.grid(row=2, column=0)

label_password = Label(text="Password")
label_password.grid(row=3, column=0)

entry_website = Entry(width=35)
entry_website.grid(row=1, column=1, columnspan=2,sticky="EW")
entry_website.focus()

entry_username = Entry(width=35)
entry_username.grid(row=2, column=1, columnspan=2,sticky="EW")


entry_password = Entry(width=21)
entry_password.grid(row=3, column=1,sticky="EW")

button_add = Button(text="Add", width=35,command=save_data)
button_add.grid(row=4, columnspan=2, column=1,sticky="EW")

button_generatePassword = Button(text="Generate Password",command=password_generator)
button_generatePassword.grid(row=3, column=2,sticky="EW")

window.mainloop()