from tkinter import *
from tkinter import messagebox
from random import choice, randint,shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,f"{password}")
    pyperclip.copy(password)
    # print(f"Your password is: {password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website:{
            "email":email,
            "password":password,
        }
    }
    # messagebox.showinfo(title="Title", message="Message")
    
    if website == "" or email == "" or password == "":
        details_info = messagebox.showinfo(title="error", message="hey ! you left the some message entery")
    else:
        
        is_ok = messagebox.askokcancel(title=website,message=f"these are the details entered: \nEmail: {email}" f"\nPassword: {password} \n Is it ok to save?")
          
        if is_ok:
        
            with open("/home/amul/Documents/anjela python/Day 29/Password Manager/data.json",'a') as data_file:
                
                json.dump(new_data,data_file,indent=4)
                website_entry.delete(0,END)
                password_entry.delete(0,END)
        

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("password manager")
window.config(padx=50,pady=20)

canvas = Canvas(height=200,width=200)
logo_img = PhotoImage(file = "/home/amul/Documents/anjela python/Day 29/Password Manager/logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(column =1,row=0)


#label

website_label = Label(text="Website:")
website_label.grid(column=0,row =1)

Email_label = Label(text="Email/Username:")
Email_label.grid(column=0,row=2)

password_label = Label(text="Password")
password_label.grid(column=0,row=3)

generatepassword_lable = Label(text="Generate Password")
generatepassword_lable.grid(column=2,row=3)


# buttons

add_button = Button(text="Add",width=36, command=save)
add_button.grid(column=1,row=4,columnspan=2)

generate_password_button = Button(text="Generate Password",command=generate_password)
generate_password_button.grid(row=3,column=2)

# Entries

website_entry = Entry(width=35)
website_entry.grid(row = 1,column=1,columnspan=2)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"xyz@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(row=3,column=1)

window.mainloop()