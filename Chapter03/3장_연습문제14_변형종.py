'''
작성일 : 2023년 4월 4일
학과 : 컴퓨터공학부
학번 : 202395018
이름 : 변형종
설명 : 연습문제 14번
'''

# 국어를 변수 socre1로 지정하고 값 받기.
score1 = int(input('국어 점수를 입력하시오'))

# 수학를 변수 socre2로 지정하고 값 받기.
score2 = int(input('수학 점수를 입력하시오'))

# 사회를 변수 socre3로 지정하고 값 받기.
score3 = int(input('사회 점수를 입력하시오'))

# 과학를 변수 socre4로 지정하고 값 받기.
score4 = int(input('과학 점수를 입력하시오'))

# 영어를 변수 socre5로 지정하고 값 받기.
score5 = int(input('영어 점수를 입력하시오'))

# 총점을 구하고 변수를 hab으로 저장
hab = (score1 + score2 + score3 + score4 + score5)

# 평균을 구하고 변수 avg로 저장
avg = hab / 5

# 총합과 평균 출력
print("총합은 {}점이고 평균은 {:.2f}입니다.".format(hab, avg))