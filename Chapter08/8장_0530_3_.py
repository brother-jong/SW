'''
작성일 : 2023년 5월 30일
학과 : 컴퓨터공학부
학번 : 202395018
이름 : 변형종
설명 : 8장 파일 입출력
'''

# open() 함수로 파일 읽기 - read() 메소드
# 파일에 쓸 내용
f = open("C:/Users/gudwhd/Documents/test.txt", "r") # 파일 오픈(읽기)
text= f.read()
print(text)
f.close() # 파일 종료