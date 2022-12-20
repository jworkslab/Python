### 리스트 함수1 복습
# numbers = [10, 30, 60, 80, 100, 90]
# add_num = [70, 100, 90]

# print(max(numbers))
# print(min(numbers))
# print(len(numbers))
# print(sum(numbers))

# numbers.append(70)
# numbers.insert(2, 50)
# print(numbers)
# numbers.pop()
# numbers.remove(50)
# print(numbers)

# numbers.extend(add_num)
# print(numbers)


### 리스트 함수2

# numbers = [10, 30, 60, 80, 100, 90, 100]

# print(numbers.index(100))
# print(numbers.count(100))

# numbers.reverse()   #역순으로 정렬
# print(numbers)

# numbers.sort()  #작은 값부터 큰 값 순서로 정렬 (오름차순)
# print(numbers)

# numbers.sort(reverse=True)  #큰 값부터 작은 값 순서로 정렬 (내림차순)
# print(numbers)


### mission
# stdnt_1 = ['박채정', 'M', 15, 'class6', '010-1111-1111']
# stdnt_2 = ['김민수', 'M', 15, 'class3', '010-2222-2222']

# print(stdnt_1)
# print(stdnt_2)

# stdnt_1.append(['오렌지', '치킨', '바나나우유'])

# my_stdnt = [stdnt_1, stdnt_2]
# print(my_stdnt)

# print(my_stdnt[0][0])

### 리스트 활용
weapon = ['맨손', '목검', '녹슨검', '철검', '명검']
money = 100
armor = ['장갑', '투구', '전투화', '갑옷', '망토']
item = [weapon, money, armor]

my_item = [item[0][0], item[1], item[2][0]]
print(my_item)

my_item[1] += 900
print(my_item)

# my_item.append(item[0][1])
my_item[0] = item[0][1]
my_item[1] -= 500
print(my_item)
