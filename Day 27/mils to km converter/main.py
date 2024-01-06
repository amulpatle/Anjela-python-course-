from tkinter import *


def miles_to_km():
    ip = float(miles_input.get())
    km = ip * 1.609
    km_result_label.config(text=f"{km}")


window = Tk()
window.title("mils to km")
window.config(padx=20,pady=20)
miles_label = Label(text="miles")

miles_input = Entry(width=7)
miles_input.grid(column=1 , row=0)

miles_label = Label(text="miles")
miles_label.grid(column=2,row=0)

km_lable = Label(text="km")
km_lable.grid(column=2,row=1)

km_result_label = Label(text="0")
km_result_label.grid(column=1,row=1)

is_equal_to_lable = Label(text="is equal to")
is_equal_to_lable.grid(column=0,row=1)

calculate_button = Button(text="calculate",command=miles_to_km)
calculate_button.grid(column=1,row=2)






window.mainloop()