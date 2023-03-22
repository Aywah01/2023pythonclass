# [7] 파이썬에 내장되어 있는 함수 eval()과 range()를 활용하여 다음 select 값에 따라
# 2가지 계산기 기능을 수행하는 코드를 작성하시오
# select = int(input("1. 입력한 수식 계산  2. 두 수 사이의 합계 : "))

select = int(input("1. 입력한 수식 계산  2. 두 수 사이의 합계 : "))

if select == 1 :
    nexp = input(" *** 수식을 입력하세요>> ")
    answer = eval(nexp)
    print(" %s 결과는 %5.1f입니다. " %(nexp,answer))
elif select == 2 :
    num1 = int(input(" *** 첫 번째 숫자를  입력하세요>> "))
    num2 = int(input(" *** 두 번째 숫자를  입력하세요>> "))
    answer = 0

    for i in range (num1 , num2 + 1) :
        answer += i
    print("%d+...+%d는 %d입니다. " %(num1, num2, answer))
    
else:
    print("1 또는 2만 입력해야 합니다. ")

