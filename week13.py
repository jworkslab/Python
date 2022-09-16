###################
### Class 클래스 ###
##################

### 더하기 함수
# result = 0

# def add(num):
#     global result
#     result += num
#     return result

# print(add(1))
# print(add(1))


### 더하기 함수 x 2
# result1 = 0
# result2 = 0

# def add1(num):
#     global result1
#     result1 += num
#     return result1

# def add2(num):
#     global result2
#     result2 += num
#     return result2

# print(add1(1))
# print(add1(1))
# print(add2(10))
# print(add2(10))


### 클래스 사용
# class Cal:
#     result = 0  #클래스 변수

#     def add(self, num): #클래스 함수
#         self.result += num
#         return self.result

# cal1 = Cal()
# cal2 = Cal()

# print(cal1.add(1))
# print(cal1.add(1))
# print(cal2.add(10))
# print(cal2.add(10))


### 생성자 __init__()
# class Cal:
#     result = 0  #클래스 변수
#     def __init__(self):
#         self.result = 0
#     def add(self, num): #클래스 함수
#         self.result += num
#         return self.result
#     def __init__(self):
#         self.name = "Jake"

# cal1 = Cal()
# cal2 = Cal()

# print(cal2.name)
# print(cal1.add(1))
# print(cal1.add(1))
# print(cal2.add(10))
# print(cal2.add(10))
# print(cal1.name)


### 클래스 상속
# class Cal:
#     result = 1  #클래스 변수
#     def __init__(self):
#         self.result = 0
#     def add(self, num): #클래스 함수
#         self.result += num
#         return self.result

# class Calsub(Cal):
#     def sub(self, num):
#         self.result -= num
#         return self.result

# cal1 = Cal()
# cal2 = Calsub()


# print(cal1.add(2))
# # print(cal1.sub(1))  # 에러발생
# print(cal2.add(10))
# print(cal2.sub(5))


### 메소드 오버라이딩
# class Cal:
#     def __init__(self, first, second):
#         self.first = first
#         self.second = second
#     def add(self):
#         result = self.first + self.second
#         return result
#     def mul(self):
#         result = self.first * self.second
#         return result
#     def sub(self):
#         result = self.first - self.second
#         return result
#     def div(self):
#         if self.second == 0:  # 나누는 값이 0인 경우 0을 리턴하도록 수정
#             return 0
#         else:
#             return self.first / self.second


# class SafeCal(Cal):
#     def div(self):
#         if self.second == 0:  # 나누는 값이 0인 경우 0을 리턴하도록 수정
#             return 0
#         else:
#             return self.first / self.second

# a = Cal(10, 0)  #객체 생성

# print(a.add())
# print(a.div())
