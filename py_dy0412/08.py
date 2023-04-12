#[8] 문자열 처리함수 split()와 

ss = input("날짜(연/월/일) 입력 ==> ")
ssList = ss.split('/')
print("입력한 날짜의 10년 후 ==> ", end = '')
print(str(int(ssList[0]) + 10) + "년", end = '')
print(ssList[1] + "월", end = '')
print(ssList[2] + "일")

# join()을 활용한 예를 테스트해보고 적으시오

seasons = ','.join(['spring','summer','fall','winter'])
print(seasons)

num = ' - '. join('010.7560.6191'.split('.'))
print(num)
