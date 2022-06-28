#배운 내용
'''round(값1, 값2): 반올림 함수 값2에는 원하는 자리에서 반올림한 결과를 출력
문자열 포매팅: 문자열 안에 어떤 값이나 변수 따위를 삽입하는 방법
'''
#2번째 프로젝트
#내가 짠 코드
print("Welcome to the tip calculator")
bill = input("What was the total bill? $")
tip = input("What percentage tip would you like to give? 10, 12, or 15?")
people = input("How many people to split the bill?")
tips = float(tip)*0.01
tip = float(bill)*tips #TypeError: can't multiply sequence by non-int of type 'float' 라는 오류가 발생해 이렇게 코드를 작
total=((float(bill)+tip)/int(people))
print(round(total,2))

#다른 사람이 짠 코드
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15?"))
people = int(input("How many people to split the bill?"))
bill_with_tip = tip / 100 * bill + bill # bill* (1 +tip/100) 도 가능
total_bill = bill_with_tip/people
final_amount = round(total_bill,2)
print(f"Each person should pay: $ {final_amount}")

'''오류가 났던 코드
print("Welcome to the tip calculator")
bill = input("What was the total bill? $")
tip = input("What percentage tip would you like to give? 10, 12, or 15?")
people = input("How many people to split the bill?")
total = float(bill)+(float(tip)*0.01*bill)
print(total)
#TypeError: can't multiply sequence by non-int of type 'float'발생
에러 발생한 이유는 5번째 줄에 float(tip)*0.01까지는 정상적으로 실행되고 마지막에
bill은 str 타입이라 str*float라는 상황이 되어서 오류가 발생함 
'''
