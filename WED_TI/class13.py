### 중간평가
#1. 








# ### review
# ### Part 1. 자료형

# # int : 정수 / ... -3, -2, -1, 0, 1, 2, 3
# # float : 실수 / 소수점을 가진 숫자 
# # str : 문자열 (string) -> 순서가 있는 자료형 / 인덱스(0부터 시작)
# # "Hello, world!" 

# # # 함수 
# # print() : 출력함수
# # input() : 입력함수 -> 항상 str 문자열로 저장

# # list 리스트 : [] / 여러개의 값을 저장 / 수정, 삭제, 추가, 복사 가능
# l.append() 
# l.insert(위치, 값)
# l.pop()
# l.remove()
# # tuple 튜플 : () / 여러개의 값을 저장 / ... 불가능 / 복사하면 링크 연결 

# # dic (dictionary) 딕셔너리 : 여러개의 값을 저장 / 인덱스 x / key : Value
# dic = {'name':'태인', '학교':'과천'}
# dic['name'] = '제이크'
# dic['학년'] = '2학년'
# del dic['key']

# ### part 2. 제어문

# ## 조건문 if
# if 조건식:
#     명령1
#     명령2
#     명령3
# elif 조건식:
#     명령
# else:
#     명령

# ## 반복문 while : 조건에 따른 반복
# while 조건식: 
#     명령

# count = 10
# while count > 0:
#     print(count)
#     count -= 1

# while True:
#     print("무한반복")

# ## 반복문 for
# for 변수 in 배열:  #배열: 순서가 있는 자료형
#     명령

# name = [태인, 제이크, 친구1, 친구2]
# for i in name:
#     print(i)


# for i in range(5): #5번 반복 / 0, 1, 2, 3, 4(5-1)
#     명령

# for i in range(1, 6): #1, 2, 3, 4, 5(6-1)

# for i in range(1, 10, 2):  #1, 3, 5, 7, 9

# for i in range(10, 0, -1): # 10, 9, 8, ..., 2, 1


# for 
#     for
#        액션
#     목적
