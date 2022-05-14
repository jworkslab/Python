### 중간미션 ###

### mission 1
print("Welcome to Merit Market~!")
menu = [['구운감자', '고래밥', '초코송이'],
	    ['코코팜', '초코우유', '쿨피스']]

print("과자 종류: {}".format(menu[0]))
print("음료 종류: {}".format(menu[1]))
print("-------------------------------------------------")

# 1) 신메뉴 간식을 입력받아, 변수 snack에 저장하세요.
# 2) 변수 snack은 menu에 있는 과자 종류에 추가하세요.
# 3) 신메뉴 추가후, 가나다 순으로 정렬하여 출력하세요.
#    수정된 메뉴 출력시, f-string을 사용해서 출력해주세요.
snack = input("추가하실 간식 메뉴를 입력해주세요: ")
menu[0].append(snack)
menu[0].sort()
print("신메뉴 과자: ", snack)
print(f"과자 종류: {menu[0]}")
print(f"음료 종류: {menu[1]}")
print("-------------------------------------------------")


### mission 2
print("베스트 도서목록을 수정해 주세요.")
best = [('언어의 온도', 344500),
		('한국사 대모험', 583110),
		('고요할수록 밝아지는 것들', 346830)]
print(best)

# 1) 새로운 책 제목(공부머리 독서법)을 입력받아, 변수 title에 저장합니다.
# 2) 해당 책의 대출번호(450820)를 입력받아, 변수 num에 저장하세요.
#    단, 대출번호는 문자열이 아닌 정수형으로 대입되어야 합니다.
# 3) 변수 title과 num을 튜플로 묶어, 변수 best 3위 자리에 대입하세요.

title = input("제목: ")
num = int(input("번호: "))
best[2] = (title, num)

print(best)


### mission 3
# 리스트 속 딕셔너리 수정하기
# 아래 연락처 목록에서 준우의 휴대폰 번호를 010-1004-1004로 수정하세요.
phoneList = [{'name':'은정', 'phone':'010-1234-5678'},
            {'name':'준우', 'phone':'010-0000-6789'}]

print(phoneList)

# # phoneList[1]['phone'] = '010-1004-1004'
# # print(phoneList)