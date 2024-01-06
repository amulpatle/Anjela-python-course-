from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

# Label



my_label = Label(text="i am label", font=("Arial", 24, "bold"))
my_label.pack()

def button_clicked():
    print("I Got Clicked")
    my_label.config(text = "Button got clicked")

button = Button(text="click", command=button_clicked)
button.pack()


#entery class

input = Entry()
input.pack()
txt = input.get()
print(txt)


window.mainloop()