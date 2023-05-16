'''
작성일 : 2023년 5월 16일
학과 : 컴퓨터공학부
학번 : 202395018
이름 : 변형종
설명 : 사용자로부터 가장 좋아하는 월을 입력 받아 ~ while 문을 사용하여 작성하시오
'''

# 1. 무한 반복하면서
#   1) 월을 입력받아 month에 저장
#   2) 비교, 판단하여 선택
#   1-1) 선택에 따른 결과를 출력

while True :
    month = int(input("가장 좋아하는 월을 입력해주세요: "))
    if month == 0 :
        print("프로그램을 종료합니다.")
        break
    
    elif month == 3 or month == 4 or month == 5 :
        print("***** {}월 *****" .format(month))
        print("{}월은 봄에 해당됩니다." .format(month))
    elif month == 6 or month == 7 or month == 8 :
        print("***** {}월 *****" .format(month))
        print("{}월은 여름에 해당됩니다." .format(month))
    elif month == 9 or month == 10 or month == 11 :
        print("***** {}월 *****" .format(month))
        print("{}월은 가을에 해당됩니다." .format(month))
    elif month == 12 or month == 1 or month == 2 :
        print("***** {}월 *****" .format(month))
        print("{}월은 겨울에 해당됩니다." .format(month))
    else :
        print("해당 월은 없습니다.")