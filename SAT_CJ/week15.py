'''
배수와 약수
    8의 배수 : 8, 16, 24, 32, 50 ...
    8이 약수 : 1, 2, 4, 8
    소수(prime number) : 약수가 1과 자기 자신인 숫자 / 2, 3, 5, 7, 11, 13
'''


### 중첩 if문
# num = int(input("숫자 입력: "))

# if num % 2 == 0:
#     print("짝수")
#     # 10보다 크거나 같은지, 작은지
#     if num >= 10:
#         print("10보다 큽니다.")
#     else:
#         print("10보다 작습니다.")

# elif num % 2 == 1:
#     print("홀수")
#     # 10보다 크거나 같은지, 작은지
#     if num >= 10:
#         print("10보다 큽니다.")
#     else:
#         print("10보다 작습니다.")

# else:
#     print(0)
#     print("10보다 작습니다.")


## if와 논리연산 (and, or, not)
# num = int(input("숫자 입력: "))

# if num % 2 == 0 and num >= 10:
#     print("짝수")
#     print("10보다 큽니다.")
# elif num % 2 == 0 and num < 10:
#     print("짝수")
#     print("10보다 작습니다.")

# elif num % 2 == 1:
#     print("홀수")
#     # 10보다 크거나 같은지, 작은지
#     if num >= 10:
#         print("10보다 큽니다.")
#     else:
#         print("10보다 작습니다.")

# else:
#     print(0)
#     print("10보다 작습니다.")


### [숙제]
## 1. 두 개의 숫자를 입력 받는다
## 2. +, -, *, / 중 한 개의 기호를 입력 받는다
## 3. 각 기호에 따른 사칙연산 결과를 출력한다

num1 = int(input("첫 번째 숫자 입력: "))
num2 = int(input("두 번째 숫자 입력: "))

cal = input("연산기호 입력: ")

if cal == '+':
    print(f"{num1} + {num2} = {num1+num2}")
elif cal == '-':
    print(f"{num1} - {num2} = {num1-num2}")
elif cal == '*':
    print(f"{num1} * {num2} = {num1*num2}")
elif cal == '/':
    print(f"{num1} / {num2} = {num1/num2}")
else:
    print("잘못 입력했습니다. +, -, *, / 중에서 입력해주세요.")