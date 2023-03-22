# [4] random.randrange() 함수를 사용하여 컴퓨터가 가위, 바위, 보 중 하나를 선택 한다. 
# 가위는 0, 바위는 1, 보는 2로 정한다. 따라서 컴퓨터는 0, 1, 2 중 하나의 값을 가지게 된다. 
# 사용자로부터 가위0 바위1 보2 중 하나를 입력 받아 컴퓨터와 대결하는 코드를 만들어보자.

import random
com= random.randrange(3)
user= int(input('가위0 바위1 보2 선택: '))
print('user= %d, com= %d' % (user, com))

if(user == com) : 
    print('비겼습니다')
elif(user == 0 and com == 2) or (user == 1 and com == 0 ) or (user == 2 and com == 1) :
    print('user 승!')
else : 
    print('com 승!')