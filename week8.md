################################################
### 반복문 while / 무한반복 / random() ###
##############################################

###열 번 찍어 안 넘어가는 나무 없다
# count = 0
# while count < 10:
#     count += 1
#     print(f"나무를 {count}번 찍었습니다.")
#     # if count == 10:
#     #     print("나무 넘어간다!")
# print("나무 넘어간다!")


### Login PG Upgrade
# member = ['Tommy', 'Marry', 'Jake1234']
# ID = input("Enter your new ID: ")

# if len(ID) >= 5 and ID not in member:
#     print(f"Welcome, {ID}")
#     member.append(ID)
# else:
#     print("Try Again ...")
# print("Logout! Bye!!")


# cnt = 3

# while cnt > 0:
#     loginID = input("Enter your ID: ")
#     if loginID in member:
#         print("Login Success")
#         # break
#     else:
#         print("Try again...")
#         cnt -= 1

# while True:
#     loginID = input("Ener your ID: ")
#     if loginID in member:
#         print("Login Success")
#         break
#     else:
#         print("Try again...")


### mission1 : 별 찍기
star = 0                  # 별 갯수를 정해줄 변수 선언
while True:               # 무한반복
    star += 1             # while 문 수행시 1씩 증가
    if star > 5: break    # star값이 5 이상이면 while문 종료
    print('*' * star)     # star값 개수만큼 '*' 출력


### mission2 : 학교에 가면
# school = []

# while True:
#     reply = input("학교에 가면~?! ")
#     if reply not in school:
#         school.append(reply)
#         print(f"{reply}(이)가 있고!")
#     else:
#         print("탈락~!!")
#         break

### for문 활용
# school = []

# while True:
#     reply = input("학교에 가면~?! ")
#     if reply not in school:
#         school.append(reply)
#         for i in school: print(f"{i}(이)가 있고!", end=' ')
#     else:
#         print("탈락~!")
#         break
