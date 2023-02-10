# This is a True & False game

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(q_text=question_text, q_answer=question_answer)
    # we don't need tags (q_text=, q_answer=) because positional parameters.
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():  # if quiz still has question remaining:
    # or quiz.answer_count():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
