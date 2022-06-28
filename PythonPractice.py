#bmi 계산기
#내가 짠 코드
height = input("enter your height in m:")
weight = input("enter your weight in kg:")
height = float(height)
weight = int(weight)
bmi = (weight/(height*height))
bmi = int(bmi)
print("your bmi is",bmi)

#다른 사람이 짠 코드
height = input("enter your height in m:")
weight = input("enter your weight in kg:")
bmi = int(weight) / float(height) ** 2
bmi_as_int = int(bmi)
print(bmi_as_int)
