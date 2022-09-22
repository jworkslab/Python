### for 활용
# num = input("Enter numbers: ")
# num = num.split() 
# num = [int(i) for i in num]

# print(num, type(num))

## 코드 단축
# num = input("Enter numbers: ").split()
# num = num.split() 
# num = [int(i) for i in input("Enter numbers: ").split()]

# print(num, type(num))

# num = input("Enter numbers: ")
# num = num.split() 
# # print(num)
# num_list = []
# for i in num:
#     num_list.append(int(i))
# num = num_list
# print(num)

# num = int(input("Enter a number: "))

# for i in range(1, num+1):
#     print(' '*(num-i)+'*'*i)

# for i in range(num, 1, -1):
#     print(i, end=' ')

# for i in range(1, num+1):
#     for j in range(num, i, -1):
#         print(' ', end='')
#     print('*'*i)

### 피라미드 출력 숙제
# num = int(input("숫자 입력: "))

# for star in range(1, num+1):    #star: 1, 2, 3, 4, 5
#     for space in range(num, star, -1):    #space: 6~2 / 6~3 / 6~4 / 6~5 / 6
#         print(' ', end='')
#     print('*'*(star*2-1))   # 1, 3, 5, 7, 9

'''
 패턴찾기
##  1 2 3 4 5    
힌트 2 4 6 8 10   > *2
##  1 3 5 7 9    > -1
'''

