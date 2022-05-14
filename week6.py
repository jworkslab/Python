###########################################
### 튜플 / 딕셔너리 / 딕셔너리 함수 / input() ###
#########################################

### 튜플 생성
# t1 = (1, 2, 3)
# t2 = 'a', 'b', 'c'
# print(t1)
# print(t2)
# # t1[1] = 3
# # print(t1)

### 튜플 연산
# print(t1+t2)
# print(t2*2)

### 튜플 슬라이싱
# print(t1[0])
# print(t2[1:3])


### 딕셔너리 생성
#대응관계를 나타내는 자료형 #연관배열 #해시
#key:value의 쌍으로 구성
# dic = {'name':'Jake', 'age':12, 'school':'KDS'}
# print(dic)
# print(dic['name'])

### 딕셔너리 추가/삭제/수정
# dic['class'] = 'Daniel'
# dic['height'] = 180
# print(dic)
# del dic['height']
# print(dic)
# dic['name'] = 'Peter'
# print(dic)

### 딕셔너리 실습 ##########################
# #미션1: 여러 과일들의 가격을 딕셔너리로 선언하기
# fruits = {'apple':500, 'banana':2500, 'mango':2000}	
# print(fruits)

# #미션2: 망고가격 출력
# print("망고는 1개당 %d원 입니다." %fruits['mango'])	
# # print("망고는 1개당 {}원 입니다." .format(fruits['mango']))
# # print(f"망고는 1개당 {fruits['mango']}원 입니다.")

# #미션3: 사과 가격 변경 500 -> 700
# fruits['apple'] = 700	
# print(fruits)

# #미션4: 새로운 과일(오렌지) 추가
# fruits['orange'] = 1200	
# print(fruits)

# #미션5: 바나나 정보 삭제
# del fruits['banana']
# print(fruits)
###########################################


### 딕셔너리 함수
# fruits = {'apple':500,'banana':2500,'mango':2000}
# print(fruits.keys())
# print(fruits.values())
# print(fruits.items())

# #반환된 값들은 다른 형태로 저장이 가능하다
# names = list(fruits.keys())
# print(names)

# prices = tuple(fruits.values())
# print(prices)

# # d1.update(d2) : 딕셔너리 d1을 d2에 맞게 추가/수정
# fruits.update({'apple':700, 'orange':1200})  
# print(fruits)

# #변수 자체가 삭제되는 것이 아니라, 변수 안에 있는 item들만 삭제 됨
# fruits.clear()  
# print(fruits)


### input() 함수
# id = input("아이디를 입력하세요 : ")
# pw = input()
# print(f"ID: {id} / PW: {pw}")

