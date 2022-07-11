#################
### Mid Test ###
###############

#[Homework Check]##############################
### 삼각형 출력
# line = int(input("[입력] "))

# for i in range(1, line+1):
#     print('*' * i)


### 수평으로 뒤집어진 삼각형 출력
# line = int(input("[입력] "))

# for i in range(1, line+1):
#     for j in range(i, line):
#         print(' ', end='')
#     print('*' * i)

# line = int(input("[입력] "))

# for i in range(1, line+1):
#     for j in range(line, i, -1):
#         print(' ', end='')
#     print('*' * i)


### 피라미드 삼각형 출력
# line = int(input("[입력] "))

# for i in range(1, line+1):
#     for j in range(i, line):
#         print(' ', end='')
#     print('*' * (2*i-1))


### 문제 10 ###
# num = int(input("[입력] "))

# for i in range(1, num+1):
#     if i%10 in [3, 6, 9]: print('X', end=' ')
#     elif i//10 in [3, 6, 9]: print('X', end=' ')
#     else: print(i, end=' ')
