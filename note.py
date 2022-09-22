# class BusinessCard:
#     def __init__(self, name, email, addr):
#         self.name = name
#         self.email = email
#         self.addr = addr
#     def print_info(self):
#         print("--------------------")
#         print("Name: ", self.name)
#         print("E-mail: ", self.email)
#         print("Address: ", self.addr)
#         print("--------------------")

# member1 = BusinessCard("kim", "kim@gmail.com", "USA")
# member1.print_info()
# member2 = BusinessCard("Chang", "Chang@gmail.com", "Korea")
# member2.print_info()

############################
# def cal(n1, n2):
#     sum = n1+n2
#     sub = n1-n2
#     mul = n1*n2
#     div = n1/n2
#     return sum, sub, mul, div #print(sum, sub, mul, div)
# ## return 값을 어떻게 주느냐에 따라 함수의 사용이 달라진다.

# print(cal(1, 2)) #cal(1, 2)


################################################
### Name Card
# def namecard(name, email, addr):
#     print("--------------------")
#     print("Name: ", name)
#     print("E-mail: ", email)
#     print("Address: ", addr)
#     print("--------------------")

# namecard("Jake", "jworkslab@gmail.com", "Korea")


## 매개변수 여러개 -> 튜플
# def namecard(*info):
#     print("--------------------")
#     for i in info:
#         print(i)
#     print("--------------------")

# namecard("Jake", "jworkslab@gmail.com", "Korea", "M", 27)


## 매개변수 여러개 -> 딕셔너리
# def namecard(**info):
#     print("--------------------")
#     for i in info:
#         print(i, ':', info[i])
#     print("--------------------")

# namecard(name = "Jake", email = "jworkslab@gmail.com", address =  "Korea")


################################################
### 지역변수 전역변수
# result = 0

# def add(num):
#     global result
#     result += num
#     return print(result)

# def sub(num):
#     global result
#     result -= num
#     return print(result)

# add(5)
# sub(2)


################################################
### 수퍼 생성자

list_id = []
list_pw = []
dic_member = {}

class New_account:
    def __init__(self):
        global list_id
        global list_pw
        self.count = 0

    def new_id(self, id):
        self.id = id

        if self.id not in list_id:
            list_id.append(self.id)
            self.count += 1
            print(f"Welcome {self.id}. You are number {self.count} of this group.")

        else:
            print(f"{self.id} is already used. Please Enter other ID.")

class School(New_account):
    #자식 클래스에서 생성자를 선언하면 부모 클래스의 생성자 속성을 물려 받을 수 없다
    #자식 클래스에서 생성자를 사용시 부모 클래스의 생성자를 물려받기 위해 super().__init__()으로 상속
    #자식 클래스에서 별도로 생성자를 선언하지 않는다면, super().__init__() 안써도 된다.
    #super(School, self).__init__() #파이선 2 버전 이하에서 사용하던 방식 #다중상속에서 상속받는 생성자의 클래스를 선택해 줄 수 있다
    def __init__(self):
        super(School, self).__init__() 
        self.cnt = 0

    def new_pw(self):
        while True:
            self.pw = input("Enter your password: ")

            if len(self.pw) < 5:
                print("Password should be more than 5 characters.")

            else:
                self.cnt += 1
                list_pw.append(self.pw + str(self.cnt))
                print(f"Password has been set.")
                print(self.pw)
                break



# gc = New_account()
gc = School()

while True:
    id = input("Enter new ID: ")
    if id == 'quit':
        break
    else:
        gc.new_id(id)
        gc.new_pw()

for i in range(len(list_id)):
    dic_member[list_id[i]] = list_pw[i]

print(dic_member)