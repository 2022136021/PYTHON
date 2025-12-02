import random
from turtle import *

class Car:
    def __init__(self, speed, color, fname, x, y):
        self.speed = speed
        self.color = color
        self.turtle = Turtle()
        self.turtle.shape(fname)
        self.turtle.speed(self.speed)
        self.turtle.penup()
        self.turtle.goto(x, y)

    def drive(self, distance):
        self.turtle.forward(distance)


register_shape("car2.gif")

car_list = []
x = -350
y = 150
gap = 70

for i in range(5):
    car_list.append(Car(random.randint(1, 10), "red", "car2.gif", x, y -i * gap))

for i in range(10):
    for car in car_list:
        car.drive(random.randint(10, 30))

