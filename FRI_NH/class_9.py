### 모듈(Module)
### 패키지(Package)
### 파일 입출력 

## mod.py 모듈 생성
# total = 0

# def add(*argm):
#     global total
#     return sum(argm)
# # anum = []
# num = input("숫자 입력: ").split()
# # for i in num:
# #     anum.append(int(i))
# num = [int(i) for i in num]

# print(add(*num))


# class CalNum: #carmel type #Cal_num : snake type
#     def __init__(self, a, b):
#         self.n1 = a
#         self.n2 = b
    
#     def add(self):
#         return self.n1+self.n2

# cal1 = CalNum(10, 20)
# n1 = cal1.add()

# class CalNum_child(CalNum):
#     def sub(self):
#         return self.n1-self.n2

#     def add(self):
#         return self.n1 + self.n2 + 10


# cal2 = CalNum_child(n1, 15)
# print(n1)
# print(cal2.add())
# print(cal2.sub())

### 모듈(module)
# import mod

# mod.add(10, 5)
# mod.sub(20, 12)

# from mod import *

# add(10, 5)
# sub(20, 12)
# mul(10, 3)

# import mod

# cal1 = mod.Cal()
# cal1.add(10)
# cal1.sub(3)

# from mod import Cal

# cal1 = Cal()
# cal1.add(10)
# cal1.sub(3)


### 내장 모듈 
# import calendar

# calendar.prmonth(2022, 9)
# print(calendar.calendar(2003))

### math 모듈
# import math

# print(math.gcd(127, 12))
# print(math.lcm(127, 12))
# print(math.sqrt(10))

## random 모듈
# import random
# from random import *

# l  = ['Tom', 'Jerry', 'Spike', 'Jake', 'Nahyun']

# print(randint(1, 100))
# print(choice(l))
# print(sample(l, 2))
# shuffle(l)
# print(l)

### time 모듈
# import time

# print(time.time())
# print(time.gmtime())
# print(time.localtime())
# print(time.ctime())

# for i in range(1, 11):
#     print(i)
#     time.sleep(1)
# print('Boo!')


### 주사위 게임
# import random

# print("Dice GAME~!@!")
# for i in range(3):
#     print("==================================")
#     com_dice = random.randint(1, 6)

#     if input("Enter 키를 눌러 주사위를 던지세요~!") == '':
#         user_dice = random.randint(1, 6)
#     print(f"컴퓨터: {com_dice}, 사용자: {user_dice}")
#     if user_dice > com_dice: print("user win!")
#     elif user_dice < com_dice: print("com win!")
#     else: print("draw game")
#     print("==================================")


### 패키지

from calcpkg import *

num_list = [int(i) for i in input("숫자 입력: ").split()]
cal1 = operation.Calc(*num_list)

print(cal1.add())