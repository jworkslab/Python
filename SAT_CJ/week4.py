a = 10
b = 20

# print(a<b and a==10) #True True -> True
# print(a>b and a==10) #False True -> False
# print(a>b and a!=10) #False False -> False

# print(a<b or a==20) #True False -> True
# print(a>b or a==10) #False True -> True
# print(a>b or a!=10) #False False -> False

# print(not a>b) #False -> True
# print(not a<b) #True -> False
# print(not a==10) #True -> False


### 포맷팅
## 포맷기호 %
# name = "Jake"
# age = 27
# height = 178.9
# # [출력] 이름: Jake, 나이: 27, 키:  178.9
# print("이름: ", name, "나이: ", age, "키: ", height) 
# print("이름: %s, 나이: %d, 키: %.3f"%(name, age, height)) #포맷기호

# print("이름: {}, 나이: {}, 키: {:.3f}".format(name, age, height)) #포맷함수
# print("이름: {2}, 나이: {0}, 키: {1}".format(name, age, height))

# print(f"이름: {name}, 나이: {age}, 키: {height:.3f}") #f-string

### Homework
## [출력] "문원중학교 2학년 ?반 ?번"
school = "문원중학교" 
s_class = 6
number = 14
print("문원중학교 2학년 6반 14번")
print("%s 2학년 %d반 %d번" %(school, s_class, number))
print("{} 2학년 {}반 {}번".format(school, s_class, number))
print(f"{school} 2학년 {s_class}반 {number}번")
