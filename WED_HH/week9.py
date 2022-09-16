### 반복문 for

# friends = ['황희', '피카츄', '꼬부기']
# print(friends[0])

# index = 0
# while index < 3:
#     print(friends[i])
#     i += 1

#for 변수 in 배열:
#for 변수 in 순서가 있는 자료형:

# for name in friends:
#     print(name)


### 딕셔너리 x for
# stdnt = {'name':'황희', 'school':'중앙고', 'grade':'1학년', 'class':'4반'}
# # print(stdnt['name'])

# for i in stdnt: #딕셔너리는 key 값이 전달된다
#     print(i)

### continue
# score = {'수학':100, '영어':80, '국어':80,
#         '체육':70, '과학':90, '사회':70}

# for i in score:
#     # 80점 이상인 과목 축하메시지 출력
#     # "축하합니다. {수학} 패스했습니다."
#     # if score[i] >= 80:
#     #     print(f"축하합니다. {i} 패스했습니다.")
#     if score[i] < 80:
#         continue
#     else:
#         print(f"축하합니다. {i} 패스했습니다.")


### range()
# r1 = list(range(11)) #range(끝값+1) #0부터 끝값까지 출력
# print(r1)

# r2 = list(range(3, 11)) #range(시작값, 끝값+1) #시작값부터 끝값까지 출력
# print(r2)

# r3 = list(range(3, 11, 2)) #range(시작값, 끝값+1, 간격)
# print(r3)

### for x range()
# for i in range(11):     #0부터 10까지 반복
#     print(i, end=' ')

# for i in range(1, 11):    #1부터 10까지 반복
#     print(i, end=' ')

### 1~100사이 홀수 출력
# for i in range(1, 11):
#     print(i, end=' ')

# num = int(input("숫자입력: "))
# # print(num, type(num))

# for i in range(num):
#     print()

# cnt = 0
# for i in range(3, 100, 3):
#     print(i, end = ' ')
#     cnt += 1
#     if cnt%10 == 0:
#         print()
        
num = int(input("숫자입력: "))

for i in range(1, num+1):
    if num % i == 0: #약수
        print(i, end=' ')
