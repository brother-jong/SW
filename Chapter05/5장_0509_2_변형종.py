'''
작성일 : 2023년 5월 9일
학과 : 컴퓨터공학부
학번 : 202395018
이름 : 변형종
설명 : 5과목의 성적을 입력 받아~ 입력한 성적이 0~100점 사이가 아닌 경우~ 출력하고 과목을 입력 받으시오.
'''

num = 1
total = 0

while num <= 5 :
    score = int(input(str(num) + "첫번째 성적 입력")) # @번째 성적
    
    if(0<= score <= 100) : # 0~100 사이
        total = total + score # 총점 + 입력받은 성적
        print(num, "첫번째 성적 :", score)
        num = num + 1
    else :
        print("유효한 성적이 아닙니다.")
print("총점 :", total) # 총점
print("평균 :", total / 5) # 평균