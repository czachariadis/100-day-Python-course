from tkinter import *

FONT = ("Arial", 24, "bold")
MULTIPLIER = 1.609344

window = Tk()
window.title("Miles to Kilometers Converter")
window.minsize(width=200, height=100)
window.config(padx = 20, pady = 20)

miles_input = Entry(width = 7)
miles_input.grid(row = 0, column = 1)

miles_label = Label(text = "Miles")
miles_label.grid(row = 0, column = 2)

is_equal_label = Label(text = "is equal to")
is_equal_label.grid(row = 1, column = 0)

km_result_label = Label(text = "0")
km_result_label.grid(row = 1, column = 1)

km_label = Label(text = "Kilometer")
km_label.grid(row = 1, column = 2)

def calculate():
    miles = miles_input.get()
    kilometers = float(miles) * MULTIPLIER
    kilometers = round(kilometers)
    km_result_label.config(text = f"{kilometers}")
    

button = Button(text = "Calculate", command = calculate)
button.grid(row = 2, column = 1)


window.mainloop()