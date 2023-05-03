'''
작성일 : 2023년 5월 3일
학과 : 컴퓨터공학부
학번 : 202395018
이름 : 변형종
설명 : 사용자로부터 입력 받은 숫자에 해당하는 구구단을 출력하는 프로그램을 작성하시오.

[문제 분석]
사용자가 입력한 단 : dan
곱하는 수 : su

입력 받은 단은 고정이다.
곱하는 수는 1부터 9까지 1씩 증가한다.
'''

# 알고리즘 for
# 1. 사용자로부터 단을 입력 받는다.
# 2. 곱하는 수는 1부터 9까지 반복하면서
#   1) 구구단을 출력한다.
print("for 반복문으로 구구단 출력")
dan = int(input("알고 싶은 단을 입력하세요: "))

print(":: {} 단 ::" .format(dan))
for num in range (1, 10):
    print("{} x {} = {}" .format(dan, num, dan*num))


# 알고리즘 while
# 1. 사용자로부터 단을 입력받는다.
# 2. 곱하는 수는 1부터
# 3. 곱하는 수는 9까지
#   1) 구구단 출력
#   2) 곱하는 수 1씩 증가
print("while 반복문으로 구구단 출력")
dan = int(input("알고 싶은 단을 입력하세요: "))

print(":: {} 단 ::" .format(dan))
num1 = 1
while num <= 9:
    print("{} x {} = {}" .format(dan, num, dan*num))
    num = num + 1