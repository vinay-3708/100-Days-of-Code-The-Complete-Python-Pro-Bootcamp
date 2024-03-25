import tkinter

window = tkinter.Tk()
window.title("MILE to KM Converter")
window.minsize(width=400, height=100)

in_km = 0
conversion_rate = 1.609344

my_entry = tkinter.Entry(width=10)
my_entry.grid(column=0, row=0)

my_label_1 = tkinter.Label(text=f"Miles is equal to {in_km} Kilometers.")
my_label_1.grid(column=1,row=0)

def result():
    in_km = conversion_rate * float(my_entry.get())
    # print(in_km)
    my_label_1.configure(text=f"Miles is equal to {in_km} Kilometers.")

button_1 = tkinter.Button(text="Calculate", command=result)
button_1.grid(row=1, column=0)


def reset():
    in_km = 0
    my_label_1.configure(text=f"Miles is equal to {in_km} Kilometers.")

button_2 = tkinter.Button(text="Reset", command=reset)
button_2.grid(row=1, column=1)

def close_window():
    window.destroy()

button_3 = tkinter.Button(text="Close", command=close_window)
button_3.grid(row=1, column=2)
window.mainloop()

