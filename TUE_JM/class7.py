### 딕셔너리 (dictionary)
# dic = {'name':'JM', 'age':14, 'school':'문원중'}
# print(dic, type(dic))

# print(dic['name'])
# #추가
# dic['grade'] = 1
# print(dic)
# #수정
# dic['name'] = '유재명'
# print(dic)
# #삭제
# del dic['school']
# print(dic)

## mission
#미션1: 여러 과일들의 가격을 딕셔너리로 선언하기
# fruits = {'apple':500, 'banana':2500, 'mango':2000}	
# print(fruits)

# #미션2: 망고가격 출력
# print("망고는 1개당 %d원 입니다." %fruits['mango'])
# print("망고는 1개당 {}원 입니다.".format(fruits['mango']))
# print(f"망고는 1개당 {fruits['mango']}원 입니다.")

# #미션3: 사과 가격 변경 500 -> 700
# fruits['apple'] = 700
# print(fruits)

# #미션4: 새로운 과일 추가
# fruits['orange'] = 1200	
# print(fruits)

# #미션5: 바나나 정보 삭제
# del fruits['banana']
# print(fruits)


## 딕셔너리 함수
score = {'MA':100, 'EN':90, 'SC':80, 'KO':90}
print(score.keys(), type(score.keys()))
print(score.values(), type(score.values()))
print(score.items())
print(score.get('MA')) 
score.update({'MA':90, 'HS':80})
print(score)
score.clear()
print(score)