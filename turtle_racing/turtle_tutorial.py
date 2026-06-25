import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']



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

def create_turtles(colors):
    turtles = []
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        turtles.append(racer)

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle Racing!')

racers = get_number_of_racers()
init_turtle()
random.shuffle(COLORS)
colors = COLORS[:racers]
