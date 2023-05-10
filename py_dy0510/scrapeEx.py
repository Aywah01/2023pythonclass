import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://www.weather.go.kr/w/index.do"
# Chrome브라우저 및 get요청
browser = webdriver.Chrome()
browser.implicitly_wait(15) # 최대 (원하는)초 동안 대기
browser.get(url)
time.sleep(15)

#지역
area = browser.find_element(
    By.CSS_SELECTOR, 'a.serch-area-btn.accordionsecond-tit').text
#체감온도
actualTemp = browser.find_element(By.CLASS_NAME, 'chill').text
#습도
humidity_str = browser.find_element(By.CSS_SELECTOR, '#current-weather > '
                                    'div.cmp-cur-weather.wbg.wbg-type2.BGDB00 > '
                                    'ul.wrap-2.no-underline > li:nth-child(1) >'
                                    ' span.val').text
#바람
wind_str = browser.find_element(By.CSS_SELECTOR,'#current-weather > div.cmp-cur-weather.wbg.wbg-type2.BGDB00 > ul.wrap-2.no-underline > li:nth-child(2) > span.val').text

#replace
wind_replace= float(wind_str.replace("북동","").replace("m/s", ""))
#split
wind_num = float(wind_str.split()[1])

#온도
temp = browser.find_element(By.CSS_SELECTOR,'#current-weather > div.cmp-cur-weather.wbg.wbg-type2.BGDB00 > ul.wrap-1 > li.w-icon.w-temp.no-w > span.tmp').text

#replace
temp_replace = float(temp.replace("℃",""))
#split
temp_split = float(temp.split('℃')[0])

print("Wind")
print("==========================")
print(wind_str)
print(f"선택지역: {area}")
print(f"체감온도: {actualTemp}")
print(f"습도: {humidity_str}")
print(f"바람: {wind_str}")
print("==========================")
print("Temperature")
print(temp)
print(f"현재온도: {temp}")
print(f"조작한데이터: {temp_replace}")

if wind_num < 0.3:
        print("이정도면 바람이 안부네요!")

if temp_replace > temp_replace-1:
        print("오늘 날씨가 더워요!")

exitinput = input("Press any key to close: ")
browser.close
