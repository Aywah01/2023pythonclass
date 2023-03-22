# [6] 1부터 n까지의 짝수의 합을 구하는 코드를 while문과 for문으로 작성하시오
# print("===1부터 n까지의 짝수의 합 구하기 =")

import random

sum = 0
num = int(input("짝수 하나를 입력하세요>>"))
i = 0
for i  in range (0, num) : 
    i += 1
    if i % 2 == 0 :
        sum += i

print("1부터 n까지의 짝수의 합 구하기 = %d" % sum)

