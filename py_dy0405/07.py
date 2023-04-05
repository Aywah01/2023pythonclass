# [7] randrange()와 set()를 이용하여 중복없는 로또번호 만들기
# 또 다른 방법 sample() 함수를 이용하면 매우 간편하다.(실습하기)

# #randrange() 함수와 집합을 이용, 중복을 제거
# mylotto = set()
# ==========================================
# 2 12 14 7 1 1 9 
# 집합: {1, 2, 7, 9, 12, 14}
# 정렬리스트: [1, 2, 7, 9, 12, 14]

# sample로 번호리스트 만들기
# sample 함수 리스트: [27, 20, 8, 32, 28, 14]
# sample 함수 정렬리스트: [8, 14, 20, 27, 28, 32]

from random import randrange
from random import sample

mylotto = set()
while True:
    num = randrange(1,100)
    print(num, end=' ')
    mylotto.add(num)
    if len(mylotto) == 6:
        break

print('\n집합: {}'.format(mylotto))
print('\n정렬리스트: {}'.format(sorted(mylotto)))

print('\nsample로 번호리스트 만들기 ')
lotto = sample (range(1,46), 6)
print('\nsample 함수 리스트: {}'.format(mylotto))
print('\nsample 함수 정렬리스트: {}'.format(sorted(mylotto)))