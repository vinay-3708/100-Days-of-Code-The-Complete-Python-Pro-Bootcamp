from question_model import Question
class QuizBrain():
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.quiz_score = 0

    def still_has_ques(self):
        return self.question_number < len(self.question_list)


    def check_answer(self, user_ans, crt_ans):
        self.user_ans = user_ans
        self.crt_ans = crt_ans
        if self.user_ans.lower() == self.crt_ans.lower():
            print("You got it correct")
            self.quiz_score += 1
        else:
            print("Nah, Thats wrong answer..!!")
        print(f"Correct answer is: {crt_ans}")
            
    def next_question(self):
        user_input = input(f'Q.{self.question_number + 1}. {self.question_list[self.question_number].text} ? (True/False): ')
        self.check_answer(user_input, self.question_list[self.question_number].answer)
        print(f"Your current score is: {self.quiz_score}/{self.question_number + 1}\n")
        self.question_number += 1
