# [1] 다음 코드는 3항조건 연산자의 예이다
# choice== 1을 choice로만 하려면 어떻게 변경해야하나?
# choice= int(input('만날까? 말까? (1/0) 입력 :'))
# print('오늘부터 1일\n') if choice else print('다음 기회에~~\n‘)
                                        
print('D반 화이팅-- 3주차 수업시작')
choice = int(input('만날까? 말까? (1/0) 입력?'))
print('오늘부터 1일\n' if choice else print('다음 기회에~~\n'))
