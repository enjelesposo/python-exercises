import random
# Ask user if rolling up or down


def askRoll(tries, score):
    if(score == 21):
        print("Nice job!")
    elif(tries == 0):
        print("You lose :(")
    else:
        print("Roll up to 21")
        print("Current: " + str(score))
        print("Tries left: " + str(tries))
        roll = input("Roll the dice up or down? ").lower()

        if(roll == "up"):
            rollUp(tries, score)
        elif(roll == "down"):
            rollDown(tries, score)


def rollUp(tries, score):
    num = random.randint(1, 6)
    print(str(num))
    score += num
    tries -= 1
    askRoll(tries, score)


def rollDown(tries, score):
    num = random.randint(1, 6)
    print(str(num))
    score -= num
    tries -= 1
    askRoll(tries, score)


askRoll(10, 0)
