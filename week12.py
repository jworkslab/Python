#####################
### Function 함수 ###
###################

### 구구단
# # 2단
# for i in range(1, 10):
#     print(f"2 x {i} = {2*i}")

# # 3단
# for i in range(1, 10):
#     print(f"3 x {i} = {3*i}")

# # 3단
# for i in range(1, 10):
#     print(f"3 x {i} = {3*i}")

### 구구단 (함수 사용)
# def multable(num):
#     for i in range(1, 10):
#         print(f"{num} x {i} = {num*i}")

# multable(2)
# multable(3)
# multable(4)


# EX1 ##########################
### 매개변수와 반환값이 없는 경우
# def multable():
#     for i in range(1, 10):
#         print(f"2 x {i} = {2*i}")

# multable()

### 매개변수만 있는 경우
# def multable(num):
#     for i in range(1, 10):
#         print(f"{num} x {i} = {num*i}")

# multable(int(input("[입력] ")))

### 반환값만 있는 경우
# def multable():
#     print(f"2 x 1 = ", end='')
#     return 2*1

# multable()
# print(multable())

### 매개변수와 반환값이 모두 있는 경우
# def multable(num):
#     for i in range(1, 10):
#         print(f"{num} x {i} = {num*i}")
#     return f"{num}단 끝~!"

# print(multable(2))

# EX2 ##########################
### 매개변수와 반환값이 없는 경우
# def welcome():
#     print("환영합니다~!")

# welcome()

### 매개변수만 있는 경우
# def welcome(user):
#     print(f"{user}님, 환영합니다~!")

# name = input("이름을 입력하세요: ")
# welcome(name)

### 반환값만 있는 경우
# def welcome():
#     return "환영합니다~!"

# welcome()
# # print(welcome())

### 매개변수와 반환값이 모두 있는 경우

# def welcome(user, cnt):
#     print(f"{user}님, 환영합니다~!")
#     cnt += 1
#     return cnt

# num = 0
# name = input("이름을 입력하세요: ")

# print(f"{welcome(name, num)}번째 손님 입장")


### 결과값이 여러개인 경우
# def cal(n1, n2):
#     sum = n1 + n2
#     sub = n1 - n2
#     mul = n1 * n2
#     div = n1 / n2
#     return sum, sub, mul, div

# num1 = int(input("[입력 1] "))
# num2 = int(input("[입력 2] "))

# # print(cal(num1, num2))
# result = cal(num1, num2)
# print(f"덧셈: {result[0]}, 뺄셈: {result[1]}, 곱셈: {result[2]}, 나눗셈: {result[3]:.2f}")

### Mission ###
# Get the area of Triangle / Rectangle / Circle
# def tri(base, high):
#     area = base * high / 2
#     return area

# def rect(base, high):
#     area = base * high
#     return area

# def circle(radius):
#     area = radius**2 * 3.14
#     return area

# while True:
#     print("어떤 도형의 넓이를 구할까요?(단위:cm)")
#     order = input("[선택] 삼각형 / 사각형 / 원 : ")
#     if order == '삼각형':
#         b = int(input(f"{order}의 밑변을 입력하세요: "))
#         h = int(input(f"{order}의 높이를 입력하세요: "))
#         print(f"{order}의 넓이는 {tri(b, h)}입니다.")
#     elif order == '사각형':
#         b = int(input(f"{order}의 밑변을 입력하세요: "))
#         h = int(input(f"{order}의 높이를 입력하세요: "))
#         print(f"{order}의 넓이는 {rect(b, h)}입니다.")
#     elif order == '원':
#         r = int(input(f"{order}의 반지름을 입력하세요: "))
#         print(f"{order}의 넓이는 {circle(r)} 입니다.")
#     else:
#         slt = input("잘못 입력하셨습니다. (계속: r / 종료: q)")
#         if slt == 'q': break

