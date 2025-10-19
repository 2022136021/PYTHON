# 반복문과 터틀 그래픽을 결합하여 스파이럴 그리기

import turtle as t

colors = ["red", "orange", "blue", "yellow", "green", "purple"]

t.bgcolor("black")

t.speed(0)

t.width(10)

length = 10

while length < 500:
    t.forward(length)
    t.pencolor(colors[length%6])
    t.right(89)
    length +=5

t.done()
