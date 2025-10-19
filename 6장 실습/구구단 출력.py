# 구구단 2단부터 9단까지 한 화면에 전부 출력

'''
for i in range(1, 10, 1):
    for dan in range(2, 10, 1):
        print("| %d X %d = %2d |" %(dan, i, dan*i), end = "   ")
    print("\n")
'''


for i in range(10) :
    for dan in range(2,10) :
        if i==0:
            print(f"=={dan}단==", end="   ")
        else:
            print("%d*%d=%2d" % (dan, i, dan*i), end="    ")
    print("\n")

for i in range(10) :
    for dan in range(9,1, -1) :
        if i==0:
            print("|%5d%s    |" %(dan, "단"), end = '   ')
        else:
            print("| %d X %d = %2d|" %(dan, i, dan*i), end = "   ")
    print("\n")
