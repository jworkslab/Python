### 문자열

# fruit1 = 'orange'
# fruit2 = 'watermelon'

# print(fruit1)
# print(fruit2)

# print(fruit1+fruit2) #문자열은 덧셈이 가능하다
# # print(fruit1-fruit2)
# print(fruit1*3) #문자열도 곱셈이 가능하다
# # print(fruit1/fruit2)

# hi = "Hello, World!"
# print(hi[0])
# print(hi[12])
# print(hi[-1])

# lipsum = "\"There is no one who loves pain itself, who seeks after it and wants to have it, simply because it is pain...\""
# name = 'Jake'
# phone = '010-4227-1132'
# print(lipsum)
# print(lipsum.count('a'))
# print(lipsum.upper())
# print(lipsum.lower())
# print(lipsum.replace('who', 'that'))
# print(name.isalpha()) #false 반환... 
# print(phone.isdigit())
# print(lipsum.split(','))
# lipsum_list = lipsum.split()
# print(lipsum_list)
# print(lipsum_list[0])
# print(lipsum_list[1])

# phone_list = phone.split('-')
# print(phone_list)

# print(len(lipsum))
# print(len(name))

# items = ['김', '밥', '단무지', '계란', '햄', '치즈']
# print(type(items))
# print(type(items[0]))
# print(items[-1])
# print(items[:3])
# print(items[2:])

# score = [100, 80, 70, 90, 100]

# score.append(80)
# print(score)
# score.insert(2, 90)
# print(score)
# score.pop()
# print(score)
# score.remove(90)
# print(score)
# score.extend(items)
# print(score)

student = [['Jake', 'M', 21, '010-4227-1132', 'Coding'], 
['Liana', 'F', 20, '010-0000-1111', 'Drama']]

print(student)
print(student[0][0], student[1][0])
