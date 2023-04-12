#[3] 다음의 두 리스트를 zip()함수를 이용하여 출력하여 출력한 내용을 확인하시오

menulist = ['기본햄버거', '치즈햄버거', '불고기버거', '와퍼킹버거']
pricelist = [4000, 4500, 5000, 7000]
tlist = list(zip(menulist, pricelist))
dlist = dict(zip(menulist, pricelist))
print(tlist)
print(dlist)