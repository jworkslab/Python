### while 복습

'''
문제: 입력한 횟수만큼 나무를 찍어서 넘어뜨리기

[입력]  4
[출력]
나무를 1번 찍었습니다.
나무를 2번 찍었습니다.
나무를 3번 찍었습니다.
나무를 4번 찍었습니다.
나무가 넘어갑니다.
'''

# num = int(input("숫자 입력: "))
# ax = 0

# while True:
#     ax += 1
#     if ax > num:
#         break
#     print(f"나무를 {ax}번 찍었습니다.")
# print("나무가 넘어갑니다.")

### [숙제] 0이 입력되기 전까지 입력된 숫자를 리스트에 추가하기
num_list = []
num = int(input("숫자 입력: "))   #입력

while num!=0:
	num_list.append(num)	#리스트에 추가
	num = int(input("숫자 입력: "))   #입력

print(num_list)