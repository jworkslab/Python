# ### 패키지
# from calcpkg import *

# num_list = [int(i) for i in input("숫자 입력: ").split()]
# cal1 = operation.Calc(*num_list)

# print(cal1.add())

# ### <check> package import error


### 파일 입출력

## 파일 생성
# f = open("test.txt", 'w', encoding="UTF-8") #w: write
# f.write("첫 번째 파일 생성")
# f.close()

## 파일 작성 
# f = open("test.txt", 'a', encoding="UTF-8")   #a: append
# print()
# for i in range(1, 11):
#     data = f"{i}번째 줄입니다.\n"
#     f.write(data)
# f.close()

## 파일 읽기
## 한 줄 읽기
# f = open("test.txt", 'r')   #r: read
# # line = f.readline()
# # print(line)
# # line = f.readline()
# # print(line)
# for i in range(3):
#     line = f.readline()
#     # print(line, end='')
#     print(line.strip())   #strip: 문자열의 앞,뒤 공백 제거

# f.close()

## 여러 줄 읽기
f = open("test.txt", 'r', encoding="UTF-8")
line = f.readlines()  #모든 줄을 읽고, 각 줄별로 리스트로 저장
print(line)
f.close()

for i in line:
    print(i.strip())