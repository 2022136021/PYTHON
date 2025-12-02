def countVowel(string) :
    count1 = 0
    count2 = 0
    
    for i in string :
        if i in ['a','e','i','o','u'] :
            count1 += 1
        elif i not in ['a','e','i','o','u',' ']:
            count2 += 1
    return count1,count2


    
    
user = input("문자열을 입력받아 모음,자음 갯수 카운팅 : ")

num1, num2 = countVowel(user)

print(f"모음은{num1}, 자음은 {num2}")
