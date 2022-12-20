### input() 함수
# print(input("이름을 입력하세요: "))

# name = input("이름을 입력하세요: ")
# print(name)

# num = int(input("첫번째 숫자를 입력하세요: "))
# print(num, type(num))

# num2 = int(input("두번째 숫자를 입력하세요: "))
# print(num2, type(num2))

# print(f"{num} + {num2} = {num+num2}")


## 계정생성 프로그램
id = input("Enter ID : ")
pw = input("Enter PW : ")

print(f"ID: {id} / PassWord: {pw}")
print(len(pw))
#len()  #길이(갯수)를 반환해주는 함수
#[숙제] : pw를 모두 '*'로 바꿔보세요


### 문자열 
# text = 'He said, "Hello~!"'
# text2 = "And then, she said, 'Hello..'"


### 문자열 연산
# fruit1 = "Orange"
# fruit2 = "Pear"

# print(fruit1 + fruit2)   #문자열 덧셈은 병합 
# # print(fruit1 - fruit2)
# print(fruit1 * 5)   #문자열 곱셈은 반복


### 인덱스(index)
# hello = "Hello, World!"
# print(hello[0])
# print(hello[-1])

# ### 인덱스 슬라이싱
# print(hello[0:4])
# # print(hello)
# print(hello[:5])
# print(hello[7:])


### 이스케이프 코드
# text = "\t\"There is no one \nwho loves pain itself, \nwho seeks after it \nand wants to have it, \nsimply because it is pain...\""

# print(text)