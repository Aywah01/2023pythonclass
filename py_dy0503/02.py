for dan in range(2, 10):
    # 3항조건 연산자를 이용하여 짝수단 만 출력
    if(dan % 2 == 0):
        print('\n%d단 :' % dan, end='') 
    else: print('')
    for num in range(1, 10):
        if num == 1 or num == 2: # num 1과 9는 출력 제외
            continue
        if dan % 2 == 0 :
            print('%2d x%2d =%3d ' % (dan, num, dan*num), end='')
        else:
            break
