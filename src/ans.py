def math_quiz():
    ans = 5 + 2
    userWrongAnswer = True
    while userWrongAnswer:
        user_answer = input('What is 5 + 2?')
        if str(ans) == user_answer:
            userWrongAnswer = False
            print('Correct!')
        else:
            userWrongAnswer = True
            print('Wrong answer, try again!')