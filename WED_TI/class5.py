### 리스트
# items = ['김', '밥', '단무지', '계란', '햄', '시금치']
# print(items)

### 리스트 인덱스
friends = ['피카츄', '라이츄', '파이리', '꼬부기']
# print(friends)
# print(type(friends))

# print(friends[0])
# print(friends[-1])
# print(friends[2:])

# score = [100, 80, 100, 90]
# print(score[1:3])

### 리스트 연산
# print(friends + score) #병합
# print(friends * 3) #반복

### 리스트 함수
## 내장 함수
# print(max(score))   #최대값 반환
# print(min(score))   #최소값 반환
# print(len(score))   #리스트의 길이(갯수) 

# name = "Jake"
# print(name, type(name))
# name = list(name)
# print(name, type(name))

# print(sum(score))

score = [100, 80, 100, 90]

# score.append(70)
# print(score)
# score.insert(2, 70)
# print(score)
# score.pop()
# print(score)
# score.remove(100)
# print(score)
# score.extend(friends)
# print(score)

## 정보
# print(score.index(80))
# print(score.count(100))

## 정렬
print(score)
score.reverse()
print(score)
score.sort()
print(score)
score.sort(reverse=True)
print(score)