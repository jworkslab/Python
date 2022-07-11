### 파일 입출력 ###

### 파일 생성 ###
# f = open("test.txt", 'w')
# f.close


### 파일 작성 ### write()
f = open("test.txt", 'w')
for i in range(1, 11):
    data = f"{i}번째 줄입니다.\n"
    f.write(data)
f.close()


### 파일 일기 ### 
## readline()
# f = open("test.txt", 'r')
# line = f.readline()
# print(line)
# f.close()


## .seek() & .tell()
# f = open("test.txt", 'r')
# for i in range(3):
#     line = f.readline()
#     print(line)
# f.seek(0,0) #처음 위치로 포인터 이동
# for i in range(3):
#     line = f.readline()
#     print(line)
# f.close()


## readlines()
# f = open("test.txt", 'r')
# line = f.readlines()
# print(line)
# f.close()

# for i in line:
#     print(i)


## way 1
# for i in line:
#     print(i, end='')

## way 2
# for i in line:
#     i = i.strip()
#     print(i)

 