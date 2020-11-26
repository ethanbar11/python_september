import random

questions = {'question1': 'answer1', 'question2': 'answer2'}
questions_lst = list(questions.keys())
question_number = random.randint(0,len(questions_lst)-1)

random_question=questions_lst[question_number]
print(random_question)
