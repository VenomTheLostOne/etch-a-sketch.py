from turtle import *
import turtle

tur = turtle.Turtle()
tur.fillcolor('cyan')
screen = Screen()
screen.title('Etch-A-Sketch')


def move_forward():
    tur.forward(10)


def move_backward():
    tur.backward(10)


def turn_left():
    tur.left(10)


def turn_right():
    tur.right(10)


screen.listen()
screen.onkey(key='w', fun=move_forward)
screen.onkey(key='s', fun=move_backward)
screen.onkey(key='a', fun=turn_left)
screen.onkey(key='d', fun=turn_right)

turtle.done()
