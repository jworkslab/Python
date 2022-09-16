### 중첩 if

### 멤버십 연산자 in
# l = [1, 3, 5, 7, 9]
# num = int(input("숫자 입력: "))

# print(7 in l)


# s = "Hello, world!"
# text = input("입력: ")

# print('s' not in s)


### 반복문 while 
# member = ['Tommy', 'Marry', 'Jake1234']
# ID = input("Enter your new ID: ")

# ### 계정생성 PG
# if len(ID) >= 5 and ID not in member:
#     print(f"Welcome, {ID}")
#     member.append(ID)
# else:
#     print("Try Again ...")
# print(member)

# ### 로그인 PG
# trylog = 3

# while trylog > 0: #반복 조건: 횟수 try 값이 0보다 클동안 반복
#     # trylog -= 1 #1
#     print("로그인")
#     log_ID = input("아이디 입력: ")
#     if log_ID in member:
#         print("로그인 성공")
#         break
#     else:
#         print("로그인 실패. 다시 입력해주세요.")
#         # trylog -= 1 #2
#     # trylog -= 1 #3

### 별 출력 1, 2
# cnt = int(input("횟수 입력: ")) #횟수 입력
# star = 1

# while  star <= cnt: #조건식
#     print('*' * star)
#     star += 1 #변화식

### 1. 0이 입력되기 전까지 입력된 숫자를 리스트에 추가하기
### 2. 사용자가 입력한 값들의 총 합을 출력하세요.

# l = []
# total = 0

# while True:
#     num = int(input("숫자 입력: "))
#     if num != 0:
#         l.append(num)
#         total += num  #total = total + num
#     else:
#         print(l)
#         break
# print(total)

### 디버깅
# l = []

# while True:
#     num = input("숫자 입력: ")
#     if num == '':
#         continue
#     elif int(num) != 0:
#         l.append(int(num))
#     else:
#         print(l)
#         print(sum(l))
#         break
