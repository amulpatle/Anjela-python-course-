from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)

# print(question_model[0])
quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()
    # quiz.check_answer()
    
print("You have complited the quiz")
print(f"Your final score is {quiz.score}/{quiz.question_number}")