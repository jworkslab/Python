### 반복문 while
# count = 0

# while count < 10:
#     count += 1
#     print(f"나무를 {count}번 찍었습니다.")
#     if count == 10:
#         print("나무 넘어간다~!")


### <숙제> 계정생성 프로그램
member = ['Tommy', 'Marry', 'Jake1234']
cnt = 0

while cnt < 3:
    ID = input("Enter your new ID: ")
    cnt += 1

    if ID in member:
        print(f"Welcome, {ID}")
        break
    else:
        print("Try Again ...")
