### 반복문 for
# students = ['재훈' ,'재명', '은석', '하하']

# print(students[0])
# print(students[1])
# print(students[2])

# index = 0
# while index < len(students):
#     print(students[index])
#     index += 1

# for i in students:
#     print(i)


## for & 딕셔너리
# dic = {'MA':90, 'EN':100, 'SS':80, 'SC':70, 'PT':90}
# point = 0
# for d in dic:
#     if dic[d] < 90:
#         # print() #지나가고
#         continue
#     else:
#         print("축하합니다. 1000 포인트 적립되었습니다.")
#         point += 1000
# print(f"총 {point} 포인트 적립되었습니다.")

## range()
## 기본형
# for i in range(5): #하나의 인자값: 횟수 의미, 0 ~ (끝값-1) 생성
#     print(i)

## 확장1
# for i in range(1, 6):  #두개의 인자값: (시작값, 끝값), 시작값 ~ (끝값-1) 생성
#     print(i)

## 확장2
# for i in range(1, 10, 2):  
#     #세개의 인자값: (시작값, 끝값, 간격), 시작값 ~ (끝값-1)까지 간격만큼 건너서 생성
#     print(i, end = ' ')


### range() 활용
# 0부터 입력한 값까지 출력
# num = int(input("숫자입력: "))

# for i in range(num+1):
#     print(i, end=' ')

## 두 수를 입력 받아, 첫 번째 입력받은 값부터 두번째 입력받은 값까지 출력
# n1 = int(input("숫자1: "))
# n2 = int(input("숫자2: "))

# for i in range(n1, n2+1, 1):
#     print(i, end = ' ')

## 1~100까지 3의 배수 출력

cnt = 0
for i in range(3,101, 3):
    print(i, end=' ')
    cnt += 1
    if cnt == 10:
        cnt = 0
        print()

