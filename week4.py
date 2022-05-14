############################################
### 문자열 연산 / 인덱스 / 슬라이싱 / 문자열 함수 ###
###########################################


### 문자열 1
fruit1 = 'apple'
fruit2 = "mango"

print(fruit1)
print(fruit2)


### 문자열은 덧셈과 곱셈이 가능하다
# print(fruit1 + fruit2)
# print(fruit1 * fruit2)


### 순서가 있는 자료형 - 문자열, 리스트, 튜플 
### 문자열에서 인덱스 활용
# s1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# s2 = "abcdefghijklmnopqrstuvwxyz"

# givenname = s1[9] + s2[0] + s2[10] + s2[4]
# print(givenname)
# surname = s1[-24] + s2[-19] + s2[-26] + s2[-13] + s2[-20]
# print(surname)
# fullname = givenname + ' ' + surname
# print(fullname)


### 인덱스 슬라이싱  #시작인덱스:끝인덱스+1
# print(fullname[2:6])
# print(fullname[:4])
# print(fullname[5:])


### 문자열 활용
# bible = "For the mind that is set \non the flesh is hostile to \nGod, for it does not \nsubmit to God's law; \nindeed, it cannot."
# print(bible)

# print(len(bible))
# print(bible[86:95])


### 문자열 함수
# print(bible.count('e'))
# print(bible.upper())
# print(bible.lower())
# print(bible.replace('flesh', 'sprit'))

# print(bible.isalpha())   #문자열이 문자로만 구성되었는지 확인 후, True / False 반환
# print(bible.isdigit())   #문자열이 숫자로만 구성되었는지 확인 후, True / False 반환
# print(bible.split(' '))  #해당 문자에서 문장을 분리시킨 후, 리스트로 저장
# print(type(bible.split(' ')))  #해당 문자에서 문장을 분리시킨 후, 리스트로 저장
# print(len(bible))   #문자열의 길이 값 반환
