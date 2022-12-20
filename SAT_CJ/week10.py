### 리스트 함수
# friends = ['Tom', 'Jerry', 'Spike']
# score = [90, 100, 70]

# print(max(score))
# print(min(score))
# print(len(score))

# text = "박채정"
# print(text, type(text))
# text = list(text)   #리스트 함수
# print(text, type(text))

# print(sum(score))

##리스트 메소드
from sys import set_coroutine_origin_tracking_depth, stderr
from turtle import st


students = ['박채정', '송건희', '제이크']
score = [100, 80, 90]

#추가
students.append('김민재')   #append() : 리스트 마지막에 값 추가
score.append(80)
print(students)
students.insert(2, '박나현')   #insert() : 원하는 위치에 값 추가
score.append(100)
print(students)

#삭제
students.pop()  #pop() : 리스트 마지막 값 삭제
print(students)
students.remove("박나현")  #remove() : 리스트에서 원하는 값 삭제
print(students)

print(score)
score.remove(80)
score.remove(100)
print(score)

print(students + score)
print(students)
students.extend(score)   #list1.extend(list2) : 리스트1에 다른 리스트2 병합
print(students)
print(score)

### list methods 이어서 할 차례 ...