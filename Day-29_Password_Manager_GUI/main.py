from tkinter import *
from tkinter import messagebox
import random

PASSWORD_LENGTH = 8

window = Tk()
window.title("Password_Manager_GUI")
window.configure(padx=50, pady=50)
# window.minsize(width=500, height=500)

number = ['0','1','2','3','4','5','6','7','8','9']
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
spl_ch = ['!','#','$','%','&','*','(',')','+']

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    password = "".join([str(random.choice(random.choice([number, alpha, spl_ch]))) for i in range(PASSWORD_LENGTH)])
    # print(password)
    if len(password_text_box.get()) == 0: 
        password_text_box.insert(string=password, index=0)
    else:
        password_text_box.delete(0, END)
        password_text_box.insert(string=password, index=0)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():
    website = website_text_box.get()
    uname = email_text_box.get()
    passwd = password_text_box.get()
    if (len(website) == 0 or len(uname) == 0 or len(passwd) == 0):
        messagebox.showerror(title="Error...!!", message="Some fields are empty. Please add input and Retry.")
    else:
        is_ok = messagebox.askokcancel(title=f"{website} Credentials", message=f"These are the given inputs. \n\nE-mail: {uname}\nPassword: {passwd}\n\nIs it Ok to save?")
        if (is_ok):
            with open("./Day-29_Password_Manager_GUI/pass_data.txt", "a") as file:
                file.write(f"{website} | {uname} | {passwd} \n")
                file.close()
            website_text_box.delete(0, END)
            email_text_box.delete(0, END)
            password_text_box.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
canvas_bg_image = PhotoImage(file="./Day-29_Password_Manager_GUI/logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=canvas_bg_image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website: ")
website_label.grid(row=1, column=0, padx=5, pady=5)

website_text_box = Entry(width=52)
website_text_box.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

email_uname_label = Label(text="email/username: ")
email_uname_label.grid(row=2, column=0, padx=5, pady=5)

email_text_box = Entry(width=52)
email_text_box.grid(row=2, column=1, columnspan=2, padx=5, pady=5)

password_label = Label(text="Password: ")
password_label.grid(row=3, column=0, padx=5, pady=5)

password_text_box = Entry(width=32)
password_text_box.grid(row=3, column=1, padx=5, pady=5)

generate_button = Button(text="Generate Password", width=14, command=password_generator)
generate_button.grid(row=3, column=2, padx=5, pady=5)

add_button = Button(text="Add", width=45, command=save_pass)
add_button.grid(row=4, column=1, columnspan=2, padx=5, pady=5)

window.mainloop()