#배운 내용
#3번째 프로젝트
'''피자 가격 계산
작은 사이즈:15$, 중간 사이즈 20$, 큰 사이즈 25$
페퍼로니 추가:2$
치즈추가 3$'''
#내가 짠 코드

print("Welcom to the Pizza Deliveries!")
size = input("What size pizza do you want?")
add_pepperoni = input("Do you want pepperoni?")
extra_cheese = input("Do you want extra cheese?")
total = 0

if size == "S":
    total += 15
    if add_pepperoni == "Y":
        total += 2
        if extra_cheese == "Y":
            total += 3
elif size =="M":
    total += 20
    if add_pepperoni == "Y":
        total += 2
        if extra_cheese == "Y":
            total += 3
else :
    total += 25
    if add_pepperoni == "Y":
        total += 2
        if extra_cheese == "Y":
            total += 3

print(total)
#문제점: else문을 그대로 사용하면 이상한 값을 입력시 큰 사이즈 피자로 계산이 되기 때문에 else를 elif로 바꾸고 마지막에 else문에는 이상한 값이 입력되면 다시 입력하라는 내용을 추가하
    
#다른 사람이 짠 코드
print("Welcom to the Pizza Deliveries!")
size = input("What size pizza do you want?")
add_pepperoni = input("Do you want pepperoni?")
extra_cheese = input("Do you want extra cheese?")
total = 0

if size == "S":
    total += 15
elif size == "M":
    total += 20
else:
    total += 25

if add_pepperoni == "Y":
    total += 2
elif extra_cheese == "Y":
    total += 3
print(total)
