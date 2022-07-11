######################################
### Module / math / random / time ###
####################################

### 사용자 정의 모듈 생성 및 활용
## mod.py 생성 
# import mod

# print(mod.sum(1, 2))
# print(mod.sub(1, 2))
# print(mod.mul(1, 2))
# print(mod.div(1, 2))

### 내장 모듈 활용
## math
# import math

# print(math.gcd(12, 64)) #최대공약수
# print(math.lcm(12, 64)) #최소공배수 
# print(math.sqrt(16))    #16이 되는 제곱근의 값 출력

# ### math.log(x)     # x의 자연로그 반환
# ### math.log(x,y)   # 밑이 y인 x의 로그값 반환
# ### math.log2(x)    # 밑이 2인 x의 로그값 반환

# print(math.log(17, 4))  #17의 자연로그, 또는 밑이 4일 때 17의 로그 값 출력 
#                         ##17을 만드는 4의 제곱근 값 반환
# print(math.log2(17))    #밑이 2인 17의 로그값 출력 (로그, log)
#                         ##17을 만드는 2의 제곱근 값 반환

###############################################
## random
# import random

# s = ['Peter', 'James', 'Andrew', 'John']

# print(random.randint(1, 10))   #a와 b를 포함한 범위에서 랜덤한 정수 반환
# print(random.randrange(1, 10, 3))   #a와 b를 포함한 범위에서 n간격의 랜덤한 정수 반환
# print(random.choice(s))   #s에서 하나의 랜덤 값을 반환
# print(random.sample(s, 2))   #s에서 n개의 값을 반환
# random.shuffle(s)   #s의 순서를 랜덤하게 섞음
# print(s)


###############################################
## time
# import time

# print(time.time())
# # epoch time   # timestamp
# # UTC(GMT+0) 기준으로 1970년 1월 1일 0시 0분 0초부터의 경과 시간
# # UTC, Universal Time Coordinated #협정세계시
# # GMT, Greenwich Mean Time #그리니치 평균시
# # 영국을 기준으로 각 지역의 시차를 규정한 것

# print(time.gmtime())     # timestamp 값을 GMT 기준의 struct_time 타입 데이터로 변환
# print(time.localtime())     # timestamp 값을 현지 시간대 기준의 struct_time 타입 데이터로 변환
# print(time.ctime())     # timestamp를 현지 시간대 기준으로 소위 미국에서 흔히 사용되는 요 월 일 시:분:초 년 포멧으로 변환
# time.sleep(3)     #  프로그램의 실행을 일정 시간(초)동안 지연

###
# tm = localtime(time())

# print("year:", tm.tm_year)
# print("month:", tm.tm_mon)
# print("day:", tm.tm_mday)
# print("hour:", tm.tm_hour)
# print("minute:", tm.tm_min)
# print("second:", tm.tm_sec)


### mission
## 시작 시간과 끝 시간 출력
# from time import *

# print("Measure Time for 5sec ...")
# start = ctime()
# sleep(5)
# end = ctime()
# print(f"start time: {start}\nend time: {end}")

## Time Recorder
# from time import *

# print("===============================")
# print("Timer")
# input("Press Enter to start")
# start = ctime()
# input("Press Enter to end")
# end = ctime()
# print(f"start time: {start}\nend time: {end}")


## Timer
# from time import *

# print("===============================")
# print("Timer")
# sec = int(input("시간을 입력하세요: "))
# while sec != 0:
#     print(sec)
#     sec -= 1
#     sleep(1)
# print("Time Out")


## Stopwatch
# from time import *

# sec = 0
# print("===============================")
# print("Stopwatch")
# input("Press Enter to start")
# start = time()
# input("Press Enter to end")
# end = time()

# print(f"Time: {end-start:.2f}")

###################
### project
### Up & Down Game

# from random import *

# num = randint(1, 100)
# cnt = 0
# print(num)
# while True:
#     answer = int(input("1 부터 100 사이의 숫자를 입력하세요: "))
#     cnt += 1
#     if answer > num: print("Down")
#     elif answer < num: print("Up")
#     else: break
# print(f"Bingo~!\n{cnt}번 만에 맞추셨습니다.")


### 주사위 게임
# from random import *

# print("주사위 게임!")

# for i in range(3):
#     num = randint(1, 6)
#     start = input("Enter키를 눌러 주사위를 던지세요!")

#     if start == '': 
#         user = randint(1, 6)

#     if user > num: print("사용자가 이겼습니다.")
#     elif user < num: print("컴퓨터가 이겼습니다.")
#     else: print("비겼습니다.")