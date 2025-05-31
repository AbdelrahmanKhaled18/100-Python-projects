from tkinter import *

def convert_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.60934, 2)
    result_label.config(text=f"{km}")

window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=300, height=200)
window.config(padx=20, pady=20)

# Entry
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

# Miles Label
mile_label = Label(text="Miles", font=("Arial", 14))
mile_label.grid(column=2, row=0)

# Is Equal Label
is_equal_label = Label(text="is equal to", font=("Arial", 14))
is_equal_label.grid(column=0, row=1)

# Result Label
result_label = Label(text="0", font=("Arial", 14))
result_label.grid(column=1, row=1)

# Kilometers Label
kilo_label = Label(text="Kilometers", font=("Arial", 14))
kilo_label.grid(column=2, row=1)

# Button
calc_button = Button(text="Calculate", command=convert_to_km)
calc_button.grid(column=1, row=2)

window.mainloop()
