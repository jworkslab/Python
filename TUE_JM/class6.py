### 리스트 함수2

score = [80, 90, 100, 70, 100]

## 리스트 정보 관련 메소드
# #.index() :  특정 값의 인덱스 반환
# print(score.index(90))
# #.count() : 특정 값의 갯수
# print(score.count(100))

## 리스트 정렬 관련 메소드
# score.reverse()   # .reverse(): 리스트 안에 있는 데이터의 순서를 역순으로 정렬
# print(score)
# score.sort()
# print(score)    # .sort(): 리스트 안에 있는 데이터를 작은 값부터 큰 값 순으로 정렬
# score.sort(reverse=True) # 내림차순: 큰 값부터 작은 값 순으로 정렬
# print(score)

## practice
# st_name = ['Jake', 'Mary', 'Emma', 'Daniel', 'Noel', 'Ariel']
# # print(st_name[2])
# ma_score = [80, 90, 70, 100, 80, 90]
# en_score = [90, 80, 90, 100, 90, 100]

# students = []

# students.append(st_name)
# students.append(ma_score)
# students.append(en_score)
# print(students)

# print(students[0][0], students[1][0], students[2][0])


### 튜플(tuple)
# num = (10, 20, 30, 40, 50)
# print(num, type(num))

# ## 튜플 연산
# print(num + num)
# print(num * 3)

# ## 튜플 & 인덱스
# print(num[2])
# print(num[1:4])

## 리스트 vs 튜플
#리스트 : 복사 가능 / 위, 변조 가능
# l1 = [1, 2, 3]
# # l2 = l1
# l2 = l1[:]  # [:] : 전체를 의미 / 전체 값 복사
# print(l1)
# print(l2)

# # l2.append(4)
# # print(l1)
# # print(l2)

# print(l1 == l2)   # == : 값이 같은지 비교
# print(l1 is l2)   # is : 객체가 같은지 비교

## 튜플 : 위변조 불가
t1 = (1, 2, 3)
t2 = t1[:]

print(t1)
print(t2)

print(t1 == t2)
print(t1 is t2)
