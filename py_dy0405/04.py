# [4] 튜플 사용 예 :  

# 1) menu와 price의 두 가지 튜플을 만든다
# menu = ('기본햄버거', '치즈햄버거', '불고기버거', '와퍼킹버거')
# price = (4000, 4500, 5000, 7000)

# 2) 다음과 같이 출력하는 코드를 작성한다

# 1 : 기본햄버거 : 4000
# 2 : 치즈햄버거 : 4500
# 3 : 불고기버거 : 5000
# 4 : 와퍼킹버거 : 7000

# 3) 새우버거 5500원을 추가하고(변경이 있다면 리스트로 변경해야한다) 다음과 같이 출력하는 코드를 작성한다

# 메뉴: ('기본햄버거', '치즈햄버거', '불고기버거', '와퍼킹버거', '새우버거')
# 가격: (4000, 4500, 5000, 7000, 5500)

menu = ('기본햄버거', '치즈햄버거', '불고기버거', '와퍼킹버거')
price = (4000, 4500, 5000, 7000)

print('No :     Menu     :  Price')
print('----------------------------')
for i in range(len(menu)):
    print(i," : " ,menu[i], " : ", price[i])
print('----------------------------')

menuList = list(menu)
priceList = list(price)
menuList.append('새우버거')
priceList.append(5500)

menu = tuple(menuList)
price = tuple(priceList)
print("메뉴: ",menu)
print("가격: ",priceList)