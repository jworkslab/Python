### 중간미션 ###

# ### mission 1
# print("과천코딩 매점에 오신 것을 환영합니다!")
# menu = [['구운감자', '고래밥', '초코송이'],
# 	    ['코코팜', '초코우유', '쿨피스']]

# print("과자 종류: {}".format(menu[0]))
# print("음료 종류: {}".format(menu[1]))
# print("-------------------------------------------------")

# # 1) 신메뉴 간식을 입력받아, 변수 snack에 저장하세요.
# # 2) 변수 snack을 menu에 있는 과자 종류에 추가하세요.
# # 3) 신메뉴 추가 후, 가나다 순으로 정렬하여 출력하세요.
# #    수정된 메뉴 출력시, f-string을 사용해서 출력해주세요.
# snack = input("새로운 간식을 입력해 주세요: ")
# menu[0].append(snack)
# menu[0].sort()
# menu[1].sort()
# print(menu)
# print(f"과자 종류: {menu[0]}")
# print(f"음료 종류: {menu[1]}")



### mission 2
# print("메뉴의 가격을 수정해 주세요.")
# snack = [('구운감자', 1000),
# 		('고래밥', 2000),
# 		('초코송이', 1500)]
# print(snack)

# # 1) 새로운 과자 메뉴를 입력받아, 변수 new에 저장합니다.
# # 2) 해당 과자의 가격을 입력받아, 변수 price에 저장하세요.
# #    단, 가격은 문자열이 아닌 정수형으로 대입되어야 합니다.
# # 3) 변수 new과 price를 튜플로 묶어, 변수 snack의 두 번째 자리에 추가하세요.
# new = input("새로운 과자를 입력하세요: ")
# price = int(input("새로운 과자의 가격을 입력하세요: "))

# # add_menu = (new, price)
# snack.insert(1, (new, price))
# print(snack)


### mission 3
# 리스트 속 딕셔너리 수정하기
# 아래 연락처 목록에서 준우의 휴대폰 번호를 010-1004-1004로 수정하세요.
# phoneList = [{'name':'은정', 'phone':'010-1234-5678'},
#             {'name':'준우', 'phone':'010-0000-6789'}]

# print(phoneList)
# phoneList[1]['phone'] = '010-1004-1004'
# print(phoneList)

# new_name = input("추가할 이름 입력: ")
# new_phone = input("추가할 연락처 입력: ")
# phoneList.append({'name':new_name, 'phone':new_phone})
# print(phoneList)


