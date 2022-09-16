a = 10
b = 20 

### 비교연산자
# print(a == b) #같다 -> False
# print(a != b) #다르다 -> True
# print(a > b) #크다 -> False
# print(a < b) #작다 -> True
# print(a >= b) #크거나 같다 -> False
# print(a <= b) #작거나 같다 -> True

### 논리연산자

### 포맷팅
# name = '한태인'
# age = 14
# height = 163.9

# ## [출력 예시] 이름: 한태인, 나이: 14, 키: 163.9
# print("이름: ", name, ", 나이: ", age, ", 키: ", height)
# ## 포맷기호
# print("이름: %s, 나이: %d, 키: %.2f" %(name, age, height))
# ## 포맷함수
# print("이름: {}, 나이: {}, 키: {:.2f}".format(name, age, height))
# print("이름: {2:.2f}, 나이: {0}, 키: {1}".format(name, age, height)) #인덱스 활용
# ## f-string
# print(f"이름: {name}, 나이: {age}, 키: {height:.2f}")

### input() : 입력함수
id = input("아이디를 입력하세요: ")
pw = int(input("비밀번호를 입력하세요: "))

print(id, type(id))
print(pw, type(pw))

