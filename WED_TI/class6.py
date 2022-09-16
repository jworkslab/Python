### 튜플 (tuple)
# l = [1, 2, 3, 4, 5]
# t1 = (1, 2, 3, 4, 5)
# t2 = ('a', 'b', 'c')
# print(t1, type(t1))

## 튜플 연산
# print(t1+t2)
# print(t2*3)

## 튜플 인덱스
# print(t1[2])
# print(t1[1:4])
# print(t2[1:])

## 리스트 vs 튜플
# l1 = [1, 2, 3]
# l2 = l1[:] #l1의 값 전체를 l2에 복사  #l2 = l1 : 링크만 연결
# print(l1)
# print(l2)
# print(l1 == l2)  #값이 같은지 여부 확인
# print(l1 is l2)  #주소가(링크) 같은지 여부 확인
# l2[1] = 4
# print(l1)
# print(l2)

# t1 = (1, 2, 3)
# t2 = t1[:] #t1의 값 전체를 t2에 복사  #t2 = t1 : 링크만 연결
# print(t1)
# print(t2)
# print(t1 == t2)  #값이 같은지 여부 확인
# print(t1 is t2)  #주소가(링크) 같은지 여부 확인
# t2 = (4, 5, 6)
# print(t1)
# print(t2)
# print(t1 == t2)  #값이 같은지 여부 확인
# print(t1 is t2)  #주소가(링크) 같은지 여부 확인


## 딕셔너리 (dictionary)
# dic = {'name':'Jake', 'age':18, 'school':'과천중'}
# print(dic, type(dic))
# print(dic['name'])

# ## 딕셔너리 추가
# dic['height'] = 178.5
# print(dic)

# ## 딕셔너리 수정
# dic['age'] = 20
# print(dic)

# ## 딕셔너리 삭제
# del dic['school']
# print(dic)

from platform import java_ver


fruits = {'apple':500, 'mango':2000, 'banana':2500, 'apple':800}
# print("망고는 1개당 %d원 입니다."%fruits['mango'])
# print("망고는 1개당 {}원 입니다.".format(fruits['mango']))
# print(f"망고는 1개당 {fruits['mango']}원 입니다.")

# fruits['apple'] = 700
# fruits['orange'] = 1200
# del fruits['banana']
# print(fruits)

### 딕셔너리 함수
# fruits_list = list(fruits.keys())
# print(fruits_list)
print(fruits.keys())
print(fruits.values())
print(fruits.items())
print(fruits.get('apple'))

fruits.update({'apple':700, 'orange':1200})
print(fruits)

fruits.clear()
print(fruits)