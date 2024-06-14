import turtle as t
import random

t.colormode(255)

# create an object
hirst = t.Turtle()


color_list = [(246, 242, 235), (247, 240, 244), (239, 242, 247), (237, 245, 240), (212, 149, 95), (215, 80, 62),
              (47, 94, 142), (231, 218, 92), (148, 66, 91), (22, 27, 40), (155, 73, 60), (122, 167, 195), (40, 22, 29),
              (39, 19, 15), (209, 70, 89), (192, 140, 159), (39, 131, 91), (125, 179, 141), (75, 164, 96),
              (229, 169, 183), (15, 31, 22), (51, 55, 102), (233, 220, 12), (159, 177, 54), (99, 44, 63),
              (35, 164, 196), (234, 171, 162), (105, 44, 39), (164, 209, 187), (151, 206, 220), (97, 127, 168),
              (34, 81, 49), (180, 188, 210), (84, 65, 30), (16, 77, 106)]

def random_color():
    choice_color = []
    random.shuffle(color_list)
    choice_color = random.choice(color_list)
    return choice_color


def drawing_dots():
    for i in range(10):
        hirst.color(random_color())
        hirst.dot()
        hirst.penup()
        hirst.forward(50)
        hirst.pendown()

def dot_init():
    hirst.pensize(10)
    hirst.setheading(225)
    hirst.penup()
    hirst.forward(500)
    hirst.pendown()
    hirst.setheading(0)

dot_init()
hirst.speed(0)
for i in range(10):
    drawing_dots()
    hirst.penup()
    hirst.setheading(90)
    hirst.forward(50)
    hirst.setheading(180)
    hirst.forward(500)
    hirst.setheading(0)






screen = t.Screen()
screen.exitonclick()