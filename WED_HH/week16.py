### 클래스 class

# class Cal:   #클래스 선언
#     result = 0  #클래스 변수

#     def add(self, n):    #메소드 선언
#         self.result += n
#         return self.result

# plus = Cal()
# minus = Cal()

# plus.add(50000)
# minus.add(25000)
# plus.add(100000)

# print(plus.add(0))
# print(minus.add(0))


### 생성자
# class Cal:   #클래스 선언
#     def __init__(self): #생성자 : 초기화 메소드
#         self.result = 0  #클래스 변수

#     def add(self, n):    #메소드 선언
#         self.result += n
#         return self.result

# class Cal_ch1(Cal):
#     def sub(self, n):
#         self.result -= n
#         return self.result

# my_acc = Cal_ch1()
# print(my_acc.add(10000))
# print(my_acc.sub(5000))

# class Cal_ch2(Cal_ch1):
#     def div(self, n):
#         self.result /= n
#         return self.result

# # bad_acc = Cal_ch2()
# # print(bad_acc.add(10000))
# # print(bad_acc.div(0))

# class Cal_ch2_safediv(Cal_ch2):
#     def div(self, n):
#         if n == 0:
#             return "0은 나눌수 없습니다."
#         else:
#             self.result /= n
#             return self.result

# good_acc = Cal_ch2_safediv()
# print(good_acc.add(10000))
# print(good_acc.div(0))

### [예제] 계산기
class Cal:
    def __init__(self, n1, n2):
        self.result = 0
        self.n1 = n1
        self.n2 = n2

    def add(self):
        self.result = self.n1 + self.n2
        print(self.result)
    
    def sub(self):
        self.result = self.n1 - self.n2
        print(self.result)

    def mul(self):
        self.result = self.n1 * self.n2
        print(self.result)

    def div(self):
        self.result = self.n1 / self.n2
        print(self.result)

num1 = int(input("첫 번째 숫자: "))
num2 = int(input("두 번째 숫자: "))

# my_cal = Cal(num1, num2)


class Cal_ch1(Cal):
    def div(self):
        if self.n2 == 0:
            print("Zero Error")
        else:
            self.result = self.n1 / self.n2
            print(self.result)

my_cal = Cal_ch1(num1, num2)

my_cal.add()
my_cal.sub()
my_cal.mul()
my_cal.div()