
# from tkinter import *       #import
# win = Tk()                  #create object
# win.geometry("500x500")     #window size
# win.title("test")           #window title
# win.mainloop()              #run window


### 파일 입출력
## w : write / r : read / a : add
# f = open("test.txt", 'w')
# for i in range(1, 12):
#     f.write(f"This is a line {i}\n")
# f.close()

# with open("test.txt", 'w') as f:
#     for i in range(1, 12):
#         f.write(f"This is a line {i}\n")

### 1줄 읽기
# f = open("test.txt", 'r')
# line = f.readline()
# print(line)
# f.close()

### 1줄씩 전체 라인 읽기
# f = open("test.txt", 'r')
# while True:
#     line = f.readline()
#     if not line: break
#     print(line)
# f.close()

### 전체 라인 리스트로 저장 후 읽기
# f = open("test.txt", 'r')
# lines = f.readlines()
# for line in lines:
#     print(line)
# print(lines)
# f.close()

### 전체 문서 텍스트로 저장 후 읽기
# f = open("test.txt", 'r')
# data = f.read()
# print(data)
# f.close()

