THEME_COLOR = "#375362"
WHITE = "#ffffff"
GREEN = "#00cc00"
RED = "#ff3300"

import time
from tkinter import *
from quiz_brain import QuizBrain

class UI:
    def __init__(self, quiz: QuizBrain):
        self.quiz_b = quiz
        self.q_score = 0
        self.window = Tk()
        self.window.title("OpenTrivia")
        self.window.configure(bg=THEME_COLOR)
        self.canvas = Canvas(bg=WHITE, width=300, height=250)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
        self.canvas_label = self.canvas.create_text(150, 125, width=280, text="Question Goes here", fill=THEME_COLOR, font=("Arial", "20", "italic"))
        self.true_image = PhotoImage(file="images/true.png")
        self.tick_button = Button(image=self.true_image, highlightthickness=0, command=self.tick_button_cmd)
        self.tick_button.grid(row=2, column=0, padx=10, pady=10)
        self.cross_image = PhotoImage(file="images/false.png")
        self.cross_button = Button(image=self.cross_image, highlightthickness=0, command=self.cross_button_cmd)
        self.cross_button.grid(row=2, column=1, padx=10, pady=10)
        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg=WHITE)
        self.score_label.grid(row=0, column=1, padx=20, pady=20)        
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg=WHITE)
        if self.quiz_b.still_has_questions():
            # self.canvas.config(bg=WHITE)
            self.score_label.config(text=f"Score: {self.q_score}")
            q_text = self.quiz_b.next_question()
            self.canvas.itemconfig(tagOrId=self.canvas_label, text=q_text)
        else:
            self.canvas.itemconfig(tagOrId=self.canvas_label, text="You have completed all the questions.\nPlease Close the App.")
            self.tick_button.config(state="disabled")
            self.cross_button.config(state="disabled")
        
    def tick_button_cmd(self):
        is_right = self.quiz_b.check_answer("True")
        self.feedback(is_right)
        
    def cross_button_cmd(self):
        is_right = self.quiz_b.check_answer("False")
        self.feedback(is_right)
        
    def feedback(self, answer):
        if answer:
            self.q_score += 1
            print("Inside True")
            self.canvas.config(bg=GREEN)
        else:
            print("Inside False")
            self.canvas.config(bg=RED)
        self.window.after(1000, self.get_next_question)
# ui = UI()