# [3] 다음을 실행하면서 함수와 람다함수의 개념을 익히시오

# add = lambda a,b : a + b

from random import randrange

hap = lambda n1 = 10, n2 = 70, n3 = 50 : n1+n2+n3
print(hap())
print(hap(10, 20))

exList = [10, 20, 30, 40 ,50]
exList2 = exList*2
print(exList2)

def multiplyn(data, n) :
    return data * n #[data * 4] -> [40, 80, 120, 160, 200]

m = randrange(2, 6)
print('m =',m)
for k in range(len(exList)):
    exList[k] = multiplyn(exList[k], m)
print(exList) #[40, 80, 120, 160, 200]

# for문 사용하지 않고 함수 multiplyn 사용
m = randrange(2, 6)
print('m =',m)
mlist = [m]*len(exList)
exList = list(map(multiplyn, exList, mlist))                           
print(exList)

# for문 사용하지 않고 람다함수 사용
testf = lambda data, n = m: data * n                             
exList = list(map(testf, exList))
print(exList)
