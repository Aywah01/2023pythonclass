# 다중반복문의 대표적인 예인 다음 구구단이 출력되도록 코드를 작성하시오

for dan in range(2, 10) :
    print('\n%d단: ' % dan , end = '')
    for num in range(1, 10) :
        print('%dx%d = %d' % (dan, num, dan * num), end = ' ')