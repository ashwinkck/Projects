import random
print("Welcome to the pig game!")
print("The max score is 50. Whoever reaches 50 first wins")

def roll():
    min_value = 1
    max_value = 6

    roll = random.randint(min_value,max_value)

    return roll

while True:
    players = input("Enter the no of players (2-4): ")
    if players == "q":
        exit()
    if players.isdigit():
        players = int(players)
        if 2<=players<=4:
            break
        else:
            print("Must be between 2-4 players")
    else:
        print("Invalid, try again")


max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:

    current_score = 0
    should_roll = input("Would you like to roll (y)?")
    if should_roll == "q":
        break
    if should_roll.lower() != "y":
        break
    
    value = roll()

    if value == 1:
        print("You rolled a 1! Turn done!")
        break
    else:
        current_score += value
        print(f"You rolled a:{value} value ")


    print(f"Your score is {current_score}")