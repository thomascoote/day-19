from turtle import Turtle, Screen
import random

"""Set turtles"""
red_t = Turtle()
red_t.color("red")

orange_t = Turtle()
orange_t.color("orange")

yellow_t = Turtle()
yellow_t.color("yellow")

green_t = Turtle()
green_t.color("green")

blue_t = Turtle()
blue_t.color("blue")

indigo_t = Turtle()
indigo_t.color("indigo")

violet_t = Turtle()
violet_t.color("violet")

racer_list = [red_t,orange_t,yellow_t,green_t,blue_t,indigo_t,violet_t]

"""Set icons to Turtle shape"""
for i in racer_list:
    i.shape("turtle")
    i.speed(5)

"""Set Screen"""
screen = Screen()
screen.setup(width=500,height=400)

print(racer_list[0])

def starting_line():
    list_of_positions = [0,-30,-60,-90,30,60,90]
    for i in racer_list:
        i.penup()
        random_pos = random.choice(list_of_positions)
        i.goto(x=-230, y=random_pos)
        list_of_positions.remove(random_pos)

def random_forwards():
    for i in racer_list:
        i.forward(random.randrange(2,6))

def check_win():
    for i in racer_list:
        if i.xcor() > 0:
            return print(f"The winner is {i}")

"""Move turtles to starting positions"""
starting_line()

while True:
    random_forwards()
    check_win()
screen.exitonclick()