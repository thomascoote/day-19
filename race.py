from tokenize import String
from turtle import Turtle, Screen
import random
from types import NoneType

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
winner = "none"
"""Set icons to Turtle shape"""
for i in racer_list:
    i.shape("turtle")
    i.speed(5)

"""Set Screen"""
screen = Screen()
screen.setup(width=500,height=400)

def starting_line():
    list_of_positions = [0,-30,-60,-90,30,60,90]
    for i in racer_list:
        i.penup()
        random_pos = random.choice(list_of_positions)
        i.goto(x=-230, y=random_pos)
        list_of_positions.remove(random_pos)

def random_forwards():
    for i in racer_list:
        i.forward(random.randrange(0,6))
        if i.xcor() > float(100.00):
            return i.pencolor()


"""Move turtles to starting positions"""
starting_line()

user_choice = screen.textinput(title="Make your bet!",prompt="Who will win the race? Red/Orange/Yellow/Green/Blue/Indigo/Violet").lower()

while True:
    winner = random_forwards()
    if winner is not None:
        print(f"The winner is {winner}!")
        break
    else:
        pass

if winner == user_choice:
    print("Congratulations!")
else:
    print("Sorry!")
exit()
screen.exitonclick()