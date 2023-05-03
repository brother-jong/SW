'''
작성일 : 2023년 5월 3일
학과 : 컴퓨터공학부
학번 : 202395018
이름 : 변형종
설명 : 하나의 숫자를 입력받아 팩토리얼을 구하는 프로그램을 작성하시오
'''
# num으로 수 입력받기
# 팩토리얼 = 1
# for 사용
# 출력
num = int(input("팩토리얼을 구할 숫자를 입력하세요: "))
factorial = 1
for i in range(num, 0, -1):
    factorial = factorial * i
print("{}! = {}".format(num, factorial))
##################################################################################
num = int(input("팩토리얼을 구할 숫자를 입력하세요: "))
factorial = 1
for num1 in range(1, num+1):
    factorial *= num1
print("{}! = {}".format(num, factorial))