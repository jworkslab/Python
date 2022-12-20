### for문 복습
'''
for 변수 in [순서가 있는 자료형 / range]:
    명령들...
'''
## 1부터 10 출력
# for number in range(1, 11):
#     print(number)

## 1부터 입력한 값까지 출력
# num = int(input("숫자입력: "))

# for n in range(1, num+1):
#     print(n, end=' ')

## 구구단 출력
# num = int(input("숫자 입력: "))
# for i in range(1, 10):
#     print(f"{num} x {i} = {num*i}")

## 더하기 프로그램
## 변수 활용
# num = int(input("숫자 입력: "))
# total = 0

# for i in range(1, num+1):
#     total += i #total = total + i

## 리스트 활용
# num = int(input("숫자 입력: "))
# num_list = []

# for i in range(1, num+1):
#     num_list.append(i)
# print(num_list)
# print(sum(num_list))

# numbers = input("숫자 입력: ")
# numbers = numbers.split()
# print(numbers)

### [숙제] 별 삼각형 출력
