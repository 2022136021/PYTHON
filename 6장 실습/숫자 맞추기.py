# 1부터 100 사이의 랜덤한 숫자를 맞추는 프로그램

import random

tries = 0
guess = 0
answer = random.randint(1, 100)

print("1부터 100 사이의 숫자를 맞추시오")

while guess != answer :
    guess = int(input("숫자를 입력하시오 : "))
    tries = tries + 1
    if guess < answer:
        print("낮음!")
    elif guess > answer:
        print("높음!")  
    else :
        print("축하합니다. 시도횟수 = ", tries)

    if tries == 10 :
        print(f'시도 횟수가 10번을 넘겼습니다. ')



'''
while guess != answer and tries < 10:
    guess = int(input("숫자를 입력하시오 : "))
    tries = tries + 1
    if guess < answer :
        print("낮음!")
    if guess > answer :
        print("높음!")
        
if guess == answer :
    print("축하합니다. 시도횟수 = ", tries)
else:
    print(f"아쉽게도 실패하셨습니다.")
'''

