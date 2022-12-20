### 튜플(tuple)
# num = (10, 20, 30, 40)
# print(num, type(num))

## 튜플 연산
# t1 = (10, 20, 30)
# t2 = (40, 50, 60)
# print(t1 + t2)
# print(t1 * 3)
# print(t1[1])
# print(t2[1:3])

## 리스트 vs 튜플
## 리스트
# l1 = [1, 2, 3]
# l2 = l1[:]

# print(l1)
# print(l2)

# print(l1 == l2) # 값이 같은지 확인
# print(l1 is l2) # 객체(존재)가 같은지 확인

# l2.append(4)
# print(l1)
# print(l2)

## 튜플
# t1 = (1, 2, 3)
# t2 = t1[:]

# print(t1)
# print(t2)

# print(t1 == t2)
# print(t1 is t2)


### 딕셔너리(dictionary)
## 생성
# dic = {'name':'박채정', 'school':'문원중', 'grade':2}
# print(dic, type(dic))

# print(dic['name'])

# ## 추가
# dic['class'] = 6
# print(dic)

# ## 수정
# dic['school'] = '과천중'
# print(dic)

# ## 삭제
# del dic['name']
# print(dic)

## 딕셔너리 실습
print(f"망고는 1개당 {}원 입니다.")