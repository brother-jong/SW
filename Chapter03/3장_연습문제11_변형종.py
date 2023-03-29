'''
작성일 : 2023년 3월 28일
학과 : 컴퓨터공학부
학번 : 202395018
이름 : 변형종
설명 : 연습문제 11
       반지름이 23인 원의 넓이를 구하시오.
'''

# 1. 반지름 23을 r변수에 저장한다.
r = 23

# 2. 원주율 3.14를 pi변수에 저장한다.
pi = 3.14

# 3. 원의 넓이를 계산하여 area변수에 저장한다.
area = r*r*pi # area = (r**2)*pi

# 원의 넓이를 출력한다.
print("반지름이", r, "인 원의 넓이는", area, "cm 입니다.")
print("반지름이 {}인 원의 넓이는 {}cm 입니다." .format(r, area))


'''
설명 : 연습문제 09
       홍김동의 본봉은 300만원이다. 이번 달 수당으로 30만원을 받았으며, 세금으로 총액의 20%를 냈다. 홍길동의 이번 달 월급 수령액을
       구하는 프로그램을 작성하시오.
'''

# 1. 본봉 300만원을 mn변수에 저장한다.
mn = 300

# 2. 수당 30만원을 ext변수에 저장한다.
ext = 30

# 3. 세금을 tax변수에 저장한다.
tax = 66

# 4. 총액을 변수 to에 저장한다.
to = 330

# 5. 총액을 계산한다.
ar = mn + ext - tax

# 6. 세금을 계산한다.
tax = to * 0.2

# 7. 수령액을 계산해서 ar변수에 저장한다.
ar = mn + ext -tax

# 8. 이번 달 수령액을 출력한다.
print("이번 달 수령액은 {}만원 입니다." .format(ar))

