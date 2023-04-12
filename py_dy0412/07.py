# [7] 다음과 같이 문자열의 각 문자를 하나씩 회전시켜 제자리로 오도록 하는 코드를 작성하시오
# 문자열의 인덱스에 주의하며 코딩하고 실행하고 확인해 보시오

import time as t

st1 = input("문자열 입력: ")

for k in range(len(st1) + 1) :
    for m in range(len(st1)) :
        print(' ', st1[ (k + m) % len(st1)], end='' ) # 한 글자씩 회전
    t.sleep(0.2)
    print('---')