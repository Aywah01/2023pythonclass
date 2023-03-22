# [5] 가위바위보 문제를 반복하여 실행하도록 while문으로 작성한다.
# 0~2의 값이 아닌 경우를 입력한 경우 가위바위보를 한 횟수(gnum)을 출력하고
# break문으로 while문을 나가고 종료하도록 프로그램 하시오  YES

import random

gnum = 0

while(True) : 
    com= random.randrange(3)
    user= int(input('가위0 바위1 보2 선택: '))

    if(user == 0 or user == 1 or user == 2) :
        print('user= %d, com= %d' % (user, com))
        gnum += 1
        if(user == com) : 
            print('비겼습니다')
        elif(user == 0 and com == 2) or (user == 1 and com == 0 ) or (user == 2 and com == 1) :
            print('user 승!')
        else : 
            print('com 승!')
    else : 
        print('== End of Game ==')
        print('가위바위보 %d 회 했습니다 ' % gnum)
        break
