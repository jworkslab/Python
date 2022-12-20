### 제어문 / 조건문 if
# num = 8
# if num == 10:
#     print(f"num 은 {num}입니다.")
#     print("지금은 조건문 if 안에 있습니다.")
# print("지금은 조건문 if 밖에 있습니다.")

# num = int(input("숫자 입력: "))

# if num > 5:
#     print("입력한 숫자는 5보다 큽니다.")
#     if num % 2 == 0: #num이 짝수라면?
#         print("짝수 입니다.")
#     elif num % 2 == 1: # num % 2 != 0 #홀수인 조건
#         print("홀수 입니다.")
#     else:
#         print("0 입니다.")
# elif num < 5:   #elif : else if 의 약자
#     print("입력한 숫자는 5보다 작습니다.")
#     ### 코딩해 주세요~! ###

# else:
#     print("입력하신 숫자는 5 입니다.")
#     print("홀수입니다.")


### 조건문 if 와 논리연산 (and, or, not)

# num = int(input("숫자 입력: "))

# if num > 5 and num % 2 == 0:
#     print("입력한 숫자는 5보다 큰 짝수 입니다.")
# elif num > 5 and num % 2 == 1: # num % 2 != 0 #홀수인 조건
#     print("입력한 숫자는 5보다 큰 홀수 입니다.")
# elif num < 5:   #elif : else if 의 약자
#     print("입력한 숫자는 5보다 작습니다.")
#     ### 코딩해 주세요~! ###
    
# else:
#     print("입력하신 숫자는 5 입니다.")
#     print("홀수입니다.")

### 멤버십 연산자 in 
# l = [1, 2, 3, 4, 5]
# print(3 in l)
# print(7 in l)

# s = "Hello"
# print('e' not in s)
# print('a' not in s)


### mission
# member = ['Tommy', 'Jaemyung', 'Marry']
# ID = input("새로운 아이디를 입력하세요: ")

### 조건문과 in 활용
## ID가 member에 있다면, "이미 가입된 아이디입니다."
## ID가 member에 없다면, "가입완료! 환영합니다~!"

# if ID in member:
#     print("이미 가입된 ID 입니다.")
# # elif ID == member[1]:
# #     print("이미 가입된 ID 입니다.")
# # elif ID == member[2]:
# #     print("이미 가입된 ID 입니다.")
# else:   #예외처리, 조건이 없다(그 외의 조건)
#     print("가입완료! 환영합니다~!")


member = ['Tommy', 'Jaemyung', 'Marry']
ID = input("새로운 아이디를 입력하세요: ")

if ID in member:
    print("이미 가입된 ID 입니다.")
else:
    print("가입완료! 환영합니다~!")