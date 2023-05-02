'''
작성일 : 2023년 5월 2일
학과 : 컴퓨터공학부
학번 : 202395018
이름 : 변형종
설명 : 첫번째 입력 받은 수부터 두번째 입력 받은 수까지 반복하면서
'''

# 두개의 정수 입력 받기
# 합계는 0
# 수는 첫번째 입력 받은 수부터
# 수는 두번째 입력받은 수까지 반복하면서
# 합계 계산
# 수는 1씩 증가
# 합계 출력

num1 = int(input("첫번째 수를 입력해주세요: "))
num2 = int(input("두번째 수를 입력해주세요: "))

# 판단 => 변수 값 교환
if num1 >= num2:
    temp = num1
    temp = num2
    num2 = temp

sum = 0
num = num1

while num <= num2:
    sum = sum + num
    num = num + 1
print("{}부터 {}까지의 합은 {}입니다." .format(num1, num2, sum))