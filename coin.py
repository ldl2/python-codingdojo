import random


def coinToss():
    head = 0
    tail = 0
    coin = ""
    for i in range(5001):
        random_toss = int(random.random() * 2 + 1)
        if random_toss == 2:
            head += 1
            coin = "head"
        else:
            tail += 1
            coin = "tail"
        print "Attempt #" + str(i) + ": Throwing a coin... It's a " + coin + "!... Got " + str(head) + " head(s) so far and " + str(tail) + " tail(s) so far"
        i += 1


coinToss()