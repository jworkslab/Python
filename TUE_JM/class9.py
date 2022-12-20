### 제어문 / 반복문 / while

# print("나무를 1번 찍었습니다.")
# print("나무를 2번 찍었습니다.")
# print("나무를 3번 찍었습니다.")
# ...
# print("나무를 9번 찍었습니다.")
# print("나무를 10번 찍었습니다.")

# count = 1

# while count<=10:
#     print(f"나무를 {count}번 찍었습니다.")
#     count += 1


### 계정생성 프로그램 업그레이드 -> 로그인 프로그램
member = ['Tommy', 'Jaemyung', 'Marry']
pw = ''

cnt = 3

while cnt > 0:
    newID = input("새로운 아이디를 입력하세요: ")

    if newID in member:
        print("이미 가입된 ID 입니다.")
        cnt -= 1
    else:
        member.append(newID)
        #"비밀번호를 입력해주세요"
        print(f"가입완료! {newID}님, 환영합니다~!")
        break
    print("다시 시도해 주세요.")

### 로그인 프로그램 실행
## ID 맞는지 여부 3회 확인
log_id = input("아이디 입력: ")

log_cnt = 3
while True:
    if log_id in member:
        log_pw = input("비밀번호 입력: ")#"비밀번호 입력: "
        if pw == log_pw: #조건문으로 비밀번호 확인
            print(f"{log_id}님 로그인 되었습니다.")
            break
    else:
        print("없는 아이디입니다. 다시 입력하세요.")
        cnt -= 1
        if cnt == 0:
            break


