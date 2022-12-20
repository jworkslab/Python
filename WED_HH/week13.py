### 중간평가
#1. 문자열 "과천코딩2022"에서 인덱스를 활용하여 '과천코딩'만 출력하세요.
# text = "과천코딩2022"
# print(text[0:4])


#2. 문자열 "Was it a car or a cat I saw?"를 거꾸로(역순으로) 출력하세요.
text = "Was it a car or a cat I saw?"
##리스트 활용
# answer =''
# text = list(text)
# text.reverse()

# for i in text:
#     answer += i

# print(answer)

## for 활용
# answer = ''
# for t in text:
#     answer = t + answer
# print(answer)

## 인덱스 활용
# print(text[::-1])


#3. 과일 이름과 먹은 갯수를 입력 받은 뒤, "어제 사과를 4개 먹었습니다." 와 같이 출력
# fruit = input("과일 입력: ")
# num = int(input("먹은 갯수 입력: "))
# print(f"어제 {fruit}(을)를 {num}만큼 먹었습니다.")

#4. 두 개의 숫자를 입력 받은 뒤, 사칙 연산(+, -, x, /) 결과 출력
# num1 = int(input("첫 번째 숫자 입력: "))
# num2 = int(input("두 번째 숫자 입력: "))

# print(f"{num1} + {num2} = {num1+num2}")
# print(f"{num1} - {num2} = {num1-num2}")
# print(f"{num1} * {num2} = {num1*num2}")
# print(f"{num1} / {num2} = {num1/num2:.2f}")

#5. 하나의 숫자를 입력 받은 뒤, 입력된 숫자가 홀수인 경우 'odd', 짝수인 경우 'even'을 출력하세요.
# num = int(input("숫자 입력: "))

# if num == 0:
#     print("zero") 
# elif num%2 == 0:
#     print("even")
# else:
#     print("odd")


#6.하나의 숫자를 입력 받은 뒤, 1부터 입력 받은 숫자까지의 약수를 출력하세요. 
# num = int(input("숫자 입력: "))

# for i in range(1, num+1):
#     if num % i == 0:
#         print(i, end=' ')

#7. 하나의 숫자를 입력 받은 뒤, 그 숫자가 소수(prime number)인지 아닌지 판별하여 소수이면 'True'를 출력하고, 아니면 'False'를 출력하세요.
# num = int(input("숫자 입력: "))
# factor = []

# for i in range(1, num+1):   #step 1. 약수 구하기
#     if num % i == 0:
#         factor.append(i)

# if len(factor) == 2:    #step 2. 약수의 갯수 구하기
#     print("True")
# else:
#     print("False")


#8. 입력 받은 10진수를 2진수로 변환해서 출력하세요. 
## 10 -> 1010
## 리스트 활용
# num = int(input("숫자입력: "))
# l = []
# ## 수학정리 : num을 2로 나누었을 때의 몫과 나머지가 필요
# while True:
#     l.append(num % 2)
#     num = num // 2
#     if num == 1:
#         l.append(num % 2)
#         break

# for i in l[::-1]:
#     print(i, end='')


## 문자열을 활용
# num = int(input("숫자 입력: "))
# s = ''
# while num > 0:
#     s = str(num % 2) + s
#     num = num // 2

# print(s)

## format() 활용
# num = format(int(input("숫자 입력: ")), 'x')
# print(num)

## 자료형 함수 활용 bin()
# num = int(input("숫자 입력: "))
# print(bin(num)[2:])

#9 #10 -> to be continued...
