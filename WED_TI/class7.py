### 제어문
## 조건문 if
# num = int(input("숫자 입력: "))

# if num > 5:
#     print(f"{num}은(는) 5보다 큽니다.")
# elif num == 5:
#     print(f"{num}은(는) 5 입니다.")
# else: #예외처리
#     print(f"{num}은(는) 5보다 작습니다.")

## 중첩if
num = int(input("숫자 입력: "))

if num > 5:
    print(f"{num}은(는) 5보다 큽니다.")
    if num%2 == 0:  #짝수라면
        print("짝수 입니다.")
    else: #elif num%2 == 1: #num%2 != 0: #짝수가 아니라면
        print("홀수 입니다.")
elif num == 5:
    print(f"{num}은(는) 5 입니다.")
    print("홀수 입니다.")
else: #예외처리
    print(f"{num}은(는) 5보다 작습니다.")
    if num%2 == 0:  #짝수라면
        print("짝수 입니다.")
    elif num%2 != 0: #짝수가 아니라면
        print("홀수 입니다.")
    else:
        print("0 입니다.")


#####
## if x 논리연산 할 차례...
