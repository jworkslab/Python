### 구구단 출력
# num = int(input("숫자 입력: "))

# for i in range(1, 10):
#     # print("%d x %d = %d"%(num, i, num*i))
#     # print("{} x {} = {}".format(num, i, num*i))
#     print(f"{num} x {i} = {num*i}")
#     # 0 x 0 = 0

### 더하기 프로그램
# total = 0
# num = int(input("숫자 입력: "))

# for i in range(1, num+1):
#     total += i

# print(total)


### 369  -> 숙제
# num = int(input("숫자 입력: "))

# for i in range(1, num+1):
#     if i%10 in [3, 6, 9]:
#         print('X', end=' ')
#     elif i//10 in [3, 6, 9]:
#         print('X', end=' ')
#     else:
#         print(i, end=' ')

## num = 
# 3 : 3, 13, 23, 30~39, 43, 53, 73, 83, 
# 6 : 6, 16, 26, 46, 56, 60~69, 76, 86, 
# 9 : 9, 19, 29, 49, 59, 79, 89, 90~99 

# 1의 자리에 3, 6, 9가 들어가는 경우
#  : num % 10 == 3 or num % 10 == 6 or num % 10 == 9
# 10의 자리에 3, 6, 9가 들어가는 경우
#  : num // 10 == 3 or num // 10 == 6 or num // 10 == 9
