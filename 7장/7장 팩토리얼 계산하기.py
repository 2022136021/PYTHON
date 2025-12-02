#팩토리얼 함수 구현
"""

#1 사용자에게 숫자를 입력받아 for문 이용하여 팩토리얼 값을 구해 출력



'''
fact = 1
for i in range(2,n+1) : #2~n까지 숫자를 i 변수에 넣음
    fact *= i
print(f"{n}! = {fact}")
'''

#2 정수값을 입력받아 1번을 호출하기
#factorial(n)
"""

#3 정수값을 입력받아 팩토리얼값을 계산하는 함수를 작성하고 호출하기를 반복
# 사용자가 0을 입력하면 프로그램 종료
def factorial(num) :
    fact = 1
    for i in range(2,num+1) : #2~n까지 숫자를 i 변수에 넣음
        fact *= i
    print(f"{n}! = {fact}")    
        
while True :
    n = int(input("1이상의 정수 입력 : "))
    if n == 0 :
        print("종료")
        break
    factorial(n)


#4 팩토리얼 함수를 재귀함수로 바꿔보기 
def calc_fact(n) :
    if n == 1 :
        return
    return calc_fact(n-1) * n

while True :
    n = int(input("1이상의 정수 입력 : "))
    if n == 0 :
        print("종료")
        break
    print(calc_fact(n-1)*n)
    
    
