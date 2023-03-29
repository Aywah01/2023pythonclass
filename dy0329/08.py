import random as r
import time as t

num = int(input('슬롯머신을 몇 번 들릴까요?'))
slot = [0]*3
for k in range(num):
    for k in range(3) :
        slot[k] = r.randrange(7,10)# 무작위 수 7, 8, 9 생성
        print('%d ' % slot[k], end = '')
        t.sleep(1)
    if slot[0] + slot[1] + slot[2] == 21 :
        print('\n잭팟이 터젔네요\n')
    else:
        print('\n아까워\n')
