### 문자열 함수
# text = "Hello, World! It is my first Python~!"

# print(text.count('l'))
# print(text.count('Hello'))
# print(text.upper())
# print(text.lower())
# print(text.replace('World', "Jaemyung"))
# print(text.isalpha())
# print(text.isdigit())

# text2 = "Hello"
# text3 = "01012341234"
# print(text2.isalpha())
# print(text3.isdigit())

# print(len(text))
# print(text.split())

# phone = "010-1234-1234"
# print(phone.split('-'))

### 김밥 만들기
# item0 = '김'
# item1 = '밥'
# item2 = '단무지'
# item3 = '계란'
# item4 = '햄'
# item5 = '시금치'

# print(item0, item1, item2, item3, item4, item5)

# items = ['김', '밥', '단무지', '계란', '햄', '시금치']
# print(items, type(items))
# print(items[4])
# print(items[2:5])


### 리스트 연산
students = ["Tom", "Jerry", "Spike"]
scores = [100, 80, 90]

# print(students + scores)    #병합
# print(students * 3)     #반복

# print(max(scores))
# print(min(scores))
# print(len(students))

# text = "hello"
# print(text, type(text))
# text = list(text)
# print(text, type(text))

# # num = int(input("숫자 입력:"))
# # print(num, type(num))

# print(sum(scores))

students.append('Donald')
print(students)
scores.append(70)

students.insert(2, 'Jake')
print(students)
scores.insert(2, 100)
print(scores)

students.pop()
print(students)
scores.remove(70)
print(scores)

print(students + scores)
print(students)
print(scores)

students.extend(scores)
print(students)
print(scores)