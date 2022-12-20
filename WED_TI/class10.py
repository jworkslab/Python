### for x range()
# print(range(10))

# for i in range(10): #0부터 9(10-1) 까지 값 생성
#     print(i, end=' ')
# print()

# for i in range(1, 11): #1부터 10(11-1) 까지 값 생성
#     print(i, end=' ')
# print()

# for i in range(1, 11, 2):  #1부터 10(11-1)까지 간격을 2씩 건너서 값 생성
#     print(i, end=' ')
# print()


## [예제] 1부터 입력한 숫자까지 출력
# num = int(input("숫자 입력: "))

# for number in range(1, num+1):
#     print(number, end=' ')


## for 활용
# text = "Hello, my name is Taein."
# print(text)
# text = text.split()
# print(text)

## 문자를 숫자로 바꾸는 과정
# num = input("숫자 입력: ")
# print(num, type(num))
# num = num.split()
# print(num, type(num))
# print(num[0], type(num[0]))

# num[0] = int(num[0])
# print(num, type(num))
# print(num[0], type(num[0]))

# ## for문 활용
# num = input("숫자 입력: ")
# num = num.split()
# # intnum = []

# # for i in num:
# #     intnum.append(int(i))

# # print(intnum)
# # num = [int(i) for i in num]
# num = list(int(i) for i in num)
# print(num, type(num))

num = input("숫자 입력: ")
num = num.split()
num = [int(i) for i in num]

print(sum(num))