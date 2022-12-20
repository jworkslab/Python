### 함수리뷰 / 지역변수와 전역변수
# total = 0   #지역변수

# def add(num):
#     global total    #전역변수
#     total += num
#     print(total)
#     # return total


# # print(add(12))
# add(12)


### 클래스 (Class)

# class Cal:
#     total = 0   #클래스 변수
#     def add(self, num):   #메소드: 클래스 내부에서 선언된 함수
#         self.total += num
#         print(self.total)
#     def min(self, num):   #메소드: 클래스 내부에서 선언된 함수
#         self.total -= num
#         print(self.total)

# cal1 = Cal()   #객체 생성

### 생성자

# class Cal:   #부모 클래스 
#     def __init__(self):
#         self.total = 0
#     def add(self, num):   #메소드: 클래스 내부에서 선언된 함수
#         self.total += num
#         print(self.total)
#     def min(self, num):   #메소드: 클래스 내부에서 선언된 함수
#         self.total -= num
#         print(self.total)

# cal1 = Cal()   #객체 생성


# ### 클래스 상속
# class Cal_ch1(Cal):   #자식 클래스
#     def mul(self, num):
#         self.total *= num
#         print(self.total)

# cal2 = Cal_ch1()
# cal2.add(10)
# cal2.min(2)
# cal2.mul(3)


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

# cal1 = Cal(20, 0)
# cal1.add()
# cal1.div()

class Cal_fix(Cal):
    def div(self):
        if self.second == 0:
            return print('Not Exist')
        else:
            self.result = self.first / self.second
            return print(self.result)

cal2 = Cal_fix(20, 0)
cal2.add()
cal2.div()