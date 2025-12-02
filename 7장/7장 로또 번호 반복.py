import random as r

def getLotto(num) :
    
    lottos = []
    for i in range(num) :        
        lotto = []
        while len(lotto) < 6 :
            n = r.randint(1,45)
            if n not in lotto :
                lotto.append(n)
        lottos.append(lotto)
    return lottos
    
num = int(input("복권 번호 반복 할 횟수 : "))

print(f"생성된 복권 번호  리스트 {getLotto(num)}")
