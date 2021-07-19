import random


def janKenPoi(round, p1_score, p2_score):
    if (p1_score >= 3):
        printScore(p1_score, p2_score)
        print("You win!")
        return
    elif (p2_score >= 3):
        printScore(p1_score, p2_score)
        print("You lose!")
        return

    printScore(p1_score, p2_score)

    # todo: render rivals play
    play2 = renderPlay()

    # todo: ask player for play
    play1 = input("Choose rock, paper, scissors? ").lower()

    print("You: " + play1)
    print("Rival: " + play2)

    checkWinner(play1, play2, p1_score, p2_score, round)


def printScore(score1, score2):
    print("Your score: " + str(score1))
    print("Rivals score: " + str(score2))


def renderPlay():
    plays = ['rock', 'paper', 'scissors']
    num = random.randint(0, 2)

    return plays[num]


def checkWinner(play1, play2, p1_score, p2_score, round):
    if (play1 == "rock" and play2 == "scissors"):
        print("Rock beats scissors.")
        p1_score += 1
        round += 1
        janKenPoi(round, p1_score, p2_score)
    elif (play1 == "rock" and play2 == "paper"):
        print("Paper beats rock.")
        p2_score += 1
        round += 1
        janKenPoi(round, p1_score, p2_score)
    elif (play1 == "rock" and play2 == "rock"):
        print("Draw")
        round += 1
        janKenPoi(round, p1_score, p2_score)
    elif (play1 == "paper" and play2 == "scissors"):
        print("Scissors beat paper.")
        p2_score += 1
        round += 1
        janKenPoi(round, p1_score, p2_score)
    elif (play1 == "paper" and play2 == "paper"):
        print("Draw!")
        round += 1
        janKenPoi(round, p1_score, p2_score)
    elif (play1 == "paper" and play2 == "rock"):
        print("Paper beats rock!")
        p1_score += 1
        round += 1
        janKenPoi(round, p1_score, p2_score)
    elif (play1 == "scissors" and play2 == "scissors"):
        print("Draw!")
        round += 1
        janKenPoi(round, p1_score, p2_score)
    elif (play1 == "scissors" and play2 == "paper"):
        print("Scissors beat paper!")
        p1_score += 1
        round += 1
        janKenPoi(round, p1_score, p2_score)
    elif (play1 == "scissors" and play2 == "rock"):
        print("Rock beats scissors.")
        p2_score += 1
        round += 1
        janKenPoi(round, p1_score, p2_score)


# invoke janKenPoi (start game)
janKenPoi(0, 0, 0)
