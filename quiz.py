### mission
### log in program v2
### 변수 ID에 신규 가입자의 아이디를 입력 받습니다.
### 신규 가입자의 아이디가 5글자 이상이어야 아이디 생성 가능
### 신규 가입자의 아이디가 기존 멤버와 중복되지 않아야 아이디 생성 가능

members = ['Tommy', 'Marry', 'Jake1234', 'Peter']

cnt = 3

while cnt > 0:
    newID = input("Enter your ID: ")
    if newID in members:
        print("Login Success~!")
        break
    else:
        print("Try Again...")
        cnt -= 1

