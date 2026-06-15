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
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back? (cross/back)")

    if answer == "left":
        answer = input("You come to a river, you can walk around it or swim across. Type walk to walk around and swim to swim across: ")

    if answer == "back":
        print("You go back and lose.")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them? (Yes/No)")

        if answer == "yes":
            print("You talk to the stranger and they give you BTC. You WIN!")
        
        elif answer == "no":
            print("You ignore the stranger and they are offended and you LOSE!")

        else:
            print("Not a valid option. You lose.")
    else:
        print("Type any one of the options")
else:
    print("Not a valid answer bro! You loose like always!!")
