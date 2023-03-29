suNo, quizNo = map(int, input().split())
numbers = list(map(int, input().split()))
pSum = [0]
temp = 0
slist = []

for i in numbers:
    temp += i
    pSum.append(temp)

# print(pSum)

for i in range(quizNo):
    s, e = map(int, input().split())
    slist.append(pSum[e] - pSum[s-1])

for i in range(quizNo):
    print(slist[i])

