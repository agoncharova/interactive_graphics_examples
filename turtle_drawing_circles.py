from turtle import Screen
import turtle as t
import random
tim = t.Turtle()
tim.shape("turtle")
t.colormode(255)

# RANDOM WALK
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r, g, b)
    return random_color

for _ in range(36):
    tim.speed('fastest')
    tim.color(random_color())
    tim.begin_fill()
    tim.circle(80)
    tim.left(10)

# screen = Screen()
# screen.exitonclick()
