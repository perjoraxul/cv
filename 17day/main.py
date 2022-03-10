from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

#simple game that prompts some questions to the user and checks if the user answered them correctly


question_bank = []
for i in range(len(question_data)) :
    question_bank.append(Question(question_data[i]["text"],question_data[i]["answer"]))


#the example from course
'''
question_bank = []
for question in question_data :
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)

'''

quiz = QuizBrain(question_bank)

while quiz.still_has_questions() :
    quiz.next_question()
    
quiz.final_score()