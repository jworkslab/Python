### 튜플 / 딕셔너리 
## 리스트 복사
# l1 = [1, 2, 3]
# l2 = l1[:]  # list(l1)
# print(l1)
# print(l2)
# print(l1 == l2) #비교연산자 == 는 값을 비교
# print(l1 is l2) #is 연산자 : 같은 객체인지 비교

### 튜플 복사 : 튜플 복사해도 객체가 생성되지 않는다 / 링크연결
# t1 = (1, 2, 3)
# t2 = t1[:]   # tuple(t1)
# print(t1)
# print(t2)
# print(t1 == t2)
# print(t1 is t2)


### 딕셔너리
# fruits = {'apple':500, 'banana':2500, 'mango':2000}
# print(fruits)
# print("망고는 1개당 %d원 입니다." %fruits['mango'])
# print("바나나는 1개당 {}원 입니다.".format(fruits['banana']))
# print(f"사과는 1개당 {fruits['apple']}원 입니다.")

# fruits['apple'] = 700
# fruits['orange'] = 1200
# del fruits['banana']
# print(fruits)





##################################
#### MISSION ####################
################################

### 중간미션 ###

# ### mission 1
# print("과천코딩 매점에 오신 것을 환영합니다!")
# menu = [['구운감자', '고래밥', '초코송이'],
# 	    ['코코팜', '초코우유', '쿨피스']]

# print("과자 종류: {}".format(menu[0]))
# print("음료 종류: {}".format(menu[1]))
# print("-------------------------------------------------")

# # 1) 신메뉴 간식을 입력받아, 변수 snack에 저장하세요.
# # 2) 변수 snack은 menu에 있는 과자 종류에 추가하세요.
# # 3) 신메뉴 추가후, 가나다 순으로 정렬하여 출력하세요.
# #    수정된 메뉴 출력시, f-string을 사용해서 출력해주세요.



# ### mission 2
# print("메뉴의 가격을 수정해 주세요.")
# snack = [('구운감자', 1000),
# 		('고래밥', 2000),
# 		('초코송이', 1500)]
# print(snack)

# # 1) 새로운 과자 메뉴를 입력받아, 변수 new에 저장합니다.
# # 2) 해당 과자의 가격을 입력받아, 변수 price에 저장하세요.
# #    단, 가격은 문자열이 아닌 정수형으로 대입되어야 합니다.
# # 3) 변수 new과 price를 튜플로 묶어, 변수 snack의 두 번째 자리에 대입하세요.



# ### mission 3
# # 리스트 속 딕셔너리 수정하기
# # 아래 연락처 목록에서 준우의 휴대폰 번호를 010-1004-1004로 수정하세요.
# phoneList = [{'name':'은정', 'phone':'010-1234-5678'},
#             {'name':'준우', 'phone':'010-0000-6789'}]

# print(phoneList)


### 제어문
### 조건문 if
num = int(input("Enter the number: "))
if num > 50:
    print(f"{num} is bigger than 50")
elif num < 50:
    print(f"{num} is less than 50")
else:
    print(f"{num} is 50")
