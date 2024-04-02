BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas
import random
import time
global RAN

window = Tk()
window.configure(padx=50, pady=50, bg=BACKGROUND_COLOR)

window.title("Flash Cards Game")

# file = open()
try:
    df = pandas.read_csv("./Day-31_FlipCards/data/words_to_learn.csv")
except FileNotFoundError:
    org_data = pandas.read_csv("./Day-31_FlipCards/data/french_words.csv")
    org_data.to_csv("./Day-31_FlipCards/data/words_to_learn.csv", index=False)
    df = pandas.read_csv("./Day-31_FlipCards/data/words_to_learn.csv")

eng_fp = PhotoImage("./Day-31_FlipCards/images/card_back.png")
def random_words():
    global RAN
    RAN = random.randint(0, len(df)-1)
    title = "French"
    fr_word = df.iloc[RAN]["French"]
    canvas.itemconfig(tagOrId=image_tag, image=card_frnt_image)
    canvas.itemconfig(tagOrId=title_tag, text=f"{title}", fill="black")
    canvas.itemconfig(tagOrId=word_tag, text=f"{fr_word}", fill="black")
    window.after(3000, func=flip_card)

def flip_card():
    eng_word = df.iloc[RAN]["English"]
    canvas.itemconfig(tagOrId=image_tag, image=eng_fp)
    canvas.itemconfig(tagOrId=title_tag, text="English", fill="white")
    canvas.itemconfig(tagOrId=word_tag, text=f"{eng_word}", fill="white")

def tick_func():
    global RAN
    try:
        prev_ran = RAN
        # print(prev_ran)
        df.drop(df.index[RAN], axis=0, inplace=True)
        df.to_csv("./Day-31_FlipCards/data/words_to_learn.csv", index=False)
    except:
        print("Exception Catched")
    finally:
        random_words()
        # print("Tick called")
def wrng_func():
    random_words()
    # print("Wrng Called")
# window.after(3000, func=flip_card) 

card_frnt_image = PhotoImage(file="./Day-31_FlipCards/images/card_front.png")
# card_back_image = PhotoImage(file="./Day-31_FlipCards/images/card_back.png")
canvas = Canvas(height=526, width=800)
image_tag = canvas.create_image(400, 263, image=card_frnt_image)
canvas.configure(bg=BACKGROUND_COLOR, highlightthickness=0)
word_tag = canvas.create_text(400, 263,text="word", font=("Ariel", "60", "bold"))
title_tag = canvas.create_text(400, 150,text="title", font=("Ariel", "40", "italic"))

canvas.grid(row=0, column=0, columnspan=2)

tick_img = PhotoImage(file="./Day-31_FlipCards/images/right.png")
tick_button = Button(image=tick_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=tick_func)
tick_button.grid(row=1, column=1)
wrng_img = PhotoImage(file="./Day-31_FlipCards/images/wrong.png")
wrng_button = Button(image=wrng_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=wrng_func)
wrng_button.grid(row=1, column=0)


window.mainloop()