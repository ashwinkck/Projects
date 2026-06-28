import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
COLORS = ['RED', 'GREEN', 'BLUE', 'ORANGE', 'YELLOW', 'BLACK', 'PURPLE', 'PINK', 'BROWN', 'CYAN']



def get_number_of_racers():
    racers = 0
    while True:
        racers = input("Enter the no of racers (2 - 10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Input should be a number.... Try again!")
            continue

        if 2 <= racers <= 10:
            return racers
        else:
            print("The input should in between (2 - 10)")
def race(colors):
    turtles = create_turtles(colors)

    while True:
        for racer in turtles:
            distance = random.randrange(1,20)
            racer.forward(distance)


            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]


def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i + 1) * spacingx, -HEIGHT//2 + 20)  #putting position x,y
        racer.pendown()
        turtles.append(racer)
    return turtles

def display_winner(color):
    writer = turtle.Turtle()
    writer.hideturtle()
    writer.penup() # preventing drawing lines while moving to pos
    writer.color(color) #Matches the color of the turtle
    writer.setpos(0,0) # Centers the text in the middle of the screen

    #Writes text on the screen
    writer.write(
        f"The winner of this racing game is {color}!",
        align="center",
        font=("Arial",20,"bold")
    )
def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle Racing!')

racers = get_number_of_racers()
init_turtle()
random.shuffle(COLORS)
colors = COLORS[:racers]
winner  = race(colors)
display_winner(winner)
print(f"The winner is the turtle with color: {winner}")
time.sleep(5)