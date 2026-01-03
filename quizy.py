
import random

testQuestion = [("the start of the Revolutionary War", 1775),
                (" United States Constitution get signed?", 1783),
                (" assassination attempt of President Lincoln?", 1865),
                (" President Roosevelt first day in office?", 1901),
                (" beginning of World War II?", 1939),
                (" ending of World War II?", 1945),
                (" first personal computer introduced?", 1975),
                (" Berlin Wall taken down?", 1989),
                ("beginning of the Vietnam War?", 1955),
                ("When was the Edo period?", 1603),
                ("When was the start of the Great Depression? ", 1929)]

playersScore = 0

random.shuffle(testQuestion)

for event, year in testQuestion:
    print(f"In what year was this {event}?")
    try:
        userGuess = int(input())
    except ValueError:
        print("your input was invalid please try again!")

        guessDifference = abs(userGuess - year)

        if guessDifference == 0:
            print("Your answer was correct good job!")
            playersScore += 10

        elif guessDifference <= 5:
            print(
                "Your 5 years off ({year}),  but you still get 5 points!")
            playersScore += 5

        elif guessDifference == 10:
            print(
                "Woah your 10 years off ({year}), close but not close enough!")
            playersScore += 2

        elif guessDifference == 20:
            print("Um... your 20 years off ({year}), oof")
            playersScore += 1

        else:
            print(
                "more than 20 years off ({year}), you get no points loser!")

            print("Your final score is {playerScore}.")
            if playersScore == 100:
                print("Good JOb! You got a perfect Score")
            elif playersScore >= 70:
                print("Good Job! your close to a perfect score")
            elif playersScore >= 40:
                print("Not bad, but you can do better!")
            else:
                print("Damn not even one point")
