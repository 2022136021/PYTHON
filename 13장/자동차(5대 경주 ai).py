import random
from turtle import *

class Car:
    def __init__(self, speed, color, fname, x, y, number):
        self.speed = speed
        self.color = color
        self.number = number            # 자동차 번호 정보도 보유
        self.turtle = Turtle()
        self.turtle.shape(fname)
        self.turtle.speed(self.speed)
        self.turtle.penup()
        self.turtle.goto(x, y)

    def drive(self, distance):
        self.turtle.forward(distance)

# 결승선 그리기 함수
def draw_finish_line(x_line, y_top, y_bottom):
    line = Turtle()
    line.hideturtle()
    line.speed(0)
    line.penup()
    line.goto(x_line, y_top)
    line.pendown()
    line.right(90)
    line.pensize(5)
    line.forward(y_top - y_bottom)

register_shape("car2.gif")

car_list = []
x = -350
y = 150
gap = 70
finish_x = 250
draw_finish_line(finish_x, y + 30, y - (gap * 4) - 30)

# 자동차에 번호 부여(1, 2, 3, 4, 5)
for i in range(5):
    car_list.append(Car(random.randint(1, 10), "red", "car2.gif", x, y - i * gap, i + 1))

arrived_cars = []         # [ (순위, 자동차 번호, 도착 x좌표) ] 형태로 기록

while len(arrived_cars) < 5:    # 모두 결승선 도착 시까지 반복
    for car in car_list:
        if car not in [c[1] for c in arrived_cars]:  # 이미 도착한 차는 더는 움직이지 않는다
            car.drive(random.randint(10, 30))
            if car.turtle.xcor() >= finish_x:
                rank = len(arrived_cars) + 1
                arrived_cars.append( (rank, car, car.turtle.xcor()) )
                car.turtle.write(
                    f"{rank}등!", align="left", font=("Arial", 16, "bold")
                )

# 도착한 순서대로 결과 정리 및 출력
print("=== 결승 결과 ===")
for rank, car, xpos in arrived_cars:
    print(f"{rank}등: {car.number}번 자동차 (최종 x: {int(xpos)})")

done()
