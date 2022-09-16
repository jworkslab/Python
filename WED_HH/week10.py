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

num = int(input("Enter a number: "))

# for i in range(1, num+1):
#     print(' '*(num-i)+'*'*i)

# for i in range(num, 1, -1):
#     print(i, end=' ')

for i in range(1, num+1):
    for j in range(num, i, -1):
        print(' ', end='')
    print('*'*i)

### 피라미드 출력 숙제
