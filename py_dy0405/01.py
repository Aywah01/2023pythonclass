# 1) 0에서 99까지의 random number를 20개 list에 만든다
#  .sort()를 이용하여 오름차순으로 정렬한 후 k번째 데이터 출력
# 2) 0에서 50까지의 데이터를 (중복없이)20개를 만든다 
#        min()으로 최소값을 k번 구하고 마지막 값을 출력

from random import randrange

exlist = []
for k in range(20) :
    exlist.append(randrange(0,100))

k = int(input("몇번째 데이터를 원하시나요?"))
print(exlist)
exlist.sort()
print(exlist)
print(k, 'th data = ', exlist[k-1])

count = 1
exlist2 = []
while count < 20:
    num = randrange(0,51)
    if num not in exlist2:
        exlist2.append(num)
        count += 1

print(exlist2)
exlist2.sort()
print(exlist2)

for d in range(k):
    mvalue = min(exlist2)
    di = exlist2.index(mvalue)
    del(exlist2[di])

print(k, 'th data', mvalue)
