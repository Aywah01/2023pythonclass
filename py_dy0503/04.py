# (4)  모두 다른 값을 가진 주어진 리스트의 최소값(min())을 구하고 그 값을 삭제하는 과정을 k 번 하는 코드를 완성하시오(k가 3이면 (3 th value 20)를 출력한다)

k = 3
exlist = [20, 10, 7, 30, 35, 70, 35]
for d in range(k):
    mvalue = min(exlist)
    di = exlist.index(mvalue)  # 최소값의 인덱스를 구하는 리스트 함수 index사용
    del(exlist[di])
print(k, 'th value', mvalue)