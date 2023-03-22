# [3] 파이썬 표준모듈 random을 불러 randrange() 함수를 이용하여 다음 코드를 작성해 보자
# 4명이서 여행을 떠나려는데, 둘은 하와이를 가자고 하고, 나머지는 다른 곳을 가자고 한다.
# 무작위 수를 만들어 0이 나오면 제주도, 1이 나오면 사이판, 2와 3이 나오면 하와이를 가기로 했다. 이러한 일을 처리할 수 있는 코드를 만들어보자.
import random

print("여행 갈까? : ")
vote = int (random.randrange(0,4))
if (vote == 0) :
    print('제주도로 출발')
elif (vote == 1) :
    print('사이판으로 출발')
else: 
    print('하와이로 출발')