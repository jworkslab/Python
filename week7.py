################################################
### 제어문 / 조건문 if / 중첩 if / 멤버십 연산자 in ###
##############################################

### 조건문 if
# num = int(input("Enter a digit number: "))

# if num > 5:
#     print("Your number is more than 5")
# elif num < 5:
#     print("Your number is less than 5")
# else:
#     print("Your number is 5")


### 중첩 if 문
# num = int(input("Enter a digit number: "))

# if num > 5:
#     print("Your number is more than 5")
#     if num % 2 == 0:
#         print(f"{num} is even number")
#     else: 
#         print(f"{num} is odd number") 
# elif num < 5:
#     print("Your number is less than 5")
#     if num % 2 == 0:
#         print(f"{num} is even number")
#     else: 
#         print(f"{num} is odd number") 
# else:
#     print("Your number is 5")
#     print(f"{num} is odd number")


### if문과 논리연산
# num = int(input("Enter a digit number: "))

# if num > 5 and num % 2 == 0:
#     print("Your number is more than 5")
#     print(f"{num} is even number")
# elif num > 5 and num % 2 != 0:
#     print("Your number is more than 5")
#     print(f"{num} is add number")
# elif num < 5 and num % 2 == 0:
#     print("Your number is less than 5")
#     print(f"{num} is even number")
# elif num < 5 and num % 2 != 0:
#     print("Your number is less than 5")
#     print(f"{num} is odd number")
# else:
#     print("Your number is 5")
#     print(f"{num} is odd number")


### 멤버십 연산자 in
# l = [1, 3, 5, 7, 9]
# print(3 in l)

# s = 'Hello'
# print('a' not in s)


### mission
### log in program v2
### 변수 ID에 신규 가입자의 아이디를 입력 받습니다.
### 신규 가입자의 아이디가 5글자 이상이어야 아이디 생성 가능
### 신규 가입자의 아이디가 기존 멤버와 중복되지 않아야 아이디 생성 가능

# member = ['Tommy', 'Marry', 'Jake1234']
# ID = input("Enter your new ID: ")

# if len(ID) >= 5 and ID not in member:
#     print(f"Welcome, {ID}")
# else:
#     print("Try Again ...")