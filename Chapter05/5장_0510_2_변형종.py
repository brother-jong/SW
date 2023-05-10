'''
작성일 : 2023년 5월 10일
학과 : 컴퓨터공학부
학번 : 202395018
이름 : 변형종
설명 : 2단부터 9단까지 구구단을 출력하시오.
'''

dan = 2
while dan <= 9 :
    print(f'==== {dan}단====')
    jul = 1
    while jul <= 9 :
        if (dan*jul) % 2 == 0 :
            print(f'{dan} x {jul} = {dan*jul}')
        jul += 1
    dan += 1


for dan in range(2,10) :
    print(f'==== {dan}단====')
    for jul in range(1,10) :
        if (dan*jul) % 2 == 0 :
            print(f'{dan} x {jul} = {dan*jul}')