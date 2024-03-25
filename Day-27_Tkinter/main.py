import tkinter

window = tkinter.Tk()
window.title("MyFirstGUIApp")
window.minsize(width=700, height=400)



my_label = tkinter.Label(text="Type and Click the Button", font=("Arial", 24, "italic"))
my_label.grid(row=0, column=0)
def button_clicked():
    print("Button_Clicked")
    # my_label["text"] = "Clicked...!"
    user_text = user_input.get()
    my_label.configure(text=user_text)

user_input = tkinter.Entry(width=15)
# user_input.insert(string="Enter Some Text")
# user_input.pack()
user_input.grid(row=2, column=3)
button = tkinter.Button(text="Click", command=button_clicked)
button.grid(row=1,column=1)

new_button = tkinter.Button(text="Submit")
new_button.grid(row=0, column=2)

#Text
text_box = tkinter.Text(width=30, height=5)
text_box.focus()
# text_box.insert(END, "Enter some text")
# text_box.pack()


#Spinbox
spin_box = tkinter.Spinbox(from_=0, to=20, width=4)
# spin_box.pack()

def scale(val):
    print(val)

#Scale
scale = tkinter.Scale(from_=0, to=100, width=5, command=scale)
# scale.pack()

#Check Button
def check_button_used():
    print(check_button_status.get())
check_button_status = tkinter.IntVar()
check_button = tkinter.Checkbutton(text="Is on?", variable=check_button_status, command=check_button_used)
# check_button.pack()


# #RadioButton
def radio_ans():
    print(radio_status.get())
radio_status = tkinter.IntVar()
radio_button = tkinter.Radiobutton(variable=radio_status, command=radio_ans, text="Age?", value=26)
# radio_button.pack()


#Listbox
def list_box_used(event):
    print(list_box.get(list_box.curselection()))
list_box = tkinter.Listbox(height=4)
fruits = ["apple", "ball", "cat", "dog"]
for item in fruits:
    list_box.insert(fruits.index(item), item)

list_box.bind("<<ListBoxSelect>>", list_box_used)
# list_box.pack()




window.mainloop()