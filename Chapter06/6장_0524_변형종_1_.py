# 튜플 생성
tuple1 = () # 빈 튜플 생성.
tuple2 = ('a',) # 원소가 하나여도 쉼표는 필수
tuple3 = ('a','b','c')

color = ('red','blue','white','white','pink','green')
print("color 내용: ", color)
print("color의 길이: ", len(color)) # len 길이
print("white의 개수: ", color.count('white')) # count 개수
print("green의 위치: ", color.index('green')) # 주소 index

# 실습 예제 6-7
# 2개의 튜플을 하나의 리스트로 만들기
fruit = ('사과', '배', '딸기', '복숭아', '망고')
price = (1000, 2000, 3000, 4000, 5000)

# 결과: [사과, 1000, 배, 2000, ....]
fp_list = [] # 2개의 튜플 내용이 저장될 리스트 생성
fp_tuple = () # 2개의 튜플 내용이 저장될 튜플 생성

for i in range(len(fruit)) :
    fp_list.append(fruit[i])
    fp_list.append(price[i])
    # fp_tuple.append(fruit[i]) # 튜플은 변경이 안됨. append(추가) 그래서 안됨.
    
    
print("과일 목록: ", fruit)
print("가격 목록: ", price)
print("과일 가격 리스트: ", fp_list)