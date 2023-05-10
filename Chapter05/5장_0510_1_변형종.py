'''
작성일 : 2023년 5월 10일
학과 : 컴퓨터공학부
학번 : 202395018
이름 : 변형종
설명 : 사용자로부터 하나의 정수를 입력 받아 다음과 같이 ★을 출력하는 프로그램을 작성하시오.
'''

# 문제 분석
# 입력 받는 수 : num
# 반복이 중첩된다.
# 입력 받은 수까지 반복하면서 줄을 만든다.
# 칸은 줄만큼 반복하면서 ★을 출력한다.
# 줄을 반복 [칸 반복 (줄까지)]


#1. 정수 입력
#2. 입력 받은 수(줄)까지 반복하면서
#   1) (칸) 쥴까지 반복하면서
#   1] ★을 출력한다.
    
num = int(input("정수를 입력하세요: "))

for jul in range(num) :
    print("★ "*(jul+1))
    

num = int(input("정수를 입력하세요: "))

for jul in range(1, num+1) :
    for kan in range(jul) :
        print("★", end=' ')
    print() # 줄바꿈