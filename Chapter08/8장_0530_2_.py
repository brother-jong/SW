'''
작성일 : 2023년 5월 30일
학과 : 컴퓨터공학부
학번 : 202395018
이름 : 변형종
설명 : 8장 파일 입출력
'''

# open() 함수로 파일 쓰기 - 추가모드ㅡ a
# 파일에 쓸 내용
f = open("C:/Users/gudwhd/Documents/test.txt", "a") # 파일 오픈(추가)
f.write("추가 메세지입니다. \n")
f.close() # 파일 종료