#################################################
### 반복문 복습 / for문 활용 / 중첩for문 / Mission ###
###############################################

### range() 활용 예제 ###########################
## 0부터 입력한 숫자까지 출력
# num = int(input())
# for i in range(1, num+1):
#     print(i, end=' ')

# for i in range(1, int(input())+1):
#     print(i, end=' ')


## 시작하는 수와 끝나는 수를 입력 받아서 두 수 사이의 숫자를 출력
# num1 = int(input())
# num2 = int(input())
# for i in range(num1, num2+1):
#     print(i, end=' ')

# num = input().split()
# a = [int(i) for i in num]
# print(a)

# num = [int(i) for i in input().split()]
# print(num)
# for i in range(num[0], num[1]+1):
#     print(i, end=' ')


## 1부터 100까지 3의 배수 출력 (10개씩 줄 바꿔서 출력)
# cnt = 0
# for i in range(1, 101):
#     if i%3==0:
#         print(i, end=' ')
#         cnt+=1
#         if cnt%10==0: print()
#     else: continue


### 입력한 값들의 합 구하기 #####################
# a = input()
# a = a.split()
# a = [int(i) for i in a]
# sum = 0
# for i in a:
# 	sum += i
# print(sum)

######################################
# sum = 0
# a = [int(i) for i in input().split()]
# # print(a)
# for i in a:
# 	sum += i
# print(sum)

######################################
# a = sum([int(i) for i in input().split()])
# print(a)

### print(sum([int(i) for i in input().split()]))


### 중첩 for문 #################################
### 삼각형 while
# star = 0                  # 별 갯수를 정해줄 변수 선언
# num = int(input("[입력] "))
# while True:               # 무한반복
#     star += 1             # while 문 수행시 1씩 증가
#     if star > num: break    # star값이 5 이상이면 while문 종료
#     print('*' * star)     # star값 개수만큼 '*' 출력


### 삼각형 for
# n = int(input("[입력] "))
# for i in range(1, n+1):
# 	print('*' * i)


### 삼각형 중첩 for
# n = int(input("[입력] "))
# for i in range(1, n+1):
# 	for j in range(n, i, -1):
# 		print(' ', end='')
# 	print('*' * i)

### 피라미드 중첩 for
# n = int(input("[입력] "))
# for i in range(1, n+1):
# 	for j in range(n, i, -1):
# 		print(' ', end='')
# 	print('*'*(2*i-1), end='')
# 	print('')

### Mission ##################################
### 덧셈 프로그램
## 1부터 입력한 수까지의 합 출력
# sum = 0
# for i in range(1, int(input("숫자 입력: "))+1):
#     sum += i 
# print(sum)


### 구구단 프로그램 
## 사용자에게 입력받은 단의 구구단 출력
# num = int(input("몇 단을 출력할까요? "))
# for i in range(1, 10):
#     print(f"{num} x {i} = {num*i}")


### 3, 6, 9 Game
## 1부터 입력받은 숫자(100 이하의 수)를 출력하면서 3, 6, 9가 들어가는 숫자는 X 출력
# for i in range(1, int(input("[입력] "))+1):
#     if i%10==3 or i%10==6 or i%10==9: print('X', end=' ')
#     elif i>29 and i<40 or i>59 and i<70 or i>89 and i<100: print('X', end=' ')
#     else: print(i, end=' ')


### Project ##################################
### 계산기 프로그램
# while True:
#     print("계산기 프로그램 (종료: 0 입력)")
#     print("==============================")
#     num1 = int(input("첫 번째 숫자 입력: "))
#     if num1 == 0:
#         print("프로그램 종료...")
#         break
#     cal = input("어떤 연산을 실행할까요? (+, -, *, /) ")
#     num2 = int(input("두 번째 숫자 입력: "))
    
#     if cal == '+': print(f"[결과] {num1} {cal} {num2} = {num1+num2}")
#     elif cal == '-': print(f"[결과] {num1} {cal} {num2} = {num1-num2}")
#     elif cal == '*': print(f"[결과] {num1} {cal} {num2} = {num1*num2}")
#     elif cal == '/': print(f"[결과] {num1} {cal} {num2} = {num1/num2}")
#     else: print("잘못 입력하셨습니다.")
#     print("==============================")