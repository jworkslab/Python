### 문자열 함수
text = "Change the world with your codes."

# print(text.count('the'))   #특정 문자의 갯수를 반환
# print(text.upper())   #문자열을 전부 대문자로 변환
# print(text.lower())   #문자열을 전부 소문자로 변환
# print(text)

# print(text.replace('codes', 'coding'))

# text = "Hello"
# print(text.isalpha()) 
# print(text.isdigit()) 

# text = "01042271132"
# print(text.isalpha()) 
# print(text.isdigit()) 

print(text.split())

phone = "010-1111-2222"
print(phone.split('-'))

date = "2022/09/17"
print(type(date.split('/')))


## () : 함수, 튜플
## [] : 인덱스, 리스트
## {} : 포맷팅, 딕셔너리

print(len(text))
