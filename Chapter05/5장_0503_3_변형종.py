'''
작성일 : 2023년 5월 3일
학과 : 컴퓨터공학부
학번 : 202395018
이름 : 변형종
설명 : 1부터 1000까지의 정수 중 사용자가 입력한 숫자의 배수만을 더하여 출력하는 프로그램을 작성하시오. while, continue 사용
'''

# 1. 정수를 입력받는다. (배수 - input_num)
# 2. 입력받은 정수가 1부터 (num)
# 3. 합계는 0
# 4. 수가 10까지 반복하면서
#   a 수를 1 증가시킨다.
#   1) 만약에 수가 입력받은 수의 배수이면 :
#       -합계를 계산한다.
#       b-1수를 1 증가시킨다.
#   c 수를 1 증가시킨다.
#   2) 아니면(배수가 아니면) :
#       b-1수를 1 증가시킨다.
#       - 다시 처음으로 돌아간다. continue
#   e 수를 1 증가시킨다.
# 5. 합계를 출력한다.

input_num = int(input("정수를 입력하세요: "))
num = 0
sum = 0
while num <= 10 :
    num = num + 1 # 증감식
    if num % input_num == 0 :
        sum = sum + num
    else :
        continue
print("{}의 배수의 합 : {}" .format(input_num, sum))

print("-----------------------------------------------------------------------------")

input_num = int(input("정수를 입력하세요: "))
num = 1
sum = 0
while num <= 10 :
    if num % input_num == 0 :
        sum = sum + num
        num = num + 1 # 증감식
    else :
        num = num + 1 # 증감식
        continue
print("{}의 배수의 합 : {}" .format(input_num, sum))

print("---for 반목문-----------------------------------------------------------------------------")

input_num = int(input("정수를 입력하세요: "))

sum = 0

for num in range(1, 11) : # 1부터 10까지 반복
    if num % input_num == 0 : # 0이면
        sum = sum + num # 합해라
    else : # 나머지가 0이면
        continue # 다시 돌아감
        

print("{}의 배수의 합 : {}" .format(input_num, sum))
