### 제어문
## 반복문 while

# count = 0

# while count < 10:
#     count += 1
#     print(f"나무를 {count}번 찍었습니다.")
#     # if count == 10:
#     #     print("나무가 넘어간다~!")
# print("나무가 넘어간다~!")


## 로그인 프로그램
# member = ['user1', 'user2', 'user3']

# ### 아이디 입력이 틀렸을 경우 3번 반복 질문
# count = 3

# while count > 0:
#     count -= 1
#     id = input("아이디를 입력하세요: ")

#     if id in member:
#         print("로그인 되었습니다.")
#         break
#     else:
#         print("존재하지 않는 아이디 입니다.")
    
#     if count == 0:
#         print("3회 실패. 아이디를 확인해주세요.")

# count = 0

# while count < 10:    #조건이 항상 참 = 무한반복
#     print("무한반복")

# count = 0
# while True:    #조건이 항상 참 = 무한반복
#     count += 1
#     print(f"무한반복 {count}")
#     if count == 10:
#         break

# loop = True
# count = 0

# while loop:    #조건이 항상 참 = 무한반복
#     count += 1
#     print(f"무한반복 {count}")
#     if count == 10:
#         loop = False


### 별찍기

star = 0
while True:   #무한반복 
    star += 1
    if star >= 5:
        break
print('*' * star)

