### 주석
# one line commant
"""
multiline commant
line 1
line 2
...
"""

'''
line 1
line 2
'''

# 출력 함수 print()
# print(10)
# print(10.3)
# print("안녕")
# print("10")
# print(5+5)
# print(5*5)
# print(5/5)
# print(5-5)

## 자료형 : 자료의 형태 / 값의 종류
# type()
# print(type(10)) #int : 정수 / ... -3, -1, -1 , 0, 1, 2, 3 ... 
# print(type(10.5))  #float : 실수 / 소수점을 가진 숫자
# print(type(5+5))
# print(type(5-5))
# print(type(5*5))
# print(type(5/2))  #나눗셈은 항상 float 자료형 반환
# print(type("hello"))  #str(string) : 문자열
# print(type("10"))
# print(type(10))

# print(5**2)  #제곱근
# print(10/3)  #몫과 나머지를 float 형식으로 반환
# print(type(10//3))  #몫만 반환
# print(type(10%3))  #나머지만 반환

## 변수
# 이름 = "Jake"
# 나이 = 20
# print(이름)
# print(나이)
# print(type(이름))
# print(type(나이))

### 변수의 연산
# num = 0
# print(num)
# num += 1  #num = num + 1
# print(num)

# name = "Jake"
# age = 27
# school = "GCCoding"
# height = 177.9

# print("안녕하세요.")
# print("제 이름은", name, "입니다.")
# print("제 나이는", age, "살 이구요, 키는", height, "입니다.")
# print(school, "에 다니고 있어요.")
# print("만나서 반갑습니다.")


## 비교연산
# A = 10
# B = 15

# print(A == B)
# print(A != B)
# print(A > B)
# print(A < B)


### 포맷팅
# name = "Jake"
# age = 27
# height = 177.9

# ## 포맷 기호
# print("제 이름은 %s입니다." %name)
# print("제 나이는 %d살이구요, 키는 %.2fcm 입니다." %(age, height))

# ## 포맷 함수 & 인덱스
# print("제 이름은 {}입니다.".format(name))
# print("제 나이는 {}살이구요, 키는 {}cm 입니다.".format(age, height))

# print("제 나이는 {1:.2f}살이구요, 키는 {0}cm 입니다.".format(age, height))

# ## f-string
# print(f"제 이름은 {name}입니다.")
# print(f"제 나이는 {age}살이구요, 키는 {height:.2f}cm 입니다.")


## 포맷팅 연습
# id = "JSAM"
# pw = "1234"
# num = 27

# #포맷 기호
# print("%s회원님, 가입해주셔서 감사합니다." %id)
# print("회원님은 저희 까페에 %d번째 가입자 이십니다." %num)
# print("가입하신 비밀번호는 %s입니다. 감사합니다." %pw)

# #포맷 함수
# print("{}회원님, 가입해주셔서 감사합니다.".format(id))
# print("회원님은 저희 까페에 {}번째 가입자 이십니다.".format(num))
# print("가입하신 비밀번호는 {}입니다. 감사합니다.".format(pw))

# #f-스트링
# print(f"{id}회원님, 가입해주셔서 감사합니다.")
# print(f"회원님은 저희 까페에 {num}번째 가입자 이십니다.")
# print(f"가입하신 비밀번호는 {pw}입니다. 감사합니다.")

# print("이름을 입력해주세요:")
# id = input("이름을 입력해주세요: ")
# print(id, type(id))
# pw = input("비밀번호를 입력해주세요: ")
# print(pw, type(pw))

# print("계산기 프로그램")
# num1 = int(input("첫번째 숫자 입력: "))
# num2 = int(input("두번째 숫자 입력: "))
# print(f"{num1} + {num2} = {num1+num2}")
# print(type(num1), type(num2))

## exercise
## 두 개의 숫자 입력 받아서 사칙연산 결과 출력
num1 = int(input("첫 번째 숫자: "))
num2 = int(input("두 번째 숫자: "))

print(f"{num1} + {num2} = {num1+num2}")
print(f"{num1} - {num2} = {num1-num2}")
print(f"{num1} * {num2} = {num1*num2}")
print(f"{num1} / {num2} = {num1/num2:.2f}")