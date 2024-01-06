from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

def button_clicked():
    print("I Got Clicked")
    # my_label.config(text = "Button got clicked")

# Label
my_label = Label(text="label", font=("Arial", 24, "bold"))
# my_label.pack()
my_label.grid(row=0,column=0)



button = Button(text="click", command=button_clicked)
# button.pack()
button.grid(column=1,row=1)

new_button = Button(text="new buttonn",command=button_clicked)
new_button.grid(column=2,row=0)

#entery class

input = Entry()
# input.pack()
input.grid(column=3,row=3)
txt = input.get()
print(txt)


window.mainloop()