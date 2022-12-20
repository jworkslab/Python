#9. 입력 받은 2진수를 10진수로 변환해서 출력하세요.
### 문자열 입력
# num = input("2진수 입력: ")
# num = list(int(i) for i in num)
# ex = len(num)-1   #3
# result = 0

# for i in num:
#     result += i * 2 ** ex
#     ex -= 1   #2

# print(result)

### 숫자 입력
# num = int(input("2진수 입력: "))

# ex = 0
# result =0

# while num > 0:
#     result += (num % 10) * 2 ** ex
#     num = num // 10 
#     ex += 1

# print(result)

### 자료형 이용
# num = input("2진수 입력: ")
# print(int(num), 2)

# num = int(input("2진수 입력: "), 2)
# print(num)

# print(int(input("2진수 입력: "), 2))


#10. 두 개의 주사위를 던져서 나올 수 있는 모든 경우의 수를 출력하세요.
### 주사위 1개 던져서 나올 수 있는 경우의 수 : 1~6, 총 6개 
## 주사위 2개 던져서 나올 수 있는 경우의 수: 6 x 6 = 36개

# for dice1 in range(1, 7):
#     for dice2 in range(1, 7):
#         print(f"({dice1}, {dice2})", end=' ')


###############################################
### 파이썬 구조
## 함수

### 외장함수
# import random
# print(random.randint(1, 10))

### 사용자 정의 함수
# def cal(n1, n2):
#     sum = n1 + n2
#     sub = n1 - n2
#     mul = n1 * n2
#     div = n1 / n2
#     return sum, sub, mul, div

# print(cal(1, 2))
l = [1, 2, 3, 4]
len(l)

print(sum(l))


