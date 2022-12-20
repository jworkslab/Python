### review
'''
[] : 인덱스, 리스트
() : 함수, 튜플
{} : 포맷팅, 딕셔너리
'''
### 딕셔너리 함수(메소드)
# score = {'MA':100, 'EN':80, 'SC':70, 'PE':90}
# print(score, type(score))

# print(score.keys(), type(score.keys()))
# print(score.values(), type(score.values()))
# print(score.items(), type(score.items()))

# print(score.get('EN'))
# print(score.get('SS'))

# # score['HS'] = 90
# # score['SC'] = 100
# score.update({'HS':90, 'SC':100})
# print(score)

# # score.clear()
# # print(score)

# # del(score['SC'])    #원하는 key의 value 삭제
# del score['SC']
# print(score)

# score.pop('HS')
# print(score)

### 활용
my_fam = ('GF', 'GM', 'Fa', 'Ma', 'Me')
# info_fam = ['name', 'birth', 'job', 'hobby', 'food']
# family = {my_fam[0]:info_fam}

info_Me = ['박채정', '081109', '학생', '게임', '도너츠']
family = {my_fam[4]:info_Me}

print(family)