### 3, 6, 9

# num = int(input("숫자 입력: "))

# for i in range(1, num+1):
#     # 1의 자리에 3 or 6 or 9 가 들어가는 경우
#     if i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
#         print('X', end = ' ')
#         # 10의 자리에 3 or 6 or 9 가 들어가는 경우
#     elif i // 10 == 3 or i // 10 == 6 or i // 10 == 9:
#         print('X', end = ' ')
#     else:
#         print(i, end = ' ')


### 1 부터 입력한 값까지 합
# num = int(input("숫자 입력: "))

# for i in range(1, num+1):

### 두 주사위를 굴렸을 때 나올 수 있는 경우의 수 출력
# dice = []
# for d1 in range(1, 7):
#     for d2 in range(1, 7):
#         print(d1, d2)

### 함수 (function)
## 외장함수

import random
# import time

print(random.randint(1, 100))
# print(time.ctime())
# print(time.localtime())
# while True:
#     print(time.sleep(1))
#     print(time.ctime())
#     # if input(''): break