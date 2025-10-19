# 무작위 2자리 산수퀴즈를 사용자에게 물어보고 정답, 오답 출력

'''
import random as r


num1 = r.randrange(10, 100)
num2 = r.randrange(10, 100)

op_list = ["x", "/", "+", "-"]
op = r.choice(op_list)

print (f' {num1} {op} {num2} = ?')
user_answer = int(input("정답을 입력해주세요. : "))

answer = 0

if op == "x" :
    answer = num1 * num2
elif op == "/" :
    answer = int(num1 / num2)
elif op == "+" :
    answer = int(num1 + num2)
elif op == "-" :
    answer = int(num1 - num2)

if answer == user_answer :
    print("정답입니다")
else :
    print("오답입니다")
'''


# 무작위 2자리 산수퀴즈를 만들어 사용자의 답과 비교한 후 사용자에게 계속할 지 물어봐서 "yes"라고 하면 산수퀴즈를 계속한다.

import random as r

answerYN = 'yes'

while answerYN == 'yes':
    num1 = r.randrange(10, 100)
    num2 = r.randrange(10, 100)

    op_list = ["x", "/", "+", "-"]
    op = r.choice(op_list)

    print (f' {num1} {op} {num2} = ?')
    user_answer = int(input("정답을 입력해주세요. : "))

    answer = 0

    if op == "x" :
        answer = num1 * num2
    elif op == "/" :
        answer = int(num1 / num2)
    elif op == "+" :
        answer = int(num1 + num2)
    elif op == "-" :
        answer = int(num1 - num2)

    if answer == user_answer :
        print("정답입니다")
    else :
        print("오답입니다")

    answerYN = input("계속 진행을 원하시면 yes를 입력해주세요 : ")
print("프로그램 종료합니다")
