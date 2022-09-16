### review
# students = ['길동', '둘리', '또치', '마이콜']

# index = 0
# while index < len(students):
#     print(students[index])
#     index += 1

# print(students[0])
# print(students[1])
# print(students[2])
# print(students[3])


### 반복문 for
# for i in students:
#     print(i)

### for x dictionary
# score = {'M':100, 'EN':80, 'WB':80, 
#          'CW':70, 'SC':90, 'SS':70}

# print(score['M'])   #딕셔너리에서 값 가져오기

# for i in score:
#     # print(score[i])  
#     # if score[i] >= 80:
#     #     print(f"{i}: 축하합니다!")
#     # else:
#     #     print(f"{i}: 80점 못넘었습니다.")
#     if score[i] < 80: continue
#     print(f"{i}: 축하합니다.")


### range()
# for i in range(10):
#     print(i, end=' ')

# for i in range(3, 10):
#     print(i, end=' ')

# for i in range(3, 10, 3):
#     print(i, end=' ')

# for i in range(10, 1, -1): #range(시작값, 끝값-1, 증감값)
#     print(i, end=' ')


### 활용
# num = int(input("숫자입력: "))

# for i in range(1, int(input("숫자입력: "))+1):
#     print(i, end=' ')

# num1 = int(input("첫번째 숫자: "))
# num2 = int(input("두번째 숫자: "))
# for i in range(num1, num2+1):
#     print(i, end=' ')

# cnt = 0

# for i in range(3, 101, 3):
#     print(i, end=' ')
#     cnt += 1
#     if cnt % 10 == 0:
#         print()

 #split 결과가 리스트로 저장됨
# num = list(int(i) for i in input().split())   #for문으로 리스트의 각 값을 int형으로 변환
# print(num)

### 예제
# num = input().split()
# num = [int(i) for i in num]
# print(sum(num))

### 별찍기 
# num = int(input("숫자입력: "))

# for i in range(1, num+1):
#     print('*'*i)

#####
# num = int(input())
# for i in range(1, num+1):
#     print(' '*(num-i)+'*'*i)

### 중첩 for문
# num = int(input())
# for i in range(1, num+1):
#     for j in range(num, i, -1):
#         print(' ', end='')
#     print('*' * i)

