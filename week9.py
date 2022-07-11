######################################
### 반복문 for / continue / range() ###
#####################################

# students = ['종훈', '은석', '제이크']

### index 활용해서 리스트 요소값 출력
# print(students[0])
# print(students[1])
# print(students[2])

### while문 활용해서 리스트 요소값 출력
# index = 0
# while index < 3:
#     print(students[index])
#     index += 1

### for문 활용해서 리스트 요소값 출력
# for i in students:
#     print(i)

### for문 활용해서 딕셔너리 요소값 출력
# score = {'M':100, 'EN':80, 'WB':80, 
#          'CW':70, 'SC':90, 'SS':70}

# for i in score:
#     print(i)
    # print(i+':',score[i], end=' ')


### continue 사용해 축하메시지 출력
# score = {'M':100, 'EN':80, 'WB':80, 
#          'CW':70, 'SC':90, 'SS':70}

# for i in score:
#     if score[i] < 80: continue
#     print(f"Congratulation for {i} ~!")


### range()
## 횟수를 지정
# for i in range(10):
#     print(i, end=' ')

## 범위를 지정
# for i in range(1, 10):
#     print(i, end=' ')

## 간격을 지정
# for i in range(1, 10, 3):
#     print(i, end=' ')


### range() 활용
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
# # print(num)
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