# [6] 0부터 12개월후의 토끼의 수를 출력하는 1,1로 시작하는 피보나치수열 13개를 출력하는 재귀함수를 작성하시오(피보나치수열의 점화식 이해)

def fibo(n):
    if n < 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

for k in range(13):
    print('%d개월 후 토끼의 수 = %d' % (k, fibo(k)))