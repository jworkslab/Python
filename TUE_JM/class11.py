### for 활용
## 자료형변환 ## 중첩for문

# num = input("원하는 숫자 입력: ")
# print(num, type(num))
# num = num.split()
# print(num, type(num))
# l = []
# for i in num:
#     l.append(int(i))
# # num[0] = int(num[0])
# # num[1] = int(num[1])
# # num[2] = int(num[2])
# print(l, type(l))

# num = input("원하는 숫자 입력: ")
# num = num.split()
# num = list(int(i) for i in num)
# print(num, type(num))

# num = input("원하는 숫자 입력: ").split()
# num = list(int(i) for i in num)
# print(num, type(num))

# num = list(int(i) for i in input("원하는 숫자 입력: ").split())
# print(num, type(num))

# num = [int(i) for i in input("원하는 숫자 입력: ").split()]
# print(num, type(num))

### 이메일 주소록 
#step 1. 사용자에게 이메일 주소 입력 받는다
# email = input("이메일 주소 입력: ").split()
# temp = []
# host = []
# id = []

# for add in email:
#     temp.append(add.split('@'))
# for i in temp:
#     id.append(i[0])
#     host.append(i[1])
# print(temp)
# print(email)
# print(id)
# print(host)

###  별찍기
## 사용자가 입력한 숫자만큼 별찍기
'''
*
**
***
****
*****
'''
# count = int(input("숫자 입력: "))
# for i in range(1, count+1):
#     print('*' * i)

'''
    *
   **
  ***
 ****
*****
'''
count = int(input("숫자 입력: "))

for i in range(1, count+1):
    #공백 출력 알고리즘
    for g in range(count, i, -1):
        print(' ', end='')
    print('*' * (i*2-1))