
name = "Tom"
age = 21
height = 177.8976
print(type(height))

### format 기호
print("이름: %s, 나이: %d, 키: %.2f" %(name, age, height))

### format() 함수
print("이름: {}, 나이: {}, 키: {:.2f}".format(name, age, height))
print("이름: {1}, 나이: {0}, 키: {2:.2f}".format(age, name, height))

### f-string
print(f"이름: {name}, 나이: {age}, 키: {height:.2f}")