import turtle
import time
WIDTH, HEIGHT = 500, 500


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
def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle Racing!')

racers = get_number_of_racers()
init_turtle()

#Starting to move the turtle, with turtle object
racer = turtle.Turtle()
racer.speed(1)
racer.penup()
racer.shape('turtle')
racer.color('green')
racer.forward(100)
racer.left(90)
racer.pendown()
racer.forward(100)
racer.right(90)
racer.backward(100)

racer2 = turtle.Turtle()
racer2.speed(2)
racer2.penup()
racer2.shape('turtle')
racer2.color('red')
racer2.forward(150)
racer2.left(90)
racer2.pendown()
racer2.forward(150)
racer2.right(90)
racer2.backward(150)

