### 문자열
# s1 = "버섯스프"
# s2 = "발로란트"

# print(s1+' '+s2)    #문자열 덧셈 : 병합
# # print(s1 + 2)  #문자열 + 숫자 : 오류, 서로 다른 자료형끼리 더하기 연산 안됨
# # print(s1-s2)    #문자열 뺄셈 : 오류, 불가능
# print(s1*3)     #문자열 곱셈 : 반복
# # print(s1/2) #문자열 나눗셈 : 오류, 불가능


### 인덱스(index): 순서가 있는 자료형의 위치값
# text = "Hello, world!"
# print(text[0])

s1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
s2 = "abcdefghijklmnopqrstuvwxyz"

name = s1[9]+s2[0]+s2[10]+s2[4]
print(name)