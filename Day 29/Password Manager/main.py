from tkinter import *
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    # messagebox.showinfo(title="Title", message="Message")
    
    if website == "" or email == "" or password == "":
        details_info = messagebox.showinfo(title="error", message="hey ! you left the some message entery")
    else:
        is_ok = messagebox.askokcancel(title=website,message=f"these are the details entered: \nEmail: {email}" f"\nPassword: {password} \n Is it ok to save?")
        
        
            
        if is_ok:
        
            with open("/home/amul/Documents/anjela python/Day 29/Password Manager/data.txt",'a') as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
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

generate_password_button = Button(text="Generate Password")
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