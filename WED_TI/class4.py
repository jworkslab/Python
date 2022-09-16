### Review
# school = input("학교: ")
# grade = int(input("학년: "))
# s_class = int(input("반: "))
# num = int(input("번호: "))

# ### [출력 예] "과천중학교 1학년 8반 27번"
# print(school, grade, "학년 ", s_class, "반 ", num, "번")
# print("%s %d학년 %d반 %d번" %(school, grade, s_class, num))   #포맷기호
# print("{} {}학년 {}반 {}번".format(school, grade, s_class, num))   #포맷함수
# print(f"{school} {grade}학년 {s_class}반 {num}번")   #f-string


### 문자열 연산
# fruit1 = "오렌지"
# fruit2 = "배"

# print(fruit1 + fruit2)  #병합
# # print(fruit1 - fruit2)   #연산불가
# print(fruit1 * 2)   #반복
# print(fruit2 / 2)   #연산불가

### 인덱스 활용
# text = "Hello, World!"
# print(text[0:5])   #Hello 출력
# print(text[-6:-1])   #World 출력
# print(text[:])  #전체 출력
# print(text[:4]) #처음부터 4번째 인덱스 전까지 출력
# print(text[-2:]) #-2번째 인덱스부터 끝까지 출력

### 이스케이프코드
text = "\t\"There is no one \nwho loves pain itself, \nwho seeks after it \nand wants to have it, \nsimply because it is pain...\""
print(text)

# print(text.count("w"))
# print(text.upper())
# print(text.lower())
# print(text.replace('who', 'that'))

# print(text.isalpha())
# print(text.isdigit())

print(text.split())
print(text.split(','))

print(len(text))