###################################
### 리스트 / 리스트 함수 / 중첩 리스트 ###
##################################

### 김밥 만들기
# item0 = '김'
# item1 = '밥'
# item2 = '단무지'
# item3 = '계란'
# item4 = '햄'
# item5 = '시금치'

# print(item0, item1, item2, item3, item4, item5)


# items = ['김', '밥', '단무지', '계란', '햄', '시금치']
# print(items)


## 리스트 & 인덱스
# students = ['종훈', '은석', '제이크']
# print(students)
# print(type(students))
# print(students[0])
# print(students[-1])

# score = [80, 90, 100, 70]
# print(score)
# print(type(score))
# print(score[0])
# print(score[1:3])


### 리스트 연산
# print(students+score)
# print(score*2)


### 내장함수 max, min, len, list
# print(max(score))   #리스트의 값들 중 최대값
# print(min(score))   #리스트의 값들 중 최소값
# print(len(score))   #리스트의 길이(갯수)

# text = "hello"
# print(text)
# print(list(text))   #자료형을 list로 변환


### 리스트 메소드
## 추가/삭제
# score.append(60)     #리스트 마지막에 값(60) 추가
# score.insert(3, 85)  #리스트의 n번째(3) 위치에 값(85) 추가
# score.pop()         #리스트의 마지막 값 삭제
# score.remove(85)    #리스트에서 해당 값(85) 삭제
# score.extend([70,90])
# score.remove(70)
# score.extend(students)
# print(score)

## 정보
# print(score.index(100)) #리스트에서 해당 값의 인덱스 반환
# print(score.count(90))  #리스트에서 해당 값의 개수 반환

## 정렬
# score.reverse()     #역순 정렬
# print(score)
# score.sort()        #오름차순 정렬(기본)
# print(score)
# score.sort(reverse=True)    #내림차순 정렬
# print(score)


### 미션. 학생 명부 만들기
s1 = ['Jake', 'M', 12, 'Daniel', '010-0000-0000']
s2 = ['Peter', 'M', 19, 'Nehemiah', '010-0000-0002']
s3 = ['Eunseok', 'F', 18, 'Nehemiah', '010-0000-0003']
# print(s1)
# print(s2)
# print(s3)


### 중첩 리스트
students = [s1, s2, s3]
print(students)
print(students[0])
print(students[0][0])


