### for 복습
# text = "hello world"
# for t in text:
#     print(t)

# list = [1, 2, 3, 4, 5]
# for l in list:
#     print(l)


### for x dictionary
# dic = {'MA':90, 'EN':100, 'SC':70, 'HS':80}
# for d in dic:
#     print(d, ':', dic[d])

### continue
# score = {'MA':90, 'EN':100, 'SC':70, 'HS':80}
# for s in score:
#     if score[s] < 80:
#         # print()
#         continue
#     else:
#         print(f"{s} 통과! 축하합니다~!")


### range() 함수
## range(start, stop, step)  ## start부터 stop-1까지 값 생성
# print(list(range(10)))    #0~9까지 정수 생성
# print(list(range(1, 11)))    #1~10까지 정수 생성
# print(list(range(1, 11, 2)))    #1~10까지 2간격으로 정수 생성
# print(list(range(4, 40, 4)))

### for x range()
# for i in range(10):
#     print(f"{i+1}번째 인사, Hello")

# for i in range(1, 11):
#     print(f"{i}번째 인사, Hello")

### [예제]1부터 사용자가 입력한 값까지 출력하는 프로그램
# num = int(input("숫자 입력: "))
# cnt = 0
# for i in range(1, num+1):
#     cnt += 1
#     print(i, end=' ')
#     if cnt == 10:
#         print()
#         cnt = 0

num1 = int(input("시작값 입력: "))
num2 = int(input("끝값 입력: "))

for n in range(num1, num2+1):
    print(n, end=' ')