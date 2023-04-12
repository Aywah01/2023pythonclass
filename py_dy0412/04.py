#[4] 얕은 리스트 복사와 깊은 리스트 복사의 예를 들어 차이점을 설명하시오.

oldList= ["짜장면","탕수육","군만두"]
newList = oldList
print(newList)
oldList[0] = '짬뽕'
oldList.append('깐풍기')
print(newList)

oldList= ["짜장면","탕수육","군만두"]
newList = oldList[:]
print(newList)
oldList[0] = '짬뽕'
oldList.append('깐풍기')
print(newList)