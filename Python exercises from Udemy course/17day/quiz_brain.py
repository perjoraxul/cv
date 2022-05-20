class QuizBrain :

    def __init__(self,q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self) :
        item = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {item.text} (True/False)? ")
        self.check_answer(user_answer, item.answer)

    def still_has_questions(self) :
        return self.question_number < len(self.question_list) 
    
    def check_answer(self, user, item) :

        if user.lower() == item.lower() :
            self.score +=1
            print("You got it!")
        else :
            print("Niet") 

        print(f"The correct answer was {item}")    
        print(f"Your current score is {self.score}/{self.question_number}")      
        print("\n") 
        
    def final_score(self) :
        print(f"You've completed the quiz. Your final score was: {self.score}/{self.question_number}")