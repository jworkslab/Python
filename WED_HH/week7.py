### 제어문
## 조건문 if
# num = int(input("숫자 입력: "))

# if num > 5:
#     print(f"{num}는(은) 5보다 큽니다.")
# elif num < 5:
#     print(f"{num}는(은) 5보다 작습니다.")
# else:
#     print(f"{num}는(은) 5입니다.")

## 중첩 if
# num = int(input("숫자 입력: "))

# if num > 5:
#     print(f"{num}은(는) 5보다 큽니다.")
#     if num%2 == 0:
#         print(f"{num}은(는) 짝수 입니다.")
#     else:
#         print(f"{num}은(는) 홀수 입니다.")
# elif num < 5:
#     print(f"{num}은(는) 5보다 작습니다.")
#     if num%2 == 0:
#         print(f"{num}은(는) 짝수 입니다.")
#     else:
#         print(f"{num}은(는) 홀수 입니다.")
# else:
#     print(f"{num}은(는) 5입니다.")
#     print(f"{num}은(는) 홀수 입니다.")

### if x 논리연산
# num = int(input("숫자 입력: "))

# if num > 5 and num%2 == 0:
#     print(f"{num}은(는) 5보다 큽니다.")
#     print(f"{num}은(는) 짝수 입니다.")
# elif num > 5 and num%2 == 1:
#     print(f"{num}은(는) 5보다 큽니다.")
#     print(f"{num}은(는) 홀수 입니다.")
#     # if num%2 == 0:
#     #     print(f"{num}은(는) 짝수 입니다.")
#     # else:
#     #     print(f"{num}은(는) 홀수 입니다.")
# elif num < 5 and num%2 == 0:
#     print(f"{num}은(는) 5보다 작습니다.")
#     print(f"{num}은(는) 짝수 입니다.")
# elif num < 5 and num%2 == 1:
#     print(f"{num}은(는) 5보다 작습니다.")
#     print(f"{num}은(는) 홀수 입니다.")
# # elif num < 5:
# #     print(f"{num}은(는) 5보다 작습니다.")
# #     if num%2 == 0:
# #         print(f"{num}은(는) 짝수 입니다.")
# #     else:
# #         print(f"{num}은(는) 홀수 입니다.")
# else:
#     print(f"{num}은(는) 5입니다.")
#     print(f"{num}은(는) 홀수 입니다.")


### 멤버십 연사자 in 
l = [1, 2, 3, 4, 5]
# print(3 in l)
# print(7 in l)
num = int(input("숫자 입력: "))

if num in l:
    print(f"{num}은(는) 리스트에 있습니다.")
else:
    print(f"{num}은(는) 리스트에 없습니다.")