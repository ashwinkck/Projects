name = input("Type your name: ")
print(f"Welcome {name} to this adventure! ")

answer = input("You are on a dirt road, it has come to an end you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across. Type walk to walk around and swim to swim across: ")

    if answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game")
    elif answer == "swim":
        print("You swam across and were eaten by an alligator")

    else:
        print("Type any one of the options")

elif answer == "right":
    print()
else:
    print("Not a valid answer bro! You loose like always!!")
