import random

print("여행 갈까? : ")
vote = int (random.randrange(0,4))
if (vote == 0) :
    print('제주도로 출발')
elif (vote == 1) :
    print('사이판으로 출발')
else: 
    print('하와이로 출발')