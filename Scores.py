import random


def scores_and_grades():
    for i in range(11):
        random_score = int(random.random() * 40 + 60)
        if random_score < 70:
            grade = "D"
        elif random_score < 80:
            grade = "C"
        elif random_score < 90:
            grade = "B"
        else:
            grade = "A"
        print "Score: " + str(random_score) + "; Your grade is " + grade
        i += 1
    print "End of Program. Bye!"


scores_and_grades()


