### [숙제] 별 삼각형 출력
# num = int(input("숫자입력: "))

# star = 1
# while True:
#     if star > num:
#         break
#     elif star <= num:
#         print('*' * star)
#     star += 1

# num = int(input('숫자 입력: '))

# ## 배열: 순서가 있는 자료형 / 인덱스 (딕셔너리 제외)
# for n in range(1, num+1):
#     print('*' * n)

num = int(input('숫자 입력: '))

# for n in range(num, 0, -1):
#     print(' ' * (n-1), end ='')
#     print('*' * (num-n+1))

'''
    range(5)  # 0~4 까지 값 생성
    range(1, 5)   #1~4 까지 값 생성
    range(1, 10, 2) #1~9까지 2 간격으로 값 생성 : 1, 3, 5, 7, 9
    range(10, 0, -1)
'''

# for star in range(1, num+1):
#     for space in range(num-star, 0, -1):
#         print(' ', end='')
#     print('*' * star)


### 피라미드 삼각형
num = int(input("숫자 입력: "))

for star in range():
    for space in range():

## [숙제] 피라미드 별 출력 알고리즘
# star + (star - 1)
# = star + star -1
# 2*star -1
