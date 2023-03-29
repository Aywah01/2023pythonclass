n=int(input("몇개의 데이터 처리 : "))
listex = [0]*n

print('%d개의 데이터 입력 : ' % n)
for k in range(n):
    listex.append(int(input())) 
    # sum += listex[k]
    
# print('리스트 데이터의 합과 평균  : %d %.2f\n' % (sum, sum/n))
# print('리스트 데이터의 최대값 최소값 : %d %d\n' % (max,min))
print('%d %d %d %d' %(sum(listex), sum(listex)/n, max(listex), min(listex)))