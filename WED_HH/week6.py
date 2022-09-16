### 튜플(Tuple)
## 튜플(Tuple) 생성
# box = (1, 2, 3, 4, 5)
# print(box)

## 튜프 연산
#순서가 있는 자료형의 연산
#순서가 있다는 것은 인덱스를 활용할 수 있다는 것
# s1 = 'abc'
# s2 = 'def'
# print(s1+s2) #병합 
# print(s1*3) #반복
# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# print(l1+l2) #병합
# print(l1*3) #반복
# t1 = (1, 2, 3)
# t2 = ('a', 'b', 'c')
# print(t1+t2) #병합
# print(t2*3) #반복
# print(t1[1])
# print(t2[1:3])

### 튜플 / 딕셔너리 
## 리스트 복사 : 복사 가능 / 위조, 변조 가능
# l1 = [1, 2, 3]
# #l2 = l1  #l1 리스트의 링크(주소)를 l2에 연결
# l2 = l1[:]  #l1 리스트의 값 전체를 l2리스트에 복사
# print(l1)
# print(l2)
# l2.append(4)
# print(l1)
# print(l2)
# print(l1 == l2) #비교연산자 == 는 값을 비교
# print(l1 is l2) #is 연산자 : 같은 객체인지 비교

### 튜플 복사 : 튜플 복사해도 객체가 생성되지 않는다 / 링크연결
# t1 = (1, 2, 3)
# t2 = t1[:]   # tuple(t1)
# print(t1)
# print(t2)
# print(t1 == t2)
# print(t1 is t2)

### 딕셔너리 (Dictionary)
dic = {'name':'Jake', 'age':12, 'school':'GCCD'}
# print(dic, type(dic))
# print(dic['name'])
# ## 딕셔너리 추가
# dic['class'] = 3
# dic['height'] = 178.9
# print(dic)
# ## 딕셔너리 수정
# dic['age'] = 27
# print(dic)
# ## 딕셔너리 삭제
# del dic['height']
# print(dic)

## 딕셔너리 함수(메소드)
# print(dic.keys())
# print(dic.values())
# print(dic.items())
# print(dic.get('school'))
# print(dic.update({'class':3, 'height':178.9, 'age':27}))
# print(dic)
# dic.clear()
# print(dic, type(dic))

fruits = {'appel':500, 'banana':2500, 'mango':2000}
print("망고는 1개당 %d원 입니다." %fruits['mango'])
print("망고는 1개당 {}원 입니다.".format(fruits['mango']))
