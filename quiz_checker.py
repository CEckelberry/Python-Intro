def check_answers(my_answers,keys):
    """
    Checks the five answers provided to a multiple choice quiz and returns the results.
    """
    results = [None, None, None, None, None]
    #Compares each of the lists and either marks it as true (matches the key) or false (it does not match the key)
    for x in range(len(my_answers)):

        if my_answers[x] == keys[x]:
            results[x] = True

        elif my_answers[(x)] != keys[x]:
            results[x] = False
    #Keeps track of the overall count of either incorrect or correct answers
    count_correct = 0
    count_incorrect = 0
    for result in results:
        if result == True:
            count_correct += 1
        if result != True:
            count_incorrect += 1
    #Prints out whether you passed the test based on the key comparison or
    if count_correct/5 > 0.7:
        return "Congratulations, you passed the test! You scored " + str(count_correct) + " out of 5."
    elif count_incorrect/5 >= 0.3:
        return "Unfortunately, you did not pass. You scored " + str(count_correct) + " out of 5."

print(check_answers(["tv", "tv", "tv", "tv", "tv" ], ["tv", "tv", "tv", "tv", "tv"])  )

