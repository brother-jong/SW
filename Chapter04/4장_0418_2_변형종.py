'''
작성일 : 2023년 4월 18일
학과 : 컴퓨터공학부
학번 : 202395018
이름 : 변형종
설명 : 현재 월을 입력 받아 계절을 출력하시오. 잘 못 입력하면 해당 월은 없음. 라고 출력
'''

# 해당 월을 입력받는다.
month = int(input("월을 입력하세요.: "))

# 만약 월이 1~12월 사이이면
if 1<=month<=12 :
    # 만약 월이 3~5월 사이이면
    if 3<=month<=5 :
        # 봄입니다.
        print("봄입니다.")
        # 아니고 만약 월이 6~8월 사이이면
    elif 6<=month<=8 :
        # 여름입니다.
        print("여름입니다.")
        # 아니고 만약 월이 9~11월 사이이면
    elif 9<=month<=11 :
        # 가을입니다.
        print("가을입니디.")
        # 아니면
    else :
        # 겨울입니다.
        print("겨울입니다.")
# 아니면
else :
    print("해당 월은 없습니다.")