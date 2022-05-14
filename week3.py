##########################
### 변수 / 연산자 / 포맷팅 ###
#########################

name = 'Jake'
age = 21
height = 178.91233452

# print("이름: ", name)
# print("나이: ", age)

print("이름: %s, 나이: %d, 키: %.2f" %(name, age, height))
print(f"이름: {name}, 나이: {age}, 키: {height:.2f}")
print("이름: {}, 나이: {}, 키: {:.2f}".format(name, age, height))
print("이름: ", name, "나이: ", age, "키: ", height)
# print("이름: "+ name+ "나이: "+ age+ "키: "+ height)  #서로 다른 자료형은 더해질 수 없다.

