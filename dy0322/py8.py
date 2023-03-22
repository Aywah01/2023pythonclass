# [9] [8]의 구구단을 break를 사용하여 다음과 같이 출력되도록 수정하시오

for dan in range(2, 10) :
    print('\n%d단: ' % dan , end = '')
    for num in range(1, 10) :
        if (num == 5) :
            break
        print('%dx%d = %d' % (dan, num, dan * num), end = ' ')
