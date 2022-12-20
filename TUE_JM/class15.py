### 함수(function)
## 사용자 정의 함수

## 기본구조 : 매개변수와 전달값 둘 다 없는 함수
# def add():   #함수정의
#     print("더하기 함수")

# add()    #함수호출


## 매개변수만 있는 함수
# def add(n1, n2):   #n1, n2는 인자값(argument)를 전달받는 매개변수(parameter)
#     total = n1 + n2
#     print(total)

# add(10, 5)    #10, 5는 add() 함수에 전달된 인자값

## 전달값(return)만 있는 함수 
# def add():
#     return "더하기 함수"

# print(add())

## 매개변수와 전달값 둘 다 가진 함수
# def add(n1, n2):   #매개변수
#     total = n1 + n2
#     return total    #전달값(return)

# print(add(10, 5))    #인자값(argument)

## <응용>
#1. cal() 함수 정의
#2. 사용자에게 두 값을 입력받아서 함수에 매개변수로 전달
#3. 입력받은 두 값의 사칙연산 결과 전달

# def cal(n1, n2):
#     add = n1 + n2
#     sub = n1 - n2
#     mul = n1 * n2
#     div = n1 / n2
#     return {'더하기':add, '빼기':sub, '곱하기':mul, '나누기':div}

# num1 = int(input("숫자 1: "))
# num2 = int(input("숫자 2: "))
# print(cal(num1, num2))


### 인자값의 갯수가 정해지지 않은 경우
# def add(n):
#     total = 0
#     for i in n:
#         total += i

#     return total 

# num_l = []
# while True:
#     num = int(input("숫자: "))
#     num_l.append(num)
#     if num == 0:
#         break

# num = [int(i) for i in input("숫자 입력: ").split()]

# print(add(num))

### 명함 프로그램
# def namecard(*argm):
#     print("==================")
#     for i in argm:
#         print(i)
#     print("==================")

# namecard("Jake", "010-0000-0000", "jworkslab@gmail.com", "Engineer")

def namecard(**argm):
    print("==================")
    for i in argm:
        print(i, ':', argm[i])
    print("==================")

info = {"이름":"Jake", "연락처":"010-0000-0000", "이메일":"jworkslab@gmail.com", "직업":"Engineer"}
namecard(**info)