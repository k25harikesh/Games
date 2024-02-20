import random

done = False
wins, losses, ties = 0, 0, 0
names = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}

while not done:
    pl_choise = input('Your next move (R, P, S) (Q for Quitting): ').upper()
    ai_choise = random.choice(['R', 'P', 'S'])

    if pl_choise == ai_choise:
        print(f"It's a tie, you both picked {names[ai_choise]}")
        ties += 1
    elif pl_choise == "R":
        if ai_choise == "P":
            losses += 1
            print(
                f"AI wins! You chose {names[pl_choise]}, and AI chose {names[ai_choise]}")
        else:
            wins += 1
            print(
                f"You won! You chose {names[pl_choise]}, and AI chose {names[ai_choise]}")
    elif pl_choise == "P":
        if ai_choise == "S":
            losses += 1
            print(
                f"AI wins! You chose {names[pl_choise]}, and AI chose {names[ai_choise]}")
        else:
            wins += 1
            print(
                f"You won! You chose {names[pl_choise]}, and AI chose {names[ai_choise]}")
    elif pl_choise == "S":
        if ai_choise == "R":
            losses += 1
            print(
                f"AI wins! You chose {names[pl_choise]}, and AI chose {names[ai_choise]}")
        else:
            wins += 1
            print(
                f"You won! You chose {names[pl_choise]}, and AI chose {names[ai_choise]}")
    elif pl_choise == "Q":
        done = True
    else:
        print("Invalid Command")

    print(f"Current stats is Wins:{wins}, Losses:{losses} and Ties:{ties} ")
    print("")
