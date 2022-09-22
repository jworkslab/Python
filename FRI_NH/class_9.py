### 모듈(Module)
### 패키지(Package)
### 파일 입출력 

## mod.py 모듈 생성
'''
def sum(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    return a / b
'''

###############################
# import mod

# print(mod.mul(3, 5))

###############################
# import calendar

# calendar.prmonth(2022, 9)
# print(calendar.calendar(2022))

### Dice Game
# from random import *

# while True:
#     com = randint(1, 6)
#     print("=======================")
#     print(f"컴퓨터 주사위: {com}")
#     if input("주사위를 던지세요!") == '':
#         user = randint(1, 6)
#         print(f"사용자 주사위: {user}")

#     if user > com: print("사용자가 이겼습니다.")
#     elif user < com: print("컴퓨터가 이겼습니다.")
#     else: print("비겼습니다.")


### Up & Down Game
# from random import randint

# num = randint(1, 100)
# cnt = 0

# while True:
#     cnt += 1
#     answer = int(input("1 부터 100 사이의 숫자를 입력하세요: "))
#     if num > answer: print("UP")
#     elif num < answer: print("Down")
#     else: 
#         print("Bingo~!")
#         break
# print(f"{cnt}번 만에 맞추셨습니다.")



# import time

# print(time.time())
# print(time.gmtime())
# print(time.localtime())
# print(time.ctime())

### Timer
# from time import sleep

# sec = int(input("시간(초) 입력: "))
# for i in range(sec, 0, -1):
#     print(i)
#     sleep(1)
# print("Time Out!!")


