### 리턴값이 여러개인 경우
### 매개변수가 여러개인 경우
### 매개변수 갯수가 정해지지 않은 경우 (튜플, 딕셔너리)
### 함수 내 변수 / 지역변수 전역변수

### 함수 응용
## return 값이 여러개인 경우
# def cal(n1, n2):
#     sum = n1+n2
#     sub = n1-n2
#     mul = n1*n2
#     div = n1/n2
#     return print(sum, sub, mul, div)

# cal(1, 2)

## 매개변수가 여러개인 경우(갯수 미정)
## 매개변수 갯수가 정해진 경우
# def namecard(name, email, addr):
#     print("=====================")
#     print("Name: ", name)
#     print("E-mail: ", email)
#     print("Address: ", addr)
#     print("=====================")

# namecard("Jake", "jworkslab@gmail.com", "Korea")

# ## 매개변수 갯수가 정해지지 않은 경우 (튜플로 저장)
# def namecard(*argm):
#     print("=====================")
#     for i in argm:
#         print(i)
#     print("=====================")

# namecard("Jake", "jworkslab@gmail.com", "Korea", "Engineer", "Python")

## 매개변수 갯수가 정해지지 않은 경우 (딕셔너리로 저장)
# def namecard(**argm):
#     print("=====================")
#     for i in argm:
#         print(i, ":", argm[i])
#     print("=====================")

# # namecard(Name="Jake", Email="jworkslab@gmail.com", Address="Korea", Job="Engineer", Skill="Python")
# nc = {"Name":"Jake", "Email":"jworkslab@gmail.com", "Address":"Korea", "Job":"Engineer", "Skill":"Python"}
# namecard(**nc)

### 지역변수 & 전역변수
# result = 0

# def add(num):
#     global result
#     result += num
#     return print(result)

# def sub(num):
#     global result
#     result -= num
#     return print(result)

# add(10)
# sub(5)


### 클래스
# class Cal:
#     # result = 0
#     def __init__(self):
#         self.result = 0

#     def add(self, num):
#         self.result += num
#         return print(self.result)

#     def sub(self, num):
#         self.result -= num
#         return print(self.result)

# class Cal_kid(Cal):
#     def mul(self, num):
#         self.result *= num
#         return print(self.result)

# class Cal_grand_kid(Cal_kid):
#     def div(self, num):
#         self.result /= num
#         return print(self.result)


# cal1 = Cal_grand_kid()

# cal1.add(10)
# cal1.sub(3)
# cal1.mul(2)
# cal1.div(2)

### 메소드 오버라이딩
class Cal:
    def __init__(self, first, second):
        self.result = 0
        self.first = first
        self.second = second
    
    def add(self):
        self.result = self.first + self.second
        return print(self.result)
    def sub(self):
        self.result = self.first - self.second
        return print(self.result)
    def mul(self):
        self.result = self.first * self.second
        return print(self.result)
    def div(self):
        self.result = self.first / self.second
        return print(self.result)

class Cal_kid_safediv(Cal):
    def div(self):
        if self.second == 0:
            return print(0)
        else:
            self.result = self.first / self.second
            return print(self.result)

a = Cal_kid_safediv(10, 0)

a.add()
a.div()