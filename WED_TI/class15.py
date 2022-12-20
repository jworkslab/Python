### 함수 (function)

# for i in range(1, 10):
#     print(f"2 x {i} = {2*i}")

# for i in range(1, 10):
#     print(f"3 x {i} = {3*i}")

# for i in range(1, 10):
#     print(f"4 x {i} = {4*i}")

### 구구단 함수
## 함수 기본형
# def mul_table():   #함수선언 #함수정의 #함수만들기
#     for i in range(1, 10):
#         print(f"2 x {i} = {2*i}")

# mul_table()   #함수호출 #함수실행 #함수사용


## 인자값과 매개변수
# def mul_table(num):   #num : 매개변수 (인자값을 저장하는 변수)
#     for i in range(1, 10):
#         print(f"{num} x {i} = {num*i}")

# # ggd = int(input("숫자 입력: "))

# # mul_table(ggd)   #ggd : 인자값 (함수에 전달하는 값)

# for i in range(1, 10):
#     mul_table(i)

## 인자값이 여러개인 경우
# def mul(n1, n2, n3):
#     print(f"{n1} x {n2} x {n3}= {n1*n2*n3}")


# num1 = int(input("숫자1 입력: "))
# num2 = int(input("숫자2 입력: "))
# num3 = int(input("숫자3 입력: "))

# mul(num1, num2, num3)

## 인자값의 갯수가 정해져 있지 않은 경우
# def mul(*arg): #arg = [1, 2, 3, 4, 5] 
#     total = 1
#     for i in range(0, len(arg)):
#         total *= arg[i]
#         print(f"{arg[i]}", end = '')
#         if i == len(arg)-1:
#             break
#         print('x', end='')
#     print(f'= {total}')

# num_list = [int(i) for i in input("숫자 입력: ").split()]
# mul(*num_list)

### 네임카드 만들기
# def namecard(**argm):
#     print("===================")
#     for i in argm:
#         print(f"{i} : {argm[i]}")
#     print("===================")

# # nc_list = input("정보입력: ").split('/')
# # namecard(*nc_list)
# # namecard("name : Jake", "mobile : 010-1111-2222", "email : jake@gmail.com")

# nc_dic = {'name':"Jake", 'mobile':"010-1111-2222", 'email':"j@gmail.com"}
# namecard(**nc_dic)

### 반환값 (return)
def namecard(*argm):
    print("===================")
    for i in argm:
        print(i)
    print("===================")
    return argm[0]

nc_list = input("정보입력: ").split('/')
namecard(*nc_list)
print(namecard(*nc_list))
