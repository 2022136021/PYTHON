import turtle as t
import random as r

def circle(r) :
    t.circle(r)

def square(length) :
    for i in range(4) :
        t.fd(length)
        t.left(90)


def drawit(x, y):
    t.up()
    t.goto(x,y)
    t.down()
    t.begin_fill()
    t.color(r.random(),r.random(),r.random())#랜덤 RGB값 지정
    
    circle(r.randint(10,40))
    t.end_fill()

s = t.Screen() #그림판 띄움
s.onscreenclick(drawit) #마우스 클릭 이벤트 처리함수 등록.

t.done()
