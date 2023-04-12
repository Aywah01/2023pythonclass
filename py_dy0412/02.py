#[2] 1부터 99까지 중 5의 배수로만 이루어진 리스트를 만드는 한 줄 컴프리헨션 문장을 쓰시오

numList = [num for num in range(1, 100) if num % 5 == 0]
print(numList)
print(dir(numList))