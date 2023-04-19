'''
작성일 : 2023년 4월 19일
학과 : 컴퓨터공학부
학번 : 202395018
이름 : 변형종
설명 : 숫자 연산자 숫자 순으로 입력 받아 사칙연산 ~ + - * / 외의 연산자를 입력하면 해당 연산자가 없습니다. 를 출력
'''

# 첫번쨰 수와 두번째 수를 변수 num1,2로 저장 연산자는 cal
num1 = int(input("첫번째 수를 입력해주세요: "))
cal = input("연산자를 입력해주세요: ")
num2 = int(input("두번째 수를 입력해주세요: "))

# 만약 연산자가 +이면~
if (cal == "+") :
    print("{}{}{}={}입니다." .format(num1, cal, num2, num1+num2))
# 아니고 만약 연산자가 -이면``
elif (cal == "-") :
    print("{}{}{}={}입니다." .format(num1, cal, num2, num1-num2))
# 아니고 만약 연산자가  *이면~
elif (cal == "*") :
    print("{}{}{}={}입니다." .format(num1, cal, num2, num1*num2))
# 아니고 만약 연산자가 /이면~
elif (cal == "/") :
    print("{}{}{}={}입니다." .format(num1, cal, num2, num1/num2))
# 해당 연산자가 없으면~
else :
    print("해당 연산자가 없습니다.")
    
