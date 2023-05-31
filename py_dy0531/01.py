import requests    # requests라는 외부 라이브러리는 서버에 데이터를 전송할떄 사용한다.
from bs4 import BeautifulSoup
api_url = "https://notify-api.line.me/api/notify"
token = "fe1XS5wPKk9WTpxWYg5EdyvrveBkfOJvniX9AZfsL5w"
headers = {'Authorization':'Bearer '+token}
headArr = ''
url = "https://finance.naver.com/"
filename = "증권뉴스.csv"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

data_rows = soup.find("div", attrs={"class" : "section_strategy"}).find("ul").find_all("span")

for row in data_rows:
    columns = row.find("a")
    
    data = [column.get_text().strip() for column in columns]
    data2 = columns = row.find("a")['href']
    print(data)
    datastr ="\n".join(data)
    datastr2 =( data2)
    headArr = headArr + "\n" + datastr + "\n링크 ({})".format(datastr2)
    #print(headArr)
    #print(datastr)
message = {
"message" : headArr }
#print(datastr)
requests.post(api_url, headers= headers , data = message)

