### 함수2 / 함수의 형태

#매개변수와 반환값 모두 없는 경우
# def welcome():
#     print("환영합니다~!")

# welcome()


#매개변수만 경우
# def welcome(user):
#     print(f"{user}님, 환영합니다~!")

# id = input("아이디를 입력하세요: ")

# welcome(id)


#반환값만 경우
# def welcome():
#     num = 10*10  #알고리즘, 연산식
#     return num

# print(welcome())

#매개변수와 반환값 모두 있는 경우
# def welcome(user):
#     print(f"{user}님, 로그인 되었습니다~!")
#     return "환영합니다~!"

# id = input("아이디를 입력하세요: ")

# print(welcome(id))


# def sum(n1, n2):
#     # t = n1+n2
#     # print(t)
    
#     # print(n1+n2)

#     return print(n1+n2)

# # def sum(n1, n2):
# #     return n1+n2

# sum(10, 2)


# def cal(n1, n2):
#     sum = n1 + n2
#     sub = n1 - n2
#     mul = n1 * n2
#     div = n1 / n2
#     return [sum, sub, mul, div]

# print(cal(10, 5))


# def sum(*num):
#     total = 0
#     for i in num:
#         total += i
#     return total

# numbers = [int(i)for i in input("숫자들 입력: ").split()]

# print(sum(*numbers))


### 수행평가
#1. 약수 구하기
# def ys(n):
#     for i in range(1, n+1):
#         if n % i == 0: 
#             print(i, end=' ')

# num = int(input("숫자입력: "))
# ys(num)

#2. 약수의 합 구하기
# def yssum(n):
#     sum = 0
#     for i in range(1, n+1):
#         if n % i == 0: 
#             sum += i
#     print(sum)

# num = int(input("숫자입력: "))
# yssum(num)

#3. 약수의 개수
# def yscnt(n):
#     cnt = 0
#     for i in range(1, n+1):
#         if n % i == 0: 
#             cnt += 1
#     print(cnt)

# num = int(input("숫자입력: "))
# yscnt(num)

#4. 소수 구분하기
# def ss(n):
#     cnt = 0
#     for i in range(1, n+1):
#         if n % i == 0:
#             cnt += 1
#     if cnt == 2:
#         print(f"{n}은 소수입니다.")
#     else:
#         print(f"{n}은 소수가 아닙니다.")

# num = int(input("숫자 입력: "))
# ss(num)

# 사칙연산
# def add(a, b):
#     c = a + b
#     print(c)

# def sub(a, b):
#     c = a - b
#     print(c)

# def mul(a, b):
#     c = a * b
#     print(c)

# def div(a, b):
#     c = a / b
#     print(c)

# n1 = int(input("첫번째 숫자: "))
# n2 = int(input("두번째 숫자: "))

# add(n1, n2)
# sub(n1, n2)
# mul(n1, n2)
# div(n1, n2)


## 별찍기

# 별찍기_1
# def star1(n): #사각형
#     for i in range(1,n+1):
#         for j in range(1,n+1):
#             print("*",end=" ")
#         print()
def star1(n): #사각형
    for i in range(1,n+1):
        print("* " * n)
        
# 별찍기_2
# def star2(n):  #삼각형
#     for i in range(1,n+1):
#         for j in range(1,i+1):
#             print("*",end=" ")
#         print()
# def star2(n):  #삼각형
#     for i in range(1,n+1):
#         print("* " * i)

# 별찍기_3  #역삼각형
# def star3(n):
#     for i in range(1,n+1):
#         for j in range(i,n+1):
#             print("*",end=" ")
#         print()
# def star3(n):
#     for i in range(n, 0, -1):
#         print("* " * i)
        
# def star4(n): #대칭 삼각형
#     for i in range(1,n+1):
#         for j in range(i,n):
#             print(" ", end = ' ')
#         print('* ' * i)

star1(5)
# star2(5)
# star3(5)
# star4(5)
