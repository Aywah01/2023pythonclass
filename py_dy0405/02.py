# [2] 다음 코드로 만들어져서 출력되는 2차원 리스트를 쓰시오

list1 = []
list2 = []
value = 0

for i  in range(0,3):
    for k in range(0,4):
        list1.append(value)
        value += 5
    list2.append(list1)
    list1 = []

print("row(i) x column(k)")
for i in range(0,3):
    for k in range(0,4):
        print("%d" % list2[i][k], end=" ")
    print("")
print("----------------------")
print("row(k) x column(i)")
# transpose

for k in range(0,4):
    for i in range(0,3):
        print("%d" % list2[i][k], end=" ")
    print("")