# [람다함수 작성연습 예제] 3개 카드의 1월부터 5월까지의 지출금액의 합을 구하는 람다함수 ctotal을 만들어 보시오
cpay1=[23900, 65000, 78000, 20100, 600]
cpay2=[123450, 25610, 658990, 25000, 678500]
cpay3=[25670, 4520, 3300, 29000, 1000]

ctotal = list(map(lambda a, b, c : a+b+c, cpay1 , cpay2 , cpay3))                                                        

print(ctotal)
for k in range(5):
    print(k+1, '월 지출', ctotal[k], '원')