# [6] 문자열 거꾸로 출력하기 코드를 작성하여 확인하시오(함수가 있지만 인덱스 활용하여 작성)

# 문자열을 입력하세요 : 행복한 오늘
# 내용을 거꾸로 출력 --> 늘오 한복행

outStr = ""
inStr = input("문자열을 입력하세요 : ")
count = len(inStr)
for k in range(0, count) :
    outStr += inStr[count - (k + 1)]
print("내용을 거꾸로 출력 --> %s" % outStr)