import csv
import requests
from bs4 import BeautifulSoup

# res = requests.get("https://naver.com/")
# print(res.text)

# url = 'https://finance.naver.com'
# res = requests.get(url)
# res.raise_for_status()
# soup = BeautifulSoup(res.text, "lxml")

# data_rows = soup.find("div", attrs={"class" :"section_strategy"}).find("ul").find_all("span")

# for row in data_rows:
#     columns = row.find("a")
#     data = [column.get_text().strip() for column in columns]
#     print(data)

# for year in range(2020, 2023):
#     url = "https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(year)
#     res = requests.get(url)
#     res.raise_for_status()
#     soup = BeautifulSoup(res.text, "lxml")

#     images = soup.find_all("img", attrs={"class":"thumb_img"})
#     for idx, image in enumerate(images):
#         print(image["src"])
#         image_url = image["src"]
#         if image_url.startswith("//"):
#             image_url = "https:" + image_url
        
#         print(image_url)
#         image_res = requests.get(image_url)
#         image_res.raise_for_status()

#         with open("movie_{}_{}.jpg".format(year, idx+1), "wb") as f:
#             f.write(image_res.content)
#             if idx >= 4:
#                 break

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

filename = "시가총액1-200.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)

title = "순위 연속  누적  종목명 현재가 전일비  등락률    거래량 시가  고가  저가".split("\t")
writer.writerow(title)

for page in range(1,3):
    res = requests.get(url + str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
        
    data_rows  = soup.find("table", attrs={"class": "type_2"}).find_all("tr")

    for row in data_rows:
        i = 1
        columns = row.find_all("td")
        if len(columns) <= 1:
            continue
        data = [column.get_text().strip() for column in columns]
        writer.writerow(data)

