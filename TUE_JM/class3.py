### 변수 복습
# num = 0
# num += 1 #num = num + 1 #변수 num에 1을 더해서 num에 대입
# print(num)
#  #num = num * 12
# print(num)

#and = &
# or = |
# num1 = 10
# print(num1==10 | num1>0)

# name = 'Jake'
# age = 14
# height = 170.5
# print("이름: %s, 나이: %d, 키: %.3f"%(name, age, height))  #포맷기호
# print("이름: {}, 나이: {}, 키: {:.3f}".format(name, age, height))  #포맷함수
# print(f"이름: {name}, 나이: {age}, 키: {height:.3f}")  #f-string


num = 10
print("%o"%num)
print("%x"%num)
print("{}은 2진수로 {}, 8진수로 {}, 16진수로 {} 입니다."
.format(num, bin(num), oct(num), hex(num)))

#bin : 2진수 함수
#oct : 8진수 함수
#hex : 16진수 함수
print(format(num, '#b'))
