'''
작성일 : 2023년 5월 24일
학과 : 컴퓨터공학부
학번 : 202395018
이름 : 변형종
설명 : 실습 예제 7-1
'''
# 실습 예제 7-1
# 랜덤으로 1~100 사이의 값을 10개 생성한 세트 2개 만들고,
# 합집합, 교집합, 차집합을 출력하시오.
# [알고리즘]
# 1. 비어있는 세트 2개 만들기
# 2. 랜덤으로 2개의 세트에 각각 10개의 값을 저장
#   랜덤, 반복하면서 10개의
#   1) 값 저장(추가)
# 3. 2개의 세트 값 출력
#   합집합, 교집합, 차집합 출력
import random
num1 = set() # set() 함수로 비어있는 세트 생성
num2 = set()

for i in range(10) :
    num1.add(random.randint(1,10))
    num2.add(random.randint(1,10))
print("set1 내용: ", num1)
print("set2 내용: ", num2)
print("set1과 set2의 합집합: ", num1 | num2)
print("set1과 set2의 교집합: ", num1 & num2)
print("set1과 set2의 차집합: ", num1 - num2)