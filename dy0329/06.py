import random

oddlist = list(range(1, 101, 2))
print(oddlist)

sum = 0
for k in range(50):
    sum += oddlist[k]
print(sum)