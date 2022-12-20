### 무한루프
# # a = 10
# num = 0

# # while a == 10:
# while True:
#     print(num)
#     num += 1


# member = ['Tommy', 'Marry', 'Jake1234']
# # cnt = 0

# while True:
#     ID = input("Enter your new ID: ")
#     # cnt += 1

#     if ID in member:
#         print(f"Welcome, {ID}")
#         break
#     else:
#         print("Try Again ...")

# reply = input()
# # print(reply, "(이)가 있고~!")


### 반복문 for
# students = ["Tom", "Jerry", "Spike"]

# for i in students:
#     print(i)

# text = "Hello World"
# for t in text:
#     print(t)

score = {'사회':70, '도덕':80, '체육':100, '미술':90, '음악':80}

for s in score:
    if score[s] < 90:
        continue
    else:
        print(f"{s} {score[s]}점~! 축합니다.")
    