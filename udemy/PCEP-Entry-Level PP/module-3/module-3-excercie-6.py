correct_answer = 1994
answer_is_correct = False
while answer_is_correct == False:
    answer =  int(input('When was Python 1.0 released? '))
    if answer == correct_answer:
        answer_is_correct = True
        print('Correct!')
        break
    elif answer > correct_answer:
        print('It was earlier than that!')
    else:
        print('It was later than that!')