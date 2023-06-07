'''
작성일 : 2023년 6월 7일
학과 : 컴퓨터공학부
학번 : 202395018
이름 : 변형종
설명 : 9장 함수와 모듈
'''

import random

# 문제를 만드는 함수
def make_question():
    num1 = random.randint(1, 48) # 랜덤으로 1 ~ 48까지 생성
    num2 = random.randint(1, 20) # 랜덤으로 1 ~ 20까지 생성
    op = random.randint(1, 3) # 랜덤으로 생성 후 op에 저장
    
    que = str(num1) # num1 문자열 변환
    
    if op == 1: 
        que = que + '+' # 문자 연산자와 연결
    if op == 2:
        que = que + '-'
    if op == 3:
        que = que + '*'
        
    que = que + str(num2) # num1 연산자 num2 연결
    
    return que


R_ans = 0 # 정답
W_ans = 0 # 오답

for i in range(5): # 5번 반복
    que = make_question()
    print(que, end='')
    
    result = int(input('='))
    
    if eval(que) == result:
        print('정답입니다.')
        R_ans += 1
        
    else:
        print('오답입니다.')
        W_ans += 1
        
print('정답: ', R_ans, '오답: ', W_ans)

if W_ans == 5: # 5문제 나옴
    print('당신은 천재입니다.')