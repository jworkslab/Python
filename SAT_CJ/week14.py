### 제어문 / 조건문 if
# a = 9

# if 조건식:
# a = int(input("숫자 입력:"))

# if a > 7:
#     print("a는 7보다 큽니다.")
# elif a > 5:     #elif : if else 의 약자
#     print("a는 5보다 큽니다.")
# else:
#     print("a는 5보다 작습니다.")

# if 실습
# score = int(input("점수 입력: "))

# '''
# 100점 ~ 91점 : A  ->  score > 90
# 90점 ~ 81점 : B  -> score > 80
# 80점 ~ 71점 : C  -> score > 70
# 나머지 : F  -> else:
# '''

### [숙제]
## 입력한 숫자가 3의 배수이면 3, 5의 배수이면 5, 그렇지 않으면 0을 출력

#어떤 수를  2로 나누었을 때, 나머지가 0이면, 2의 배수에요.
#어떤 수를 6으로 나누었을 때, 나머지가 0이면, 6의 배수이죠. 

num = int(input("숫자 입력: "))

if num % 3 == 0:
    print(3)
elif num % 5 == 0:
    print(5)
else:
    print(0)