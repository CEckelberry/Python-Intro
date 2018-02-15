def check_answers(my_answers,keys):
    """
    Checks the five answers provided to a multiple choice quiz and returns the results.
    """
    results = [None, None, None, None, None]
    for x in range(len(my_answers)):

        if my_answers[x] == keys[x]:
            results[x] = True

        elif my_answers[(x)] != keys[x]:
            results[x] = False

    count_correct = 0
    count_incorrect = 0
    for result in results:
        if result == True:
            count_correct += 1
        if result != True:
            count_incorrect += 1
    if count_correct/5 > 0.7:
        return "Congratulations, you passed the test! You scored " + str(count_correct) + " out of 5."
    elif count_incorrect/5 >= 0.3:
        return "Unfortunately, you did not pass. You scored " + str(count_correct) + " out of 5."

print(check_answers(["tv", "tv", "tv", "tv", "tv" ], ["tv", "tv", "tv", "tv", "tv"])  )

