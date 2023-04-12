# [9] 유효 암호 검사
# 암호를 만들 때 소문자, 대문자, 숫자, 특수문자 중 3개 이상을 조합하여 만들어야 한다면 이 규칙에 맞는 유효한 암호인지 검사하는 코드를 작성해 보시오

# 암호 입력: hsrhee1004
# !!불가능한 암호!!

# 암호 입력: 1004hsrhee!!
# 사용 가능

upp, low, dig, pct = 0, 0, 0, 0
pswd = input('Input Password: ')

if pswd.isalnum() == False:
    pct = 1
for k in pswd:
    if k.isupper():
        upp = 1 # 대문자 있으면 upp = 1
    elif k.islower(): 
        low = 1 # 소문자 있으면 low = 1
    elif k.isdigit():
        dig = 1 # 숫자 있으면 dig = 1

if (low + upp + dig + pct >= 3) :
    print('사용 가능')
else : 
    print('!!불가능한 암호!!')